# Nginx DevOps Assignment

## Overview

This project is created to understand basic DevOps concepts using Nginx, Docker, and GitHub Actions. Multiple applications are deployed behind a single Nginx reverse proxy with simple CI/CD automation.



## Architecture

Client request comes to Nginx, and Nginx forwards the request to the correct application running inside Docker.

Client → Nginx → Docker Network → app1 / app2 / app3 / app4



## Routing

Host-based routing is used.

* app1.localhost → app1
* app2.localhost → app2
* app3.localhost → app3
* app4.localhost → app4

Example command:

```bash
curl -H "Host: app1.localhost" http://localhost/health
```



## Applications

Each application has the following endpoints:

* `/health` – returns application health
* `/time` – returns current UTC time

Applications run inside Docker and are accessed only through Nginx.



## Docker Setup

All services run on the same Docker network.
Only Nginx exposes a port to the host machine.

To start the project:

```bash
docker compose up -d
```



## CI/CD

### CI Pipeline

* Checks which application code is changed
* Ensures VERSION file is updated when code changes
* Builds Docker images
* Checks required endpoints

### CD Pipeline

* Starts all services using Docker Compose
* Verifies routing through Nginx



## Versioning

Each application has a VERSION file.
Version is updated whenever application code changes.

Example:

```
1.0.1
```



## Completion

* Project runs successfully on fresh setup
* All applications work through Nginx
* CI and CD pipelines pass successfully
