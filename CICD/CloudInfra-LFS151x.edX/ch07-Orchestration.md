# Chapter 7. Containers: Container Orchestration

## Introduction and Learning Objectives
### Container Orchestration
Running containers on a single node is fine, but, in production, we need to run containers at scale. That is when we can see the real benefits of containers. To run containers in a multi-host environment at scale, we need to find solutions to numerous problems, which are summarized below:

+ Who can bring multiple hosts together and make them part of a cluster?
+ Who will schedule the containers to run on specific hosts?
+ How can containers running on one host reach out to containers running on different hosts?
+ Who will make sure that the container has the dependent storage, when it is scheduled on a specific host?
+ Who will make sure that containers are accessible over a service name, so that we do not have to bother about container accessibility over IP addresses?

__Container orchestration__ tools, along with different plugins (like networking and storage), help us address the problems mentioned above.

__Container orchestration__ is an umbrella term which encompasses container scheduling and cluster management. Container scheduling allows us to decide on which host a container or a group of containers should be deployed. With the cluster management orchestrator we can manage the existing nodes, add or delete nodes, etc.  Some of the available solutions for container orchestration are:

+ Docker Swarm
+ Kubernetes
+ Mesos Marathon
+ Cloud Foundry Diego
+ Amazon ECS
+ Azure Container Service.

In this chapter, we will provide more details on the options available.

### Learning Objectives
By the end of this chapter you should be able to:

+ Describe different container orchestration tools: __Docker Swarm, Kubernetes, Mesos, Nomad, Amazon ECS, Google Container Engine__, and __Azure Container Service__.
+ Deploy sample applications using various container orchestration tools: __Docker Swarm, Kubernetes, Mesos, Nomad, Amazon ECS, Google Container Engine__, and __Azure Container Service__.


## Docker Swarm
### Introduction to Docker Swarm
__Docker Swarm__ is a native container orchestration tool from __Docker, Inc.__ It logically groups multiple __Docker__ engines to create a virtual engine, on which we can deploy and scale applications.

### The Swarm Cluster
Figure 7.1 below illustrates the major components of a __Swarm__ cluster:

+ __Swarm Manager__

    It accepts commands on behalf of the cluster and takes the scheduling decisions. One or more nodes can be configured as managers, but they work in active/passive modes.

+ __Swarm Agents__

    They are hosts which run the __Docker Engine__ and participate in the cluster.

+ [__Swarm Discovery Service__][swarmsvc]

    The recommended way to do node discovery is using [libkv][libkv], which abstracts out multiple __Key-Values__ like `etcd`, `consul`, `zookeeper`.

+ __Overlay Networking__

    __Swarm__ uses [libnetwork][libnet] to configure the Overlay Network, employing __VxLAN__ between different hosts.

![image][img1]

Figure 7.1: Components of a __Swarm__ Cluster (retrieved from [LinkedIn SlideShare][img1])

### Features
Next, we will focus on the characteristics of __Docker Swarm__:

+ It is compatible with __Docker__ tools and API, so that the existing workflow does not change much.
+ It provides native support to __Docker__ networking and volumes.
+ It has a built-in scheduler support-flexible scheduling. 
    + Filters:
        - Node filters (constraint, health)
        - Container filters (affinity, dependency, port)
    + Strategies:
        - `spread`
        - `binpack`
        - `random`
+ It can scale up to large numbers of nodes. For example, __Docker Swarm__ has been tested with 1000 nodes with 50000 containers.
+ It supports failover and High Availability for the cluster manager.
+ It supports the pluggable scheduler architecture, through which we can use __Mesos__ or ____Kubernetes____ as a scheduler.
+ Node discovery can be done via a hosted discovery service, a static file, a key-value store like `etcd` or `consul`.

Since we are illustrating the characteristics for __Docker Swarm__, we will also discuss briefly about __Docker Machine__ and __Docker Compose__ in the next few units.

