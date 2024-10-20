FROM ghcr.io/nginxinc/nginx-unprivileged:1-bookworm
COPY css /usr/share/nginx/html/
COPY images /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/
USER 5000