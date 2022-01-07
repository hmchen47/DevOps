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

- Demo: integrating ISE and NAD TrustSec
  - Work Centers > TrustSec > Components subtab > Network Devices folder
  - Network Devices: fields - Name, IP/Mask, Profile Name, Location, Type, Description > entry - Name = SW2-3750x-136, IP/Mask = 192.168.1.136 > 'SW2-3750x-136' link
  - Network Devices: Name = SW2-3750x-136, Description = 'Sw2 at .136', IP Address = 192.168.1.136/32, Device Profile = Cisco, RADIUS Authentication Settings, Advanced TrustSec Settings
  - Advanced TrustSec Settings: sections - Device Authentication Settings, HTTP REST API Settings, TrustSec Notification and Updates, Device Configuration Deployment, Out of Bound (OOB) TrustSec PAC > Advanced TrustSec Settings = On
    - Device Authentication: Use Device ID for TrustSec Identification = On, Device Id = SW2-3750x-136
    - TrustSec Notification and Updates: Send Configuration changes to device = On Using CoA = On (Change of Authorization), Send to = ISE-02 > 'Test Connection' button > green checked
    - Device Configuration Deployment: Include this device when deploying Security Group Tag Mapping Updates = On, EXEC Mode Username = admin, EXEC Mode Password = `****`, Enable Mode Password = `****`
    - Out of Bound (OOB) TrustSec PAC > 'Generate PAC' button
    - Generate Pac: Identity = SW2-3750x-136, Encryption Key = `****`, PAC Time to Live = 1 week > 'Generate' button


## Verify TrustSec

