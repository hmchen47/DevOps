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




## Patching Endpoints



