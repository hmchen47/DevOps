# 27. Troubleshoot OSPF Authentication for IPv4

Trainer: Keith Barker


## Intro to IPv4 OSPF Authentication and Troubleshooting

- Learning goals
  - IPv4 OSPF authentication
  - config OSPF authentication
  - virtual links authentication
  - troubleshooting OSPF authentication


## Overview of OSPF Authentication

- OSPF authentication overview
  - preventing from hacker on subnets as an OSPF fully adjacent router
  - authentication options
    - NULL (0): no authentication
    - simple/ plain text (1): authentication using plain text key
    - MD5/encrypted (2): using MD5 to encrypting key
  - locations to apply authentication
    - area
    - interfaces #\to$ more secure & predecent


- Planning OSPF authentication
  - area 0: no authentication
  - area 1: plain text key authentication
  - area 2: md5 authentication

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('page')"
      src    = "img/27-ospf.png"
      alt    = "Example OPSF network w/ 3 areas"
      title  = "Example OPSF network w/ 3 areas"
    />
  </figure>

- Demo: config and verify all routers
  - general config for all routers

    ```cfg
    ! config apply to all routers (R1~R8)
    conf t
    ip router ospf 1
    area 1 authentication
    area 2 authentication message-digest
    end
    ```
  
  - config R1 and all other routers

    ```text
    R1# conf t
    R1(config)# ip router ospf 1
    R1(config-router)# area 1 authentication
    R1(config-router)# area 2 authentication message-digest
    R1(config-router)# end
    ```

  - verify OSPF 

    ```text
    R1# show ip ospf
      Routing Process "ospf 1" with ID 1.1.1.1 
      <...truncated...>
        Area BACKBONE(0) 
            Number of interfaces in this area is 4 (1 loopback)
            Area has no authentication
            <...truncated...>
    
    R1# show ip ospf int g0/0
    GigabitEthernet0/0 is up, line protocol is up
      <...truncated...>
      Neighbor Count is 0, Adjacent neighbor count is 0
      Suppresses hello for 0 neighbor(0)
    ! nothing about authentication due to area 0

    R5# show ip ospf
      Routing Process "ospf 1" with ID 1.1.1.1 
      <...truncated...>
        Area 1 
            Number of interfaces in this area is 4 (1 loopback)
            Area has simple password authentication
            <...truncated...>
        Area 2
            Number of interfaces in this area is 0
            Area has message digest authentication
      <...truncated...>

    R5# show ip ospf int g1/0
    GigabitEthernet0/0 is up, line protocol is up
      <...truncated...>
      Suppresses hello for 0 neighbor(0)
      Simple password authentication enabled

    ! area 2 routers still forming adjacency even not key set 
    ```


- Demo: config key for OSPF Area 1 routers
  - task: enable plain text password for authentication on interfaces btw R3 & R5 and R5 & R7
  - command to set plain text key: `ip ospf authentication-key cisco123`
  - apply the plain text key to interfaces on R3, R5 & R7

    ```text
    R3(config)# int f4/1
    R3(config-if)# ip ospf authentication-key cisco123

    R5(config-if)# show ip cdp neighbors
    Device ID     Local Intrfce   Holdtme    Capability  Platform  Port ID
    R3            Fas 4/0         165           R        7206VXR   Fas 4/1
    R7            Gig 1/0         141           R        7206VXR   gig 2/0

    R5(config)# int f4/0
    R5(config-if)# do debug ospf adj
    OSPF-1 ADJ  Fa4/0: Rcv pkt from 10.1.35.3,  :  Mismatched Authentication Key - Clear Text

    R5(config-if)# ip ospf authentication-key cisco123
    OSPF-1 ADJ  Fa4/0: 2 Way Communicastion to 3.3.3.3, state 2WAY
    <...truncated...>
    %OSPF-5-ADJCHG: Process 1, Nbr 3.3.3.3 on FastEthernet4/0 from LOADING to FULL, Loading Done
    R5(config-if)# end
    R5# undebug all

    ! same process applied to g1/0 on R3 and g2/0 on R7
    ```

- Demo config MD5 key for OSPF Area 2 routers
  - task: enable MD5 key for authentication on interfaces btw R6 & R8
  - cmd to set MD5 key: `ip ospf message-digest-key 1 md5 cisco123`
  - apply the md5 key to interfaces on R6 and R8

    ```text
    R6# show ip ospf
      Routing Process "ospf 1" with ID 1.1.1.1 
      <...truncated...>
        Area 2
            Number of interfaces in this area is 0
            Area has message digest authentication
      <...truncated...>

    R6# show cdp neighbor
    Device ID     Local Intrfce   Holdtme    Capability  Platform  Port ID
    R4            Fas 3/2         133           R        7206VXR   Ser 3/1
    R8            Fas 4/0         179           R        7206VXR   Fas 4/1

    R6# show ip ospf int f4/0
    FastEthernet4/0 is up and line protocol is up
    <...truncated...>
      Message digest authentication enabled
        No Key configured, using default key id 0

    R6# conf t
    R6(config)# int f4/0
    R6(config-if)# ip ospf message-digest-key 1 md5 cisco123

    R8(config)$ int f4/1
    R8(config-if)# ip ospf message-digest-key 1 md5 cisco123
    R8(config-if)# end
    ```

