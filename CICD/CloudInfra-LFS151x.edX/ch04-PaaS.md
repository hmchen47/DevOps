# Chapter 4. Platform as a Service (PaaS)

## Introduction and Learning Objectives
### Platform as a Service
__Platform as a Service (PaaS)__ is a class of Cloud Computing services which allows its users to develop, run, and manage applications without worrying about the underlying infrastructure. With __PaaS__, users can simply focus on building their applications, which is a great help to developers.

We can either use __PaaS__ services offered by different cloud computing providers like __Amazon, Google, Azure__, etc., or deploy it on-premise, using software like __OpenShift Origin, Deis__, etc.

__PaaS__ can be deployed on top of __IaaS__, or, independently on VMs, bare-metal, and Containers.

In this chapter, we will take a closer look at some of the __PaaS__ providers and their features. We will also provide a demo video for each one of them.

### Learning Objectives
By the end of this chapter you should be able to:

+ Explain the concept of __Platform as a Service (PaaS)__.
+ Distinguish between different __PaaS__ providers.
+ Deploy an application on top of different __PaaS__ providers: __Cloud Foundry, OpenShift, Heroku, Deis__.


## Cloud Foundry
### Introduction to Cloud Foundry
[Cloud Foundry][cf] is an Open Source platform as a service (__PaaS__) that provides a choice of clouds, developer frameworks, and application services. It can be deployed on-premise or on __IaaS__, like __AWS, vSphere__, or __OpenStack__. There are many commercial [CF cloud providers][cfcp] as well, like __HPE Helion Cloud Foundry, IBM Bluemix, Pivotal Cloud Foundry__, etc.

### Features
Among the characteristics employed by __Cloud Foundry__ are the following:

+ Application portability
+ Application auto-scaling
+ Centralized platform management
+ Dynamic routing
+ Role-based application deployment
+ Horizontal and vertical scaling
+ Application health management
+ Centralized logging
+ Security
+ Support for different __IaaS__ technologies.

### Cloud Foundry Subsystems
__Cloud Foundry (CF)__ has three major subsystems:

+ [__Bosh__][bosh]

    __CF__ runs on top of VMs from existing __IaaS__ like __AWS, vSphere__, or __OpenStack__. It uses two kinds of VMs:

    - _Component VMs_: They run all the different components of __CF__ to provide different __PaaS__ functionalities.
    - _Application VMs_: They run _Garden_ containers, inside which the application is deployed.

    __Bosh__ provides the system orchestration to configure VMs into well-defined state-through-manifest files. __Bosh__ runs on top of existing __IaaS__ to provision VMs automatically. Then, using the manifest files, it configures __CF__ on them.

+ __Cloud Controller__ 

    It runs the applications and other processes on provisioned VMs. It also manages the life-cycle and demand of applications.

+ __(Go) Router__ 
    
    It routes the incoming traffic to the Cloud Controller or the application.

### Buildpacks
__CF__ uses __buildpacks__, which provide the framework and runtime support for the applications. They are programming language-specific and have information about how to download dependencies and configure specific applications. Below are some of the languages for which we have well-defined __buildpacks__:

+ Java
+ Python
+ GO
+ Ruby
+ PHP
+ Node.js
+ .Net

Custom buildpacks can also be created. When an application is pushed to __CF__, it automatically detects the required buildpack and installs it on the __Droplet Execution Agent (DEA)__, where the application needs to run. A droplet contains an OS-specific pre-built root-filesystem called __stack__, a buildpack and source-code of the application. A _droplet_ is then given to the application VM (__Diego Cell__), which unpacks, compiles, and runs it. The application runs a container using the [Garden runtime][garden].

__CF__ also supports running __Docker__ images, but it uses the __Garden__ runtime to run them.

### Cloud Foundry Components
The following diagram describes the components of __Cloud Foundry__:

![image][img1]

Figure 4.1: Cloud Foundry Components (by [Cloud Foundry Foundation][cff], retrieved from cloudfoundry.org)

Below we will provide details about each component:

+ __Routing__ 

    The __Router__ is part of this component, which routes the incoming traffic to the Cloud Controller or the application.

+ __Authentication__ 

    __OAuth2 Server (UAA)__ and __Login Server__ are part of this component and provide identity management.

