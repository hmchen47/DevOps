# Endpoint Security


## 43. Explain Various Types of Endpoint Defenses


### Anti-Virus and Anti-Malware

- Anti-virus & Anti-Malware overview
  - used to be different but getting merged
  - EPP
    - point-in-time
    - comapring hash value: patterns
    - scanning signature: creator, date, etc.
    - performing actions
  - actions: quarantine, delete, remediate
  - anti-malware
    - generic term for bad software not to enter computers
    - including anti-virus (self-duplicated)

- [Point-in-time](https://imaginenext.ingrammicro.com/security/comparison-point-in-time-vs-retrospective-security)
  - security measures serve as gatekeepers to a network
  - a piece of code passes certain tests $\implies$ granted access
  - technologies
    - signatures
    - sandboxing
    - fuzzy fingerprinting
    - machine learning

### Indicators of Compromise (IoC)

- Indicators of Compromise (IoC)
  - pieces of forensic data, such as data found in system log entries or files, that identify potentially malicious activity on a system or network
  - components
    - destination of network traffic, e.g., North Korea? Russia?
    - volume of outbound traffic,e.g., SFTP or email data from 100MB to 10GB
    - run as admin/sudo
    - SQL injection:
      - disk I/O w/ read volume or SQL monitoring
      - web server log


### Retrospective Analysis

- Retrospective security overview
  - part of EDR
  - a protection system that covers the entire attack continuum
  - before an attack happens and includes continuous analysis and advanced analytics during and after the event
  - able to view any point in the past
  - tools: retrospection, attack chain correlation, behavioral indications of compromise (IOCs), trajectory and breach hunting
  - able to monitoring the environmental changes


### Dynamic File Analysis

- Dynamic file analysis overview
  - able to scan files w/o being detected
  - polymorphic file: changing nature of file to pass EPP. e.g., file extention
  - EDR able to detect the changes and send to AMP on cloud
  - EPP then downloading the changes to detect the incoming files




## 44. Endpoint Security


### Why Endpoint Protection is Critical

- Endpoint protection overview
  - people prerequisite: training for social engineering, screen locking, etc.
  - network prerequisite: WSA, ESA, Umbrella, NGFW/IPS, Application Visibility & Control
  - purpose
    - improving security
    - compliance
    - risk management strategy
  - solution: AMP & AnyConnect
    - update periodically
    - limited right for access
    - posture: machine to meet the minimal requirements
      - OS-build
      - AV/AM updated to a certain date
      - registry, file, location, etc.
    - agent: permant or temporary
  - AnyConnect w/ ISE for identities


### The Value of Mobile Device Management

- Mobile device management (MDM)
  - devices: laptops w/ WiFi, mobile phones
  - locations: local or remote
  - on-board: brining on a mobile device into mobile device management system
  - inventory: the devices in MDM system
  - advantages
    - application protection: allowing to run on devices
    - data protection: enforcing encryption
    - malware/virus protection
    - identity management
    - provisioning: automatic and routine
    - templates: consistent policies
  - [MDM Solutions](https://www.trustradius.com/mobile-device-management-mdm) (some popular ones)
    - Microsoft Endpoint Manager (Microsoft Intune + SCCM)
    - Workspace ONE Unified Endpoint Management (UEM) Powered by AirWatch
    - IBM MaaS360 with Watson
    - Cisco Meraki SM


### Using Multi-Factor Authentication

- Multi-factor authentication (MFA) overview
  - authentication methods
    - password
    - 802.1x
      - wireless mostly
      - supplicant: AnyConnect
      - authenticator: switch or MLC
      - authentication server: AAA, Radius, ISE
    - local/central web authentication: redirect to server or ISE to login 
  - factors - categories of authentication
    - knowledge: user knows, e.g., password, SIN, security questions
    - possession: user has, e.g., token generator
    - inherence: user is/does, e.g., biometrics, fingerprint, iris, face
  - MFA: authenticating user from 2 of 3 factors


### Posture Assessment for Endpoint Security

- Posture assessment overview
  - the strength of the cybersecurity controls and protocols for predicting and preventing cyber threats
  - typical procedure for posturing
    - checking device posture before allowing fully access network, such as minimum anti-virus and os updates or patch
    - redirect to a quarantine page if not compliant
    - remediate the incompliant items to gain the full access
  - components
    - posture agent: a piece of software on endpoint devides to connect to the server
    - posture server: ISE


- Demo: config posture assessment on ISE
  - Work Centers tab > Posture: subtabs - Overview, Network Devices, Client Provisioning, Policy Elements, Posture Policy, Policy Sets, Troubleshoot, Reports, Settings
  - Overview subtab: processes - 1) Prepare; 2) Define; 3) Go Live & Monitor
    - Prepare: Network Access Devices, Updates, Client Provisioning Resources(NAC or AnyConnect), Acceptable Use Policy (AUP), Settings
    - Define: Policy Elements (conditions, remediation, posture requirements), Posture Policy, Client Provisioning Portal
    - Go Live & Monitor: Auditing, Troubleshooting
  - Network Devices subtab: devices controlling access
  - Client Provisioning: folders - Client Provisioning Policy, Resources, Client Provisioning Portal
    - Client Provisioning Policy: list of default and customized provisioning policies
    - Resources: list of files for download and able to add new profiles w/ details
    - Client Provisioning Portal: default or customized portals
  - Policy Elements: flders - Conditions (Firewall Condition, Anti-Malware, Anti-Virus, File, Registry, etc.), Remediations (Anti-Malware, Anti-Virus, Ant-Spyware, Firewall)


