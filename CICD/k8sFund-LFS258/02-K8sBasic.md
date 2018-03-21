Basics of Kubernetes
====================

## 2.1 Basics of Kubernetes

## 2.2 Introduction
[video][vid1]

[vid]: https://lms.quickstart.com/custom/858487/media/Basics%20of%20Kubernetes.mp4

## 2.3 Learning Objectives
+ Discussion Kubernetes
+ Learn the basic Kubernetes terminology
+ Discuss the configuration tools
+ Learn what community resources are available

## 2.4 What is Kubernetes?
+ Challenege: 
    + connecting containers across multiple hosts, scaling them, deploying applications w/o downtime
    + service discovery among several aspects
+ [Kubernetes][k8s]:
    + a sey of primitives and a powerful open and extensible API
    + an open-source system for automating deployment, scaling, and management of containerized applications
    + originated from Borg @ Google, 15 yrs experience
    + Helmsman = pilot of the ship
    + the pilot of a ship of containers
    + K8s, pronounced like _Kate's_

[k8s]: https://kubernetes.io/

## 2.5 Components of Kubernetes
Kuubernets:
+ small web servers = microservices
+ transient server deployment
+ many nginx servers instead of large Apache web server with many `httpd` daemons to responding to page requests
+ decoupling: 
    + Service: tie traffic from one agent to another (e.g. frontend web server to backend DB) and handle new IP or other info
    + API-call driven: communication between components; flexible
+ Communication info stored in __JSON__ format, but mostly written in __YAML__ 
+ K8s agents convert the YAML to JSON prior to presistent to the database
+ written in __Go Language__, a portable language like a hybridization btw C__, Python, and Java

## 2.6 Challenges
+ Containers, and __Docker__ specifically, have empowered developers with ease of building container images, simplicity of sharing images via Docker registries, and providing a powerful user experience to manage containers
+ challenge: managing containers at scale and archetecturing a distributed application based on microservices' principles
    + continuous integration pipeline: build, test and verify container images
    + need a cluster of machines acting as base infrastructure on which to run containers
    + need a system to launch containers, and watch over them when things fail and self-heal
    + perform rolling updates and rollbacks
    + eventually tear down the resource when no longer needed
+ Requirements:
    + flexible, scalable, and easy-to-use network and storage
    + network join the resource to other containers while still keeping the traffic secure from others
    + a storage structure providing and keeping or recycling storage in a seamless manaber

## 2.7 Other Solutions
Solutions other than Kubernetes
+ [Docker Swarm](https://docs.docker.com/swarm/)
    + Docker Inc. solution
    + restructured recently based on [SwarmKit](https://github.com/docker/swarmkit)
    + embedded with the __Docker Engine__
+ [Apache Mesos](http://mesos.apache.org/)
    + data center scheduler, running containers through the use of framework
    + [Marathon](mesos.apache.org): the framework to orchestrate containers
+ [Nomad](https://www.nomadproject.io/)
    + Hashicrop, makers of __Vagrant__ and __Consul__
    + Solution for managing containerized applications
    + schedule tasks defined in Jobs
    + with a Docker driver defined a running containers as a task
+ [Rancher](http://rancher.com/)
    + a container-agnostic system
    + provide a single pane of glass interface to manage applications
    + Support Mesos, Swarm, Kubernetes

## 2.8 The Borg Hertiage
+ Inspired by Borg - internal system used by Google to manage its applications
+ Kubernetes utilizing valuable lessons learned from Borg
+ part of the current growth in Kubernetes making it easier to work with and handle workloads not found in a Google data center
+ [Large-scale cluster management at Google with Brog](https://research.google.com/pubs/pub43438.html)
+ Google contributed `cgroup` to the Linux kernel in 2007 - limiting the resources used by collection of processes
+ `cgroup` and __Linux namespaces__: heart of containers, including Docker
+ __Mesos__ 
    + inspired by discussions with Google
    + build a multi-level scheduler, better use a data center cluster
+ Cloud Foundry Foundation
    + 12 factor application principles
    + great guidance to build web applications that can scale easily, be deployed in the cloud, and automate builds
    + Borg and Kubernetes address these principles

![The Kubernetes Lineage](https://image.slidesharecdn.com/cloudfoundry-theplatformforforgingcloudnativeapplications-151006123238-lva1-app6891/95/cloud-foundry-the-platform-for-forging-cloud-native-applications-24-638.jpg?cb=1444134833)