### Docker Machine
[Docker Machine][docmach] helps us configure and manage one or more __Docker__ engines running locally or on cloud environments. With __Docker Machine__ we can start, inspect, stop, and restart a managed host, upgrade the __Docker__ client and daemon, and configure a __Docker__ client to talk to our host.

![image][img2]

Figure 7.2: Provisioning Docker Hosts on Remote Systems (by Docker, Inc., retrieved from [docker.com][img2])

__Docker Machine__ has drivers for __Amazon EC2, Google Cloud, Digital Ocean, Vagrant__, etc., to set up __Docker__ engines. One can also add already running instances of the __Docker__ engine to the __Docker Machine__:
+ Setting up the Docker engine using the Virtual Box driver:

    `$ docker-machine create -d virtualbox dev1`
+ Setting up the Docker engine using Digital Ocean:
    
    `$ docker-machine create --driver digitalocean --digitalocean-acc ess-token=<TOKEN> dev2`

We can also use __Docker Machine__ to configure a __Swarm__ cluster.

### Docker Compose
[__Docker Compose__][doccomp] allows us to define and run multi-container applications trough a configuration file. In a configuration file we can define services, images or __Dockerfiles__ to use, network, etc. Below we provide a sample of a compose file:
```bash
# Mongo DB
db:
  image: mongo
  expose:
    - 27017
  command: --smallfiles
# Python App
web:
  image: nkhare/dockchat:v1
  ports:
    - "5000:5000"
  links:
   - db:db
```

With the above compose file, we would take the __images__ mentioned in the image section and we would link them together to run the application. Instead of using existing images, we can also build them from the __Dockerfile__.

### Demo
In the following video we will show how you can use __Docker Swarm__ to deploy a Microservice, and then scale up and scale down.

[video][vid1]

### Benefits of Using Docker Swarm
Some of the benefits of using __Docker Swarm__ are:

+ It provides native clustering for __Docker__.
+ It is well-integrated with the existing __Docker__ tools and workflow.
+ Its setup is easy, straightforward and flexible.
+ It manages a cluster of containers as a single entity.
+ It provides scalability and supports High Availability.
+ Efficiency and productivity are increased by reducing deployment and management time, as well as duplication of efforts.

### References
+ https://www.docker.com/products/docker-swarms
+ https://docs.docker.com/swarm/


## Kubernetes
### Introduction to Kubernetes
__Kubernetes__ is an __Apache 2.0__-licensed Open Source project for automating deployment, operations, and scaling of containerized applications. It was started by __Google__, but many other companies like __Docker, Red Hat__, and __VMware__ contributed to it.

In March of 2016, [__Cloud Native Computing Foundation (CNCF)__][cncf], the nonprofit organization dedicated to advancing the development of cloud-native applications and services and driving alignment among container technologies, [accepted __Kubernetes__ as the first hosted project][first]. The IP is transferred to the __CNCF__ from __Google__.

As of now, __Kubernetes__ supports __Docker__ as container runtime, but it has a plan to support other container runtimes like __rkt__ in the near future.

### The Kubernetes Architecture
The __Kubernetes__ architecture and its key components are illustrated in Figure 7.3 below.

![image][img3]

Figure 7.3: The __Kubernetes__ Architecture (retrieved from [blog.arungupta.me][kuberarch])

### The Kubernetes Architecture - Key Components
Next, we will discuss the key components of the Kubernetes architecture.

+ __Cluster__

    The __cluster__ is a group of systems (physical or virtual) and other infrastructure resources used by __Kubernetes__ to run containerized applications.

+ __Node__
    
    The __node__ is a system on which __pods__ are scheduled and run. The __node__ runs a daemon called __kubelet__, which allows it to communicate with the __master__ node.

+ __Master__

    The __master__ is a system that takes __pod__ scheduling decisions and manages the replication and manager nodes.

+ __Pod__

    The __pod__ is a co-located group of containers with shared volumes. It is the smallest deployment unit in __Kubernetes__. A __pod__ can be created independently, but it is recommended to use the __Replication Controller__, even if only a single __pod__ is being deployed.

