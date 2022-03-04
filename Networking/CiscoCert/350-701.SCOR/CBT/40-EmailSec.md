# 40. Cisco Email Security

Trainer: Keith Barker



## Introduction to Cisco Email Security

- Learing goals
  - Email security appliance (ESA)
  - incoming mail security
  - outgoing emil security
  - spam filtering
  - anti-virus
  - DLP
  - encryption emails


## Cisco Email Security Overview

- Email security overview
  - mail user agent (MUA), e.g., outlook
  - email server: mail transfer agent (MTA) to forward email to destination MTA
  - protocols used to download emails: IMAP / POP3
  - protocol used to send email: SMTP
    - MX: mail exchange record, including a list of destination mail server domain anmes
    - A: record of IP address resolving for mail server
  - ESA (email security appliance)
    - a middle-of-the-man security device
    - as an email server from outside world
    - relay emails to internal email server
    - both on-premise and cloud-based solution (CES)

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('page')"
      src    = "img/39-esadash.png"
      alt    = "Snapshot of ESA Dashboard"
      title  = "Snapshot of ESA Dashboard"
    />
  </figure>


## ESA Inbound Mail Overview

- Inbound email on ESA
  - components:
    - public listener: a logical component receiving inbound requests from untrusted world
    - private listener: intacting w/ email server
  - ESA checking
    - reputation of senders
    - host access table (HAT)
  - incorporating w/ Talos
    - having real-time reaction on malicious
    - recipient access table (RAT)


- Demo: ESA incoming mail
  - ESA: tabs - Monitor, Mail Policies, Security Services, Network System Adminstration
  - Incoming Mail Policies: sections - Find Policies, Policies; fields - Order, Policy Name, <span style="color: cyan;">Anti-Spam, Anti-Virus, Advanced Malware Protection, GrayMail, Content Filters, Outbreak Filters, Advanced Phising Protection</span>
  - default entry - Policy Name = Default Policy, Anti-Spam = 'IronPort Anti-Spam, Positive: Quarantine, Suspected: Quarantine', Anti-Virus = 'Sophos, Encrypted: Deliver, Unscannable: Deliver, Virus Positive: Drop', Advanced Malware Protection = Greymail = Advanced Phising Protection = Not Available, Content Filters = SampleFilter, Outbreak Filters = 'Retention Time: Virus: 1 day'


## Blocking Incoming Email