### Patching Endpoints

- Patch management for endpoints
  - [Talos - Vulnerability Information](https://talosintelligence.com/vulnerability_info)
    - zero-day vulnerabilities
    - disclosed vulnerabilities
  - [Talos > Vulnerability Information > Microsoft Advisories](https://talosintelligence.com/ms_advisory_archive/ms-2022)
    - list of vulnerabilities
    - redirect to MSRC to review the impact and details
  - procedure for change management
    - test the update first to find negative impacts
    - communicate w/ end users to implement the update




## 45. Describe Controls for End Users' Network Access


### Endpoint Profiling

- Profiling endpoints overview
  - network profiling:
    - gathering basic info 
    - making assumptions
    - deciding access permission
  - access control w/ ISE
    - check MAC adddress w/ existing db when plugged in
      - pre-configured w/ Mac address bypass (MAB)
      - gathering device info and associated w/ existing profile if existed and then config the port, e.g., Cisco Phone w/ Voice VLAN
  

- Demo: ISE sandbox
  - [DevNet Sandbox](https://developer.cisco.com/sandbox.html)
  - reservation required
  - Identity Service Engine w/ MUD Lab
  - access ISE w/ browser
  - Work Centers tab > Profiler > Overview: procedures - 1) Prepare; 2) Define; 3) Go Live & Monitor
  - Work Centers tab > Profiler > Network Devices > entry - Name = Centos, Profile Name = Cisco ->
    - Services = Radius, TACACS, TrustSec, MAB, 802.1X, WebAuth
    - CoA = RFC, Port Bounce, Port Shutdown, Re-Auth, RFC Push (default CoA port: 1700, default DTLS CoA Port: 2083)
    - Native URL Redirect: Dynamic
  - Work Centers tab > Profiler > Policy Elements > Policy Conditions > Profiler Conditions > list of profiler for devices
  - Work Centers tab > Profiler > Profiling Policies: policies for devices


### Identity-Based Authentication

- Identity-based authentication overview
  - username and password: a almost must part of the authentication
  - using 802.1x to force users typing in their username and password
    - supplicant: endpoint devices
    - authenticator: switch or WLC
    - authentication server: identity data store - ISE, ACS, NAP, integrateing w/ AD
  - Remote access w/ VPN
  - BYOD: enterprise, guest
  - profiling


### Authenticating with AnyConnect

- AnyConnect authentication
  - a powerful agent w/ many modules
  - firewall
    - Firepower Threat Defence (FTD) w/ Firepower Management Center (FMC) - optional or ASA
    - pool of IP addresses
  - AnyConnect features
    - VPN: prompt to enter username and password
    - Network
    - Web Security
    - System Scan
    - Roaming Security
    - AMP Enabler
  - gear icon on bottom - settings and statistics of AnyConnect Secure Mobility Client


### Posture Assessment

- Demo: posture assessment w/ AnyConnect
  - download profile from server to check the compliance of posture
  - AnyConnect capable of checking
    - OS
    - AMP installed & installation
    - firewall
    - encryption
  - Web Security: leveraging Umbrella to identify category of web site accessed
  - System Scan: enforcing system scanning about config of firewall, AV, encryption
  - Roaming Security: content security w/ Umbrella
  - AMP enabler: installing AMP


### Cisco TrustSec and Security Group Tags (SGTs)

- Cisco TrustSec and Security Group Tags
  - DNA center
  - identify person than IP address and VLANs
  - control access resources from one to another based on identity
  - major component of SD-Access
  - TrustSec architecture
    - building a secure networks by establishing domains of trusted network devices
    - device authenticated by its peer
    - components
      - authenticated networking infrastructure
      - secure group-based access control
      - secure communication
  - Security Group Tag (SGT)
    - the security group number of the device in L2 frame
    - specify the privileges of a traffic source within a trusted network
    - secure group access automatically generated
    - classify users into groups, e.g., IT, HR, Engineering, Consultant, etc.
    - classify devices into groups, e.g. IT servers, HR servers, Printers, IoT devices, windows servers, etc.


