Kubernetes
==========

## Introduction
In this chapter, we will explain what __Kubernetes__ is, its features, and the reasons why one should use it. We will explore the evolution of Kubernetes from [Borg](https://research.google.com/pubs/pub43438.html), which is a cluster manager created by Google. 

We will also talk about the __Cloud Native Computing Foundation (CNCF)__, which currently hosts the Kubernetes project, along with other cloud-native projects, like Prometheus, Fluentd, rkt, containerd, etc. 

## Learning Objectives
By the end of this chapter you will be able to:

+ Define Kubernetes.
+ Explain the reasons for using Kubernetes.
+ Discuss the features of Kubernetes.
+ Discuss the evolution of Kubernetes from Borg.
+ Explain what the Cloud Native Computing Foundation does.

## What Is Kubernetes?
According to the [Kubernetes website](https://kubernetes.io/),

> "Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications."

Kubernetes comes from the Greek word __κυβερνήτης__:, which means _helmsman or ship pilot_. With this analogy in mind, we can think of Kubernetes as the manager for shipping containers.

Kubernetes is also referred to as __k8s__, as there are 8 characters between k and s.

Kubernetes is highly inspired by the Google Borg system, which we will explore in this chapter. It is an open source project written in the Go language, and licensed under the [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Kubernetes was started by Google and, with its v1.0 release in July 2015, Google donated it to the [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/). We will discuss more about CNCF a little later.

Generally, Kubernetes has new releases every three months. The current stable version is 1.7 (as of June 2017).

## From Borg to Kubernetes
According to the abstract of [Google's Borg](https://research.google.com/pubs/pub43438.html) paper, published in 2015,

> "Google's Borg system is a cluster manager that runs hundreds of thousands of jobs, from many thousands of different applications, across a number of clusters each with up to tens of thousands of machines."

For more than a decade, Borg was Google's secret to run containerized workloads in production. Whatever services we use from Google, like Gmail, Drive, etc., they are all serviced using Borg.

Some of the initial authors of Kubernetes were Google employees who have used Borg and developed it in the past. They poured in their valuable knowledge and experience while designing Kubernetes. Some of the features/objects of Kubernetes that can be traced back to Borg, or to lessons learnt from it, are:

+ API Servers
+ Pods
+ IP-per-Pod
+ Services
+ Labels.

We will explore all of them, and more, in this course.

## Kubernetes Features
Kubernetes offers a very rich set of features for container orchestration. Some of its fully supported features are:

+ __Automatic binpacking__

    Kubernetes automatically schedules the containers based on resource usage and constraints, without sacrificing the availability.

+ __Self-healing__

    Kubernetes automatically replaces and reschedules the containers from failed nodes. It also kills and restarts the containers which do not respond to health checks, based on existing rules/policy.

+ __Horizontal scaling__

    Kubernetes can automatically scale applications based on resource usage like CPU and memory. In some cases, it also supports dynamic scaling based on customer metrics.

+ __Service discovery and Load balancing__

    Kubernetes groups sets of containers and refers to them via a DNS name. This DNS name is also called a Kubernetes __service__. Kubernetes can discover these services automatically, and load-balance requests between containers of a given service.

+ __Automated rollouts and rollbacks__

    Kubernetes can roll out and roll back new versions/configurations of an application, without introducing any downtime.

+ __Secrets and configuration management__

    Kubernetes can manage secrets and configuration details for an application without re-building the respective images. With secrets, we can share confidential information to our application without exposing it to the stack configuration, like on GitHub.

+ __Storage orchestration__

    With Kubernetes and its plugins, we can automatically mount local, external, and storage solutions to the containers in a seamless manner, based on Software Defined Storage (SDS).

+ __Batch execution__

    Besides long running jobs, Kubernetes also supports batch execution.

There are many other features besides the ones we just mentioned, and they are currently in alpha/beta phase. They will add great value to any Kubernetes deployment once they become GA (generally available) features. For example, support for RBAC (Role-based access control) is currently in beta phase with the Kubernetes 1.6 release.

## Why Use Kubernetes?
We just looked at some of the fully-supported Kubernetes features. We should also mention that Kubernetes is very portable and extensible. Kubernetes can be deployed on the environment of our choice, be it VMs, bare-metal, or public/private/hybrid/multi-cloud setups. Also, Kubernetes has a very modular and pluggable architecture. We can write custom APIs or plugins to extend its functionalities.

For a successful open source project, the community is as important as having great code. Kubernetes has a very thriving community across the world. It has more than 1350 contributors, who, over time, have done over 47,000 commits. There are meet-up groups in different cities which meet regularly to discuss about Kubernetes and its ecosystem. There are _Special Interest Groups (SIGs)_, which focus on special interests, such as scaling, bare-metal, networking, etc. We will discuss more about them in our last chapter, _Kubernetes Communities_.

## Kubernetes Users
With just a few years since its debut, many companies are running workloads using Kubernetes. We can find numerous user case studies on the Kubernetes website:

+ [Box](https://blog.box.com/blog/kubernetes-box-microservices-maximum-velocity/)
+ [eBay](https://www.nextplatform.com/2015/11/12/inside-ebays-shift-to-kubernetes-and-containers-atop-openstack/)
+ [Pearson](https://kubernetes.io/case-studies/pearson/)
+ [SAP](https://www.youtube.com/watch?v=4gyeixJLabo)
+ [Wikimedia](https://kubernetes.io/case-studies/wikimedia/)
+ And many more.

## Cloud Native Computing Foundation (CNCF)
The Cloud Native Computing Foundation (CNCF) is one of the projects hosted by The Linux Foundation. CNCF aims to accelerate the adoption of containers, microservices, and cloud-native applications.

![CNCF logo](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5ed4693d263ae3853fe7f0383b17a8de/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/logo_cncf.png)

CNCF hosts a set of projects, with more to be added in the future. CNCF provides resources to each of the projects, but, at the same time, each project continues to operate independently under its pre-existing governance structure and with its existing maintainers. Currently, the following projects are part of CNCF:

+ [containerd](http://containerd.io/) for Container Runtime
+ [rkt](https://github.com/rkt/rkt) for Container Runtime
+ [Kubernetes](https://kubernetes.io/) for Container Orchestration
+ [Linkerd](https://linkerd.io/) for Service Mesh
+ [gRPC](http://www.grpc.io/) for Remote Procedure Call
+ [Container Network Interface (CNI)[(https://github.com/containernetworking/cni)] for Container Networking
+ [CoreDNS](https://coredns.io/) for Service Discovery
+ [Prometheus](https://prometheus.io/) for Monitoring
+ [OpenTracing](http://opentracing.io/) for Tracing
+ [Fluentd](http://www.fluentd.org/) for Logging.

As we can see, the current set of CNCF projects can cover the entire lifecycle of an application, from its execution using container runtimes, to its monitoring and logging. This is very important to meet the CNCF goal. 

## CNCF and Kubernetes
For Kubernetes, the Cloud Native Computing Foundation:

+ Provides a neutral home for the Kubernetes trademark and enforces proper usage
+ Provides license scanning of core and vendored code
+ Offers legal guidance on patent and copyright issues
+ Creates open source [curriculum](https://www.cncf.io/announcement/2017/03/29/cloud-native-computing-foundation-makes-kubernetes-certified-administrator-exam-curriculum-freely-available-2/), [training](https://training.linuxfoundation.org/linux-courses/system-administration-training/kubernetes-fundamentals), and [certification](https://www.cncf.io/announcement/2016/11/08/cloud-native-computing-foundation-launches-certification-training-managed-service-provider-program-kubernetes/)
+ Manages a software conformance [working group](https://ponymail.cncf.io/thread.html/Zaw9xi4cg7fx9v6)
+ Actively markets Kubernetes
+ Hosts and funds developer marketing activities like [K8Sport](http://k8sport.org/)
+ Supports ad hoc activities, like offering a neutral [k8s AMI](https://lists.cncf.io/mailman/listinfo/cncf-images) in the AWS Marketplace
+ Funds conferences and meetup events.

## Knowledge Check
Q1. What is Kubernetes licensed under? Select the correct answer.

    A. GPLv2
    B. MIT
    C. Apache License Version 2.0
    D. None of the above

    Ans: c

Q2. In which programming language is Kubernetes written? Select the correct answer.

    A. Python
    B. C++
    C. Java
    D. Go

    Ans: d

Q3. Which of the following are features of Kubernetes?

    A. Self-healing
    B. Batch execution
    C. Secrets and configuration management
    D. Horizontal scaling

    Ans: a, b, c, d

