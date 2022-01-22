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

    ```text
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

- Troubleshooting site-to-site IPsec VPN
  - config info
    - crypto maps
    - crypto ACLs
    - IP address space for subnets
    - interfaces to build tunnel
    - endpoints: client and server
  - issue: no reachability
  - tshoot

    ```text
    R1# show run | section crypto
    crypto isakmp policy 5
     encr aes 256
     hash sha256
     authentication pre-share
     group 5
     lieftime 5000
    crypto isakmp key Cisco!23 address 0.0.0.0
    crypto ipsec transform-set Demo-Set esp-aes esp-sha384-hmac
     mode tunnel
    crypto map Demo-Map 10 ipsec-isakmp
     set peer 25.2.2.2
     set transform-set Demo-Set
     set pfs group15
     match address Crypto-ACL
     crypto map Demo-Map
    
    R1# show crypto map
    Crypto Map "Demo-MAP" 10 ipsec-isakmp
          Peer = 25.2.2.2
          Extended IP access list Crypto-ACL
              access-list Crypto-ACL permit ip 10.1.0.0 0.0.255.255 10.2.0.0 0.0.255.255
          Current peer: 25.2.2.2
          Security association lifetime: 4608000 kilobytes/3600 seconds
          Responder-Only (Y/N): N
          PFS (Y/N): Y
          DH group:  group15
          Transform sets={ 
                  Demo-SET:    { esp-aes esp-sha384-hmac  }, 
          }
          Interfaces using crypto map Demo-MAP:
                  GigabitEthernet0/1

    R1# show crypto isakmp sa
    IPv4 Crypto ISAKMP SA
    dst     src     state     conn-id status

    R1# show isakmp sa detail
    IPv4 Crypto ISAKMP Sa

    C-id  Local   Remote    I-VRF   Status  Encr  Hash  aAuth DH Lifetime

    R1# show crypto isakmp policy
    Global IKE policy
    Protection suite of priority 5
          encryption algorithm:   AES - Advanced Encryption Standard (256 bit keys).
          hash algorithm:         Secure Hash Standard 2 (256 bit)
          authentication method:  Pre-Shared Key
          Diffie-Hellman group:   #5 (1536 bit)
          lifetime:               5000 seconds, no volume limit

    R1# show crypto session
    Interface: GigabitEthernet0/1
    Session status: DOWN
    Peer: 25.2.2.2 port 500
      IPSEC FLOW: permit ip 10.1.0.0/255.255.0.0 10.2.0.0/255.255.0.0
            Active SAs: 0, origin: crypto map
    
    R1# debug crypto isakmp
    R1# show users
        Line    User    Hosts(s)      Idle      Location
    * 0 con 0           idle          00:00:00
  
    R1# show ip int brief
    Interface           IP-Address  OK? Method  Status                Protocol
    GigabitEthernet0/0  unassigned  YES TFTP    administratively down down
    GigabitEthernet0/1  15.1.1.1    YES TFTP    up                    up
    GigabitEthernet0/2  unassigned  YES TFTP    administratively down down
    GigabitEthernet0/3  10.1.0.1    YES TFTP    up                    up

    R1# ping 10.2.0.2 source 10.1.0.1
    .....
    ! no debug msg shown -> checking routing table
    R1# show ip route
    Gateway of last resort is not set

          10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        10.1.0.0/24 is directly connected, GigabitEthernet0/3
    L        10.1.0.1/32 is directly connected, GigabitEthernet0/3
          15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        15.1.1.0/24 is directly connected, GigabitEthernet0/1
    L        15.1.1.1/32 is directly connected, GigabitEthernet0/1

    ! no 10.2.0.0 and no default route
    R1# config t
    R1(config)# ip route 0.0.0.0 0.0.0.0 15.1.1.5
    R1(config)# end
    
    R1# ping 15.1.1.5
    !!!!!
    R1# show ip route
    Gateway of last resort is 15.1.1.1 to network 0.0.0.0

    s*    0.0.0.0 [1/0] via 15.1.1.5
          10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        10.1.0.0/24 is directly connected, GigabitEthernet0/3
    L        10.1.0.1/32 is directly connected, GigabitEthernet0/3
          15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        15.1.1.0/24 is directly connected, GigabitEthernet0/1
    L        15.1.1.1/32 is directly connected, GigabitEthernet0/1

    R1# ping 10.2.0.2 source 10.1.0.1
    !!!!!
    ...
    ISAKMP: (0): Can not start Aggressive mode, trying Main mode.
    ISAKMP: (0): found peer-shared key matching 25.2.2.2
    ...
    ISAKMP: (0): Checking ISAKMP transfor 1 against priority 5 policy
    ISAKMP: (0):      encryption AES-CBC
    ISAKMP: (0):      keylength of 256
    ISAKMP: (0):      hash sha256
    ISAKMP: (0):      default group 5
    ISAKMP: (0):      auth pre-share
    ISAKMP: (0):      life type in seconds
    ISAKMP: (0):      life duration (basic) of 5000
    ISAKMP: (0): attrs are acceptable. Next payload is 0
    ...
    ISAKMP: (0): Old State = IKE_I_MM2    New State = IKE_I_MM2
    ISAKMP-PAK: (0): sending packet to 25.2.2.2 my_port 500 peer_port 500 (I) MM_SA
    ...
    ISAKMP: (0): Old State = IKE_I_MM2    New State = IKE_I_MM3
    ...
    ISAKMP: (0): Old State = IKE_I_MM3    New State = IKE_I_MM4
    ...
    ISAKMP: (1001): Old State = IKE_I_MM4    New State = IKE_I_MM5
    ...
    ISAKMP: (1001): Old State = IKE_I_MM5    New State = IKE_I_MM6
    ...
    ISAKMP: (1001): Old State = IKE_I_MM6    New State = IKE_P1_COMPLETE

    R1# undebug all

    R1# show crypto isakmp sa
    IPv4 Crypto ISAKMP SA
    dst       src       state     conn-id status
    25.2.2.2  15.1.1.1  OM_IDLE      1001 ACTIVE

    R1# show crypto isakmp sa detail
    IPv4 Crypto ISAKMP SA
    C-id  Local     Remote    I-VRF Status  Encr  Hash    Auth  DH  Lifetime
    1001  15.1.1.1  25.2.2.2        ACTIVE  aes   sha256  psk   5   01:18:30
           Engine-id:Conn-id =  SW:1

    R1# show crypto session
    Interface: GigabitEthernet0/1
    Session status: UP-ACTIVE
    Peer: 25.2.2.2 port 500
      IKEv1 SA: local 15.1.1.1/500 remote 25.2.2.2/500 Active
      IPSEC FLOW: permit ip 10.1.0.0/255.255.0.0 10.2.0.0/255.255.0.0
            Active SAs: 2, origin: crypto map
    ```

## IKEv1, Phase 1, Bad Config

- Troubleshooting IKEv1 Phase 1
  - issue: IPsec tunnel not working
  
  ```text
  R1# show run | section crypto
  crypto isakmp policy 5
   encr aes 192
   hash sha256
   authentication pre-share
   group 5
   lieftime 5000
  crypto isakmp key Cisco!23 address 0.0.0.0
  crypto ipsec transform-set Demo-Set esp-aes esp-sha384-hmac
   mode tunnel
  crypto map Demo-Map 10 ipsec-isakmp
   set peer 25.2.2.2
   set transform-set Demo-Set
   set pfs group15
   match address Crypto-ACL
   crypto map Demo-Map

  R1# show ip route
  Gateway of last resort is 15.1.1.1 to network 0.0.0.0

    s*    0.0.0.0 [1/0] via 15.1.1.5
          10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        10.1.0.0/24 is directly connected, GigabitEthernet0/3
    L        10.1.0.1/32 is directly connected, GigabitEthernet0/3
          15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        15.1.1.0/24 is directly connected, GigabitEthernet0/1
    L        15.1.1.1/32 is directly connected, GigabitEthernet0/1
  
  R2# show ip route
  Gateway of last resort is 15.1.1.1 to network 0.0.0.0

    s*    0.0.0.0 [1/0] via 15.1.1.5
          10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        10.1.0.0/24 is directly connected, GigabitEthernet0/3
    L        10.1.0.1/32 is directly connected, GigabitEthernet0/3
          25.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        25.2.2.0/24 is directly connected, GigabitEthernet0/2
    L        25.2.2.2/32 is directly connected, GigabitEthernet0/2

  R1# ping 25.2.2.2
  !!!!!

  R1# show crypto isakmp sa
  IPv4 Crypto ISAKMP SA
  dst       src       state     conn-id status

  R1# debug crypto isakmp
  R2# debug crypto isakmp

  R2# show users
      Line    User    Hosts(s)      Idle      Location
  * 0 con 0           idle          00:00:00

  R1# show debugging
  Cryptographic subsystems:
    Crypto ISAKMP debugging is on

  R1# ping 10.2.0.2 source 10.1.0.1

  R1# undebug all
  R2# undebug all

  R2# 
  ISAKMP-PAK: (0): received packet from 15.1.1.1 dport 500 sport 500 Global (N) 
  ...
  ISAKMP: (0): found peer pre-shared key match 15.1.1.1
  ...
  ISAKMP-ERROR: (0): Proposed key length does not match policy
  ISAKMP-ERROR: (0): attrs are not acceptable. Next payload is 0
  ISAKMP-ERROR: (0): no offers accepted!
  ISAKMP-ERROR: (0): phase 1 SA policy not acceptable! (local 25.2.2.2 remote 15.1.1.1)

  R2# show crypto isakmp policy
  Global IKE policy
  Protection suite of priority 5
        encryption algorithm:   AES - Advanced Encryption Standard (256 bit keys).
        hash algorithm:         Secure Hash Standard 2 (256 bit)
        authentication method:  Pre-Shared Key
        Diffie-Hellman group:   #5 (1536 bit)
        lifetime:               5000 seconds, no volume limit

  R1# show crypto isakmp policy
  Global IKE policy
    Protection suite of priority 5
          encryption algorithm:   AES - Advanced Encryption Standard (192 bit keys).
          hash algorithm:         Secure Hash Standard 2 (256 bit)
          authentication method:  Pre-Shared Key
          Diffie-Hellman group:   #5 (1536 bit)
          lifetime:               5000 seconds, no volume limit

  R1# conf t
  R1(config)# crypto isakmp policy 5
  R1(config-isakmp)# encryption aes 256
  R1(config-isakmp)# end

  R1# debug crypto isakmp
  R2# debug crypto isakmp

  R1# show crypto map
  Crypto Map "Demo-MAP" 10 ipsec-isakmp
          Peer = 25.2.2.2
          Extended IP access list Crypto-ACL
              access-list Crypto-ACL permit ip 10.1.0.0 0.0.255.255 10.2.0.0 0.0.255.255
          Current peer: 25.2.2.2
          Security association lifetime: 4608000 kilobytes/3600 seconds
          Responder-Only (Y/N): N
          PFS (Y/N): Y
          DH group:  group15
          Transform sets={ 
                  Demo-SET:    { esp-aes esp-sha384-hmac  }, 
          }
          Interfaces using crypto map Demo-MAP:
                  GigabitEthernet0/1

  ping 10.2.0.2 source 10.1.0.1
  !!!!
  ... ! ni ISAKMP-ERROR shown

  R1# show crypto isakmp sa
  IPv4 Crypto ISAKMP SA
    dst       src       state     conn-id status
    25.2.2.2  15.1.1.1  OM_IDLE      1001 ACTIVE

  R1# show crypto isakmp sa detail
  IPv4 Crypto ISAKMP SA
  C-id  Local     Remote    I-VRF Status  Encr  Hash    Auth  DH  Lifetime
  1001  15.1.1.1  25.2.2.2        ACTIVE  aes   sha256  psk   5   01:22:12
         Engine-id:Conn-id =  SW:1

  R1# show crypto engine connection active
  Crypto Engine Connections

     ID  Type   Algorithm     Encrypt   Decrypt   LastSeqN  IP-Address
      1  IPsec  AES+SHA384          0         4          4  15.1.1.1
      2  IPsec  AES+SHA384          4         0          0  15.1.1.1
   1001  IKE    AHA256+AES256       0         0          0  15.1.1.1
  ```



## IKEv1, Phase 2 Bad Config

- Tshooting Ipsec tunnel
  - issue: IPsec tunnel not working but others working well
  - IKEv1
    - phase 1: working weell
    - phase 2: Ipsec tunnel not working
  
  ```text
  R1# shop run | sec crypto
  R1# show run | section crypto
  crypto isakmp policy 5
   encr aes 256
   hash sha256
   authentication pre-share
   group 5
   lieftime 5000
  crypto isakmp key Cisco!23 address 0.0.0.0
  crypto ipsec transform-set Demo-Set esp-aes esp-sha384-hmac
   mode tunnel
  crypto map Demo-Map 10 ipsec-isakmp
   set peer 25.2.2.2
   set transform-set Demo-Set
   set pfs group15
   match address Crypto-ACL
   crypto map Demo-Map

  R1# show crypto map
  Crypto Map "Demo-MAP" 10 ipsec-isakmp
          Peer = 25.2.2.2
          Extended IP access list Crypto-ACL
              access-list Crypto-ACL permit ip 10.1.0.0 0.0.255.255 10.2.0.0 0.0.255.255
          Current peer: 25.2.2.2
          Security association lifetime: 4608000 kilobytes/3600 seconds
          Responder-Only (Y/N): N
          PFS (Y/N): Y
          DH group:  group15
          Transform sets={ 
                  Demo-SET:    { esp-aes esp-sha384-hmac  }, 
          }
          Interfaces using crypto map Demo-MAP:
                  GigabitEthernet0/1

  R1# show crypto session
  Interface: GigabitEthernet0/1
    Session status: DOWN
    Peer: 25.2.2.2 port 500
      IPSEC FLOW: permit ip 10.1.0.0/255.255.0.0 10.2.0.0/255.255.0.0
            Active SAs: 0, origin: crypto map
  
  R1# pint 10.2.0.2 source 10.1.0.1
  .....
  R1# show crypto isakmp sa
  IPv4 Crypto ISAKMP SA
    dst       src       state     conn-id status
    25.2.2.2  15.1.1.1  OM_IDLE      1001 ACTIVE

  R1# show crypto ipsec sa
  interface: Tunnel0
      Crypto map tag: Virtual-Access1-head-0, local addr 15.1.1.1

    protected vrf: (none)
    local Ident  (addr/mask/port/prot): (10.1.0.0/255.255.0.0/0/0)
    remote Ident (addr/mask/port/prot): (10.2.0.0/255.255.255.255/0/0)
    current-peer 25.2.2.2 port 500
      PERMIT, flags={origin_is_acl}
    #pkts encaps: 0, #pkts encrypt: 0, #pkts digest: 0
    #pkts decaps: 0, #pkts decrypt: 0, #pkts verify: 0
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts errors 5, #recv errors 5

     local crypto endpt.: 15.1.1.1, remote crypto endpt.: 25.2.2.2
     plaintext mtu 1500, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
     current outbound spi: 0x0(0)
     FPS (Y/N): N, DH group: none

     inbound esp sas:
      ...

  R1# show crypto engine connections active
  Crypto Engine Connections

     ID  Type   Algorithm     Encrypt   Decrypt   LastSeqN  IP-Address
   1001  IKE    AHA256+AES256       0         0          0  15.1.1.1

  ! no IPsec connection present --> IPsec tunnel broken
  R1# debug crypto ipsec
  R2# debug crypto ipsec

  R1# ping 10.2.0.2 source 10.1.0.1
  .....

  IPSEC(sa_request): ,
    (key eng. msg.) OUTBOUND local= 15.1.1.1:500, remote= 25.2.2.2:500,
      local_proxy= 10.1.0.0/255.255.0.0/256/0,
      remote_proxy= 10.2.0.0/255.255.0.0/256/0,
      protocol= ESP, transform=esp-aes (Tunnel),
      lifedur= 3600s and 4608000kb,
      spi= 0x0(0), conn_id= 0, keysize= 128, flags= 0x0

  IPSEC:(SESSION_ID = 1) (key_engine) request timer fired: count = 1,
    (identity) local= 15.1.1.1:0, remote= 10.2.2.2:0,
      local_proxy= 10.1.0.0/255.255.0.0/256/0,
      remote_proxy= 10.2.0.0/255.255.0.0/256/0
  IPSEC(sa_request): ,
    (key eng. msg.) OUTBOUND local= 15.1.1.1:500, remote= 25.2.2.2:500,
      local_proxy= 10.1.0.0/255.255.0.0/256/0,
      ...

  R2#
  IPSEC(validate_proposal_request): proposal part #1,
    (key eng. msg) INBOUND local= 25.2.2.2:0, remote= 15.1.1.1:0,
      local_proxy= 10.2.0.0/255.255.0.0/256/0
      remote_proxy= 10.1.0.0/255.255.0.0/256/0
      protocol= ESP, transform=esp-aes (Tunnel),
      lifedur= 0s and 0kb,
      spi= 0x0(0), conn_id= 0, keysize= 128, flags= 0x0
  Crypto mapdb : proxy_match
          src addr     : 10.2.0.0
          dst addr     : 10.1.0.0
          protocol     : 0
          src port     : 0
          dst port     : 0
  IPSEC(ipsec_process_proposal): transforma proposal not supported for idenitty: {esp-aes }

  ! probably not compatible IPsec transform set
  R1# show crypto map
  Crypto Map "Demo-MAP" 10 ipsec-isakmp
          Peer = 25.2.2.2
          Extended IP access list Crypto-ACL
              access-list Crypto-ACL permit ip 10.1.0.0 0.0.255.255 10.2.0.0 0.0.255.255
          Current peer: 25.2.2.2
          Security association lifetime: 4608000 kilobytes/3600 seconds
          Responder-Only (Y/N): N
          PFS (Y/N): Y
          DH group:  group15
          Transform sets={ 
                  B-SET:    { esp-aes  }, 
          }
          Interfaces using crypto map Demo-MAP:
                  GigabitEthernet0/1

  R2# show crypto map
  Crypto Map "Demo-MAP" 10 ipsec-isakmp
          Peer = 15.1.1.1
          Extended IP access list Crypto-ACL
              access-list Crypto-ACL permit ip 10.2.0.0 0.0.255.255 10.1.0.0 0.0.255.255
          Current peer: 15.1.1.1
          Security association lifetime: 4608000 kilobytes/3600 seconds
          Responder-Only (Y/N): N
          PFS (Y/N): Y
          DH group:  group15
          Mixed-mode : Disabled
          Transform sets={ 
                  Demo-SET:    { esp-aes esp-sha384-hmac  }, 
          }
          Interfaces using crypto map Demo-MAP:
                  GigabitEthernet0/2

  R1# undebug all
  R2# undebug all

  R1# conf t
  R1(config)# do show run | section crypto
  crypto isakmp policy 5
     encr aes 256
     hash sha256
     authentication pre-share
     group 5
     lieftime 5000
    crypto isakmp key Cisco!23 address 0.0.0.0
    crypto ipsec transform-set Demo-Set esp-aes esp-sha384-hmac
     mode tunnel
    crypto ipsec transform-set B-Set esp-aes
     mode tunnel
    crypto map Demo-Map 10 ipsec-isakmp
     set peer 25.2.2.2
     set transform-set B-Set
     set pfs group15
     match address Crypto-ACL
     crypto map Demo-Map

  R1(config)# crypto map Demo-Map 10 ipsec-isakmp
  R1(config-crypto-map)# set transform-set Demo-Set
  R1(config-crypto-mao)# int g0/1
  R1(config-if)# no crypto map Demo-Map
  R1(config-if)# crypto map Demo-Map
  R1(config-if)# end

  ! regenerte traffic w/ debug
  R1# debug crypto ipsec
  R2# debug crypto ipsec

  R1# ping 10.2.0.2 source 10.1.0.1
  .!!!!

  IPSEC(sa_request): ,
    (key eng. msg.) OUTBOUND local= 15.1.1.1:500, remote= 25.2.2.2:500,
      local_proxy= 10.1.0.0/255.255.0.0/256/0,
      remote_proxy= 10.2.0.0/255.255.0.0/256/0,
      protocol= ESP, transform=esp-aes (Tunnel),
      lifedur= 3600s and 4608000kb,
      spi= 0x0(0), conn_id= 0, keysize= 128, flags= 0x0
  IPSEC:(SESSION_ID = 1) (key_engine) request timer fired: count = 1
  IPSEC:(SESSION_ID = 1) (key_engine) request timer fired: count = 1,
    (identity) local= 15.1.1.1:0, remote= 10.2.2.2:0,
      local_proxy= 10.1.0.0/255.255.0.0/256/0,
      remote_proxy= 10.2.0.0/255.255.0.0/256/0
      protocol= ESP, transform=esp-aes esp-sha384-hmac (Tunnel),
      lifedur= 0s and 0kb,
      spi= 0x0(0), conn_id= 0, keysize= 128, flags= 0x0
  ...

  R2#
  IPSEC(validate_proposal_request): proposal part #1,
    (key eng. msg) INBOUND local= 25.2.2.2:0, remote= 15.1.1.1:0,
      local_proxy= 10.2.0.0/255.255.0.0/256/0
      remote_proxy= 10.1.0.0/255.255.0.0/256/0
      protocol= ESP, transform=esp-aes esp-sha384-hmac (Tunnel),
      lifedur= 0s and 0kb,
      spi= 0x0(0), conn_id= 0, keysize= 128, flags= 0x0
  Crypto mapdb : proxy_match
          src addr     : 10.2.0.0
          dst addr     : 10.1.0.0
          protocol     : 0
          src port     : 0
          dst port     : 0
  (ipsec_process_proposal)Map Accepted: Demo-Map, 10
  IPSEC(key-engine): got a queue event with 1 KMI message(s)
  ...

  R1# undebug all
  R2# undebug all

  R1# show crypto session
  Interface: GigabitEthernet0/1
    Session status: UP-ACTIVE
    Peer: 25.2.2.2 port 500
      IKEv1 SA: local 15.1.1.1/500 remote 25.2.2.2/500 Active
      IPSEC FLOW: permit ip 10.1.0.0/255.255.0.0 10.2.0.0/255.255.0.0
            Active SAs: 2, origin: crypto map

  R1# show crypto ipsec sa
  interface: Tunnel0
      Crypto map tag: Virtual-Access1-head-0, local addr 15.1.1.1

    protected vrf: (none)
    local Ident  (addr/mask/port/prot): (10.1.0.0/255.255.0.0/0/0)
    remote Ident (addr/mask/port/prot): (10.2.0.0/255.255.255.255/0/0)
    current-peer 25.2.2.2 port 500
      PERMIT, flags={origin_is_acl}
    #pkts encaps: 4, #pkts encrypt: 4, #pkts digest: 4
    #pkts decaps: 4, #pkts decrypt: 4, #pkts verify: 4
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts errors 5, #recv errors 5

     local crypto endpt.: 15.1.1.1, remote crypto endpt.: 25.2.2.2
     plaintext mtu 1500, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
     current outbound spi: 0x0(0)
     FPS (Y/N): N, DH group: none

     inbound esp sas:
      ...
  ```


## IKEv2 Troubleshooting

- Tshooting IKEv2
  - tunnel interface 0 on both sides w/ IP address space 10.12.12.0/24
  - encrypting/decrypting traffic btw 10.1.0.0 and 10.2.0.0
  - IKEv2 SA and children SA $\to$ IPsec SA

  ```text
  R1# show ip route
  Gateway of last resort is 25.2.2.5 to network 0.0.0.0
    S*   0.0.0.0/0 [1/0] via 25.2.2.5
         1.0.0.0/32 is subnetted, 1 subnets
            1.1.1.1 is directly connected, Loopback0
         10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
    C       10.1.0.0/24 is directly connected, GigabitEthernet0/3
    L       10.1.0.0/32 is directly connected, GigabitEthernet0/3
    D       10.2.0.0/24 [90/28160256] via 10.12.12.2 00:06:45, Tunnel0
    C       10.12.12.0/24 is directly connected, Tunnel0
    L       10.12.12.1/32 is directly connected, Tunnel0
         15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C       15.1.1.0/24 is directly connected, GigabitEthernet0/1
    L       15.1.1.1/32 is directly connected, GigabitEthernet0/1
  
  R1# show run int tun 0
  Current Configuration : 200 bytes
  !
  interface tunnel0
   ip address 10.12.12.0 255.255.255.0
   tunnel source GigabitEthernet0/1
   tunnel mode ipsec ipv4
   tunnel destination 25.2.2.2
   tunnel protection ipsec profile Demo-IPsec-Profile
  end

  R1# show crypto session
  Interface: Tunnel0
    Session status: UP-ACTIVE
    Peer: 25.2.2.2 port 500
      Session ID: 2
      IKEv2 SA: local 15.1.1.1/500 remote 25.2.2.2/500 Active
      IPSEC FLOW: permit ip 0.0.0.0/0.0.0.0 0.0.0.0/0.0.0.0
            Active SAs: 2, origin: crypto map
  
  ! no crypto map w/ IKEv2
  R1# show run | include map

  R1# show crypto mao
  Crypto Map: "Tunnel0-head-0" IKEv2 profile: Demo-v2-Profile

  Crypto Map "Tunnel0-head-0" 65536 ipsec-isakmp
          IKEv2 Profile: Demo-v2-Profile
          Profile name: Demo-IPsec-Profile
          Security association lifetime: 4608000 kilobytes/3600 seconds
          Responder-Only (Y/N): N
          PFS (Y/N): Y
          DH group:  group15
          Transform sets={ 
                  Demo-SET:    { esp-256-aes esp-sha512-hmac  }, 
          }
  
  Crypto Map "Tunnel0-head-0" 65537 ipsec-isakmp
          MAP is a PROFILE INSTANCE
          Peer = 25.2.2.2
          IKEv2 Profile: Demo-v2-Profile
          Extended IP access list
            access-list permit ip any any
          Current peer: 25.2.2.2
          Security association lifetime: 4608000 kilobytes/3600 seconds
          ...

  R1# show crypto ikev2 ?
    authorization       
    certificate-cache   Show certificate in ikev2 certificate-cahe
    client              Show Client status
    cluster             Show Cluster load
    diagnose            Shows ikev2 diagnose
    policy              Show policies
    profile             Shows ikev2 profiles
    proposal            Show proposals
    sa                  Shows ikev2 SAs
    session             Shows ikev2 active session 
    stats               Shows ikev2 sa stats
  
  R1# show crypto ikev2 sa
  Tunnel-id Local           Remote          fvrf/ivrf   Status
  1         15.1.1.1/500    25.2.2.2/500    none/none   READY
      Encr: AES-CBC, keysize: 256, PRF: SHA512, Hash: SHA512,
        DH Grp: 16, Auth sign: PSK, Auth verify: PSK

  R1# show crypto ikev2 connections active
  Crypto Engine Connections

       ID  Type    Algorithm      Encrypt  Decrypt LastSeqN IP-Address
        5  IPsec   AES256+SHA512      156        0        0 15.1.1.1
        6  IPsec   AES256+SHA512       25      156      156 15.1.1.1
     1003  IKEv2   SHA512+AES256        0        0        0 15.1.1.1

  R1# show crypto ipsec sa
  interface: Tunnel0
      Crypto map tag: Tunnel0-head-0, local addr 15.1.1.1

    protected vrf: (none)
    local Ident  (addr/mask/port/prot): (0.0.0.0/0.0.0.0/0/0)
    remote Ident (addr/mask/port/prot): (0.0.0.0/0.0.0.0/0/0)
    current-peer 25.2.2.2 port 500
      PERMIT, flags={origin_is_acl}
    #pkts encaps: 166, #pkts encrypt: 166, #pkts digest: 166
    #pkts decaps: 166, #pkts decrypt: 166, #pkts verify: 166
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts errors 0, #recv errors 0

     local crypto endpt.: 15.1.1.1, remote crypto endpt.: 25.2.2.2
     plaintext mtu 1500, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
     current outbound spi: 0x87...73(228...39)
     FPS (Y/N): N, DH group: none

     inbound esp sas:
      spi: 0xA1A...38(27...48)
      ...
      status: ACTIVE(ACTIVE)
      ...
    outbound esp sas:
      spi: 0x87...73(228...39)
      ...
      Status: ACTIVE (ACTIVE)
    
  ! turn on debug
  R1# debug crypto ikev2
  R2# debug crypto ikev2

  R1# conf t
  R1(config)# int tun 0
  R1(config-if)# shutdown
  ...
  R1(config-if)# end

  R1# show log
  ...
  IKEv2:(SESSION ID = 2, SA ID = 1):Verify peer's policy
  IKEv2:(SESSION ID = 2, SA ID = 1):Peer's policy verified
  IKEv2:(SESSION ID = 2, SA ID = 1):Get peer's authentication method
  IKEv2:(SESSION ID = 2, SA ID = 1):Peer's authenticaton method is 'PSK'
  ...

  R2#
  ...
  IKEv2:(SESSION ID = 3, SA = 1): IKEV2 SA created; inserting SA into database.
  ...

  R1# undebug all
  R2# undebug all

  R1# show crypto session


  R1(config-if)# no shut
  Interface: Tunnel0
  Profile: Demo-v2-Profile
  Session status: UP-ACTIVE
  Peer: 25.2.2.2 port 500
    Session ID: 2
    IKEv2 SA: local 15.1.1.1/500 remote 25.2.2.2/500 Active
    IPSEC FLOW: permit ip 0.0.0.0/0.0.0.0 0.0.0./0.0.0.0
          Active SAs: 2., origin: crypto map
  ```



## Summary Troubleshooting IPsec

- Summary
  - troubleshooting IPsec VPN
  - main possible issues
    - routing w/ tunnel
    - incompatible IKEv1 phase 1 settings
    - incompatible IKEv2 phase 2 (Ipsec) setting