### Change of Authorization (CoA)

- Change of authorization
  - detecting vulnerabilities occurred $\to$ change status of the network access and actions allowed
  - using profiling and authentication to stop spreading of malware
  - leveraging a feature of Radius protocol to change authorization
    - AMP for endpoint working w/ ISE to gain user authentication
    - able to access servers
    - AMP detected attacks and advised ISE
    - ISE using UDP:3799 CoA request to authenticator
    - authenticator becomes a dynamic authorization server according to CoA request
      - quarantine VLAN
      - shutdown port to disconnect
    - authorization returns CoA-Ack once change implemented, otherwise, CoA-NAK
  - similar procedure applied to remote access w/ VPN on firewall
    - once posture complied, supplicant info ISE to send CoA to authorize



## 46. 802.1X Fundamentals


### Network Authentication and Authorization

- 802.1X protocol
  - providing an authentication mechanism to devices wishing to attach to a LAN or WLAN
  - define the encapsulation of the Extensible Authentication Protocol (EAP) over IEEE 802.11
  - wired or wireless btw supplicant and authenticator
  - wireless AP wired connected to switch (WLC)
  - goal: authenticate user before attached to the network
  - authenticator:
    - a device request credentials from users
    - layer 2/3 switch and wireless LAN controller (WLC)
  - supplicant:
    - a piece of software (built-in or 3rd-party) interacting w/ authenticator
    - able to prompt to ask for username and password
  - authentication server:
    - identity server to validate identities
    - using Radius protocol
    - Radius server, AAA server, or ISE
  - once authenticated, able to authorize the user via downloadable ACL or TrustSec
    - specifying VLAN used
    - specifying port used
    - specifying user's security group
  - supplicant w/o 802.1x
    - MAC authn bypass (MAB): authn w/ MAC address
    - examples: IP camera, printer

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=150
        src   = "img/46-dot1x.png"
        alt   = "Network for 802.1X authentication and authorization"
        title = "Network for 802.1X authentication and authorization"
      >
    </a>
    <a href="https://en.wikipedia.org/wiki/IEEE_802.1X" ismap target="_blank">
      <img style="margin: 0.1em;" height=200
        src   = "https://upload.wikimedia.org/wikipedia/commons/1/1f/802.1X_wired_protocols.png"
        alt   = "EAP data is first encapsulated in EAPOL frames between the Supplicant and Authenticator, then re-encapsulated between the Authenticator and the Authentication server using RADIUS or Diameter."
        title = "EAP data is first encapsulated in EAPOL frames between the Supplicant and Authenticator, then re-encapsulated between the Authenticator and the Authentication server using RADIUS or Diameter."
      >
    </a>
  </div>



### Options for Authentication

- EAP options
  - extensible authentication protocol (EAP)
  - Windows wireless network adapter > Properties
  - Authentication tab
    - Enable IEEE 802.1X authentication = On
    - Authentication method: PEAP, EAP-SIM, EAP-TTLS, EAP-AKA, EAP-AKA*, EAP-TEAP
  - EAP-TTLS (extensible authentication protocol - tunnel TLS): encrypted tunnel
  - PEAP (Protected EAP): developed by MS, Cisco and RSA


- Demo: config 802.1X
  - supplicant: Windows PEAP
    - wireless network adapter > Properties
    - settings: (*)Secured password (EAP-MSCHAPv2), smart card or other certificate
    - credential Advanced settings: Specify authentication mode = User Authentication > 'Replace credentials' button > Replace credentials: username & password > 'OK' buttone
    - verify: enable the network adapter to check the connection
  - authenticator: Cisco Sw 3750x

    ```text
    SW# show authentication sessions
    Interface    MAC Address     Method   Domain   Status   Fg    Session ID
    Gi2/0/2      8cae.4cfd.b87f  dot1x    DATA     Auth           0A1E0001000000150066BFA0
    Session count = 1

    SW# show authentication sessions mac 8cae.4cfd.b87f details
          Interface: GigabitEthernet2/0/2
        MAC Address: 8cae.4cfd.b87f
       IPv6 Address: unknown
       IPv4 Address: 10.80.0.12
          User-Name: bob
             Status: Authorized
             Donaim: DATA
      <...truncated...>
    Server policies:
         vlan group: vlan: 80
          SGT value: 17
    Method status list:
          Method    State
          dot1x     Authc Success
    ```

  - verify logs on ISE
    - log in ISE w/ username and password
    - OPeration tab > RADIUS > Live Logs
    - entry - Identity = bob, Endpoint ID = 8C:AE:4C:FD:B8:7F > icon in Details field
    - Report for bob authentication
      - Overview: Event = 5200 Authentication Succeeded, Username = bob
      - Authentication Details: Policy Server = ISE-02, Event = 5200 Authentication Succeeded, Username = bob
      - Steps: Extracted EAP-Response/Identity; Prepared EAP-Request proposing EAP-TLS with challenge, ...
  - ISE settings
    - Work Centers tab > Network Access > Policy Elements > Results > Allowed Protocols subfolder > Allowed Protocols Services > entry - Service Name  = Default Network Access > 'Default Network Access' link
    - Allowed Protocols: 
      - Authentication Bypass: Process Host Lookup = On
      - Authentication Protocols: PAP/ASCII, EAP-MD5, EAP-TLS, PEAP, EAP-FAST, EAP-TTLS, TEAP; LEAP (cisco, light-weight)
      - PEAP > Inner Methods: EAP-MS-CHAPv2, EAP-GTC, EAP-TLS
      - EAP-FAST > Inner Methods: EAP-MS-CHAPv2, EAP-GTC, EAP-TLS, PACs
      - EAP-TTLS > Inner Methods: PAP/ASCII, CHAP. MS-CHAPv1, MS-CHAPv2, EAP-MD5, EAP-MS-CHAPv2