- Demo: config NULL authentication on OSPF Area 2
  - task: config null authentication btw R4 & R6

  ```text
  R4(config)# int ser 3/1
  R4(config-if)# ip ospf authentication null

  R6(config)# int ser 3/2
  R6(config-if)# ip ospf authentication null
  ```



## Implement OSPF Authentication

- Demo: config OSPF authentication
  - tasks
    - Area 0 w/ MD5 authentication
    - password: Cisco!23
    - R1 & R2 MD5 pw
    - R3 & R4 simple pw
    - R2 & R4 no auth
  - general config for R1 ~ R4
    
    ```cfg
    conf t
    router ospf 1
    area 0 authentication message-digest
    end
    ```

  - config R1 & R2 w/ MD5 pwd

    ```text
    R1# show cdp neighbors
    Device ID     Local Intrfce   Holdtme    Capability  Platform  Port ID
    Core1         Gig 1/0         119           R S I    IOSv      Gig 1/0
    R3            Gig 2/0         155             R      7206VXR   Gig 1/0

    R1# conf t
    R1(config)# int g1/0
    R1(config-if)# ip ospf message-digest-key 1 md5 cisco123
    R1(config-if)# end

    R2# show cdp neighbors
    Device ID     Local Intrfce   Holdtme    Capability  Platform  Port ID
    Core1         Gig 2/0         138           R S I    IOSv      Gig 2/0
    R4            Gig 1/0         173             R      7206VXR   Gig 2/0

    R2# conf t
    R2(config)# int g1/0
    R2(config-if)# ip ospf message-digest-key 1 md5 cisco123
    R2(config-if)# end
    ```

  - config R1 & R3 w/ simple pwd

    ```text
    ! verify R3 interface
    R3# show cdp neighbors
    Device ID     Local Intrfce   Holdtme    Capability  Platform  Port ID
    R1            Gig 1/0         138             R      7206VXR   Gig 2/0
    R4            Gig 4/0         160             R      7206VXR   Fas 4/1
    R5            Gig 4/1         168             R      7206VXR   Fas 4/0
    R8            Gig 3/2         157             R      7206VXR   Ser 3/1

    R3# show ip ospf int f4/0
    FastEthernet4/0 is up, line protocol is up
      <...truncated...>
      Message digest authentication enabled
        No key configured, using default key 0

    ! config f4/0 on R3 w/ simple password 
    R3# conf t
    R3(config)# int f4/0
    R3(config-if)# ip ospf authentication
    R3(config-if)# do show ip ospf int f4/0
    FastEthernet4/0 is up, line protocol is up
      <...truncated...>
      Simple password authentication enabled

    R3(config-if)# ip ospf authentication-key cisco123

    ! config f4/1 on R4 w/ simple password
    R4(config)# int f4/1
    R4(config-if)# do debug ip ospf adjacency
    OSPF-1 ADJ  Fa4/1: Rcv pkt from 10.0.34.3 : Mismatched Authentication type. Input packet specified type 1, ...
    R4(config-if)# ip ospf authentication-key cisco1233
    R4(config-if)# end
    %OSPF-5=ADJCHG: Process 1, Nbr 3.3.3.3 on FastEthernet4/1 from LOADING to FULL, Loading Done

    R4# undebug all
    R4# show ip ospf neighbors
    Neighbor ID     Pri State     Dead Time Address     Interface
    3.3.3.3         1   FULL/BDR  00:00:36  10.0.34.3   FastEthernet4/1
    2.2.2.2         1   FULL/BDR  00:00:35  10.0.24.2   GigabitEthernet2/0
    6.6.6.6         1   FULL/BDR  00:00:35  10.0.46.2   Serial3/1
    ```

  - config R2 & R4 w/o authentication

    ```text
    R2# show cdp neighbors
    Device ID     Local Intrfce   Holdtme    Capability  Platform  Port ID
    Core1         Gig 2/0         138           R S I    IOSv      Gig 2/0
    R4            Gig 1/0         173             R      7206VXR   Gig 2/0

    R2# conf t
    R2(config)# int g1/0
    R2(config-if)# ip ospf authentication null

    R4# show cdp neighbors
    Device ID     Local Intrfce   Holdtme    Capability  Platform  Port ID
    R2            Gig 2/0         158             R      7206VXR   Gig 1/0
    R3            Fas 4/1         158             R      7206VXR   Gig 4/0
    R6            Ser 3/1         137             R      7206VXR   Ser 3/2

    R4# conf t
    R4(config)# int g2/0
    R4(config-if)# ip ospf authentication null
    R4(config-if)# end
    ```

- Demo: verify reachability

  ```text
  R7# traceroute 192.168.1.8
  Tracing the route to 192.168.1.8
  VRF info: (vrf in name/id, vrf out name/id)
    1 10.1.57.5 100 ms ...
    2 10.1.35.3 64 ms ...
    3 10.0.13.1 96 ms ...
    4 10.0.12.2 88 ms ...
    5 10.0.24.4 276 ms ...
    6 10.2.46.6 176 ms ...
    7 10.2.68.8 148 ms ...
  ```



## Virtual Links and Authentication




## Troubleshooting OSPF Authentication Lab 01




## Troubleshooting OSPF Authentication Lab 02




## Troubleshoot OSPF Authentication for IPv4




## Virtual lab: Troubleshoot OSPF Authentication for IPv4




