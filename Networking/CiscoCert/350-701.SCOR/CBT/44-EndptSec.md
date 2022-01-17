# 44. Endpoint Security

Trainer: Keith Barker


## Introduction to Endpoint Security

- Learning goals
  - endpoint protection
  - mobile device management
  - MFA
  - posture assessment
  - patch management


## Why Endpoint Protection is Critical

- Endpoint protection overview
  - people prerequisite: training for social engineering, screen locking, etc.
  - network prerequisite: WSA, ESA, Umbrella, NGFW/IPS, Application Visibility & Control
  - purpose
    - improving security
    - compliance
    - risk management strategy
  - solution: AMP & AnyConnect
    - update periodically
    - limited right for access
    - posture: machine to meet the minimal requirements
      - OS-build
      - AV/AM updated to a certain date
      - registry, file, location, etc.
    - agent: permant or temporary
  - AnyConnect w/ ISE for identities


## The Value of Mobile Device Management

- Mobile device management (MDM)
  - devices: laptops w/ WiFi, mobile phones
  - locations: local or remote
  - on-board: brining on a mobile device into mobile device management system
  - inventory: the devices in MDM system
  - advantages
    - application protection: allowing to run on devices
    - data protection: enforcing encryption
    - malware/virus protection
    - identity management
    - provisioning: automatic and routine
    - templates: consistent policies
  - [MDM Solutions](https://www.trustradius.com/mobile-device-management-mdm) (some popular ones)
    - Microsoft Endpoint Manager (Microsoft Intune + SCCM)
    - Workspace ONE Unified Endpoint Management (UEM) Powered by AirWatch
    - IBM MaaS360 with Watson
    - Cisco Meraki SM


## Using Multi-Factor Authentication

- Multi-factor authentication (MFA) overview
  - authentication methods
    - password
    - 802.1x
      - wireless mostly
      - supplicant: AnyConnect
      - authenticator: switch or MLC
      - authentication server: AAA, Radius, ISE
    - local/central web authentication: redirect to server or ISE to login 
  - factors - categories of authentication
    - knowledge: user knows, e.g., password, SIN, security questions
    - possession: user has, e.g., token generator
    - inherence: user is/does, e.g., biometrics, fingerprint, iris, face
  - MFA: authenticating user from 2 of 3 factors


## Posture Assessment for Endpoint Security

- Posture assessment overview
  - the strength of the cybersecurity controls and protocols for predicting and preventing cyber threats
  - typical procedure for posturing
    - checking device posture before allowing fully access network, such as minimum anti-virus and os updates or patch
    - redirect to a quarantine page if not compliant
    - remediate the incompliant items to gain the full access
  - components
    - posture agent: a piece of software on endpoint devides to connect to the server
    - posture server: ISE


- Demo: config posture assessment on ISE
  - Work Centers tab > Posture: subtabs - Overview, Network Devices, Client Provisioning, Policy Elements, Posture Policy, Policy Sets, Troubleshoot, Reports, Settings
  - Overview subtab: processes - 1) Prepare; 2) Define; 3) Go Live & Monitor
    - Prepare: Network Access Devices, Updates, Client Provisioning Resources(NAC or AnyConnect), Acceptable Use Policy (AUP), Settings
    - Define: Policy Elements (conditions, remediation, posture requirements), Posture Policy, Client Provisioning Portal
    - Go Live & Monitor: Auditing, Troubleshooting
  - Network Devices subtab: devices controlling access
  - Client Provisioning: folders - Client Provisioning Policy, Resources, Client Provisioning Portal
    - Client Provisioning Policy: list of default and customized provisioning policies
    - Resources: list of files for download and able to add new profiles w/ details
    - Client Provisioning Portal: default or customized portals
  - Policy Elements: flders - Conditions (Firewall Condition, Anti-Malware, Anti-Virus, File, Registry, etc.), Remediations (Anti-Malware, Anti-Virus, Ant-Spyware, Firewall)


## Patching Endpoints

- Patch management for endpoints
  - [Talos - Vulnerability Information](https://talosintelligence.com/vulnerability_info)
    - zero-day vulnerabilities
    - disclosed vulnerabilities
  - [Talos > Vulnerability Information > Microsoft Advisories](https://talosintelligence.com/ms_advisory_archive/ms-2022)
    - list of vulnerabilities
    - redirect to MSRC to review the impact and details
  - procedure for change management
    - test the update first to find negative impacts
    - communicate w/ end users to implement the update




