Kubernetes Volume Management
============================

## Introduction
To back a Pod with a persistent storage, Kubernetes uses __Volumes__. In this chapter, we will learn about Volumes and their types. We will also discuss about __Persistent Volume__ and __Persistent Volume Claim__ objects, which help us attach storage volumes to Pods. 

## Learning Objectives
+ Explain the need for persistent data management.
+ Discuss Kubernetes Volume and its types.
+ Discuss Persistent Volumes and Persistent Volume Claims.

## Volumes
As we know, containers, which create the Pods, are ephemeral in nature. All data stored inside a container is deleted if the container crashes. However, `kubelet` will restart it with a clean state, which means that it will not have any of the old data.

To overcome this problem, Kubernetes uses [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/). A Volume is essentially a directory backed by a storage medium. The storage medium and its content are determined by the Volume Type.

![Volume](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f8ef48bf4407f52f960fda25652ed324/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/volumes.jpg)

In Kubernetes, a Volume is attached to a Pod and shared among the containers of that Pod. The Volume has the same life span as the Pod, and it outlives the containers of the Pod - this allows data to be preserved across container restarts.

## Volume Types
A directory which is mounted inside a Pod is backed by the underlying Volume Type. A Volume Type decides the properties of the directory, like size, content, etc. Some of the Volume Types are:

+ `emptyDir`

    An `empty` Volume is created for the Pod as soon as it is scheduled on the Worker Node. The Volume's life is tightly coupled with the Pod. If the Pod dies, the content of emptyDir is deleted forever.

+ `hostPath`

    With the `hostPath` Volume Type, we can share a directory from the host to the Pod. If the Pod dies, the content of the Volume is still available on the host.

+ `gcePersistentDisk`

    With the `gcePersistentDisk` Volume Type, we can mount a [Google Compute Engine (GCE) persistent disk](https://cloud.google.com/compute/docs/disks/) into a Pod.

+ `awsElasticBlockStore`

    With the `awsElasticBlockStore` Volume Type, we can mount an [AWS EBS Volume](https://aws.amazon.com/ebs/) into a Pod.

+ `nfs`

    With [nfs](https://en.wikipedia.org/wiki/Network_File_System), we can mount an NFS share into a Pod.

+ `iscsi`

    With [iscsi](https://en.wikipedia.org/wiki/ISCSI), we can mount an iSCSI share into a Pod.

+ `secret`

    With the `secret` Volume Type, we can pass sensitive information, such as passwords, to Pods. We will take a look at an example in a later chapter.

+ `persistentVolumeClaim`

    We can attach a [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) to a Pod using a `persistentVolumeClaim`. We will cover this in our next section.

You can learn more details about Volume Types in the [Kubernetes Documentation](https://kubernetes.io/docs/concepts/storage/volumes/).

## Persistent Volumes
In a typical IT environment, storage is managed by the storage/system administrators. The end user will just get instructions to use the storage, but does not have to worry about the underlying storage management.

In the containerized world, we would like to follow similar rules, but it becomes challenging, given the many Volume Types we have seen earlier. Kubernetes resolves this problem with the Persistent Volume subsystem, which provides APIs for users and administrators to manage and consume storage. To manage the Volume, it uses the PersistentVolume (PV) API resource type, and to consume it, it uses the PersistentVolumeClaim (PVC) API resource type.

A Persistent Volume is a network attached storage in the cluster, which is provisioned by the administrator.

![Persistent Volume](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6a5fdd4a886946de42f45f19053d1a4c/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/Persistent_Volume.jpg)

Persistent Volumes can be provisioned statically by the administrator, or dynamically, based on the StorageClass resource. A StorageClass contains pre-defined provisioners and parameters to create a Persistent Volume.

Some of the Volume Types that support managing storage using Persistent Volumes are:

+ GCEPersistentDisk
+ AWSElasticBlockStore
+ AzureFile
+ NFS
+ iSCSI
+ CephFS
+ Cinder

For a complete list, as well as more details, you can check out the Kubernetes Documentation.

## Persistent Volume Claims
A PersistentVolumeClaim (PVC) is a request for storage by a user. Users request for Persistent Volume resources based on size, access modes, etc. Once a suitable Persistent Volume is found, it is bound to a Persistent Volume Claim.

![Persistent Volume Claim](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8a09bc09358d8d677608c412510d2ecb/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/Persistent_Volume_Claim_1.jpg)

After a successful bind, the PersistentVolumeClaim resource can be used in a Pod.

![Persistent Volume Claim used in a Pod](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9002609cfc5f59584c82544a336e21a5/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/Persistent_Volume_Claim_used_in_a_Pod__2_.jpg)

Once a user finishes its work, the attached Persistent Volumes can be released. The underlying Persistent Volumes can then be reclaimed and recycled for future usage. 

To learn more, you can check out the [documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).

## Using the hostPath Volume Type Demo
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://youtu.be/6Z1CrunVg2w)

## Knowledge Check 
Q1. Inside a Pod, a Volume is shared among containers. True or False?

    Ans: True

Q2. Which of the following is a valid VolumeType? Select all answers that apply.

    A. emptyDir
    B. hostPath
    C. secret
    D. persistentVolumeClaim

    Ans: a, b, c, d

Q3. How can Persistent Volumes be provisioned? Select all answers that apply.

    A. Statically
    B. Dynamically
    C. None of the above

    Ans: a, b

