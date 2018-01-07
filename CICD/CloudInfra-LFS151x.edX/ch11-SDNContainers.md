# Chapter 11. Software Defined Networking and Networking for Containers

## Introduction and Learning Objectives
### Software Defined Networking and Networking for Containers
Traditional networks cannot cope with the kind of demand mobile devices, cloud computing, and other similar technologies are generating. With the advancement in compute and storage virtualization, we can quickly meet compute and storage requirements. To connect devices, applications, VMs, and containers, we need a similar level of virtualization in networking. This will allow us to meet the end-to-end business requirements.

__Software Defined Networking (SDN)__ decouples the network control layer from the layer which forwards the traffic. This allows SDN to program the control layer to create custom rules in order to meet the networking requirements.

Part of this course has covered containers extensively. Next, let's take a look at container networking and see how it is one of the use-cases for __SDN__.

### Learning Objectives
By the end of this chapter you should be able to:

+ Define __Software Defined Networking__.
+ Discuss the basics of __Software Defined Networking__.
+ Discuss different networking options with containers.


## Software Defined Networking (SDN)
### SDN Architecture
In Networking we have three planes defined:

+ __Data Plane__

    The Data Plane, also called the __Forwarding Plane__, is responsible for handling data packets and apply actions to them based on rules which we program into lookup-tables.

+ __Control Plane__

    The Control Plane is tasked with calculating and programming the actions for the Data Plane. This is where the forwarding decisions are made and where services (e.g. Quality of Service and VLANs) are implemented.

+ __Management Plane__

    The Management Plane is the place where we can configure, monitor, and manage the network devices.

### Activities Performed by a Network Device
Every network device has to perform three distinct activities:

+ __Ingress and egress packets__

    These are done at the lowest layer, which decides what to do with ingress packets and which packets to forward, based on forwarding tables. These activities are mapped as __Data Plane__ activities. All routers, switches, modem, etc. are part of this plane.

+ __Collect, process, and manage the network information__

    By collecting, processing, and managing the network information, the network device makes the forwarding decisions, which the __Data Plane__ follows. These activities are mapped by the __Control Plane__ activities. Some of the protocols which run on the __Control Plane__ are routing and adjacent device discovery.

+ __Monitor and manage the network__

    Using the tools available in the __Management Plane__, we can interact with the network device to configure it and monitor it with tools like __SNMP (Simple Network Management Protocol)__.

In [__Software Defined Networking__][sdn] we decouple the __Control Plane__ with the __Data Plane__. The Control Plane has a centralized view of the overall network, which allows it to create forwarding tables of interest. These tables are then given to the Data Plane to manage network traffic.

![image][img1]

Figure 11.1: The SDN Framework

The Control Plane has well-defined APIs that take requests from applications to configure the network. After preparing the desired state of the network, the Control Plane communicates that to the Data Plane (also known as the __Forwarding Plane__), using a well-defined protocol like [OpenFlow][openflow].

We can use configuration tools like __Ansible__ or __Chef__ to configure SDN, which brings lots of flexibility and agility on the operations side as well.


## Networking for Containers
### Introduction to Networking for Containers
Similar to VMs, we need to connect containers on the same host and across hosts. The host kernel uses the __Network Namespace__ feature of the Linux Kernel to isolate the network from one container to another on the system. __Network Namespaces__ can be shared as well.

On a single host, when using the __Virtual Ethernet__ (`veth`) feature with Linux bridging, we can give a virtual network interface to each container and assign it an IP address. With Linux Kernel features, like __IPVLAN__, we can configure each container to have a unique and world-wide routable IP address. IPVLAN is a recent feature and support to different container runtimes is coming soon.

As of now, if we want to do multi-host networking with containers, the most common solution is to use some form of __Overlay__ network driver, which encapsulates the Layer 2 traffic to a higher layer. Examples of this type of implementation are the __Docker Overlay Driver, Flannel, Weave__, etc. __Project Calico__ allows multi-host networking on Layer 3 using __BGP (Border Gateway Protocol)__.

### Container Networking Standards
Two different standards have been proposed so far for container networking:

