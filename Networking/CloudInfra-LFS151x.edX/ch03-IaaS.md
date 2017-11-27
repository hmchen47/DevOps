# Chapter 3. Infrastructure as a Service

## Introduction and Learning Objectives
### Infrastructure as a Service
__Infrastructure as a Service  (IaaS)__ is a form of Cloud Computing which provides on-demand physical and virtual computing resources, storage, network, firewall, load balancers, etc. To provide virtual computing resources, __IaaS__ uses some form of Hypervisor, like __Xen, KVM, VMware ESX/ESXi, Hyper-V__, etc.  

__Infrastructure as a Service__ is the backbone of all cloud services, providing the compute resources. After getting the compute resources, we provide other services on top of that.

Example

> Let's say that you want to have a set of 10 __Linux__ systems with 4GB RAM each, and two __Window__ systems with 8GB each to deploy your software. You can go to any of the __IaaS__ providers and request these systems. Generally, a __IaaS__ provider creates the respective VMs in the background, puts them in the same internal network, and shares the credentials with you, thus allowing you to access them.

> Other than VMs, some __IaaS__ providers offer bare-metal machines for provisioning.

In this chapter, we will take a closer look at some of the __IaaS__ providers and their features. We will also provide a demo video for each one of them.

### Learning Objectives
By the end of this chapter you should be able to:

+ Explain the concept of __Infrastructure as a Service (IaaS)__.
+ Distinguish between different __IaaS__ providers.
+ Provision a Virtual Machine on top of different __IaaS__ providers.


## Amazon EC2
### Introduction to Amazon EC2
__[Amazon Web Services][aws] (AWS)__ is one of the leaders in providing different cloud services. With [Amazon Elastic Compute][aec], __Amazon__ provides the __IaaS__ infrastructure, on which most of the other services are built. We can manage compute resources from the __Amazon EC2__ web interface and can scale up or down depending on the need. __AWS__ also [offers a command line][awscl] to manage the instances from the command line.

__Amazon EC2__ uses mostly the __XEN Hypervisor__ to provision compute resources.

### Features and Tools
__Amazon EC2__ offers compute instances for different resources, which we can choose from depending on our need. Some examples of instances offered are the following:

+ `t2.nano`: 512 MiB of memory, 1 vCPU, 3 CPU Credits/hour, EBS-only, 32 bit or 64-bit platform.
+ `c4.large`: 3.75 GiB of memory, 2 vCPUs, 64-bit platform.
+ `d2.8xlarge`: 244 GiB of memory, 36 vCPUs, 24 x 2000 GB of HDD-based instance storage, 64-bit platform, 10 Gigabit Ethernet.

__Amazon EC2__ provides some pre-configured images, called __Amazon Machine Images (AMIs)__. These images can be used to quickly start instances. We can also create our own custom __AMIs__ to boot our instances.

One important aspect to note is that Amazon supports configuring security and network access to our instances.

With __Amazon Elastic Block Store (EBS)__ we can attach/detach persistent storage to our instances.

__EC2__ supports the provisioning of dedicated hosts, which means we can get an entire physical machine for our use.

__Amazon EC2__ has many other features, allowing you to:

+ Create an __Elastic IP__ for remapping the Static IP address automatically
+ Provision a __Virtual Private Cloud__ for isolation
+ Use __CloudWatch__ for monitoring resources and applications
+ Use __Auto Scaling__ to dynamically resize your resources, etc.

### Demo
Let's take a look at the following demo, which illustrates an example of how to create and destroy an instance on AWS, using Amazon EC2 compute service.

[video][vid1]   

### Benefits of Using Amazon EC2
Some of the benefits of using __Amazon EC2__ are:

+ It is an easy-to-use __Iaa__S solution.
+ It is flexible and scalable.
+ It provides a secure and robust functionality for your compute resources.
+ It enables automation.
+ It is cost-effective: you only pay for the time and resources you use.
+ It is designed to work in conjunction with other __AWS__ components.

### References
+ https://aws.amazon.com/ec2/
+ https://aws.amazon.com/ec2/details/


## Azure Virtual Machine
### Introduction to Azure Virtual Machine
[__Azure__][azure] is __Microsoft's__ Cloud offering, which has products in different domains, such as compute, Web & Mobile, Data & Storage, Internet of Things, and many others. Through __Azure Virtual Machine__, __Microsoft__ provides compute provisioning and management:

