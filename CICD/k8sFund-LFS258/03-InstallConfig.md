# Installation and Configuration

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

+ Choice of installation:
    + Google Container Engine (GKE):
        + a cloud service from the Google Cloud Platform
        + allow request a Kubernetes cluster with the latest stable version
    + Minikube:
        + a single binary to deploy into Oracle VirtualBox
        + local and single node to provide platform for learning, testing, and development
+ Tools:
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
    + pass these parameters on the command line, or switch the shell between contexts with a command:

        ```bash
        $ kubectl config use-context foobar
        ```

## 3.6 Using Google Kubernetes Engine (GKE)

+ To use GKE
    + account on [Google Cloud](https://cloud.google.com/)
    + method of payment for the services you will use
    + the `gcloud` command line client
+ Methods of installation
    + [Interactive installer](https://cloud.google.com/sdk/downloads#linux)
    + [GKE quickstart guide](https://cloud.google.com/kubernetes-engine/docs/quickstart)
+ To create Kubernetes cluster

    ```bash
    $ gcloud container clusters create linuxfoundation
    $ gcloud container cluster list
    $ kubectl get nodes
    ```

    + by installing `gcloud`, `kubectl` installed automatically
    + commands create the cluster, install it, and the, listed the nodes of the cluster with `kubectl`
+ To delete Kubernetes cluster

    ```bash
    $ gcloud container clusters delete linuxfoundation
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
+ The `minikube` VM also runs Dockers, in order to run containers

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

+ Pod networking choices - varying levels of development and feature set
    + [__Calico__](https://www.projectcalico.org)
        + A flat L3 network which communicates w/o IP encapsulation
        + used in production with software such as __Kubernetes__, __OpenShift__, __Docker__, __Mesos__ and __OpenStack__
        + Viewed as simple and flexible networking model
        + Scale well for large environment
        + Other options: __Canal__ allows for integration with __Flannel__, allowing for implementation of network policies
    + [__Flannel__](https://github.com/coreos/flannel)
        + A L3 IPv4 network btw the nodes of the a cluster
        + Developed by __CoreOS__, a long history with Kubernetes
        + Focused on traffic btw hosts, not how containers configure local networking
        + Using one of several backend mechanism, such as VXLAN
        + A flannel agent on each node allocates subnet leases for the host
        + While it can be configured after deployment, it is much easier prior to any Pods being added.
    + [__Kube-router__](https://github.com/cloudnativelabs/kube-router)
        + Feature-filled single binary claimed to "do it all"
        + Project in alpha stage
        + promise to offer a distributed load balancer, firewall, and router purposely built for Kubernetes
    + [__Romana__](https://github.com/romana/romana)
        + Aiming at network and security automation for cloud native applications
        + Aiming at large cluster, IPAM-aware topology and integration with __kops__ cluster
    + [__Weave Net__](https://www.weave.works/oss/net/)
        + used as an add-on for a CNI-enabled Kubernetes
+ Container Network Interface (CNI)
    + a CNCF project
    + used by several container runtimes
    + a standard to handle deployment management and cleanup of network resources

## 3.10 More Installation Tools

+ Kubernetes installed on a server
+ configuration management systems: __Chef__, __Puppet__, __Ansible__, __Terraform__
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
+ How to chose the best option: [Picking the Right Solution](https://kubernetes.io/docs/setup/pick-right-solution/)
+ With `systemd` becoming the dominant `init` system on Linux, Kubernetes components will end up being as _systemd unit files_ in most cases. Or, they will be run via a kubelet running on the head node (i.e. `kubeadm`)

## 3.12 Main Deployment Configurations

+ High level main deployment configurations:
    + Single-node
    + Single head node, multiple workers
    + Multiple head nodes with HA, multiple workers
    + HA `etcd`, HA head nodes, multiple workers
+ Choice of option: depend on how advanced in Kubernetes journey and goals
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
    + Download the controller binary and set a few flags to run
+ Reference Documentation of the API Server: [`kube-apiserver`](https://kubernetes.io/docs/reference/generated/kube-apiserver/)

## 3.14 Using Hyperkube

+ `kubeadm`: run the API server, the scheduler, and the controller-manger as container while running all the components as regular system daemons in unit files
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

## 3.15 Compiling from Source

+ The list of binary releases on [GitHub](https://github.com/kubernetes/kubernetes/releases) - other scenarios to get start with K8s , except for `gcloud`, `minikube`, and `kubeadmin`
+ Compile from source files with Makefile by cloning from GitHub
    + Build with __Golang__: download Golang from [here](https://golang.org/doc/install)

        ```bash
        $ cd $GOPATH
        $ git clone https://github.com/kubernetes/kubernetes
        $ cd kubernetes
        $ make
        ```

    + Build on [Docker host](https://docs.docker.com/install/) containing Golang
        + clone the repository anywhere and run `make quick-release`
        + built binary located in `_output/bin` 

## 3.16 Lab 3.1 - Install Kubernetes

### Overview

+ Learn to use `kubeadm`
+ Lab based on Ubuntu instance on Google Cloud Platform (GCP)
+ Able to run on AWS, local machine, or inside of a virtualization
    + Local machine: `sudo` enabled
    + AWS, GCP: ssh client or Putty
    + Require `.pem` or `.ppk` file to access nodes
+ Install Kubernetes on a single node, and then grow cluster
+ Recommend resources: 2vCPUs, 7.5G memory
+ Exercise files in YAML provided, but encourage to write your own
+ Download YAML files in compress tar file by visiting `https://training.linuxfoundation.org/cm/LFS258/` with user: `LFtraining` and password: `Penguin2014`
+ Alternatively, download and expand the tart file

    ```bash
    $ wget \
    https://training.linuxfoundation.org/cm/LFS258/LFS258_V2018-01-16_SOLUTIONS.tar.bz2 \
    --user=LFtraining --password=Penguin2014
    $ tar -xvf LFS258_V2018-01-16_SOLUTIONS.tar.bz2
    ```

## Install Kubernetes

1. Open a terminal session on your first node. E.g. connect to GCP node with ssh client or Putty.

    ```bash
    [student@laptop ~]$ ssh -i LFS458.pem student@35.226.100.87
    The authenticity of host '54.214.214.156 (35.226.100.87)' can't be established.
    ECDSA key fingerprint is SHA256:IPvznbkx93/Wc+ACwXrCcDDgvBwmvEXC9vmYhk2Wo1E.
    ECDSA key fingerprint is MD5:d8:c9:4b:b0:b0:82:d3:95:08:08:4a:74:1b:f6:e1:9f.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added '35.226.100.87' (ECDSA) to the list of known hosts.
    <output_omitted>
    ```

2. Become as `root` and update and upgrade teh system

    ```bash
    $ sudo -i
    [sudo] password for <username>:
    # apt-get update && apt-get upgrade -y
    <output_ommitted>
    ```

3. __Docker__ and __CoreOS Rocket - rkt__ are main choices for a container environment. __Docker__ is used here while __rkt__ requires a fair amount of extra work to enable for Kubernetes.

    ```bash
    # apt install -y docker.io
    <output_omitted>
    ```

4. Add new repo for kubernetes. Create the file and add an entry for the main repo.

    ```bash
    # vim /etc/apt/sources.list.d/kubernetes.list
    deb http://apt.kubernetes.io/ kubernetes-xenial main
    ```

5. Add a GCP key for the packages.

    ```bash
    # curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    OK
    ```

    OpenGPG might need to install before the above command working. Based on the instruction from [Using PGP](https://nsrc.org/workshops/2014/btnog/raw-attachment/wiki/Track3Agenda/2-1-1.pgp-lab.html)

    ```bash
    # apt-get install gnupg
    # apt-get install rng-tools
    # sed -i -e 's|#HRNGDEVICE=/dev/hwrng|HRNGDEVICE=/dev/urandom|' /etc/default/rng-tools
    # service rng-tools start
    ```

6. Update teh new repo.

    ```bash
    # apt update
    <output_omitted>
    ```

7. Install the software with the newest release.

    ```bash
    # apt install -y kubeadm kubectl
    <output_omitted>
    ```

    Historically, nre version have a lots of change and a chance of bugs. For specific version installation, follow the command

    ```bash
    # apt install -y kubeadm=1.9.1-00 kubelet=1.9.1-00
    <output_omitted>
    ```

8. Network Configuration

    + The expected demands of the cluster will be the main concern for decision on Container Network Interface (CNI) for pod network.
    + There can be only one pod network per cluster, though the CNI-Genie project is trying to change this.
    + Types of communications: container-to-container, pod-to-pod, pod-to-service, and external-to-service
    + Docker uses host-private networking
      + `docker0` virtual bridge
      + `vteth` interfaces on that host
    + __Flannel__ mained by CoreOS, Prohject Calico, OVN, Contrails
    + Download Flannel and Calico

    ```bash
    $ wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
    ```

9. Review the network settings and configurations.  Decide the network address that Flannel will expect and be used for Master Node.

    ```bash 
    # less kube-flannel.yml
    <output_omitted>
    # grep Network kube-flannel.ym
      "Network": "10.244.0.0/16",
      hostNetwork: true
    ```

  10. Calico Use Only, Not Flannel

    + Download the [configuration file][calio] for Calico
    + Check the expected IP range for container (different from Flannel)

    ```bash
    # wget https://goo.gl/eWLkzb -O calico.yaml
    # less calico.yaml
    ...
      # Configure the IP Pool from which Pod IPs will be chosen.
        - name: CALICO_IPV4POOL_CIDR
          value: "192.168.0.0/16"
    ...
    ```

11. Initialize the master

    + Read through the output carefully.
    + The provided output is in beta, therefore, some differences are expected.
    + The final portion is the direction to run as a non-root user with token provided.
    + The token info can be obtained with `kubeadm token list` command.
    + The output also instruct how to create a pod network to the cluster, see step 12.
    + The network settings for Flannel also listed.

    ```bash
    # exit
    logout
    $ sudo kubeadm init --pod-network-cidr 10.244.0.0/16
    [kubeadm] WARNING: kubeadm is in beta, please do not use it for production clusters.
    [init] Using Kubernetes version: v1.9.1
    [init] Using Authorization modes: [Node RBAC]
    [preflight] Running pre-flight checks

    <output-omitted>

    Your Kubernetes master has initialized successfully!

    To start using your cluster, you need to run (as a regular user):
      mkdir -p $HOME/.kube
      sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
      sudo chown $(id -u):$(id -g) $HOME/.kube/config

    You should now deploy a pod network to the cluster.
    Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
      http://kubernetes.io/docs/admin/addons/

    You can now join any number of machines by running the following on each node
    as root:
      kubeadm join --token 563c3c.9c978c8c0e5fbbe4 10.128.0.3:6443
      --discovery-token-ca-cert-hash sha256:726e98586a8d12d428c0ee46
      cbea90c094b8a78cb272917e2681f7b75abf875f
    ```

  Output messages after the command executed

  ```
  [preflight] Running pre-flight checks.
    [WARNING FileExisting-crictl]: crictl not found in system path
  [preflight] Some fatal errors occurred:
    [ERROR Swap]: running with swap on is not supported. Please disable swap
  [preflight] If you know what you are doing, you can make a check non-fatal with `--ignore-preflight-errors=...`
  ```

  + Additional software to prevent `[WARNING FileExisting-crictl]` with the [cri-tools](https://github.com/kubernetes-incubator/cri-tools/releases) repo on github
  + Install Go Language and execute `go get github.com/kubernetes-incubator/cri-tools/cmd/crictl` with root/sudo, then copy `crictl` to `/usr/bin`
  + `[ERROR Swap]`: see [ref](https://github.com/kubernetes/kubeadm/issues/610) to turn off swap with `swapoff -a`

  ```
  [preflight] Some fatal errors occurred:
    [ERROR CRI]: unable to check if the container runtime at "/var/run/dockershim.sock" is running: exit status 1
    [preflight] If you know what you are doing, you can make a check non-fatal with `--ignore-preflight-errors=...`
  ```

  + Please refer to GibHub [issue ##657](https://github.com/kubernetes/kubeadm/issues/657) with the flag `--ignore-preflight-errors=cri`

  ```bash
  $ sudo kubeadm init --ignore-preflight-errors=cri --pod-network-cidr 10.244.0.0/16
  [init] Using Kubernetes version: v1.9.6
  [init] Using Authorization modes: [Node RBAC]
  [preflight] Running pre-flight checks.
    [WARNING CRI]: unable to check if the container runtime at "/var/run/dockershim.sock" is running: exit status 1
  [certificates] Generated ca certificate and key.
  [certificates] Generated apiserver certificate and key.
  [certificates] apiserver serving cert is signed for DNS names [prj kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 10.0.2.15]
  [certificates] Generated apiserver-kubelet-client certificate and key.
  [certificates] Generated sa key and public key.
  [certificates] Generated front-proxy-ca certificate and key.
  [certificates] Generated front-proxy-client certificate and key.
  [certificates] Valid certificates and keys now exist in "/etc/kubernetes/pki"
  [kubeconfig] Wrote KubeConfig file to disk: "admin.conf"
  [kubeconfig] Wrote KubeConfig file to disk: "kubelet.conf"
  [kubeconfig] Wrote KubeConfig file to disk: "controller-manager.conf"
  [kubeconfig] Wrote KubeConfig file to disk: "scheduler.conf"
  [controlplane] Wrote Static Pod manifest for component kube-apiserver to "/etc/kubernetes/manifests/kube-apiserver.yaml"
  [controlplane] Wrote Static Pod manifest for component kube-controller-manager to "/etc/kubernetes/manifests/kube-controller-manager.yaml"
  [controlplane] Wrote Static Pod manifest for component kube-scheduler to "/etc/kubernetes/manifests/kube-scheduler.yaml"
  [etcd] Wrote Static Pod manifest for a local etcd instance to "/etc/kubernetes/manifests/etcd.yaml"
  [init] Waiting for the kubelet to boot up the control plane as Static Pods from directory "/etc/kubernetes/manifests".
  [init] This might take a minute or longer if the control plane images have to be pulled.
  [apiclient] All control plane components are healthy after 53.501839 seconds
  [uploadconfig] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
  [markmaster] Will mark node prj as master by adding a label and a taint
  [markmaster] Master prj tainted and labelled with key/value: node-role.kubernetes.io/master=""
  [bootstraptoken] Using token: ba3edb.1b9344bf6ce19d91
  [bootstraptoken] Configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
  [bootstraptoken] Configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
  [bootstraptoken] Configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
  [bootstraptoken] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
  [addons] Applied essential addon: kube-dns
  [addons] Applied essential addon: kube-proxy

  Your Kubernetes master has initialized successfully!

  To start using your cluster, you need to run the following as a regular user:

    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

  You should now deploy a pod network to the cluster.
  Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
    https://kubernetes.io/docs/concepts/cluster-administration/addons/

  You can now join any number of machines by running the following on each node
  as root:

    kubeadm join --token ba3edb.1b9344bf6ce19d91 10.0.2.15:6443 --discovery-token-ca-cert-hash sha256:34e555e3f502b0b0aa0786ea841fa8b62daa66569863d62adc34f8e72dc3da41
  ```

12. Follow the direction to allo a non-root user access to the cluster.

    ```bash
    # exit
    logout
    $ mkdir -p $HOME/.kube
    $ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    $ sudo chown $(id -u):$(id -g) $HOME/.kube/config
    $ less .kube/config
    apiVersion: v1
    clusters:
    - cluster:
    <output_omitted>
    ```

13. Apply the configuration to cluster.

    + Copy the config file to the non-root user directory.
    + Verify the new flannel interface
    ```bash
    $ sudo cp /root/kube-flannel.yml ./
    $ kubectl apply -f kube-flannel.yml
    clusterrole "flannel" created
    clusterrolebinding "flannel" created
    serviceaccount "flannel" created
    configmap "kube-flannel-cfg" created
    daemonset "kube-flannel-ds" created

    $ ip a
    <output_omitted>
    4: flannel.1: <BROADCAST,MULTICAST> mtu 8951 qdisc noop state DOWN group default
        link/ether 32:44:47:b7:78:85 brd ff:ff:ff:ff:ff:ff
    ```

14. Verify the available nodes of the cluster.

    + It may take 1~2 min to change from NotReady to Ready.
    + The `NAME` field can be used to check the details.
    ```bash
    $ kubectl get node
    NAME              STATUS  AGE VERSION
    lfs458-node-1a0a  Ready   1m  v1.9.1
    ```

    Actual output:
    ```
    NAME      STATUS    ROLES     AGE       VERSION
    prj       Ready     master    2h        v1.9.6
    ```

15. Check the details of the node.

    + Work line by line to check the resource and their current status.
    + Status `Taints`: The master won't allow pods by default for security reason.
    + Status `False`: Read through each line to find the error

    ```bash
    $ kubectl describe node <name>
    Name: lfs458-node-1a0a
    Role:
    Labels: beta.kubernetes.io/arch=amd64
    beta.kubernetes.io/os=linux
    kubernetes.io/hostname=lfs458-node-1a0a
    node-role.kubernetes.io/master=
    Annotations: node.alpha.kubernetes.io/ttl=0
    volumes.kubernetes.io/controller-managed-attach-detach=true
    Taints: node-role.kubernetes.io/master:NoSchedule
    <output_omitted>
    ```

16. Determine if the DNS and flannel ready for use. Status shows `Running`, it might take 1~2 min to transitition from `Pending`.

    ```bash
    $ kubectl get pods --all-namespaces
    NAMESPACE   NAME                                      READY STATUS  RESTARTS AGE
    kube-system etcd-lfs458-node-1a0a                     1/1   Running 0        12m
    kube-system kube-apiserver-lfs458-node-1a0a           1/1   Running 0        12m
    kube-system kube-controller-manager-lfs458-node-1a0a  1/1   Running 0        12m
    kube-system kube-dns-2425271678-w80vx                 3/3   Running 0        13m
    kube-system kube-flannel-ds-wj92l                     1/1   Running 0        1m
    kube-system kube-proxy-5st9z                          1/1   Running 0        13m
    kube-system kube-scheduler-lfs458-node-1a0a           1/1   Running 0        12m
    ```

17. Allow the master to run other pods.  Note: minus sign `-` is the syntax to remove a taint.

    ```bash
    $ kubectl taint nodes --all node-role.kubernetes.io/master-
    node "lfs458-node-1a0a" untainted
    $ kubectl describe node <name> | grep -i taint
    Taints: <none>
    ```

18. Enable `bash` auto-completion for `kubectl` with long node name.

    ```bash
    $ source <(kubectl completion bash)
    $ echo "source <(kubectl completion bash)" >> ~/.bashrc
    ```

19. Verify auto-completion with 3-letter node name.

    ```bash
    $ kubectl des<Tab> n<Tab><Tab> <name>-<Tab>
    ```

+ [Lab 3.1 - PDF](https://lms.quickstart.com/custom/858487/LAB_3.1.pdf)

[calio]: https://docs.projectcalico.org/v2.6/getting-started/kubernetes/installation/hosted/kubeadm/1.6/calico.yaml

## 3.17 Lab 3.2 - Grow the Cluster

1. (Workers) Connect to second node and setup as master node.

    ```bash
    $ sudo -i
    # apt update && apt upgrade -y
    # apt install -y docker.io
    # vim /etc/apt/sources.list.d/kubernetes.list
    deb http://apt.kubernetes.io/ kubernetes-xenial main
    # curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    # apt update
    # apt install -y kubeadm kubectl
    ```

2. (Master) Find the IP address of the master node.  The interface name depends on the where the node is running.  E.g. the primary interface of the node type inside GCP is `ens4`.

    ```bash
    $ ip addr show ens4
        inet 10.128.0.3/32 brd 10.128.0.3 scope global ens4
        inet6 fe80::4001:aff:fe8e:2/64 scope link
    ```

3. (Master) Find the token on the master node.

    + The token last for 24 hrs by default.
    + Generate new token with the `sudo kubeadm token create`

    ```bash
    student@lfs458-node-1a0a:~$ sudo kubeadm token list
    TOKEN                   TTL EXPIRES     USAGES      DESCRIPTION
    27eee4.6e66ff60318da929 23h 2017-11-03T13:27:33Z
    authentication,signing The default bootstrap token generated
    by 'kubeadm init'....
    ```

4. (Master) Starting from v1.9, create and use the Discovery Token CA Cert Hash, created from the master to ensue the node joins the cluster in a secure manner. Run this command on the master node to create one.

    ```bash
    $ openssl x509  -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa \
                    -pubin -outform der 2>/dev/null | openssl dgst \
                    -sha256 -hex | sed 's/^.* //'
    6d541678b05652e1fa5d43908e75e67376e994c3483d6683f2a18673e5d2a1b0
    ```
5. (Workers) Join the cluster from the second node.

    + Use the generated token and hash
    + Use the private IP address of the master node and port `6443`
    
    ```bash
    # kubeadm join \
        --token 27eee4.6e66ff60318da929 10.128.0.3:6443  --discovery-token-ca-cert-hash \
        sha256:6d541678b05652e1fa5d43908e75e67376e994c3483d6683f2a18673e5d2a1b0
    [preflight] Running pre-flight checks.
    [WARNING FileExisting-crictl]: crictl not found in system path
    [discovery] Trying to connect to API Server "10.142.0.2:6443"
    [discovery] Created cluster-info discovery client, requesting info from
    "https://10.142.0.2:6443"
    [discovery] Requesting info from "https://10.142.0.2:6443" again to
    validate TLS against the pinned public key
    [discovery] Cluster info signature and contents are valid and TLS
    certificate validates against pinned roots, will
    use API Server "10.142.0.2:6443"
    [discovery] Successfully established connection with API Server
    "10.142.0.2:6443"
    This node has joined the cluster:
    * Certificate signing request was sent to master and a response
    was received.
    * The Kubelet was informed of the new secure connection details.
    Run 'kubectl get nodes' on the master to see this node join the cluster.
    ```

    Whe doing lab, the command issues instead:

    ```bash
    # kubeadm join --ignore-preflight-errors=cri --token 44d148.2a750f5fe1f90105 10.0.2.15:6443 \
        --discovery-token-ca-cert-hash sha256:34e555e3f502b0b0aa0786ea841fa8b62daa66569863d62adc34f8e72dc3da41
    [preflight] Running pre-flight checks.
    [WARNING Service-Docker]: docker service is not enabled, please run 'systemctl enable docker.service'
    [WARNING FileExisting-crictl]: crictl not found in system path
    [discovery] Trying to connect to API Server "10.0.2.15:6443"
    [discovery] Created cluster-info discovery client, requesting info from "https://10.0.2.15:6443"
    [discovery] Failed to request cluster info, will try again: [Get https://10.0.2.15:6443/api/v1/namespaces/kube-public/configmaps/cluster-info: dial tcp 10.0.2.15:6443: getsockopt: connection refused]
    [discovery] Failed to request cluster info, will try again: [Get https://10.0.2.15:6443/api/v1/namespaces/kube-public/configmaps/cluster-info: dial tcp 10.0.2.15:6443: getsockopt: connection refused]
    ```

6. (Workers) Try to run the `kubectl` command. 

    + Failed
    + No authentication in local `~/.kube/config` file

    ```bash
    # exit 
    $ kubectl get nodes
    The connection to the server localhost:8080 was refused
    - did you specify the right host or port?

    $ ls -l ~/.kube
    ```

7. (Master) Verify the node has joined the cluster. It might take a few minutes to show `Ready` state.

    ```bash
    $ kubectl get nodes
    ```

8. (Master) Display the current namespace configured on tyhe cluster.

    ```bash
    $ kubectl get namespace
    ```

9. (Master & Worker) Display the network interfaces

    ```bash
    $ ip a
    ```

10. (Master) Verify the deployment with the following command.

    ```bash 
    $ kubectl run nginx --image nginx
    ```

11. (Master) Display the details of the deployment.

    ```bash
    $ kubectl describe deployment nginx
    ```

12. (Master) Display the basic stepsthe cluster took in order to pull and deploy the new application. [About 10 long lines of output]

    ```bash
    kubectl get events
    ```

13. (Master) Display the output in YAML format.

    + The output can used to create the deployment or new deployment
    + Middle of the file shows the status info of the current deployment

    ```bash
    $ kubectl get deployment nginx -o yaml
    ```

14. (Master) Revise the YAML file.

    + Run command again and redirect the output to a file
    + Edit the file 
        + remove lines with `creationTimestamps`, `resourceVersion`, `selfLink` and `uid`
        + remove all the lines including and after `status:`
    
    ```bash
    $ kubectl get deployment nginx -o yaml > first.yml
    $ vim first.yml
    ```

15. (Master) Delete the existing deployment

    ```bash
    $ kubectl delete deployment nginx
    ```

16. (Master) Create deployment with edited file

    ```bash
    $ kubectl create -f first.yml
    ```

17. (Master) Compare the current deployment and first deployment.

    + Run the command again and redirect to YAML file
    + The `time stamp`, `resource version` and `uid` are generated for each resource generated
    + They will cause conflicts or false information
    + `status` should not be hard-coded as well

    ```bash
    $ kubectl get deployment nginx 0o > second.yml
    $ diff first.yml second.yml
    ```
18. (Master) Show the help output to view examples

    + __nginx__ container is a light weight web server
    + Create a `service` to view the default welcome page
    + Middle of output provides several examples

    ```bash
    $ kubectl expose -h
    ```

19. (Master) Gain access to the web server

    ```bash
    $ kubectl expose deployment/nginx
    ```

20. (Master) Explore configuration file

    + Change an existing configuration in a cluster: `kubectl` sub-commands
        + `apply`: a three-way diff of previous, current, and supplied input to determine modifications to make; changes not mentioned are unaffected
        + `edit`: perform a get, open an editor, then an apply
        + `patch`: update API objects in place with JSON patch and merge patch or strategic merge patch functionality
    + `kubectl replace --force`: disruptive update if configuration w/ resource field not able to update once initialized
    + Edit the first deployment YAML file with port 80

    ```yaml
    .
        spec:
          containers:
          - image: nginx
            imagePullPolicy: Always
            name: nginx
            ports:                      # Add these
            - containerPort: 80         # three
              protocol: TCP             # lines
            resources: {}
    .
    ```

21. (Master) Apply the changes to the running deployment. Warning message might show.

    ```bash
    $ kubectl apply -f first.yml
    ```

22. (Master) View the Pod and Deployment.

    ```bash
    $ kubectl get deploy pod
    ```

23. (Master) Try to expose the resource again.

    ```bash
    $ kubectl expose deployment.nginx
    ```

24. (Master) Verify the service configuration

    + Check the service info first, then the endpoint info
    + the Cluster IP != current endpoint
    + Note down the current endpoint IP, e.g. 10.244.1.99:80 in this example

    ```bash
    $ kubectl get svc nginx
    NAME CLUSTER-IP     EXTERNAL-IP PORT(S) AGE
    nginx 10.100.61.122 <none>      80/TCP  3m

    $ kubectl get ep nginx
    NAME    ENDPOINTS       AGE
    nginx   10.244.1.99:80  4m
    ```

25. (Master & Workers) Determine which node the container running.

    + Log into Worker node nad use `tcpdump` to view traffic on `flannel.1` interface
    + Leave the command running while `curl` requests
    + Check the `tcpdump` output, including `HTTP: HTTP/1.1 200 OK` and `ack` response

    ```bash
    (Master) $ kubectl describe pod nginx-7cbc4b4d9x-d27xw | grep Node:
    
    (Worker) $ sudo tcpdump -i flannel.1
    ```

26. (Master) Verify by accessing to the Cluster IP, port 80.

    + View the generic `nginx` and working page
    + The address: `ENDPOINT` IP address
    + If the `curl` command times out, the pod may be running on the other node
    + Run same command on that node

    ```bash
    $ curl 10.100.61.122:80
    ```

27. (Workers & Workers) Verify with different network interfaces

    + Run `tcpdump` on different terminal with different interface
    
    ```bash
    $ sudo tcpdump cni0
    $ sudo tcpdump vethfa2c0158
    ```

28. (Master) Scale up the deployment from 1 to 3 erb servers

    ```bash
    $ kubectl get deployment nginx
    $ kubectl scale deployment nginx --replicas=3
    $ kubectl get deployment nginx
    ```

29. (Master) Verify the current endpoint.

    ```bash
    $ kubectl get ep nginx
    ```

30. (Master) Delete the oldest pod of the nginx deployment and delete it.

    + Use the `AGE` field to determine the oldest pod
    + Observe the terminals with `tcpdump` running

    ```bash
    $ kubectl get po -o wide
    $ kubectl delete po nginx-<id>
    ```

31. (Master) Observer the web server again.

    + List the containers running
    + One should be newer than the others.
    + If the `tcpdump` was using `veth` interface of that container, it will error out.

    ```bash
    $ kubectl gte pod
    ```

32. (Master) Observe the endpoint again.

    + The original endpoint IP is no longer in use.
    + Delete any of the pods
    + The service will forward traffic to the existing backend pods.

    ```bash
    $ kubectl get ep nginx
    ```

33. (Master) Verify by accessing the web server again w/ the ClusterIP addr ans any endpoint IP address.

    ```bash
    $ curl 10.100.61.122:80
    ```

+ [Vab 3.2 - PDF](https://lms.quickstart.com/custom/858487/LAB_3.2.pdf)

## 3.18 Lab 3.3 - Access from Outside the Cluster

[Lab 3.3 - PDF](https://lms.quickstart.com/custom/858487/LAB_3.3.pdf)

## 3.19 Knowledge Check

Q1. What is the `kubeadm` command used for? Select the correct answer.

    a. Assign an administrator to the cluster
    b. Start a new Pod
    c. Create a cluster and add nodes
    d. All of the above

    Ans: c

Q2. Which of the following is the main binary for working with objects for a Kubernetes cluster? Select the correct answer.

    a. OpenStack
    b. Make
    c. adminCreate
    d. kubectl

    Ans: d

Q3. How many pod networks can you have per cluster? Select the correct answer.

    a. 1
    b. 2
    c. 3
    d. 4

    Ans: a

Q4. The `~/.kube/config` file contains ____. Select teh correct answer.

    a. Endpoints
    b. SSL keys
    c. Contexts
    d. All of the above

    Ans: d