- Demo: verify TrustSec config
  - topology
    - SW2 @ .133
    - Bob connected to SW2 w/ g2/0/1, SG = ISE_Ops
    - Luis connected to SW2 on g2/0/2, SG = ISE_ADmins
    - PCB-PC connected to SW2 w/ MAB on g2/0/2

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
        onclick= "window.open('page')"
        src    = "img/24-trustsecnet.png"
        alt    = "Example network for TrustSec"
        title  = "Example network for TrustSec"
      />
    </figure>

  - bring up SW interfaces
  
    ```text
    SW2(config)# int range g2/0/1-3
    SW2(config-if-range)# no shutdown
    SW2(config-if-range)# end

    ! TrustSec SXP
    SW2# term mon
    %CTS-6-SXP_TIMER_STOP: Connection <192.168.1.136> hold timer stopped
    %CTS-6-SXP_TIMER_START: Connection <192.168.1.136> hold timer started
    ```

  - verify interface status on ISE
    - Operatoins tab > RADIUS subtab > Live Logs: fields - Time, Status, Details, Repeat, Identity, Endpoint D, Endpoint P, Authentication, Authorization
    - entries - Identity = DC:A6:32:96:92:A8; Identity = Bob; Identity = Luis > Identity = DC:A6:32:96:92:A8 > 'Details' icon
    - Authentication: section - Overview, Authentication Details, Steps
  - policy for TrustSec (Matrix): Work Centers tab > TrustSec > TrustSec Policy subtab
  - modify authentication/authorization policy
    - Policy tab > Policy Sets subtab: fields - Status, Policy Set Name, Description, Conditions, Allowed Protocols / Server Sequence, Hits, Actions, View
    - entry - Policy Set Name = Our-Site1-Switch-Policy-Set; Conditions = 'Device-Location EQUALS All Locations#site1' AND 'DEVICE-Device Type EQUALS ALL Device TYpes#switch' > 'View' icon
    - Policy Sets -> Out-Site1-Switch-Policy-Set: sections - Authentication, Authorization Policy - Local Exceptions, Authorization Policy - Global Exceptions, Authorization Policy
      - Authentication Policy: entries - Rule Name = Our-Authen-dot1x, Our-Authen-MAB, Default
      - Authorization Policy: entry - Rule Name = ISE-OPS, Results = ISE_Operations
      - Authorization Policy: entry - Rule Name = Admins, Results = Ise-admins
      - Authorization Policy: Rule Name = MAB-Author-Rule, Results = PCB-PC Author Profile
  - verify authentication & authorization
    - Operations tab > RADIUS subtab > Live Logs 
      - entry - Identity = bob, Status = session icon > 'Details' icon > Overview: Authorization Result = ISE-OPerations
      - entry - Identity = Luis, Status = session icon > 'Details' icon > Overview: Authorization Result = ise-admins
      - entry - Identity = DC:A6:32:96:92:A8, Status = session icon > 'Details' icon > Overview: Authorization Result = PCB-PC 
  - add TrustSec policy to Authorization policy
    - Policy tab > Policy Sets subtab > Authorization Policy
      - entry - Rule Name = ISE-OPS, Condition = Our-DC ExternalGroup EQUALS ogit.com/ISE-Operations, Results = (Profiles = ISE_Operations) + (Security Groups = ISE_Ops)
      - entry - Rule Name = Admins, Condition = Our-DC ExternalGroup EQUALS ogit.com/ISE-Admins, Results = (Profiles = ise-admins) + (Security Groups = ISE_Admins)
      - entry - Rule Name = MAB-Author-Rule, Condition = Network_Access_Authentication_Passed, Results = (Profiles = ISE_Operations) + (Security Groups = PCB_PCs)
      - 'Save' button > circle w/ 1 on top banner (beside Work Center tab) -> 'Completed sending 1 TrustSec CoA notificatona to releveant network devices.' > 'OK' button
  - verify pushing TrustSec policy on SW2
  
    ```text
    SW2# cts refresh environment-data
    SW2# cts refresh policy
    SW2# show cts security groups
    Security Group Table:
    =====================
      <...TRUNCATED...>
      16:ISE_Admins
      17:ISE_Ops
      18:PCB_PCs

    SW2# show authentication sessions
    Interface MAC Address     Method  Domain  Status  Fg  Session ID
    Gi2/0/3   dca6.3296.92a8  mab     DATA    Auth        Success 0A1E...6B15
    Gi2/0/2   8cae.4cfd.b87f  dot1x   DATA    Auth        Success 0A1E...6362
    Gi2/0/1   5882.a899.5c81  dot1x   DATA    Auth        Success 0A1E...6594
    Session count = 3

    SW2# show cts role-based sgt-map all
    IP Address        SGT         Source
    ============================================
    10.30.0.1         2           INTERNAL
    10.80.0.1         2           INTERNAL
    192.168.1.136     2           INTERNAL

    IP-SGT Active Bindings Summary
    ============================================
    Total number of INTERNAL bindings = 3
    Total number of active   bindings = 3
    ! SGT not 16, 17  & 18

    SW2# conf t
    SW2(config)# int range g2/0/1-3
    SW2(config-if-range)# shutdown
    SW2(config-if-range)# no shutdown
    SW2(config-if-range)# end

    SW2# show cts role-based sgt-map all
    IP Address        SGT         Source
    ============================================
    10.30.0.1         2           INTERNAL
    10.80.0.1         2           INTERNAL
    10.80.0.11        17          LOCAL
    10.80.0.12        18          LOCAL
    10.80.0.13        16          LOCAL
    192.168.1.136     2           INTERNAL

    IP-SGT Active Bindings Summary
    ============================================
    Total number of LOCAL    bindings = 3
    Total number of INTERNAL bindings = 3
    Total number of active   bindings = 6
    
    SW2# show cts role-based permissions
    IPv4 Role-based permissions default:
        Permit IP-00
    IPv4 Role-based permissions from group 16: ISE_Admins to group 18: PCB_PCs:
        No_Telnet-20
    IPv4 Role-based permissions from group 17: ISE_OPs to group 18: PCB_PCs:
        No_Telnet-20
    RBACL Monitor All for Dynamic Policies : FALSE
    RBACL Monitor All for Configured Policies : FALSE

    ! verify telnet    from ISE_Admins to PCB_PCs
    Admin> ping 10.80.0.12
    !!!!!

    Raspberrypi# ip addr
    <...TRUNCATED...>
    2: eth0: ...
      inet 10.80.1.12/24 ...
    
    ! testing terminal emulator to telnet 10.80.10.12 (no allowed)
    SW2# show cts role-based counters
    Role-based counters
    From To SW-Denied HW-Denied SW-Permitted HW_Permitted
    *    *  0         0         8233         5726
    16   18 0         5         0            16
    17   18 0         -         0            -
    ```

  - recommendation: test protocols before pulling SG ACLs



## SGT eXchange Protocol (SXP)

- SXP overview
  - not all devices w/ Cisco
  - a.k.a. Scalable Group Tag (SGT) eXchange protocol (SXP)
  - SGTs assigned to endpoints connecting to the network w/ common network policies
  - SXP:
    - a control-plane mechanism used to transport an endpoint's SGT w/ the IP address from one SGT-aware network device to another
    - a control protocol for propagating IP-to-SGT binding informationacross network devices w/o capability to tag packets
  - TrustSec filtering packets at egress interface