+ We can manage Virtual Machines from __Azure's__ web interface.
+ __Azure__ also provides a [command line utility][azcli] to manage resources and applications on the __Azure Cloud__.

### Features and Tools
__Azure__ lets you choose between different tiers, based on the usage and the Operating Systems or the pre-defined application Virtual Machines (__SharePoint__, __Oracle__, etc.). To learn more, please take a look [here][azvm].

Using Resource Manager templates, we can define the template for the Virtual Machine Deployment.

__Azure__ offers other features as well, like making seamless hybrid connections, faster I/O in certain types of tiers, backups, etc.

### Demo
Let's take a look at the following demo, which illustrates how we can create a Virtual Machine instance on __Microsoft Azure__ platform.

[video][vid2]

### Benefits of Using Azure Virtual Machine
Some of the benefits of using __Azure__ Virtual Machine are:

+ It is an easy-to-use __IaaS__ solution.
+ It is flexible and scalable.
+ It provides a secure and robust functionality for your compute resources.
+ It enables automation.
+ It is cost-effective: you only pay for the time and resources you use.
+ It is designed to work in conjunction with other __Azure__ Services.

### References
+ https://azure.microsoft.com/en-in/services/virtual-machines/


## DigitalOcean
### Introduction to DigitalOcean
[DigitalOcean][do] helps you create a simple cloud quickly, in as little as 55 seconds. All of the VMs are created on top of the __KVM__ Hypervisor and have __SSD (Solid-State Drive)__ as the primary disk.

### Features and Tools
Based on your need, __DigitalOcean__ offers different plans. Some examples of plan offerings are listed below:

+ 2GB Memory, 2 Core Processor, 40 GB SSD Disk, 3 TB transfer
+ 48GB Memory, 16 Core Processor, 480 GB SSD Disk, 8 TB transfer.

__DigitalOcean__ provides other features, like Floating IPs within the same datacenter, Shared Private Networking and Team Accounts, etc.

### Demo
Next, we will take a look at a video showing how to create a Virtual Machine on __DigitalOcean__.

[video][vid3]

### Benefits of Using DigitalOcean
Some of the benefits of using __DigitalOcean__ are:

+ It allows you to configure a cloud in as little as 55 seconds.
+ It is flexible and scalable.
+ It provides a high level of security by using KVM virtualized droplets.
+ It enables automation.
+ It is cost-effective: you only pay for the time and resources you use.
+ It is focused on providing a simple, user-friendly experience.

### References
+ https://www.digitalocean.com


## Google Compute Engine
### Introduction to Google Compute Engine
[__Google Cloud Platform__][gcp] is __Google's__ Cloud offering, which has many products in different domains, like Compute, Storage, Networking, Big Data, and others. [Google Compute Engine][gce] provides the compute service. We can manage the instances through GUI, APIs or [command line][gccli]. Access to the individual VM's console is also available.

### Features and Tools
__GCE__ supports different machine types, which we can choose depending on our need. They are categorized in the following [types][gcemt]:

+ Standard machine types
+ High-CPU machine types
+ High-memory machine types
+ Shared-core machine types
+ We can also configure custom machine types.

__GCE__ has other features like Persistent Disk, Local SSD, Global Load Balancing, Compliance & Security, Automatic Discount, etc.

### Demo
Let's take a look at the following demo, illustrating how we can create and destroy an instance on __Google Compute Engine__.

[video][vid4]

### Benefits of Using Google Compute Engine
Some of the benefits of using __Google Compute Engine__ are:    

+ It is flexible and allows you to scale your applications easily.
+ Fast boot time.
+ It is very secure, encrypting all data stored.
+ It enables automation.
+ It is cost-effective: you only pay for the time and resources you use.
+ It supports custom machine types.

### References
+ https://cloud.google.com/compute/


## OpenStack
### Introduction to OpenStack
Earlier in this chapter we have seen examples for consuming the services of different cloud providers to provision our infrastructure. What if we want to become a cloud provider and offer cloud computing services?

With [__OpenStack__][ostk], we can offer a cloud computing platform for public and private clouds. __Openstack__ was started as a joint project between [Rackspace][rspace] and [NASA][nasa] in 2010. In 2012, a non-profit corporate entity, called the __OpenStack Foundation__, was formed and it is managing it since then. It is now supported by more than 500 organizations. __OpenStack__ is an Open Source software platform, which is released under an __Apache 2.0 License__.

