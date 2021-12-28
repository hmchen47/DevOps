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

- Verify on R1

  ```bash
  R1# show crypto ikev2 proposal default
  IKEv2 proposal: default
      Encryption : AES-CBC-256 AES-CBC-192 AES-CBC-128
      Integrity  : SHA512 SHA 384 SHA256 SHA96 MD596
      PRF        : SHA512 SHA 384 SHA256 SHA1 MD5
      DH Group   : DH_GROUP_4096_MODP/Group 16

  R1# show crypto ikev2 sa
  Tunnel-id Local         Remote        fvrf/ivrf   Status
  1         15.1.1.1/500  25.2.2.2/500  none/none   READ
    Encr: AES-CBC, Keysize: 256, PRF: SHA512, Hash: SHA512, DH Grp:16, Auth sign: PSK, Auth verify: PSK

  R1# show crypto ipsec transform-set
  Transfor set deafult: { esp-aes esp-sha-hmac  }
      will negotiate = { Transport,  },
  Transfor set Demo-Set: { esp-256-aes esp-sha512-hmac  }
      will negotiate = { Tunnel,  },

  R1# sho crypto ipsec profile
  IPSEC profile Demo-IPsec-Profile
      IKEv2 Profile: Demo-v2-Profile
      Security association lifetime; 4608000 kilobytes/3600 seconds
      Responder-Only (Y/N): N
      PFS (Y/N): N
      Mixed-mode : Disabled
      Transfor set = {
        Demo-Set: { esp-256-aes esp-sha512-hmac  }
      }
      
  IPSEC profile default
      IKEv2 Profile: Demo-v2-Profile
      Security association lifetime; 4608000 kilobytes/3600 seconds
      Responder-Only (Y/N): N
      PFS (Y/N): N
      Mixed-mode : Disabled
      Transfor set = {
        Demo-Set: { esp-aes esp-sha-hmac  }
      }

  R1# show crypto ipsec sa
  interface: Tunnel0
      Crypto map tag: Tunnel0-head-0, local addr 15.1.1.1

    protected vrf: (none)
    local Ident  (addr/mask/port/prot): (10.0.0.0/0.0.0.0/0/0)
    remote Ident (addr/mask/port/prot): (10.0.0.0/0.0.0.0/0/0)
    current-peer 25.2.2.2 port 500
      PERMIT, flags={origin_is_acl}
    #pkts encaps: 0, #pkts encrypt: 0, #pkts digest: 0
    #pkts decaps: 0, #pkts decrypt: 0, #pkts verify: 0
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts errors 0, #recv errors 0

     local crypto endpt.: 15.1.1.1, remote crypto endpt.: 25.2.2.2
     plaintext mtu 1422, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
     current outbound spi: 0xD6F40E5C(3606318684)
     FPS (Y/N): N, DH group: none

     inbound esp sas:
      epi: 0x83A96616(2208917014)
        transform: esp-256-aes esp-sha512-hmac ,
        in use settings = {Tunnel, }
        conn id: 1, flow_id: SW:1, sibling_flag 80000040, crypto mao: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4189686/3262)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE(ACTIVE)

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0xD6F40E5C(3606318684)
        transform: esp-256-aes esp-sha512-hmac ,
        in use settings = {Tunnel, }
        conn id: 2, flow_id: SW:2, sibling_flag 80000040, crypto mao: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4189686/3262)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE(ACTIVE)

     outbound ah sas:

     outbound pcp sas:

  R1# show crypto map
  Crypto Map: "Tunnel0-head-0" IKEv2 profile: Demo-v2-Profile

  Crypto Map IPv4 "Tunnel0-head-0" 65536 ipsec-isakmp
    IKEv2 Profile: Demo-v2-Profile
    Profile name: Demo-IPsec-Profile
    Security association lifetime; 4608000 kilobytes/3600 seconds
      Responder-Only (Y/N): N
      PFS (Y/N): N
      Mixed-mode : Disabled
      Transfor set = {
        Demo-Set: { esp-256-aes esp-sha512-hmac  }
      }

  Crypto Map IPv4 "Tunnel0-head-0" 65537 ipsec-isakmp
      Map is a PROFILE INSTANCE
      peer = 25.2.2.2
      IKEv2 profile: Demo-v2-Profile
      Extended IP access list
            access-list permit ip any any
      Current peer: 25.2.2.2
      Security association lifetime; 4608000 kilobytes/3600 seconds
      Responder-Only (Y/N): N
      PFS (Y/N): N
      Mixed-mode : Disabled
      Transfor set = {
        Demo-Set: { esp-aes esp-sha-hmac  }
      }
      Always create SAs
      Interfaces using crypto map Tunnel0-head-0

  R1# show crypto ipsec sa
  interface: Tunnel0
      Crypto map tag: Tunnel0-head-0, local addr 15.1.1.1

    protected vrf: (none)
    local Ident  (addr/mask/port/prot): (10.0.0.0/0.0.0.0/0/0)
    remote Ident (addr/mask/port/prot): (10.0.0.0/0.0.0.0/0/0)
    current-peer 25.2.2.2 port 500
      PERMIT, flags={origin_is_acl}
    #pkts encaps: 0, #pkts encrypt: 0, #pkts digest: 0
    #pkts decaps: 0, #pkts decrypt: 0, #pkts verify: 0
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts errors 0, #recv errors 0

     local crypto endpt.: 15.1.1.1, remote crypto endpt.: 25.2.2.2
     plaintext mtu 1422, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
     current outbound spi: 0xD6F40E5C(3606318684)
     FPS (Y/N): N, DH group: none

     inbound esp sas:
      epi: 0x83A96616(2208917014)

  R1# show ip route
  Gateway of last resort is 25.2.2.5 to network 0.0.0.0
    S*   0.0.0.0/0 [1/0] via 25.2.2.5
         1.0.0.0.0/32 is subnetted, 1 subnets
    C       1.1.1.1 is directly connected, Loopback0
         10.0.0.0/32 is variably subnetted, 4 subnets, 2 masks
    C       10.2.0.0/24 is directly connected, GigabitEthernet0/3
    L       10.2.0.0/32 is directly connected, GigabitEthernet0/3
    C       10.12.12.0/24 is directly connected, Tunnel0
    L       10.12.12.0/32 is directly connected, Tunnel0
         15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C       15.1.1.0/24 is directly connected, GigabitEthernet0/1
    L       15.1.1.1/32 is directly connected, GigabitEthernet0/1
  ```


