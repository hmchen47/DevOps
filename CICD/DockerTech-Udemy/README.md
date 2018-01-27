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
    + Verify images: `dcoker images`
    + Execute docker container: `docker run -d -p 5000:5000 <CONTID>`
    + Verify process: 
        + running processes: `docker ps`
        + all processes including stop ones: `docker ps -a`
21. Text Direction: Containerize a Hello World Web Application
22. Implement a Simple Key-value Lookup Service
    + checkout dockerapp v0.2: `git stash && git checkout v0.2`
    + Redis:
        + in-memory data structure store, used as DB, cache, and message broker
        + built-in replication and different level of on-disk persistence
        + Python implementation: check app/app.py for dockerapp v0.2
23. Create Docker Container Links
    + link: secure channel between containers w/o network ports
    + redis: link flask and Python app container
    + build radis: `docker run -d --name redis radis:3.2.0`
    + checkout dockerapp v0.3
    + run dockerapp w/ redis link: `docker run -d -p 5000:5000 --link redis dockerapp:v0.3`
    + Verify:
        + login container: `docker exec -it <contid> bash`
        + get redis IP addr: `ping <ip addr of redis>`
    + purpose: isolation of containers -> Microservice architecture
24. D3: Automate Current Workflow with Docker Compose
    + Tool for defining and running multi-container Docker apps
    + Compose file: 
        1. define environment w/ Dockerfile
        2. define services w/docker-compose.yml
        3. run `docker-compose up -d`
    + Verify: `docker-compse ps`
    + Stop services: `docker-compose stop`
    + display images: `docker-compose images`
25. Deep Dive into Docker Compose Workflow
    + Containers start: `docker-compose up -d`
    + Container instances: `docker-compose ps`
    + Logging:
        + Output colored and aggregated logs: `docker-compose logs`
        + Follow log output: `docker-compose logs -f`
    + Remove all containers: `docker-compose rm`
    + Rebuild all the images: `docker-compose build`
26. Extra Learning: [Things to Watch out When Working with Docker Containers](https://www.level-up.one/things-watch-working-docker-containers/)

# Section: 4 - Docker Networking
27. Introduction to Docker Networking
    + types of networks: 
        + closed network / None network
        + bridge network
        + host network
        + overlay network
    + Display networks" `docker network ls`
28. None Network
    + no network - totally isolated
    + max level of network protection
    + create none network container: `docker run -d --net none busybox sleep 1000`
    + Verify:
        + host connectivity: `ping 8.8.8.8`
        + login Docker container: `docker exec -it <contid> /bin/bash`
        + container connectivity: `ping 8.8.8.8`
29. Bridge Network
    + 2 network interfaces: loopback and private
    + no connectivity between two different bridge networks -> sol: manually connect 
    + reduce level of network isolation
    + detail inspection: `docker network inspect [bridge]` -> get subnet for bridge network
    + exam network within container: `docker exec -it <cont> ifconfig`
    + create customized bridge network: `docker network create --driver bridge <net_name>`
    + verify IP range: `docker network inspect <net_name>`
    + new container w/ new bridge network: `docker run -d --name <cont_name> --net <net_name> busybox sleep 1000`
30. D3: Host Network and Overlay Network
    + open network: full access to the host's interface
    + min network security model
    + create open container: `docker run -d --name <cont_name> --net host <img>`
    + overlay network: support mult-host networking out-of-box
31. D3: Text Lecture: [Overlay Network](https://docs.docker.com/engine/userguide/networking/overlay-standalone-swarm/#create-a-swarm-cluster)
32. D3: Define Container Networks with Docker Compose
    + Start docker containers: `docker-compose up -d`
    + Removing default network: `docker-compose down`
    + docker-compose.yml:
        ```yaml
        networks:
            my_net:
                driver: bridge
        Service:
            ...
                networks:
                    - my_net
            redis:
                networks:
                    -my_net
        ```

# Section: 5 - Create a Continuous Integration Pipeline
33. Write and Run Unit Tests inside Containers
    + unit test: test some basic functionality of docker app code
    + external services
    + execute asap
    + Python pakage:
        + unit testing framework
        + import unittest
        + checkout dockerapp v0.5
    + Pros: single container image for development, test, and production
    + app/test.py added
    ```python
    import unittest
    import app

    class TestDockerapp(unittest.TestCase):

        def setUp(self):
            self.app = app.app.test_client()

        def test_save_value(self):
            response = self.app.post('/', data=dict(submit='save', key='2', cache_value='two'))
            assert response.status_code == 200
            assert b'2' in response.data
            assert b'two' in response.data

        def test_load_value(self):
            self.app.post('/', data=dict(submit='save', key='2', cache_value='two'))
            response = self.app.post('/', data=dict(submit='load', key='2'))
            assert response.status_code == 200
            assert b'2' in response.data
            assert b'two' in response.data

    if __name__=='__main__':
    unittest.main()
    ```
34. Introduction to Continuous Integration
    + a software engineering practice in which isolated changes are immediately tested and reported
35. Text Direction: Introduction to Continuous Integration
    + URL of the Github account to fork: https://github.com/jleetutorial/dockerapp
    + Checking for existing SSH keys: https://help.github.com/articles/checking-for-existing-ssh-keys/
    + Generating a new SSH key and adding it to the ssh-agent: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
    + Adding a new SSH key to your GitHub account: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
36. D3: [Link CircleCI with Github Account for Setting up a CI Workflow](https://www.udemy.com/docker-tutorial-for-devops-run-docker-containers/learn/v4/t/lecture/8288504?start=0)
    + checkout dockerapp v0.6
    + CircleCI: hosted countinous integration server
    + edit `.circlci/config.yml`
    ```yaml
    version: 2
    jobs:
    build:
        working_directory: /dockerapp
        docker:
        - image: docker:17.05.0-ce-git
        steps:
        - checkout
        - setup_remote_docker
        - run:
            name: Install dependencies
            command: |
                apk add --no-cache py-pip=9.0.0-r1
                pip install docker-compose==1.15.0
        - run:
            name: Run tests
            command: |
                docker-compose up -d
                docker-compose run dockerapp python test.py

    ```
    + Circule CI
        + Sigup CircleCI wirh GitHub
        + Add Project > select and setup project
        + start build -> auto test with `config.yml`
    + Procedure
        1. edit local files and git commits
        2. push to GitHub
        3. login CircleCI and/or refresh
        4. select releated branch and start build -> auto test with unit test module
37. Push Docker Images To DockerHub from CircleCI
    + 
38. Trouble Shooting: Push Docker Images to Docker Hub

    If you are able to run `docker login`, but encountered the following __unauthorized: authentication required__ error while running `docker push`
    ```
    [root@terry ~]# docker login --username=1972
    Password:
    Login Succeeded
    [root@terry ~]#
    [root@terry ~]# docker push asiye_yigit_tutorial/debian:1.01
    The push refers to a repository [docker.io/asiye_yigit_tutorial/debian]
    29303f03b719: Preparing
    77a77cd4826d: Preparing
    fe4c16cbf7a4: Preparing
    unauthorized: authentication require
    ```
    Soution:

        Creating the repository on Docker hub before running docker push.

    Take a look at [stackoverflow.com](http://stackoverflow.com/questions/36663742/docker-unauthorized-authentication-required-upon-push-with-successful-login)

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


