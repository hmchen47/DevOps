# 41. Cisco Umbrella

Trainer: Keith Barker


## Introduction to Cisco Umbrella

- Learning goals
  - Cisco Umbrella
  - policy
  - identity
  - digital certificates
  - VA


## Cisco Umbrella Overview

- Cisco Umbrella overview
  - security issues of DNS
    - bad/incorrect info
    - malicious web site
    - tunneling by attackers
  - Umbrella
    - Talos providing intelligence
    - a could solution
    - DNS as part of Umbrella service
    - DNS requests forwarding to Umbrella


## Umbrella Components

- Umbrella components
  - OpenDNS public DNS server: 208.67.222.222 & 208.67.220.220
  - Umbrella DNS service (licensed): filtering 17 categories of web sites
  - local DNS server
    - virtual appliance installed in DHCP server
    - internet DNS forwards to local DNS server
    - external DNS forwards to public DNS server
  - remove access
    - Umbrella client on PC
    - redirect to OpenDNS
    - enforce filtering

- Demo: Umbrella DNS service
  - verify PC

    ```text
    PC> ipconfig -all
    Windows Ip Configuration:
      <...truncated...>
    Ethernet adapter EEthernet0:
      <...truncated...>
      IPv4 Address      : 192.168.1.116(preferred)
      Subnet Mask       : 255.255.255.0
      Default Gateway   : 192.168.1.1
      DNS Servers       : 8.8.8.8
      <...truncated...>
    ```

  - verify connectivity w/ web browser
    - open 'www,google.com' -> OK
    - open 'cbtnuggets.com' -> OK
    - open 'internetbadguys.com' -> OK
  - config DNS server to OpenDNS
    - Control Panel > Network and Internet > Network and Sharing Center > Change adapter settings
    - Ethernet0 > right click on icon > Properties
    - Ethernet-0 Properties > Internet Protocol Version 4(TCP/IPv4) > Properties
    - Use the forwarding DNS server address: Preferred DNS server = 208.67.222.222, 208.67.220.220
  - verify w/ 'internetbadbuys.com' -> Blocked
  - open 'welcome.umbrella.com' -> indicating Umbrella service used


## Policy Overview

- Policy overview
  - analogy: shopping cart w/ many different items
  - possible components
    - destinations
    - content categories
    - apps
    - TLS decryption (optional)
    - security settings: malware sites
    - feedback (block page)
    - 3rd party features


## Policy Components

- Demo: create a customized policy on Umbrella
  - log on Umbrella
  - left panel folders - Overview, Deployment, Policies, Reporting, Investigate, Admin
  - Policy folder > Management > All Policies
  - Default Policy: Policy Name = Default Policy, Applied to All Identities, 2 Destination Listed Enforces, Security Setting Applied: Default Settting, Content Setting Applied: Default Settings, Filer Analysis Nor Enabled, Customer Block Page Applied, No Application Setting Applied
  - Policy folder > Management > Policy Components: Destination Lists, Content Categories, Application Settings, Security Settings, Block Page Appearance, Integration
  - Policy folder > Management > Policy Components > Destination Lists > 'Add' icon on top right corner
  - New Destination List: List Name = Our Custom Destination List; Destination in this list should be = Blocked, input field = www.acme.com > 'Add' button > 'Save' button
    - Destination Lists: new entry - Our Custom Destination List, Type = Blocked, Domains = 1, IPs = 0, URLs = 0
  - Policy folder > Management > Policy Components > Content Categories > 'Add' icon
    - Add New Content Setting: Seting Name = Our Custom Content Filtering; Copy From Existing = High; Categories to Block = Alcohol, Adware, Adult Themes, Chat, ... (inherited from High and modify from the setting) > 'Save' button
  - Policy folder > Management > Policy Components > Application Settings > 'Add' icon
    - Add New Application Setting: Give Your Setting a Name = Our Custom App Setting; Application to Control = Google Drive, IDrive, InCloudDrive, ... > 'Save' button
  - Policy folder > Management > Policy Components > Security Settings > 'Default Settings' link
    - Default Settings: Setting Name = Default Settings; checked items = Malware, Command and Control Callbacks, Phising Attacks > 'Add' icon
    - Setting Name = Our Custom Security Setting; checked items = Malware, Newly Seen Domains, Command and Control Callbacks, Phising Attacks, Dynamic DNS, Potentially Harmful Domains, DNS Tunneling VPN, Cryptomining > 'Save' button
    - new entry - Our Custom Security Setting, Setting Enabled = 8, Integrations = 0
  - Policy folder > Management > Policy Components > Block Page Appearance > 'Add' icon
    - Add New Block Page Appearance: Block Page Appearance Name = Custom Block Page; Blocked erequests should be treated: The Same = On, Show a Block page with a custom message = (*)Show on a block page with the default message | (type in whatever to show on blocked page) | Redirect users to this URL = (enter a URL); Allow blocked users to contact an admin from the block page = admin@ogit.com > 'Save' button



## Policy Creation




## Core Identities




## Umbrella CA Certificates




## Reporting and Investigation




## Umbrella VA




## Umbrella Summary



