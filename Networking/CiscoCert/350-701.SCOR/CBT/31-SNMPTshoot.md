# 31. Troubleshoot SNMP

Trainer: Keith Barker


## Introduction to Troubleshooting SNMP

- Learning goals
  - SNMP versions
  - SNMPv2 config and verification
  - SNMPv3 config and verification


## SNMP Overview

- SNMP fundamentals
  - components
    - agent: client software either built-in or add-on
    - manager: dedicated server or software running on PC
  - messages
    - `get` and `set` requests
      - from server to ask for info from agent
      - default: udp port 161
    - `traps` or `inform` message
      - report events to server
      - default: udp port 162
  - management information base (MIB)
    - a detailed record for each components on a device
    - tree structure
    - different MIBs from device to device
  - access control used to control who able to request info


- Versions of SNMP
  - SNMPv2c
    - using 'community strings' as passwords
    - specify different community strings for RO / RW `get` & `set` requests
  - SNMPv3
    - 'views' as scope of MIBs
    - 'groups' as the privilege of corresponding views
    - 'users' as the members of groups
    - rarely used due to complexity
    - example:
      - Group A able to do read only on View 1
      - Group B able to read/write permisssion on View 1



## SNMPv2 Configuration

- Demo: config SNMPv2c on R1
  - topology
    - R1 as SNMP agent
    - SNMP server connected to cloud
  
  - verify current SNMP config

    ```text
    R1# show run | inc snmp
    snmp-server community Cisco!23 RW
    <...truncated...>
    ```

  - verify SNMP manager settings
    - OBSERVIUM: an free SNMP manager
    - basic config: protocol version = v2c; transport = UDP; port = 161
    - SNMP v1/v2c authentication: SNMP community = Cisco!23
    - info about the connected device: graphs tab > subtabs - Graphs, System, Processor, Memory, Storage, Netstats, Firewall, Authentication, OSPF, Poller



## SNMPv3 Client Configuration




## SNMPv3 Server Configuration




## Troubleshooting SNMP



