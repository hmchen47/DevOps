# 11. Debugging for IPsec Tunnels

Trainer: Keith Barker


## Introduction to Debugging IPsec

- learning goal
  - basic concept of IPsec troubleshooting 
  - troubleshotting procedures for IPsec
  - show and debug commands for difference scenarios


## Overview of IPsec Options

- Implementing IPsec VPN
  - methods
    - IKEv1
    - IKEv2
  - scenarios
    - site-to-site
    - remote access
  - site-to-site IPsec VPN
    - crypto map
    - crypto ACL
  - virtual tunnel interfaces (VTI)
  - DMVPN: NHRP
  - GET VPN: IKEv1 phase 1 for gms and ks


## Troubleshooting Tips for IPsec

- Tshooting methodology for IPsec
  - routing issues: most likely forgotten issue on encrypted traffic via tunnel
  - reachability:
    - connectivity btw R1 & R2
    - default IPsec negotiation w/ UDP:500
    - IPsec tunnel w/ ESP:50
  - correct policy implement
    - IKE version
    - matched IKEv1 phase 1 & 2 policies
    - password


- Verify routing issue
  - traffic from 10.1.0.0 to 10.2.0.0
  - verify routes on R1
    - no explicit route for 10.2.0.0 

    ```bash
    R1# show ip route
    Gateway of last resort is 15.1.1.1 to network 0.0.0.0

    s*    0.0.0.0 [1/0] via 15.1.1.5
          10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        10.1.0.0/24 is directly connected, GigabitEthernet0/3
    L        10.1.0.1/32 is directly connected, GigabitEthernet0/3
          15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        15.1.1.0/24 is directly connected, GigabitEthernet0/1
    L        15.1.1.1/32 is directly connected, GigabitEthernet0/1
    ```


- Verify reachability btw endpoints of tunnel


## IKEv1, Phase 1, Missing Routes




## IKEv1, Phase 1, Bad Config




## IKEv1, Phase 2 Bad Config




## IKEv2 Troubleshooting




## Summary Troubleshooting IPsec



