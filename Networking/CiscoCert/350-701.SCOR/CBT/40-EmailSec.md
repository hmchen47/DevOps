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
  - default entry - Policy Name = Default Policy, Anti-Spam = 'IronPort Anti-Spam, Positive: Delivery, Suspected: Delivery', Anti-Virus = 'Sophos, Encrypted = Deliver, Unscannable: Deliver, Virus Positive: Drop', Advanced Malware Protection = Greymail = Not Available, Content Filters = 'Sample-OutBound-Filter, HighSecEncrypt', Outbreak Filters = 'Retention Time: Virus: 1 day', DLP = 'PCI-DSS (Payment Card Industry), Canada PIPEDA (Personal Information), Contact Information (US)




## SPAM Filtering




## Email Anti-Virus




## DLP




## Encryption



