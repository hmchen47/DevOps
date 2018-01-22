Docker Technologies for DevOps and Developers
=============================================
By [W. Tao](https://www.udemy.com/docker-tutorial-for-devops-run-docker-containers/learn/v4/content)

# Section: 1 - Get Started with Docker Technologies
1. Course Overview: Welcome to the Docker Technology World
2. How to Take this Course and How to Get Support
3. Text Lecture: How to Take this Course and How to Get Support
4. Course Slides:  Docker Slides.pdf
5. Introduction to Virtualization Technologies
    + Hypervisor-based virtualization
    + Hypervisor-based vs. Container-based virtualization
    + Runtime isolation
    + Container virtualization
6. Docker Software's Client-Server Architecture
    + Docker client - CLI & Kitematic
    + Docker daemon = Docker Engine = Docker server - Linux-based only
7. Install Docker for Mac/Windows
    + Google w/  Docker install
8. Install Docker Toolbox - Mac
9. Install Docker Toolbox - Windows
10. Important Concepts of Docker Technology
    + Images
    + Containers
    + Registries and Repositories
11. Run Our First Hello World Docker Container
    + Docker Hub - busybox <- official image
    + syntax: `docker run [-flag...][--lflag...] <image:tag> [cmd [args]]`
        + ex: `docker run busybox:1.28 echo "Hello world!"` -> display "Hello world!" in stdout
        + ex: `docker run busybox:1.28 sleep 100` -> sleep 100 secs
        + flags: `-i` = interactive; `-t` = pseudo tty
12. Deep Dive into Docker Containers
    + Foreground vs. detached: -d = background; ex. `docker run -d busybox:1.28 sleep 100`
    + display instaces: `docker ps [-a]`
        + fiedls: CONTAINER ID [cid]; IMAGE; COMMAND; CREATED; STATUS; PORTS; NAMES
    + remove instace after completion: `--rm`; ex. `docker run --rm busybox:1.28 sleep 1`
    + display low level info about a image or container: `docker inspect <cid>`
13. Docker Port Mapping and Docker Logs Command
    + Docker Hub: tomcat:8.0 - Apache server, port 8080
    + Access outside of the host on port 8888
        + syntax: `docker -it -d -rm -p 8888:8080 tomcat:8.0`
        + flag: `-p host_port:container_port`
        + broswer: http://localhost:8888 or http://host-ip:8888
    + Docker log: `docker logs <cid>`
14. Extra Learning: [Deep Dive into Docker Logging](https://www.level-up.one/deep-dive-into-docker-logging/)

# Section: 2 - Working with Docker Images
15. Docker Image Layers
    + kernel (bootfs), base image (OS), images, writable (container)
    + writable layer 
16. Build Docker Images by using Docker Commit Command
    + Ways to build Docker container - Commit change & Dockerfile
    + Docker Commit:
        + Git packge required
        + Syntax: `docker commit <cid> <image:tag>`
        + Verify: `docker images`
17. Build Docker Images by Writing Dockerfile
    + Dockerfile:
        + Instruction -> image
        + Syntax: `docker build -t <image:tag> <.|path>`
        + FROM instruction: base image
        + Chain RUN instruction: a RUN, an image -> chain cmds, sorted
        + CMD instruction: container inside cmds
        + COPY instruction: copy local files or dirs
        + ADD instruction: Internet, not recommended
18. Dockerfile In-depth
    + Docker cache & Aggregate caching: 
        + Not updated as needed when caching
        + Sol 1: chain instruction -> RUN instruction changed
        + Sol 2: `docker build -t <image:tag> --no-chache=true`
19. Push Docker Images to Docker Hub
    + Lastest tag: 
        + avoid
        + assign tag: `docker tag <cid> <image:tag>`
    + Docker Hub
        + URL: https://hub.docker.com
        + link anme: `docker_hub_id/repo_name`

# Section: 3 - Create Containerized Web Applications
20. Containerize a Simple Hello World Web Application
    + Build docker container: `docker build -t <imgname:tag>`
    + Verify: `dcoker images`
    + Execute docker container: `docker run -d -p 5000:5000 <CONTID>`
21. Text Direction: Containerize a Hello World Web Application
22. Implement a Simple Key-value Lookup Service
    + checkout dockerapp v0.2: `git stash && git checkout v0.2`
    + Redis:
        + in-memory data structure store, used as DB, cache, and message broker
        + built-in replication and different level of on-disk persistence
        + Python implementation: check app/app.py for dockerapp v0.2
23. Create Docker Container Links
24. D3: Automate Current Workflow with Docker Compose
25. Deep Dive into Docker Compose Workflow
26. Extra Learning: [Things to Watch out When Working with Docker Containers](https://www.level-up.one/things-watch-working-docker-containers/)

# Section: 4 - Docker Networking
27. Introduction to Docker Networking
28. None Network
29. Bridge Network
30. D3: Host Network and Overlay Network
31. D3: Text Lecture: Overlay Network
32. D3: Define Container Networks with Docker Compose

# Section: 5 - Create a Continuous Integration Pipeline
33. Write and Run Unit Tests inside Containers
34. Introduction to Continuous Integration
35. Text Direction: Introduction to Continuous Integration
36. D3: Link CircleCI with Github Account for Setting up a CI Workflow
37. Push Docker Images To DockerHub from CircleCI
38. Trouble Shooting: Push Docker Images to Docker Hub

# Section: 6 - Deploy Docker Containers in Production
39. D3: Introduction to Running Docker Containers in Production
40. Register Digital Ocean Account for Deploying Containerized Applications
41. D3: Deploy Docker Application to the Cloud with Docker Machine
42. Text Direction: Deploy Docker Application to the Cloud with Docker Machine
43. D3: Introduction to Docker Swarm and Set up Swarm Cluster
44. D3: Deploy Docker App Services to the Cloud via Docker Swarm
45. Extra learning Material: Dockers Monitoring Tools

# Section: 7 - Additional Learning Materials
46. What is new in Docker 17.06
47. Docker's Native support for Kubernetes
48. Future Learning
49. Text Lecture: Future Learning
50. Coupons to Our Other Courses


