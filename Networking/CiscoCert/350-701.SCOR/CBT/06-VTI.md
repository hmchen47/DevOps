# 06. Cisco Point-To-Point GRE over IPsec VPNs

Trainer: Keith Barker


## Introduction to P2P GRE over IPsec VPNs

- Learning goal
  - GRE tunneling protocol
  - the configuration and verification of Cisco Remote Access VPNs
  - the use of AnyConnect
  - the configuration and verification of Cisco Remote Access VPNs
  - the use of AnyConnect


## Overview of GRE over IPsec VPNs

- Issues of IPsec tunnel
  - originally designed for site-to-site IPsec VPN
  - no logical IP address w/ S2S IPsec tunnel
  - not supporting broadcast and multicast
  - unable to use routing protocols


- Generic Routing Encapsulation (GRE)
  - a protocol for encapsulating data packets to set up a direct network connection
  - creating GRE tunnel to enable
    - network address space associated to the tunnel
    - carrying other protocols other than IP only
    - broadcast and multicast w/ the address space
    - running routing protocols
  - packet format

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
        onclick= "window.open('https://ipcisco.com/lesson/gre-tunnel-overview-ccnp/')"
        src    = "https://ipcisco.com/wp-content/uploads/gre-header-1.jpg"
        alt    = "GRE Header"
        title  = "GRE Header"
      />
    </figure>

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://blog.51sec.org/2016/10/cisco-ios-router-configuration-ipsec.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=160
        src   = "https://thenetworkology.files.wordpress.com/2013/07/ipsec-over-gre.png"
        alt   = "IpSec ove GRE"
        title = "IpSec ove GRE"
      >
    </a>
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=160
        src   = "https://thenetworkology.files.wordpress.com/2013/07/gre-over-ipsec2.png"
        alt   = "GRE ove IPsec"
        title = "GRE ove IPsec"
      >
    </a>
  </div>

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://blog.51sec.org/2016/10/cisco-ios-router-configuration-ipsec.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=110
        src   = "https://www.firewall.cx/images/stories/gre-ipsec-tunnel-transport-1.gif"
        alt   = "IpSec ove GRE packet format"
        title = "IpSec ove GRE packet format"
      >
    </a>
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=110
        src   = "https://www.firewall.cx/images/stories/gre-ipsec-tunnel-transport-2.gif"
        alt   = "GRE ove IPsec packet format"
        title = "GRE ove IPsec packet format"
      >
    </a>
  </div>


## P2P GRE Tunnel Design

- Designing GRE tunnel
  - create tunnel btw R1 & R2
  - tunnel address space: 10.12.12.0/24
  - use EIGRP as routing protocol
    - autonomous system: 1
    - network: 10.0.0.0/8 



## P2P GRE Tunnel Implementation

- Implementing P2P GRE tunnel on R1

  ```bash
  ! verify interface config
  R1# sh ip int br
  Interface           IP-Address  OK? Method  Status                Protocol
  GigabitEthernet0/0  unassigned  YES TFTP    administratively down down
  GigabitEthernet0/1  15.1.1.1    YES TFTP    up                    up
  GigabitEthernet0/2  unassigned  YES TFTP    administratively down down
  GigabitEthernet0/3  10.1.0.1    YES TFTP    up                    up

  ! create tunnel intf 0 w/ Ip addr
  R1# conf t
  R1(config)# int tunnel 0
  R1(config-if)# ip addr 10.12.12.1 255.255.255.0
  R1(config-if)# tunnel source 15.1.1.1
  R1(config-if)# tunnel destination 25.2.2.2
  R1(config-if)# do show run int tun 0
  Current configuration : 115 bytes
  ! 
  interface Tunnel0
   ip address 10.12.12.1 255.255.255.0
   tunnel source 15.1.1.1
   tunnel destination 25.2.2.2
  end
  ```


- Implementing P2P GRE tunnel on R2

  ```bash
  R2# conf t
  R2(config)# int tunnel 0
  R2(config-if)# ip addr 10.12.12.2 255.255.255.0
  R2(config-if)# tunnel source 25.2.2.2
  R2(config-if)# tunnel destination 15.1.1.1
  R1(config-if)# do show run int tun 0
  Current configuration : 115 bytes
  ! 
  interface Tunnel0
   ip address 10.12.12.2 255.255.255.0
   tunnel source 25.2.2.2
   tunnel destination 15.1.1.1
  end
  ```


- Config EIGRP on R1 & R2

  ```bash
  R2# show ip route
  Gateway of last resort is not set

  s*    0.0.0.0 [1/0] via 25.2.2.5
        10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
  C        10.2.0.0/24 is directly connected, GigabitEthernet0/3
  L        10.2.0.1/32 is directly connected, GigabitEthernet0/3
  C        10.12.12.0/24 is directly connected, Tunnel0
  L        10.12.12.1/32 is directly connected, Tunnel0
        25.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
  C        25.2.2.0/24 is directly connected, GigabitEthernet0/2
  L        25.2.2.2/32 is directly connected, GigabitEthernet0/2

  ! config EIGRP
  R2# conf t
  R2(config)# router eigrp 1
  R2(config-router)# no auto-summary
  R2(config-router)# net 10.0.0.0 0.255.255.255
  R2(config-router)# end

  R2#sh ip eigrp interfaces 
  EIGRP-IPv4 Interfaces for AS(1)
                          Xmit Queue   Mean   Pacing Time   Multicast    Pending
  Interface        Peers  Un/Reliable  SRTT   Un/Reliable   Flow Timer   Routes
  Gi0/3              0        0/0         0       0/1            0           0
  Tu0                0        0/0         0       6/6            0           0
  ```

  ```bash
  ! config EIGRP
  R1# conf t
  R1(config)# router eigrp 1
  R1(config-router)# no auto-summary
  R1(config-router)# net 10.0.0.0 0.255.255.255
  R1(config-router)# end

  R1# show ip route eigrp
  Gateway of last resort is not set

        10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
  D        10.2.0.0/24 [90/26880256] via 10.12.12.2 00:00:09, Tunnel0
  ```


## P2P GRE Tunnel Verification




## IPsec Tunnel Protection Design




## IPsec Virtual Tunnel Interface Configuration




## IPsec Static VTI Verification





