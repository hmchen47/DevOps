# 20. Configure and Verify Cisco Dynamic ARP Inspection

Trainer: keith Barker


## Introducing Dynamic ARP Inspection (DAI)

- Learning goals
  - Dynamic ARP Inspection (DAI)
  - implement DAI
  - ARP ACL
  - DAI options and features


## Why is DAI Needed

- ARP and issue
  - PCA $\leftrightarrow$ PAC
    - ARP cache in PCA w/ entry - (IP-C, MAC-C)
    - ARP cache in PCC w/ entry - (IP-A, MAC-A)
  - PCB running malicious software to send ARP message w/ (IP-C, MAC-B)
  - PCA updating cache w/ entry - (IP-C, MAC-B)
  - PCB sending ARP message w/ (IP-A, MAC-B) as well
  - PCC updating cache w/ entry - (IP-A, MAC-B)
  - PCB forwarding received packets to appropriate destination after eavesdropping or manipulating
  - Solution: Dynamic ARP Inspection (DAI)

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('page')"
      src    = "img/20-arp.png"
      alt    = "APR process and issue"
      title  = "APR process and issue"
    />
  </figure>



## The Recipe and Commands for DAI

- DAI overview
  - DHCP snooping used to map IP and MAC addresses
  - commands
    - enable DAI on vlan: `ip arp inspecton clan 30`
    - enable intf as DAI trusted port: `if) ip arp inspect trust`
    - verify DAI: `show ip arp inspect vlan 30`
  - router a DHCP client $\to$ not offering DHCP snooping
    - manually config static L2 & L3 mapping
    - config the port on switch connected to router as a trusted port


## Implementing DAI

- Config DAI
  - topology:
    - R3 connected to Switch (SW) on port g3/3
    - PC2 connected to SW on port g0/2
    - another switch (subnet 10.1.0.0/24) connected to SW on port g0/1
  - task: implement DAI for SW
  
  ```bash
  ! verify DHCP snooping enabled
  SW# show ip dhcp snooping binding
  MacAddress           IpAddress    LeaseSec   Type           VLAN    Interface
  -------------------  ----------   ---------  -------------  ----    -------------------
  00:50:79:66:68:04    10.16.20.101 85604      dhcp-snooping   40     GigabitEThernet0/2
  00:15:5D:77:77:01    10.16.20.102 85689      dhcp-snooping   30     GigabitEthernet0/1
  Total number of binding: 2

  SW# shop ip arp inspection vlan 30
  Source Mac Validation       : Disabled
  Destination Mac Validation  : Disabled
  IP Address Validation       : Disabled
  
  Vlan Configuration Operation ACL Match Static ACL
  ---- ------------- --------- --------- ----------
    30 Disabled      Inactive
  
  Vlan ACL Logging DHCP Logging Probe Logging
  ---- ----------- ------------ -------------
    30 Deny        Deny         Off
  
  ! config interface trust first
  SW# conf t
  SW(config)# int g3/3
  
  SW(config-if)# do show cdp neighbor
  Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
  R3               Gig 3/3           154               R    7206VXR   Gig 1/0

  SW(config-if)# ip arp inspection trust
  SW(config-if)# exit

  ! enable DAI
  SW(config)# ip arp inspection vlan 30
  SW(config)# end

  ! verify DAI
  SW# show ip arp inspection vlan 30
  Source Mac Validation       : Disabled
  Destination Mac Validation  : Disabled
  IP Address Validation       : Disabled
  
  Vlan Configuration Operation ACL Match Static ACL
  ---- ------------- --------- --------- ----------
    30 Enabled       Active
  
  Vlan ACL Logging DHCP Logging Probe Logging
  ---- ----------- ------------ -------------
    30 Deny        Deny         Off

  ! ARP deny msgs
  SW#
  ...
  %SW_DAI-4-DHCP_SNOOPING_DENY: 2 Invalid ARPs (Req) on Gi0/1, vlan 30.
    ([0015.5d67.8322/10.1.0.111/0000.0000.0000/10.1.0.1/00:29:59 UTC ...])
  %SW_DAI-4-DHCP_SNOOPING_DENY: 2 Invalid ARPs (Req) on Gi0/1, vlan 30.
    ([0015.5d44.5566/10.1.0.120/0000.0000.0000/10.1.0.1/00:30:00 UTC ...])
  ...

  ! another switch connected to SW  w/ untrusted port
  ! DHCP messages dropped amd no (IP, MAC) mapping generated
  ```


