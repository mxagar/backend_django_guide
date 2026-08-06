# Shared base: built once, reused by both stages below so the apt-get
# layer and the student user are not duplicated across the two images.
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
    && chmod 0440 /etc/sudoers.d/student \
    # Ubuntu creates home directories as 750 (owner + group only). NGINX's
    # worker processes run as www-data, which is neither student nor in
    # its group, so without this it can't even traverse /home/student to
    # reach the bind-mounted nginx-html/html folders -- causing 403s.
    && chmod o+rx /home/student

# ---- backend-node -----------------------------------------------------
# Course uses Node.js/Express here; we use Python/FastAPI instead.
# Packages are installed now, in the image, rather than by hand over SSH.
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

# ---- nginx-node ---------------------------------------------------------
# Adds only NGINX on top of the shared base, skipping recommended
# packages (docs, geoip modules, etc.) that aren't needed for the lab.
FROM base AS nginx-node

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        nginx \
        vim \
        curl \
        iproute2 \
    && rm -rf /var/lib/apt/lists/*

RUN chown -R student:student /var/www

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