### Options after Authentication

- Authorization options
  - Radius response w/ successful authn
  - possible components in response
    - VLAN: best practice to used a void VLAN before assigning
    - dACL (downloadbale): filtering or permitting certain types of traffic
    - SGT: TrustSec enabled to control the access


- Demo: authorization options on ISE
  - Work Centers tab > Network Access > Policy Elements > Results > Authorization Policies subfolder
  - Standard Authorization Profiles: fields - Name, Profile 
  - create new one: 'Add' icon > Authorization Profile: Name = abc
    - Common Task: DACL Name, Ipv6 DACL Name, ACL (Filter-ID), ACL IPv6 (Filter-ID), Security Group, VLAN, Voice Domain Permission, Web Redirection (CWA, MDM, NSP, CPP), Auto Smart Port, Assess Vulnerabilities, Reauthentication, MacSec Policy, Interface Template, Web Authentication (Local Web Auth), Airspace ACL Name, Airspace Ipv6 ACL Name, ASA VPN, AVC Profile Name, UPN Lookup
    - Advanced Attribute Settings: many options based on company and products




## 47. Configure ISE for 802.1X


### Identity Stores

- Demo: identity store on ISE
  - add new user: Work Centers tab > Network Access > Indentities: folders - Endpoints, Network Access Uses, Identity Source Sequences
    - Network Access Users: fields - Status, Name
    - entry - Name = bob, Status = Enabled > 'Remove' icon
    - 'Add' icon > Network Access Users List > New Network Access User: Name = Sample-Local-User, Status = Enabled; Passwords: Login Password = `****` > 'Submit' button
    - new entry - Name = Sample-Local-User, Status = Enabled
  - add new users from external server: Work Centers tab > Network Access > External Identity Sources (Ext Id Sources): folders - Certificate AuthenticationProfile, Activity Directory, LDAP, ODBC, RADIUS Token, RSA SecureID, SMAL Id Providers, Social Login


### Configure ISE to use AD

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


### Adding Network Devices to ISE

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



### Policy Set Overview

- Policy set overview
  - topology
    - switch as authenticator
    - client as supplicant
    - ISE as authentication server
  - switch request sent to ISe regarding to client's connection
  - two policies involved once request received on authn server
    - authentication: the resources able to access
    - authorization: fully or partially access resources

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 400px;"
      onclick= "window.open('page')"
      src    = "img/47-dot1xnet.png"
      alt    = "Example network for 802.1X authentication"
      title  = "Example network for 802.1X authentication"
    />
  </figure>


- Demo: config policies on ISE
  - Policy tab: subtabs - Policy Sets, Posture, Policy Elements (Dictionaries, Conditions, Results), Profiling, Client Provisioning
  - Policy Sets: fields - Status, Policy Set Name, Conditions, Allowed Protocols / Server Sequence, Hits, Actions, View
    - alternatives: Work Centers tab > TrustSec > Policy Sets, Work Centers tab > Network Access > Policy Sets, Work Centers tab > Guest Access > Policy Sets, Work Centers tab > BYOD > Policy Sets, or Work Centers tab > Posture > Policy Sets
    - entry - Name = Default policy set, Conditions = (empty), Allowed Protocols / Server Sequence = Default Network Access *, Hits = 15, Actions = gear icon, View = right arrow (`>`) icon
      - Conditions = (empty): wide open, not specific to any groups
      - Allowed Protocols / Server Sequence = Default Network Access *: all EAP methods enabled
      - `>` icon: viewing details
        - fields - Status, Rule Name, Conditins, Use, Hits, Actions (gear icon)
        - entries - Authentication Policy (3), Authorization Policy - Local Exceptions, Authorization Policy - Global Expectations, Authorization Policy (12)
      - Authentication Policy (3): Rule Name = Dot1X, MAB , Default (top-down order)
        - Dot1X: Conditions = Wired_802.1X OR Wireless_802.1X, Use = ALL_User_ID_Store
        - MAB: Conditions = Wired_MAB OR Wireless_MAB, Use = ALL_User_ID_Store
        - Default: Conditions = (empty), Use = ALL_User_ID_Store
      - Authorization Policy (12): Wireless Black List Default, Profiled Cisco IP Phones, Profile Non Cisco Phones, Unknown_Compliance_Redirect, ..., Base_Authenticated_Access, Default (top-down order)
        - not configured items just using 'Base_Authenticated_Access'
  - two main components in policy sets
    - authentication policy
    - authorization ploicy


