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
  - Identity Service Engine Lab
  - access ISE w/ browser
  - Work Centers tab > Profiler > Overview: procedures - 1) Prepare; 2) Define; 3) Go Live & Monitor
  - Work Centers tab > Profiler > Network Devices > entry - Name = Centos, Profile Name = Cisco ->
    - Services = Radius, TACACS, TrustSec, MAB, 802.1X, WebAuth
    - CoA = RFC, Port Bounce, Port Shutdown, Re-Auth, RFC Push (default CoA port: 1700, default DTLS CoA Port: 2083)
    - Native URL Redirect: Dynamic
  - Work Centers tab > Profiler > Policy Elements > Policy Conditions > Profiler Conditions > list of profiler for devices
  - Work Centers tab > Profiler > Profiling Policies: policies for devices


## Identity-Based Authentication




## Authenticating with AnyConnect




## Posture Assessment




## Cisco TrustSec and Security Group Tags (SGTs)




## Change of Authorization (CoA)




## Summarizing Network Access Controls for Endpoints