+ __APP Lifecycle__ 

    As the name suggests, this component manages the application lifecycle. It has the following elements:

    - _Cloud Controller_: A developer connects to the _Cloud Controller (CC)_ to push the application deployment. It then directs to the _Diego Brain_ to fulfill the request. It also manages organizations, spaces, user roles, services, and more.
    - _Diego Brain_: It coordinates with an individual _Diego Cell_ to stage and deploy the application.
    - _nsync, Converger_, and _Cell Reps_: They make sure the expected state and count of the individual application is met. They can start or stop processes to reach to desired state.
    
+ __App Storage and Execution__

    It has the following elements: 
    - _Blob Store_: It stores large binary files, like application code packages, buildpacks and droplets.
    - _Diego Cell_: Every application VM runs a _Diego Cell_, which runs the application using _Garden_ containers. It also reports the application status and other data to the __BBS (Bulletin Board System)__ and __Loggregator__.

+ __Services__ 

    Generally, applications depend on services such as databases. The service brokers make sure the service on which an application depends is always available.

+ __Messaging__

    Component VMs communicate with each other internally through HTTP/HTTPS protocols. The _Consul server_   stores long-lived control data, such as component IP addresses. The __Bulletin Board System (BBS)__ stores frequently updated and disposable data, such as the application status and heartbeat messages.

+ __Metrics & Logging__ 

    The _Metrics Collector_ collects metrics and statistics from the __CF__ components. The _Loggregator_    (Log aggregator system) transmits application logs to developers.

### Demo
In the following video we will show how you can deploy an application on Cloud Foundry.

[video][vid1]

### Benefits of Using Cloud Foundry
Some of the benefits of using __Cloud Foundry__ are:

+ It is an Open Source platform, but there are also many commercial __Cloud Foundry__ providers. 
+ It offers centralized platform management.
+ It enables horizontal and vertical scaling.
+ It provides infrastructure security.
+ It provides multi-tenant compute efficiency.
+ It offers support for multiple __IaaS__ providers.
+ It supports the full lifecycle: development, testing, and deployment, thus enabling a continuous delivery strategy. It also provides integration with CI/CD tools.
+ It is a simple and flexible solution, supported by an extensive community of developers.
+ It reduces the chance of human errors.
+ It is cost-effective, reducing the overhead for Ops teams. 

### References
+ https://www.cloudfoundry.org/
+ https://docs.cloudfoundry.org/


## OpenShift
### Introduction to OpenShift
[OpenShift][os] is an Open Source __PaaS__ solution provided by __Red Hat__. The latest release of __OpenShift__, __OpenShift v3__, is built on top of the container technology, which uses __Docker__ and __Kubernetes__ underneath. __OpenShift v3__ can be deployed on top of a full-fledged __Linux OS__ or on a Micro OS which is specifically designed to run containers and __Kubernetes__. Currently, it is supported only on the __Atomic Host__ Micro OS and its variants.

__Red Hat__ offers three different plans for __OpenShift__:

+ __OpenShift Online__ 
    
    With the Online plan, you can deploy your applications on the __OpenShift Cluster__ managed by __Red Hat__ and pay as per your usage.

+ __OpenShift Dedicated__ 

    With the Dedicated plan, you can get your own dedicated __OpenShift Cluster__, which is managed by __Red Hat__.

+ __OpenShift Enterprise__
    
    With the Enterprise plan, you can create your own private __PaaS__ on your hardware.

All the upstream development on OpenShift happens on [GitHub][ghos] and it is referred to as [OpenShift Origin][oso].

### Features
With __OpenShift v3__, we can deploy any application which is running with __Docker__ containers.

As __OpenShift v3__ uses __Kubernetes__, we get all the features offered by __Kubernetes__, like adding or removing nodes at runtime, persistent storage, auto-scaling, etc.

__OpenShift v3__ has a framework called _Source to Image (S2I)_, which enables us to create __Docker__ images from the source code repository to deploy applications easily.

__OpenShift v3__ integrates well with Continuous Deployment tools to deploy applications as part of the CI/CD pipeline.

With the _Dedicated_ or _Enterprise_ plans you get a GUI to manage projects, users, access, etc.

### Installing OpenShift
You do not have to worry about the installation if you opt for the _Online_ or _Dedicated_ plans, as the __Red Hat__ engineering or support team will assist you with it. As announced in January of 2016, __Google__ and __Red Hat__ will be working closely to integrate and deliver __OpenShift Dedicated__ on the Google Cloud Platform.