+ __The Container Network Model (CNM)__

    Docker, Inc. is the primary driver for this networking model. It is implemented using the `libnetwork` project, which has the following utilizations:

    - __Null__ - NOOP implementation of the driver. It is used when no networking is required.
    - __Bridge__ - It provides a Linux-specific bridging implementation based in Linux Bridge.
    - __Overlay__ - It provides a multi-host communication over VXLAN.
    - __Remote__ - It does not provide a driver. Instead, it provides a means of supporting drivers over a remote transport, by which we can write third-party drivers.

+ The __Container Networking Interface (CNI) Proposal__ 

    __CoreOS__ is the primary driver for this networking model. It is derived from the __rkt Networking Proposal__. __Kubernetes__ has added support for CNI.

### Service Discovery
Now that we provided an overview on networking, let's take a moment to discuss about __Service Discovery__ as well. This becomes extremely important when we do multi-host networking and use some form of orchestration, like Docker Swarm or Kubernetes. 

__Service Discovery__ is a mechanism by which processes and services can find each other automatically and talk. With respect to containers,  it is used to map a container name with its IP address, so that we can access the container without worrying about its exact location (IP address).

Service Discovery has two parts:

+ __Registration__

    When a container starts, the container scheduler registers the mapping in some key-value store like `etcd` or `Consul`. And, if the container restarts or stops, then the scheduler updates the mapping accordingly.

+ __Lookup__

    Services and applications use _Lookup_ to get the address of a container, so that they can connect to it. Generally, this is done using some kind of __DNS (Domain Name Server)__, which is local to the environment. The DNS used resolves the requests by looking at the entries in the key-value store, which is used for _Registration_. __SkyDNS__ and __Mesos-DNS__ are examples of such DNS services.


## Docker Single Host Networking
### Listing the Available Networks
If we list the available networks after installing the Docker daemon, we should see something like the following:
```bash
$ docker network ls
NETWORK ID          NAME          DRIVER
6f30debc5baf        bridge        bridge
a1798169d2c0        host          host
4eb0210d40bb        none          null
```
`bridge`, `null`, and `host` are different network drivers available on a single host.

### Bridge
Like the hardware bridge, we can emulate a __software bridge__ on a Linux host. It can forward traffic between two networks based on MAC (hardware address) addresses. By default, Docker creates a `docker0` Linux Bridge. All the containers on a single host get an IP address from this bridge, unless we specify some other network with the `--net= option`. Docker uses the Linux's __Virtual Ethernet (veth)__ feature to create two virtual interfaces, one end of which is attached to the container and other end to the `docker0` bridge.

Looking at the network configuration after installing Docker on a single host, we can see the default bridge as illustrated below:

```bash
$ ifconfig
docker0   Link encap:Ethernet  HWaddr 02:42:A9:DB:AF:39
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```

We can create a new container doing the following:

```bash
$ docker run -it --name=c1 busybox /bin/sh
/ # ip a
1: lo: <LOOPBACK,UP,LOWE_UP> mtu 65536 qdisc noqueue qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
7: eth0@if8: <BROADCAST,MULTICAST,UP, LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:2/64 scope link
       valid_lft forever preferred_lft forever
```
As we can see, the new container got the IP address from the private IP address range `172.17.0.0/16`, which is catered by the bridge network.

### Inspecting a Bridge Network
We can inspect a network to get more information about it. In the example below, container c1 is a bridge network.

```bash
$ docker network inspect bridge
[
     {
        "Name": "bridge",
        "Id": "6f30debc5baff467d437e3c7c3de673f21b51f821588aca2e30a7db68f10260c",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16"
                }
            ]
        },
        "Internal": false,
        "Containers": {
            "613f1c7812a9db597e7e0efbd1cc102426edea02d9b281061967e25a4841733f": {
                 "Name": "c1",
                 "EndpointID": "80070f69de6d147732eb119e02d161326f40b47a0cc0f7f14ac7d207ac09a695",
                 "MacAddress": "02:42:ac:11:00:02",
                 "IPv4Address": "172.17.0.2/16",
                 "IPv6Address": ""
             }
         },
         "Options": {
             "com.docker.network.bridge.default_bridge": "true",
             "com.docker.network.bridge.enable_icc": "true",
             "com.docker.network.bridge.enable_ip_masquerade": "true"
             "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
             "com.docker.network.bridge.name": "docker0",
             "com.docker.network.driver.mtu": "1500"
         },
         "Labels": {}
      }
 ]
 ```

