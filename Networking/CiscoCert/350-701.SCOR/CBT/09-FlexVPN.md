# 09. Cisco FlexVPN

Trainer: keith Barker


## Introduction to FlexVPN

- Learning goal
  - FlexVPN concept
  - IKEv2 to enble the flexibility
  - Site-to-site Flex VPN config and verification


## FlexVPN Overview

- FlexVPN concept
  - a network allowing w/ multiple VPNs
    - site-to-site VPM
    - remote access VPNs
    - DMVPN - hub-and -spoke VPN
  - FlexVPN allowing these VPNs coexisted
  - IKEv2 used to achieve the security goal on mixed VPNs


## FlexVPN Components

- IKEv2 components
  - proposals:
    - a collection of transforms used in the negotiation of IKE SAs as part of IKE_SA_INIT exchange
    - tansform types used in the negotiation
      - encryption algorithm
      - integrity algorithm
      - pseudo-ramdom function (PRF) algorithm
      - Diffie-Hellman (DH) group
    - default proposal
  - policy:
    - containing proposals used to negotiate the encryption, integrity, PRF algorithm, and DH group in the IKE_SA_INIT exchange
    - able to have match statements used as selection criteria to select a profile during negotiation
    - default policy
  - profile: a repository of non-negotiable parameters of the IKE SA, such as local or remote identities and authentication methods and services that are available to authenticated peers that match the profile
  - keyrings: a repository of symmetric or asymmetric pre-shared keys

- IPsec profile
  - transform set
  - IKEv2 profile (same as IKEv2)


- Purpose of crypto maps
  - created for IPsec to set up SAs for traffic flows that must be encrypted
  - components
    - crypto ACL: which traffic should be protected by IPsec
    - remote peer: where IPsec-protected traffic should be sent
    - local address: used to send traffic
    - transform set: which IPsec security type should be applied to this traffic
    - SAs established manually or via IKE
    - other parameters probably necessary to define an IPsec SA



## IKEv2 Flex VPN Site-To-Site Planning




## IKEv2 FlexVPN Site-To-Site Configuration




## IKEv2 FlexVPN Verification




## Adding Routing to FlexVPN




## FlexVPN Summary



