# 29. Firepower Access Control Policies

Trainer: Keith Barker


## Access Control Policy Overview

- Access control policy definition
  - high level requirements specifying how access is managed and who may access information under what circumstances
  - enforced through a mechanism that translates a user's access request
  - NIST, [Access Control Policy and Implementation Guides](https://csrc.nist.gov/Projects/Access-Control-Policy-and-Implementation-Guides)
  - [access control policy](https://www.luc.edu/its/aboutits/itspoliciesguidelines/access_control_policy.shtml) of Loyola University Chicago


- Typical procedure to check new session of ingress traffic (in sequence)
  - 1\. pre-filter
  - 2\. L3/L4 ACL
  - 3\. security intelligence (SI) based on IP address
  - 4\. SSL policy (decryption)
  - 5\. SI based on URL/DNS
  - 6\. App (L7) filtering
  - 7\. file/malware analysis and IPS (access control policy applied)
  - 8\. forward traffic


- Cisco Secure Firewall Management Center (FMC):
  - an administrative service to manage Cisco security products running on multiple platforms
  - a.k.a. Firepower Management Center
  - providing extensive intelligence about the users, applications, devices, threats and vulnerabilities that exist in your network
  - using this information to analyze your network’s vulnerabilities
  - providing tailored recommendations regarding security policies to implement, plus prioritization of security events to investigate
  - the centralized event and policy manager for
    - Firewall Threat Defence (FTD) OS
    - ASA w/ FirePower SDervice
    - Secure IPS (Firepower Next-Gen IPS / NGIPS)
    - FirePOWER Threat Defence for ISR
    - Malware Defence (AMP)


- Demo: access control policy of FMC
  - FirePower > tabs - Overview, Analysis, Policies, Devices, Objects, AMP, Intelligence
  - Policies > subtabs - Access Control , network Discovery, Application Detectors, Correlation, Actions
  - Access Control subtab > Starter Policy: tabs - Rules, Security Intelligence, HTTP Response, Advanced
  - Starter Policy > Rules
    - top-down fashion
    - Pre-filter Policy = Default Prefilter Policy; SSL Policy = None; Identity Policy = None
    - Deafult Action: Access Control: Block All | Access Control: Trust All Traffic | Network Discovery Only (default) | Instrusion Prevention: Maximum Detection | Instrusion Prevention: Connectivity Over Security | Instrusion Prevention: Balanced Security and Connectivity | Instrusion Prevention: Security Over Connectivity
    - main categories - Mandatory - Starter Policy, Default - Starter Policy
    - Loggin icon: disabled
    - icons after fields - shield icon = intrusion policy; files icon = file policy
  - Starter Policy > Security Intelligence
    - sections - Available Objects (Networks, URLs), Available Zone, DNS Policy, Whitelist, Blacklist

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=140
        src   = "img/29-firepower.png"
        alt   = "Snapshot of FirePower: Starter Policy - Rule"
        title = "Snapshot of FirePower: Starter Policy - Rule"
      >
    </a>
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=140
        src   = "img/29-fpintelligence.png"
        alt   = "Snapshot of FirePower: Starter Policy - Security Intelligence"
        title = "Snapshot of FirePower: Starter Policy - Security Intelligence"
      >
    </a>
  </div>



## Access Control Policy Rule Actions Concepts

- Actions of access control policy rule
  - 4 options
    - allow: ready for further inspection
    - trust: no further analysis required, e.g., backup service, VoIP
    - monitor: logging, handy for testing or troubleshooting
    - block (options):
      - block w/ reset - TCP traffic w/ TCP reset
      - block w/ interactivity - interactive w/ customer web page
  - example: ICMP echo request (inside zone) to 8.8.8.8 (outside zone) w/ action = block
    - just drop packets
    - no further analysis required



## Access Control Policy Rule Actions Demonstration

- Demo: actions of access control policy rules w/ FMC
  - verify Linux reachability
    
    ```text
    Sbox# ifconfig
    eth0: flags-4163<UP,BROADCAST, RUNNING,MULTICAST> mtu 1500
      inet 10.1.0.103   netmask 255.255.255.0   broadcast 10.1.0.255
      <...truncated...>

    SBox# ping 8.8.8.8
    <...success...>

    SBox# ping www.cisco.com
    <...success...>
    ```

  - config policy on FMC
    - FirePower > Policies tab > Access Control subtab > field - Access Control Policy, Status, Last Modified
    - entry: Access Control Policy = Starter Policy > 'Edit' icon
    - Starter Policy > Rules tab > Mandatory - Starter Policy > 'Add Rule' link
    - Add Rule > Name = No Ping 8.8.8.8; Enable = On; Action = Allow; Insert = into Mandatory; tabs - Zones, Networks, VLAN Tags, Users, Applications, Ports, URLs, SGT/ISE Attributes, Inspection, Logging, Comments
      - Zones tab > Source Zones = inside_zone, Destination Zones = outside_zone
      - Networks tab > Source Networks = (empty), Destination Networks = Google_8.8.8.8; none existed $\implies$ 1+1 icond on Availabe Networks
      - Ports tab > Available Ports > '+' icon > New Port Objects: Name = ICMP_Request_IPv4; Protocol = ICMP; Type = 8 (Echo Request); Code = Any > 'Save' button
      - Ports tab > Selected Source Ports = (empty); Selected Destination Ports = ICMP_Request_IPv4; Action = Block; Logging tab -> Log at the Beginning  of Connection = On > 'Add' button
    - Mandatory procedure to make the policy effect: Starter Policy > <span style="color: cyan;">'Save' button</span> > <span style="color: cyan;">'Deploy' link</span> on top banner > Deploy Policies > FTD-1 = On > `Deploy` button
  - Verify w/ SBox

    ```text
    SBox# ping 8.8.8.8
    <...fail...>
    SBox# ping www.cisco.com
    <...success...>
    ```

  - verify w/ FMC
    - Anslysis tab > Connections subtab > Events > Connection Events: fields - Firest Pacjet, Last Packet, Action, Reason, Initiator IP, Responder IP, Responder Country, Ingress Security Zone, Egress Security Zone, Source Port / ICMP Type, Destination ICMP Code
    - entry: Initiator IP = 10.1.0.103, Action = Block, Responder IP = 8.8.8.8, Source Port / ICMP Type = 8 (Echo Request) / icmp
    - entries before the ICP request packet all allowed for DNS lookup


## URL Filtering

- URL filtering overview
  - probably company policy to block certain types of web sites
  - user signing agreement to agree banning these web sites
  - ACL to block these web sites


- Demo: blocking sports web site w/ FMC
  - verify w/ Kali Linus
    - open web browser to browse 'Top 15 Most Popular Sports Website'
    - click on the links to the websites to verify the connectivity
  - FMC > Overview tab > Dashboards subtab > Summary Dashboard: tabs - Network, Threats, Intrustion Events, Status, Geolocation, QoS > Network tab
    - Network tab: charts - Unique Application over Time, Top Web Applications Seen, Top Client Applications Seen
    - Top Web Applications Seen (in tod-down order): Yahoo!, Google, CBS, Akamai, ...
  - config policy to block sports web sites: FMC > Policies tab > Access Control subtab > Access Control Policy = Starter Policy > 'Edit' icon
    - Starter Policy > Rule tab > Mandatory - Starter Policy > entry - # = 1, Name = No Ping to 8.8.8.8 > right click - Insert new rule
    - Add Rule: Insert = below rule 1; Name = No Sports; Action = Block with reset; Enabled = on
      - Zones tab: Source Zones = inside_zone; Destination Zones = outside_zone
      - Network tab: Source Networks = IPv4-Private-10.0.0.0-8; Destination Networks = (empty)
      - URLs tab: Reputations = Any; Selected URLs = Sports (Any Reputation)
      - Logging tab: Log at Beginning of Connection = On
      - 'Add' button
    - entry: # = 2, Name = No Sports, Source Zones = inside_zone, Dest Zone = outside_zone
    - 'Save' button > 'Deploy' link on top banner > FTD-1 = On > 'Deploy' button
    - green circle icon to check the status of deployment
  - Verify w/ Kali Linux
    - browse sports web site: 'The connection was reset' message on page
    - browse other web sites: ok



## Malware and File Inspections

- Demo: creating malware policy w/ FMC
  - FMC > Policies tab > Access Control subtab > Malware & File > Empty by default > 'New File Policy' button
  - create policy:
    - New File Policy: Name = Malware-n-File_Policy > 'Save' button
    - Malware-n-File Policy > tabs - Rules, Advanced; fields - File Types, Application Protocol, Direction, Action > Rules tab > 'Add' Rule
    - View Rule: Application Protocol = Any; Direction of Transfer = Any; Action = Block Files; File Type Categories = PDF Files; <span style="color: cyan;">Selected File Categories and Types = Category: PDF files</span> > 'Save' button
  - add the policy into ACL
    - FMC > Policies tab > Access Control > Access Control subtab > Access Control Policy = Starter Policy > 'Edit' icon
    - Starter Policy > entries w/ 'Files' icon gray out (no File policy included)
      - either add the File policy to existing rules or create new
      - both entries: action = block
      - expect to allow the PDF files
    - entry # = 2 > right click > Insert new rules
    - Add rule: Insert = below value 2; Name = Looking for PDFs; Action = Allow
      - Networks tab: Source Networks = IPv4-Private-10.0.0.0-8
      - Inspection tab: Intrusion Policy = None; File Policy = Malware-n-File_Policy
      - Logging tab: Log at Beginning of Connection = On
      - 'Add' button
    - entry - # = 3, Name = Looking for PDFs, File icon = On > 'Save' button
  - verify the file policy before deploying
    - browse a PDF file and download it > success
  - deploy the policy: FMC > 'Deploy' link > Deploy Policies: FTD-1 = On > 'Deploy' button
  - verify the file policy:
    - clear cache from browser in Kali Linux
    - browse the PDF document again > 'The connection was reset' message shown (PDF file allowed only from IPv4-Private-10.0.0.0-8)
    - browse a PDF file w/ HTTPS > ok



## SSL/TLS Decryption

- Inspecting traffic w/ SSL/TLS descryption
  - policy blocking some L7 applications and/or web sites
  - encrypted payload and header probably not able to be inspected, in particular, HTTPS
  - solution:
    - making firewall as man-in-the-middle device to inspect the packets
    - two sessions requested: inside session and outside sessions
    - firewall resigning the packets
  - scenario for inbound traffic:
    - user in branch office accessing the corporate service
    - servers in corperate servers w/ private keys
    - user's computer using know public key
    - some traffic not allowed to decrypt, such as financial and mediacal info
  - decryption and encryption intensively resource consuming


- Demo: decryption SSL/TLS in FMC
  - assume that the certificate and key are ready for use
  - FMC > Policies tab > Access Control > SSL subtab > entry - SSL Policy > 'Edit' icon
  - create rule for SSL policy: SSL Policy: tabs - Rules, Trusted CA certificates, Undecryptable Actions
    - Rules tab: 'Add' Rule > Add Rule: Insert = into Category Standard Rules; Name = xxx
  - apply the rule into access control policy: Policy tab > Access Control > Access Control subtab
    - entry - Starter Policy > 'Edit' icon
    - Starter Policy > SSL Policy = None > 'None' link
    - SSL Policy to use for inspecting encrypted connections = SSL Policy > 'OK' button
    - 'Save' button > 'Deploy' link > Deploy 


## IPS Inspection

- Demo: adding IPS policy to access control
  - create intrusion policy
    - Policies tab > Access Control > Intrusion subtab > empty by default > 'Create Policy' button
    - Create Intrusion Policy: Name = Our-IPS-Policy; Drop when Inline = On; Base Policy = Balanced Security and Connectivity > 'Create and Edit Policy' button
    - Create Policy: Our-IPS-Policy > folders - Policy Information (Rules, Firepower Recommendations), Advanced Settings, Policy Layers > Policy Information
    - Policy Information: Name = Our-IPS-Policy > 'Commit Changes' button
    - entry - Intrusion Policy = Our-IPS-Policy, Drop wne Inline = Yes, Status = No access control policies use this policy 
  - apply intrusion policy to access control policy
    - Policies tab > Access Control > Access Control subtab > entry - Access Control Policy = Starter Policy > 'Edit' icon
    - Starter Policy > Mandatory - Starter Policy
      - 3 entries w/ greyout shield icons - no Intrustion policy applied
      - nay policy w/ action = Block resulting packet drop and w/o further investigation, i.e., # = 1 & 2 not applicable
      - entry - # = 3, Name = Looking for PDFs, the only entry applicable > 'Edit' icon
      - Editing Rule - Looking for PDFs > Inspection subtab: Intrusion Policy = Our-IPS-Policy > 'Save' button
      - 'Save' button > 'Deploy' link > Deploy Policies: FTD-1 = On > 'Deploy' button
    - alternative, Default Action = Intrusion Prevention: Our-IPS-Policy