- Demo: verify policy sets on ISE
  - client on windows
    - Network adapter > disable and enable again > Status = Authentication Failed > Properties
    - Ethernet 2 Properties > Authentication tab: Network authentication method = PEAP
      - 'Settings' button > Protected EAP Properties: Verify the server's security by validating the certificate = On, Trusted Root Certification Authorities = ISE-02.ogit.com; Select Authentication Method = EAP-MSCHAPv2 > 'OK' button
      - 'Advanced Settings' button > Specify authentication mode = User Authentication > 'Save credentials' button > Windows Security: username = bob & passoword = `****` > 'Ok' button
    - Network adapter > Status = Unidentified network
  - verify on ISE
    - Operations tab > RADIUS > Live Logs > entry - Identity = bob > 'detail' icon
      - Overview: Authentication Policy = Default >> Dot1X, Authorization Policy = Default > Basic_Authenticated_Access
    - Policy tab > Policy Sets > entry - Policy Set Name = Defult > '>' icon on view
      - Authentication Policy: entry - Rule Name = Dot1X
      - Authorization Policy: entry - Rule Name = Basic_Authenticated_Access
    - log each single events: Work Centers tab > Network Access > Settings > Protocol folder > RADIUS > Suppression & Report tab: Suppress Repeated Failed Clients = Supress repeated successful authentications = Off


### Creating a Policy Set

- Plan for authentication policy
  - site 1
  - switch
  - use AD


- Demo: config a new policy set on ISE
  - verify network devices
    - WorkCenters > Network Resources > Network Devices > entry - Name = switch1 > 'switch1' link
      - Network Devices: Name = switch1, Location = site 1, Device Type = switch
    - WorkCenters > Network Access > Active Directory - Our-DC
      - Groups tab: 4 entries - ogit.com/ISE-Admins, ogit.com/ISE-Operations, ogit.com/Users/Domain Admins, ogit.com/Users/Domain Users
  - create a policy
    - Policy tab > Policy Sets > '+' icon
      - new entry - Rule Name = Our-Site1-Switch-Policy-Set > '+' icon under Conditions
      - Conditions Studio:
        - Select attribute for condition: Dictionary = DEVICE Location = All Locations#site 1 > 'New' button
        - Select attribute for condition: Dictionary = DEVICE Device Type = ALL Device Types#switch > 'AND' label for both > 'Use' button
      - new entry - Name = Our-Site1-Switch-Policy-Set, Conditions = DEVICE Location = ... AND DEVICE Device Type = ... > 'Save' button
      - '>' under view to review the details
    - Authentication Policy > '+' icon
      - new entry - Rule Name = Our-authn-dot1x > '+' icon under Conditions
      - Conditions Studio: drag Wired_801.1X from template > 'Use' button
      - new entry - Use = Our-DC
    - Authorization Policy  > '+' icon
      - new -entry - New Rule = If-You-Authenticated-good-enough > '+' icon under Conditions
      - Conditions Studio: drag Network_Access_Authentication_Passed > 'Use' button
      - new entry - Profiles = PermitAccess > 'Save' button


- Demo: verify new policy set
  - Wired Network Adapter > Disable * Enable again > Enabled
  - ISE log: Operations tab > RADIUS > Live Logs > top entry - Identity = bob, Status = 'Session' icon > 'detail' icon
    - Overview: Authentication Policy = Default>>Dot1X, Authorization Policy = Default>>Basic_Authenticated_Access, Authorization Result = permitAccess -> not using created policy set
  - verify the created policy set and retry
  - ISE log: Operations tab > RADIUS > Live Logs > top entry - Identity = bob, Status = 'Session' icon > 'detail' icon
    - Overview: Authentication Policy = Our-Site1-Switch-Policy-Set>>Our-authen-dot1x, Authorization Policy = Our-Site1-Switch-Policy-Set>>if-You-Authenticated-good-enough, Authorization Result = permitAccess -> as expected, last time action too quick and the log not refreshed



