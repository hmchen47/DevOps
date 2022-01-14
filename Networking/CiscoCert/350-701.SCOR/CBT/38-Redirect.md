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

- Plan for web traffic redirect w/ WCCP
  - redirect TCP:80 and TCP:443 traffic to WSA
  - ACL to match and redirect traffic
  - config WCCP to adopt the ACLs
  - router w/ IP 192.168.1.136


## WSA Configuration for WCCP

- Demo: config WSA to redirect web traffic
  - topology
    - R1 w/ 192.168.1.136
    - WSA w/ 192.168.1.155
  - task: config WCCP to redirect web traffic to WSA
  - Web Security Virtual Appliance (WSA)
    - tabs - Reporting, Web Secure Manager, Security Services, Network, System Administration
    - Network tab > Transparent Redirection > Transparent Redirection Device: Type = L4 switch or No Device > 'Edit Device' button
    - Transparent Redirection > Transparent Redirection Device: Type = WCCP v2 Router; WCCP v2 Service > 'Add Service' button
    - Add WCCP v2 Service: Service Profile Name = JUST-HTTP; Service: standard Service ID: 0 web-cache (destination port 80) = On; Router IP address = 192.168.1.136; Router Security: Enable Security Service = On, Passphrase = `****` > 'Submit' button
    - Transparent Redirection > Transparent Redirection Device: Type = WCCP v2 Router; WCCP v2 Service: fields - Service Profile Name, Service ID, Router IP adddresses, Ports, Delete
    - entry - Service Progfile Name = Just-HTTP, Service ID = 0, Router IP addresses = 192.168.1.136, Ports = 80 > 'Add Service' button
    - Add WCCP v2 Service > Service Profile Name = HTTPS; Service: Dynamic Service ID = 90, Port numbers = 443, Router IP address = 192.168.1.136; Router Security: Enable Security fir Service = On, Passphrase = `****` > 'Submit' button
    - entry - Service Progfile Name = HTTPS, Service ID = 90, Router IP addresses = 192.168.1.136, Ports = 443
    - Transparent Redirection > 'Commit Changes' button on top right corner > Uncommit Changes > 'Commit Changes' button


## IOS Configuration for WCCP

- Demo: config Router for WCCP
  - PC w/ 192.168.1.116
  - `web-cache`: standard web caching serverice, i.e., port 80

  ```text
  SW# conf t
  ! config extended ACLs for web traffic 
  SW(config)# ip wccp source-interface vlan1
  SW(config)# ip access-list extended HTTP
  SW(config-ext-nacl)# permit tcp host 192.168.1.116 any eq 80
  SW(config-ext-nacl)# exit
  SW(config)# ip access-list extended HTTPS
  SW(config-ex-nacl)# permit ip tcp host 192.168.1.116 any eq 443
  SW(config-ex-nacl)# exit

  ! config standard ACL to redirect traffic
  SW(config)# ip access-list standard WSA
  SW(config-std-nacl)# permit host 192.168.1.155
  SW(config-std-nacl)# exit

  ! config WCCP
  SW(config)# ip wccp web-cache redirect-list HTTP group-list WSA password Cisco!23
  SW(config)# ip wccp 90 redirect-list HTTP group-list WSA password Cisco!23
  SW(config)# end

  SW# debug ip wccp packets
  WCCP-PKT:IPv4:S0: Sending ISY to 192.168.1.155, rcv_id:8
  WCCP-PKT:IPv4:S0: Sending 708 bytes rom 192.168.1.136 to 192.168.1.155
  WCCP-PKT:IPv4:D90: Sending ISY to 192.168.1.155, rcv_id:6
  WCCP-PKT:IPv4:D90: Sending 708 bytes rom 192.168.1.136 to 192.168.1.155
  SW# undebug all

  ! apply WCCP to interface
  SW# conf t
  SW(config)# int vlan 1
  SW(config-if)# ip wccp web-cache redirect in
  SW(config-if)# ip wccp 90 redirect in
  SW(config-if)# end

  ! verify config
  SW# show ip wccp
  Global WCCP information:
   Router information:
       Router Identifier:                   192.168.1.136
       Configured source-interface:         Vlan1

   Service Identifier: web-cache
       <...truncated...>
       Redirect access-list:                HTTP
       Total Packets Denied Redirect:       0
       Total Packets Unassigned:            0
       Group access-list:                   WSA
       <...truncated...>

   Service Identifier: 90
       <...truncated...>
       Redirect access-list:                HTTPS
       Total Packets Denied Redirect:       0
       Total Packets Unassigned:            0
       Group access-list:                   WSA
       <...truncated...>
  ```


## Testing WCCP

- Demo: verify WCCP redirecting web traffic
  - NB: clear browser cache before testing
  - PC IP addr: 182.168.1.116
  - verify PC auto and manual proxy setting: both off
  - verify PC reachability to the Internet: `ping 8.8.8.8`
  - open web browser w/ google search 'alcohol'
  - open any website w/ search result 
  - page asking for sign in w/ username and password via http://esa.ogit.com


## Traffic Redirection Summary

- Summary
  - PBR and WCCP to redirect web traffic for inspection
  - WSA to inspect web traffic



