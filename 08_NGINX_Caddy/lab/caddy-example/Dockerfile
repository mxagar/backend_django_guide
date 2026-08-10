# Shared base: built once, reused by both stages below so the apt-get
# layer and the student user are not duplicated across the two images.
# Mirrors lab/nginx-security-load-balancing-optimization/Dockerfile.
FROM ubuntu:24.04 AS base

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends sudo \
    && rm -rf /var/lib/apt/lists/*

RUN useradd \
        --create-home \
        --shell /bin/bash \
        student \
    && usermod --append --groups sudo student \
    && echo "student ALL=(ALL) NOPASSWD:ALL" \
        > /etc/sudoers.d/student \
    && chmod 0440 /etc/sudoers.d/student

# ---- backend-node -----------------------------------------------------
# Identical to the NGINX lab's backend stage -- same two FastAPI
# backends, unchanged, so the two labs are directly comparable.
FROM base AS backend-node

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Ubuntu 24.04 blocks plain `pip install` outside a venv (PEP 668);
# --break-system-packages is fine for a throwaway lab container.
RUN pip install --no-cache-dir --break-system-packages "fastapi[standard]"

USER student
WORKDIR /home/student/backend_app

EXPOSE 3000

# main.py is provided by the bind mount in compose.yaml, not the image.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]

# ---- caddy-node ---------------------------------------------------------
# Installs Caddy via its official apt repository -- the same commands
# you'd run on a real Ubuntu server, see "## Extra: Caddy -- Alternative
# to NGINX" in the README. Direct 1:1 swap for the `apt-get install
# nginx` used in the NGINX lab's nginx-node stage.
FROM base AS caddy-node

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg \
    && rm -rf /var/lib/apt/lists/*

RUN curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' \
        | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' \
        | tee /etc/apt/sources.list.d/caddy-stable.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends caddy \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 80

# Foreground run, config path explicit -- equivalent to the NGINX lab's
# `nginx -g "daemon off;"`.
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]