#!/usr/bin/env python3
"""Validate the public page and its complete local asset dependency graph."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DESTINATIONS = [
    'https://github.com/benvon', 'https://vaughan.social/@benvon',
    'https://www.linkedin.com/in/benvon/', 'mailto:ben@benvon.net',
    'https://www.credly.com/users/ben-vaughan.b1571c06', 'https://www.benvon.net/',
]
ALLOWED = {'css': {'.css'}, 'fonts': {'.woff2'}, 'images': {'.png', '.svg'}}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.assets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag in {'img', 'script'} and attrs.get('src'):
            self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') in {'stylesheet', 'icon', 'preload'}:
            self.assets.append(attrs['href'])
        if attrs.get('srcset'):
            self.assets.extend(item.strip().split()[0] for item in attrs['srcset'].split(','))


def assets(root=ROOT):
    """Return every HTML/CSS asset; reject remote, missing or unsafe dependencies."""
    page = Page()
    page.feed((root / 'index.html').read_text())
    pending = [(root, url) for url in page.assets]
    found = set()
    while pending:
        parent, url = pending.pop()
        if url == 'https://plausible.io/js/plausible.js':
            continue
        parts = urlsplit(url)
        assert not parts.scheme and not parts.netloc, f'Unexpected remote asset: {url}'
        path = parent / unquote(parts.path).lstrip('/')
        path = path.resolve()
        assert path.is_relative_to(root.resolve()), f'Asset outside public root: {url}'
        assert path.is_file(), f'Missing asset: {url}'
        rel = path.relative_to(root.resolve()).as_posix()
        assert rel.split('/')[0] in ALLOWED, f'Unsafe asset: {rel}'
        if rel in found:
            continue
        found.add(rel)
        if path.suffix == '.css':
            css = path.read_text()
            assert not re.search(r'@import\b', css), f'CSS imports are unsupported: {rel}'
            pending.extend((path.parent, value) for value in re.findall(r'url\(\s*[\"\']?([^\)\"\']+)', css))
    return page, found


def verify(root=ROOT):
    page, found = assets(root)
    elements = page.elements
    select = lambda tag: [a for t, a in elements if t == tag]
    assert [a.get('href') for a in select('a')] == DESTINATIONS, 'Keep exactly the six personal destinations, in order'
    assert any('theme-auto' in a.get('class', '').split() for a in select('html')), 'Missing theme-auto'
    assert len(select('main')) == 1, 'Use one semantic main element'
    assert any(a.get('aria-label') and 'button-stack' in a.get('class', '').split() for a in select('nav')), 'Use labeled link navigation'
    assert {'css/reset.css', 'css/style.css', 'css/brands.css'} <= found, 'Missing canonical CSS'
    assert any(p.startswith('fonts/') for p in found), 'Use local fonts'
    assert any(a.get('class', '').startswith('avatar') and a.get('width') and a.get('height') and a.get('alt') for a in select('img')), 'Avatar needs dimensions and alt text'
    for a in select('a'):
        if a.get('target') == '_blank':
            assert 'noopener' in a.get('rel', '').split(), 'External tabs need noopener'
    for img in select('img'):
        if 'icon' in img.get('class', '').split():
            assert img.get('aria-hidden') == 'true' and img.get('alt') == '', 'Decorative icons must not repeat link labels'
    scripts = select('script')
    assert len(scripts) == 1 and scripts[0].get('src') == 'https://plausible.io/js/plausible.js' and scripts[0].get('data-domain') == 'benvon.net' and 'defer' in scripts[0], 'Preserve only the existing Plausible script'
    for directory, suffixes in ALLOWED.items():
        assert (root / directory).is_dir(), f'Missing serving directory: {directory}'
        for path in (root / directory).rglob('*'):
            assert not path.is_symlink(), f'Symlink in serving files: {path.relative_to(root)}'
            if path.is_file():
                assert (path.suffix in suffixes or path.relative_to(root).as_posix() == 'fonts/OFL.txt') and not any(p.startswith('.') for p in path.relative_to(root).parts), f'Unsafe serving file: {path.relative_to(root)}'
    print(f'PASS: six destinations, semantics, analytics, and {len(found)} local assets (including CSS URLs)')
    return found


if __name__ == '__main__':
    verify()
