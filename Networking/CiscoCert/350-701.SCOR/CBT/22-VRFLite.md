# 22. VRF-lite

Trainer: Keith Barker


## Introduction to VRF-lite

- Learning goals
  - VRF-lite
  - config VRF-lite
  - VRF-lite on multi-layer switch
  - VRF-lite w/ routing
  - DHCP VRF services


## VRF-lite Overview

- Virtual Routing Forwarding-Light (VRF-lite) fundamentals
  - a feature enabling a service provider to support two or more VPNs whose IP addresses probably overlapped
  - using input interfaces to distinguish routes for different VPNs
  - forming virtual packet-forwarding tables by associating one or more Layer 3 interfaces with each VRF
  - either physical or logical
  - VRF-lite interfaces = L3 interfaces
  - devices including VRF-lite
    - customer edge (CE) devices:
      - providing customer access to the service provider network over a data link to one or more provider edge routers
      - advertising the site’s local routes to the provider edge router
      - learning the remote VPN routes from the advertisements
    - provider edge (PE) routers:
      - exchanging routing information with CE devices by using static routing or a routing protocol
      - only required to maintain VPN routes for those VPNs to which it is directly attached
      - eliminating the need for the PE to maintain all of the service provider VPN routes
      - associated with a single VRF if all of these sites participate in the same VPN
      - mapped to a specified VRF
      - any routers in the service provider network that do not attach to CE devices
  
- Demo: two routing tables w/ vrf-lite
  - a router w/ 2 separated VPNs (blue and pink)
  - R1 w/ global (default) routing table
  - VRF as sub-routing table
  - creating two separated sub-routing tables
  - assigning interfaces which sub-routing table belongs to
    - blue routing table (A): g0/0 and g0/1
    - pink routing table (B): g0/2 and g0/3
  - an interfaces belonging to only one sub-routing table and global routing table
  - MPLS using VRF as part of its solution to separate different customers (VPNs)
  - lite version: only separating routing tables and associated interfaces locally
  - analogy: VLAN on L2 switches

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('page')"
      src   = "img/22-vrflite.png"
      alt   = "VRF-lit for seperated VPNs"
      title = "VRF-lit for seperated VPNs"
    />
  </figure>



## VRF-lite Configuration Basics

- Commands for VRF-lites
  - procedure
    - create VRF
    - assign L2 interfaces to the VRF
  - creating VRF
    - IPv4 only: `ip vrf VRF_NAME`
    - IPv4 and/or IPv6:
      - enable VRF: `vrf definition VRF_NAME`
      - specify address space: `address-family ipv6|ipv6`
  - config each interface: `if) vrf forwarding VRF_NAME`


## VRFs on a Multi-Layer Switch

- VRFs and Multi-layer switches
  - procedure
    - create VRF
    - allocate L3 interfaces
  - create SVI: `int vlan #`
  - associate SVI to designed VRF


## VRF-lite Design

- Plan for VRF-lite
  - cust1 w/ 2 subnets: 10.101.0.0/24 & 10.12.0.0/24
  - cust2 w/ 2 subnets: 10.201.0.0/24 & 10.12.0.0./24
  - not L3 router but switches
  - using VLANs to map for each subnets
    - vlan 101: 10.101.0.0/24
    - vlan 102: 10.12.0.0/24
    - vlan 201: 10.201.0.0/24
    - vlan 202: 10.12.0.0./24
  - create SVI for each vlan
  - vlan 102 & 202 w/ the same IP address space

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('page')"
      src   = "img/22-vrfdemo.png"
      alt   = "Example network for VRF-lite"
      title = "Example network for VRF-lite"
    />
  </figure>


## VRF-lite Implementation

- Demo: config VRF-lite on SW1

  ```bash
  SW1# conf t
  SW1(config)# vrf definition Cust1
  SW1(config-vrf)# description Routing for Cust1
  SW1(config-vrf)# address-family ipv4
  SW1(config-vrf-af)# exit
  SW1(config-vrf)# exit

  SW1(config)# vrf definition Cust2
  SW1(config-vrf)# description Routing for Cust2
  SW1(config-vrf)# address-family ipv4
  SW1(config-vrf-af)# exit
  SW1(config-vrf)# exit

  SW1(config)# vlan 101
  SW1(config-vlan)# name Cust10VLAN-101
  SW1(config-vlan)# vlan 102
  SW1(config-vlan)# name Cust10VLAN-102
  SW1(config-vlan)# vlan 201
  SW1(config-vlan)# name Cust10VLAN-201
  SW1(config-vlan)# vlan 202
  SW1(config-vlan)# name Cust10VLAN-202

  SW1(config)# int g0/0
  SW1(config-if)# switchport trunk encapsulation dot1q
  SW1(config-if)# switchport mode trunk
  SW1(config-if)# exit

  SW1(config)# int vlan 101
  SW1(config-if)# vrf forwarding Cust1
  SW1(config-if)# ip address 10.101.0.1 255.255.255.0
  SW1(config-if)# no shutdown
  SW1(config-if)# exit

  SW1(config)# int vlan 102
  SW1(config-if)# vrf forwarding Cust1
  SW1(config-if)# ip address 10.12.0.1 255.255.255.0
  SW1(config-if)# no shutdown
  SW1(config-if)# exit

  SW1(config)# int vlan 201
  SW1(config-if)# vrf forwarding Cust2
  SW1(config-if)# ip address 10.201.0.1 255.255.255.0
  SW1(config-if)# no shutdown
  SW1(config-if)# exit

  SW1(config)# int vlan 202
  SW1(config-if)# vrf forwarding Cust2
  SW1(config-if)# ip address 10.12.0.1 255.255.255.0
  SW1(config-if)# no shutdown
  SW1(config-if)# exit
  SW1(config)# end

  SW1# show vrf
  Name    Default RD    Protocols   Interfaces
  Cust1   <not set>     ipv4        Vl101
                                    VL102
  Cust2   <not set>     ipv4        Vl201
                                    VL202

  SW1# show ip route
  Gateway of last resort is not set.

  SW1# show ip route vrf Cust1
  Gateway of last resort is not set.
      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
  C    10.12.0.0/24 is directly connected, Vlan102
  L    10.12.0.1/32 is directly connected, Vlan102
  C    10.101.0.0/24 is directly connected, Vlan101
  L    10.101.0.1/32 is directly connected, Vlan101

  SW1# show ip route vrf Cust2
  Gateway of last resort is not set.
      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
  C    10.12.0.0/24 is directly connected, Vlan202
  L    10.12.0.1/32 is directly connected, Vlan202
  C    10.201.0.0/24 is directly connected, Vlan201
  L    10.201.0.1/32 is directly connected, Vlan201
  ```

