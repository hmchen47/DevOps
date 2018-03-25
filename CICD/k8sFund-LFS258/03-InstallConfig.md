Installation and Configuration
==============================

## 3.1 Installation and Configuration

## 3.2 Introduction
[Video][vid]

[vid]: https://lms.quickstart.com/custom/858487/media/Installation%20and%20Configuration.mp4

## 3.3 Learning Objectives
+ Download installation and configuration tools
+ Install a Kubernetes master and grow a cluster
+ Configure a network solution for secure communications
+ Discuss highly-available deployment considerations

## 3.4 Installation Tools
Choice of installation:
+ Google Container Engine (GKE):
    + a cloud service from the Google Cloud Platform
    + allow request a Kubernetes cluster with the latest stable version
+ Minikube:
    + a single binary to deploy into Oracle VirtualBox
    + local and single node to provide platform for learning, testing, and development

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
    + another way to create a Kubernetes cluster on AWS
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
+ Context:
    + a combination of a cluster and user credentials
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

## 3.7 Using Minikube
+ an open source project within the GitHub [Kubernetes organization](https://github.com/kubernetes/minikube)
+ Download minikube
    ```bash
    $ curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.22.2/minikube-linux-amd64
    $ chmod +x minikube
    $ sudo mv minikube /usr/local/bin
    ```
+ Starting Kubernetes on local machine
    ```bash
    $ minikube start
    $ kubectl get nodes
    ```
    + start a VirtualBox virtual machine that will contain a single node Kubernetes deployment and the Docker engine
    + run all the components of Kubernetes together
+ The minikube VM also runs Dockers, in order to run containers


## 3.8 Installing with `kubeadm`
+ The most straightforward method to start building a real cluster
+ Appear in Kubernetes v1.4.0 and bootstrap a cluster quickly
+ [Documentation](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/) on the Kubernetes website
+ Package repositories available for Ubuntu 16.04 and CentOS 7.1
+ Procedures:
    + `kubeadm init`: run on the head node and token returned
    + Create a network for IP-per-Pod criteria:
        ```bash
        kubeadm join --token token head-node-IP
        ```
    + Alternatively create the network with `kubectl`, by using a resource manifest of the network
+ To use the Weave network
    ```bash
    $ kubectl create -f https://git.io/weave-kube
    ```
+ Once these steps completed, a functional multi-node Kubernetes cluster, and able to use `kubectl` to interact with

## 3.9 Installing a Pod Network
Pod networking choices - varying levels of development and feature set
+ __Calico__ (https://www.projectcalico.org//)
    + A flat L3 network which communicates w/o IP encapsulation
    + used in production with software such as __Kubernetes__, __OpenShift__, __Docker__, __Mesos__ and __OpenStack__
    + Viewed as simple and flexible networking model
    + Scale well for large environment
    + Other options: __Canal__ allows for integration with __Flannel__, allowing for implementation of network policies
+ __Flannel__ (https://github.com/coreos/flannel)
    + A L3 IPv4 network btw the nodes of the a cluster
    + Developed by __CoreOS__, a long history with Kubernetes
    + Focused on traffic btw hosts, not how containers configure local networking
    + Using one of several backend mechanism, such as VXLAN
    + A flannel agent on each node allocates subnet leases for the host
    + While it can be configured after deployment, it is much easier prior to any Pods being added.
+ __Kube-router__ (https://github.com/cloudnativelabs/kube-router)
    + Feature-filled single binary claimed to "do it all"
    + Project in alpha stage
    + promise to offer a distributed load balancer, firewall, and reouter purposely built for Kubernetes
+ __Romana__ (https://github.com/romana/romana)
    + Aimning at network and security automation for cloud native applications
    + Aiming at large cluster, IPAM-aware topology and integration with __kops__ cluster
+ __Weave Net__ (https://www.weave.works/oss/net/)
    + used as an add-on for a CNI-enabled Kubernetes

Container Network Interface (CNI)
+ a CNCF project
+ used by several container runtimes
+ a standard to handle deployment management and cleanup of network resources

## 3.10 More Installation Tools
+ Kubernetes installe don a server
+ configuration management systems: Chef, Puppet, Ansible, Terraform
+ Installation tools
    + __kubespray__
        + in the Kubernetes incubator
        + an advanced __Ansible__ playbook to setup a Kubernetes cluster on various OSes and use different providers
        + known as __kargo__
    + __kops__: a command line to create a Kubernetes cluster on AWS 
    + __kube-aws__: a command line making use of the AWS Cloud Formation to provide a Kubernetes cluster on AWS
    + __kubeicorn__
        + a tool to leverage the use of Kubeadm to build a cluster
        + no dependency on DNS
        + running on several OSes
        + using snapshot to capture a cluster and move it
+ Best practice to install Kubernetes: [step-by-step manual commands](https://github.com/kelseyhightower/kubernetes-the-hard-way)

## 3.11 Installation Considerations
+ Start experimenting with a single-mode deployment
    + Run all the Kubernetes components: API server, controller, scheduler, kubelet, and kube-proxy
    + e.g. Minikube
+ Consideration to deploy on a cluster of servers (physical or virtual)
    + Which provider should I use? A public or private cloud? Physical or virtual?
    + Which operating system should use? Kubernetes runs on most operating systems (e.g. Debian, Ubuntu, CentOS, etc.), plus on container-optimized OSes (e.g. CoreOS, Atomic)
    + Which networking solution should I use? Do I need an overlay?
    + Where should I run my `etcd` cluster?
    + Can I configure Highly Available (HA) head nodes?
+ How to chhose the best option: [Picking the Right Solution](https://kubernetes.io/docs/setup/pick-right-solution/)
+ With `systemd` becoming the dominant `init` system on Linux, Kubernetes components will end up being as _systemd unit files_ in most cases. Or, they will be run via a kubelet running on the head node (i.e. `kubeadm`)

## 3.12 Main Deployment Configurations
+ High level main deployment configurations:
    + Single-node
    + Single head node, multiple workers
    + Multiple head nodes with HA, multiple workers
    + HA `etcd`, HA head nodes, multiple workers
+ Choice of option: depend on how advanced in Kubernetes journey and golas
+ Single-node deployment:
    + all components run on the same server
    + great for testing, learning, and developing around Kubernetes
+ Single head node and multiple workers
    + a single node `etcd` instance running on the head node with the API, the scheduler, and the controller-manager
+ Multiple head nodes and multiple worker nodes
    + Head nodes in an HA configuration
    + Worker nodes add more durability to the cluster
    + The API server will be fronted by a load balancer, the scheduler and the controller-manager
    + Controller-manager elected a leader via flags
    + `etcd` setup can still be single node
+ HA `etcd`, HA head nodes, and multiple workers
    + The most advanced and resilient setup
    + `etcd` runs as a true cluster to provide HA and run on nodes separate from the Kubernetes head nodes
+ Kubernetes Federation
    + high availability
    + multiple clusters joined together with a common control panel
    + allowing movement of resources from one cluster to another administratively or after failure

## 3.13 Systemd Unit File for Kubernetes
+ A simple `systemd` unit file to run the `controller-manager`
    ```yaml
    -name: kube-controller-manager.service
        command: start
        content:
            [Unit]
            Description=Kubernetes Controller Manager
    Documentation=http://github.com/kubernetes/kubernetes
        Requires=kube-apiserver.service
        After=kube-apiserver.service
        [Service]
        ExecStartPre=/usr/bin/curl -Lo /opt/bin/kube-controller-manager -z \
        /opt/bin/kube-controller-manager \
        https://storage.googleapis.com/kubernetes-release/release/v1.7.6/bin/linux/amd64/kube-controller-manager
        ExecStartPre=/opt/bin/chmod +x /opt/bin/kube-controller-manager
        ExecStartPre=/opt/bin/kube-controller-manager \
        --service-account-private-key-file=/opt/bin/kube-serviceaccount.key \
        --root-ca-file=/var/run/kubernetes/apiserver.crt \
        --master=127.0.0.1:8080 \
        --logtostderr=true
        Restart=always
        RestartSec=10
    ```
    + Not a perfect unit file.
    + Download the controller binaryans set a few flags to run
+ Reference Documentation of the API Server: [`kube-apiserver`](https://kubernetes.io/docs/reference/generated/kube-apiserver/)

## 3.14 Using Hyperkube
+ `kubeadm`: run the API server, the scheduler, and the controller-manger as container while running all the componentsas regular system daemons in unit files
+ `hyperkube`:
    + a handy all-in-one binary
    + available as a container image
    + e.g. gcr.io/google_containers/hyperkube:v1.9.2
+ Installation with `kubelet` under `hyperkube`:
    + run as a system daemon
    + config to read in manifests that specify how to run te other components, including the API server, the scheduler, etcd, the controller
    + monitor and restart if needed
+ Demo: download `hyperkube` image and run a container
    ```bash
    $ docker run --rm gcr.io/google_containers/hyperkube:v.1.9.2 /hyperkube apiserver --help
    $ docker run --rm gcr.io/google_containers/hyperkube:v.1.9.2 /hyperkube scheduler --help
    $ docker run --rm gcr.io/google_containers/hyperkube:v.1.9.2 /hyperkube controller-manager --help
    ```
+ Best practice to learn the various configuration flags