## ARP Access Lists for Non-DHCP Devices

- Troubleshooting dropped ARP msgs from untrusted port connected to a switch
  - dropped DHCP messages allowed by permitted ACL
  
  ```bash
  SW# show ip dhcp snooping binding
  MacAddress           IpAddress    LeaseSec   Type           VLAN    Interface
  -------------------  ----------   ---------  -------------  ----    -------------------
  00:50:79:66:68:04    10.16.20.101 85604      dhcp-snooping   40     GigabitEThernet0/2
  00:15:5D:77:77:01    10.16.20.102 85689      dhcp-snooping   30     GigabitEthernet0/1
  Total number of binding: 2

  ! config interface trust first
  SW# conf t
  SW(config)# int g3/3
  SW(config-if)# ip arp inspection trust
  SW(config-if)# exit

  SW(config)# ip arp inspection vlan 30

  SW(config)# arp access-list DEMO-LIST
  SW(config-arp-nacl)# permit ip host 10.1.0.111 mac host 0015.5d67.8322
  SW(config-arp-nacl)# permit ip host 10.1.0.120 mac host 0015.5d44.5566
  SW(config-arp-nacl)# exit

  SW(config)# ip arp inspection filter DEMO-LIST vlan 30
  SW(config)# end

  SW# show arp access-list
  ARP access list DEMO-LIST
      permit ip host 10.1.0.111 mac host 0015.5d67.8322
      permit ip host 10.1.0.120 mac host 0015.5d44.5566

  SW# show arp inspection vlan 30
  Source Mac Validation       : Disabled
  Destination Mac Validation  : Disabled
  IP Address Validation       : Disabled
  
  Vlan Configuration Operation ACL Match Static ACL
  ---- ------------- --------- --------- ----------
    30 Enabled       Active    DEMO-LIST No
  
  Vlan ACL Logging DHCP Logging Probe Logging
  ---- ----------- ------------ -------------
    30 Deny        Deny         Off

  SW# show ip arp inspection statistics
  Vlan Forwarded Dropped DHCP Drops ACL Drops
  ---- --------- ------- ---------- ----------
    30        46      46         46          0
  
  Vlan DHCP Permits ACL Permits Probe Permit  Source MAC Failures
  ---- ------------ ----------- ------------  -------------------
    30            0          46            0                    0
  
  Vlan Dest MAC Failures IP Validation Failures Invalid Protocol Data
  ---- ----------------- ---------------------- ---------------------
    30                 0                      0                     0

  ! generate traffic from Kali Linux
  Kali# ifconfig
  eth0: flags=4163 ...
      inet 10.16.20.102 ...

  Kali# ping 10.16.20.7
  ....

  ! statistics increased
  SW# show ip arp inspection statistics
  Vlan Forwarded Dropped DHCP Drops ACL Drops
  ---- --------- ------- ---------- ----------
    30        101     46         46          0
  
  Vlan DHCP Permits ACL Permits Probe Permit  Source MAC Failures
  ---- ------------ ----------- ------------  -------------------
    30            1          99            0                    0
  
  Vlan Dest MAC Failures IP Validation Failures Invalid Protocol Data
  ---- ----------------- ---------------------- ---------------------
    30                 0                      0                     0
  ```


## Additional DAI Options and Features




## Applying DAI to the Production Network




## Review of Configure and Verify Cisco Dynamic ARP Inspection




## Configure and Verify Cisco Dynamic ARP Inspection



