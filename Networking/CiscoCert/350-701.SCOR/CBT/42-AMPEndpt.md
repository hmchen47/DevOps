# 42. Understand and Configure AMP for Endpoints

Trainer: Knox Hutchinson


## Introducing Endpoint Security

- Learning goals
  - endpoint protection
  - advanced malware protection (AMP)
  - outbreak control
  - groups and policies



## The Types of Endpoint Protection

- Types of encpoint protection
  - endpoint prevention platforms (EPPs) 
    - stop file from entering the environment
    - anti-virus
    - anti-malware
    - action: quarantine, fix, delete
  - endpoint detection and response platforms (EDRs)
    - maintaining the security about the environment in an on-going monitoring way
    - point-in-time malicious
    - anomalous behavior
    - continuous monitoring
    - analytics ML and AI
    - centralized solution
    - focusing on protecting the endpoints
  - extended detection and response (XDR): integrating security across endpoints, cloud computing, email, and other solutions
  - Solution: Cisco AMP

## Introducing Advanced Malware Protection (AMP) for Endpoints

- Advanced Malware Protection (AMP)
  - AMP existed in network solutions, e.g., firewall, ESA, etc.
  - scanning file entering the system
  - endpoint solution
    - prevention: 
      - constantly updated
      - sanboxing: quarantine files
      - ML & AI 
    - detection
      - continuously monitoring
      - anomalous behavior
      - entering point and trajectory
    - response
      - contain/quarantine
      - telemetry: dashboard on threat overview on the whole network


## Configuring Simple Outbreak Controls in AMP

- Demo: config outbreak control in AMP
  - AMP - Secure Endpoint: tabs: Dashboard, Analysis, Outbreak Control, Management, Accounts
  - Dashboard tab: subtabs - Dashboard, Inbox, Overview, Events, IOS Clarity
  - Dashboard subtab: charts for Compromises, Quarantined Detections, Vulnerabilities; event list for Significant Compromise Artifacts, Compromise Event Types
  - Outbreak Control tab > CUSTOM DETECTION, APPLICATION CONTROL, NETWORK, ENDPOINT IOC
    - CUSTOM DETECTION (mostly commonly used): Simple, Advanced, Android
    - Application  CONTROL: Blocked Applications, Allowed Applications
    - NETWORK: IP Block and Allow Lists
    - ENDPOINT IOC: Scan Summary
    - CUSTOM DETECTION: using hash signature of a file to identify malicious file
  - Outbreak Control tab > CUSTOM DETECTION > Simple > 'Create' button > Name = cbtdemo > 'Save' button
    - entry - cbtdemo > 'Edit' button > tabs - Add SHA-256, Upload File, Upload Set of SHA-256s
    - Upload File > File = nuclearvirus.xlsx, Note = CBT Knox stop nuke 
    - entry - cbtdemo: 1 file, Not associated with any policy or group
    - action: Bob created the file and report hash that time, then we detect malicious now and report to AMP. AMP checks db and find Bob report it. AMP infos Bob to quarantine the file.
  - [dCloud Demo](https://dcloud2-sjc.cisco.com/content/instantdemo/amp-demonow-instant)

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('page')"
      src    = "img/42-ampdash.png"
      alt    = "Snapshot of AMP Dashboard"
      title  = "Snapshot of AMP Dashboard"
    />
  </figure>



## Explore Other Outbreak Controls





## Understand Groups and Policies





## Summarizing Endpoint Security