Detailed instructions for installing __OpenShift v3__ are given in the [documentation][osdoc].

### Demo
In the following demo we will illustrate how you  can deploy an application in the __OpenShift__ environment. 

[video][vid2]

### Benefits of Using OpenShift
Some of the benefits of using __OpenShift__ are:

+ It is an Open Source __PaaS__ solution.
+ It uses __Docker__ and __Kubernetes__ underneath for deployment.
+ It provides integration with CI/CD tools.
+ It is a simple and flexible solution, supported by an active community of developers.
+ It enables developers to be more efficient and productive, allowing them to quickly develop, host, and scale applications in the Cloud in a streamlined and standardized manner.
+ It enables application portability, meaning that any application created on __OpenShift__ can run on any platform that supports __Docker__.
+ __OpenShift__ users have the choice to deploy their applications on top of different infrastructures (physical or virtual; public, private or hybrid).

### References
+ https://www.openshift.com/
+ https://github.com/openshift/origin


## The Heroku Platform
### Introduction to Heroku
[Heroku][heroku] is a fully-managed container-based cloud platform, with integrated data services and a strong ecosystem. __Heroku__ is used to deploy and run modern applications. It is a [Salesforce][salesf] company.

__Heroku__ has multiple products but, at its core, it has the __Heroku Platform__, which is a __PaaS__ platform used to deploy applications. The __Heroku Platform__ supports the following languages:

+ Node.js
+ Ruby
+ Python
+ Go
+ PHP
+ Clojure
+ Scala
+ Java,

but it can be easily extended to other languages.

### Heroku Core Concepts
The __Heroku__-centric development and deployment workflow needs to be followed if you want to use it. This workflow is very developer-friendly. Let's take a look at some of its core concepts next:

+ Applications should contain the source code, its dependency information and the list of named commands to be executed to deploy it, in a file called [`Procfile`][procf].
+ For each supported language, it has a pre-built image, which contains a compiler for that language. This pre-built image is referred to as a [buildpack][buip]. [More than one buildpacks][mbuip] can be used together. We can also create a custom buildpack as well.
+ While deploying, we need to send the application's content to __Heroku__, either via __Git, GitHub, Dropbox__ or via an API. Once the application is received by __Heroku__, a buildpack is selected based on the language of preference.
+ To create the runtime which is ready for execution, we compile the application after fetching its dependency and configuration variables on the selected buildpack. This runtime is often referred to as a __slug__.
+ We can also use third party [add-ons][addon] to get access to value-added services like logging, caching, monitoring, etc.
+ A combination of _slug, configuration variables_, and _add-ons_ is referred to as a __release__, on which we can perform upgrade or rollback.
+ Depending on the process-type declaration in the `Procfile`, a virtualized __UNIX__ container is created to serve the process in an isolated environment, which can be scaled up or down, based on the requirements. Each virtualized __UNIX__ container is referred to as a __Dyno__. Each _dyno_ gets its own ephemeral storage.
+ __Dyno Manager__ manages  across all applications running on __Heroku__.

### Features
Individual components of an application can be scaled up or down using _dynos_.

It is a very rich ecosystem, and it allows us to extend the functionality of an application with [add-ons][addon]. Add-ons allow us to easily integrate our applications with other fully-managed cloud services like database, logging, email, etc.

Applications can be easily integrated with __Salesforce__.


### Demo
In the following video we will show how you can deploy a sample application on the __Heroku__ platform.

[video][vid3]

### Benefits of Using Heroku
Some of the benefits of using the __Heroku__ platform are:

+ It enables a development-friendly workflow.
+ It provides a rich ecosystem, allowing to extend the functionality through add-ons.
+ It supports Continuous Integration and Deployment.
+ It is easy to start and allows us to quickly scale our applications, both horizontally and vertically. 
+ It provides the ability to do automated backups.

### References
+ https://www.heroku.com
+ https://elements.heroku.com/addons


## Deis
### Introduction to Deis
__Deis__ (pronounced DAY-iss) is an Open Source __PaaS__ platform, which runs on top of __Docker__ and [__CoreOS__][core].

### The Underlying Technology
#### Docker

__Docker__ is the container runtime used by __Deis__ to run applications. For more information on __Docker__ and containers, please refer to Chapter 5 (Containers). 

#### CoreOS