### Creating A Bridge Network
We can also create our own bridge network by doing the following:

`docker network create --driver bridge isolated_nw`

which would create its own __Linux Bridge__ on the host system. To create a container and have it use the newly created network, we have to start the container with the `--net=isolated_nw` option:

`$ docker run --net=isolated_nw -itd --name=c2 busybox`

A `bridge` network does not support automatic service discovery, so we have to rely on the legacy `--link` option.

### Null
As the name suggests, NULL means no networking. If we attach a container to a null driver, then it would just get the loopback interface. It would not be accessible from the outside.
```bash
$ docker run -it --name=c3 --net=none busybox /bin/sh
/ # ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 1disc noqueue qlen 1
         link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet ::1/128 scope host
       valid_lft forever preferred_lft forever
```

### Host
Using the `host` driver, we can share the host machine's __network namespace__ with a container. In doing so, the container would have full access to the host's network. We can see below that running an `ifconfig` command inside the container lists all the interfaces of the host system:
```bash
$ docker run -it --name=c4 --net=host  busybox /bin/sh
/ # ifconfig
docker0   Link encap:Ethernet  HWaddr 02:42:A9:DB:AF:39

          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::42:a9ff:fedb:af39/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:536 (536.0 B)  TX bytes:648 (648.0 B)

eth0      Link encap:Ethernet  HWaddr 08:00:27:CA:BD:10
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:feca:bd10/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3399 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2050 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1021964 (998.0 KiB)  TX bytes:287879 (281.1 KiB)

eth1      Link encap:Ethernet  HWaddr 08:00:27:00:42:F9
          inet addr:192.168.99.100  Bcast:192.168.99.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe00:42f9/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:71 errors:0 dropped:0 overruns:0 frame:0
          TX packets:46 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:13475 (13.1 KiB)  TX bytes:7754 (7.5 KiB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:16 errors:0 dropped:0 overruns:0 frame:0
          TX packets:16 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:1021964376 (1.3 KiB)  TX bytes:1376 (1.3 KiB)

vethb3bb730 Link encap:Ethernet  HWaddr 4E:7C:8F:B2:2D:AD
          inet6 addr: fe80::4c7c:8fff:feb2:2dad/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:16 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:648 (648.0 B)  TX bytes:1296 (1.2 KiB)
```

### Sharing Network Namespaces among Containers
Similar to host, we can share the network namespaces among containers. So, two or more containers can have the same network stack and reach each other by referring to localhost.

Let's take a look at its IP address:
```bash
$ docker run -it --name=c5 busybox /bin/sh
/ # ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
        valid_lft forever preferred_lft forever

10: eth0@if11: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.3/16 scope global eth0
        valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:3/64 scope link
        valid_lft forever preferred_lft forever
```
Now, if we start a new container with the `--net=container:CONTAINER` option, we can see that the other container has the same IP address.
```bash
$ docker run -it --name=c6 --net=container:c5 busybox /bin/sh
/ # ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
        valid_lft forever preferred_lft forever

12: eth0@if13: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.3/16 scope global eth0
        valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:3/64 scope link
        valid_lft forever preferred_lft forever
```
__Kubernetes__ uses the feature detailed above to share the same __network namespaces__ among multiple containers in a __pod__.


## Docker Multi-Host Networking
### Introduction to Docker Multi-Host Networking
As mentioned previously in this course, most of the multi-host networking solutions for Docker are based on the Overlay network, in which we encapsulate the container's IP packet inside the host's packet, while sending it over the wire. While receiving, we decapsulate the whole packet and forward the container's packet to the receiving container.

Examples of multi-host networking solutions based on Overlay networks are:

+ __Docker Overlay Driver__
+ __Flannel__
+ __Weave__.

__Project Calico__ uses the __Border Gateway Protocol (BGP)__ to do IP-based routing instead of encapsulation. As it works on Layer 3, it requires some hardware support.

### Docker Overlay Driver
As mentioned in the [Docker documentation][docdoc], the __Docker Overlay Network__ driver supports multi-host networking natively. This is accomplished with _"`libnetwork`, a built-in VXLAN-based overlay network driver, and Docker’s `libkv` library"_.

