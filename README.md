# Ben's links

A personalized [LittleLink](https://github.com/sethcottle/littlelink) page, served by an unprivileged NGINX container. Source and asset provenance are recorded in [docs/upstream.md](docs/upstream.md).

## Edit and verify

Edit `index.html` for the six links, name, bio, and existing Plausible settings. CSS and fonts are local. No application framework or package manager is required.

Install [mise](https://mise.jdx.dev/) and Docker, then run:

```sh
mise install
mise run verify
```

This entry point validates exact destinations, accessible page structure, analytics, local asset closure (including CSS fonts), and safe serving files. It builds `links:local` and smoke tests it as UID/GID 5000 with a read-only root, dropped capabilities, no privilege escalation, and temporary `/tmp` storage. Every referenced asset must match its source bytes; repository files and stock NGINX pages must return 404. The Python scripts use only the standard library and also run directly with Python 3.11+.

For a browser preview after verification:

```sh
docker run --rm --read-only --cap-drop=ALL --security-opt=no-new-privileges \
  --user=5000:5000 --tmpfs=/tmp:rw,noexec,nosuid,size=32m,mode=1777 \
  -p 127.0.0.1:8080:8080 links:local
```

Open [localhost:8080](http://localhost:8080) and check mobile, light, dark, keyboard focus, and link labels. Stop with Ctrl-C. The origin serves the original mailto link; edge email handling is a separate production check.

## Releases

Pull requests validate, build, and smoke test without registry or signing write permissions. Only a push to `main` that passes validation publishes `ghcr.io/benvon/littlelink_docker:sha-<full-source-sha>` for amd64 and arm64. CI signs the exact manifest digest with Sigstore and reports it in the workflow summary. Weekly Dependabot PRs propose base-image and action updates; there are no scheduled publications or automatic deployments.

Use the immutable digest for deployment. For example, replace the digest placeholder in:

```sh
cosign verify ghcr.io/benvon/littlelink_docker@sha256:<digest> \
  --certificate-identity=https://github.com/benvon/littlelink_docker/.github/workflows/docker-publish.yml@refs/heads/main \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com
```

Production deployment and image promotion are managed separately from this public source repository. The superseded app Deployment, Service, and HPA manifests have been retired. Remaining tunnel, namespace, and ingress files have separate ownership; do not apply, move, or clean them up as part of site maintenance.

## Additional checks

Run `actionlint` for workflow changes and `gitleaks dir --redact <export-directory>` on an export of tracked and proposed files for a secret scan (exclude ignored local credentials). Review upstream changes and image vulnerability results when updating dependencies. Never add credentials to this public repository.
