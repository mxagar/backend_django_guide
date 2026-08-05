FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y \
        nginx \
        vim \
        curl \
        sudo \
        iproute2 \
        procps \
    && rm -rf /var/lib/apt/lists/*

# Create a normal user similar to the "ubuntu" user on EC2.
RUN useradd \
        --create-home \
        --shell /bin/bash \
        student \
    && usermod --append --groups sudo student \
    && echo "student ALL=(ALL) NOPASSWD:ALL" \
        > /etc/sudoers.d/student \
    && chmod 0440 /etc/sudoers.d/student

# Let the student user manage website files without sudo.
RUN chown -R student:student /var/www

EXPOSE 80

# NGINX must stay in the foreground inside a container.
CMD ["nginx", "-g", "daemon off;"]