+ __Replication Controller__

    The __Replication Controllers__ manage the lifecycle of __pods__. They make sure that the desired number of __pods__ is running at any given point in time. Below we provide an example of a __replication controller__, which makes sure that at least two copies of my __pod__ are running:
    ```docker
    apiVersion: v1
    kind: ReplicationController
    metadata:
    name: frontend
    spec:
    replicas: 2
    template:
        metadata:
        labels:
            app: dockchat
            tier: frontend
        spec:
        containers:
        - name: chat
            image: nkhare/dockchat:v1
            env:
            - name: GET_HOSTS_FROM
            value: dns
            ports:
            - containerPort: 5000
    ```
+ __Replica Sets__
    
    According to the [documentation][kuberep] provided by Kubernetes, 

    > "Replica Set is the next-generation [Replication Controller][repctl]. The only difference between a Replica Set and a Replication Controller right now is the selector support. Replica Set supports the new set-based selector requirements as described in the [labels user guide][labusr] whereas a Replication Controller only supports equality-based selector requirements."

+ __Deployments__

    With __Kubernetes 1.2__, a new object has been added,  Deployment. According to the __Kubernetes__ [documentation][kubedep],

    > "A Deployment provides declarative updates for [Pods][kubepod] and [Replica Sets][kuberep] (the next-generation Replication Controller). You only need to describe the desired state in a Deployment object, and the Deployment controller will change the actual state to the desired state at a controlled rate for you. You can define Deployments to create new resources, or replace existing ones by new ones.
    >
    > A typical use case is:
    >
    > - Create a Deployment to bring up a Replica Set and Pods.
    > - Check the status of a Deployment to see if it succeeds or not.
    > - Later, update that Deployment to recreate the Pods (for example, to use a new image).
    > - Rollback to an earlier Deployment revision if the current Deployment isn’t stable.
    > - Pause and resume a Deployment."

    Below we provide a [sample deployment][kubesmp]:
    ```docker
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
    name: nginx-deployment
    spec:
    replicas: 3
        template:
        metadata:
        labels:
            app: nginx
        spec:
        containers:
        - name: nginx
            image: nginx:1.7.9
            ports:
            - containerPort: 8
    ```
+ __Service__

    The __service__ groups sets of __pods__ together and provides a way to refer to them from a single static IP address and the corresponding __DNS__ name. Below we provide an example of a service file:
    ```docker
    apiVersion: v1
    kind: Service
    metadata:
    name: frontend
    labels:
        app: dockchat
        tier: frontend
    spec:
    type: LoadBalancer
    ports:
    - port: 5000
    selector:
        app: dockchat
        tier: frontend
    ```
+ __Label__

    The __label__ is an arbitrary key-value pair which is attached to a resource like __pod, replication controller__, etc. In the example above we defined __labels__ as `app` and `tier`.

+ __Selector__

    __Selectors__ enable us to group resources based on __labels__. In the above example, the `frontend` __service__ will select all `pods` which have the labels `app==dockchat` and `tier==frontend`.

+ __Volume__

    The __volume__ is an external filesystem or storage which is available to __pods__. They are built on top of [Docker volumes][docvol].

+ __Namespace__

    The __namespace__ adds a prefix to the name of the resources, so that it is easy to distinguish between different projects, teams, etc. in the same cluster.

### Features
Among the features of __Kubernetes__ are the following:

+ It automatically places containers based on resource requirements and other constraints.
+ It supports horizontal scaling through CLI and UI. It can auto-scale based on the CPU load as well.
+ It supports rolling updates and rollbacks.
+ It supports multiple volume plugins like the __GCP/AWS__ disk, __NFS, iSCSI, Ceph, Gluster, Cinder, Flocker__, etc. to attach volumes to __Pods__.
+ It automatically self-heals by restarting failed pods, rescheduling pods from failed nodes, etc.
+ It deploys and updates secrets for application without rebuilding the image.
+ It supports Batch execution.