- Talos, [IP and Domain Reputation Center](https://talosintelligence.com/reputation_center)


- Demo: ESA 
  - Mail Policies tab > Host Access Table (HAT) > HAT Overview
  - HTA Overview > Sender Groups (listener: IncomingMail 10.1.1.1:25): fields - Order, Sender Groups, SenderBase Reputation Score, External Threat Feed Sources Applied, Mail Flow Policy
  - entries - Sender Group = RELAYLIST, WHITELIST, BLACKLIST, SUSPECTLIST, UNKNOWNLIST
  - SenderBase Reputation Score (SBRS): block = (-10, -3), throttle = (-3, -1), accept = (-1, 10)
  - 'BLACKLIST' link > Sender Group: BLACKLIST - IncomingMail 10.1.1.1:25 > sections - Send Group Settings, Find Senders, Send List: Display All Items in List
  - Send List: Display All Items in List > 'Add Sender...' button
  - Add Sender to BLACKLIST: Sender Type = IP Addresses | (*)Geolocation; Ad Country: Country Name = Aruba > 'Submit' button > 'Commit Changes' button on the top-right corner > 'Commit Changes' button
  - modify mail flow policy on block
    - Mail Policy Host Access Table (HAT) > HAT Overview > Mail Flow Policy = BLOCKED > 'BLOCKED' link
    - Mail Policy Host Access Table (HAT) > Mail Flow Policy > Policy Name = BLOCKED > 'BLOCKED' link
    - Network tab > Listeners > Listener Name = IncomingMail, HOST Access Table = HAT > 'HAT' link HAT Overview > Mail Flow Policy = BLOCKED > 'BLOCKED' link


## ESA Outbound Mail Overview

- Demo: config and verify outgong mail settings
  - Network tab > Listeners > Listeners: sections - Listerners. Global Settings
  - Listerners: fields - Listener Name, Interface, Port, Host Access Table, Recipient Table
  - Listeners > default entries - Listener Name = IncomingMail, Host Access Table = HAT, Recipient Access Table = RAT; Listener Name = OutgoingMail, Host Access Table = HAT, Recipient Access Table = N/A
  - 'OutgoingMail' link > Edit Listener: Name = PrivateListener > 'Submit' button > 'Commit Changes' button > 'Commit Changes' button
  - 'RAT' link > Recipient Access Table Overview > Overview for Listener: fields - Order, Recipient Address, Default Action
    - entries - Recipient Address = 'admin@ogit.com, keith@ogit.com', Default Action = Accept (Bypass LDAP); Recipient Address = ogit.com, Default aCtion = Accept; Recipient Name = All Other Recipients, Default Action = Reject
  - Listeners > Listener Name = PrivateListener, Host Access Table = HAT > 'HAT' link
  - HAT Overview > Sender Groups > Sender Group = RELAYLIST, MAil Flow Policy = RELAYED > 'RELAYLIST' link
  - Sender Group: REPLAYLIST - PrivateListener 10.2.2.1:25 > Sender List: Display All Items in List: Sender = 192.168.1.100 (email server)


- Demo: policies for outbound mails
  - Mail Policies tab > Outgoing Mail Policies: fields - Policy Name, <span style="color: cyan;">Anti-Spam, Anti-Virus, Advanced Malware Protection, Greymail, Content Filters, Outbreak Filters, DLP</span>
  - default entry - Policy Name = Default Policy, Anti-Spam = 'IronPort Anti-Spam, Positive: Delivery, Suspected: Delivery', Anti-Virus = 'Sophos, Encrypted = Deliver, Unscannable: Deliver, Virus Positive: Drop', Advanced Malware Protection = Greymail = Not Available, Content Filters = 'Sample-OutBound-Filter, HighSecEncrypt', Outbreak Filters = 'Retention Time: Virus: 1 day', DLP = 'PCI-DSS (Payment Card Industry Data Security Standard), Canada PIPEDA (Personal Information Protection and Electronic Act), Contact Information (US)'



## SPAM Filtering

- Demo: config Spam filtering on ESA
  - Security Services tab > Anti-Spam > IronPort Anti-Spam: sections - IronPort Anti-Spam Overview, Rule Updates
    - IronPort Anti-Spam Overview > 'Edit Global Settings...' button > Enable IronPort Anti-Spam Scanning = On > 'Submit' button
    - Rule Updates: entries
  - System Adminstration tab > Feature Keys: what keys on the system
  - Mail Policies > Email Security Policies > Incoming Mail Policies > entry - Policy Name = Default Policy, Anti-Spam = 'IronPort Anti-Spam, Positive: Quarantine, Suspected: Quarantine' > 'IronPort Anti-Spam, Positive: Quarantine, Suspected: Quarantine' link to modify existing policy
  - Mail Policies: Anti-Spam: sections - Anti-Spam Settings, Positive-Identified SPam Settings, Suspected Spam Settings
    - Anti-Spam Settings: Enable nti-Spam Scanning for this Policy = use IronPort Anti-Spam service
    - Positive-Identified SPam Settings: Apply this Action to Message = Deliver | (*)Drop | Spam Quatantine | Bounce
    - Suspected Spam Settings: Enable Suspected Spam Scanning = Yes, Apply This Action to Message = Span Quarantine
    - Spam Threshold: IronPort Anti-Spam = Use the Default Thresholds (default: suspected = 50~90, spam > 90)


## Email Anti-Virus

- Demo: comfig anti-virtual on ESA
  - Mail Policies tab > Incoming Mail Policies > Policies
  - default entry - Policy Name = Default Policy, Anti-Spam = 'IronPort Anti-Spam, Positive: Quarantine, Suspected: Quarantine', Anti-Virus = 'Sophos, Encrypted: Deliver, Unscannable: Deliver, Virus Positive: Drop', Advanced Malware Protection = Greymail = Advanced Phising Protection = Not Available, Content Filters = SampleFilter, Outbreak Filters = 'Retention Time: Virus: 1 day' > 'Sophos, Encrypted: Deliver, Unscannable: Deliver, Virus Positive: Drop' link (license required to enable)
  - license: System Administration tab > Feature Key Settings > Feature Keys: list of available license keys
  - add Anti-Virus license: Security Services > Anti-Virus (Sophos, McAfee) > 'Sophos > Sophos Anti-Virus: sections - Sophos Anti-Virus Overview, Current Sophos Anti-Virus files
    - Sophos Anti-Virus Overview: Anti-Virus Scanning by Sophos Anti-Virus = Enabled
    - Current Sophos Anti-Virus files > 'Update Now' button to check for updates
  - Mail Policies: Anti-Virus: sections - Anti-Virus Settings, Message Scanning, Required Messages, Encrypted Messages,  Unscannable Messages, Virus Infected Messags
    - Anti-Virus Settings: Enable Anti-Virus Scanning for This Policy = Yes, Use Sophos Anti-Virus = On
    - Message Scanning: Scan for Viruses only
    - 'Submit' button > 'Commit Changes' button > 'Commit Changes' button
  - default entry - Policy Name = Default Policy, Anti-Virus = 'Sophos, Encrypted: Drop, Unscannable: Deliver, Virus Positive: Drop'


## DLP

- Demo: config DLP on ESA
  - DLP for outgoing mails only
  - Mail Policies tab > Email Security Manager > Outgoing Mail Policies > Policies
  - default entry - Policy Name = Default Policy, Anti-Spam = 'IronPort Anti-Spam, Positive: Delivery, Suspected: Delivery', Anti-Virus = 'Sophos, Encrypted = Deliver, Unscannable: Deliver, Virus Positive: Drop', Advanced Malware Protection = Greymail = Not Available, Content Filters = 'Sample-OutBound-Filter, HighSecEncrypt', Outbreak Filters = 'Retention Time: Virus: 1 day', DLP = 'PCI-DSS (Payment Card Industry Data Security Standard), Canada PIPEDA (Personal Information Protection and Electronic Act), Contact Information (US)'
  - DLP Policies:
    - PCI-DSS (Payment Card Industry Data Security Standard) = Enable
    - Canada PIPEDA (Personal Information Protection asnd Electronic Act) = Enable
    - Contact Information (US) = Enable
  - add new default DLP policy:
    - Mail Policies tab > Data Loss Prevention (DLP) > DLP Policy Manager > Active DLP Policies for Outgoing Mail: fields - Order, DLP Policy > 'Add DLP Policy...' button
    - DLP Policy Manager > Add DLP Policy from Template > Acceptable Use > Add Contact Information > 'Add' link
    - Policy: Contact Information > DLP Policy Name = Test DLP
    - Severity Settings: Critical Severity Incident = Default Action; High/Medium/Low Severity Incident = Inherit Action from Critical Severity Incident
    - 'Submit' button > 'Commit Changes' button > 'Commit Changes' button
  - Mail Policies tab > Email Security Manager > Outgoing Mail Policies > Policies > entry - Policy Name = Default Policy, DLP = 'PCI-DSS (Payment Card Industry Data Security Standard), Canada PIPEDA (Personal Information Protection asnd Electronic Act), Contact Information (US)' > 'PCI-DSS (Payment Card Industry Data Security Standard), Canada PIPEDA (Personal Information Protection and Electronic Act), Contact Information (US)' link
  - Mail Policies: DLP > DLP Policies > Test DLP = Enable > 'Submit' button > 'Commit Changes' button > 'Commit Change' button 


## Encryption

- Demo: email encryption on ESA
  - create a profile for encryption
    - Security Services tab > Cisco IronPort Email Encryption
    - Email Encryption Global Settings: Cisco IronPort Email Encryption = Enable (or 'Edit Settings' button to enable)
    - Email Encryption Profiles > 'Add Encryption Profile...' button
    - Add Encryption Envelope Profile: sections - Encryption Profile Settings, Key Server Settings, Envelope Settings, Notification Settings
      - Encryption Profile Settings: Profile Name = Test
      - Key Server Settings: Key Service Type = Cisco Registered Envelope Service
      - Envelope Settings: Envelope Message Security = High Security; Logo Link = No Link; Read Receipts = Enable Read Receipts
      - 'Submit' button
    - Email Encryption Profiles: new entry - Profile = Test, Key Service = Cisco Registered Envelope Service, Provision Status = Not provisioned > 'Commit Changes' button > 'Commit Changes' button
  - apply the creates profile to filter
    - Mail Policies tab > Outgoing Content Filters > Filters: fields - Order, Filter Name, Description | Rules | Policies
    - entry - Order = 2, Filter Name = HighSecEncrypt > 'HighSecEncrypt' link
    - Edit Outgoing Content Filter: sections - Content Filter Settings, Conditions, Actions
      - Content Filter Settings: Name = HighSecEncrypt
      - Confitions: Condition = Subject Header, Rule = 'subject == "\\[send secure]\\"' > 'Subject Header' link
      - Edit Condition > ATtachment Content: Contains text = supersecrete > 'Ok' button
      - Actions: Action = Encrypt on Delivery, Rule = 'encrypt-deferred("HighSecurity", "$subject", 0)'
  - apply the filter to policy
    - Mail Policies tab > Email Security Manager > Outgoing Content Filters > Policies > entry - Policy Name = Default Policy, Content Filters = 'Sample-OutBound-Filter, HighSecEncrypt' > 'Sample-OutBound-Filter, HighSecEncrypt' link


