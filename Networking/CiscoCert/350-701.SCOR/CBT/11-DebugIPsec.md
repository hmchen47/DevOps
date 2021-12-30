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

- Troubleshooting site-to-site IPsec VPN
  - config info
    - crypto maps
    - crypto ACLs
    - IP address space for subnets
    - interfaces to build tunnel
    - endpoints: client and server
  - issue: no reachability
  - tshoot

    ```bash
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
      IPSEC FLOW: permit ip 10.1.0.0/55.255.0.0 10.2.0.0/255.255.0.0
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
      IPSEC FLOW: permit ip 10.1.0.0/55.255.0.0 10.2.0.0/255.255.0.0
            Active SAs: 2, origin: crypto map
    ```

## IKEv1, Phase 1, Bad Config

- Troubleshooting IKEv1 Phase 1 on R1
  - issue: IPsec tunnel not working
  
  ```bash
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

     ID  Type   Algorithm     Encrypt   Decrypt   LasySeqN  IP-Address
      1  IPsec  AES+SHA384          0         4          4  15.1.1.1
      2  IPsec  AES+SHA384          4         0          0  15.1.1.1
   1001  IKE    AHA256+AES256       0         0          0  15.1.1.1
  ```



## IKEv1, Phase 2 Bad Config




## IKEv2 Troubleshooting




## Summary Troubleshooting IPsec



