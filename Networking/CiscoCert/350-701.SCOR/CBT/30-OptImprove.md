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





## NTP with Authentication





## Change Control




