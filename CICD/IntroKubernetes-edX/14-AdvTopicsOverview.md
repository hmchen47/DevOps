Advanced Topics - Overview
==========================

## Introduction
So far, in this course, we have spend most of our time understanding the basic Kubernetes concepts and simple workflows to build a solid foundation. To support enterprise class production workloads, Kubernetes can do auto-scaling, rollbacks, quota management, RBAC, etc. In this chapter, we will get a high-level overview about such advanced topics, but diving into details would be out of scope for this course. 

## Learning Objectives
+ Discuss advanced Kubernetes concepts: DaemonSets, StatefulSets, Helm, etc.

## Annotations
With [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/), we can attach arbitrary non-identifying metadata to objects, in a key-value format:
```json
"annotations": {
  "key1" : "value1",
  "key2" : "value2"
}
```

In contrast to Labels, annotations are not used to identify and select objects. Annotations can be used to:

+ Store build/release IDs, PR numbers, git branch, etc.
+ Phone/pager numbers of persons responsible, or directory entries specifying where such information can be found
+ Pointers to logging, monitoring, analytics, audit repositories, debugging tools, etc.
+ Etc.

For example, while creating a Deployment, we can add a description like the one below:
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
    name: webserver
    annotations:
        description: Deployment based PoC dates 2nd June'2017
....
....
```
We can look at annotations while describing an object:
```bash
$ kubectl describe deployment webserver
Name:                webserver
Namespace:           default
CreationTimestamp:   Sat, 03 Jun 2017 05:10:38 +0530
Labels:              app=webserver
Annotations:         deployment.kubernetes.io/revision=1
                     description=Deployment based PoC dates 2nd June'2017
