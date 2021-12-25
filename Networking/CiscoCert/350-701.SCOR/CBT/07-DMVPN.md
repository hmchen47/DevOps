# 07. Cisco DMVPN

Trainer: Keith Barker


## Introduction to DMVPN

- Learning goals
  - concept of DMVPN
  - implementing and verifying mGRE
  - configuring and verifying of DMVPM

## DMVPN Overview

- DMVPN network
  - hub-spoke network
  - R1 w/ headquarter, R2 w/ site 2, and R3 w/ site 3
  - R1~3 connected via Internet, private network or MPLS
  - NBMA: Non-Broadcast Multiple Access
  - mGRE: tunnel interfaces btw R1 & R2, R1 & R3
  - user traffic from R2 to server connected to R3
  - R2 viewing R3 as the next hop $\to$ traffic directly from R2 to R3, not via R1
  - issue: how do R2 know the Ip address space, 35.3.3.0?
  - solution:
    - using mGRE + NHRP 
    - R2 & R2 dynamically negotiate to build tunnel btw
    - directly routing the traffic by themselves

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('page')"
      src    = "img/07-dmvpn.png"
      alt    = "text"
      title  = "text"
    />
  </figure>



## Planning for the mGRE Tunnel

- mGRE tunnel design
  - full mesh of tunnels
  - tunnel IP addresses: 172.16.123.0/24 w/ R1 = .1, R2 = .2, R3 = .3
  - tunnel type: mGRE - same tunnel intf for multiple pairing w/ other devices
  - tunnel source:
    - R1: 15.1.1.1 (G0/1)
    - R2: 25.2.2.2 (G0/2)
    - R3: 35.3.3.3 (G0/3)
  - tunnel destination: not required, dymanically identify the end of the tunnel
  - MTU (optional):
    - recommended: adjust maximum segment size
    - GRE w/ additional overhead
    - a little than the default value $\to$ no fragment for the final packets
  - tunnel key: same for all routers


## mGRE Tunnel Configuration

- Config mGRE on R1
  - preventing from packet segmentation w/ mtu = 1400

  ```bash
  ! DMVPN Hub
  R1#conf t
  R1(config)# int tunnel 0
  R1(config-if)# description DMVPN Hub
  R1(config-if)# ip address 172.16.123.1 255.255.255.0
  R1(config-if)# ip mtu 1400
  R1(config-if)# ip tcp adjust-mss 1360
  R1(config-if)# tunnel source g0/1
  R1(config-if)# tunnel mode gre multipoint
  R1(config-if)# tunnel key 6783
  R1(config-if)# end
  ```


- Config mGRE on R2

  ```bash
  R2# conf t
  R2(config)# int tunnel 0
  R2(config-if)# description DMVPN Spoke site 2
  R2(config-if)# ip address 172.16.123.1 255.255.255.0
  R2(config-if)# ip mtu 1400
  R2(config-if)# ip tcp adjust-mss 1360
  R2(config-if)# tunnel source g0/2
  R2(config-if)# tunnel mode gre multipoint
  R2(config-if)# tunnel key 6783
  R2(config-if)# end
  ```

- Config mGRE on R3

  ```bash
  R3# conf t
  R3(config)# int tunnel 0
  R3(config-if)# description DMVPN Spoke site 3
  R3(config-if)# ip address 172.16.123.3 255.255.255.0
  R3(config-if)# ip mtu 1400
  R3(config-if)# ip tcp adjust-mss 1360
  R3(config-if)# tunnel source g0/3
  R3(config-if)# tunnel mode gre multipoint
  R3(config-if)# tunnel key 6783
  R3(config-if)# end
  ```


## NHRP Overview and Design

- NHRP overview
  - only tunnel interface config on R1~3
  - none knowing what the other side of tunnel suppose to be
  - NHRP used to
    - train spokes to check in the hub
    - dynamically learn the reachable addresses btw themselves


- NHRP design
  - build tunnel btw R1 & R2, R1 & R3
  - train R2/R3 to know where the hub is
  - multicast packet on R2/R3 sending to the hub
  - config the tunnel IP address to associate w/ the public NBMA address
    - R1: 172.16.123.1 $\leftrightarrow$ 15.1.1.1
    - R2: 172.16.123.2 $\leftrightarrow$ 25.2.2.2
    - R3: 172.16.123.3 $\leftrightarrow$ 35.3.3.3
  - NHRP authentication password: Cisco!23
  - train R1 to dynamically learn the other end of the tunnels
  - next hop server (NHS) config on R2 & R3
    - R2 sending packet to 172.16.123.3
    - R2 not knowing the R3
    - specify the next hop server as R1
    - a request sent to R1 for getting the reachable address of 17216.123.3
    - R1 returns the details of R3
    - R2 proceeds to build tunnel w/ R3
  - goal of DMVPN: dynamically building tunnels btw spokes, in particular, many spokes
  - R1 redirecting traffic w/ NHRP while R2 & R3 building a NHRP shortcut


## Configuring NHRP for DMVPN

- Config NHRP on hub

  ```bash
  R1# conf t
  R1(config)# int tunnel 0
  R1(config-if)# authentication Cisco!23
  R1(config-if)# ip nhrp map multicast dynamic
  R1(config-if)# ip nhrp network-id 1223
  R1(config-if)# ip nhrp redirect
  R1(config-if)# end
  ```


- Config NHRP on spokes (R2 & R3)
  - NHS using tunnel IP address of hub
  - mapping tunnel address to public Ip address (T.P.)
  - tunnel supporting multicast by forwarding to public IP address of hub

  ```bash
  R2# conf t
  R2(config)# int tunnel 0
  R2(config-if)# authentication Cisco!23
  R2(config-if)# ip nhrp map 172.16.123.1 15.1.1.1
  R2(config-if)# ip map multicast 15.1.1.1
  R2(config-if)# ip nhrp network-id 1223
  R2(config-if)# ip nhs 172.16.123.1
  R2(config-if)# ip nhrp shortcut
  R2(config-if)# end

  R2# show run int tun 0
  Current configuration : 379 bytes
  !
  interface Tunnel0
   description DMVPN spoke site 2
   ip address 172.16.123.3 255.255.255.0
   no ip redirects
   ip mtu 1400
   ip nhrp authentication Cisco!23
   ip nhrp map 172.16.123.1 15.1.1.1
   ip nhrp map multicast 15.1.1.1
   ip nhrp network-id 123
   ip nhrp nhs 172.16.123.1
   ip tcp adjust-mss 1360
   tunnel source GigbitEthernet0/3
   tunnel mode gre multipoint
   tunnel key 123
  end
  ```


- Verify NHRP settings

  ```bash
  R1# show ip nhrp
  172.16.123.2/32 via 172.16.123.2
     Tunnel0 created 00:01:17, expire 00:08:43
     Type: dynamic, Flags: registered nhop
     NBMA address: 25.2.2.2
  172.16.123.3/32 via 172.16.123.3
     Tunnel0 created 00:01:08, expire 00:08:52
     Type: dynamic, Flags: registered nhop
     NBMA address: 35.3.3.3
  ```

  ```bash
  R2# show ip nhrp
  172.16.123.1/32 via 172.16.123.1
     Tunnel0 created 00:02:06, never expire
     Type: static, Flags:
     NBMA address: 15.1.1.1
  ```


## Adding Routing to DMVPN




## Verifying DMVPNs




## Adding IPsec Protection Profiles




## DMVPN Summary




