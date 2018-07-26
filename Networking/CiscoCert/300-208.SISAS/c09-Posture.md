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

+ Implementing NAC Agent Provisioning: Profiles, Policies, and Ports
    + Provision Policy
    + ACLs and Redirection
    + Posture Agent Profiles
    + Authorization Profiles'

+ Provison Policy
    + Types of system
    + Redirect if Agent not existed -> ISE server

+ ACLs & Redirect
    + DACL
    + CPP (Client Posturing Portal)

+ Posture Agent profile: ISE - Posture to report to

+ Demo: Create a Posture Profile
    + ISE Validation: Operations > Authentication > Show Live Serssions > C0A Action=Session termination with port bounce: Endpoint ID=CB:BC:C8:97:00:5C, Identity=it-bob -> Successfully re-authenticate using existing supplicant
    + Posture Profile: Policy > Policy Elements > Results > Client Provisioning > Resources (same as downloaded software) > Add (ISE Posture Agent Profile): Name=Nuglab_AgentProfile, Discovery host=ise.nuglab.com > Submit

+ Demo: Client Provisioning Policy <br/>
    Policy > Client Provisioning > Name=All-Windows, OS=Windows All, Conditions=(AD1:ExternalGroups EQUALS nuglab.com/Users/Domain Users), Results=(Agent=NAC Agent 4.9.4.3, Profile=Nuglab_AgentProfile, Compliant mode=None) > Done > Save

+ Demo: Authorization Profile
    + Policy > Policy Elements > Results > Authentication > Downloadable ACL > Add: Name=ACL-During-Posture, DAACL=(permit ip any any) > Submit
    + Policy ? Policy Elements > Results > Authorization > Authorization Profile > Add: Name=POSTURE-AUTH-PROFILE, Tasks=(DACL=ACL-During-Posture, Web Redirection (CWA, DRW, MDM, NSP, CPP)=Client Provisioning (Posture)=REDIRECT(ACL)) > Submit

+ Demo: Apply Profile
    + Policy > Authorization > User and PC Authenticated > edit: Conditions=(AD1:ExternalGroups: EQUALS nuglab.com/Users/Domain Users, Network Access:UseCase EQUALS Guest Flow, __Session:PostureStatus EQUALS Compliant__) > Done > Save
    + Policy > Authorization > User and PC Authenticated > edit (Duplicate Below): Name=User with Unknown PC, Conditions=(AD1:ExternalGroups: EQUALS nuglab.com/Users/Domain Users, Network Access:UseCase EQUALS Guest Flow, __Session:PostureStatus EQUALS Unknown__), Permissions=__POSTURE-AUTH-PROFILE__

+ Verification:
    + PC - triggering: AnyConnect > Network Profile=Class Fast 
    + SW1
        ```cfg
        show authentication sessions int gi0/7
        ! User-Name=it-bob, Status=Authz Success, 
        ! ACS ACL=xACSACLx-IP-ACl-During-Posture-543aebab, URL Redirect ACL=REDIRECT
        ! URL Redirect=https://ise.nuglab.com:8443/guestportal/gateway?sessionId=010203040000000170065EFD8&action=cpp
        ```
    + PC: IE (http://www.google.com) >  Client Provisioning Portal: click to install agent > Install Cisco NAC Agent > Full Network Access > ok
    + SW1
        ```cfg
        show authentication sessions int gi0/7
        ! User-Name=it-bib, Status=Authz Success, 
        ! CS ACL=xACSACLx-IP-PERMIT_ALL_TRAFFIC-537cb1d6
        ! vlan Policy=1 (No Redirection anymore)
        ```
    + ISE Verification: Operations > Authentication > Entries for transaction
        + Posture status=unknown: No Agent, Profile=Our-Author-Profile -> POSTURE-AUTH-PROFILE => Redirect to CPP & install agent
        + Posture status=compliant: Agent installed, Profile=Our-Auth-Profile


## Enforcing PostureRequirements


