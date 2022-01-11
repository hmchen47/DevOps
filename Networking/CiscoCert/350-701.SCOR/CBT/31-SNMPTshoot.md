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
    - 'views': scope of MIBs, where
    - 'groups': the privilege of corresponding views, what
    - 'users':
      - the members of groups, who
      - including user-name, groups, auth (key; MD5 | SHA), privacy (key, AES)
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
    - Obserium: a free SNMP manager
    - basic config: protocol version = v2c; transport = UDP; port = 161
    - SNMP v1/v2c authentication: SNMP community = Cisco!23
    - info about the connected device: graphs tab > subtabs - Graphs, System, Processor, Memory, Storage, Netstats, Firewall, Authentication, OSPF, Poller


## SNMPv3 Client Configuration

- Demo: config SNMPv3

  ```text
  ! verify current setting
  R1# show run | inc snmp
  snmp-server group GROUPA v3 priv read VIEW1
  snmp-server group GROUPB v3 priv read FULL write FULL
  snmp-server group admingroup v3 priv read fullview write fullview
  snmp-server view FULL iso included
  snmp-server view VIEW1 sysUpTime included
  snmp-server view VIEW1 ifOperStatus included
  snmp-server view fullview iso included
  snmp-server ifindex persist

  R1# conf t
  R1(config)# snmp-server user Jim admingroup v3 
    auth sha Cisco!23 prov aes 256 Cisco!23
  R1(config)# end
  ```

  ```text
  ! verify snmp settings
  ! running config unable to view user
  R1# show run | inc snmp
  snmp-server group GROUPA v3 priv read VIEW1
  <...truncated...>
  snmp-server ifindex persist

  R1# show snmp user
  User name: Jim
  Engine ID: 80000090300F4CFE249B1A0
  storage-type: nonvolatile   active
  Authentication protocol: SHA
  Privacy Protocol: SEA256
  Group-name: admingroup

  User name: Bob
  Engine ID: 80000090300F4CFE249B1A0
  storage-type: nonvolatile   active access-list: 1
  Authentication protocol: SHA
  Privacy Protocol: SEA256
  Group-name: GroupA
  <...truncated...>

  R1# show snmp view
  FULL iso - included nonvolatile active
  *ilmi system - included permanent active
  *ilmi atmForumUni - included permanent active
  VIEW1 systemUpTime - included nonvolatile active
  VIEW2 ifOperStatus - included nonvolatile active
  <...truncated...>

  R1# show snmp group
  <...truncated...>
  group name: GROUPA                    security mode:v3 priv
  contextname: <no context specified>   storage type: nonvolatile
  readview: VIEW1                       writeview: <no writeview specified>
  notifyview: <no notifyview specified>
  row status: active

  group name: GROUPB                    security mode:v3 priv
  contextname: <no context specified>   storage type: nonvolatile
  readview: FULL                        writeview: FULL
  notifyview: <no notifyview specified>
  row status: active

  group name: admingroup                security mode:v3 priv
  contextname: <no context specified>   storage type: nonvolatile
  readview: fullview                    writeview: fullview
  notifyview: <no notifyview specified>
  row status: active
  ```



## SNMPv3 Server Configuration





## Troubleshooting SNMP



