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




## ESA Outbound Mail Overview




## SPAM Filtering




## Email Anti-Virus




## DLP




## Encryption



