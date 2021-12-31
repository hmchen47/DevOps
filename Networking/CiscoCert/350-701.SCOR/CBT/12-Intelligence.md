# 12. Security Intelligence

Trainer: Keith Barker


## Introduction to Security Intelligence

- Learn goals
  - security intelligence
  - Talos
  - authoring, sharing and using security intelligence


## Security Intelligence Overview

- Security intelligence
  - Talos: an organization in Cisco who gathers malware info from the Internet
  - features
    - collecting data
    - authorizing
    - sharing
    - using/consuming info
  - appliances using and feedback to Talos
    - Email Security Appliance (ESA): connected to Switches
    - Web Security Appliance (WSA): connected to switches
    - Firewall / IPS: Next Generation Firewall (NGFW) / FirePower
    - Advanced Malware Protection (AMP): all devices
    - ThreatGrid

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 33vw;"
      onclick= "window.open('page')"
      src    = "img/12-secintelligence.png"
      alt    = "Security Intelligence"
      title  = "Security Intelligence"
    />
  </figure>



## Cisco Talos Overview

- Talos overview
  - [Talos website](https://talosintelligence.com/)
  - homepage legend
    - blue: legitimated email
    - orange: spam
    - green: malware
  - important tabs: Software, Vulnerability Information, Reputation Center, Library, Incident Response
  - Software:
    - Snort: open source intrustion prevention system capable of real-time traffic analysis and packet logging
    - ClamAV: open source antivirus engine for detection trojans, virus, malware, & other malicious threats
    - etc.
  - Vulnerability Information: Vulnerability Reports, Microsoft Advisories
  - Reputation Center: IP & Domain Reputation, Talos File Reputation, Reputation Support, AMP Threat Naming Conventions, AWBO Exercises, Intelligence Categories
  - Library: publications, presentations
  - Incident Response: contract or support agreements


## Talos Vulnerability Information

- Talos vulnerabilities reports
  - tabs: zero-day reports, disclosed vulnerability reports
  - disclosed vulnerability reports: subtabs - report id, title, report date, cve number, cvss score
  - CVSS score:
    - [Common Vulnerability Scoring System Calculator](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)
    - Basic score metrics: exploitability metrics, impact metrics
      - exploitability metrics:
        - attack vector (AV): network, adjacent network, local , physical
        - attack complexity (AC): low, high
        - privileges required (PR): none, low, high
        - user interaction (UI): none, required
        - scope (S): unchanged, changed
      - impact metrics
        - confidentiality impact (C): none. low, high
        - integrity impact (I): none. low. high
        - availability impact (A): none, low, high
  - CVE number
    - [Common Vulnerabilities and Exposures](https://cve.mitre.org/): a list of public known cybersecurity vulnerabilities
    - Talos report containing the number 


## Talos Reputation Center




## Security Intelligence Summary



