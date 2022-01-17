# 47. Configure ISE for 802.1X

Trainer: Keith Barker



## Introduction to Configuring ISE

- Learning goals
  - identity stores
  - integrateing w/ AD
  - network devices
  - policy sets
  - authz policies


## Identity Stores

- Demo: identity store on ISE
  - add new user: Work Centers tab > Network Access > Indentities: folders - Endpoints, Network Access Uses, Identity Source Sequences
    - Network Access Users: fields - Status, Name
    - entry - Name = bob, Status = Enabled > 'Remove' icon
    - 'Add' icon > Network Access Users List > New Network Access User: Name = Sample-Local-User, Status = Enabled; Passwords: Login Password = `****` > 'Submit' button
    - new entry - Name = Sample-Local-User, Status = Enabled
  - add new users from external server: Work Centers tab > Network Access > External Identity Sources (Ext Id Sources): folders - Certificate AuthenticationProfile, Activity Directory, LDAP, ODBC, RADIUS Token, RSA SecureID, SMAL Id Providers, Social Login


## Configure ISE to use AD

- Demo: integrating AD w/ ISE
  - Work Centers tab > Network Access > Ext Id Sources
  - Work Centers tab > Device Administration > Ext Id Sources
  - Active Directory > 'Add' icon: add AD server to import users
  - Connection tab: Join Point Name = Our-DC, Active Directory Domain = ogit.com > 'Sumbit' button > Would you like to join all ISE Nodes to this Active Directory Domain? > 'Yes' button
    - Join Domain: AD User Name = administrator, Password = `****`, Specify Organizational Unit = 'CN=COMPUTERS,DC=OGIT,DC=COM' = Disable (uncheck) > 'OK' button > Join Status: ISE Node = ISE-02.ogit.com, Node Status = Completed > 'Close' button
    - new entry - ISE Node = ISE-02.ogit.com, ISE Node Role = STANDALONE, Status = Operational, Domain Controller = DC.ogit.com, Site = Deafult-First-Site-Name
  - Groups tab > 'Add' icon
    - AD serever: Users - Bob, Luis; Groups - ISE-Admin (Luis), ISE-Operations (Bob)
    - Select Directory Groups: Domain = ogit.com > 'Retrieve Groups' button > Name = ogit.com/ISE-Admin, ogit.com/IS-Operations = On > 'Ok' button
    - 2 new entries - Name = ogit.vom/ISE-Admin, SID = S1-5-21-6813...4-1107; Name = ogit.com/ISE-Operations, SID = S1-5-21-6813...4-1108
    - Select Directory Groups: Domain = ogit.com, Name Filter = domain* > 'Retrieve Groups' > Name = ogit.com/Users/Domain Admins, ogit.com/Users/Domain Users = On > 'Ok' button
    - 2 new entries - Name = ogit.vom/Users/Domain Admins, SID = S1-5-21-6813...4-512; Name = ogit.com/Users/Domain Users, SID = S1-5-21-6813...4-513
    - 'Save' button


## Adding Network Devices to ISE

- Demo: add network device on ISE
  - Work Centers tab > Network Access > Network Resources: folders - Network Devices, Device Groups, Default Device, External RADIUS Servers, RADIUS Server Sequences, External MDM Servers
  - Network Devices: fields - Name, IP/Mask, Profile Name, Location, Type > 'Add' icon
  - Network Devices: Name = switch1, IP Address = 192.168.1.133; RADIUS Authentication Settings = On -> RADIUS UDP Settings: Protocol = RADIUS, Shared Secret = `****` (same as switch1) > 'Submit' button
    - new entry - Name = switch1, IP/Mask = 192.168.1.133. Profile Name = Cisco, Local = All Locations, Type = All Device Types
  - Device Groups > Network Device Group: fields - Name, No. of Network Devices > 3 entries > 'Add' icon
    - Add Group: Name = site 1, Parent Group = All Locations > 'Save' button
    - same prodcure to create switch and router w/ 'All Device TTypes' and 'site 2' w/ 'All Locations'
    - Name = All Device Types: 2 subentries - Name = switch, router
    - Name = All Locations: 2 subentries - Name = site1, site 2 
  - Network Devices: entry - Name = switch1 > Network Devices > network Device Group: Location = site 1, Device Type = switch
    - new entry - Name = switch1, IP/Mask = 192.168.1.133. Profile Name = Cisco, Local = site 1, Type = switch



## Policy Set Overview




## Creating a Policy Set




## Authorization Policies




## Summary



