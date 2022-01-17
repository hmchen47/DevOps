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


## Adding Network Devices to ISE




## Policy Set Overview




## Creating a Policy Set




## Authorization Policies




## Summary



