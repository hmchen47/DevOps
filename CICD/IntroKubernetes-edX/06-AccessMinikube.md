Accessing Minikube
==================

## Introduction
In this chapter, we will study the different access methods to any Kubernetes cluster. We will use __kubectl__ to access Minikube via CLI, the Kubernetes dashboard to access it via GUI, and the curl command, with the right credentials to access it via APIs.

## Learning Objectives
Review methods to access any Kubernetes cluster.
Configure __kubectl__ for Linux, macOS, and Windows.
Access the minikube dashboard.
Access minikube via APIs.

## Accessing Minikube
Any healthy running Kubernetes cluster can be accessed via one of the following methods:

+ __Command Line Interface (CLI)__

    __kubectl__ is the CLI tool to manage the Kubernetes cluster resources and applications. In later chapters, we will be using __kubectl__ to deploy the applications and manage the Kubernetes resources.
+ __Graphical User Interface (GUI)__

    The Kubernetes dashboard provides the GUI to interact with its resources and containerized applications. In one of the later chapters, we will be using it to deploy a containerized application.
+ __APIs__

    As we know, Kubernetes has the API Server, and operators/users connect to it from the external world to interact with the cluster. Using both CLI and GUI, we can connect to the API Server on the Master Node to perform different operations. We can directly connect to the API Server using its API endpoints and send commands to it, as long as we can access the Master Node and have the right credentials.

The methods we just outlined are applicable to all Kubernetes clusters. Next, we will see how we can access the minikube environment we set up in the previous chapter.

## kubectl
__kubectl__ is generally installed before installing minikube, but we can also install it later. There are different methods that can be used to install __kubectl__, which are mentioned in the [Kubernetes Documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl/). Next, we will look at the steps to install __kubectl__ on Linux, macOS, and Windows systems.

## Installing kubectl on Linux
To install __kubectl__ on Linux, follow the instructions below:

+ Download the latest stable __kubectl__ binary

    `$ curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl`

+ Make the __kubectl__ binary executable

    `$ chmod +x ./kubectl`

+ Move the __kubectl__ binary to the `PATH`

    `$ sudo mv ./kubectl /usr/local/bin/kubectl`

## Installing kubectl on macOS
There are two ways to install __kubectl__ on macOS: manually and using the Homebrew package manager. Next, we will provide instructions for both methods.

To manually install __kubectl__ on macOS, follow the instructions below:

+ Download the latest stable __kubectl__ binary

    `$ curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl`

+ Make the __kubectl__ binary executable

    `$ chmod +x ./kubectl`

+ Move the __kubectl__ binary to the PATH

    `$ sudo mv ./kubectl /usr/local/bin/kubectl`

To install __kubectl__ on macOS using the Homebrew package manager, do:

`$ brew install kubectl`

## Installing kubectl on Windows
To install __kubectl__ on Windows, follow the steps below:

+ Get the latest __kubectl__ release from [here](https://storage.googleapis.com/kubernetes-release/release/stable.txt)
+ Depending on the latest release, download the __kubectl__ binary. In the example below, we are downloading the v1.6.3 release

    `$ curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.6.3/bin/windows/amd64/kubectl.exe`

+ Once downloaded, move the __kubectl__ binary to the `PATH`.

## kubectl Configuration File
To connect to the Kubernetes cluster, __kubectl__ needs the Master Node endpoint and the credentials to connect to it. While starting minikube, the startup process creates, by default, a configuration file, `config`, inside the `.kube` directory, which resides in user's `home` directory.  That configuration file has all the connection details. By default, the __kubectl__ binary accesses this file to find the Master Node's connection endpoint, along with the credentials. To look at the connection details, we can either see the content of the `~/.kube/config(Linux)` file, or run the following command:

```bash
$ kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /Users/nkhare/.minikube/ca.crt
    server: https://192.168.99.100:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /Users/nkhare/.minikube/apiserver.crt
    client-key: /Users/nkhare/.minikube/apiserver.key
```
Once __kubectl__ is installed, we can get information about the minikube cluster with the `kubectl cluster-info` command: 

```bash
$ kubectl cluster-info
Kubernetes master is running at https://192.168.99.100:8443
```
To further debug and diagnose cluster problems, use `kubectl cluster-info dump`.

You can find more details about the kubectl command line options [here](https://kubernetes.io/docs/user-guide/kubectl-overview/).

## Using the 'minikube dashboard' Command
As mentioned earlier, the [Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/) provides the user interface for the Kubernetes cluster. To access the Dashboard of Minikube, we can use `minikube dashboard`, which would open a new tab on our web browser, displaying the Kubernetes dashboard:

`$ minikube dashboard`

![Kubernetes dashboard](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c135ecab3d99d7749a14098bc3825609/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/Kubernetes_Dashboard.png)

## Using the 'kubectl proxy' Command
Using the `kubectl proxy` command, __kubectl__ would authenticate with the API Server on the Master Node and would make the dashboard available on `http://localhost:8001/ui`.

```bash
$ kubectl proxy
Starting to serve on 127.0.0.1:8001
```
After running the above command, we can access the dashboard at http://127.0.0.1:8001/ui.

![Accessing the Kubernetes dashboard](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/2a773ae5f9dc188f071cc7c68e9545f4/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/Acessing_the_Kubernetes_Dashboar_2.png)

## APIs - with 'kubectl proxy'
When __kubectl__ proxy is configured, we can send requests to localhost on the proxy port:

```bash
$ curl http://localhost:8001/
{
  "paths": [
    "/api",
    "/api/v1",
    "/apis",
    "/apis/apps",
    ......
    ......
    "/logs",
    "/metrics",
    "/swaggerapi/",
    "/ui/",
    "/version"
  ]
}%
```
With the above curl request, we requested all the API endpoints from the API Server.

## Accessing the Kubernetes Cluster Demo
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://youtu.be/SQ_kTmgiVKQ)


## Knowledge Check
Q1. How can we access the cluster? Select the correct answer.

    A. Via APIs
    B. Via GUI
    C. Via CLI
    D. All of the above

    Ans: D

Q2. While starting minikube, a configuration file, 'config', gets created by default inside what directory on Linux? Select the correct answer.

    A. /tmp
    B. /home/user/.kube
    C. /root
    D. /home/user

    Ans: B

Q3. Which of the following commands do we use to open up a proxy port on localhost for the Kubernetes cluster? Select the correct answer.

    A. kubectl create
    B. kubectl proxy
    C. kubectl localhost
    D. kubectl proxy create

    Ans: B

