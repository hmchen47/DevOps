# Chapter 5. Containers

## Introduction and Learning Objectives
### Containers
[Operating-System-level virtualization][oslv] allows us to run multiple isolated user-space instances in parallel. These user-space instances have the application code, the required libraries, and the required runtime to run the application without any external dependencies. These user-space instances are referred to as __containers__.

In this chapter, we will talk about __containers__, as well as provide details on basic __Docker__ operations.

### Learning Objectives
By the end of this chapter you should be able to:

+ Explain the concept of __containers__.
+ Describe the basic __Docker__ operations.


## Containers
### Introduction
Most of the time, our end goal is to run an application. But we need to make sure this works on multiple hardware and platforms, like Developer Laptops, VMs, Datacenters, Public and Private clouds, etc.

![image][img1]

Figure 5.1: Running an Application (by __Docker, Inc__., retrieved from [docker.com][dockerapp])

As developers, we do not want to worry about these aspects and we expect our application to work, irrespective of the underlying platform. By using a container technology like __Docker__, we can bundle our application with all its dependencies in a box.

![image][img2]

Figure 5.2: A __Docker__ Container (by __Docker, Inc.__, retrieved from [LinkedIn SlideShare][linkedin])

The box is then shipped to different platforms and it will run identically on each one of them.

### Images and Containers
In the container world, this box (containing our application and all its dependencies) is referred to as an __image__. A running instance of this box is referred to as a __container__. We can spin multiple containers from the same image.

An image contains the application, its dependencies and the user-space libraries. User-space libraries like `glibc` enable switching from user-space to kernel-space. An image does not contain any kernel-space components.

When a __container__ is created from an image, it runs as a process on the host's kernel. It is the host kernel's job to isolate and provide resources to each container. 

### The Container Technology: Building Blocks
We will now take a look at some of the building blocks of the container technology, provided by the __Linux__ Kernel.

#### Namespaces 
A namespace wraps a particular global system resource like network, process IDs in an abstraction, that makes it appear to the processes within the namespace that they have their own isolated instance of the global resource. The following global resources are namespaced:

+ pid - provides each namespace to have the same PIDs. Each container has its own PID 1.
+ net - allows each namespace to have its network stack. Each container has its own IP address.
+ mnt - allows each namespace to have its own view of the filesystem hierarchy.
+ ipc - allows each namespace to have its own interprocess communication.
+ uts - allows each namespace to have its own hostname and domainname.
+ user - allows each namespace to have its own user and group ID number spaces. A root user inside a container is not the root user of the host, on which the container is running.

#### cgroups 
_Control groups_ are used to organize processes hierarchically and distribute system resources along the hierarchy in a controlled and configurable manner. The following __cgroups__ are available for __Linux__:

+ blkio
+ cpu
+ cpuacct
+ cpuset
+ devices
+ freezer
+ memory

#### Union filesystem 
The __Union__ filesystem allows files and directories of separate filesystems, known as __layers__, to be transparently overlaid on each other, to create a new virtual filesystem.

An image used in __Docker__ is made of multiple layers and, while starting a new container, we merge all those layers to create a read-only filesystem. On top of a read-only filesystem, a container gets a read-write layer, which is an ephemeral layer and it is local to the container. 

### Container Runtimes
Namespaces and __cgroups__ have existed in the __Linux__ kernel for quite some time, but consuming them to create containers was not easy. After __Docker__ was launched in 2013, containers started to become mainstream. __Docker__ hid all the complexities in the background and came up with an easy workflow to share and manage both images and containers. Some of the container runtimes are provided below:

#### [runC][runc]
In the last few years, we have seen a rapid growth in the interest and adoption for container technologies. Most of the cloud providers and IT vendors offer support for containers. To make sure there is no vendor locking and no inclination towards a particular company or project, IT companies came together and formed an open governance structure, called "[The Open Container Initiative][oci]", under the auspices of __The Linux Foundation__. The governance body came up with [specifications][spec] to create standards on Operating System process and application containers. [runC][runc] is the CLI tool for spawning and running containers according to the specifications.

#### [Docker][docker]
__Docker__ is an Open Source, __Apache 2.0__-licensed project. __Docker, Inc.__ is the primary sponsor of the project.

Until __Docker 1.10__ release, __Docker__ used [libcontainer][libcont] to access the host's kernel features to create containers. With __Docker 1.11__ it started using __runC__ as container runtime, which is an implementation of the [OCI specifications][ocispec]. __Docker__ uses the containerd daemon to control __runC__ containers.

![image][img3]

Figure 5.3: Docker Engine and __containerd__ (by __Docker, Inc.__, retrieved from docker.com)

As far as end users are concerned, there is no change in the user-experience between __Docker 1.10__ and __Docker 1.11__. 

Currently, __Docker__ is fully supported on __Linux__. Native support on __Mac__ and __Windows__ is in the pipeline.

