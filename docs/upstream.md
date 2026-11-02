# Upstream sources

Reviewed 2026-11-02.

- Canonical framework: [sethcottle/littlelink v3.11.0](https://github.com/sethcottle/littlelink/tree/3c9162c9f8324d5e002259ed8b4b3cc377b08486), revision `3c9162c9f8324d5e002259ed8b4b3cc377b08486`.
- `css/reset.css`, `css/style.css`, `css/brands.css`, all four `fonts/*.woff2`, and the five used SVG icons (`github`, `mastodon`, `linkedin`, `generic-email`, `generic-website`) are copied unchanged from that revision. Personalized HTML adapts the canonical theme-auto, main/nav/button-stack, and decorative-icon patterns. Credly and Website use the default button style. Existing personal images and unused historical icons remain.
- Retain [LICENSE.md](../LICENSE.md), the upstream MIT license and copyright notice. Local Open Sans font files are distributed with the canonical source; the Open Sans project’s [SIL Open Font License](https://github.com/googlefonts/opensans/blob/main/OFL.txt) is retained in `fonts/OFL.txt`. The image includes the MIT notice under `/licenses/` and the font license alongside the fonts.
- Intermediate fork reviewed at [davisdre/littlelink revision 04afcabb820a5022daf5af074bc3aa281d5183c3](https://github.com/davisdre/littlelink/tree/04afcabb820a5022daf5af074bc3aa281d5183c3). It moved to standard NGINX, broad `COPY .`, and Docker Hub workflows including PR publishing. Those choices do not satisfy this project's non-root, asset allowlist, or PR permission requirements, so they were not imported.
- Container base: [NGINX unprivileged](https://github.com/nginx/docker-nginx-unprivileged), `ghcr.io/nginx/nginx-unprivileged:1.31.8-alpine-slim@sha256:633f37ad70b9fd48d4da573db1ebc9111a9ad174e5178e83bd2ef45381fde5e2`. The manifest supports linux/amd64 and linux/arm64. It keeps HTTP on port 8080, PID/temp paths under `/tmp`, and is run here as UID/GID 5000.

Actions are pinned to official release commits, with release versions alongside each pin. Dependency changes require a reviewed PR and repeat verification. Upstream examples, additional analytics, deployment credentials, and unrelated container/workflow choices are not imported.
