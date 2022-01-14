# 38. Capture and Redirection Methods

Trainer: Keith Barker


## Introduction to Capture and Redirection Methods

- Learning goals
  - capture and redirect web traffic
  - policy based routing
  - WSA and WCCP


## Capture and Redirection Overview

- Capturing and redirecting web traffic
  - web security appliance (WAS) connected in inside zone to examine the web traffic
  - explicit forwarding
    - computer configured to forward web traffic to WSA
    - configured manually 
    - automatic: proxy auto-config file (PAC), group policy object (GPO)
  - capture and redirect web traffic
    - network devices in the path of network to capture and redirect the web traffic
    - options
      - PBR: policy base routing
      - WCCP: web cache communication protocol


## Policy Based Routing (PBR) Overview

- Policy based routing overview
  - via access control list (ACL)
  - route map: if TCP:443 then forward to WSA
  - applied to interfaces in default gateway


## PBR Configuration and Testing

- Demo: config PBR
  - topology
    - PC not explicitly config to forward traffic to WSA
    - SW connecting PC, WSA, AD, R1 and other network devices
    - WAS w/ .155 IP address
    - AD w/ .100 IP address
    - R1 as the default gateway
  - task: redirect web traffic to WAS for inspection before browse the Internet
  - verify PV Windows proxy setting: Proxy Settings > Manual proxy setup > Use a proxy server = Off

  ```text
  PC> ip config /all
  <...truncated...>
  IPv4 Address      : 192.168.1.116
  Subnet Mask       : 255.255.255.0
  Deafult Gateway   : 192.168.1.136
  <...truncated...>

  ! open web browser to access a web site
  SW# show ip int brief | exclude una
  Interface     IP-Address      OK? Method  Status        Protocol
  Vlan1         192.168.1.136   YES VNARM   up            up

  SW# terminal monitor
  SW# who
      Line      User  Host(s)   Idle        Location 
     0 con 0          idle      00:00:34
  *  2 vty 1          idle      00:00:00  192.168.1.151

  ! config ACL
  SW# conf t
  SW(config)# ip access-list extended ACL-ForPBR
  SW(config-ext-nacl)# permit tcp host 192.168.1.116 any eq 443
  SW(config-ext-nacl)# exit
  SW(config)# route-map Redirect-Policy permit 10
  SW(config-route-map)# match ip address ACL-ForPBR
  SW(config-route-map)# set ip next-hop 192.168.1.155
  SW(config-route-map)# exit

  ! apply to interface
  SW(config)# int vlan1
  SW(config-if)# ip policy route-map Redirect-Policy
  SW(config-if)# end

  ! verify config
  SW# show ip policy
  Interface       Route map
  Vlan1           Redirect-Policy

  ! verify from PC w/ browser open fireballwhisky.com
  ! the web page unable to be displayed
  ```


## WCCP Overview and Planning




## WSA Configuration for WCCP




## IOS Configuration for WCCP




## Testing WCCP




## Traffic Redirection Summary



