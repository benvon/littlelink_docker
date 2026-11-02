# Project instructions

This public repository contains Ben Vaughan's static LittleLink page and its container build. Keep exactly the six personalized destinations and existing Plausible analytics. Preserve local fonts, accessible markup, automatic light/dark themes, and upstream license/provenance notices.

Use mise shims and run `mise run verify` after serving-asset or container changes. Docker must remain compatible with UID/GID 5000, port 8080, a read-only root, dropped capabilities, and writable `/tmp`. Copy only public static assets into the image. Run `actionlint` after workflow changes; pin actions and the base image to immutable revisions. PR jobs must remain read-only; only pushes to main publish/sign the exact digest with a full source SHA tag.

Do not add private deployment details or credentials. Legacy Kubernetes ownership is outside normal site work; do not alter `kubernetes/tunnel/`, namespace, or ingress files. Production deployment and image promotion are managed separately. Preserve user work and use signed Conventional Commits.
