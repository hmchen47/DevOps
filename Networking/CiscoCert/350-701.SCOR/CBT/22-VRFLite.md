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
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('page')"
      src    = "img/22-vrflite.png"
      alt    = "VRF-lit for seperated VPNs"
      title  = "VRF-lit for seperated VPNs"
    />
    <figcaption> Fig. 1: ... </figcaption>
  </figure>


## VRF-lite Configuration Basics




## VRFs on a Multi-Layer Switch




## VRF-lite Design




## VRF-lite Implementation




## VRF-lite Adding Routing




## VRF-lite Routing Verification




## DHCP VRF Services




## VRF-lite Summary



