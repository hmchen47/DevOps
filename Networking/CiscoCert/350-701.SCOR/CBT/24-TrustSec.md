# 24. Configure Cisco TrustSec

Trainer: Keith Barker


## Introduction to TrustSec

- Learning goals
  - TrustSec
  - group ACLs
  - TrustSec policies
  - config TrustSec
  - verify TrustSec
  - SGT eXchange protocol (SXP)


## TrustSec Overview

- TrustSec overview
  - Device A connected to SW-A w/ MAB or 802.1x
  - identity of user authenticated via ISE
  - security group
    - used for authentication
    - a logical group w/ members
  - security group associated w/ a security group tag (SGT), a number
  - example: 3 security groups
    - ISE-admin w/ STG = 18
    - ISE-Ops w/ STG = 19
    - PCB-PCs w/ tag = 20
  - frames w/ a security group traversing across network including STG
  - able to control frames btw groups and within group
  - ISE able to implement policies btw security groups

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=200
        src    = "img/24-trustsec.png"
        alt    = "Example network for TrustSec"
        title  = "Example network for TrustSec"
      >
    </a>
    <a href="https://www.routexp.com/2019/05/introduction-to-secure-group-tagging-sgt.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=160
        src   = "https://bit.ly/32Nfp1j"
        alt   = "Secure Group Tagging"
        title = "Secure Group Tagging"
      >
    </a>
  </div>



## TrustSec Security Groups

- Demo: create TrustSec security groups on ISE
  - Work Centers tab > TrustSec: subtabs - Overview, Components, TrustSec Policy, Policy Sets, SXP, Troubleshoot, Reports, Settings
  - Components subtab > folders - Security Groups, IP SGT Static Mapping, Security Group ACLs, Network Devices, TrustSec Servers > Security Groups
  - Security Groups: fields - Icon, Name, SGT (Dec/Hex), Description; Icons - Edit, Add, Import, Export, Trash, Push, Verify Deploy
    - entry: Name = Auditors, SGT = 9
    - entry: Name = BYOD, SGT = 15
  - 'Add' icon > Security Groups List > New Security Group: Name = ISE_Admin, SGT = 16 > 'Submit' button
  - 'Add' icon > Security Groups List > New Security Group: Name = ISE_Ops, SGT = 17 > 'Submit' button
  - 'Add' icon > Security Groups List > New Security Group: Name = PCB_PCs, SGT = 18 > 'Submit' button


## Security Group ACLs

- Demo: create security group policies on ISE
  - Work Centers tab > TrustSec > Components subtab > Security Group ACLs
  - Security Group ACLs: fields - Name, Description, IP Version; Icons - Edit, Add, Duplicate, Push, Verify Deploy
  - 'Add' icon > Security Group ACLs: Name = NO_ICMP, IP Version = IPv4, Security Group ACL content = 'deny icmp' + 'permit ip' > 'Submit' button
  - Security Group ACLs: new entry - Name = NO_ICMP, IP Version = IPv4
  - 'Add' icon > Security Group ACLs: Name = No_Telnet, IP Version = IPv4, Security Group ACL content = 'deny tcp dst eq 23' + 'permit ip' > 'Submit' button
  - Security Group ACLs: new entry - Name = No_Telnet, IP Version = IPv4


## TrustSec Policies

- Plan for TrustSec policies btw groups
  - deny telnet: ISE-Ops $\to$ PCB-PCs
  - deny telnet: ISE Admin $\to$ PCB-PCs
  - deny peer FTP: PCB-PCs $\leftrightarrow$ PCB-PCs


- Demo: create TrustSec policies on ISE
  - Work Centers tab > TrustSec > TrustSec Policy subtab > folders - Egress Policy (Metrices List, Matrix, Source Tree, Destination Tree), Network Device Authorization
  - Matrix: Vertical = Source, Horizontal = Destination; Icons - Edit, Add, Clear, Deploy, Verify Deploy, Monitor All -Off, Import, Export, View
  - View: Condensed with SGACL names, Condensed without SGACL names, Full with SGACL names, Full without SGACL names
  - 'Add' icon > Create Security Group ACL Mapping ... > Source Security Group = ISE_Admin; Destination Security Group = PCB_PCs; Assigned Security Group ACLs = No_Telnet > 'Save' button
  - 'Add' icon > Create Security Group ACL Mapping ... > Source Security Group = ISE_Ops; Destination Security Group = PCB_PCs; Assigned Security Group ACLs = No_Telnet > 'Save' button


## Configure Network Devices for TrustSec

- Demo: config network devices for TrustSec
  - SW-A = SW2-3750x
    - a Catalyst 3750 box w/ console access
    - 3 devices connected to SW2: 2 windows, 1 raspberry pie
  - `cts` = Cisco TrustSec
  - `cts logging verbose`: debugging purpose; terminal monitored, otherwise, vty w/ ssh occupies the bandwidth
  - `pac` = protected access credential
  - `cts credentials id SW2-3750x-136 password Cisco!23`: config on privilege mode
  - `cts refresh`: ensure ISE updated

  ```text
  SW2# conf t
  SW2(config)# cts authorization list DemoSGList
  SW2(config)# aaa authorization network DemoSGList group Demo-Group
  SW2(config)# cts logging verbose
  SW2(config)# cts role-based enforcement
  SW2(config)# cts role-based enforcement vlan-list all
  SW2(config)# radius-server vsa send authentication
  SW2(config)# dot1x system-auth-control

  SW2(config)# radius server Demo_ISE
  SW2(config)# pac key Cisco!23
  SW2(config)# exit

  SW2# cts credentials id SW2-3750x-136 password Cisco!23
  SW2# show cts pacs
  AID: CE01...56FE
  PAC-Info:
    PAC-type = Cisco TrustSec
    AID = CE01...56FE
    I-ID: SW2-3750x-136
    A-ID_Info: Identity Service Engine
    Credential Lifetime: 22:44:34 UTC ...
  PAC-Opaque: 0002...6DE9
  Refresh timer is set for 14y42w

  SW2# cts refresh environment-data
  Environment data download in progress
  SW2# cts refresh policy
  Policy refresh in progress

  SW2# show cts environment-data
  CTS Environment Data
  ====================
  Current state = COMPLETE
  Last status = successful
  Local Device SGT:
    SGT tag = 2-04:TrustSec_Devices
  Server List Info:
  <...TRUNCATED...>
  Security Group Name Table:
    <...TRUNCATED...>
    16-c3:ISE_Admins
    17-c3:ISE_Ops
    18-c3:PCB_PCs
  <...TRUNCATED...>
  ```


## ISE and NAD TrustSec Integration




## Verify TrustSec




## SGT eXchange Protocol (SXP)