To configure the __Overlay__ network, we have to first configure a key-value store and connect it with the __Docker Engine__ on each host, so that we can store all the network configurations in a central location. Docker uses `libkv` to configure the key-value store, which currently supports `Consul`, `etcd`, and `Zookeeper` (distributed store). 

![image][img2]

Figure 11.2: The Key-Value Store (by Docker, Inc., retrieved from [docker.com][kvs])

Once the key-value store is configured, we can create an Overlay network with the following command:

`$docker network create --driver overlay multi-host-network`

In the command above, multi-host-network is the network name, which we created.

![image][img3]

Figure 11.3: Docker Overlay Network (by Docker, Inc., retrieved from [docker.com][donet])

To create a container which uses the multi-host Overlay network we created, we have to start the container with a command like the following:

`$ docker run -itd --net=multi-host-network busybox`

All the containers which we created on different hosts using the Overlay network are accessible to each other.

![image][img4]

Figure 11.4: Docker Overlay Network with Connected Containers (by Docker, Inc., retrieved from [docker.com][doncc])

### Demo
In the following video we will see how we can leverage Docker's multi-host networking and connect containers from different hosts.

[video][vid1]

## Docker Networking Plugins
We can extend the functionality of Docker with plugins. __Docker__ provides plugins for `Network` and `Volumes`. Some of the Docker network plugins are:

+ [__Weave Network Plugin__][wnetp]

    [Weave Net][wnet] provides multi-host container networking for Docker. It provides service discovery and does not require any external cluster store to save networking configuration. __Weave Net__ has the __Docker Networking Plugin__, which we can use with __Docker Deployment__.

+ [__Kuryr Network Plugin__][knetp]

    It is part of the __OpenStack Kuryr__ project, which also implements [Libnetwork's][libnet] remote driver API by utilizing [Neutron][neutron], which is OpenStack's networking service. 

We can also write our own driver with __Docker Remote Driver__ APIs. 

### Demo
Next, we will see how we can use the Weave plugin to connect containers from different hosts.

[video][vid2]


## Knowledge Check
1. In Software Defined Networking, we decouple ___________.

        Ans: Control Plane with Data Plane

2. Which of the following network drivers is provided by Docker? Please select all answers that apply.

        A, Null
        B. Overlay
        C. Bridge
        D. Host

        Ans: <A, C, D> ?

3. Can we share network namespaces among containers on the same host?

        Ans: Yes

4. Which key-value library is used by Docker to provide shared storage for configuring multi-host networking using the overlay driver? Please select the correct answer.

        A. libcontainer
        B. libnetwork
        C. libkv
        D. liboverlay

        Ans: C



[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V001600_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V003600_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/75cf2c883adc3d24bb86f506c1c49474/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/LFS151-SDN-Framework.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/700fba20e7da4f61a79e72ad6b558584/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_11.2_-The_Key-Value_Store.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/19315be465385455f8d2506dbe9f1ed4/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_11.3_-_Docker_Overlay_Network.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e1c5d5fb1568606fa3d33bb06a2192c0/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_11.4-_Docker_Overlay_Network_with_Connected_Containers.png

[sdn]: https://en.wikipedia.org/wiki/Software-defined_networking
[openflow]: http://en.wikipedia.org/wiki/OpenFlow
[docdoc]: https://courses.edx.org/courses/course-v1:LinuxFoundationX+LFS151.x+2T2016/courseware/b5d5959248e24467b640307bff6a2890/f4e9dd4c66dd4c07a31b300e773d375a/docs.docker.com/engine/userguide/networking/dockernetworks/
[kvs]: https://docs.docker.com/engine/userguide/networking/images/engine_on_net.png
[donet]: https://docs.docker.com/engine/userguide/networking/images/overlay_network.png
[doncc]: https://docs.docker.com/engine/userguide/networking/images/overlay-network-final.png
[wnetp]: https://github.com/weaveworks/weave/tree/master/plugin
[wnet]: https://www.weave.works/docs/net/latest/introducing-weave/
[knetp]: https://github.com/openstack/kuryr
[libnet]: https://github.com/docker/libnetwork
[neutron]: https://wiki.openstack.org/wiki/Neutron