- Demo: config VRF-lite on SW2
  - same config as SW1 but SVi Ip addresses

  ```bash
  SW2(config)# int vlan 101
  SW2(config-if)# vrf forwarding Cust1
  SW2(config-if)# ip address 10.101.0.2 255.255.255.0
  ...TRUNCATED...
  SW2(config)# int vlan 102
  SW2(config-if)# vrf forwarding Cust1
  SW2(config-if)# ip address 10.12.0.2 255.255.255.0
  ...TRUNCATED...
  SW2(config)# int vlan 201
  SW2(config-if)# vrf forwarding Cust2
  SW2(config-if)# ip address 10.201.0.2 255.255.255.0
  ...TRUNCATED...
  SW2(config)# int vlan 202
  SW2(config-if)# vrf forwarding Cust2
  SW2(config-if)# ip address 10.12.0.2 255.255.255.0
  ...TRUNCATED...

  SW2# show vrf
  Name    Default RD    Protocols   Interfaces
  Cust1   <not set>     ipv4        Vl101
                                    VL102
  Cust2   <not set>     ipv4        Vl201
                                    VL202

  SW2# show ip route vrf Cust1
  Gateway of last resort is not set.
      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
  C    10.12.0.0/24 is directly connected, Vlan102
  L    10.12.0.2/32 is directly connected, Vlan102
  C    10.101.0.0/24 is directly connected, Vlan101
  L    10.101.0.2/32 is directly connected, Vlan101

  SW2# show ip route vrf Cust2
  Gateway of last resort is not set.
      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
  C    10.12.0.0/24 is directly connected, Vlan202
  L    10.12.0.2/32 is directly connected, Vlan202
  C    10.201.0.0/24 is directly connected, Vlan201
  L    10.201.0.2/32 is directly connected, Vlan201

  SW1# show ip route
  Gateway of last resort is not set.
  ```


## VRF-lite Adding Routing

- Demo: config routing per VRF
  - Cust1: OSPF routinng
  - Cust2: EIGRP routing
  - same commands for both switches

  ```bash
  SW1# conf t
  SW1(config)# router ospf 1 vrf Cust1
  SW1(config-router)# network 0.0.0.0 255.255.255.255 area 1
  SW1(config-router)# exit

  SW1(config)# router eigrp Cust2-EIGRP
  SW1(config-router)# address-family ipv4 vrf Cust2 autonomous-system 1
  SW1(config-router-af)# network 0.0.0.0
  SW1(config-router-af)# end

  SW1# show ip ospf neighbor
  Neighbor ID     Pri    State      Dead Time    Address     Interface
  10.101.0.2        1    FULL/DR    00:00:33     10.12.0.2   Vlan102
  10.101.0.2        1    FULL/DR    00:00:35     10.101.0.2  Vlan101

  SW1# show eigrp address-family ipv4 vrf Cust2 interfaces
  EIGRP-IPv4 VR(Cust2-EIGRP) Address-Family Interfaces for AS(1)
             VRF(Cust2)
                      Xmit Queue   PeerQ       Mean  Pacing Time     Multicast    Pending 
  Interface    Peers  Un/Reliable  Un/Reliable SRTT  Un/Reliable     Flow Timer   Services
  Vl201          1        0/0        0/0        14      0/0          127           0 
  Vl202          1        0/0        0/0         0      0/0          127           0

  SW1# show ip eigrp vrf Cust2 neighbors
  EIGRP-IPv4 VR(Cust2-EIGRP) Address-Family Neighbors for AS(1)
             VRF(Cust2)
  H   Address     Interfaces    Hold  Uptime   SRTT    RTO   Q
                                (sec)          (ms)         Cnt
  1   10.12.0.2   Vl202           12  00:03:22    1   4500   0
  0   10.201.0.2  Vl201           13  00:03:22   14    100   0

  ! verify connectivity
  SW1# ping 10.12.0.2
  .....

  SW1# ping vrf Cust1 10.12.0.2
  !!!!!
  ```


## VRF-lite Routing Verification




## DHCP VRF Services




## VRF-lite Summary



