# Intoduction to Web-App Back-End Development

This is my guide for web-app backend development, based on the [Meta Back-End Developer Professional Certificate](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/professional-certificates/meta-back-end-developer) specialization on Coursera. From that specializatuon, I have selected these topics/courses:

1. [Introduction to Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/introduction-to-back-end-development)
2. [Introduction to Databases & Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/intro-to-databases-back-end-development)
3. [Django Web Framework](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/django-web-framework?authProvider)
4. [APIs](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/apis)
5. [The Full Stack](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/the-full-stack?authProvider=deutschetelekom)
6. [Back-End Developer Capstone Project](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/back-end-developer-capstone)

This module deals with the first topic/course: **Introduction to Back-End Development**.

Table of Contents:

- [Intoduction to Web-App Back-End Development](#intoduction-to-web-app-back-end-development)
  - [Intoduction](#intoduction)
    - [How the web works](#how-the-web-works)

## Intoduction

### How the web works

- Devices connect and communicate through wired or wireless connections, forming a network.
- As more devices join, direct connections become complex; this is solved using network switches.
- Network switches connect multiple devices and can also connect to other switches.
- Many interconnected networks together form the Internet.
- Online services (websites, streaming, etc.) are hosted on servers, while user devices act as clients (client-server model).

- **Server = computer providing services** to clients (e.g., websites, messaging).
- Usually hosted in **data centers** with power, cooling, and connectivity redundancy.
- Data centers are **geographically distributed** --> faster access via proximity.
- **Hardware vs software**:
  - Hardware = physical resources (CPU, RAM, storage)
  - Software = code/services running on the machine
- Servers are **specialized by purpose** (storage-heavy vs compute-heavy).
- A **web server** is software that:
  - Stores and serves website content
  - Handles **HTTP request–response cycle**
- Core role: **respond to client requests at scale** (thousands/sec).

- **Webpage vs website**:
  - Webpage = single document
  - Website = collection of linked webpages
- **Webpages are just text documents** sent from server --> browser
- **Core stack (always the same)**:
  - HTML --> structure/content
  - CSS --> styling/layout
  - JavaScript --> behavior/interactivity
- **Browser pipeline**:
  - Receives HTML/CSS/JS
  - Parses sequentially
  - Builds visual output --> **rendering**
- **JS is the dynamic layer**: validation, updates, real-time UI
- **Links form the web graph**: pages can link across sites
- **Scale insight**: massive, continuously growing system, but built on same 3 primitives
- **Key mental model**:
  --> webpage = code --> browser interprets --> UI rendered

- **Browser = client app** that requests and displays web content
- **Core flow (always the same)**:
  1. User enters URL
  2. Browser sends request (HTTP)
  3. Server processes it (may query DB)
  4. Server returns response
  5. Browser renders page
- **URL structure**: protocol (HTTP), domain, path
- **Request–response cycle = fundamental abstraction** of the web
- **Dynamic requests**: user actions (e.g., search) → new requests with parameters
- **Server side**: logic + database lookup → builds response
- **Browser side**: renders returned code into UI
- **Same pattern applies** to search, chat, streaming, etc.