__CoreOS__ is a lightweight OS to run just containers. We will learn about it in Chapter 6 (Micro OSes for Containers). As of now, __CoreOS__ supports __Docker__ and __rkt__ as container runtime. __Deis__ supports __Docker__ for the time being.

### The System Architecture of Deis
The diagram below illustrates the System Architecture of __Deis__, which showcases three major components:

![image][img2]

Figure 4.2: The System Architecture of Deis (by [Engine Yard][eng], retrieved from [deis.io][deisio])

#### The Control Plane

It performs all management tasks, including the container scheduling. It has a blob of storage called __Store__, which is created from a containerized __Ceph__ cluster. The __Store__ is used to hold:

+ Docker images and configuration data
+ Platform state
+ Logs from the data plane.

End users interact with the __Control Plane__ using __DEIS__ APIs. Users also reach to the __Control Plane__ when they run the `git push` command.

#### The Data Plane

The __Data Plane__ is where all the containers would run. It connects the application containers with the __Router Mesh__ and sends the container logs to the __Control Plane__.

#### The Router Mesh

The __Router Mesh__ connects end users to the application containers. Each router in the mesh can load balance an application running on the __Data Plane__.

### Features
Next, we will mention some of the most important features for __Deis__:

+ It can deploy any applications written in any language or framework.
+ It is 100% Open Source.
+ It can be deployed on-premise or on any cloud provider.
+ It scales the application and the underlying nodes in the cluster effortlessly.

### Installing Deis
__Deis__ can be installed on any system that supports __CoreOS__. It can be installed on VMs, bare-metal, and most of the cloud providers, like __Amazon AWS, Google Compute Engine, Microsoft Azure, OpenStack__, etc.

Detailed instructions for each of the installation type is given in its documentation. Please refer to it to setup your environment.

After doing the installation, we can list the machines in the cluster with the following command:
```bash
$ deisctl machines 
MACHINE        IP        METADATA
000e3c13...    172.17.8.100    controlPlane=true,dataPlane=true,routerMesh=true
97c77e60...    172.17.8.101    controlPlane=true,dataPlane=true,routerMesh=true
cff57996...    172.17.8.102    controlPlane=true,dataPlane=true,routerMesh=true
```

In the above example, each of the machines is part of the Control Plane, the Data Plane, and the Router Mesh. In larger deployments, we can have different components running on different machines. __Etcd__, which is a distributed key-value pair, can also run in a separate environment and we can just refer to it from __Deis__.

Once the __Deis__ platform is ready, we can interact with the __Deis__ _Controller_ from the [Deis client][deisclt]. To install it on __Linux__ or __Mac OS X__, run the following commands:
```bash
$ curl -sSL http://deis.io/deis-cli/install.sh | sh
$ ln -fs $PWD/deis /usr/local/bin/deis
```
After setting up the __Deis CLI__, we need to [register a user][usrreg] to the _Controller_ and add the SSH public keys for the user.

### Deploying an Application
__Deis__ can deploy any application that can run inside a __Docker__ container. In order to scale horizontally, applications must follow the [12-factor methodology][12fac] and store the state in external backing services.

__Docker__ images can be either downloaded from a __Docker__ Registry or can be built from a `Dockerfile`. Deis can deploy applications from __Docker__ images or `Dockerfiles`.

Other than __Docker__, __Deis__ also supports deploying applications using the [Heroku Buildpacks][buip]. __Heroku__ buildpacks support most of the languages, like __Ruby, Python, Node.js, Java, Clojure, Scala, Play, PHP, Perl, Dart__, and __Go__. After processing the buildpack, __Deis__ creates a __Docke__r image, which is then used for application deployment.

### Example: Deploying an Application
Next we will see how we can deploy an application with __Deis__. For this example, we will use the sample helloworld application given in the [Deis documentation][deisdoc].

Let's clone the repository and look at the `Dockerfile`:
```bash
$ git clone https://github.com/deis/helloworld.git
$ cd helloworld

FROM debian:jessie

# install curl
RUN apt-get update && apt-get install -qy curl

# install go runtime
RUN curl -s https://storage.googleapis.com/golang/go1.2.2.linux-amd64.tar.gz | tar -C /usr/local -xz

# prepare go environment
ENV GOPATH /go
ENV GOROOT /usr/local/go
ENV PATH $PATH:/usr/local/go/bin:/go/bin

# add the current build context
ADD . /go/src/github.com/deis/helloworld

# compile the binary
RUN cd /go/src/github.com/deis/helloworld && go install -v .

EXPOSE 80

ENTRYPOINT ["/go/bin/helloworld"]
```
With the __Docker__ image created from the above `Dockerfile`, we can create a container, which would:

