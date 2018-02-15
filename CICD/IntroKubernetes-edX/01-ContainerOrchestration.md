Container Orchestration
=======================

# Introduction
With container images, we confine the application code, its runtime, and all of its dependencies in a pre-defined format. And, with container runtimes like [runC](https://runc.io/), [containerd](https://containerd.io/), or [rkt](https://github.com/rkt/rkt) we can use those pre-packaged images, to create one or more containers. All of these runtimes are good at running containers on a single host. But, in practice, we would like to have a fault-tolerant and scalable solution, which can be achieved by creating a single __controller/management unit__, after connecting multiple nodes together. This controller/management unit is generally referred to as a __Container Orchestrator__. 

In this chapter, we will explore why we should use container orchestrators, different implementations of container orchestrators, and where to deploy them. 

# Learning Objectives
By the end of this chapter you will be able to:

+ Define the concept of Container Orchestration.
+ Explain the reasons for doing Container Orchestration.
+ Discuss different Container Orchestration options.
+ Discuss different Container Orchestration deployment options.

# What Are Containers?
Before we dive into Container Orchestration, let's review first what containers are.

Containers are an application-centric way to deliver high-performing, scalable applications on the infrastructure of your choice.

![What are containers?](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5bd6e5b9191c79b780f131d2784cf456/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/containers.png)

With a container image, we bundle the application along with its __runtime__ and __dependencies__. We use that image to create an isolated executable environment, also known as __container__. We can deploy containers from a given image on the platform of our choice, such as desktops, VMs, Cloud, etc.

# What Is Container Orchestration?
In Development and Quality Assurance (QA) environments, we can get away with running containers on a single host to develop and test applications. However, when we go to production, we do not have the same liberty, as we need to ensure that our applications:

+ Are fault-tolerant
+ Can scale, and do this on-demand
+ Use resources optimally
+ Can discover other applications automatically, and communicate with each other
+ Are accessible from the external world 
+ Can update/rollback without any downtime. 

Container Orchestrators are the tools which group hosts together to form a cluster, and help us fulfill the requirements mentioned above.

# Container Orchestrators
Nowadays, there are many Container Orchestrators available, such as:

+ __Docker Swarm__

    Docker Swarm is a Container Orchestrator provided by Docker, Inc. It is part of Docker Engine.

+ __Kubernetes__

    Kubernetes was started by Google, but now, it is a part of the Cloud Native Computing Foundation project.

+ __Mesos Marathon__

    Marathon is one of the frameworks to run containers at scale on Apache Mesos.

+ __Amazon ECS__

    Amazon EC2 Container Service (ECS) is a hosted service provided by AWS to run Docker containers at scale on its infrastructrue.

+ __Hashicorp Nomad__

    Nomad is the Container Orchestrator provided by HashiCorp.

We have explored different Container Orchestrators in another edX MOOC, _Introduction to Cloud Infrastructure Technologies (LFS151x)_. We highly recommend that you take _LFS151x_.

# Why Use Container Orchestrators?
Though we can argue that containers at scale can be maintained manually, or with the help of some scripts, Container Orchestrators can make things easy for operators.

Container Orchestrators can:

+ Bring multiple hosts together and make them part of a cluster
+ Schedule containers to run on different hosts
+ Help containers running on one host reach out to containers running on other hosts in the cluster
+ Bind containers and storage
+ Bind containers of similar type to a higher-level construct, like services, so we don't have to deal with individual containers
+ Keep resource usage in-check, and optimize it when necessary
+ Allow secure access to applications running inside containers.

With all these built-in benefits, it makes sense to use Container Orchestrators to manage containers. In this course, we will explore Kubernetes. 

# Where to Deploy Container Orchestrators?
Most Container Orchestrators can be deployed on the infrastructure of our choice. We can deploy them on bare-metal, VMs, on-premise, or on a cloud of our choice. For example, Kubernetes can be deployed on our laptop/workstation, inside a company's datacenter, on AWS, on OpenStack, etc. There are even one-click installers available to setup Kubernetes on the Cloud, like Google Container Engine on Google Cloud, or Azure Container Service on Microsoft Azure. Similar solutions are available for other Container Orchestrators, as well.

There are companies who offer managed Container Orchestration as a Service. We will explore them for Kubernetes in one of the later chapters.

# Knowledge Check
Q1. What are the benefits of doing Container Orchestration? Select the correct answer.

    A. Fault-tolerance
    B. Optimal use of resources
    C. Scaling the applications
    D. All of the above

    Ans: d

Q2. What can Container Orchestrators do? Select all answers that apply.

    A. Schedule containers on different nodes
    B. Always provision the underlying infrastructure
    C. Help connecting containers from different hosts on the same cluster
    D. None of the above

    Ans: a, c

Q3. Which of the following are Container Orchestrators? Select all answers that apply.

    A. Vault
    B. Docker Swarm
    C. Kubernetes
    D. Ansible

    Ans: b, c
