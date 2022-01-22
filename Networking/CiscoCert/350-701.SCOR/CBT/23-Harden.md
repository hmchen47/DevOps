# 23. Network Infrastructure Device Hardening

Trainer: keith Barker


## Introduction to Device Hardening

- Learning goals
  - securing network infrastructure
  - best pratices to protect
    - management plane
    - control plane
    - data plane
  - routers and switches hardening



## Device Hardening Overview

- Device hardening overview
  - the process to eliminate a means of attack by 
    - patching vulnerabilities
    - turning off non-essential services and 
    - configuring system with security controls
      - password management
      - file permissions and 
      - disabling unused network ports
  - improving security possibly broken 
    - management plane
    - control plane
    - data plane
  - management plane
    - protocols btw users and systems
    - e.g., SSH, SNMP, NetFlow, FTP. TFTP, AAA, NTP, Syslog, etc.
  - control plane
    - protocols btw devices
    - e.g., routing protocols, STP, MAC addresses
  - data plane: user traffic, end-to-end


## Cisco Guide to Harden IOS Devices

- Cisco device hardening guideline
  - [Cisco Guide to Harden Cisco IOS Devices](https://www.cisco.com/c/en/us/support/docs/ip/access-lists/13608-21.html)
  - Document ID: 13608
  - considerations for the document
    - not every solution perfect for every network
    - testing every plan before deploying


## Management Plane Hardening

- General Management Plane Hardening
  - password mgmt: TACACS+ + local user account
    - `algorithm-type [md5 | scrypt | sha256]`: algorithm to user for hashing the plaintext secret, type 9 password
    - `secret`: using type 5 password
  - enhanced password security
  - login password retry lockout
  - no Service Password-Recovery
  - disable Unused Services (*)
  - EXEC Timeout: timeout connection
  - keepalives for TCP Sessions
  - management Interface Use: create loopback intf w/ IP address
  - Memory Threshold Notifications
  - CPU Thresholding Notification (*)
  - Reserve Memory for Console Access
  - Memory Leak Detector
  - Buffer Overflow: Detection and Correction of Redzone Corruption
  - Enhanced Crashinfo File Collection
  - Network Time Protocol: authentication always
  - Disable Smart Install

  ```text
  ! local user account
  R1(config)# username admin1 privilege 15 password Cisco!23
  R1(config)# username admin1 privilege 15 secret Cisco!23
  R1(config)# username admin1 privilege 15 algorithm-type scrypt secret Cisco!23

  ! disable unused services
  R1# show control-plane host open-ports
  Active internet connections (servers and established)
  Prot        Local Address      Foreign Address             Service    State
   tcp                 *:23                  *:0              Telnet   LISTEN

  ! enable ssh & https
  R1(config)# line vty 0 4
  R1(config-line)# transport input ssh
  R1(config-line)# exit
  R1(config)# ip http secure-server
  R1(config)# end

  R1# show control-plane host open-ports
  Active internet connections (servers and established)
  Prot        Local Address      Foreign Address             Service    State
   tcp                 *:22                  *:0          SSH-Server   LISTEN
   tcp                 *:23                  *:0              Telnet   LISTEN
   tcp                *:443                  *:0        HTTPS-Server   LISTEN
   tcp                *:443                  *:0           HTTP CORE ESTABLIS
  ```


- Limit Access to the Network with Infrastructure ACLs
  - infrastructure ACL:
    - on edge routers
    - only allowing from certain admin computers to access management plane
    - specifying connections from hosts or networks that need to be allowed to network devices
    - all other traffic to the infrastructure is explicitly denied
  - ICMP Packet Filtering
  - Filter IP Fragments
  - ACL Support for Filtering IP Options
  - ACL Support to Filter on TTL Value


- Secure Interactive Management Sessions
  - Management Plane Protection
  - Control Plane Protection: very granularity to protect CPU, queue, threshold, etc.; control plane policing - less granularity to protect CPU
  - Encrypt Management Sessions
  - SSHv2 (*)
  - SSHv2 Enhancements for RSA Keys
  - Console and AUX Ports
  - Control vty and tty Lines
  - Control Transport for vty and tty Lines
  - Warning Banners


- Authentication, Authorization, and Accounting
  - TACACS+ Authentication
  - Authentication Fallback
  - Use of Type 7 Passwords: even type 9
  - TACACS+ Command Authorization
  - TACACS+ Command Accounting
  - Redundant AAA Servers


- Fortify the Simple Network Management Protocol
  - SNMP Community Strings
  - SNMP Community Strings with ACLs
  - Infrastructure ACLs
  - SNMP Views
  - SNMP Version 3: preferred
  - Management Plane Protection


- Logging Best Practices
  - Send Logs to a Central Location
  - Logging Level
  - Do Not Log to Console or Monitor Sessions
  - Use Buffered Logging (*)
  - Configure Logging Source Interface
  - Configure Logging Timestamps


- Cisco IOS Software Configuration Management
  - Configuration Replace and Configuration Rollback
  - Exclusive Configuration Change Access
  - Cisco IOS Software Resilient Configuration
  - Digitally Signed Cisco Software
  - Configuration Change Notification and Logging

  ```text
  R1# dir
  ! get the iso file name

  R1# show software authenticity file flash0:vios-adventerprisek9-m

  ! configuration rollback
  R1(config)# archive
  R1(config-archive)# path flash0:KB-Backup.cfg
  R1(config-archive)# maximum 10
  R1(config-archive)# time-period 2
  R1(config-archive)# write-memory
  R1(config-archive)# log config
  R1(config-archive-log-cfg)# end

  ! verify rollback
  R1# dir 
  ! a copy of curren running config
  R1# write
  ! generate a startup config but also a copy of backup
  R1# configure replace flash0:KB-Backup.cfg-....
  ! replace current running config w/ the backup config
  ```




## Control Plane Hardening

- Primary considerations of control plane
  - routing protocols
  - authentication


- General Control Plane Hardening
  - consider to turn of the features
  - IP ICMP Redirects: suggesting better routes
  - ICMP Unreachables: hacker flooding to explore existence of subnets
  - Proxy ARP


- General Control Plane Hardening
  - consider to turn off the features
  - IP ICMP Redirects: suggesting better routes
  - ICMP Unreachables: hacker flooding to explore existence of subnets
  - Proxy ARP


- Limit CPU Impact of Control Plane Traffic
  - Understand Control Plane Traffic: drop pkts before impact CPU
  - Infrastructure ACLs (*)
  - Receive ACLs (*)
  - CoPP
  - Control Plane Protection
  - Hardware Rate Limiters


- Secure BGP
  - TTL-based Security Protections (*)
  - BGP Peer Authentication with MD5
  - Configure Maximum Prefixes
  - Filter BGP Prefixes with Prefix Lists (*)
  - Filter BGP Prefixes with Autonomous System Path Access Lists 


- Secure Interior Gateway Protocols
  - Routing Protocol Authentication and Verification with Message Digest 5
  - Passive-Interface Commands: stop sending routing updates
  - Route Filtering
  - Routing Process Resource Consumption


- Secure First Hop Redundancy Protocols (FHRP)
  - including: HSRP, VRRP, GLBP
  - no authentication by default


## Data Plane Hardening

- General Data Plane Hardening
  - IP Options Selective Drop
  - Disable IP Source Routing
  - Disable ICMP Redirects
  - Disable or Limit IP Directed Broadcasts


- Filter Transit Traffic with Transit ACLs
  - ICMP Packet Filtering
  - Filter IP Fragments
  - ACL Support for Filtering IP Options


- Anti-Spoofing Protections (*)
  - Unicast RPF
  - IP Source Guard
  - Port Security
  - Dynamic ARP Inspection
  - Anti-Spoofing ACLs


- Limit CPU Impact of Data Plane Traffic
  - Features and Traffic Types that Impact the CPU
  - Filter on TTL Value
  - Filter on the Presence of IP Options
  - Control Plane Protection


- Traffic Identification and Traceback
  - NetFlow (*)
  - Classification ACLs


- Access Control with VLAN Maps and Port Access Control Lists
  - Access Control with VLAN Maps
  - Access Control with PACLs
  - Access Control with MAC


- Private VLAN Use
  - Isolated VLANs
  - Community VLANs
  - Promiscuous Ports
  - VRF-lite


## Device Hardening Checklist

- Management Plane
  - Passwords
    - Enable MD5 hashing (secret option) for enable and local user passwords
    - Configure the password retry lockout
    - Disable password recovery (consider risk)
  - Disable unused services
  - Configure TCP keepalives for management sessions
  - Set memory and CPU threshold notifications
  - Configure
    - Memory and CPU threshold notifications
    - Reserve memory for console access
    - Memory leak detector
    - Buffer overflow detection
    - Enhanced crashinfo collection
  - Use iACLs to restrict management access
  - Filter (consider risk)
    - ICMP packets
    - IP fragments
    - IP options
    - TTL value in packets
  - Control Plane Protection
    - Configure port filtering
    - Configure queue thresholds
  - Management access
    - Use Management Plane Protection to restrict management interfaces
    - Set exec timeout
    - Use an encrypted transport protocol (such as SSH) for CLI access
    - Control transport for vty and tty lines (access class option)
    - Warn using banners
  - AAA
    - Use AAA for authentication and fallback
    - Use AAA (TACACS+) for command authorization
    - Use AAA for accounting
    - Use redundant AAA servers
  - SNMP
    - Configure SNMPv2 communities and apply ACLs
    - Configure SNMPv3
  - Logging
    - Configure centralized logging
    - Set logging levels for all relevant components
    - Set logging source-interface
    - Configure logging timestamp granularity
  - Configuration Management
    - Replace and rollback
    - Exclusive Configuration Change Access
    - Software resilience configuration
    - Configuration change notifications


- Control Plane
  - Disable (consider risk)
    - ICMP redirects
    - ICMP unreachables
    - Proxy ARP
  - Configure NTP authentication if NTP is being used
  - Configure Control Plane Policing/Protection (port filtering, queue thresholds)
  - Secure routing protocols
    - BGP (TTL, MD5, maximum prefixes, prefix lists, system path ACLs)
    - IGP (MD5, passive interface, route filtering, resource consumption)
  - Configure hardware rate limiters
  - Secure First Hop Redundancy Protocols (GLBP, HSRP, VRRP)


- Data Plane
  - Configure IP Options Selective Drop
  - Disable (consider risk)
    - IP source routing
    - IP Directed Broadcasts
    - ICMP redirects
  - Limit IP Directed Broadcasts
  - Configure tACLs (consider risk)
    - Filter ICMP
    - Filter IP fragments
    - Filter IP options
    - Filter TTL values
  - Configure required anti-spoofing protections
    - ACLs
    - IP Source Guard
    - Dynamic ARP Inspection
    - Unicast RPF
    - Port security
  - Control Plane Protection (control-plane cef-exception)
  - Configure NetFlow and classification ACLs for traffic identification
  - Configure required access control ACLs (VLAN maps, PACLs, MAC)
  - Configure Private VLANs



## Hardening Review

- Summary
  - management plane
  - control plane
  - data plane
  - checklist