### Demo
In the following video we will show how you can deploy a containerized application on __Kubernetes__.

[video][vid2]

### Benefits of Using Kubernetes
Some of the benefits of using __Kubernetes__ are:

+ It is an Open Source system that packages all the necessary tools: orchestration, service discovery, load balancing.
+ It manages multiple containers at scale.
+ It automates deployment, scaling, and operations of application containers.
+ It is portable, extensible and self-healing.
+ It provides consistency across development, testing, and production environments.
+ It is highly efficient in utilizing resources.
+ It is highly available.

### References
+ http://kubernetes.io/
+ http://kubernetes.io/docs/
+ https://github.com/kubernetes/kubernetes


## Deploying Containers on Mesos
### Introduction to Apache Mesos
When we install and setup a physical machine, we generally use if for very specific purposes, such as running __Hadoop, Spark__, containers __Jenkins__, etc. Some of them might not be using all the system resources (e.g. CPU, memory) and some might be starving for more. Therefore, it would be helpful to have the ability to combine all the physical resources across all the machines and execute tasks on specific machines, based on the resource requirements. [Apache Mesos][mesos] was created with this in mind, so that we can optimally use the resources available, even if we are running disparate applications on a pool of nodes.

[Apache Mesos][mesos] helps us treat a cluster of nodes as one big computer, which manages CPU, memory, and other resources across a cluster. __Mesos__ provides functionality that crosses between __Infrastructure as a Service (IaaS)__ and __Platform as a Service (PaaS)__. It is an Open Source __Apache__ project.

### Mesos Components
Next, we will provide details on __Mesos__ components, which are illustrated in Figure 7.4. 

+ __Master__

    Master nodes are the brain of the cluster and provide a single source of truth for running tasks. There is one active master node at any point in time. The master node mediates between __schedulers__ and __slaves__. Slaves advertise their resources to the master node, then the master node forwards them to the scheduler. Once the scheduler accepts the offer, it sends the task to run on the slave to the master, and the master forwards these tasks to the slave.

+ __Slave__

    Slaves manage resources at each machine level and execute the tasks submitted via the scheduler.

+ __Frameworks__

    Frameworks are distributed applications that solve a specific use case. They consist of a scheduler and an __executor__. The scheduler gets a resource offer, which it can accept or decline. The executor runs the job on the slave, which the scheduler schedules. There are many existing frameworks and we can also create custom ones. Some of the existing frameworks are: __Hadoop, Spark, Marathon, Chronos, Jenkins, Aurora__, and many more.

+ __Executor__

    Executors are used to run jobs on slaves. They can be __SHELL__ scripts, __Docker__ containers, and programs written in different languages (e.g. __Java__).

![image][img4]

Figure 7.4: __Mesos__ Components (by __The Apache Software Foundation__, retrieved from [mesos.apache.org][mescomp])

### Mesos Features
__Mesos__ has the following features:

+ It can scale to 10,000 nodes.
+ It uses __ZooKeeper__ for fault-tolerant replicated master and slaves.
+ It provides support for __Docker__ containers.
+ It enables native isolation between tasks with __Linux Containers__.
+ It allows multi-resource scheduling (memory, CPU, disk, and ports).
+ It uses __Java, Python__ and __C++__ APIs for developing new parallel applications.
+ It uses __WebUI__ for viewing cluster statistics.

__Mesos__ ships binaries for different components (e.g. master, slaves, frameworks, etc.), which we can bind together to create our __Mesos Cluster__. The __Apache Mesos__ website has detailed documentation to do the setup.

### Mesosphere DC/OS
[Mesosphere][mesph] offers a commercial solution on top of __Apache Mesos__. __Mesosphere__ is one of the primary contributors to the __Mesos__ project and to frameworks like __Marathon__. Their commercial product, [Mesosphere Enterprise DC/OS][mesent], offers a one-click install and enterprise features like security, monitoring, user interface, etc. on top of __Mesos__. 

