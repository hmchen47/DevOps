# 26. EIGRP Neighbor Relationships and Authentication

Trainer: Keith Barker


## Introduction to EIGRP Relationships and Authentication

- Learning goals
  - EIGRP
  - EIGRP neighbors
  - EIGRP authentication
  - config EIGRP neighbor and authentication


## Neighborship Overview

- EIGRP neighbors overview
  - requirements:
    - same autonomous system number w/ multicast addr 224.0.0.10 
    - agreed k values: lowest bandwidth on path, delays
    - authentication
    - ACLs to permit 224.0.0.10 & traffic btw
  - IP mask not critical to form EIGRP neighbor
    - R3 subnet: 10.1.35.0/24
    - R5 subnet: 10.1.35.0/25
    - still able to form EIGRP neighbor

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('page')"
      src    = "img/26-eigrp.png"
      alt    = "Example network for EIGRP neighbors"
      title  = "Example network for EIGRP neighbors"
    />
  </figure>

## Authentication Overview

- EIGRP authentication plan
  - classic mode on R1
  - named mode on R2
  - authenticate R1 & R2
  - IPv4 using AS #4
  - IPv6 using AS #6
  - key chain: 6783 cisco


- Demo: config EIGRP authentication on R1

  ```text
  ! Classic IPv4
  R1# conf t
  R1(config)# router eigrp 4
  R1(config-router)# network 0.0.0.0
  R1(config-router)# end

  ! Classic IPv6
  R1# conf t
  R1(config)# ipv6 unicst-routing
  R1(config)# ipv6 router eigrp 6
  R1(config-rtr)# no shutdown
  R1(config-rtr)# exit
  R1(config)# int gig 0/0
  R1(config-if)# ipv6 eigrp 6
  R1(config-if)# int gig 1/0
  R1(config-if)# ipv6 eigrp 6
  R1(config-if)# int gig 2/0
  R1(config-if)# ipv6 eigrp 6
  R1(config-if)# int gig 4/0
  R1(config-if)# ipv6 eigrp 6
  R1(config-if)# int gig 4/1
  R1(config-if)# ipv6 eigrp 6
  R1(config-if)# int ser 3/1
  R1(config-if)# ipv6 eigrp 6
  R1(config-if)# int ser 3/1
  R1(config-if)# ipv6 eigrp 6
  R1(config-if)# int loop 0
  R1(config-if)# ipv6 eigrp 6
  R1(config-if)# end

  R1# show ip eigrp interfaces
  EIGRP-IPv4 Interfaces for AS(4)
              Xmit    Queue         Peer        Mean  Pacing Time   Multicast   Pending
  Interface   Peers   Un/Reliable   Un/Reliable SRTT  Un/Reliable   Flow Timer  Routes
  Gi0/0         0         0/0        0/0          0      0/0            0          0
  Gi1/0         0         0/0        0/0          0      0/0            0          0
  Gi2/0         0         0/0        0/0          0      0/0            0          0
  Lo0           0         0/0        0/0          0      0/0            0          0

  R1# show ipv6 eigrp interfaces
  EIGRP-IPv4 Interfaces for AS(4)
              Xmit    Queue         Peer        Mean  Pacing Time   Multicast   Pending
  Interface   Peers   Un/Reliable   Un/Reliable SRTT  Un/Reliable   Flow Timer  Routes
  Gi0/0         0         0/0        0/0          0      0/0            0          0
  Gi1/0         0         0/0        0/0          0      0/0            0          0
  Gi2/0         0         0/0        0/0          0      0/0            0          0

  ! config key chain
  R1# conf t
  R1(config)# key chain Demo-Chain
  R1(config-keychain)# key 6783
  R1(config-keychain-key)# key-string cisco
  R1(config-keychain-key)# do show key chain
  Key-chain Demo-Chain:
    key 6783 -- text "cisco"
      accept lieftime (always valid) - (always valid) [valid now]
      send lifetime (always valid) - (always valid) [valid now]

  ! apply key chain to g1/0
  R1(config-keychain-key)# int g1/0
  R1(config-if)# ip authentication key-chain eigrp 4 Demo-Chain
  R1(config-if)# ip authentication mode eigrp 4 md5
  R1(config-if)# end

  ! verify 
  R1# show ip eigrp interfaces detail
  EIGRP-IPv4 Interfaces for AS(4)
              Xmit    Queue         Peer        Mean  Pacing Time   Multicast   Pending
  Interface   Peers   Un/Reliable   Un/Reliable SRTT  Un/Reliable   Flow Timer  Routes
  Gi0/0         0         0/0        0/0          0      0/0            0          0
    <...truncated...>
  Gi1/0         0         0/0        0/0          0      0/0            0          0
    <...truncated...>
    Authentication mode is md5,  key-chain is "Demo-Chain"
  Gi2/0         0         0/0        0/0          0      0/0            0          0
  <...authenticated...>

  ! enable authentication for IPv6
  R1# conf t
  R1(config)# int g1/0
  R1(config-if)# ipv6 authentication key-chain eigrp 6 Demo-Chain
  R1(config-if)# ipv6 authentication mode eigrp 6 md5
  R1(config-if)# end

  R1# show ipv6 eigrp interfaces detail
  EIGRP-IPv4 Interfaces for AS(4)
              Xmit    Queue         Peer        Mean  Pacing Time   Multicast   Pending
  <...truncated...>
  Gi1/0         0         0/0        0/0          0      0/0            0          0
    <...truncated...>
    Authentication mode is md5,  key-chain is "Demo-Chain"
  <...authenticated...>
  ```