### Authorization Policies

- Demo: config authorization policies
  - Work Centers > Network Access > Policy Elements: folders - Conditions, Results
  - Results: subfolders - Allowed Protocols, Authorization Profiles, Downloadable ACL
  - create new DACL: Downloadable ACL > 'Add' icon 
    - Downloadable ACL: Name = NoICMP-Telnet; IP version = IPv4; DACL Content = 'deny icmp any any; deny tcp any any eq 23'
    - validate w/ 'Check DACL Syntax' button -> DACL is valid
    - 'Submit' button
  - Authorization Profiles > Standard Authorization Profiles > 'Add' icon
    - Authorization Profile: Name = ise-admins, Access Type = ACCESS_ACCEPT; Common Tasks: VLAN = On, Edit Tag ID/Name = 30 > 'Submit' button
    - Authorization Profile: Name = ISE-Operations, Access Type = ACCESS_ACCEPT; Common Tasks: DACL = NiICMP-Telnet, VLAN = On, Edit Tag ID/Name = 80 > 'Submit' button
    - Standard Authorization Profiles: 2 new entry - Name = ise-admins, Profile = Cisco; Name = ISE-Operations, Profile = Cisco
  - Policy tab > Policy Sets > entry - Policy Set Name = Our-Site1-Switch-Policy-Set > '>' icon under Vew
    - Authorization Policy > entry - Rule Name = if-You-Authenticated-good-enough > 'gear' icon under Actions > 'Delete' label
    - '+' icon > new entry - Rule Name = admins > '+' button under Conditions
    - Consitions Studio: Select attribute for condition > Dictionaries = Our-DC, Attribute = ExternalGroups > Our-DC ExternalGroups = ogit.com/ISE-Admins > 'Use' icon
    - new entry - Rule Name =  Admins, Conditions = Our-DC ExternalGroups Equals ogit.com/ISE-Admins, Results - Profiles = ise-admins
    - new entry - Rule Name = ISE-OPS, Conditions = Our-DC ExternalGroups Equals ogit.com/ISE-Operations, Results - Profiles = ISE-Operations
    - 'Save' button


- Demo: verify authorization policies
  - verify w/ bob on PC
    - Client > Network Adapter > Properties > Authentication tab > 'Advanced Settings' button > Replace Credentials: usernam e= bob, password = `****` > 'OK' button
    - Network adapter > Status = Unidentified network
    - ping from PC w/ 10.30.0.1 -> -> failed
  - verify switch

    ```text
    SW# show vlan brief
    VLAN Name           Status    Ports
    ---- -------------- --------- -----------------------------
    1    default        active    
    10   VLAN0010       active    
    20   VLAN0020       active
    30   VLAN0030       active
    80   VLAN0040       active    Fa0/1
    999  VLAN0999       active    Fa0/2, ..., Fa0/8
    <...truncated...>

    SW# show run int f0/1
    interface FastEthernet0/1
      switchport access vlan 999
      <...truncated...>

    SW# show access-lists
    Extended IP access list Auth-Default-ACL-OPEN
        10 permit ip any any (80 matches)
    Extended IP access list xACSACLx-IP-NOICMP-TELNET-5f152814 (per-user)
        10 deny icmp any any
        20 deny tcp any any eq telnet

    SW# show authentication sessions interface f0/1
                Interface:  FastEthernet0/1
              MAC Address:  5882.a899.5c81
               IP Address:  10.80.0.12
                User-Name:  bob
                   Status:  Authz Success
                   Domain:  DATA
          Security Policy:  Should Secure
          Security Status:  Unsecure
           Oper host mode:  multi-domain
         Oper control dir:  both
            Authorized By:  Authentication Server
              Vlan Policy:  80
                  ACS ACL:  xACSACLx-IP-NOICMP-TELNET-5f152814
          Session timeout:  N/A
             Idle timeout:  N/A
        Common Session ID:  C0A8...A84B
          Acct Session ID:  0x0000008E
                   Handle:  0x2F000064
        
    Runnable method list:
            Method    State
            dot1x     Authc Success
            mab       Not run
    ```

  - verify w/ Luis on PC
    - Client > Network Adapter > Properties > Authentication tab > 'Advanced Settings' button > Replace Credentials: usernam e= luis, password = `****` > 'OK' button
    - Network adapter > Status = Unidentified network
    - ping from PC w/ 10.30.0.1 -> succeed
  - verify switch

    ```text
    %LINEPROTO-5-UPDOWN: Line protocol on interface Vlan 80 change status to down
    %LINEPROTO-5-UPDOWN: Line protocol on interface Vlan 30 change status to up
    %AUTHMGR-5-SUCCESS: Authorization succeeded for client (5882.a899.5c81) on 
      Interface Fa0/1 AuditSessionID C0A8...A84B

    SW# show int status
    Port      Name      Status        VLan    Duplex  Speed  Type
    FA0/1               connected     30      a-full  a-100  10/100BaseT
    <...truncated...>
    ```




