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
    - example:
      - Group A able to do read only on View 1
      - Group B able to read/write on View 1



## SNMPv2 Configuration




## SNMPv3 Client Configuration




## SNMPv3 Server Configuration




## Troubleshooting SNMP



