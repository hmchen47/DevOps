Installing Kubernetes
=====================

## Introduction
In this chapter, we will first discuss about the different configurations in which Kubernetes can be installed. We will then discuss about the infrastructure requirements to install Kubernetes, and we will also look at some of the tools which can help us with the installation. 

## Learning Objectives
By the end of this chapter you will be able to:

+ Discuss about the different Kubernetes configuration options.
+ Discuss infrastructure considerations before installing Kubernetes.
+ Discuss infrastructure choices for a Kubernetes deployment.
+ Review Kubernetes installation tools and resources.

## Kubernetes Configuration
Kubernetes can be installed using different configurations. The four major installation types are briefly presented below:

+ __All-in-One Single-Node Installation__

    With All-in-One, all the Master and Worker components are installed on a single node. This is very useful for learning, development, and testing. This type should not be used in production. Minikube is one such example, and we are going to explore it in future chapters.

+ __Single-Node etcd, Single-Master, and Multi-Worker Installation__

    In this setup, we will have a single Master Node, which will also run a single-node etcd instance. Multiple Worker Nodes are connected to the Master Node.

+ __Single-Node etcd, Multi-Master, and Multi-Worker Installation__

    In this setup, we will have multiple Master Nodes, which will work in HA mode, but we will have a single-node etcd instance. Multiple Worker Nodes are connected to the Master Nodes.

+ __Multi-Node etcd, Multi-Master, and Multi-Worker Installation__

    In this mode, etcd is configured in a clustered mode, outside the Kubernetes cluster, and the Nodes connect to it. The Master Nodes are all configured in an HA mode, connecting to multiple Worker Nodes. This is the most advanced and recommended production setup.

## Infrastructure for Kubernetes Installation
Once we decide on the installation type, we also need to make some infrastructure-related decisions, such as:

+ Should we set up Kubernetes on bare-metal, public cloud, or private cloud?
+ Which underlying system should we use? Should we choose RHEL, CoreOS, CentOS, or something else?
+ Which networking solution should we use?
+ And so on.

The Kubernetes documentation has details in regards to [choosing the right solution](https://kubernetes.io/docs/setup/pick-right-solution/). Next, we will take a closer look at these solutions.

## Localhost Installation
There are a few localhost installation options available to deploy single- or multi-node Kubernetes clusters on our workstation/laptop:

+ [Minikube](https://kubernetes.io/docs/getting-started-guides/minikube/)
+ [Ubuntu on LXD](https://kubernetes.io/docs/getting-started-guides/ubuntu/local/).

Minikube is the preferred and recommended way to create an all-in-one Kubernetes setup. We will be using it extensively in this course.

## On-Premise Installation
Kubernetes can be installed on-premise on VMs and Bare Metal.

__On-Premise VMs__

    Kubernetes can be installed on VMs created via Vagrant, VMware vSphere, KVM, etc. There are different tools available to automate the installation, like Ansible or kubeadm.

__On-Premise Bare Metal__

    Kubernetes can be installed on on-premise Bare Metal, on top of different Operating Systems, like RHEL, CoreOS, CentOS, Fedora, Ubuntu, etc. Most of the tools used to install VMs can be used with Bare Metal as well. 

## Cloud Installation
Kubernetes can be installed and managed on almost any Cloud environment.

### Hosted Solutions
With Hosted Solutions, any given software is completely managed by the provider. The user will just need to pay hosting and management charges. Some examples of vendors providing Hosted Solutions for Kubernetes are listed below:

+ [Google Container Engine (GKE)](https://cloud.google.com/container-engine/)
+ [Azure Container Service](https://azure.microsoft.com/en-us/services/container-service/)
+ [OpenShift Dedicated](https://www.openshift.com/dedicated/)
+ [Platform9](https://platform9.com/support/kubernetes-at-the-command-line-up-and-running-with-kubectl/)
+ [IBM Bluemix Container Service.](https://console.ng.bluemix.net/docs/containers/container_index.html)

### Turnkey Cloud Solutions
With Turnkey Cloud Solutions, we can deploy a solution or software with just a few commands. For Kubernetes, we have some Turnkey Cloud Solutions, with which Kubernetes can be installed with just a few commands on an underlying IaaS platform, such as:

+ [Google Compute Engine](https://kubernetes.io/docs/getting-started-guides/gce/)
+ [Amazon AWS](https://kubernetes.io/docs/getting-started-guides/aws/)
+ [Microsoft Azure](https://kubernetes.io/docs/getting-started-guides/azure/)
+ [Tectonic by CoreOS](https://coreos.com/tectonic)

### Bare Metal
Kubernetes can be installed on Bare Metal provided by different cloud providers.

## Kubernetes Installation Tools/Resources
While discussing installation configuration and the underlying infrastructure, let's take a look at some useful tools/resources available:

+ __kubeadm__

    [kubeadm](https://github.com/kubernetes/kubeadm) is a first-class citizen on the Kubernetes ecosystem. It is a secure and recommended way to bootstrap the Kubernetes cluster. It has a set of building blocks to setup the cluster, but it is easily extendable to add more functionality. Please note that kubeadm does not support the provisioning of machines.

+ __Kubespray__

    With [Kubespray](https://github.com/kubernetes-incubator/kubespray) (formerly known as Kargo), we can install Highly Available Kubernetes clusters on AWS, GCE, Azure, OpenStack, or Bare Metal. Kubespray is based on Ansible, and is available on most Linux distributions. It is a [Kubernetes Incubator](https://github.com/kubernetes-incubator/kargo) project.

+ __Kops__

    With [Kops](https://github.com/kubernetes/kops), we can create, destroy, upgrade, and maintain production-grade, highly-available Kubernetes clusters from the command line. It can provision the machines as well. Currently, AWS is officially supported. Support for GCE and VMware vSphere are in alpha stage, and other platforms are planned for the future.

If the existing solutions and tools do not fit your requirements, then you [can always install Kubernetes from scratch](https://kubernetes.io/docs/getting-started-guides/scratch/).

It is worth checking out the [Kubernetes The Hard Way]() GitHub project by [Kelsey Hightower](https://twitter.com/kelseyhightower), which shares the manual steps involved in bootstrapping a Kubernetes cluster

## Knowledge Check
Which of the following is a valid Kubernetes configuration? Select all answers that apply.

    A. All-in-One Kubernetes Installation
    B. Single Master (with etcd) and Multi-Worker Nodes
    C. External etcd Cluster, Single Master and Multi-Worker Nodes
    D. External etcd Cluster, Multi-Master and Multi-Worker Nodes

    Ans: a, b, c, d

Q2. Which of the following are Kubernetes hosted solutions? Select all answers that apply.

    A. Google Compute Engine
    B. Google Container Engine
    C. Openshift Dedicated
    D. Amazon ECS

    Ans: b, c


Q3. Which of the following are Kubernetes installation tools? Select all answers that apply.

    A. kops
    B. kubeadm
    C. kubespray (formerly known as kargo)
    D. None of the above

    Ans: a, b, c


