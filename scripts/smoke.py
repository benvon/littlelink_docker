#!/usr/bin/env python3
"""Build-independent Docker smoke test: python3 scripts/smoke.py IMAGE."""
import json
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from verify import ROOT, verify


def docker(*args):
    return subprocess.check_output(['docker', *args], text=True).strip()


def smoke(image):
    expected = verify()
    config = json.loads(docker('image', 'inspect', image))[0]['Config']
    assert config['User'] == '5000:5000', 'Image must default to UID/GID 5000'
    container = docker('run', '--detach', '--read-only', '--cap-drop=ALL',
                       '--security-opt=no-new-privileges', '--user=5000:5000',
                       '--tmpfs=/tmp:rw,noexec,nosuid,size=32m,mode=1777',
                       '--publish=127.0.0.1::8080', image)
    try:
        port = json.loads(docker('inspect', container))[0]['NetworkSettings']['Ports']['8080/tcp'][0]['HostPort']
        base = f'http://127.0.0.1:{port}'
        for attempt in range(50):
            try:
                with urlopen(base, timeout=2) as response:
                    assert response.status == 200
                    assert response.read() == (ROOT / 'index.html').read_bytes(), 'Unexpected root page'
                break
            except (URLError, ConnectionError):
                time.sleep(0.1)
        else:
            raise AssertionError('Container did not become ready')
        assert docker('exec', container, 'id', '-u') == '5000', 'Wrong runtime UID'
        assert docker('exec', container, 'id', '-g') == '5000', 'Wrong runtime GID'
        status = docker('exec', container, 'cat', '/proc/1/status')
        assert 'Uid:\t5000\t5000\t5000\t5000' in status, 'NGINX must run as UID 5000'
        expected_files = {'index.html'} | {p.relative_to(ROOT).as_posix() for name in ['css', 'fonts', 'images'] for p in (ROOT / name).rglob('*') if p.is_file()}
        actual_files = set(docker('exec', container, 'find', '/usr/share/nginx/html', '-type', 'f').splitlines())
        assert actual_files == {'/usr/share/nginx/html/' + p for p in expected_files}, 'Unexpected serving files in image'
        # Check content, not just status: a fallback/welcome page must not pass.
        for path in {'index.html', *expected}:
            with urlopen(f'{base}/{path}', timeout=5) as response:
                assert response.status == 200, path
                assert response.read() == (ROOT / path).read_bytes(), f'Unexpected content: {path}'
        excluded = ['.git/config', '.github/workflows/docker-publish.yml', 'Dockerfile',
                    'README.md', 'AGENTS.md', 'mise.toml', 'docker-compose.yml',
                    'scripts/verify.py', 'docs/upstream.md', '50x.html',
                    'kubernetes/10-deployment.yaml', 'not-a-real-page']
        for path in excluded:
            try:
                urlopen(f'{base}/{path}', timeout=5)
            except HTTPError as error:
                assert error.code == 404, f'{path}: {error.code}'
            else:
                raise AssertionError(f'Excluded path served: {path}')
        print(f'PASS: UID/GID 5000, read-only root, {len(expected) + 1} matching files, {len(excluded)} excluded paths')
    except Exception:
        print(docker('logs', container), file=sys.stderr)
        raise
    finally:
        docker('rm', '--force', container)


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1].startswith('-'):
        sys.exit('Usage: python3 scripts/smoke.py IMAGE')
    smoke(sys.argv[1])
