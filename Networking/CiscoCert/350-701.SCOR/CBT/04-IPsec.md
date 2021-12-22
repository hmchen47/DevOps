# 04. IPsec Fundamentals

Trainer: Keith Barker

## Introduction to IPsec

- Learning goal
  - protecting data in motion and at rest
  - ensuring confidentiality and integrity
  - IPsec to achieve these goals


## IPsec Overview

- IPsec overview
  - main goals
    - privacy: encryption
    - integrity: hashing
  - types of IPsec:
    - site2site: protect traffic btw PC1 & PC2 $\to$ IPsec tunnel btw R1 & R2
    - remote access: protect traffic btw windows user and R1 $\to$ Ipsec tunnel btw PC and R1
  

- IPsec packet format
  - original IP packet
    - IP header: src = PC1, dst = PC2
    - payload
  - prefix ESP header: port 50
  - prefix new IP header: src = R1, dst = R2

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=150
        src   = "img/03-netarch.png"
        alt   = "Example network topology"
        title = "Example network topology"
      >
    </a>
    <a href="http://www.sharetechnote.com/html/IP_Network_IPSec_ESP.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=150
        src   = "http://www.sharetechnote.com/image/IP_Security_IPSec_ESP_01.png"
        alt   = "IPsec packet format"
        title = "IPsec packet format"
      >
    </a>
  </div>


- Internet Key Exchange (IKE)
  - DMVPN: hub-and-spoke network architecture
    - tunnels btw hub and spokes
    - tunnels btw spokes
  - crypto map
    - an instruction
    - operations
      - PC1 sending packet to PC2
      - R1 seeing the traffic and apply crypto map on the outgoing interface
      - R1 encrypting traffic and sending to R2
      - R2 decrypting the traffic and forwarding to PC2
    - old fashion and not flexible
  - virtual tunnel interface (VTI)
    - using GRE on virtual tunnel
    - applying crypto on the traffic abd sending via the virtual tunnel


## IKEv1 and IKEv2



## Crypto Map IPsec



## VTI IPsec



## DMVPNs



## FlexVPN



## GET VPN



## NAT Traversal



## IPsec Fundamentals Summary