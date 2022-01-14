# 39. Cisco Web Security

Trainer: Keith Barker


## Introduction to Cisco Web Security

- Learning goals
  - web security appliance (WSA)
  - WSA integrating w/ AD
  - WSA features
    - identification profile
    - access and decryption policies
    - filtering
    - TLS decryption
    - digital certification management


## Web Security Appliance Overview

- Web security appliance overview
  - either physical or virtual machine
  - WSA as a proxy or just redirect to send web requests
  - proxy w/ many policies
    - subnets
    - AD user/group
    - port
    - URL filtering
    - apps
    - DLP
    - malware
  - web reputation based on Talos


## WSA and AD Integration

- Integrating WSA and AD
  - WSA: tabs - Reporting, Web Security Manager, Security Services, Network, System Administration
  - Network tab > Authentication
  - Authentication > Authentication Realms > 'Add Realms' button
  - Add Realm: sections - Authentication Realm, LDAP Authentication/Active Directory Authentication
    - Authentication Realm: Realm Name = ADServer, Authentication Server Type and Scheme(s) = Active Directory (Kerberos, NTLMSSP or Basic Authentication), Test Current Setting
    - Active Directory Authentication
      - Active Directory Server: Set Source Interface = On, Source Interface = Management, 192.168.1.100
      - Active Directory Account: Active Directory Domain = ogit.com, 'Join Domain' button > Computer Account Credentials: Username = administrator, password = `****`
      - Test Current Settings: 'Start Test' button > message displayed 
      - 'Submir' button > Authentication >'Commit Change' button on top right corner > Uncommitted Change: Comment (optional) = Just add ed AD to the Mix > 'Commit Changes' button


## WSA Identification Profiles

- Demo: WAS identity profile
  - assumption: web proxy set via either on local machine or WCCP/PBR redirect
  - Web Security Manager tab > Identification Profiles
  - Client / user Identification Profiles: fields - Order, Transaction Criteria, Authentication / Identification Decision, End-User Acknowledgement, Delete > 'Add Identification Profile...' button
  - Identification Profiles: Add Profile > sections - Client / User Identification Profile Settings, User Identification Method, Membership Definition
    - Client / User Identification Profile Settings: Enable Identification Profile = on, Name = OurProfileOne, Insert above = 1 (Global Profile)
    - User Identification Method: Identification and Authentication = Authenticate Users; Authentication Realm: Select a Realm or Sequence = ADServer, Select a Scheme = Use Basic (in production - Use Kerberos or NTLMSSP); Authentication Surrogates = IP Address
    - Membership Definition: Define Members by Protocol = HTTP/HTTPS
    - 'Submit' button > Identification Profiles: Warning - The policy group "OurProfileOne" was added
    - entry - Order = 1, Transaction Criteria = OurProfileOne, Authentication/Identification Decision = Realm: ADServer (Scheme: Basic), End-User Acknowledgement = (global profile)
    - 'Commit Changes' button > Uncommitted Changes: Comments (optional) = added identity profile > 'Commit Changes' button
  - verify w/ PC browser to open a alcohol website and a sign in page shown
  - verify on WSA: Reporting tab > URL Categories: URL Categories Matched > entry - URL Category = Alcohol, ...
  - not really block the alcohol web traffic but just ask for sign in to allow traffic went through


## WSA Access Policies

- Demo: WSA access policies
  - Web Security manager tab > Access Policies > Policies: fields - Order, Group, Protocols and User Agents, URL Filtering, Applications, Objects, Anti-Malware and Reputation
  - order of policies: to-down
  - default entry - Group = Global Policy, Protocols and User Agenets = No blocked items, URL Filtering = Monitor: 86, Applications = Monitor: 345, Objects = No blocked items, Anti-Malware and Reputation = 'Web Reputation: Enabled, Advanced Malware Protection: Enabled, Anti-Malware Scanning: Enabled' 
  - Policies > 'Add Policy' button
  - Access Policy: Add Group: sections - Policy Settings, Policy Member Definition
    - Policy Settings: Enable policy = On, Policy Name = NoDrinkForBob, Insert Above Policy = 1 (Global Policy)
    - Policy Member Definition: Identification Profiles and Users = Select One or More Identification Profiles, Identification Profile = OurProfileOne, Authorized Users and Groups = Select Groups and Users, Groups = No groups entered, Users = No users entered > 'No users entered' link > Authorized Users = bob > 'Done' > 'Submit' button
    - new entry - Order = 1, Group = NoDrinkForBob, Protocols and User Agents = URL Filtering = Applications = Objects = AntiMalware and Reputation = (global policy) > '(global policy)' link under URL Filtering
    - Access Policies: URL Filtering: NoDrinkFor Bob: sections Custom and External URL Category Filtering, Predefined URL Category Filtering
    - Predefined URL Category Filtering: fields - Category, Use Global Settings, Override Global Settings (Block, Monitor, Warn, Quota-Based, Time-Based)
    - modify: Access Policies: URL Filtering: NoDrinkFor Bob: entry - Category = Alcohol, Block = On > 'Submit' button
    - 'Commit Change' button on top-right corner > Uncommitted Changes: Comments = Sorry Bob > 'Commit Changes' button
  - Access Policies: Success - Your changes have been committed.
  - Verify w/ open Alcohol website using Bob and other user to sign in


## WSA Application Filtering

- Demo WSA application filtering
  - task: forbit Bob to browse facebook.com
  - Verify from PC for Google Translate -> OK
  - Web Security Manager tab > Access Policies > entry - Group = NoDrinkForBob, Application = (global policy) > 'NoDrinkForBob' link
    - Access Policy: NoDrinkForBob > Policy Settings: Policy Name = SorryBob > 'Submit' button
    - entry - Group = SorryBob, Application = (global policy) > 'NoDrinkForBob' link
    - Access Policies: Application Visibility and Control: SorryBob > sections - Edit Application Settings, Application Settings
    - Application Settings: entry - Applications = Internet Utilities - Google Translate = Used Global (Monitor) > 'Used Global (Monitor)' link
    - Set action for application Google Translate = Block > 'Apply' button > 'Submit' button
    - modified entry: Order = 1, Group = SorryBob, Protocols and User Agent = (global policy), URL FIltering = 'Block: 1, Monitor: 85', Application = 'Block: 1, Monitor: 344', Objects = Anti-Malware and Reputation = (global policy)
    - 'Commit Changes' button > Uncommitted Changes > 'Commit Changes' button
  - verify from PC for Google Translate w/ Bob account -> blocked
  - failed scenario:
    - payload was encrypted and application filtering not working
    - TLS decryption to deep inspect on the traffic


## WSA TLS Decryption Overview

- WSA TLS decryption overview
  - verify WSA setting: Google Translate blocked
    - Access Policies: Appplications Visibility and Control: SorryBob > Applications Settings
    - entry - Applications = Google Translate, Settings = Block
  - verify from PC
    - open Chrome in incognito mode w/ 'translate.google.com'
    - sign in: Username = bob, Password = `****`
    - Page shown 'his Page Cannot Be Displayed'
  - verify from PC w/ Google search engine
    - incognit mode open 'google.com' ans search for 'translate'
    - access Google Translate from searching result
    - Google Translate working
  - issue: WSA no idea about application layer so far, i.e., the payload of packets
  - solution: TLS decryption
    - 2 HTTPS sessions: 1) btw PC and WSA; 2) btw WSA and web server
    - WSA able to see the dst of original request and establish the 2nd HTTPS session w/ web server


## WSA Certificate Management




## WSA Decryption Policy




## WSA Additional Security Features



