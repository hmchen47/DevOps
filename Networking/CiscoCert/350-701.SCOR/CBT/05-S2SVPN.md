# 05. Cisco Router Site-To-Site VPNs

Trainer: Keith Barker


## Introducing Site-To-Site VPNs

- Learning goal
  - configure IPsec site-to-site tunnels by using IKEv1 and crypto maps
  - verify IPsec site-to-site tunnels


## Planning for IPsec Site-To-Site

- Site-to-site IPsec VPN
  - topology:
    - site 1: R1 + PC1
    - site 2: R2 + PC2
  - sharing info and protecting the traffic btw 2 sites
  - encrypted traffic only btw R1 & R2, PC1 & PC2 unawaring the encryption


- Requirements to build the site-to-site IPsec VPN
  - using IKEv1 to establish IPsec VPN
  - IKE Phase 1
    - authentication:
      - how peers to prove each other authorized?
      - solutions: preshared key, digital signature
    - hashing: packet integrity
    - encryption: ASE recommended
    - DH group:
      - a way to generate keying material
      - how to generate the keys for R1 & R2 encryption and decryption
    - lifetime
  - IKE Phase 2
    - the IPsec tunnel
    - encryption
    - interesting traffic: what traffic will be encrypted
    - peers: R1 & R2
    - tunnel mode: encrypted the whole packet and adding an new IP header
    - keying material: recycling from phase 1 or generating a new pair (PFS)


## Designing a Site-To-Site VPN




## Configuring an IKE Phase 1 Policy




## Configuring an IKE Phase 2 (IPsec) Policy




## Enabling the IPsec Policy




## Protocol Analysis IPsec