## Adding Routing to FlexVPN

- Adding EIGRP for tunnel network on R1

  ```bash
  R1# config
  R1(config)# router eigrp 1
  R1(config-router)# net 10.0.0.0
  R1(config-router)# end

  R1# show ip eigrp int
  EIGRP-IPv4 Interfaces for AS(1)
                      Xmit Queue    PeerQ         Mean    Pacing Time   MTU
  Interface   Peers   Un/Reliable   Un/Reliable   SRTT    Un/Reliable   Flow
  Gi0/3         0         0/0        0/0            0        0/0
  Tu0           0         0/0        0/0            0        6/6
  ```


- Adding EIGRP for tunnel network on R2

  ```bash
  R2# debug ip routing

  R2# conf t
  R2(config)# router eigrp 1
  R2(config-router)# net 10.0.0.0
  R2(config-router)# end

  %DUAL-5-NBRCHANGE: EIGRP-IPv4 1: Neighbor 10.12.12.1 (Tunnel0) is up: new adjacency

  R2# show ip route

  Gateway of last resort is 25.2.2.5 to network 0.0.0.0
  S*   0.0.0.0/0 [1/0] via 25.2.2.5
       2.0.0.0.0/32 is subnetted, 1 subnets
  C       2.2.2.2 is directly connected, Loopback0
       10.0.0.0/32 is variably subnetted, 5 subnets, 2 masks
  D       10.1.0.0/24 [90/26880256], via 10.12.12.1, 00:00:17, Tunnel0
  C       10.2.0.0/24 is directly connected, GigabitEthernet0/3
  L       10.2.0.0/32 is directly connected, GigabitEthernet0/3
  C       10.12.12.0/24 is directly connected, Tunnel0
  L       10.12.12.0/32 is directly connected, Tunnel0
       25.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
  C       25.1.1.0/24 is directly connected, GigabitEthernet0/2
  L       25.1.1.1/32 is directly connected, GigabitEthernet0/2

  R2# ping 10.1.0.50
  !!!!!
  R2# traceroute 10.1.0.50
  Tracing the route to 10.1.0.50
  VRF info: (vrf in name/id, vrf out name/id)
    1 10.12.12.1 19 ms 16 ms 14 ms
    2 10.1.0.50 12 ms 16 ms 10 ms

  R2# show crypto ipsec sa
  interface: Tunnel0
      Crypto map tag: Tunnel0-head-0, local addr 25.2.2.2

    protected vrf: (none)
    local Ident  (addr/mask/port/prot): (10.0.0.0/0.0.0.0/0/0)
    remote Ident (addr/mask/port/prot): (10.0.0.0/0.0.0.0/0/0)
    current-peer 15.2.2.2 port 500
      PERMIT, flags={origin_is_acl}
    #pkts encaps: 88, #pkts encrypt: 88, #pkts digest: 88
    #pkts decaps: 94, #pkts decrypt: 94, #pkts verify: 94
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts errors 0, #recv errors 0

     local crypto endpt.: 25.1.1.1, remote crypto endpt.: 15.2.2.2
     plaintext mtu 1422, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
     current outbound spi: 0x83A96616(2208917014)
     FPS (Y/N): N, DH group: none
    ...
  ```


- Verify w/ traffic capture on tunnel
  - pkt: src=25.2.2.2, dst=15.1.1.1, prot=ESP, info=ESP (SPI=0x83A96616) $\to$ encrypted payload


## FlexVPN Summary



