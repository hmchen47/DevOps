Installation and Configuration
==============================

## 3.1 Installation and Configuration

## 3.2 Introduction
[Video][vid]

[vid]: https://lms.quickstart.com/custom/858487/media/Installation%20and%20Configuration.mp4

## 3.3 Learning Objectives
+ Download instalaltion and configuration tools
+ Install a Kubernetes master and grow a cluster
+ Configure a network solution for secure communications
+ Discuss highly-available deployment considerations

## 3.4 Installation Tools
Choice of instalaltion:
+ Google Container Engine (GKE): 
    + a cloud service from the Google Cloud Platform
    + allow reuest a Kubernetes cluster with the latest stable version
+ Minikube: 
    + a single binary to deploy into Oracle VirtualBox
    + local and single node to provide platfoem for learning, testing, and development

Tools:
+ __`kubectl`__
    + the Kubernetes command line interface
    + run on local machine and target the API server endpoint
    + create, manage, and delete all Kubernetes resources (e.g. Pods, Deployments, Services)
+ __`kubeadm`__
    + a newer tool that makes installing Kubernetes easy and avoids vendor-specific installers
    + `kubeadm init`: run on Master Node
    + `kubeadm join`: run on Worker Nodes and cluster bootstraps itself
    + allow Kubernetes to be deployed in a number of places, where AWS uses  this method in this course
+ __`kubespray`__ or __`kops`__
    + another way to create a Kubernrtes cluster on AWS
    + create `systemd` unit file in a very traditional way
+ __hyperkube__
    + use a container image
    + contain all the key Kubernetes binaries
    + run a Kubernetes cluster by just starting a few containers on nodes