- Demo: config EIGRP authentication on R2

  ```text
  ! config key chain
  R2# conf t
  R2(config)# key-chain Demo-Chain
  R2(config-keychain)# key 6783
  R2(config-keychain-key)# key-string cisco
  R2(config-keychain-key)# end

  ! named config
  R2# conf t
  !remove previous protocols
  R2(config)# no router eigrp 4
  R2(config)# no ipv6 router eigrp 6

  R2(config)# ipv6 unicast-routing
  R2(config-router)# router unicast-routing
  R2(config-router)# router eigrp Demo-Named-EIGRP
  R2(config-router)# address-family ipv4 unicast autonomous-system 4
  R2(config-router-af)# network 0.0.0.0
  R2(config-router-af)# exit

  R2(config-router)# do show key chain
  Key-chain Demo-Chain:
    key 6783 -- text "cisco"
      <...truncated..>

  ! apply the key chain for all IPv4 interfaces
  R2(config-router)# address-family ipv4 unicast autonomous-system 4
  R2(config-router-af)# af-interface default
  R2(config-router-af-interface)# authentication mode md5
  R2(config-router-af-interface)# authentication key-chain Demo-Chain
  R2(config-router-af-interface)# address-family ipv6 unicast autonomous-system 6
  R2(config-router-af)# af-interface default
  R2(config-router-af-interface)# authentication mode md5
  R2(config-router-af-interface)# authentication key-chain Demo-Chain
  R2(config-router-af-interface)# end

  R2# show ipv6 eigrp neighbors
  EIGRP-IPv4 VR(Demo-Named_EIGRP) Address-Family Neighbors for AS(4)
  H   Address         Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                      (sec)         (ms)       Cnt Num
  0   10.1.12.1       Gi2/0             12 00:00:56 1559  5000  1  3
  ! H: a sequence number to represent the order of adjacency formed
  ! Interface: the local interface paring w/ the neighbor from
  ! Hold timer: 15 seconds by default but refresh 5 sec periodically
  ! Uptime: how long having the neighborship
  ! SRRT: smoothed round-trip times
  ! RTO: retransition interval
  ! Q: the number of outstanding requests to form neighbor, expecting 0 in most cases
  ! seq num: packets of negotiation flow btw neighbors

  R2# show ip eigrp neighbors
  EIGRP-IPv4 VR(Demo-Named_EIGRP) Address-Family Neighbors for AS(4)
  H   Address         Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                      (sec)         (ms)       Cnt Num
  0   10.1.12.1       Gi2/0             11 00:03:49 1559  5000  1  3
    Version 11.0/2.0, Tetrans: 1, Retries: 0, Prefixes: 3
    Topology-ids from peer - 0

  R2# show ip route eigrp
  Gateway of last resort is not set.
      1.0.0.0/32 is subnetted, 1 subnets
  D    1.1.1.1 [90/2570240] via 10.0.12.1, 00:.4:59, GigabitEthernet2/0
      10.0.0.0/8 is variably subnetted, 8 subnets, 2 masks
  D    10.0.1.0/24 [90/15360] via 10.0.12.1 00:.4:59, GigabitEthernet2/0
  D    10.0.13.0/24 [90/15360] via 10.0.12.1 00:.4:59, GigabitEthernet2/0
  ```



## EIGRP Hands on Lab with Authentication




## EIGRP Neighbor Relationships and Authentication




