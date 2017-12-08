# Chapter 15. Tools for Cloud Infrastructure II (Build & Release)

## Introduction and Learning Objectives
### Tools for Cloud Infrastructure: Build & Release
With source code management tools like Git, we can easily version the code and retrieve the same bits we saved in the past. This saves a lot of time and helps developers automate most of the non-coding activities, like creating automated builds, running tests, etc. Extending the same analogy to infrastructure would allow us to create a reproducible deployment environment, which is referred to as __Infrastructure as a Code__. 

__Infrastructure as a Code__ helps us create a near production-like environment for development, staging, etc.  With some tooling around them, we can also the create same environments on different cloud providers.  

By combining  Infrastructure as a Code with versioned software, we are guaranteed to have a re-producible build and release environment every time.  In this chapter we will take a look into two such tools: __Terraform__ and __BOSH__.

### Learning Objectives
By the end of this chapter you should be able to:

+ Discuss and use build and release tools: Terraform and BOSH.


## Terraform
### Introduction to Terraform
__Terraform__ is a tool that allows us to define the infrastructure as code. This helps us deploy the same infrastructure on VMs, bare metal or cloud. It helps us treat the infrastructure as software. The configuration files can be written in __HCL (HashiCorp Configuration Language)__.

### Terraform Providers
Physical machines, VMs, network switches, containers, etc. are treated as resources, which are exposed by providers.

A provider is responsible for understanding API interactions and exposing resources, which makes __Terraform__ agnostic to the underlying platforms. A custom provider can be created through plugins.

__Terraform__ has providers in different stacks:

+ IaaS: AWS, DigitalOcean, GCE, OpenStack, etc.
+ PaaS: Heroku, CloudFoundry, etc.
+ SaaS: Atlas, DNSimple, etc.

### Features
According to the [Terraform website][terra], it has following key features:

+ __Infrastructure as Code__: Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used.
+ __Execution Plans__: Terraform has a "planning" step where it generates an _execution plan_. The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure.
+ __Resource Graph__: Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.
+ __Change Automation__: Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors."

### Demo
The following demo will show us how to use Terraform to treat our infrastructure as a code.

[video][vid1]

### Benefits of Using Terraform
Some of the benefits of using Terraform are:

+ It allows to build, change, and version infrastructure in a safe and efficient manner.
+ It can manage existing, as well as customized service providers. It is agnostic to underlying providers.
+ It can manage a single application or an entire datacenter.
+ It is a flexible abstraction of resources.

### References
+ https://www.terraform.io/docs/providers/


## BOSH
### Introduction to BOSH
According to bosh.io,

> "BOSH is an open source tool for release engineering, deployment, lifecycle management, and monitoring of distributed systems." 

__BOSH__ was primarily developed to deploy the Cloud Foundry PaaS, but it can deploy other software as well (e.g. Hadoop). BOSH supports multiple Infrastructure as a Service (IaaS) providers. BOSH creates VMs on top of IaaS, configures them to suit the requirements, and then deploys the applications on them. Supported IaaS providers for BOSH are:

+ Amazon Web Services EC2
+ OpenStack
+ VMware vSphere
+ vCloud Director.

With __Cloud Provider Interface (CPI)__, __BOSH__ supports additional IaaS providers such as __Google Compute Engine__ and __Apache CloudStack__.

### Key Concepts
Some of the key concepts around BOSH are detailed next:

+ Stemcell 

    A Stemcell is a versioned, IaaS-specific, Operating System image with some pre-installed utilities (e.g. BOSH Agent). Stemcells do not contain any application-specific code. The BOSH team is in charge of releasing stemcells, which are listed here.

+ Release

    A Release is placed on top of a Stemcell,  and consists of a versioned collection of configuration properties, templates, scripts, source code, etc., to build and deploy software. 

+ Deployment 

    A Deployment is a collection of VMs which are built from Stemcells, populated with specific Releases on top of them and having disks to keep persistent data.

+ BOSH Director

    The BOSH Director is the orchestrator component of BOSH, which controls the VM creation and deployment. It also controls software and service lifecycle events. We need to upload Stemcells, Releases and Deployment manifest files to the Director. The Director processes the manifest file and does the deployment. 

### Sample Deployment
Next, we will reproduce an example of a sample deployment manifest from the BOSH website. This sample [deployment manifest][depmani] must be then uploaded to the BOSH Director: 
```yaml
name: my-redis-deployment

director_uuid: cf8dc1fc-9c42-4ffc-96f1-fbad983a6ce6

releases:
- {name: redis, version: 12}

networks:
- name: default
    type: manual
    subnets:
    - range:    10.10.0.0/24
        gateway:  10.10.0.1
        dns:      [10.10.0.2]
        reserved: [10.10.0.2-10.10.0.10]
        cloud_properties: {subnet: subnet-9be6c3f7}

resource_pools:
- name: redis-servers
    network: default
    stemcell:
        name: bosh-aws-xen-ubuntu-trusty-go_agent
        version: 2708
    cloud_properties:
        instance_type: m1.small
        availability_zone: us-east-1c

compilation:
    workers: 2
    network: default
    cloud_properties:
        instance_type: m1.small
        availability_zone: us-east-1c

update:
    canaries: 1
    max_in_flight: 10
    update_watch_time: 1000-30000
    canary_watch_time: 1000-30000

jobs:
- name: redis-master
    instances: 1
    templates:
    - {name: redis-server, release: redis}
    persistent_disk: 10_240
    resource_pool: redis-servers
    networks:
    - name: default

- name: redis-slave
    instances: 2
    templates:
    - {name: redis-server, release: redis}
    persistent_disk: 10_240
    resource_pool: redis-servers
    networks:
    - name: default
```

### Demo
In the following demo we will see how we can use BOSH to deploy our infrastructure, and then deploy an application on top of it.

[video][vid2]

### Benefits of Using BOSH
Some of the benefits of using BOSH are:

+ It is an Open Source tool "for release engineering, deployment, lifecycle management, and monitoring of distributed systems" (bosh.io).
+ It supports IaaS providers like AWS, OpenStack, VMware vSphere, Google Compute Engine, etc.

### References
+ https://bosh.io
+ https://bosh.io/docs/deployment-basics.html


## Knowledge Check
1. A BOSH Stemcell is ______________. Please select the correct answer.

        A. A collection of VMS
        B. A source code application with all its dependencies
        C. A versioned Operating System
        D. None of the above

        Ans: C

2. In which language is the configuration for Terraform written? 

        Ans: HCL



[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V003700_DTH.mp4

[terra]: https://www.terraform.io/intro/index.html
[depmani]: https://bosh.io/docs/deployment-basics.html


