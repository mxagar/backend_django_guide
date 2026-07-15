# Web-App Back-End Development Guide

This is my guide for web-app backend development, based on selected courses from:

- the [Meta Back-End Developer Professional Certificate](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/professional-certificates/meta-back-end-developer) specialization on Coursera (focusing on Django),
- and the [Backend Developer with Python](https://www.udacity.com/course/backend-developer-with-python--nd0044) nanodegree on Udacity (focusing on Flask and SQLAlchemy).

From these specializations, I have selected the following topics/courses:

1. [Introduction to Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/introduction-to-back-end-development)
2. [Introduction to Databases for Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/intro-to-databases-back-end-development)
3. [Django Web Framework](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/django-web-framework?authProvider)
4. [APIs](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/apis)
5. [The Full Stack](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/the-full-stack?authProvider=deutschetelekom)
6. [Flask SQLAlchemy Data Modelling](https://www.udacity.com/course/sql-and-data-modeling-for-the-web--cd0046)
7. [Software Architecture Patterns](https://www.udacity.com/course/software-architecture-patterns--cd14601)
8. [Implement NGINX Web Servers and Reverse Proxy Solutions](https://www.coursera.org/learn/implement-nginx-web-servers-and-reverse-proxy-solutions)

Strong Python and Git/Version Control skills are required for these courses.

Each of the topics/courses has its own sub-folder with the relevant materials, including notes, setup information, code snippets, and exercises.

Check also my following guides on related topics:

- [Web-App Front-End Development Guide](https://github.com/mxagar/frontend_react_guide)
- [Web-App Deployment Guide](https://github.com/mxagar/webapp_deployment_guide)
- [DevOps and Software Engineering Guide](https://github.com/mxagar/software_devops_ibm)

## Setup

Each subdirectory may contain its own setup instructions. If you need a generic Python environment, you can use the following recipe based on [uv](https://docs.astral.sh/uv/):

```bash
# Create a virtual environment with the correct Python version
uv venv --python 3.11

# Install the dependencies from pyproject.toml/uv.lock
uv lock
uv sync

# Activate the virtual environment
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

# Start running commands in the environment
uv run python path/to/script.py
uv run pytest

# To update the submodules, run the following command:
git submodule update --init --recursive
```

Common uv usage commands:

```bash
# Add a dependency to pyproject.toml, update the lockfile, and install it
uv add <package>

# Remove a dependency from the project
uv remove <package>

# Refresh uv.lock without installing packages
uv lock

# Create/Sync the virtual environment with pyproject.toml and uv.lock
uv sync

# Run a command inside the project environment
uv run <command>
```

The environment variables are stored in the `.env` file, which is ignored by git. You can create a `.env` file with the necessary environment variables for your setup.

## Authorship

Mikel Sagardia, 2026.  
No guarantees.  
