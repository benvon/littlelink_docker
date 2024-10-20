#!/usr/bin/env bash
NAMESPACE=links
helm repo add cloudflare https://cloudflare.github.io/helm-charts
helm repo update
helm upgrade --install --namespace ${NAMESPACE} --create-namespace ${NAMESPACE}tunnel cloudflare/cloudflare-tunnel-remote -f ./values.yaml