__DC/OS__ has recently been [open-sourced by Mesosphere][mesopen].

By default, __DC/OS__ comes with the __Marathon__ framework and others can be added as required.

The __Marathon__ framework has the following features:

+ It starts, stops, scales, and updates applications.
+ It has a nice web interface, API.
+ It is highly available, with no single point of failure.
+ It uses native __Docker__ support.
+ It supports rolling deploy/restart.
+ It allows application health checks.
+ It provides artifact staging.

### Mesosphere DC/OS Architecture
We will now discuss the __Mesosphere DC/OS__ architecture. There are two main components: the __DC/OS Master__ and the __DC/OS Agents__.

The __DC/OS Master__ has the following default components:

+ __Mesos master process__

    It is similar to the master component of Mesos.
+ __Mesos DNS__

    It provides service discovery within the cluster, so applications and services running inside the cluster can reach to each other.

+ __Marathon__

    It is a framework which comes by default with DC/OS and provides the "init system".

+ __ZooKeeper__

    It is a high-performance coordination service that manages the __DC/OS__ services.

+ __Admin router__

    It is an open-source Nginx configuration created by Mesosphere, providing central authentication and proxy to __DC/OS__ services within the cluster.

The __DC/OS Agent__ nodes have the following components:

+ __Mesos agent process__

    It runs the `mesos-slave` process, which is similar to the __slave__ component of __Mesos__.

+ __Mesos containerizer__

    It provides lightweight containerization and resource isolation of executors, using __Linux__-specific functionality, such as __cgroups__ and namespaces.

+ __Docker container__

    It provides support for launching tasks that contain __Docker__ images.

__DCOS__ has its own [command line][dcoscmd] and web [interfaces][dcosui] and comes with a simple packaging and installation.

### Demo
In the following video we will learn how we can deploy containers on __Mesos__, using its __Marathon__ framework.

[video][vid3]

### Benefits of Using Mesos
Some of the benefits of using __Mesos__ are:

+ It is an Open Source solution, but it also has a commercial version.
+ It provides support for __Docker__ containers.
+ It allows multi-resource scheduling.
+ It is highly available and scalable.
+ It provides service discovery and load balancing.

### References
+ http://mesos.apache.org/
+ https://mesosphere.com/
+ https://docs.mesosphere.com/overview/architecture/


## Nomad by Hashicorp
### Introduction to Nomad
__Nomad__ is a cluster  manager and resource scheduler from __HashiCorp__, which is distributed, highly available, and scales to thousands of nodes. It is especially designed to run micro-services and batch jobs. It supports different workloads, like containers (Docker), VMs, and individual applications. 

It is distributed as a single binary which has all of its dependency and runs in a server and client mode. To submit a job, the user has to define it using a declarative language called [HashiCorp Configuration Language (HCL)][hcl] with its resource requirements. Once submitted, __Nomad__ will find available resources in the cluster and run it to maximize the resource utilization.

Below we provide a sample job file:
```c
# Define the hashicorp/web/frontend job
job "hashicorp/web/frontend" {
    # Run in two datacenters
    datacenters = ["us-west-1", "us-east-1"]

    # Only run our workload on linux
    constraint {
        attribute = "$attr.kernel.name"
        value = "linux"
    }

    # Configure the job to do rolling updates
    update {
        # Stagger updates every 30 seconds
        stagger = "30s"

        # Update a single task at a time
        max_parallel = 1
    }

    # Define the task group
    group "frontend" {
        # Ensure we have enough servers to handle traffic
        count = 10

        task "web" {
            # Use Docker to run our server
            driver = "docker"
            config {
                image = "hashicorp/web-frontend:latest"
            }

            # Ask for some resources
            resources {
                cpu = 500
                memory = 128
                network {
                    mbits = 10
                    dynamic_ports = ["http"]
                }
            }
        }
    }
} 
```
which would use 10 containers from the `hashicorp/web-frontend:latest` __Docker__ image.

