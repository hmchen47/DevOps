# 10. Cisco Remote Access VPNs

Trainer:: Keith Barker


## Introduction to RA VPNs

- Learning goals
  - options for remote access
  - configurations of Cisco Remote Access VPNs
  - verifications of Cisco Remote Access VPNs
  - the use of AnyConnect


## RA VPN Overview

- RV VPN concept
  - PC: end user
  - R1: router for corporate HQ network
  - security options
    - IPsec
    - SSL/TLS
  - push:
    - pushing policy from R1 to PC
    - authentication
    - routing
    - firewall
    - restrictions
  - split tunneling: corporate traffic route to R1 while other traffic via Internet
  - Cisco AnyConnect client software


## FlexVPN IPsec RA VPNs

- Components of FlexVPN IPsec RA VPNs
  - IKEv2 sa
    - encryption
    - authentication
    - PRF
    - encryption
  - IPsec sa
    - transform set
    - profile
  - AAA method
    - authentication: local authentication w/ certificate on R1 or Radius server in 10.1.0.0/24
    - authorization policy
  - addresses range of users
  - virtual template: used to provide configuration for dynamically created virtual-access interfces


## FlexVPN RA Design




## Setting CA Services in IOS




## Configuring FlexVPN RA




## AnyConnect Profile Editor




## Testing and Verifying the RA VPN




## Flex VPN RA Summary



