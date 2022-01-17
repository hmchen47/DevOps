# Implememting and Operating Cisco Security Core Technologies 350-701 (SCOR)


Trainers: Knox Hutchinson, Keith Barker, Bart Cstale

Institution: CBY Nugget


[Original Contents](https://www.cbtnuggets.com/it-training/cisco/scor-350-701)


## Summary

- [Security Fundamental](00a-SecConcept.md)
- [Virtual Private Networks (VPNs)](00b-VPNs.md)
- [Security Intelligence](00c-Intelligence.md)
- [L2 Security](00d-L2Sec.md)
- [Routing Authentication](00e-RoutingSec.md)
- [Management Plane Security](00f-MgmtSec.md)
- [Security for Cloud Service](00g-CloudSec.md)
- [Application Layer Security](00h-AppLSec.md)
- [Endpoint Security](00i-EndptSec.md)
- [Data Exfiltration](00j-Exfiltrate.md)



## Security Fundamental

### 01\. [Explain Common Threats Against On-premises and Cloud Environments](01-Threats.md)

- Introducing the Cybersecurity Landscape
- Know Your Assets
- Know Your Vulnerabilities
- Know Your Threats
- Virus, Worms, Trojan, and Malware
- Phishing and Social Engineering
- DDoS - Attacking Availability
- Spoofing and MitM Attacks
- Summarizing the Threat Landscape

### 02\. [Compare Common Security Vulnerabilities](02-Security.md)

- Introducing Common Attack Vectors
- Get to Know OWASP
- The SQL Injection’; SELECT * FROM table
- Cross-Site Scripting; var doCode{}
- Password Protection
- Plain-Text Protocols
- The Buffer Overflow
- Summarizing Common Vulnerabilities

### 03\. [Components of Cryptography](03-Cyrptograph.md)

- Introduction to Components of Cryptography
- Data Integrity
- Data Privacy
- SSL and TLS
- Public Key Infrastructure (PKI)
- IPsec
- Authentication
- Components of Cryptography Summary

### 04\. [IPsec Fundamentals](04-IPsec.md)

- Introduction to IPsec
- IPsec Overview
- IKEv1 and IKEv2
- Crypto Map IPsec
- VTI IPsec
- DMVPNs
- FlexVPN
- GET VPN
- NAT Traversal
- IPsec Fundamentals Summary

### 23\. [Network Infrastructure Device Hardening](23-Harden.md)

- Introduction to Device Hardening
- Device Hardening Overview
- Cisco Guide to Harden IOS Devices
- Management Plane Hardening
- Control Plane Hardening
- Data Plane Hardening
- Device Hardening Checklist
- Hardening Review



## Virtual Private Networks (VPNs)

### 05\. [Cisco Router Site-To-Site VPNs](05-S2SVPN.md)

- Introducing Site-To-Site VPNs
- Planning for IPsec Site-To-Site
- Designing a Site-To-Site VPN
- Configuring an IKE Phase 1 Policy
- Configuring an IKE Phase 2 (IPsec) Policy
- Enabling the IPsec Policy
- Protocol Analysis IPsec

### 06\. [Cisco Point-To-Point GRE over IPsec VPNs](06-VTI.md)

- Introduction to P2P GRE over IPsec VPNs
- Overview of GRE over IPsec VPNs
- P2P GRE Tunnel Design
- P2P GRE Tunnel Implementation
- P2P GRE Tunnel Verification
- IPsec Tunnel Protection Design
- IPsec Virtual Tunnel Interface Configuration
- IPsec Static VTI Verification

### 07\. [Cisco DMVPN](07-DMVPN.md)

- Introduction to DMVPN
- DMVPN Overview
- Planning for the mGRE Tunnel
- mGRE Tunnel Configuration
- NHRP Overview and Design
- Configuring NHRP for DMVPN
- Adding Routing to DMVPN
- Verifying DMVPNs
- Adding IPsec Protection Profiles
- DMVPN Summary

### 08\. [Cisco GET VPN](08-GETVPN.md)

- Introduction to GET VPN
- GET VPN Overview
- GET VPN Key Servers (KS)
- GET VPN Members (GM)
- GET VPN Design
- Implementing KS Configuration
- Implementing GM Configuration
- GET VPN verification
- GET VPN Summary

### 09\. [Cisco FlexVPN](09-FlexVPN.md)

- Introduction to FlexVPN
- FlexVPN Overview
- FlexVPN Components
- IKEv2 Flex VPN Site-To-Site Planning
- IKEv2 FlexVPN Site-To-Site Configuration
- IKEv2 FlexVPN Verification
- Adding Routing to FlexVPN
- FlexVPN Summary

### 10\. [Cisco Remote Access VPNs](10-RAVPNs.md)

- Introduction to RA VPNs
- RA VPN Overview
- FlexVPN IPsec RA VPNs
- FlexVPN RA Design
- Setting CA Services in IOS
- Configuring FlexVPN RA
- AnyConnect Profile Editor
- Testing and Verifying the RA VPN
- Flex VPN RA Summary

### 11\. [Debugging for IPsec Tunnels](11-DebugIPsec.md)

- Introduction to Debugging IPsec
- Overview of IPsec Options
- Troubleshooting Tips for IPsec
- IKEv1, Phase 1, Missing Routes
- IKEv1, Phase 1, Bad Config
- IKEv1, Phase 2 Bad Config
- IKEv2 Troubleshooting
- Summary Troubleshooting IPsec



## Security Intelligence

### 12\. [Security Intelligence](12-Intelligence.md)

- Introduction to Security Intelligence
- Security Intelligence Overview
- Cisco Talos Overview
- Talos Vulnerability Information
- Talos Reputation Center
- Security Intelligence Summary

### 13\. [Explain APIs in the SDN Architecture](13-APISDN.md)

- Introducing APIs and SDN
- What is an API anyway?
- The Northbound API
- The Southbound API
- The Eastbound API
- The Westbound API
- Summarizing APIs and SDN

### 14\. [DNA Center Foundations](14-DNA.md)

- Introducing DNA Center
- What DNA Center Does
- What an SD-Access Fabric Does
- The Four Workflows of DNA Center
- The DNA Center Platform APIs
- Summarizing DNA Center

### 15\. [Interpret Basic Python Scripts used with Cisco Security](15-Python.md)

- Introducing Basic Python Security Scripts
- Extending Python and Setting Variables
- Getting Authenticated
- Getting Monitored Applications
- Summarizing Interpreting Python Scripts

### 16\. [Troubleshoot NetFlow](16-NetFlow.md)

- Introduction to Troubleshooting NetFlow
- NetFlow Overview
- Flavors of NetFlow
- NetFlow v5
- Flexible NetFlow
- NetFlow Collectors and Analyzers
- Troubleshoot NetFlow

### 17\. [The Components of Network Security Design](17-SecDesign.md)

- Intro to components of Network Security Design
- Network Access Control
- End Point Security
- Next Generation Firewalls and IPS
- TrustSec and MACsec




## L2 Security

### 18\. [Configure and Verify Cisco Port Security](18-PortSec.md)

- Introducing Port Security
- Understanding Port Security and Why we Need It
- Port Security Defaults
- Implementing Port Security on Layer 2 Interface
- Customizing Port Security
- Configuring Auto Errdisable Recovery
- Applying Port Security Skills in Production
- Review of Configure and Verify Cisco Port Security
- Cisco CCNA (200-301) Assessment Lab: Security

### 19\. [Configure and Verify Cisco DHCP Snooping](19-DHCPSnoop.md)

- Introducing DHCP Snooping
- Why is DHCP Snooping Needed
- The Recipe for DHCP Snooping
- Building and Implementing DHCP Snooping in PT
- Adding Source Guard to a Switch
- Applying DHCP Snooping in Production
- Review of Configure and Verify Cisco DHCP Snooping
- Configure and Verify Cisco DHCP Snooping

### 20\. [Configure and Verify Cisco Dynamic ARP Inspection](20-ARPInspec.md)

- Introducing Dynamic ARP Inspection (DAI)
- Why is DAI Needed
- The Recipe and Commands for DAI
- Implementing DAI
- ARP Access Lists for Non-DHCP Devices
- Additional DAI Options and Features
- Applying DAI to the Production Network
- Review of Configure and Verify Cisco Dynamic ARP Inspection
- Configure and Verify Cisco Dynamic ARP Inspection

### 21\. [Private VLANS](21-PVLANs.md)

- Introduction to Private VLANs
- PVLANs Overview
- Promiscuous Ports
- PVLAN Design
- Implement PVLANs
- Verify PVLANs
- Trunking and PVLANs
- PVLAN Summary

### 22\. [VRF-lite](22-VRFLite.md)

- Introduction to VRF-lite
- VRF-lite Overview
- VRF-lite Configuration Basics
- VRFs on a Multi-Layer Switch
- VRF-lite Design
- VRF-lite Implementation
- VRF-lite Adding Routing
- VRF-lite Routing Verification
- DHCP VRF Services
- VRF-lite Summary

### 24\. [Configure Cisco TrustSec](24-TrustSec.md)

- Introduction to TrustSec
- TrustSec Overview
- TrustSec Security Groups
- Security Group ACLs
- TrustSec Policies
- Configure Network Devices for TrustSec
- ISE and NAD TrustSec Integration
- Verify TrustSec
- SGT eXchange Protocol (SXP)

### 25\. [Additional Layer 2 Security](25-L2Sec.md)

- Introduction to Additional Layer 2 Security Options
- Layer 2 Security Overview
- Storm Control
- Root Guard
- BPDU Guard
- Summary of Layer 2 Security




## Routing Authentication

### 26\. [EIGRP Neighbor Relationships and Authentication](26-EIGRPAuth.md)

- Introduction to EIGRP Relationships and Authentication
- Neighborship Overview
- Authentication Overview
- EIGRP Hands on Lab with Authentication
- EIGRP Neighbor Relationships and Authentication

### 27\. [Troubleshoot OSPF Authentication for IPv4](27-OSPFAuthIPv4.md)

- Intro to IPv4 OSPF Authentication and Troubleshooting
- Overview of OSPF Authentication
- Implement OSPF Authentication
- Virtual Links and Authentication
- Troubleshooting OSPF Authentication Lab 01
- Troubleshooting OSPF Authentication Lab 02
- Virtual lab: Troubleshoot OSPF Authentication for IPv4

### 28\. [Troubleshoot OSPF Authentication for IPv6](28-OSPFAuthIPv6.md)

- Intro to IPv6 OSPF Authentication and Troubleshooting
- IPv6 OSPF Authentication Overview
- Implement and Verify Authentication
- Troubleshooting OSPF Authentication Lab 01
- Troubleshooting OSPF Authentication Lab 02
- Virtual lab: Troubleshoot OSPF Authentication for IPv6



## Management Plane Security

### 29\. [Firepower Access Control Policies](29-Firepower.md)

- Access Control Policy Overview
- Access Control Policy Rule Actions Concepts
- Access Control Policy Rule Actions Demonstration
- URL Filtering
- Malware and File Inspections
- SSL/TLS Decryption
- IPS Inspection

### 30\. [Management Options to Improve Security](30-OptImprove.md)

- Introduction to Secure Network Management
- Overview of Secure Management
- Syslog Overview
- NTP with Authentication
- Change Control

### 31\. [Troubleshoot SNMP](31-SNMPTshoot.md)

- Introduction to Troubleshooting SNMP
- SNMP Overview
- SNMPv2 Configuration
- SNMPv3 Client Configuration
- SNMPv3 Server Configuration
- Troubleshooting SNMP

### 32\. [Troubleshoot Network Problems using Logging](32-LoggingTshoot.md)

- Introduction to Troubleshooting using Logging
- Logging Overview
- Configuring Logging
- Conditional Debugging
- Troubleshoot Network Problems using Logging



## Security for Cloud Service

### 33\. [Cloud Service and Deployment Models](33-CloudModel.md)

- Planning for Cloud Services
- Plan for Infrastructure As A Service
- Plan for Platform As A Service
- Plan for Software As A Service
- Plan for Cloud Deployment Models

### 34\. [Planning for Software Development Methodologies](34-SWDevelop.md)

- Software and App Development Methodologies
- Plan for Waterfall Method
- Plan for Lean and Agile Methods
- Plan for Kanban and Scrum Teams
- Continuous Integration, Deployment, and Delivery
- Understand CICD Pipelines in Action
- Plan for DevOps
- Plan for DevSecOps

### 35\. [Planning for and Securing Cloud Software-as-a-Service](35-SaaSSec.md)

- Planning for Software-as-a-Service Security
- Federating Identities with SAML, OAuth, and OpenID
- Cisco Zero-Trust for the Workforce
- Cisco Cloudlock Access Security Broker
- Securing DNS with Cisco Umbrella and OpenDNS
- Securing Communications with Cisco Email Security

### 36\. [Planning for and Securing Cloud Infrastructure-as-a-Service](36-IaaSSec.md)

- Planning for Cloud Infrastructure Security
- Assessing Cloud Service Providers
- Isolating and Segmenting Cloud Networks
- Leveraging Virtual Appliances
- Hardening, Protecting, and Maintaining Cloud VMs
- Planning for Infrastructure-as-Code
- Monitor and Analyze with Stealthwatch
- Understand the Tenets of Zero Trust Security
- Zero Trust Token Auth Demo

### 37\. [Planning for and Securing Cloud Platform-as-a-Service](37-PaaSSec.md)

- Securing Cloud Platform-as-a-Service
- Plan for Containers
- Secure Container Images and Registries
- Orchestrating Containers
- Open Web Application Security Project Controls
- Cisco Zero-Trust Architecture Overview
- Securing Workloads with Cisco Tetration
- Visibility with Cisco AppDynamics




## Application Layer Security

### 38\. [Capture and Redirection Methods](38-Redirect.md)

- Introduction to Capture and Redirection Methods
- Capture and Redirection Overview
- Policy Based Routing (PBR) Overview
- PBR Configuration and Testing
- WCCP Overview and Planning
- WSA Configuration for WCCP
- IOS Configuration for WCCP
- Testing WCCP
- Traffic Redirection Summary

### 39\. [Cisco Web Security](39-WebSec.md)

- Introduction to Cisco Web Security
- Web Security Appliance Overview
- WSA and AD Integration
- WSA Identification Profiles
- WSA Access Policies
- WSA Application Filtering
- WSA TLS Decryption Overview
- WSA Certificate Management
- WSA Decryption Policy
- WSA Additional Security Features

### 40\. [Cisco Email Security](40-EmailSec.md)

- Introduction to Cisco Email Security
- Cisco Email Security Overview
- ESA Inbound Mail Overview
- Blocking Incoming Email
- ESA Outbound Mail Overview
- SPAM Filtering
- Email Anti-Virus
- DLP
- Encryption


### 41\. [Cisco Umbrella](41-Umbrella.md)

- Introduction to Cisco Umbrella
- Cisco Umbrella Overview
- Umbrella Components
- Policy Overview
- Policy Components
- Policy Creation
- Core Identities
- Umbrella CA Certificates
- Reporting and Investigation
- Umbrella VA
- Umbrella Summary



## Endpoint Security


### 42\. [Understand and Configure AMP for Endpoints](42-AMPEndpt.md)

- Introducing Endpoint Security
- The Types of Endpoint Protection
- Introducing Advanced Malware Protection (AMP) for Endpoints
- Configuring Simple Outbreak Controls in AMP
- Explore Other Outbreak Controls
- Understand Groups and Policies

### 43\. [Explain Various Types of Endpoint Defenses](43-EndptTypes.md)

- Introducing Endpoint Defense Mechanisms
- Anti-Virus and Anti-Malware
- Indicators of Compromise (IoC)
- Retrospective Analysis
- Dynamic File Analysis
- Summarizing Endpoint Protection Mechanisms

### 44\. [Endpoint Security](44-EndptSec.md)

- Introduction to Endpoint Security
- Why Endpoint Protection is Critical
- The Value of Mobile Device Management
- Using Multi-Factor Authentication
- Posture Assessment for Endpoint Security
- Patching Endpoints

### 45\. [Describe Controls for End Users' Network Access](45-NetAccess.md)

- Introducing Network Access Control for Endpoints
- Endpoint Profiling
- Identity-Based Authentication
- Authenticating with AnyConnect
- Posture Assessment
- Cisco TrustSec and Security Group Tags (SGTs)
- Change of Authorization (CoA)


### 46\. [802.1X Fundamentals](46-8021xFund.md)

- Introduction to 802.1x Fundamentals
- Network Authentication and Authorization
- Options for Authentication
- Options after Authentication

### 47\. [Configure ISE for 802.1X](47-ISEdot1x.md)

- Introduction to Configuring ISE
- Identity Stores
- Configure ISE to use AD
- Adding Network Devices to ISE
- Policy Set Overview
- Creating a Policy Set
- Authorization Policies
- Summary

### 48\. [Configure a Switch for 802.1X](48-Sw8021x.md)

- Introduction to Switch Configuration for 802.1X
- Configure Global AAA Parameters
- Port Configuration
- Testing and Verifying
- Switch Configuration Summary



## Data Exfiltration

### 49\. [Explain Exfiltration Techniques](49-Exfiltration.md)

- Introducing Attacker Exfiltration Techniques
- DNS Tunneling Exfiltration
- HTTP(S) Exfiltration
- Outbound File Transfers
- Text-Based Protocols
- Recapping Exfiltration Techniques

### 50\. [Explaining the Benefits of Streaming Telemetry](50-Streaming.md)

- Introducing Streaming Telemetry
- What is Telemetry?
- Network Telemetry
- Endpoint Telemetry
- Summarizing Telemetry

### 51\. [Describing the Features of Various Cisco Security Offerings](51-SecOffer,md)

- Introducing Cisco Security Platforms
- Stealthwatch
- pXGrid
- Umbrella Investigate
- Cognitive Threat Analytics
- AnyConnect Network Visibility Module
- Summarizing Cisco Security Platforms


