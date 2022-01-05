# 21. Private VLANS

Trainer: Keith Barker


## Introduction to Private VLANs

- Learning goals
  - PVLANs modes
  - config PVLANs
  - Verify PVLANs
  - trunkking w/ PVLANs


## PVLANs Overview

- VLAN fundamentals
  - traditional VLAN
    - create a vlan, said Vlan 100
    - asssign vlan 100 to a couple of ports
    - the ports w/ L3 scheme 10.100.0.0/24
    - frames allowed to send btw ports using broadcast
  - issue w/ traditional vlan: unable to filter broadcast frames
  - solution: PVLAN
  
  
- Private VLAN (PVLAN) fundamentals
  - create a primary vlan, said vlan 100
  - logical sub-divisions of primary vlan created to separate the ports
  - secondary vlan as the sub-section of primary vlan
  - create secondary vlans associated w/ a subset of ports in the primary vlan
  - two types of secondary vlans
    - community:
      - ports within the same community able to communicate w/ each other
      - ports belonging to different communit vlans unable to communicate w/ each other
    - isolated: ports within unable to communicate w/ each other
  - ports w/ the same primary vlan and IP address space $\to$ IP address not decisive


## Promiscuous Ports

- Promiscuous ports overview
  - ports w/o any restriction in a primary vlan
  - acting as a default gateway in L3 routing
  - example:
    - primary vlan = 100, community vlan = 200, community vlan = 300, isolated vlan = 400
    - IP address space of vlan 100: 10.100.0.0/24
  - promiscuous ports
    - associated w/ primary vlan, not any secondary vlan
    - able to communicate w/ any port in the primary vlan
    - ports connected to other switches as trunk


## PVLAN Design

- Planning PVLAN
  - primary vlan: 100
  - IP address space: 10.100.0.0/24
  - community vlan: 200 w/ port 0/1-2
  - community vlan: 300 w/ port 1/1-2
  - isolated vlan: 400 w/ port 2/1-2


## Implement PVLANs

- Config PVLAN

  ```bash
  SW1# conf t

  ! reset existed config
  SW1(config)# no vlan 2-1000
  SW1(config)# deafult int range g0/0-3
  SW1(config)# default int range 1/0-3
  SW1(config)# default int range 2/0-3

  SW1(config)# spanning mode rapid

  SW1(config)# vtp mode ransport

  ! create secondary vlan
  SW1(config)# vlan 200
  SW1(config-vlan)# name Community A
  SW1(config-vlan)# private-vlan community
  SW1(config-vlan)# exit
  
  SW1(config)# vlan 300
  SW1(config-vlan)# name Community B
  SW1(config-vlan)# private-vlan community
  SW1(config-vlan)# exit
  
  SW1(config)# vlan 400
  SW1(config-vlan)# name Isolated VLAN
  SW1(config-vlan)# private-vlan isolated
  SW1(config-vlan)# exit
  
  ! create primary vlan
  SW1(config)# vlan 100
  SW1(config-vlan)# name Primary VLAN
  SW1(config-vlan)# private-vlan primary
  SW1(config-vlan)# private-vlan association 200, 300, 400
  SW1(config-vlan)# exit

  ! associate ports w/ pvlan
  SW1(config)# interface range GigabitEthernet0/1-2
  SW1(config-if)# switchport private-vlan host-association 100 200
  SW1(config-if)# switchport mode private-vlan host
  SW1(config-if)# exit

  SW1(config)# interface range GigabitEthernet1/1-2
  SW1(config-if)# switchport private-vlan host-association 100 300
  SW1(config-if)# switchport mode private-vlan host
  SW1(config-if)# exit

  SW1(config)# interface range GigabitEthernet2/1-2
  SW1(config-if)# switchport private-vlan host-association 100 400
  SW1(config-if)# switchport mode private-vlan host
  SW1(config-if)# exit

  ! switch virtual interface w/ vlan 100
  SW1(config)# interfac vlan 100
  SW1(config-if)# no shutdown
  SW1(config-if)# private-vlan mapping add 200,300,400
  SW1(config-if)# ip addr 10.100.0.1 255.255.255.0
  SW1(config-if)# end
  ```

## Verify PVLANs




## Trunking and PVLANs




## PVLAN Summary



