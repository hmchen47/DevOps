# 18. Configure and Verify Cisco Port Security

Trainer: Keith Barker


## Introducing Port Security

- Learning goals
  - configure and verify port security on a Cisco switch port
  - how to change the default settings of port security
  - how to use errdisable recovery
  - how to apply port security to multilayer switch trunk interfaces


## Understanding Port Security and Why we Need It

- Security challenges of switch port
  - 1\. who/what connect to the port
  - 2\. multiple ports via another switch
  - 3\. hacker - Content Addressable Memory (CAM) table overflow, Mac flooding


- Demo: CAM table overflow

  ```bash
  SW# show vlan brief
  VLAN Name           Status    Ports
  ---- -------------- --------- -----------------------------
  1    default        active    Gi0/3, Gi1/1, Gi1/2, Gi1/3
                                ...
  10   VLAN0010       active    Gi0/0
  20   VLAN0020       active    Gi1/0
  30   VLAN0030       active
  40   VLAN0040       active
  ...

  SW# show mac address-table vlan 10
          Mac Address Table
  Vlan  Mac Address     Type    Ports
  ----  -----------     ------  -----
    10  0015.5d44.5566  DYNAMIC Gi0/0
    10  0015.5d67.8322  DYNAMIC Gi0/0
    10  0015.d221.800a  DYNAMIC Gi0/1
    10  0015.d259.800a  DYNAMIC Gi0/1
  Total Mac Addresses for this criterion: 4

  SW# show mac address-table int g0/0 vlan 10
          Mac Address Table
  Vlan  Mac Address     Type    Ports
  ----  -----------     ------  -----
    10  0015.5d44.5566  DYNAMIC Gi0/0
    10  0015.5d67.8322  DYNAMIC Gi0/0
  Total Mac Addresses for this criterion: 2

  ! connect a Kali Linux box to g0/0
  SW# show mac address-table int g0/0 vlan 10
          Mac Address Table
  Vlan  Mac Address     Type    Ports
  ----  -----------     ------  -----
    10  0015.5d44.5566  DYNAMIC Gi0/0
    10  0015.5d67.8322  DYNAMIC Gi0/0
    10  0015.5d77.7701  DYNAMIC Gi0/0
  Total Mac Addresses for this criterion: 3

  Kali# macof -i eth0 -n 50

  SW# show mac address-table count vlan 10
  Mac Entries for Vlan 10:
  --------------------------
  Dynamic Address Count : 53
  Static Address Count  : 0
  Total Mac Addresses   : 53

  Total Mac Addess Space Available: 53207136
  ```



## Port Security Defaults


- Switch port mode
  - access mode: `switchport mode access`
  - host mode: `switchport host`
    - config as access mode
    - enable portfast
    - disable EtherChannel
  - 


## Implementing Port Security on Layer 2 Interface




## Customizing Port Security




## Configuring Auto Errdisable Recovery




## Applying Port Security Skills in Production




## Review of Configure and Verify Cisco Port Security




## Cisco CCNA (200-301) Assessment Lab: Security



