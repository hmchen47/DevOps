# Chapter 16. Tools for Cloud Infrastructure III (Key-Value Pair Store)

## Introduction and Learning Objectives
### Tools for Cloud Infrastructure: Key-Value Pair Store
While building any distributed and dynamically-scalable environment, we need an endpoint which is a single point of truth. For example, we need such an endpoint if we want each node in a distributed environment to look up for some value before doing an operation. For such cases, all the nodes can reach out to a central location and get the value of a given variable/key.

As the name suggests, the __Key-Value Pair Storage__ provides the functionality to store or retrieve the `value` of a `key`. Most of the `Key Value` stores provide REST APIs to do operations like `GET`, `PUT`, `DELETE` etc., which helps when doing all the operations over `HTTP`. Some examples of Key-Value stores are:

+ __etcd__
+ __Consul__.

## Learning Objectives
By the end of this chapter you should be able to:

+ Discuss and use key-value store tools like __etcd__ and __Consul__.


## etcd
### Introduction to etcd
[__etcd__][etcd] is an Open Source distributed key-value pair storage, which is based on the [Raft consensus algorithm][raft]. It was started by [CoreOS][coreos] and it is written in __Go__.

### Features
__etcd__ can be configured to run standalone or in a cluster. In a cluster mode, it can gracefully handle the master election during network partitions and can tolerate machine failures, including the master.

We can also watch on a value of a key, which allows us to do certain operations based on the value change.

It is currently being used in many projects like __Kubernetes, Fleet, Locksmith, vulcand__.

### Use Cases
Some of the cases in which etcd is used are:

+ Store connections, configuration and other settings
+ Service Discovery in conjunction with tools like __skyDNS__.

### Benefits of Using __etcd__
Some of the benefits of using __etcd__ are:

+ It is an Open Source _distributed key-value pair_ storage.
+ It provides reliable data storage across a cluster of machines.
+ It is easy to deploy, setup, and use.
+ It provides seamless cluster management across a distributed system.
+ It is secure and offers very good documentation.

### References
+ https://github.com/coreos/etcd
+ https://coreos.com/etcd/


## Consul
### Introduction to Consul
[Consul][consul] is a distributed, highly-available system which can be used for service discovery and configuration.

Other than providing a distributed key-value store, it also provides features like:

+ Service discovery in conjunction with DNS or HTTP
+ Health checks for services and nodes
+ Multi-datacenter support.

__Consul__ can be configured on a single node or on multi-nodes, which is recommended. Consul is built on top of [Serf][serf], which provides membership, failure detection, and event broadcast. Consul also uses the [Raft consensus algorithm][raft] for leadership election and consistency.

### Use Cases
Some of the cases in which __Consul__ is used are:

+ Store connections, configuration and other settings
+ Service discovery in conjunction with DNS or HTTP.

### Benefits of Using Consul
Some of the benefits of using __Consul__ are:

+ It is a distributed, highly-available system which can be used for service discovery and configuration.
+ It provides health checks for services and nodes.
+ It provides out-of-the-box native multi-datacenter support.
+ It implements embedded service discovery.

### References
+ https://www.consul.io/docs/index.html


## Knowledge Check
Q. Is etcd based on the Raft Consensus Algorithm?

    Ans: yes



[etcd]: https://github.com/coreos/etcd
[raft]: https://raft.github.io/
[coreos]: https://coreos.com/
[consul]: https://www.consul.io/
[sef]: https://www.serfdom.io/



