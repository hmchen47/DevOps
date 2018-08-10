# Posture Assessment

## What is Posture?

+ Posture Assessment & Remediation: Checking and Enforcing Compliance
    + NAC Agents
    + Checks
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
    + Authorization Profiles w.r.t. Posture
        1. __Unknown__: Redirect to ISE to download NAC Agent
        2. __Noncompliance__: update, quarantine, remediation
        3. __Compliance__: right privilege, proper VLAN, etc.

## Planning and/or Updating NAC Files on the ISE Server

+ Preparing ISE for Posture Provisioning Downloads from Cisco
    + Provisioning Resources Predefined: Rules, AV & AS version info
    + Agent and Software: Windows  & Mac

+ NAC Agent Functionality
    1.  Deployed Active Directory Groups Policy Objects
    2.  Authorization profile to check compliance

+ AV & AS Compliance
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

+ Provision Policy
    + Types of system
    + Redirect if Agent not existed -> ISE server

+ ACLs & Redirect
    + DACL
    + CPP (Client Posturing Portal)

+ Posture Agent profile: ISE - Posture to report to

+ Demo: Create a Posture Profile
    + ISE Validation: Operations > Authentication > Show Live Sessions > CoA Action=Session termination with port bounce: Endpoint ID=CB:BC:C8:97:00:5C, Identity=it-bob -> Successfully re-authenticate using existing supplicant
    + Posture Profile: Policy > Policy Elements > Results > Client Provisioning > Resources (same as downloaded software) > Add (ISE Posture Agent Profile): Name=Nuglab_AgentProfile, Discovery host=ise.nuglab.com > Submit

+ Demo: Client Provisioning Policy <br/>
    Policy > Client Provisioning > Name=All-Windows, OS=Windows All, Conditions=(AD1:ExternalGroups EQUALS nuglab.com/Users/Domain Users), Results=(Agent=NAC Agent 4.9.4.3, Profile=Nuglab_AgentProfile, Compliant mode=None) > Done > Save

+ Demo: Authorization Profile
    + DACL: Policy > Policy Elements > Results > Authentication > Downloadable ACL > Add: Name=ACL-During-Posture, DACL=(permit ip any any) > Submit
    + Profile: Policy Elements > Results > Authorization > Authorization Profile > Add: Name=POSTURE-AUTH-PROFILE, Tasks=(DACL=ACL-During-Posture, Web Redirection (CWA, DRW, MDM, NSP, CPP)=Client Provisioning (Posture)=REDIRECT(ACL)) > Submit

