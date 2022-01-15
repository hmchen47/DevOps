# 41. Cisco Umbrella

Trainer: Keith Barker


## Introduction to Cisco Umbrella

- Learning goals
  - Cisco Umbrella
  - policy
  - identity
  - digital certificates
  - VA


## Cisco Umbrella Overview

- Cisco Umbrella overview
  - security issues of DNS
    - bad/incorrect info
    - malicious web site
    - tunneling by attackers
  - Umbrella
    - Talos providing intelligence
    - a could solution
    - DNS as part of Umbrella service
    - DNS requests forwarding to Umbrella


## Umbrella Components

- Umbrella components
  - OpenDNS public DNS server: 208.67.222.222 & 208.67.220.220
  - Umbrella DNS service (licensed): filtering 17 categories of web sites
  - local DNS server
    - virtual appliance installed in DHCP server
    - internet DNS forwards to local DNS server
    - external DNS forwards to public DNS server
  - remove access
    - Umbrella client on PC
    - redirect to OpenDNS
    - enforce filtering

- Demo: Umbrella DNS service
  - verify PC

    ```text
    PC> ipconfig -all
    Windows Ip Configuration:
      <...truncated...>
    Ethernet adapter EEthernet0:
      <...truncated...>
      IPv4 Address      : 192.168.1.116(preferred)
      Subnet Mask       : 255.255.255.0
      Default Gateway   : 192.168.1.1
      DNS Servers       : 8.8.8.8
      <...truncated...>
    ```

  - verify connectivity w/ web browser
    - open 'www,google.com' -> OK
    - open 'cbtnuggets.com' -> OK
    - open 'internetbadguys.com' -> OK
  - config DNS server to OpenDNS
    - Control Panel > Network and Internet > Network and Sharing Center > Change adapter settings
    - Ethernet0 > right click on icon > Properties
    - Ethernet-0 Properties > Internet Protocol Version 4(TCP/IPv4) > Properties
    - Use the forwarding DNS server address: Preferred DNS server = 208.67.222.222, 208.67.220.220
  - verify w/ 'internetbadbuys.com' -> Blocked
  - open 'welcome.umbrella.com' -> indicating Umbrella service used


## Policy Overview




## Policy Components




## Policy Creation




## Core Identities




## Umbrella CA Certificates




## Reporting and Investigation




## Umbrella VA




## Umbrella Summary



