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

- Design of site-to-site FlexVPN
  - IKEv2 components
    - proposal: default but DH group 16
    - policy: deefault
    - profile: R1 & R2
    - keyrings: named IOS-Keys, pre-shared key
  - IPsec profile
    - transform set: AES 256, HMAC SHA 512
    - IKEv2 profile same as profile above
  - using VTI w/ IPsec


## IKEv2 FlexVPN Site-To-Site Configuration

- Config IKEv2 FlexVPN site-to-site on R1

  ```bash
  ! config loopback 0 and line terminal width
  R1# conf t
  R1(config)# int loop 0
  R1(config-if)# ip address 1.1.1.1 255.255.255.255
  R1(config-if)# exit
  R1(config)# line con 0
  R1(config-line)# width 100
  R1(config-line)# exit

  ! default policy
  R1(config)# do show crypto ikev2 policy
  IKEv2 policy: default
      Match fvrf : any
      Match address local : any
      Proposal    : default
  
  ! default proposal
  R1(config)# do show crypto ikev2 proposal
  IKEv2 proposal: default
      Encryption : AES-CBC-256 AES-CBC-192 AES-CBC-128
      Integrity  : SHA512 SHA 384 SHA256 SHA96 MD596
      PRF        : SHA512 SHA 384 SHA256 SHA1 MD5
      DH Group   : DH_GROUP_1536_MODP/Group 5 DH_GROUP_1024_MODP/Group 2

  R1(config)# crypto ike2 proposal default
  R1(config-ikev2-proposal)# group 15
  R1(config-ikev2-proposal)# exit

  R1(config)# do show crypto ikev2 proposal
  IKEv2 proposal: default
      Encryption : AES-CBC-256 AES-CBC-192 AES-CBC-128
      Integrity  : SHA512 SHA 384 SHA256 SHA96 MD596
      PRF        : SHA512 SHA 384 SHA256 SHA1 MD5
      DH Group   : DH_GROUP_4096_MODP/Group 16
  
  ! config keyring
  R1(config)# crypto ikev2 keyring ISO-Keys
  R1(config-ikev2-keyring)# peer R2
  R1(config-ikev2-keyring-peer)# address 25.2.2.2
  R1(config-ikev2-keyring-peer)# pre-shared-key Cisco!23
  R1(config-ikev2-keyring-peer)# exit
  R1(config-ikev2-keyring)# exit

  ! config profile
  R1(config)# crypto ikev2 profile Demo-v2-Profile
  IKEv2 profile MUST have:
      1. A local and a remote authentication methods.
      2. A match identity or a match certificate or match any statement.
  R1(config-ikev2-profile)# match identity remote access 25.2.2.2 255.255.255.255
  R1(config-ikev2-profile)# authentication remote pre-share
  R1(config-ikev2-profile)# authentication local pre-share
  R1(config-ikev2-profile)# keyring local IOS-Keys
  R1(config-ikev2-profile)# exit

  ! create transform set
  R1(config)# crypto ipsec transform-set Demo-Set esp-aes esp-sha512-hmac
  R1(crypto-crypto-trans)# mode tunnel
  R1(config-crypto-trans)# exit

  ! create IPsec profile
  R1(config)# crypto ipsec profile Demo-Ipsec-Profile
  R1(ipsec-profile)# set transform-set Demo-Set
  R1(ipsec-profile)# set ikev2-profile Demo-v2-Profile
  R1(ipsec-profile)# exit

  ! config tunnel intf
  R1(config)# int tunnel 0
  R1(config-if)# ip address 10.12.12.0 255.255.255.0
  R1(config-if)# tunnel source G0/1
  R1(config-if)# tunnel mode ipsec ipv4
  R1(config-if)# tunnel protection ipsec profile Demo-v2-Profile
  R1(config-if)# exit
  ```


## IKEv2 FlexVPN Verification




## Adding Routing to FlexVPN




## FlexVPN Summary