Other than providing a __IaaS__ solution, __OpenStack__ has evolved over time to provide other services, like Database, Storage, etc.

### Components/Features
Due to the modular nature of __OpenStack__, anyone can add additional components to get specific features or functionality. Some of the major __Openstack__ components are:

+ [Keystone][keystone]

    Provides Identity, Token, Catalog, and Policy services to projects.
+ [Nova][nova]

    Provides on-demand compute resources.
+ [Horizon][horizon]

    Provides the Dashboard, which is a web-based user interface to manage the __Openstack__ Service.
+ [Neutron][neutron]

    Implements the network as a service and provides network capabilities to different __Openstack__ components.
+ [Glance][glance]

    Provides a service where users can upload and discover data assets, like images and metadata.
+ [Swift][swift]

    Provides a highly available, distributed, eventually consistent object/blob store.
+ [Cinder][cinder]

    Provides block storage as a service.
+ [Heat][heat]

    Provides a service to orchestrate composite cloud applications, using a declarative template format through an __OpenStack__-native REST API.
+ [Ceilometer][ceilmeter]

    It is part of the Telemetry project and provides data collection services for billing and other purposes.

Each of the __OpenStack__ components is also modular by design. For example, with __Nova__ we can select an underneath Hypervisor depending on the requirement, which can be either __libvirt (qemu/KVM), Hyper-V, VMware, XenServer, Xen__ via __libvirt__.


### Demo
In the following example we will show how you can deploy an instance with __OpenStack__.

[video][vid5]

### Benefits of Using OpenStack
Some of the benefits of using __OpenStack__ are:

+ It is an Open Source solution.
+ It is a cloud computing platform for public and private clouds.
+ It offers a flexible, customizable, vendor-neutral environment. 
+ It provides a high level of security.
+ It facilitates automation throughout the stages of the cloud lifecycle.
+ By reducing system management overhead and  avoiding vendor lock-in, it can be cost-effective.

### References
+ https://www.openstack.org/


## Knowledge Check
1. What is the name of the IaaS solution provided by Amazon Web Services? Please select the correct answer.

        A. Amazon Cloud Deploy
        B. Amazon Elastic Compute Cloud 
        C. Amazon Cloud Formation
        D. Amazon S3

        Ans: B
        Explanation
        The IaaS solution provided by Amazon Web Services is called Amazon Elastic Compute Cloud or Amazon EC2.

2. Digital Ocean does not provide SSD as the primary disk. Please select the correct answer.

        Ans: False

3. Which of the following are components of OpenStack? Please select all answers that apply.

A. Nova 
B. Keystone 
C. DevStack
D. Glance 

Ans: A, B, D

[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V000700_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V000800_DTH.mp4
[vid3]: https://edx-video.net/LINLFS15/LINLFS152016-V000100_DTH.mp4
[vid4]: https://edx-video.net/LINLFS15/LINLFS152016-V000900_DTH.mp4
[vid5]: https://edx-video.net/LINLFS15/LINLFS152016-V002000_DTH.mp4

[aws]: https://aws.amazon.com/
[aec]: https://aws.amazon.com/ec2/
[awscl]: https://aws.amazon.com/cli/
[azure]: https://azure.microsoft.com/
[azvm]: https://azure.microsoft.com/en-in/pricing/details/virtual-machines/
[azcli]: https://github.com/azure/azure-xplat-cli
[do]: https://www.digitalocean.com/
[dopl]: https://www.digitalocean.com/pricing/
[gcp]: https://cloud.google.com/
[gce]: https://cloud.google.com/compute/
[gccli]: https://cloud.google.com/sdk/gcloud/
[gcemt]: https://cloud.google.com/compute/docs/machine-types
[ostk]: https://www.openstack.org/
[rspace]: https://www.rackspace.com/
[nasa]: http://www.nasa.gov/
[keystone]: http://docs.openstack.org/developer/keystone/
[nova]: http://docs.openstack.org/developer/nova/
[horizon]: http://docs.openstack.org/developer/horizon/
[neutron]: http://docs.openstack.org/developer/neutron/
[glance]: http://docs.openstack.org/developer/glance/
[swift]: http://docs.openstack.org/developer/swift/
[cinder]: http://docs.openstack.org/developer/cinder/
[heat]: http://docs.openstack.org/developer/heat/
[ceilmeter]: http://docs.openstack.org/developer/ceilometer/


