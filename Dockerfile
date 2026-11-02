FROM ghcr.io/nginx/nginx-unprivileged:1.31.8-alpine-slim@sha256:633f37ad70b9fd48d4da573db1ebc9111a9ad174e5178e83bd2ef45381fde5e2
USER root
# Remove the stock index and error page before copying the public asset allowlist.
RUN rm -rf /usr/share/nginx/html/*
COPY LICENSE.md /licenses/littlelink-MIT.txt
COPY index.html /usr/share/nginx/html/index.html
COPY css/ /usr/share/nginx/html/css/
COPY fonts/ /usr/share/nginx/html/fonts/
COPY images/ /usr/share/nginx/html/images/
USER 5000:5000
EXPOSE 8080
