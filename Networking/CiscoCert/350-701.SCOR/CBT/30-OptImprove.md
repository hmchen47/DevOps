# 30. Management Options to Improve Security

Trainer: Keith Barker


## Introduction to Secure Network Management

- Learning goals
  - secure management
  - syslog
  - NTP authentication
  - change control


## Overview of Secure Management

- Mechanisms to secure network management
  - out of band (OOB) management
    - separated management network physically or logically
    - isolated management traffic from user traffic
  - secure protocols: including SCP, SFTP, HTTPS, SNMPv3, VPN, SSL, SSH or IPsec
  - security measures
    - including DHCP snooping, ARP inspection (DAI), port security
    - preventing from using DTP
    - unused access ports assigned to unused VLAN
  - hardening
  - AAA
    - controling access and privilege
    - ISE and TACACS+ as Cisco solution
    - authentication: MFA or 2FA
    - parser views for local user to control access and privilege
    - implementing modular policy framework (MPF): class-maps, policy-maps
  - firewall
    - cisco solutions: FirePower, ASA
    - NetFlow Secure Event Logging (NSEL) in ASA able to generate reports
    - flow control w/ NetFlow v9, w/ actions - flow teardown or flow deny
    - NetFlow collector to generate charts and reports
  - software define network (SDN)
    - controller interacting w/ network devices
    - ensuring secure connecting btw controller and devices
  - change control
    - backup of configurations on devices


## Syslog Overview

- Syslog overview
  - what able to be logged
    - events on devices
    - what going on
    - what happending
    - logged locally or sent to server
  - commands
    - able to track all commands used w/ AAA
    - track w/ syslog as well
  - where the msgs to go and store
    - read only message stored on server besides syslog server


- Demo: config syslog on router
  - config syslog server: `logging host 2.2.2.2`
  - config the interface that the router uses to send syslog packets: `logging source-interface loop 0`
  - config the timestamp format for log msgs: `service timestamps log`

  ```text
  R1# show logging
  <...truncated...>
    Console logging: level debugging, 3800 messages logged, xml disabled,
                     filtering disbaled
    Monitor logging: level debugging, 0 messages logged, xml disabled,
                     filtering disbaled
    Buffer logging: level debugging, 3800 messages logged, xml disabled,
                     filtering disbaled
    Exception logging: size (8192 bytes)
    Count and timestamp logging messages: disabled
    Persistent logging: disabled
  
  R1# conf t
  ! config syslog server
  R1(config)# logging host 2.2.2.2
  %SYS-6-LOGGINGHOST_STARTSTOP: Logging to host 2.2.2.2 port 514 started ...

  R1(config)# logging source-interface loop 0
  R1(config)# service timestamps log datetime show-timezone localtime year msec
  R1(config)# service timestamps debug datetime show-timezone localtime year msec
  R1(config)# end

  R1# show ntp status
  Clock is synchronized, stratum 2, reference is 2.2.2.2
  <...truncated...>
  Nov 20 2020 1651:59.981 PST: %SYS-6-LOGGINGHOST_STARTSTOP: ...
  ```




## NTP with Authentication





## Change Control




