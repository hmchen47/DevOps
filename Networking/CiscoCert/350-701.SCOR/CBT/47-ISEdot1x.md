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
  - add new users from external server: Work Centers tab > Network Access > External Identity Sources: folders - Certificate AuthenticationProfile, Activity Directory, LDAP, ODBC, RADIUS Token, RSA SecureID, SMAL Id Providers, Social Login
    - Active Directory > 'Add' icon: add AD server to import users


## Configure ISE to use AD




## Adding Network Devices to ISE




## Policy Set Overview




## Creating a Policy Set




## Authorization Policies




## Summary



