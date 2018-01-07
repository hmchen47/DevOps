# Chapter 12. Software Defined Storage and Storage Management for Containers

## Introduction and Learning Objectives
### Software Defined Storage (SDS) and Storage Management for Containers
__Software Defined Storage (SDS)__ is a form of storage virtualization in which storage hardware is separated from the software, which manages it. By doing this, we can bring hardware from different sources and we can manage them with software. Software can provide different features, like replication, erasure coding, snapshot, etc. on top of the pooled resources. Once the pooled storage is configured in the form of a cluster, __SDS__ allows multiple access methods like _File, Block_, and _Object_. 

In this chapter, we will first look at some examples for Software Defined Storage and then dive into storage management for containers.

Some examples of Software Defined Storage are:

+ Ceph
+ Gluster
+ FreeNAS
+ Nexenta
+ VMware  Virtual SAN.

![image][img1]

Figure 12.1: Software Defined Storage (SDS)

### Learning Objectives
By the end of this chapter you should be able to:

+ Discuss the basics of __Software Defined Storage__.
+ Discuss different storage options with containers.

## Ceph
### Introduction to Ceph
According to ceph.com: 

> "__Ceph__ is a distributed object store and file system designed to provide excellent performance, reliability and scalability."

__Ceph__ is an Open Source defined and unified storage solution. It can deliver _Object, Block_ and _File_ system storage.

### Ceph Architecture
Everything in __Ceph__ is stored as objects. __Ceph__ uses the __CRUSH (Controlled Replication Under Scalable Hashing)__ algorithm to deterministically find out, write, and read the location of objects.

![image][img2]

Figure 12.2: Ceph Architecture (by Red Hat, Inc., retrieved ceph.com)

Next, we will take a closer look at Ceph's architecture:

+ __Reliable Autonomic Distributed Object Store (RADOS)__

    It is the object store which stores the objects. This layer makes sure that data is always in a consistent and reliable state. It performs operations like replication, failure detection, recovery, data migration, and rebalancing across the cluster nodes. This layer has the following three major components:

    - __Object Storage Device (OSD)__ - This is where the actual user content is written and retrieved with read operations. One __OSD daemon__ is typically tied to one physical disk in the cluster.
    - __Ceph Monitors (MON)__ - Monitors are responsible for monitoring the cluster state. All cluster nodes report to Monitors. Monitors map the cluster state through the OSD, Place Groups (PG), CRUSH and Monitor maps.
    - __Ceph Metadata Server (MDS)__ - It is needed only by __CephFS__, to store the file hierarchy and metadata for files.

    ![image][img3]

    Figure: 12.3: Components of Storage Clusters (by Red Hat, Inc., retrieved from [ceph.com][csc])

+ __Librados__

    It is a library that allows direct access to RADOS from languages like C, C++, Python, Java, PHP, etc. __Ceph Block Device, RADOSGW__, and __CephFS__ are implemented on top of Librados.

+ __Ceph Block Device__

    This provides the block interface for Ceph. It works as a block device and has enterprise features like thin provisioning and snapshots.

+ __RADOS Gateway (RADOSGW)__

    This provides a REST API interface for Ceph, which is compatible with __Amazon S3__ and __OpenStack Swift__.

+ __Ceph File System (CephFS)__

    This provides a POSIX-compliant distributed filesystem on top of Ceph. It relies on __Ceph MDS__ to track the file hierarchy.

### Demo
Next, we will learn to create a block object using Ceph.

[video][vid2]

### Benefits of Using Ceph
Among the benefits of using __Ceph__ are:

+ It is an Open Source storage solution, which supports _Object, Block_, and _Filesystem_ storage.
+ It runs on any commodity hardware, without any vendor lock-in.
+ It provides data safety for mission-critical applications.
+ It provides automatic balance of filesystems for maximum performance.
+ It is scalable and highly available, with no single point of failure.
+ It is a reliable, flexible, and cost-effective storage solution.

### References
+ ceph.com
+ docs.ceph.com


## Gluster
### Introduction to Gluster
According to gluster.org:

> "__GlusterFS__ is a scalable network filesystem. Using common off-the-shelf hardware, you can create large, distributed storage solutions for media streaming, data analysis, and other data- and bandwidth-intensive tasks. __GlusterFS__ is free and open source software."

