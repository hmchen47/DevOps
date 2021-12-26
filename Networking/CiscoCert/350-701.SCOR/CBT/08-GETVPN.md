# 08. Cisco GET VPN

Trainer: Keith Barker


## Introduction to GET VPN

- GET VPN overview
  - Group Encrypted Transport (GET)
  - a technology w/ central controller to create groups of SAs and keys for multiple secured devices
  - a tunnel-less VPN technology meant for private networks
  - Multicast rekeying: a way to to enable encryption for "native" multicat packets and unicast rekeying over a private WAN


## GET VPN Overview

- GET VPN overview
  - group member: R1~R3
  - encrypted w/ IPsec
  - example: client (.50) w/ R3 subnet sending queries to server (.10) in R1 subnet
    - original pkt: src = 10.3.0.50 = CLT, dst = 10.1.0.10 = SRV
    - pkt out R3 g0/3: encrypting original pkt, add esp header (port 50) and new IP header w/ src=CLT, dst = SRV
    - IPsec transport mode reserving the original IP addresses
    - transport network: MPLS or Internet


  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('page')"
      src    = "img/08-getvpn.png"
      alt    = "Example networ topology for GET VPN"
      title  = "Example networ topology for GET VPN"
    />
  </figure>


- Benefits of GET VPN
  - a ket server in charge of control plane for all IPsec tunnels
  - features
    - generate keys
    - creating ACLs
    - communicating w/ group members
  - handling group policy for all group members in one point
  - all subnets of group members encrypted based on the policy
  - key server inforing the group members about the subnets
  - GDOI: Group Domain Interpretation
  - any change of the policy in key server propagating to all group members


## GET VPN Key Servers (KS)




## GET VPN Members (GM)




## GET VPN Design




## Implementing KS Configuration




## Implementing GM Configuration




## GET VPN verification




## GET VPN Summary



