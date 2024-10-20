FROM ghcr.io/nginxinc/nginx-unprivileged:1-bookworm
COPY . /usr/share/nginx/html/
USER 5000