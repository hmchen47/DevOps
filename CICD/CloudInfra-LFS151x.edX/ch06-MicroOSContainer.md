# Chapter 6. Containers: Micro OSes for Containers

## Introduction and Learning Objectives
### Micro OSes for Containers
Our ultimate goal is to run applications on top of containers. It makes sense to get rid of all the packages and services from the Host Operating System (OS), which do not help us in running containers. Keeping that in mind, different vendors have come forward with specialized OSes to run just containers.

Once we remove the packages which are not required to boot the base OS and run container-related services, we are left with specialized OSes, which are referred to as __Micro OSes for containers__. Some examples of Micro OSes are:

+ Atomic Host 
+ CoreOS
+ RancherOS 
+ Ubuntu Snappy 
+ VMware Photon
+ Microsoft Nano.

![image][img1]

Figure 6.1: Micro OSes to Run Containers

In this chapter we will provide details on some of the most utilized Micro OSes.

### Learning Objectives
By the end of this chapter you should be able to:

+ Discuss the characteristics and functionality of Micro OSes, which are specially designed to run containers.
+ Describe different Micro OSes designed to run containers: Project Atomic, CoreOS, VMware Photon, and RancherOS.
+ Deploy containers and containerized applications on Micro OSes.

## Atomic Host
### Introduction to Atomic Host
[Atomic Host][atomh] is a lightweight Operating System, assembled out of a specific __RPM__ content. It allows us to run just containerized applications in a quick and reliable manner. Atomic Host can be based on __Fedora, CentOS__, or __Red Hat Enterprise Linux (RHEL)__.

__Atomic Host__ is a sub-project of __Project Atomic__, which includes other sub-projects, such as [Nulecule][nulec], [AtomicApp][atomapp], [Atomic Registry][atomreg]. With __Atomic Host__, we can develop, run, administer and deploy containerized applications. 

### Components of Atomic Host
__Atomic Host__ has a very minimal base OS, but it includes components like __Systemd__ and __Journald__ to help its users and administrators. It is built on top of the following:

+ `rpm-ostree`

    One cannot manage individual packages on __Atomic Host__, as there is no `rpm` or other related commands. To get any required service, you would have to start a respective container. __Atomic Host__ has two bootable, immutable, and versioned filesystems; one is used to boot the system and the other is used to fetch updates from upstream. `rpm-ostree` is the tool to manage these two versioned filesystems.
+ `systemd`

    It is used to manage system services for __Atomic Host__.
+ __Docker__ 

    __Atomic Host__ currently supports __Docker__ as a container runtime.
+ Kubernetes

    With __Kubernetes__, we can create a cluster of __Atomic Hosts__ to run applications at scale.

__Atomic Host__ also comes with a command called `atomic`. This command provides a high-level, coherent entry point to the system, and fills in the gaps that are not filled by __Linux__ container implementations, such as upgrading the system to the new `rpm-ostree`, running containers with pre-defined `docker run` options using [labels][label], verifying an image etc.

__Atomic Host__ can be managed using tools such as [__Cockpit__][cockpit].

### Demo
In the following video we will take a look at some basic operations that we can do with __Atomic Host__.

[video][vid1]

### Benefits of Using Atomic Host
Some of the benefits of using Atomic __Host are__:

+ It is an OS specifically designed to run containerized applications.
+ It enables us to perform quick updates and rollbacks.
+ It provides increased security through __SELinux__.
+ It can be installed on bare-metal, as well as VMs.
+ It can be based on __Fedora, CentOS__, and __Red Hat Enterprise Linux__.
+ Nodes can be clustered on __Atomic Host__ using __Kubernetes__.

### References
+ http://www.projectatomic.io/


## CoreOS
### Introduction to CoreOS
__CoreOS__ is a minimal Operating System, used to run containers at scale. __CoreOS__ supports `docker` and `rkt` as container runtimes. It is designed to operate in a cluster mode. 

![image][img2]

Figure 6.2: A High-Level Illustration of the CoreOS Cluster Architecture (by Offnfopt/[Public Domain][domain], retrieved from [Wikipedia][wikicore])

### CoreOS Availability
__CoreOS__ is available on most of the cloud providers, such as __Amazon EC2, Digital Ocean, Microsoft Azure, Google Cloud__, etc. It can be installed on bare-metal, as well as on VMs. While booting up the instance, [cloud-config][cconfig] is used to boot it for a given configuration.