### Features
Among the characteristics of __Nomad__ are the following:

+ It handles both cluster management and resource scheduling.
+ It supports multiple workloads, like containers (Docker), VMs, unikernels, and individual applications.
+ It ships with just one binary for both the server and the client daemon, which reduces the cost of operations.
+ It has multi-datacenter and multi-region support. We can have a Nomad client/server running in different clouds, which form the same logical Nomad cluster.
+ It bin-packs applications onto servers to achieve high resource utilization.

### Demo
In the following demo we will show how you can deploy a containerized application using __Nomad__.

[video][vid4]

### Benefits of Using Nomad
Some of the benefits of using __Nomad__ are:

+ It is an Open Source solution that is distributed as a single binary for server and agents.
+ It is highly available and scalable.
+ It maximizes resource utilization.
+ It provides multi-datacenter and multi-region support.
+ When maintenance is done, there is zero downtime to the datacenter and services.
+ It simplifies operations, provides flexible workloads, and fast deployment.

### References
+ https://www.hashicorp.com/blog/nomad.html
+ https://nomadproject.io


## Amazon ECS
### Introduction to Amazon ECS
__Amazon ECS__ is part of the __Amazon Web Services (AWS)__ offerings to provide container orchestration and management on top of the __EC2__ instances, using Docker.

### Amazon ECS Components
Figure 7.6 illustrates the Amazon ECS architecture:

![image][img5]

Figure 7.6: Amazon ECS Components (by Amazon Web Services, Inc., retrieved from [LinkedIn SlideShare][ecscomp]) 

Next, we will discuss in more detail some of its components:

+ Cluster

    It is a logical grouping of container instances on which tasks are placed.

+ Container instance

    It is an EC2 instance with an ECS agent that has been registered with a cluster.

+ Task definition

    It specifies the blueprint of an application, which consists of one or more containers. Below, you can see an example of a sample __task definition__ file (from [docs.aws.amazon.com][awsdoc]):
    ```jason
    {
    "containerDefinitions": [
    {
        "name": "wordpress",
        "links": [
        "mysql"
        ],
        "image": "wordpress",
        "essential": true,
        "portMappings": [
        {
            "containerPort": 80,
            "hostPort": 80
        }
        ],
        "memory": 500,
        "cpu": 10
    },
    {
        "environment": [
        {
            "name": "MYSQL_ROOT_PASSWORD",
            "value": "password"
        }
        ],
        "name": "mysql",
        "image": "mysql",
        "cpu": 10,
        "memory": 500,
        "essential": true
    }
    ],
    "family": "hello_world"
    }
    ```

+ Scheduler 

    It places tasks on the container instances. The following scheduling options are provided on ECS:

    - Service scheduler.
    - RunTask action.
    - StartTask action.

+ Service

    It allows one or more instances of tasks to run, depending on the task definition. Below you can see the template of a service definition (from [docs.aws.amazon.com][awssvc]). If there is an unhealthy task, then the __service__ restarts it again. One __load balancer (ELB)__ is attached to each service.
    ```jason
    {
        "cluster": "",
        "serviceName": "",
        "taskDefinition": "",
        "loadBalancers": [
            {
                "loadBalancerName": "",
                "containerName": "",
                "containerPort": 0
            }
        ],
        "desiredCount": 0,
        "clientToken": "",
        "role": "",
        "deploymentConfiguration": {
            "maximumPercent": 200,
            "minimumHealthyPercent": 100
        }
    }
    ```

+ Task

    It is a running container instance from the task definition.

+ Container

    It is a Docker container created from the task definition.

### Amazon ECS Features
Among the features of _Amazon ECS_ are the following:

