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

- Talos reputation center
  - IP & Domain reputation
    - 'ihaveabadreputation.com': a website for testing purpose w/ web reputation = untrusted | poor, threat category = malicious sites
    - additional info: ip address, whois, email volume history, top network owners
  - file reputation
    - maintining a reputation disposition on billions of files
    - fed into AMP, FirePower, CalmAV, and open-source Snort
  - intelligence categories
    - subtabs - content categories, threat categories
    - content categories: used by Umbrella, FirePower, other services tied w/ Talos
    - threat categories

      <table id="threat-categories" data-toggle="table" data-search="true" data-pagination="true" data-page-list="[25, 50, 100, ALL]" data-page-size="25" data-mobile-responsive="true">
        <thead style=""><tr><th style="" data-field="category" tabindex="0"><div>
            <span style="font-size: 1.2em;">Category</span>
          </div></th><th style="" data-field="description" tabindex="0"><div>
            <span style="font-size: 1.2em;">Description</span>
          </div></th></tr></thead>
        <tbody><tr data-index="0"><td style="">
          <strong>Malware Sites</strong>
          </td><td style="">
            Websites that are known to contain, serve, or support malware in its delivery, propagation, or in carrying out its malicious intent.
          </td></tr><tr data-index="1"><td style="">
            <strong>Spyware and Adware</strong>
          </td><td style="">
            Sites that are known to contain, serve, or support Spyware and Adware activities.
          </td></tr><tr data-index="2"><td style="">
            <strong>Phishing</strong>
          </td><td style="">
            Phishing and other fraudulent sites that copy or mimic legitimate sites for the purposes of surreptitiously acquiring sensitive information, such as user names, passwords, credit card numbers, etc..., for use in malicious activities.
          </td></tr><tr data-index="3"><td style="">
            <strong>Botnets</strong>
          </td><td style="">
            Known to participate in a Bot network. These include Command and Control (CNC, C2) Servers and sites that deliver or receive data as part of the malicious transaction (bots, zombies).
          </td></tr><tr data-index="4"><td style="">
            <strong>Spam</strong>
          </td><td style="">
            Known to serve, deliver or aide in the propagation of Spam.
          </td></tr><tr data-index="5"><td style="">
            <strong>Exploits</strong>
          </td><td style="">
            Sites that are known to host or aide in exploits, drive-by-downloads and other activities that identifies and compromises vulnerable systems.
          </td></tr><tr data-index="6"><td style="">
            <strong>High Risk Sites and Locations</strong>
          </td><td style="">
            Domains and hostnames that match against the OpenDNS predictive security algorithms from security graph.
          </td></tr><tr data-index="7"><td style="">
            <strong>Bogon</strong>
          </td><td style="">
            Bogons are IP Addresses that are known to belong to reserved IP address spaces that is supposedly unallocated or undelagated.  Sites in this category are bogons that are known to be sending traffic.
          </td></tr><tr data-index="8"><td style="">
            <strong>Ebanking Fraud</strong>
          </td><td style="">
            Known to engage in fraudulent activities that relate to electronic banking.
          </td></tr><tr data-index="9"><td style="">
            <strong>Indicators of Compromise (IOC)</strong>
          </td><td style="">
            Hosts that have been observed to engage in Indicators of Compromise.
          </td></tr><tr data-index="10"><td style="">
            <strong>Domain Generated Algorithm</strong>
          </td><td style="">
            Domains that are extracted from malware that employ algorithms that generate domains for potential use in future malicious activities such as hosting malware or as an exfiltration destination.
          </td></tr><tr data-index="11"><td style="">
            <strong>Open HTTP Proxy</strong>
          </td><td style="">
            Hosts that are known to run Open Web Proxies and offer anonymous web browsing services.
          </td></tr><tr data-index="12"><td style="">
            <strong>Open Mail Relay</strong>
          </td><td style="">
            Commonly used by Spam and Phishing attackers, sites in this category are hosts that are known to offer anonymous email relaying services.
          </td></tr><tr data-index="13"><td style="">
            <strong>TOR exit Nodes</strong>
          </td><td style="">
            Hosts known to offer exit node services for the Tor Anonymizer network.
          </td></tr><tr data-index="14"><td style="">
            <strong>DNS Tunneling</strong>
          </td><td style="">
            Sites that provide DNS Tunneling as a service. These services can be for PC or mobile and create a VPN connection specifically over DNS to send traffic that may bypass corporate policies and inspection.
          </td></tr><tr data-index="15"><td style="">
            <strong>Dynamic DNS</strong>
          </td><td style="">
            Sites that are hosting dynamic DNS services. Attackers can use this technology as an evasion technique against IP blacklisting.
          </td></tr><tr data-index="16"><td style="">
            <strong>Newly Seen Domains</strong>
          </td><td style="">
            Domains that have recently been registered, or not yet seen via telemetry. The behavior of these URLs has not been observed enough to establish the appropriate reputation. Spammers and malicious actors may rely on newly registered, or previously unused domains to disguise their activities, and avoid interdiction due to low reputation. Some legitimate URLs may briefly appear in this threat category as they become visible.
          </td></tr><tr data-index="17"><td style="">
            <strong>Cryptojacking</strong>
          </td><td style="">
            Websites with embedded scripts to mine cryptocurrency which use the visitor's web browser. The script may belong to the owner of the web site, or injected by a malicious third-party, and is used as a method of generating revenue.
          </td></tr><tr data-index="18"><td style="">
            <strong>Linkshare</strong>
          </td><td style="">
            Websites that share copyrighted files without permission. The web site may be compromised, or otherwise involved in illegal file sharing.
          </td></tr><tr data-index="19"><td style="">
            <strong>Malicious Sites</strong>
          </td><td style="">
            Sites exhibiting malicious behavior that do not necessarily fit into another, more granular, threat category.
          </td></tr></tbody>
      </table>


## Security Intelligence Summary