+ Demo: Apply Profile
    + AuthZ Policy - Compliant: Policy > Authorization > User and PC Authenticated > edit: Conditions=(AD1:ExternalGroups: EQUALS nuglab.com/Users/Domain Users, Network Access:UseCase EQUALS Guest Flow, __Session:PostureStatus EQUALS Compliant__) > Done > Save
    + AuthZ Policy - Unknown: Policy > Authorization > User and PC Authenticated > edit (Duplicate Below): Name=User with Unknown PC, Conditions=(AD1:ExternalGroups: EQUALS nuglab.com/Users/Domain Users, Network Access:UseCase EQUALS Guest Flow, __Session:PostureStatus EQUALS Unknown__), Permissions=__POSTURE-AUTH-PROFILE__

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
        ! ACS ACL=xACSACLx-IP-PERMIT_ALL_TRAFFIC-537cb1d6
        ! vlan Policy=1 (No Redirection anymore)
        ```
    + ISE Verification: Operations > Authentication > Entries for transaction
        + Posture status=unknown: No Agent, Profile=Our-Author-Profile -> POSTURE-AUTH-PROFILE => Redirect to CPP & install agent
        + Posture status=compliant: Agent installed, Profile=Our-Auth-Profile


## Enforcing PostureRequirements

+ Enforcing Posture Compliance: Requirements, Remediation and Verification
    + Posture Requirements
    + Posture Remediation
    + Posture Policy

+ Posture Requirements:
    + NAC Agent implemented
    + AV: remediation for quarantine, VLAN

+ Demo: Posture requirements
    +  Validation: Policy > Policy Elements > Results > Posture > Remediation Actions > Requirements > Any_AV_Installation_Win: OS=Windows All, Conditions=Any_av_win_inst, Remediation Actions=Message Text Only
    + Default Action List: Policy > Policy Elements > Results > Posture > Remediation Actions (default: AV, AS, File Launch Program, Link, Windows Server Update Service, Windows Update)
    + Remediation: Policy > Policy Elements > Results > Posture > Remediation Actions > File Remediation > Add: Name=Microsoft_Security_Essentials, version=test-v2, File_to_Upload=mseinstall.exe
    + Requirement: Policy > Policy Elements > Results > Posture > Remediation Actions > Requirements > Any_AV_Installation_Win > edit: Name=Win_Must_Have_AV, OS=Windows All, Conditions=Any_av_win_inst, Remediation Actions=(Action=Microsoft_Security_Essentials, message shown to Agent user=This endpoint has failed check for any AV installation, Please install the MSE ...) > Done > Save

+ Demo: Posture Policy
    + Posture Policy: Policy > Posture > Rule Name=Windows Must have an AV, OS=Windows All, other conditions=(Create a New Conditions > AD1:ExternalGroup EQUALS nuglab.com/Users/Domain Users), Requirements=Win_MUst_Have_AV > Done > Save
    + AuthZ Policy: Policy > Authorization > User and PC Authenticated > edit (Duplicate Above): Name=User with non-compliant PC, Conditions=(AD1:ExternalGroups: EQUALS nuglab.com/Users/Domain Users, Network Access:UseCase EQUALS Guest Flow, __Session:PostureStatus EQUALS Noncompliant__)

+ Demo: Verification & Triggering
    + ISE: Operations > Authentication > Show Live Sessions > Identity=it-bob, host/nuglab.com > CoA Action (session terminate with port shutdown) -> Terminate teh session
    + SW1: 
        ```cfg
        int gi0/7
          shut
          no shut
          do show authentication sessions int gi0/7
        ! URL Redirect ACL=REDIRECT, ACS ACL=xACSACLx-IP-ACL-During-Posture-543aebab
        ! URL Redirect=https://ISE.nuglab.com:8443/gurstportal/gateway?sessionId=0102030400000018006A4FC8&action=cpp
        ```
    + PC: Cisco NAC Agent > Temporary Network Access: There is at least one mandatory requirement failing.  You are required to update your system before you can access teh network, Show Details=(Mandatory, Requirement Name=Win_Must_Have_AV) > Repair > Download > Save: mseinstall.exe (Download & Install file) > Full Network Access > ok

+ Demo: Reauthentication
    + SW3:
        ```cfg
        show authentication sessions int gi0/7
        ! User-name=it-bob, Status=Authz Success
        ! ACS ACL=xACSACLx-IP-PERMIT_ALL_TRAFFIC-537cb1d6
        ! dot1x=Authc Success, mab=Not Run, Vlan=1, (No Redirection)
        ```
    + PC: Cisco NAC Agent > List of AntiVirus and AntiSpyware Products Detected by the Agent:
        + Product Name=Microsoft Security Essentials, Product Version=4.6.0305.0, Definition Version=1.185.3127.0, Definition Date=10/13/2014
        + Product Name=Windows Defender, Product Type=Microsoft AS, Product Version=6.1.7600.16358, Definition Version=1.185.2784.0, Definition Date=10/09/2014
    + ISE: Operations > Reports > Endpoints and Users > Posture Detail Assessment: Time Range=Last 30 Minutes > Run > Entry > Details: Client OS=Windows 7 Pro 64-bit, Client NAC Agent=Cisco NAC Agent 4.9.3.4, AV Installed=(Microsoft Security Essentials; 4.6.0305.0;;; Microsoft AV), AS Installed=(Windows Defender; 6.1.7600.16385; 1.185.2784.0;10/09/2014; Microsoft AS, Microsoft Security Essentials;4.6.0305;...)