## 48. Configure a Switch for 802.1X


### Configure Global AAA Parameters

- Demo: config AAA on switch
  - `aaa authentication login default local`: use local user to authenticate, here `admin`
  - `address ipv4 192.168.1.105 auth-port 1812 acct-port 1813`: explicitly presents ports used
  - `automate-tester username testuser`: auto test periodically
  - `aaa server radius dynamic-author`: CoA
  - `dot1x system-auth-control`: allow to do 802.1z authentication
  - `ip device tracking`: tracking the alive
  
  ```text
  ! verify hardware & OS support
  SW# show version
  <...truncated...>
  Switch  Ports Model         SW Version    SW Image
  ------  ----- -----         ----------    ----------
  *    1  9     WS-C3560-8pc  15.0(2)SE11   C3560-IPSERVICESK9-M

  SW# show users
        Line    User    Host(s)   Idle      Location
  *  1  vty 0   admin   idle      00:00:00  192.168.1.151

  SW# show ssh
  Connection  Version Mode  Encryption  Hmac      State             Username
  0           2.0     IN    aes256-cbc  hmac-sha1 Session started   admin
  0           2.0     IN    aes256-cbc  hmac-sha1 Session started   admin

  SW# conf t
  SW(config)# username admin privi 15 secret Cisco!23

  ! config AAA
  SW(config)# aaa new-model
  SW(config)# aaa authentication login default local
  SW(config)# aaa authentication dot1x default group radius
  SW(config)# aaa authorization network default group radius
  SW(config)# aaa accounting dot1x default start-stop group radius

  ! config RADIUS server
  SW(config)# radius server Demo-ISE
  SW(config-radius-server)# address ipv4 192.168.1.105 auth-port 1812 acct-port 1813
  SW(config-radius-server)# key Cisco!23
  SW(config-radius-server)# automate-tester username testuser
  SW(config-radius-server)# exit

  ! group name for RADIUS servers
  SW(config)# aaa group server radius Demo-Group
  SW(config-sg-radius)# server name Demo-ISE
  SW(config-sg-radius)# exit
  ```

  ```text
  ! retrial limit
  SW(config)# radius-server dead-criteria time 3 tries 3
  SW(config)# radius-server deadtime 15
  SW(config)# aaa server radius dynamic-author
  SW(config-local-da-radius)# client 192.168.1.133
  SW(config-local-da-radius)# server-key Cisco!23
  SW(config-local-da-radius)# exit

  ! allow to send vendor specific attribute
  SW(config)# ip radius source-interface g0/1
  SW(config)# radius-server vsa send authentication
  SW(config)# radius-server vsa send accounting

  ! allow tracking and 802.1x authn
  SW(config)# dot1x system-auth-control
  SW(config)# ip device tracking
  SW(config)# end

  SW# wr
  ```


### Port Configuration

- Demo: config port for 802.1X
  - `authentication host-mode [single-host | multi-auth | multi-domain | multi-host]`:
    - config interface switchport 802.1x host mode
    - `single-host`: default mode, allowing a single host to to be authenticated
    - `multi-auth`: multiple devices allowed to independently authenticate through the same port
    - `multi-domain`: allowing one host fro the data domain and one from voice domain, i.e., IP phone
    - `multi-host`: the first device to authenticate will open the port and all other devices able to use the port
  - `authentication violation [protect | replace | restrict | shutdown]`
    - `protect`: drop packets w/o syslog
    - `replace`: remove the current session and initiate authentication w/ the new host
    - `restrict`: generating syslog
    - `shutdown`: disable the port
  - `authentication open`: a fallback solution in lab env to allow traffic if failed
  - `dot1x pae authenticator`: enable 802.1x authentication on the port w/ default parameters
  - `authentication port-control auto`:
    - unauthorized state until authenticated w/ authentication server
    - authorized after authentication

    ```text
    SW# conf t
    SW(config)# vlan 10,20,30,80,999

    ! config almost all interfaces
    SW(config-vlan)# int range f0/1-8
    SW(config-if-range)# switchport host
    SW(config-if-range)# switchport access vlan 999

    ! authentication config
    SW(config-if-range)# authentication priority dot1x mab
    SW(config-if-range)# authentication order dot1x mab
    SW(config-if-range)# authentication event fail action next-method
    SW(config-if-range)# authentication event server dead action authorize vlan 10
    SW(config-if-range)# authentication event server alive action reinitialize
    SW(config-if-range)# authentication host-mode multi-domain
    SW(config-if-range)# authentication violation restrict
    SW(config-if-range)# authentication open
    ```

    ```text
    ! MAB config
    SW(config-if-range)# mab
    SW(config-if-range)# dot1x pae authenticator
    SW(config-if-range)# dot1x timeout tx-period 5
    SW(config-if-range)# authentication port-control auto
    SW(config-if-range)# end

    SW# wr
    SW# show int status
    Port      Name      Status        VLan    Duplex  Speed  Type
    Fa0/1               connected     999     a-full   auto  10/100BaseTX
    Fa0/2               notconnected  999       auto   auto  10/100BaseTX
    Fa0/3               notconnected  999       auto   auto  10/100BaseTX
    <...truncated...>

    %AUTHMGR-5-START: Starting 'dot1x' for client ...
    %DOT1X-5-FAIL: Authentication failed for client ...
    %AUTHMGR-7-RESULT: Authentication result 'no-response' from 'dot1x' ...
    %AUTHMGR-7-FAILOVER: Failing over from 'dot1x' for client ...
    %AUTHMGR-5-START: Starting 'mab' for client ...
    %AUTHMGR-7-RESULT: Authentication result 'no-response' from 'mab' ...
    %AUTHMGR-7-FAILOVER: Failing over from 'mab' for client ...
    %AUTHMGR-7-NOMOREMETHODS: Exhausted all authentication methods for client ...
    ```