...
...
```

## Deployment Features
Earlier, we have seen how we can use the Deployment object to deploy an application. This is just a basic functionality. We can do more interesting things, like recording a Deployment - if something goes wrong, we can revert to the working state.

The graphic below depicts a situation in which our update fails:

![Deployment update fails](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e125eb20e6c5a6a46b29008db6c99276/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/deploymentrollback1.png)

If we have recorded our Deployment before doing the update, we can revert back to a known working state.

![Deployment Rollback](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/11c1c84cf42ea7c18f91c69781d8b74d/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/deploymentrollback2.png)

In addition, the Deployment object also provides the following features:

+ Autoscaling
+ Proportional scaling
+ Pausing and resuming.

To learn more, check out the available [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#scaling-a-deployment).

## Jobs
A [Job](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#what-is-a-job) creates one or more Pods to perform a given task. The Job object takes the responsibility of Pod failures. It makes sure that the given task is completed successfully. Once the task is over, all the Pods are terminated automatically.

Starting with the Kubernetes 1.4 release, we can also perform Jobs at specified times/dates, such as [cron jobs.](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) 

## Quota Management
When there are many users sharing a given Kubernetes cluster, there is always a concern for fair usage. A user should not take undue advantage. To address this concern, administrators can use the [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) object, which provides constraints that limit aggregate resource consumption per Namespace.

We can have the following types of quotas per Namespace:

+ __Compute Resource Quota__: We can limit the total sum of compute resources (CPU, memory, etc.) that can be requested in a given Namespace.
+ __Storage Resource Quota__: We can limit the total sum of storage resources (persistentvolumeclaims, requests.storage, etc.) that can be requested.
+ __Object Count Quota__: We can restrict the number of objects of a given type (pods, ConfigMaps, persistentvolumeclaims, ReplicationControllers, Services, Secrets, etc.).

## DaemonSets
In some cases, like collecting monitoring data from all nodes, or running a storage daemon on all nodes, etc., we need a specific type of Pod running on all nodes at all times. A [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) is the object that allows us to do just that. 

Whenever a node is added to the cluster, a Pod from a given DaemonSet is created on it. When the node dies, the respective Pods are garbage collected. If a DaemonSet is deleted, all Pods it created are deleted as well.

## StatefulSets
Before Kubernetes 1.5, the [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) controller was referred to as PetSet. The StatefulSet controller is used for applications which require a unique identity, such as name, network identifications, strict ordering, etc. For example, `MySQL cluster`, `etcd cluster`.

The StatefulSet controller provides identity and guaranteed ordering of deployment and scaling to Pods.

## Role Based Access Control (RBAC)
[Role-based access control](https://kubernetes.io/docs/admin/authorization/rbac/) (RBAC) is an authorization mechanism for managing permissions around Kubernetes resources. It is added as a beta resource in Kubernetes 1.6 release.

Using the RBAC API, we define a role which contains a set of additive permissions. Within a Namespace, a role is defined using the _Role_ object. For a cluster-wide role, we need to use the _ClusterRole_ object.

Once the roles are defined, we can bind them to a user or a set of users using _RoleBinding_ and _ClusterRoleBinding_.

## Kubernetes Federation
With the [Kubernetes Cluster Federation](https://kubernetes.io/docs/concepts/cluster-administration/federation/) we can manage multiple Kubernetes clusters from a single control plane. We can sync resources across the clusters, and have cross cluster discovery. This allows us to do Deployments across regions and access them using a global DNS record.

The Federation is very useful when we want to build a hybrid solution, in which we can have one cluster running inside our private datacenter and another one on the public cloud. We can also assign weights for each cluster in the Federation, to distribute the load as per our choice.

## Third Party Resources (Objects)
In most cases, the existing Kubernetes objects are sufficient to fulfill our requirements to deploy an application, but we also have the flexibility to do more. Using the [ThirdPartyResource](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-third-party-resource/) object type, we can create our own API objects. In this case, we will need to write a controller, which can listen to their creation/update/deletion. The controller would then perform operations accordingly.

For example, the [etcd-operator](https://github.com/coreos/etcd-operator) uses the ThirdPartyResource to create objects, and, depending on that, its controller creates/configures/manages etcd clusters on top of Kubernetes.

ThirdPartyResource is getting deprecated with Kubernetes 1.7. A new object type called __Custom Resource Definition (CRD)__ is getting introduced in beta with the Kubernetes 1.7 release, which will help you create new custom resources. CRD will replace the ThirdPartyResource object in the next few releases. For more details, please checkout out the [example from CoreOS.](https://coreos.com/blog/custom-resource-kubernetes-v17) 

## Helm
To deploy an application, we use different Kubernetes manifests, such as Deployments, Services, Volume Claims, Ingress, etc. Sometimes, it can be tiresome to deploy them one by one. We can bundle all those manifests after templatizing them into a well-defined format, along with other metadata. Such a bundle is referred to as _Chart_. These Charts can then be served via repositories, such as those that we have for `rpm` and `deb` packages. 

[Helm](https://github.com/kubernetes/helm) is a package manager (analogous to `yum` and `apt`) for Kubernetes, which can install/update/delete those Charts in the Kubernetes cluster.

Helm has two components:

+ A client called _helm_, which runs on your user's workstation
+ A server called _tiller_, which runs inside your Kubernetes cluster.

The client _helm_ connects to the server _tiller_ to manage Charts. Charts submitted for Kubernetes are available [here](https://github.com/kubernetes/charts).

## Monitoring and Logging
In Kubernetes, we have to collect resource usage data by Pods, Services, nodes, etc, to understand the overall resource consumption and to take decisions for scaling a given application. Two popular Kubernetes monitoring solutions are _Heapster_ and _Prometheus_.

[Heapster](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-usage-monitoring/) is a cluster-wide aggregator of monitoring and event data, which is natively supported on Kubernetes. 

[Prometheus](https://prometheus.io/), now part of [CNCF](https://www.cncf.io/) (Cloud Native Computing Foundation), can also be used to scrape the resource usage from different Kubernetes components and objects. Using its client libraries, we can also instrument the code of our application.

Another important aspect for troubleshooting and debugging is Logging, in which we collect the logs from different components of a given system. In Kubernetes, we can collect logs from different cluster components, objects, nodes, etc. The most common way to collect the logs is using [Elasticsearch](https://kubernetes.io/docs/tasks/debug-application-cluster/logging-elasticsearch-kibana/), which uses [fluentd](http://www.fluentd.org/) with custom configuration as an agent on the nodes. __fluentd__ is an open source data collector, which is also part of CNCF.