+ It is compatible with Docker, as each Amazon ECS instance runs the __Docker Daemon__.
+ It provides a managed cluster, so that users do not have to worry about managing and scaling the cluster.
+ __Task definition__ allows the user to define the applications through a `.json` file. Shared data volumes,  as well as resource constraints for Memory and CPU can also be defined in the same file.
+ It provides APIs to manage clusters, tasks, etc.
+ Amazon ECS __scheduler__ places containers based on resource needs and availability requirements. It also has provisions to integrate with third party schedulers, like __Mesos Marathon__.
+ Amazon ECS allows easy updates of containers to new versions.
+ The __Amazon ECS CLI__ is compatible with __Docker Compose__.
+ The monitoring feature is available through __AWS CloudWatch__.
+ The logging facility is available through __AWS CloudTrail__.
+ It supports third party __Docker Registry__ or __Docker Hub__.

### Demo
In the following demo we will show how you can deploy a containerized application using __Amazon Container Service (Amazon ECS)__.

[video][vid5]

### Benefits of Using Amazon ECS
Some of the benefits we can get from using __Amazon ECS__ are:

+ It provides a managed cluster.
+ It is built on top of Amazon EC2.
+ It is highly available and scalable.
+ It leverages other AWS services, such as __Cloud Watch Metrics__.

### References
+ https://aws.amazon.com/ecs/details/
+ http://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html


## Google Container Engine
### Introduction to Google Container Engine
[__Google Container Engine (GKE)__][gke] is a fully-managed solution for running __Kubernetes__ on __Google Cloud__. As we learned earlier, Kubernetes is used for automating deployment, operations, and scaling of containerized applications.

### GKE Features and Benefits
Some of the features and benefits of the __Google Container Engine__ are listed below:

+ It has all of __Kubernetes'__ features.
+ It is a fully-managed service, so the users do not have to worry about managing and scaling the cluster.
+ We can store images privately, using the private container registry.
+ Logging can be enabled easily using __Google Cloud Logging__.
+ It supports __Hybrid Networking__ to reserve an IP address range for the container cluster.
+ It enables a fast setup of managed clusters. 
+ It facilitates increased productivity for Dev and Ops teams.

### References
+ https://cloud.google.com/container-engine/


## Azure Container Service
### Introduction to Azure Container Service
[__Azure Container Service (ACS)__][acs] simplifies the creation, configuration, and management of containerized applications on __Microsoft Azure__.

It either uses __Apache Mesos__ or __Docker Swarm__ to orchestrate applications, which are containerized using the __Docker runtime__. For __Mesos__, ACS includes the __Marathon__ and __Chronos__ frameworks by default. __Apache Mesos__ and __Docker Swarm__ clusters can be accessed by __DC/OS CLI__ and __Docker CLI__ respectively.

![image][img6]

Figure 7.7: The __ACS Cluster__ (by Microsoft, retrieved from [azure.microsoft.com][acsclu])

In __Azure__ and __Azure Stack__, the [__Azure Resource Manager__][acsrsc] represents the management layer (API), which allows us to connect to our deploying resources. ACS has templates for both __Mesos__ and __Docker Swarm__, which [can be used to deploy][acsdep] the cluster on top of VMs.

### ACS Features and Benefits
Among the features and benefits of __ACS__, it is important to mention the ones below:

+ It can easily manage containerized applications on the Microsoft Azure platform.
+ It allows for an easy deployment of container orchestration tools: __Apache Mesos Marathon__ and __Docker Swarm__.
 
### Demo
In the following video we will show how you can deploy containers using __Microsoft's Azure Container Service__.

[video][vid6]

### References
+ https://azure.microsoft.com/en-in/documentation/services/container-service
+ https://azure.microsoft.com/en-in/documentation/articles/container-service-deployment/

## Knowledge Check
1. We cannot have more than one Swarm Manager when we configure the container clustering via Docker Swarm. 

        Ans: False
        Explain: one or more Swarm Managers with active/passive mode

2. In Kubernetes, a Pod consists of ____________. Please choose the correct answer from the dropdown menu.

        Ans: A pod consists of one or more containers.

3. Which framework is used by Mesos to schedule containers? Please select the correct answer.

