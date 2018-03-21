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

