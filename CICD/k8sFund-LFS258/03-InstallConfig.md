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

## 3.5 Installing `kubectl`
+ Configure and Manage cluster: `kubectl`, __RESTful__ calls or __Go__ Language
+ RHEL 7/CentOS 7: `kubectl` in `kubernetes-client` package
+ download [here](https://github.com/kubernetes/kubernetes/tree/master/pkg/kubectl), then compile and install `kubectl` 
+ configuration file: ~/.kube/config
    + containing all the Kubernetes endpoints that might use
    + including cluster definitions (.i.e. IP endpoints), credentials, and contexts
+ context:
    + a combinationof a cluster a d user credentials
    + pass these parameters on the command line, or switch the shell between contexts with a command: `$ kubectl config use-context foobar`

## 3.6 Using Google Kubernetes Engine (GKE)
+ To use GKE
    + account on [Google Cloud](https://cloud.google.com/)
    + method of payment for the services you will use
    + the `gcloud` command line client
+ Methods of installation 
    + [document](https://cloud.google.com/sdk/downloads#linux)
    + [GKE quickstart guide](https://cloud.google.com/kubernetes-engine/docs/quickstart)
+ To create Kubernetes cluster
    ```bash
    $ gcloud container clusters create linuxfundation
    $ gcloud container cluster list
    $ kubectl get nodes
    ```
    + by installing `gcloud`, `kubectl` insalled automatically
    + commands create the cluster, install it, and the, listed the nodes of the cluster with `kubectl`
+ To delete Kubernetes cluster
    ```bash
    $gcloud container clusters delete linuxfoundation
    ```


