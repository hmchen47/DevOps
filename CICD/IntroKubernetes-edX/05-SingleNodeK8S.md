Setting Up a Single-Node Kubernetes Cluster with Minikube
=========================================================

# Introduction
As we mentioned in the previous chapter, [Minikube](https://github.com/kubernetes/minikube) is the easiest and most recommended way to run an All-in-One Kubernetes cluster locally. In this chapter, we will check out the requirements to install Minikube on our workstation, as well as the installation instructions to set it up on Linux, Mac and Windows. 

# Learning Objectives
By the end of this chapter you will be able to:

+ Discuss Minikube.
+ Install Minikube on Linux, Mac, and Windows.
+ Verify the installation.

# Requirements for Running Minikube
Minikube runs as a VM. Therefore, we need to make sure that we have the supported hardware and the hypervisor to create VMs. Next, we outline the requirements to run Minikube on our workstation/laptop:

+ [__kubectl__](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

    __kubectl__ is a binary to access any Kubernetes cluster. Generally, it is installed before starting minikube, but we can install it later, as well. If __kubectl__ is not found while installing minikube, we will get a warning message, which can be safely ignored (just remember that we will have to install __kubectl__ later). We will explore __kubectl__ in future chapters.

+ _On macOS

    [xhyve driver](https://github.com/kubernetes/minikube/blob/master/docs/drivers.md#xhyve-driver), [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or [VMware Fusion](http://www.vmware.com/products/fusion.html) hypervisors

+ On Linux

    [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or [KVM](https://github.com/kubernetes/minikube/blob/master/docs/drivers.md#kvm-driver) hypervisors

+ On Windows

    [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or [Hyper-V](https://github.com/kubernetes/minikube/blob/master/docs/drivers.md#hyperV-driver) hypervisors

+ VT-x/AMD-v virtualization must be enabled in BIOS
+ Internet connection on first run.

In the chapter, we will use VirtualBox as hypervisor on all three operating systems - Linux, macOS, and Windows, to create the Minikube VM. 

# Installing Minikube on Linux
Next, we will learn how to install minikube on Linux (Ubuntu 16.04):

+ __Install the hypervisor (VirtualBox), if you haven't done so already__

    ```bash
    $ sudo apt-get install virtualbox
    ```

+ __Install minikube__

    We can download the latest release from the minikube release page. Once downloaded, we need to make it executable and copy it in the PATH:

    ```bash
    $ curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.20.0/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
    ```

+ __Start minikube__
    We can start minikube with the `minikube start` command:

    ```bash
    $ minikube start
    Starting local Kubernetes v1.6.4 cluster...
    Starting VM...
    Moving files into cluster...
    Setting up certs...
    Starting cluster components...
    Connecting to cluster...
    Setting up kubeconfig...
    Kubectl is now configured to use the cluster.
    ```

+ __Check the status__

    With the `minikube status` command, we can see the status of minikube:

    ```bash
    $ minikube status
    minikube: Running
    localkube: Running
    kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100
    ```
+ __Stop minikube__

    With the `minikube stop` command, we can stop minikube:

    ```bash
    $ minikube stop
    Stoppin
    ```

# Installing Minikube on macOS
On macOS, Minikube uses __VirtualBox as the default hypervisor__, which we will use as well. But, if you would like to use the __xhyve__ hypervisor to start Minikube VM, then, while starting, you will need to pass the `--vm-driver=xhyve`

Next, we will learn how to install minikube on macOS

+ __Install [VirtualBox](http://download.virtualbox.org/virtualbox/5.1.22/VirtualBox-5.1.22-115126-OSX.dmg) on macOS.__
+ __Install minikube __

    We can download the latest release from the `minikube release` page. Once downloaded, we need to make it executable and copy it in the `PATH`.

    ```bash
    $ curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.20.0/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
    ```

+ __Start minikube__

    We can start minikube with the `minikube start` command:

    ```bash
    $ minikube start
    Starting local Kubernetes v1.6.4 cluster...
    Starting VM...
    Downloading Minikube ISO
    90.95 MB / 90.95 MB [==============================================] 100.00% 0s
    Moving files into cluster...
    Setting up certs...
    Starting cluster components...
    Connecting to cluster...
    Setting up kubeconfig...
    Kubectl is now configured to use the cluster.
    ```

+ __Check the status__

    We can see the status of minikube with the `minikube status` command:

    ```bash
    $ minikube status
    minikube: Running
    localkube: Running
    kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.10
    ```

+ __Stop minikube__

    We can stop minikube with the `minikube stop` command:

    ```bash
    $ minikube stop
    Stopping local Kubernetes cluster...
    Machine stopped.
    ```

# Installing Minikube on Windows
We will be using VirtualBox as the hypervisor to create the minikube VM. Make sure Hyper-V is disabled while running VirtualBox. 

Please note that Windows support is currently in the experimental phase, and you might encounter issues during installation. 

Following are the instructions to install minikube on Windows 10: 

+ Install [VirtualBox](http://download.virtualbox.org/virtualbox/5.1.22/VirtualBox-5.1.22-115126-Win.exe)
+ Go to the [minikube release page](https://github.com/kubernetes/minikube/releases)
+ Download the [minikube binary](https://github.com/kubernetes/minikube/releases/download/v0.20.0/minikube-windows-amd64.exe) from the _Distribution_ section
+ Add the downloaded minikube binary to your `PATH`
+ Download [kubectl](https://storage.googleapis.com/kubernetes-release/release/v1.6.3/bin/windows/amd64/kubectl.exe) and add it to your `PATH` 
+ __Start minikube__

    ```bash
    $ minikube start --vm-driver=virtualbox

    Starting local Kubernetes v1.6.4 cluster
    Starting VM...
    Downloading Minikube ISO
    90.95 MB / 90.95 MB [==============================================] 100.00% 0s
    Moving files into cluster...
    Setting up certs...
    Starting cluster components...
    Connecting to cluster...
    Setting up kubeconfig...
    Kubectl is now configured to use the cluster.
    ```

    With the `--vm-driver=virtualbox` option, we are suggesting `minikube` to choose VirtualBox as a hypervisor to create the virtual machine.

+ __Check the status__

    We can see the status of minikube with the `minikube status` command:

    ```bash
    $ minikube status
    minikube: Running
    localkube: Running
    kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100
    ```

+ __Stop minikube__

    ```bash
    $ minikube stop
    Stopping local Kubernetes cluster...
    Machine stopped.
    ```

# Installing Minikube Demo

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)][vid1]

[vid1]: https://youtu.be/5g73AH0TJZU

# Knowledge Check
Q1. What can we do with minikube? Select the correct answer.

    A. Set up an All-in-One Kubernetes cluster on our workstation
    B. Set up a multi-node cluster
    C. Set-up and etcd cluster
    D. None of the above

    Ans: a

Q2. On which of the following systems can minikube be installed on? Select the correct answer.

    A. Linux
    B. Windows
    C. macOS
    D. All of the above

    Ans: d

Q3. When started for the first time, minikube requires Internet access. 

    Ans: true