### Testing and Verifying

- Demo: verify 802.1X config
  - change settings on PC
    - Network adaptor > Properties > Authentication tab: Enable IEEE 802.1X authentication = Off > 'Ok' button
    - `authentication open` allowing the access though still authentication failed
      - a great way for stage testing
      - remove before put into production
  - verify on SW

    ```text
    SW# authentication session interface f0/1
                Interface:  FastEthernet0/1
              MAC Address:  5882.a899.5c81
               IP Address:  10.80.0.12
                User-Name:  bob
                   Status:  Authz Failed
    <...truncated...>

    SW# show int status
    Port      Name      Status        VLan    Duplex  Speed  Type
    Fa0/1               connected     999     a-full   auto  10/100BaseTX
    <...truncated...>
    ! still in vlan 999
    ```

  - modify the username and password
    - Network adaptor > Properties > Authentication tab: Enable IEEE 802.1X authentication = On
    - 'Advanced Settings' button > 802.1X settings > 'Save credentials' button
    - Save Credentials: username = b0b, password = `****` > 'Ok' button
  - verify msgs on SW

    ```text
    %AUTHMGR-5-START: Starting 'dot1x' for client ...
    %DOT1X-5-SUCCESS: Authentication successful for client ...
    %AUTHMGR-7-RESULT: Authentication result 'success' from 'dot1x' ...
    %AUTHMGR-5-VLANASSIGN: VLAN 80 to Interface Fa0/1 ...
    %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan80,change state to up
    %AUTHMGR-5-SUCCESS: Authorizarion succeeded for client ...
    
    SW# authentication session interface f0/1
                Interface:  FastEthernet0/1
              MAC Address:  5882.a899.5c81
               IP Address:  10.80.0.10
                User-Name:  bob
                   Status:  Authz Success
                    <...truncated...>
                  ACS ACL:  xACSACLx-IP-NOICMP-TELNET-5f152814
                    <..truncated...>
    Runnable method list:
            Method    State
            dot1x     Authc Success
            mab       Failed over

    SW# show access-list
    Extended IP access list AUth-Default-ACL-OPEN
        10 permit ip any any (77 matches)
    Extended IP access list xACSACLx-IP-NOICMP-TELNET-5f152814 (per-user)
        10 deny icmp any any
        20 deny tcp any any eq telnet

    SW# show vlan brief
    VLAN Name           Status    Ports
    ---- -------------- --------- -----------------------------
    1    default        active    
    10   VLAN0010       active    
    20   VLAN0020       active
    30   VLAN0030       active
    80   VLAN0040       active    Fa0/1
    999  VLAN0999       active    Fa0/2, ..., Fa0/8
    <...truncated...>

    SW# show int status
    Port      Name      Status        VLan    Duplex  Speed  Type
    Fa0/1               connected     80      a-full   auto  10/100BaseTX
    <...truncated...>
    ```

  - verify RADIUS log on ISE
    - Operations tab > RADIUS > Live Logs
    - the 1st entry - Identity = bob, Status = Session > 'Detail' icon
    - Overview: Username = bob, Authentication Policy = Our-Site1-Switch-Policy-Set>>Our-auth-dot1x, Authorization Policy = Our-Site1-Switch-Policy-Set>>ISE-OPS, Authorization Result = ISE-Operations