### GlusterFS Volumes
To create shared storage, we need to start by grouping the machines in a __Trusted Pool__. Then, we group the directories (called _bricks_) from those machines in a __GlusterFS volume__, using [__FUSE (Filesystem in Userspace)__][fuse]. GlusterFS supports different kinds of volumes:

+ Distributed GlusterFS Volume
+ Replicated GlusterFS Volume
+ Distributed Replicated GlusterFS Volume
+ Striped GlusterFS Volume
+ Distributed Striped GlusterFS Volume.

Figure 12.4 illustrates an example of a distributed GlusterFS volume:

![image][img4]

Figure 12.4: Distributed GlusterFS Volume (by Gluster, Inc., retrieved from [gluster.org][gluster])

GlusterFS does not have a centralized metadata server. It uses an elastic [hashing][hash] algorithm to store files on bricks.

The GlusterFS volume can be accessed using one of the following methods:

+ Native FUSE mount
+ NFS (Network File System)
+ CIFS (Common Internet File System).

### Demo
In the following video we will show how you can mount a GlusterFS volume and look at a file inside it.

[video][vid2]

### Benefits of Using Gluster
Among the benefits of using Gluster are:

+ It is an Open Source storage solution that supports Object, Block, and Filesystem storage.
+ It does not have a metadata server.
+ It is scalable, modular and extensible.
+ It is POSIX-compliant, providing High Availability via local and remote data replication.

### References
+ https://www.gluster.org/
+ http://gluster.readthedocs.org/


## Storage Management for Containers
### Introduction to Storage Management for Containers
Containers are ephemeral in nature, which means that whatever is stored inside the container would be gone as soon as the container is deleted. It is best practice to store data outside the container, which would be accessible even after the container is gone.

In a multi-host environment, containers can be scheduled to run on any host. We need to make sure the data volume required by the container is available on the node on which the container would be running.

In this section, we will see how Docker uses the __Docker Volume__ feature to store persistent data and allows vendors to support their storage to its eco-system, using __Docker Volume Plugins__. We will start by looking into different __Storage Backends__, which Docker supports in order to store images, containers, and other metadata.

### Docker Storage Backends
Docker uses [__Copy-on-write__][cowr] to start containers from images, which means we do not have to copy an image while starting a container. All of the changes done by a container are saved in a filesystem layer. Docker images and containers are stored on the host system and we can choose the storage backend for Docker storage, depending on our requirements. Docker supports the following storage backends on Linux:

+ __AUFS (Another Union File System)__
+ __BtrFS__
+ __Device Mapper__
+ __Overlay__
+ __VFS (Virtual File System)__
+ __ZFS__.

### Docker Volumes
According to the Docker Documentation:

> "A __data volume__ is a specially-designated directory within one or more containers that bypasses the Union File System. Data volumes provide several useful features for persistent or shared data:
>
> + Volumes are initialized when a container is created. If the container’s base image contains data at the specified mount point, that existing data is copied into the new volume upon volume initialization. (Note that this does not apply when mounting a host directory.)
> + Data volumes can be shared and reused among containers.
> + Changes to a data volume are made directly.
> + Changes to a data volume will not be included when you update an image.
> + Data volumes persist even if the container itself is deleted.

Next, we will take a closer look at a few examples of how to create volumes.

### Creating a Container with Volumes
To create a container with volume, we can use either the "`docker run`" or the "`docker create`" commands, like the following:

`$ docker run -d --name web -v /webapp nkhare/myapp`

The above command would create a volume inside the Docker working directory (default to `/var/lib/docker/`) on the host system. We can get the exact path via the "`docker inspect`" command:

`$ docker inspect web`

### Creating a Named Volume
We can give a specific name to a volume and then use it for different operations. To create a named volume, we can run the following command: 

`$ docker volume create --name my-named-volume`

and then later mount it.

### Mounting a Host Directory Inside the Container
We can also mount a host directory inside a container using the volume's feature:

`$ docker run -d --name web -v /mnt/webapp:/webapp nkhare/myapp`

which would mount the host's "`/mnt/webapp`" directory to "`/webapp`", while starting the container.

### Creating a Data Volume Container
If we want to share persistent data across containers or share persistent data with a non-persistent container, then we can use the __Data Volume Container__. A Data Volume Container just creates a volume and does nothing like the following:

`$ docker create -v /dbdata --name dbstore busybox /bin/true`

Now, let's share the volume dbstore container with other containers:

`$ docker run --volumes-from dbstore --name=client1 centos /bin/sh`

