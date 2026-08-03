# Intoduction to Web-App Back-End Development

This is my guide for web-app backend development, based on selected courses from:
- the [Meta Back-End Developer Professional Certificate](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/professional-certificates/meta-back-end-developer) specialization on Coursera
- and the [Backend Developer with Python](https://www.udacity.com/course/backend-developer-with-python--nd0044) nanodegree on Udacity.

From these specializations, I have selected the following topics/courses:

1. [Introduction to Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/introduction-to-back-end-development)
2. [Introduction to Databases for Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/intro-to-databases-back-end-development)
3. [Django Web Framework](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/django-web-framework?authProvider)
4. [APIs](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/apis)
5. [The Full Stack](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/the-full-stack?authProvider=deutschetelekom)
6. [Flask SQLAlchemy Data Modelling](https://www.udacity.com/course/sql-and-data-modeling-for-the-web--cd0046)
7. [Software Architecture Patterns](https://www.udacity.com/course/software-architecture-patterns--cd14601)
8. [Implement NGINX Web Servers and Reverse Proxy Solutions](https://www.coursera.org/learn/implement-nginx-web-servers-and-reverse-proxy-solutions)

This module deals with the eighth topic/course: **Implement NGINX Web Servers and Reverse Proxy Solutions**.

Table of Contents:

- [Intoduction to Web-App Back-End Development](#intoduction-to-web-app-back-end-development)
  - [1. Getting Statrted with NGINX Website Deployment](#1-getting-statrted-with-nginx-website-deployment)
    - [Introduction and Objectives](#introduction-and-objectives)
    - [NGINX Fundamentals through Demos](#nginx-fundamentals-through-demos)
      - [Demo Part 1a: Create an AWS EC2 Instance](#demo-part-1a-create-an-aws-ec2-instance)
      - [Demo Part 1b: Install and Launch NGINX](#demo-part-1b-install-and-launch-nginx)
      - [Demo Part 2: NGINX Basic Configuration](#demo-part-2-nginx-basic-configuration)
    - [Completing Website Deployment with NGINX](#completing-website-deployment-with-nginx)
  - [2. Project Setup and Core NGINX Configuration](#2-project-setup-and-core-nginx-configuration)
    - [Reverse Proxy Introduction and Case Content](#reverse-proxy-introduction-and-case-content)
    - [Lab Preparation and Secure Server Access](#lab-preparation-and-secure-server-access)
    - [NGINX Configuration and Static Content Hosting](#nginx-configuration-and-static-content-hosting)
  - [3. Backend Integration and Reverse Proxy Implementation](#3-backend-integration-and-reverse-proxy-implementation)
    - [Backend Services Creation](#backend-services-creation)
    - [Virtual Hosting and Reverse Proxy Architecture](#virtual-hosting-and-reverse-proxy-architecture)
  - [4. Security, Load Balancing, and Performance Optimization](#4-security-load-balancing-and-performance-optimization)
    - [Access Control and SSL Security](#access-control-and-ssl-security)
    - [Advanced SSL and Load Balancing Strategies](#advanced-ssl-and-load-balancing-strategies)
    - [Monitoring, Optimization, and Project Wrap-Up](#monitoring-optimization-and-project-wrap-up)
  - [Extra: Caddy](#extra-caddy)

## 1. Getting Statrted with NGINX Website Deployment

### Introduction and Objectives

- This tutorial covers deploying an already-built website (HTML, JavaScript, CSS) onto a production server using NGINX (pronounced "engine-x"), an open-source web server and reverse proxy, free on Linux.
- What a web server does: mediates HTTP (hypertext transfer protocol) requests/responses between users and a backend server (e.g. Google), handling many simultaneous, varied requests (images, music, etc.) efficiently and smoothly.
- NGINX architecture:
  - A master process handles privileged operations: reading configuration and binding to the website's allocated ports.
  - Worker processes (helpers) and a cache manager/cache loader handle the rest; the cache loader loads disk cache into memory, and the cache manager manages that disk cache.
  - It is event-driven: sockets listen for incoming events (HTTP requests); workers pick up events based on request type (GET, POST, etc.) and perform the read/write I/O (input/output) against the backend.
  - Goal: handle any volume of traffic efficiently via load balancing and efficient CPU/memory usage.
- NGINX benefits: efficient load balancing and concurrent-connection handling, large community/forum support, proven compatibility with common web applications, smoother and faster site performance, and reverse-proxy capability.
- Hands-on lab plan (5 steps): install NGINX, enable the firewall for NGINX, deploy the demo website, check the NGINX service status, and manage the NGINX process after deployment.

![NGINX Architecture](./assets/nginx_architecture.png)

- Diagram walkthrough: users send HTTP/HTTPS requests, which the master routes to workers (Worker 1, 2, 3).
  - Worker 1 and the proxy cache exchange data directly, serving cached responses without hitting the backend.
  - Worker 2 feeds the proxy cache, which is populated and maintained by the cache manager and cache loader.
  - Worker 3 forwards requests onward to the backend resources: web server, application server, Memcached, and other backend services.
- NGINX workers vs. Django: the "workers" in the diagram are NGINX's own worker processes, not Django; each runs an event loop handling many connections concurrently (non-blocking I/O), accepting requests, serving static/cached content directly, and proxying the rest onward.
- Where Django runs: Django never runs inside NGINX. NGINX only serves static files and reverse-proxies dynamic requests to a separate WSGI/ASGI (web/asynchronous server gateway interface) server such as Gunicorn, uWSGI, or Daphne/Uvicorn, which is where Django actually executes. In the diagram, this is the "Application Server"/"Backend" box that Worker 3 forwards to.
- Multiple Django instances: whether several Django backends run is a deployment choice, at two independent levels.
  - Within one app server: Gunicorn/uWSGI can spawn multiple worker processes (like NGINX's own workers) from a single codebase and app-server instance.
  - Across app servers: separate app-server instances (different ports, containers, or machines) can each run their own Gunicorn+Django stack, with NGINX load-balancing across them via an `upstream` block (round-robin, least-connections, etc.) -- covered in the "Load Balancing" topic of section 4.

A typical Django setup looks like this:

```
Internet
   ↓
Nginx
   ↓
Gunicorn / Uvicorn
   ↓
Django
   ↓
PostgreSQL
```

With multiple Django replicas (Nginx acts as the entry point and load-balances requests between them):

```
                 ┌─ Django replica 1
Internet → Nginx ├─ Django replica 2
                 └─ Django replica 3
```

### NGINX Fundamentals through Demos

#### Demo Part 1a: Create an AWS EC2 Instance

- Goal for this lab: create an AWS EC2 (Elastic Compute Cloud) virtual machine, then (in Part 1b) install NGINX on it and open the firewall for it.
- Launch steps in the AWS console:
  - Click "Launch instance," pick a Free Tier eligible AMI (Amazon Machine Image).
    - The original demo uses Ubuntu Server 18.04, which has reached end of standard support; prefer a current LTS (long-term support) release such as Ubuntu Server 22.04 or 24.04 instead.
  - Configure the security group's inbound rules to allow the ports the server needs: SSH (port 22, for remote access) and a custom TCP rule for HTTP (port 80, for the web server) -- both open to the traffic source you expect.
  - Select an existing key pair (or create one) for SSH access, then launch the instance and give it a name (e.g. "Nginx server").
- Once the instance is running, connect to it over SSH (secure shell) using its public DNS (domain name system) name and the key pair:

```bash
ssh -i "your-key.pem" ubuntu@<ec2-public-dns>
```

#### Demo Part 1b: Install and Launch NGINX

- With the instance up and connected, install and verify NGINX:
  - Update the package index so installed software is current.
  - Install NGINX from the Ubuntu package repository.
  - List the firewall (`ufw`, uncomplicated firewall) application profiles to confirm an NGINX profile is registered.
  - Allow the NGINX HTTP profile through the firewall so port 80 traffic reaches the server.
  - Check the NGINX service status to confirm it's active and running.
- Verify from a browser by visiting the instance's public DNS address -- it should show the default "Welcome to nginx!" page.


```bash
sudo apt update
sudo apt install nginx
sudo ufw app list
sudo ufw allow 'Nginx HTTP'
sudo service nginx status
```

#### Demo Part 2: NGINX Basic Configuration

- Case study recap: a startup has a new website ready and wants it deployed with NGINX; Part 1 installed NGINX and opened the firewall, this lab explores NGINX's configuration layout and then scaffolds a placeholder site to deploy next.
- Key locations to know for managing and debugging a site:
  - `/var/www/html` -- the default web root holding the built-in "Welcome to nginx!" page served out of the box.
  - `/etc/nginx` -- the main configuration directory:
    - `sites-available/` stores one server-block config file per site you might host.
    - `sites-enabled/` holds only the sites NGINX actually serves; a config in `sites-available` takes effect only once it's symlinked into `sites-enabled`. Each server block sets what port to listen on, the server (domain) name, the site's root folder, and its default index file.
    - `nginx.conf` is the global config file -- edits here affect the whole server, not a single site.
  - `/var/log/nginx` -- holds `access.log` (every incoming request) and `error.log` (server errors), the first places to check when debugging a deployment.
- Demo site scaffold: create a placeholder site (`demo.com`) matching the case study, to be wired up and deployed in the next lab.
  - Create the site's web root, using `-p` to create parent directories as needed (the narrated `-b` flag doesn't exist for `mkdir`).
  - Recursively hand ownership of that folder to the current user so it can be edited without `sudo`.

```bash
sudo mkdir -p /var/www/demo.com/html
sudo chown -R $USER:$USER /var/www/demo.com/html
```

### Completing Website Deployment with NGINX

## 2. Project Setup and Core NGINX Configuration

### Reverse Proxy Introduction and Case Content

### Lab Preparation and Secure Server Access

### NGINX Configuration and Static Content Hosting

## 3. Backend Integration and Reverse Proxy Implementation

### Backend Services Creation

### Virtual Hosting and Reverse Proxy Architecture

## 4. Security, Load Balancing, and Performance Optimization

### Access Control and SSL Security

### Advanced SSL and Load Balancing Strategies

### Monitoring, Optimization, and Project Wrap-Up

## Extra: Caddy



