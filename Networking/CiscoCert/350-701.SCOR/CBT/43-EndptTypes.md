# 43. Explain Various Types of Endpoint Defenses

Trainer: Knox Hutchinson


## Introducing Endpoint Defense Mechanisms

- Learning goals
  - Anti-Virus & Anti-Malware
  - Indicators of compromise
  - Retrospective analysis
  - dynamic file anallysis


## Anti-Virus and Anti-Malware

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
  - a piece of code passes certain tests $\timplies$ granted access
  - technologies
    - signatures
    - sandboxing
    - fuzzy fingerprinting
    - machine learning

## Indicators of Compromise (IoC)

- Indicators of Compromise (IoC)
  - pieces of forensic data, such as data found in system log entries or files, that identify potentially malicious activity on a system or network
  - components
    - destination of network traffic, e.g., North Korea? Russia?
    - volume of outbound traffic,e.g., SFTP or email data from 100MB to 10GB
    - run as admin/sudo
    - SQL injection:
      - disk I/O w/ read volume or SQL monitoring
      - web server log


## Retrospective Analysis

- Retrospective security overview
  - part of EDR
  - a protection system that covers the entire attack continuum
  - before an attack happens and includes continuous analysis and advanced analytics during and after the event
  - able to view any point in the past
  - tools: retrospection, attack chain correlation, behavioral indications of compromise (IOCs), trajectory and breach hunting
  - able to monitoring the environmental changes


## Dynamic File Analysis

- Dynamic file analysis overview
  - able to scan files w/o being detected
  - polymorphic file: changing nature of file to pass EPP. e.g., file extention
  - EDR able to detect the changes and send to AMP on cloud
  - EPP then downloading the changes to detect the incoming files


## Summarizing Endpoint Protection Mechanisms

- Summary
  - anti-virus & anti-malware
  - IoC
  - retrospective security
  - dynamic file analysis