+ Run the `helloworld` binary at start time.
+ Expose `port 80` to accept the connection.

To create the application on the controller, run the following command:
```bash
$ deis create
```
If we look at the `.git/config` file, we can see that the following entry has been added:
```bash
[remote "deis"]
    url = ssh://git@deis.local3.deisapp.com:2222/upbeat-zeppelin.git
    fetch = +refs/heads/*:refs/remotes/deis/*
```
To deploy the application on the platform, we need to run the following command:
```bash
$ git push deis master
```
With the `push` command, we get the following:

+ A new build is triggered.
+ A new deployment is created.
+ A new image for the application is pushed into the Docker Registry on the Control Plane.
+ Containers are deployed on the Data Plane with new images.
+ The router is configured accordingly.

![image][img3]

Figure 4.3: Deis Workflow (retrieved from [docs.deis.io][deiswf])

### Demo
Next, we will see how we can use __Deis__ to deploy an application, and then scale it up.

[video][vid4]

### Benefits of Using Deis
Some of the benefits of using __Deis__ are:

+ It is 100% Open Source and free.
+ It uses __Docker__ and __CoreOS__ for deployment.
+ __Deis__ makes it easy to deploy and manage applications on-premise or any cloud provider.
+ It is language-and framework-agnostic.
+ There is no vendor lock-in, which can reduce infrastructure costs considerably.
+ Applications can be scaled up or down with a single command.
+ It is a self-service platform.

### References
+ http://docs.deis.io/en/latest/understanding_deis/architecture/
+ http://deis.io


## Knowledge Check
1. Is it necessary to run PaaS on top of IaaS? Please select the correct answer.

        Ans: False

2. Which container orchestration engine is used by OpenShift v3 in the background? Please select the correct answer.

        A. Docker Swarm
        B. Apache Mesos
        C. Kubernetes
        D. None of the above

        Ans: C

3. Which of following PaaS solutions can be configured on-premise? Please select all answers that apply.

        A. OpenShift v3 
        B. Google Compute Engine
        C. Deis 
        D. Heroku

        Ans: A, C



[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V001200_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V002200_DTH.mp4
[vid3]: https://edx-video.net/LINLFS15/LINLFS152016-V002100_DTH.mp4
[vid4]: https://edx-video.net/LINLFS15/LINLFS152016-V004700_DTH.mp4

[img1]: https://docs.cloudfoundry.org/concepts/images/cf_architecture_block.png
[img2]: ./diagrams/DeisSystemDiagram.png
[img3]: ./diagrams/DeisGitPushWorkflow.png

[cf]: https://www.cloudfoundry.org/
[cfcp]: https://www.cloudfoundry.org/learn/certified-providers/
[bosh]: http://bosh.io/
[build]: https://docs.cloudfoundry.org/buildpacks/]]
[garden]: https://github.com/cloudfoundry-incubator/garden
[cff]: https://www.cloudfoundry.org/
[os]: https://www.openshift.com/
[ghos]: https://github.com/openshift/origin
[oso]: https://www.openshift.org/
[osdoc]: https://docs.openshift.com/enterprise/3.1/install_config/index.html
[heroku]: http://www.heroku.com/
[salesf]: https://www.salesforce.com/
[procf]: https://devcenter.heroku.com/articles/procfile
[buip]:https://devcenter.heroku.com/articles/buildpacks
[mbuip]: https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app
[addon]: https://elements.heroku.com/addons
[core]: https://coreos.com/
[deisarch]: http://docs.deis.io/en/latest/_images/DeisSystemDiagram.png
[eng]: https://engineyard.com/
[deisio]: http://docs.deis.io/en/latest/_images/DeisSystemDiagram.png
[deisclt]: http://docs.deis.io/en/latest/using_deis/install-client.html
[usrreg]: http://docs.deis.io/en/latest/using_deis/register-user.html
[12fac]: http://12factor.net/
[deisdoc]: http://docs.deis.io/en/latest/using_deis/using-dockerfiles/
[deiswf]: http://docs.deis.io/en/latest/_images/DeisGitPushWorkflow.png



