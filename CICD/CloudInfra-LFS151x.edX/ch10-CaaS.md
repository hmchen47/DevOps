# Chapter 10. Container as a Service (CaaS)

## Introduction and Learning Objectives
### Container as a Service
These days we can notice the frequent use of a new as a Service model: __Container as a Service (CaaS)__. Earlier, we talked about __IaaS, PaaS__, and __SaaS__, in which we provision infrastructure, application, and software on demand. If we follow the definition, then, with __CaaS__, we would get containers on demand. This brings __CaaS__ closer to __IaaS__. However, containers are typically used to confine and deploy an application, which brings __CaaS__ closer to __PaaS__.

As __CaaS__ sits between __IaaS__ and __PaaS__, it would have capabilities to support both Dev and Ops. With effective tooling and extensibility, __CaaS__ could become the game changer. Currently, there are a few solutions labeled as __CaaS__, such as the following:

+ __OpenStack Magnum__
+ __Docker Universal Control Plane__.

Other solutions are labeled as __CaaS__ enablers, like the following:

+ __Kubernetes__
+ __AWS EC2 Container Service (ECS)__
+ __Tectonic (CoreOS + Kubernetes)__
+ __Rancher__
+ and many more.

In this chapter we will look at the current CaaS solutions: __OpenStack Magnum__ and __Docker Universal Control Plane__.

### Learning Objectives
By the end of this chapter you should be able to:

+ Explain the concept of __Container as a Service (CaaS)__ and see what its benefits are for the software lifecycle. 
+ Discuss current CaaS solutions: __Docker Universal Control Plane__ and __OpenStack Magnum__.


## Docker Universal Control Plane
### Introduction to Docker Universal Control Plane
As the name suggests, the [__Docker Universal Control Plane (UCP)__][ducp] provides a centralized container management solution (on-premises or on a virtual private cloud), regardless of where your applications are running. __UCP__ is part of the _RUN_ management of Docker.

![image][img1]

Figure 10.1: The Docker CaaS Ecosystem (by Docker, Inc., retrieved from [LinkedIn SlideShare][dcaas])

__UCP__ works with existing Docker tools, like __Docker Machine__ and __Docker Swarm__, which makes adding or deleting nodes to UCP easy. UCP also integrates well with existing authentication mechanisms like __LDAP/AD__, which allows Ops teams to define fine-grained policies and roles. With fine-grained policies and roles, a developer has a limited view of the cluster, but he/she has full control of the deployment.

### Features and Benefits
Among the features and benefits of the __Docker Universal Control Plane__ are the following:

+ It integrates well with authentication tools like __LDAP/AD__ and __SSO__ with __Docker Trusted Registry__.
+ It integrates with exiting Docker tools like __Docker Machine__, __Docker Swarm__, __Docker Trusted Registry__.
+ It is easy to setup and use.
+ It manages applications and containers from a central location through the __web Admin GUI__.
+ It can be easily setup with High Availability.
+ With proper authentication, it can be operated from the CLI.
+ It provides a centralized container management solution (on-premises or on a virtual private cloud).

### Docker Datacenter
__Docker__ has another project called [__Docker Datacenter__][ddc], which is built on top of __UCP__ and __Docker Trusted Registry__. __Docker Datacenter__ is hosted completely behind the firewall.

With __Docker Datacenter__ we can build an enterprise-class __CaaS__ platform on-premises, as it is built on top of __Docker Swarm__ and integrates well with Docker tools, __Docker Registry__. It also has other features, such as __LDAP/AD__ integration, monitoring, logging, network and storage plugins. 

![image][img2]

Figure 10.2: __Docker Datacenter__ (by Docker, Inc., retrieved from [docker.com][ddcd])

### Demo
Next, we will take a closer look at __Docker Universal Control Plane__, a "container as a service" solution from Docker.

[video][vid1]

### References
+ http://www.docker.com/products/docker-universal-control-plane
+ https://www.docker.com/products/docker-datacenter


## Project Magnum on OpenStack
### Introduction to Project Magnum
[OpenStack Magnum][magnum] is a __CaaS__ service provided on top of __OpenStack__. Containers are orchestrated and scheduled on clusters created by __Kubernetes__, __Docker Swarm__, or __Mesos__. __OpenStack Magnum__ provides two services:

+ __Server API__

    Magnum Client talks to this service.

+ __Conductor__

    It manages the cluster lifecycle through __Heat__ and communicates with the __Cluster Container Orchestration Engine (COE)__.

![image][img3]

Figure 10.3: Magnum Architecture (by the OpenStack Foundation, retrieved from [openstack.org][magarch])

### Magnum Components
Next, we will talk about the building blocks of __OpenStack Magnum__:

+ __Bay__

    Bays are nodes on which the __Container Orchestration Engine__ sets up the respective __Cluster__.

+ __BayModels__

    It stores metadata information about __Bays__ like the __Container Orchestration Engine, Keypairs, Images__ to use, etc.

+ __Container Orchestration Engine (COE)__

    It is the __Container Orchestrator__ used by Magnum. Currently, it supports __Kubernetes, Docker Swarm__, and __Mesos__. __COEs__ are on top of Micro OSes, like __Atomic Host, CoreOS__, etc.

+ __Pod__

    A pod is a co-located group of application containers that run with a shared context.

+ __Service__

    It is an abstraction which defines a logical set of pods and a policy by which to access them.

+ __Replication Controller__

    It is an abstraction for managing a group of pods to ensure that a specified number of resources are running.

+ __Container__

    This is a Docker container.

### Features and Benefits
Some of the features and benefits of __OpenStack Magnum__ are:

+ __Magnum__ offers an asynchronous API that is compatible with __Keystone__.
+ It brings multi-tenancy by default, as it creates a __Bay__ per tenant. This means that for each tenant there would be a separate cluster, depending on the __COE__.
+ __Magnum__ makes containers available as first-class citizens in __OpenStack__.
+ It enables High Availability and scalability.
+ It supports __Kubernetes, Docker Swarm__, and __Mesos__ for container orchestration and scheduling.

### References
+ https://wiki.openstack.org/wiki/Magnum


## Knowledge Check
1. The goal of CaaS (Container as a Service) is to serve _______________. 

        Ans: Both Developer and Operations teams

2. Can the Docker Universal Control Plane interact with existing authentication tools like LDAP/AD? Please select the correct answer.

        Ans: yes

3. Which of the following container orchestration engines are supported by OpenStack Magnum? Please select all answers that apply.

        A. Mesos
        B. Kubernetes
        C. Docker Swarm
        D. Amazon ECS

        Ans: A, B, C


[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V004500_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e531a967ddfed4d270e0529802120178/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig.10.1_-_The_Docker_CaaS_Ecosystem.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a7f79f160ca545f97d5111eee0602510/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_10.2_-_Docker_Datacenter.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7636e7435e9c9af6336e8ea57821cbd6/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig.10.3_-_Magnum_architecture.png

[ducp]: http://www.docker.com/products/docker-universal-control-plane
[dcaas]: http://image.slidesharecdn.com/harishdockerenterprisemeetup-160405142059/95/dockerizing-within-enterprises-10-638.jpg
[ddc]: https://www.docker.com/products/docker-datacenter
[ddcd]: https://www.docker.com/sites/default/files/image_docker_1_1.png
[magnum]: https://wiki.openstack.org/wiki/Magnum
[manarch]: https://wiki.openstack.org/w/images/6/61/Magnum_architecture.png