`$ docker run --volumes-from dbstore --name=client2 centos /bin/sh`


## Volume Plugins for Docker
### Introduction to Volume Plugins for Docker
We can extend the functionality of the __Docker Engine__ with the use of plugins. With plugins, third-party vendors can integrate their solutions with the Docker eco-system. Docker provides two kinds of plugins, __Network__ and __Volume Plugins__. We have talked about Network Plugins in the previous chapter. Some examples of Volume Plugins are:

+ __Flocker__
+ __GlusterFS__
+ __Blockbridge__
+ __EMC REX-Ray__.

Volume plugins are especially helpful when we migrate a stateful container, like a database, on a multi-host environment. In such an environment, we have to make sure that the volume attached to a container is also migrated to the host where the container is migrated or started afresh.

### Flocker Volume Plugin
According to clusterhq.com,

> "Flocker is an open-source container data volume manager for your Dockerized applications."

A __Flocker Docker Volume__ is referred to as a __dataset__, which can be used with any of the containers in the cluster.

__Flocker__ manages Docker containers and data volumes together. Your volumes would follow the container while doing the migration, if the container (micro-service) is managed by Flocker.

![image][img5]

Figure 12.5: Flocker (by ClusterHQ, retrieved from clusterhq.com)

Flocker is designed to work with existing container tools like __Docker Compose, Docker Swarm, Kubernetes__, and __Mesos__.

In this section we will present the basic use of the Flocker's volume plugin.

### Supported Storage Options for Flocker
Some of the supported storage options for Flocker are:

+ __AWS Elastic Block Storage (EBS)__
+ __OpenStack Cinder__ with any supported backend
+ __EMC ScaleIO, XtremeIO, VMAX__
+ __VMware vSphere__ and __vSan__
+ __NetApp OnTap__.

For a detailed list of supported storage options, please visit the [ClusterHQ website][clhq].

### Demo: Flocker Volume Plugin
In the following demo we will see how we can use Flocker Volume Plugin with Docker.

[video][vid3]

### Flocker References
+ https://github.com/ClusterHQ/flocker 
+ https://clusterhq.com/flocker/introduction/

### GlusterFS Volume Plugin
Earlier in this chapter we saw how we can create a shared storage pool using GlusterFS. Docker provides a plugin for GlusterFS, which we can use to attach/detach storage to one or more containers on-demand.

### Demo: GlusterFS Volume Plugin
In the following demo we will see how we can use the __GlusterFS Volume Plugin__ for Docker to mount the __Gluster Volume__ created on a remote machine to the container.

[video][vid4]

## Knowledge Check
1. Which of the following methods is generally used by Software Defined Storage to allow access to shared content? Please select the correct answer.

        A. File
        B. Block
        C. Object
        D. All of the above

        Ans: A, B, C, D

2. We cannot share a directory of the host system as a volume inside a container, on the same host.

        Ans: False

3. With the Flocker Volume Plugin, ________________. 

        Ans: The volume follows the container.



[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V005100_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V001700_DTH.mp4
[vid3]: https://edx-video.net/LINLFS15/LINLFS152016-V004400_DTH.mp4
[vid4]: https://edx-video.net/LINLFS15/LINLFS152016-V002700_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f68f1ffdbee4d1faa71c4a91ba458264/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/LFS151-SoftwareDefinedStorage_SDS___1_.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3c415636feba4cc561a542f5fe913066/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_12.2_Ceph_Architecture.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b1f87c3f864b3f234318ca325431a479/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_12.3_Components_of_Storage_Clusters.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/af8557ab803967d9e8a9b1c708f499fa/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_12.4-Distributed_GlusterFS_Volume.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/81aff05babcaceb4beb50486ceb811f2/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_12.5_Flocker.jpg

[carch]: http://docs.ceph.com/docs/hammer/_images/stack.png
[csc]: http://docs.ceph.com/docs/master/_images/ditaa-fbe8ee62a8a21a317df92d84a62447c4ecd11e34.png
[gluster]: http://www.gluster.org/community/documentation/index.php/Setting_Volumes
[fuse]: https://en.wikipedia.org/wiki/Filesystem_in_Userspace
[hash]: https://en.wikipedia.org/wiki/Hash_function
[cowr]: https://en.wikipedia.org/wiki/Copy-on-write
[clhq]: https://clusterhq.com/flocker/introduction/#storage-options



