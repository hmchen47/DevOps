# Posture Assessment

## What is Posture?

+ Posture Assessment & Remediation: Checking anfd Enforcing Compliance
    + NAC Agents
    + Cjecks
    + Status

+ Posture Assessment
    + Before connect to network, e.g.
        + Windows update
        + AntiVirus, AntiSpyware
        + Windows Registry settings
        + Applications/Services - Running
    + NAC = Network Access Control
    + NAC Agents: check requirements before access network
    + Policies: 
        + Authentication: mab, dot1x, WebAuth
        + Authorization: Customized, Guest Flow, WebAuth
    + Posture: compliance, no-compliance, unknown
    + Authorization Profiles w.r.t. Posture
        1. Unknown: Redirect to ISE to download NAC Agent
        2. Noncompliance: update, quaratine, remediation
        3. Compliance: right privilege, proper VLAN, etc.

## Planning and/or Updating NAC Files on the ISE Server

+ Preparing ISE for Posture Provisioning Downloads from Cisco
    + Provisioning Resources Predefined: Rules, AV & AS version info
    + Agent and Software: Windows  & Mac

+ NAC Agent Functionality
    1. Deployed Active Directory Groups Policy Objects
    2. Authorization profile to check compliance

+ AV & AS Complance
    + ISE: 
        + Administration > System - Settings > Posture = (General settings, Reassessments, Updates, Acceptable Use Policy)
        + Administration > System - Settings > Posture > Updates: Update feed URL=(https://www.cisco.com/web/secure/pmbu/posture-update.xml), Web
    + Download New Agents <br/>
        Policy > Policy Elements > Results > Client Provisioning > Resources > Add (Agent resource from Cisco site): select all or appropriate items > Save


## Providing NAC Agents from ISE



## Enforcing PostureRequirements