#### [rkt][RKT]
__rkt__ (pronounced "rock-it") is an Open Source, __Apache 2.0__-licensed project from __CoreOS__. It implements the [App Container specification][appcspec].

### Containers vs. VMs
A Virtual Machine runs on top of a [Hypervisor][hyper], which emulates different hardware, like CPU, Memory, etc., so that a Guest OS can be installed on top of them. Different kinds of Guest Operating Systems can run on top of one Hypervisor. Between an application running inside a Guest OS and in the outside world, there are multiple layers: the Guest OS, the Hypervisor, the Host OS. 

![image][img4]

Figure 5.4: Docker Containers versus VMs (by __Docker, Inc.__)

On the other hand, containers run directly as a process on top of the Host OS. There is no indirection as we see in VMs, which help containers to get near-native performance. Also, as the containers have very little footprint, we can pack a higher number of containers than VMs on the same physical machine. As containers run on the Host OS, we need to make sure containers are compatible with the Host OS.

### Docker Runtime
__Docker runtime__ is from __Docker, Inc.__, which has built multiple products around the runtime:

+ Docker Datacenter
    - Docker Trusted Registry
    - Universal Control Plane
+ Docker Cloud
+ Docker Hub.

__Docker__ uses a client-server architecture, in which a __Docker client__ connects to a server (__Docker Host__) and executes the commands.

![image][img5]

Figure 5.5: Docker Architecture (by Docker, Inc., retrieved from docker.com)

### Basic Docker Operations
You can find a list of basic Docker operations below:

+ List images:

    `$ docker images`
+ Pulling an alpine image:

    `$ docker pull alpine`
+ Run a container from a locally-available image:

    `$ docker run -it alpine sh`
+ Run a container in the background (-d option) from an image :

    `$ docker run -d nginx`
+ List only running containers:

    `$ docker ps` 
+ List all containers: 

    `$ docker ps -a`
+ Inject a process inside a running container:

    `$ docker exec -it <container_id/name> bash`
+ Stop a container:

    `$ docker stop <container id/name> `
+ Delete a container:

    `$ docker rm  <container id/name>`

### Demo
The following video illustrates some of the basic operations with __Docker__.

[video][vid1]

### Benefits of Using Containers
Some of the benefits of using containers are:

+ They have very little footprint.
+ They can be deployed very fast (within milliseconds).
+ They are a flexible solution, as they can run on any computer, infrastructure, or cloud environment.
+ They can be scaled up or down with ease.
+ There is a very rich ecosystem built around them.
+ Problem containers can be easily and quickly isolated when troubleshooting and solving problems.
+ Containers use less memory and CPU than VMs running similar workloads.
+ Increased productivity with reduced overhead.

### References
+ https://lwn.net/Articles/531114/
+ https://lwn.net/Articles/671722/
+ https://www.docker.com/
+ https://runc.io/
+ https://containerd.tools/
+ https://github.com/coreos/rkt

## Knowledge Check
1. Which of the following resources can be namespaced?

        A. Net 
        B. User 
        C. PID 
        D. IPC 

        Ans: A, B, C, D

2. What do we have to use to control the resources utilization among a set of processes?

        Ans: Control Group

3. Do we need to emulate hardware in order to run a container?

        Ans: No



[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V001000_DTH.mp4
[vid2]: 
[vid3]: 
[vid4]: 
[vid5]: 

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f6a8a12f7176586ff22a63aaae7eb4f8/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Running_an_Application.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ab813032f150e0d74d9016b2e8a55ed3/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Docker_Container.jpeg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/164b808d0b00542b6fb5ffe53980125e/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Docker_Engine_and_containerd.png
[img4]:https://prod-edxapp.edx-cdn.org/assets/courseware/v1/dda30a84088be3492f2f5ca355c395ab/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Docker_Containers_vs._VMs.png
[img5]: ./diagrams/architecture.svg
[img6]: 
[img7]: 

[oslv]: https://en.wikipedia.org/wiki/Operating-system-level_virtualization
[dockerapp]: https://blog.docker.com/wp-content/uploads/2013/08/the_challenge.jpg
[linkedin]: http://image.slidesharecdn.com/dockerintronovember-131125185628-phpapp02/95/docker-introduction-10-638.jpg?cb=1385405862
[runc]: https://github.com/opencontainers/runc
[docker]: https://github.com/docker/docker
[rkt]: https://github.com/coreos/rkt
[oci]: https://www.opencontainers.org/
[spec]: https://github.com/opencontainers/specs
[libcont]: https://github.com/opencontainers/runc/tree/master/libcontainer
[ocispec]: https://www.opencontainers.org/
[appcspec]: https://github.com/coreos/rkt/blob/master/Documentation/app-container.md
[hyper]: https://en.wikipedia.org/wiki/Hypervisor
[dockerarch]: https://docs.docker.com/engine/article-img/architecture.svg