- Demo: config SXP
  - config on switches connecting the endpoints

    ```text
    SW2# conf t
    SW2(config)# cts sxp enable
    SW2(config)# cts sxp deafult password Cisco!23
    SW2(config)# cts sxp connection peer 192.168.1.105 password default mode peer speaker hold-time 0 0
    SW2(config)# end

    SW2# show cts security-groups
    Security Group Table:
    =====================
      <...TRUNCATED...>
      16:ISE_Admins
      17:ISE_Ops
      18:PCB_PCs

    SW2# show cts role-based sgt-map all
    IP Address        SGT         Source
    ============================================
    10.30.0.1         2           INTERNAL
    10.80.0.1         2           INTERNAL
    10.80.0.11        17          LOCAL
    10.80.0.12        18          LOCAL
    10.80.0.13        16          LOCAL
    192.168.1.136     2           INTERNAL

    IP-SGT Active Bindings Summary
    ============================================
    Total number of LOCAL    bindings = 3
    Total number of INTERNAL bindings = 3
    Total number of active   bindings = 6

    SW2# show authentication sessions
    Interface MAC Address     Method  Domain  Status  Fg  Session ID
    Gi2/0/3   dca6.3296.92a8  mab     DATA    Auth        Success 0A1E...461B
    Gi2/0/2   8cae.4cfd.b87f  dot1x   DATA    Auth        Success 0A1E...3EF6
    Gi2/0/1   5882.a899.5c81  dot1x   DATA    Auth        Success 0A1E...3F85
    Session count = 3

    SW2# show authentication sessions mac 5882.a899.5c81 details
              Interface:  GigabitEthernet2/0/1
              MAC Address:  5882.a899.5c81
               IP Address:  10.80.0.13
                User-Name:  Luis
                   Status:  Authzorized
                   Domain:  DATA
           Oper host mode:  multi-auth
         Oper control dir:  both
          Session timeout:  N/A
          Restart timeout:  N/A
    Periodic Acct timeout:  N/A
        Common Session ID:  Success 0A1E...3F85
          Acct Session ID:  0x00000054
                   Handle:  0x79000026
           Current Policy:  POLICY_Gi2/0/1

    Local Policy:
       Service Template: DEFAULT_LINKSEC_POLICY_SHOULD_SECURE (priority 150)
          Security Policy: Should Secure
          Security Status: Link unsecure
    Server Policy:
               Vlan Group:  Vlan: 80
                SGT Value:  16
      Methods status list:
              Method        State
              dot1x         Authc Success
    ```

  - verify ISE on ISe
    - Work Center tab > TrustSec > SXP subtab: folders - SXP Devices, All SXP Mappings
    - SXP Devices: fields - Name, IPAddress, Status, Peer Role, Password, Negotiation, SXP, Connected To, Duration, SXP Domain
    - entry - Name = SW2, IP Address = 172.16.1.136 Status = On, Peer Role = LISTENER > 'Edit' icon
    - Work Centers tab > TrustSec > SXP: folders - SXP Devices, ALL SXP Mappings
      - entry: IP Address = 10.80.0.11/32, SGT = ISE_OPs (17/0011), Learned From = 192.1691.105, 192.168.01.136, Learned By = session, SXP Domain = default, PSNs Involved = ISE_02
      - entry: IP Address = 10.80.0.12/32, SGT = ISE_OPs (18/0011), Learned From = 192.1691.105, 192.168.01.136, Learned By = session, SXP Domain = default, PSNs Involved = ISE_02
      - entry: IP Address = 10.80.0.13/32, SGT = ISE_OPs (16/0011), Learned From = 192.1691.105, 192.168.01.136, Learned By = session, SXP Domain = default, PSNs Involved = ISE_02
    - Administration tab > System > Deployment: folders - Deployment, PAN Failover > Deployment
    - Deployment Nodes List > ISE-02 > End Node: subtabs - General Settings, Profiling Configuration > General Settings
      - End Node: Hostname = ISE-02, FQDN = ISE-02.ogit.com, Node Type = Identity Service Engine (ISE), Role = Primary, Policy Service = On, Enable SXP Service = On, pxGrid = On > 'Save' button
  - verify commands

    ```text
    SW2# show ip device tracking all
    SW2# show cts roll-based sgt-map all
    SW# show role-based permissions
    ```