A. Hadoop
B. Chronos
C. Marathon
D. Jenkins

Ans: C

3. Which container orchestration engine is supported by Azure Container Service? Please select all  answers that apply.
        A. Docker Swarm
        B. Kubernetes
        C. Amazon ECS
        D. Mesos Marathon

        Ans: A, D
        Explanation
        Docker Swarm and Mesos Marathon are container orchestration engines supported by Azure Container Service.




[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V003400_DTH.mp4
[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V001500_DTH.mp4
[vid3]: https://edx-video.net/LINLFS15/LINLFS152016-V003300_DTH.mp4
[vid4]: https://edx-video.net/LINLFS15/LINLFS152016-V002500_DTH.mp4
[vid5]: https://edx-video.net/LINLFS15/LINLFS152016-V002600_DTH.mp4
[vid6]: https://edx-video.net/LINLFS15/LINLFS152016-V003100_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8b5dbcc9d903ba0d592ece5adfb30b20/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Components_of_a_Docker_Swarm_Cluster.jpg
[img2]: https://docs.docker.com/machine/img/provision-use-case.png
[img3]: http://blog.arungupta.me/wp-content/uploads/2015/01/kubernetes-architecture.png
[img4]: http://mesos.apache.org/assets/img/documentation/architecture3.jpg
[img5]: http://www.allthingsdistributed.com/images/ecs1.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0a8a441c624f75e936547c2b5e369625/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Figure_7.7-_The_ACS_Cluster.png

[swarmsvc]: https://docs.docker.com/swarm/discovery/
[libkv]: https://github.com/docker/libkv
[libnet]: https://github.com/docker/libnetwork
[docmach]: https://docs.docker.com/machine/overview/
[doccomp]: https://docs.docker.com/compose/overview/
[cncf]: https://cncf.io/
[first]: http://www.linuxfoundation.org/news-media/announcements/2016/03/cloud-native-computing-foundation-accepts-kubernetes-first-hosted-0
[kuberarch]: http://blog.arungupta.me/wp-content/uploads/2015/01/kubernetes-architecture.png
[kuberep]: http://kubernetes.io/docs/user-guide/replicasets/
[repctl]: http://kubernetes.io/docs/user-guide/replication-controller/
[labusr]: http://kubernetes.io/docs/user-guide/labels/#label-selectors
[kubedep]: http://kubernetes.io/docs/user-guide/deployments/
[kubepod]: http://kubernetes.io/docs/user-guide/pods/
[kubesmp]: http://kubernetes.io/docs/user-guide/deployments/
[docvol]: https://docs.docker.com/userguide/dockervolumes/
[mesos]: http://mesos.apache.org/
[mescomp]: http://mesos.apache.org/assets/img/documentation/architecture3.jpg
[mesph]: https://mesosphere.com/product/
[mesent]: https://mesosphere.com/enterprise/
[mesopen]: https://mesosphere.com/blog/2016/04/19/open-source-dcos/
[dcoscmd]: https://docs.mesosphere.com/usage/cli/
[dcosui]: https://docs.mesosphere.com/usage/webinterface/
[hcl]: https://github.com/hashicorp/hcl
[ecscomp]: http://www.slideshare.net/AmazonWebServices/amazon-ec2-container-service-deep-dive
[awsdoc]: http://docs.aws.amazon.com/AmazonECS/latest/developerguide/example_task_definitions.html
[awssvc]: http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_paramters.html
[gke]: https://cloud.google.com/container-engine/
[acs]: https://azure.microsoft.com/en-in/documentation/services/container-service/
[acsclu]: https://acom.azurecomcdn.net/80C57D/cdn/mediahandler/docarticles/dpsmedia-prod/azure.microsoft.com/en-us/documentation/articles/container-service-intro/20160325103110/acs-cluster.png
[acsrsc]: https://azurestack.eu/2015/06/azure-resource-manager-templates-json/
[acsdep]: https://azure.microsoft.com/en-in/documentation/articles/container-service-deployment/