### CoreOS Partitions
__CoreOS__ does not have any package manager and the Operating System is treated as a single unit. It has two root partitions, which are called _active_ and _passive_. When the system is booted with the _active_ partition, the _passive_ partition can be used to download the latest updates. Other than manual updates, __CoreOS__ offers a feature to self-update, in which all the nodes of the cluster get updated one by one, without causing any downtime. Your Ops team can choose specific [release channels][rchann] to deploy and control the application with [update strategies][ustrat].

As shown in Figure 6.3 below, partition A was initially _active_ and updates were getting installed on partition B. After the reboot, partition B becomes _active_ and updates are installed on partition A, if available.

![image][img3]

Figure 6.3: __CoreOS__ Partitions (by __CoreOS, Inc.__, retrieved from [www.slideshare.net][slidcore])

### CoreOS Components
CoreOS is built on top of the following:

+ `Docker/rkt`

    CoreOS supports both `docker` and `rkt` as container runtime to run applications.
+ [etcd][etcd]

    It is a distributed key-value pair, used to save the cluster state, configurations, etc.
+ [systemd][sysd]

    It is an __init__ system which helps us manage services on most __Linux__ distributions. A sample __init__ file looks like the following:

    ```bash
    [Unit]
    Description=My Service
    Requires=docker.service
    After=docker.service

    [Service]
    ExecStart=/usr/bin/docker run busybox /bin/sh -c "while true; do echo Hello World; sleep 1; done"

    [Install]
    WantedBy=multi-user.target
    ```
+ [fleet][fleet]

    It is used to launch applications using the `systemd` unit files. With `fleet`, we can treat the __CoreOS cluster__ as a single __init__ system. A sample `fleet` configuration file looks like the following:
    ```bash
    [Unit]
    Description=My Advanced Service
    After=etcd.service
    After=docker.service

    [Service]
    TimeoutStartSec=0
    ExecStartPre=-/usr/bin/docker kill apache1
    ExecStartPre=-/usr/bin/docker rm apache1
    ExecStartPre=/usr/bin/docker pull coreos/apache
    ExecStart=/usr/bin/docker run --name apache1 -p 8081:80 coreos/apache /usr/sbin/apache2ctl -D FOREGROUND
    ExecStartPost=/usr/bin/etcdctl set /domains/example.com/10.10.10.123:8081 running
    ExecStop=/usr/bin/docker stop apache1
    ExecStopPost=/usr/bin/etcdctl rm /domains/example.com/10.10.10.123:8081

    [Install]
    WantedBy=multi-user.target
    ```

### Support
As a company, __CoreOS__ [provides paid support][paid] for the production environment. They have a [hosted][host] and [enterprise][enter] registry product called [Quay][quay]. They also enterprise the __Kubernetes__ solution called [Tectonic][tecton].

### Demo
In the following video will see what are the requirements to create a CoreOS cluster and deploy a sample application on top of it.

[video][vid2]

### Benefits of Using CoreOS
Some of the benefits of using __CoreOS__ are:

+ It is a system built for High Availability and security.
+ It is available on most cloud providers.
+ It supports __Docker__ and __rkt__ container runtimes.
+ It has a self-update feature.
+ It offers paid support for production environment.
+ It allows users to have different versions of software on different machines and to update these machines without any downtime. 

### References
+ https://coreos.com/
+ https://coreos.com/docs/


## VMware Photon
### Introduction to VMware Photon
__Photon OS™__ is a technology preview of a minimal __Linux__ container host. It is designed to have a small footprint and boot extremely quickly on __VMware__ platforms.

### Features and Availability
__Photon OS™__ is optimized for __VMware__ products and platforms. It supports __Docker, rkt__  , and the __Pivotal Garden__ container specifications. It also has a new, open-source, __yum__-compatible package manager ([__tdnf__][tdnf]).

If you want to try it out, __Photon OS™__ is available on __Amazon EC2, Google Cloud__, and __Microsoft Azure__.

### Demo
Next, we will see how we can upgrade the existing OS on __VMware Photon__, using the `rpm ostree` command.

[video][vid3]

### Benefits of Using VMware Photon
Some of the benefits of using __VMware Photon__ are:

+ It is an Open Source technology with a small footprint.
+ It supports __Docker, rkt__, and __Pivotal Garden__ container runtimes.
+ We can use __Kubernetes, Swarm__ and __Mesos__ clusters on top of __Photon__.
+ It boots extremely quickly on __VMware__ platforms.
+ It provides an efficient lifecycle management with a __yum__-compatible package manager.

### References
+ https://vmware.github.io/photon/


## RancherOS
### Introduction to RancherOS
[RancherOS][ranos] is a 20 MB __Linux__ distribution that runs __Docker__ containers. It has the least footprint of all the Micro OSes available nowadays. This is possible because it runs directly on top of the __Linux__ kernel.

__RancherOS__ is a product provided by [Rancher][rancher], which is an end-to-end platform used to deploy and run private container services.

### Components
__RancherOS__ runs two instances of the __Docker daemon__. Just after booting, it starts the first instance of the __Docker daemon__ with `PID 1` to run system containers like `dhcp`, `udev`, etc. To run user-level containers, the __System Docker daemon__ creates a service to start other __Docker daemons__.

![image][img4]

Figure 6.4: __RancherOS Architecture__ (by __Rancher__, retrieved from [rancher.com][ranarch])

### Demo
The following demo will illustrate how you can start containers on __RancherOS__.

[video][vid4]

### Benefits of Using RancherOS
Some of the benefits of using __RancherOS__ are:

+ It has the least footprint of all Micro OSes available.
+ It runs directly on top of the __Linux__ kernel.
+ It enables us to perform updates and rollbacks in a simple manner.
+ We can use the __Rancher__ platform to setup __Kubernetes__ and __Swarm__ clusters.

### References
+ http://rancher.com/
+ http://rancher.com/rancher-os/


## Knowledge Check
1. Atomic Host can be based on:

        A. Fedora
        B. Ubuntu
        C. CentOS
        D. RHEL

        Ans: A, C, D

2. Which of the following Micro OSes has the least footprint?

        Ans: RancherOS

3. CoreOS supports automatic updates.

    Ans: True


[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V001100_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V001300_DTH.mp4
[vid3]: https://edx-video.net/LINLFS15/LINLFS152016-V004200_DTH.mp4
[vid4]: https://edx-video.net/LINLFS15/LINLFS152016-V002300_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4737e5aa0cad67db9b1979342a89736d/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Micro_OSes_for_Containers.png
[img2]: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/CoreOS_Architecture_Diagram.svg/2000px-CoreOS_Architecture_Diagram.svg.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/658654242ec996b0d44dd0a9461880d6/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/2c4clustered-computing-with-coreos-fleet-and-etcd-49-638.jpg
[img4]: ./diagrams/Figure_6.4-_RancherOS_Architecture.png

[atomh]: http://www.projectatomic.io/
[nulec]: http://www.projectatomic.io/docs/nulecule/
[atomapp]: http://www.projectatomic.io/docs/atomicapp
[atomreg]: http://www.projectatomic.io/registry/
[label]: https://github.com/docker/docker/pull/9882/
[cockpit]: http://www.projectatomic.io/docs/cockpit/
[domain]: https://en.wikipedia.org/wiki/Public_domain
[wikicore]: https://en.wikipedia.org/wiki/CoreOS#/media/File:CoreOS_Architecture_Diagram.svg
[cconfig]: https://coreos.com/os/docs/latest/cloud-config.html
[rchann]: https://coreos.com/releases/
[ustrat]: https://coreos.com/os/docs/latest/update-strategies.html
[slidcore]: https://www.slideshare.net/deview/2c4clustered-computing-with-coreos-fleet-and-etcd
[etcd]: https://coreos.com/etcd/
[sysd]: https://coreos.com/docs/launching-containers/launching/getting-started-with-systemd/
[fleet]: https://coreos.com/using-coreos/clustering/
[host]: https://quay.io/plans/
[paid]: https://coreos.com/products/premium-managed-linux/
[enter]: https://tectonic.com/quay-enterprise/
[quay]: https://quay.io/
[tecton]: https://tectonic.com/
[tdnf]: https://github.com/vmware/photon/blob/master/docs/tyum.md
[ranos]: http://rancher.com/rancher-os/
[rancher]: http://rancher.com/
[ranarch]: http://rancher.com/wp-content/themes/rancher-2016/assets/images/rancheros-docker-kernel.png

