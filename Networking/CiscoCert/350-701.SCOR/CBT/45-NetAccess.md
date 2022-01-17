# 45. Describe Controls for End Users' Network Access

Trainer: Knox Hutchinson


## Introducing Network Access Control for Endpoints

- Learning goals
  - profiling
  - authentication
  - authentication w/ AnyConnect
  - posture assessment
  - TrustSec and SGTs
  - change of authorization


## Endpoint Profiling

- Profiling endpoints overview
  - network profiling:
    - gathering basic info 
    - making assumptions
    - deciding access permission
  - access control w/ ISE
    - check MAC adddress w/ existing db when plugged in
      - pre-configured w/ Mac address bypass (MAB)
      - gathering device info and associated w/ existing profile if existed and then config the port, e.g., Cisco Phone w/ Voice VLAN
  

- Demo: ISE sandbox
  - [DevNet Sandbox](https://developer.cisco.com/sandbox.html)
  - reservation required
  - Identity Service Engine w/ MUD Lab
  - access ISE w/ browser
  - Work Centers tab > Profiler > Overview: procedures - 1) Prepare; 2) Define; 3) Go Live & Monitor
  - Work Centers tab > Profiler > Network Devices > entry - Name = Centos, Profile Name = Cisco ->
    - Services = Radius, TACACS, TrustSec, MAB, 802.1X, WebAuth
    - CoA = RFC, Port Bounce, Port Shutdown, Re-Auth, RFC Push (default CoA port: 1700, default DTLS CoA Port: 2083)
    - Native URL Redirect: Dynamic
  - Work Centers tab > Profiler > Policy Elements > Policy Conditions > Profiler Conditions > list of profiler for devices
  - Work Centers tab > Profiler > Profiling Policies: policies for devices


## Identity-Based Authentication

- Identity-based authentication overview
  - username and password: a almost must part of the authentication
  - using 802.1x to force users typing in their username and password
    - supplicant: endpoint devices
    - authenticator: switch or WLC
    - authentication server: identity data store - ISE, ACS, NAP, integrateing w/ AD
  - Remote access w/ VPN
  - BYOD: enterprise, guest
  - profiling


## Authenticating with AnyConnect

- AnyConnect authentication
  - a powerful agent w/ many modules
  - firewall
    - Firepower Threat Defence (FTD) w/ Firepower Management Center (FMC) - optional or ASA
    - pool of IP addresses
  - AnyConnect features
    - VPN: prompt to enter username and password
    - Network
    - Web Security
    - System Scan
    - Roaming Security
    - AMP Enabler
  - gear icon on bottom - settings and statistics of AnyConnect Secure Mobility Client


## Posture Assessment

- Demo: posture assessment w/ AnyConnect
  - download profile from server to check the compliance of posture
  - AnyConnect capable of checking
    - OS
    - AMP installed & installation
    - firewall
    - encryption
  - Web Security: leveraging Umbrella to identify category of web site accessed
  - System Scan: enforcing system scanning about config of firewall, AV, encryption
  - Roaming Security: content security w/ Umbrella
  - AMP enabler: installing AMP


## Cisco TrustSec and Security Group Tags (SGTs)

- Cisco TrustSec and Security Group Tags
  - DNA center
  - identify person than IP address and VLANs
  - control access resources from one to another based on identity
  - major component of SD-Access
  - TrustSec architecture
    - building a secure networks by establishing domains of trusted network devices
    - device authenticated by its peer
    - components
      - authenticated networking infrastructure
      - secure group-based access control
      - secure communication
  - Security Group Tag (SGT)
    - the security group number of the device in L2 frame
    - specify the privileges of a traffic source within a trusted network
    - secure group access automatically generated
    - classify users into groups, e.g., IT, HR, Engineering, Consultant, etc.
    - classify devices into groups, e.g. IT servers, HR servers, Printers, IoT devices, windows servers, etc.


## Change of Authorization (CoA)




## Summarizing Network Access Controls for Endpoints



