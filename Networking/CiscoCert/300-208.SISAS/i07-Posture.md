# Posture Assessment

## Posture Assessment Overview

+ Posture Services - Policies
    + Posture Policy defines the health requirements of endpoints
    + Through posture policies, ISE defines a Windows/Mac endpoint compliance requirements
        + Antivirus, Antispyware, firewall, OS updates
        + Processes running, file existence, registry entries
    + ISE collects endpoint data and matches it against its posture policies
    + Endpoint data collected through
        + NAC Agent
        + AnyConnect Posture module available in AnyConnect 4.0
    + Wireless counterpart: MDM (Mobile Device Management) --> EEM (Enterprise Mobility Management)

+ Posture and Client Provisioning Policies Workflow in Cisco ISE
    <a href="https://www.cisco.com/c/en/us/td/docs/security/ise/2-4/admin_guide/b_ise_admin_guide_24/b_ise_admin_guide_24_new_chapter_010111.html#ID37">
        <br/><img src="https://www.cisco.com/c/dam/en/us/td/i/300001-400000/310001-320000/310001-311000/310142.tif/_jcr_content/renditions/310142.jpg" alt="Posture and Client Provisioning Policies Workflow in Cisco ISE" width="450">
    </a>

+ Requirements for Automatic Remediation
    1.  permanent agent supported
    2.  what the software intended to do, e.g., installing antivirus software, access privileges

+ NAC Agent Overview
    + NAC Agent
        + Temporary web agent based on ActiveX or Java (Windows): Limited remediation
        + Permanent agent (Windows and Mac): Automatic remediation - Not always available
    + NAC Agent compliance module (OPSWAT) used for antivirus and antispyware vendor support
    + NAC Permanent Agent deployment options
        + Manual installation, not scalable
        + Unattended installation, customization available -> Silent activities
        + ISE Client Provisioning Policy (CPP) - ISE Web Service
            + Can also be used to automatically update NAC Agent or compliance module

+ NAC Agent Connectivity Requirements
    + NAC Agent communicates directly with ISE
        + Supplicant requires IP connectivity to ISE
        + NAD is completely bypassed, makes sense as it does not understand posture data
        + No need to know the info, eg., vendor, software, version, etc.
    + TCP 8443 to ISE: Required if NAC Agent is installed through _CPP_
    + UDP/TCP 8909 to ISE: Required for _NAC Agent wizard_ installation via CPP
    + UDP/TCP 8905 to ISE
        + Used by _SWISS protocol_ (report collected data to ISE)
        + Required for _ISE discovery_ and _NAC Agent update_
    + ISE no longer uses legacy port 8906 for SWISS protocol

## Posture Services

+ Posture Services - Status
    + Posture status options for an endpoint
        + __Unknown__: no data was collected from the endpoint
            + Usually means NAC Agent is not installed
            + Could be that it is not running or does not have ISE connectivity
        + __Noncompliant__: at least one requirement is not satisfied
            + Remediation process can be started automatically
        + __Compliant__: all requirements are satisfied
    + Posture status is used as condition in authorization policies
        + Network access is thus granted based on the health / security state of the endpoint

+ Posture Assessment Work Flow: How AAA order of processing is changed
    + Supplicant Authentication
    + Initial Authorization Policy pushed (posture status Unknown)
    + Posture Discovery and Assessment starts
        + Posture data is received by ISE from NAC Agent
        + Posture state is changed to Compliant or Noncompliant
    + ISE triggers CoA requesting endpoint re-authentication
    + Supplicant Authentication same as in first step
        + Intermediate authorization is applied if posture status is Noncompliant
        + Remediation starts, fixes problems, posture status changes to Compliant
    + ISE triggers CoA requesting endpoint re-authentication
    + Final authorization is applied if posture status is Compliant
    + Posture flow Pre ISE 2.2 & in ISE 2.2
        <a href="https://www.cisco.com/c/en/us/support/docs/security/identity-services-engine-22/210523-ISE-posture-style-comparison-for-pre-and.html">
            <br/><img src="https://www.cisco.com/c/dam/en/us/support/docs/security/identity-services-engine-22/210523-ISE-posture-style-comparison-for-pre-and-00.png" alt="Posture flow Pre ISE 2.2" width="800">
            <br/><img src="https://www.cisco.com/c/dam/en/us/support/docs/security/identity-services-engine-22/210523-ISE-posture-style-comparison-for-pre-and-05.png" alt="Posture flow in ISE 2.2" width="800">
        </a>

+ Posture Configuration Steps on Supplicant
    + Install NAC Agent
        + Ideally, provision the FQDN of ISE PSN, to avoid ISE dynamic discovery
        + FQDN automatically provisioned if Agent installed via CPP
    + ISE Discovery process
        + HTTP discovery probe on port 80 to ISE PSN, if configured
        + HTTPS discovery probe on port 8905 to ISE PSN, if configured
        + HTTP discovery probe on port 80 to default gateway
        + HTTPS reconnect probe on 8905 to previously contacted ISE PSN
    + To avoid endpoint being quarantined for remediation
        + Ensure endpoint satisfies security policies configured on ISE

+ Posture Configuration Steps on NAD
    + NAD is not aware of the posture process
    + NAD just receives authentication status and authorization to be applied from ISE
    + Allow NAC Agent connectivity with ISE
        + Requires static pre-authentication ACL

+ Posture Configuration Steps on ISE
    + CoA is enabled by default for posture assessment
    + Configure posture policies
        + Per operating system
        + Per group of users
    + Configure authorization policies with posture status as condition
        + For Unknown status, redirect to client provisioning portal
        + For Noncompliant status, restrict access for remediation to work
        + For Compliant status, grant network access as desired
    + Optionally configure client provisioning policies
        + Only when NAC Agent has not been pre-deployed
        + Required downloading of NAC Agent and compliance module to ISE


## Posture Configuration

+ Topology
    <br/><img src="./diagrams/sisas-net0.png" alt="Network Topology - Complete" width="450">

+ Demo: Reset Network Back to Basic Config
    + Purpose: ensure connectivity and authentication between PC-B & SW3
    + SW1 Config:
        ```cfg
        show run int f1/0/5
        ! interface FastEnthernet 1/0/5
        !   switchport access vlan 81
        !   switchport mode access
        !   switchport voice vlan 80
        !   logging event spanning-tree
        !   authentication host-mode multi-domain
        !   mab
        !   dot1x pae authenticator
        !   spanning-tree portfast
        ! end
    + PC-B: 
        + NIC > Properties > Authentication: Enable IEEE 802.1x authentication, Network authentication method=PEAP (outer method)
        + PEAP Settings (Outer method): Validate server certificate, Trust Root Certificate Authorities=inelab-CA, Authentication Method=smart card or other certificate
        + Configure (Inner method): user certificate on this computer, use simple certificate selection, validate server certificate, Trust Root Certificate Authorities=inelab-CA

    + SW3 Config:
        ```cfg
        show run int gi1/0/5
        ! interface GigabitEthernet1/0/5
        !   switchport access vlan 90
        !   switchport mode access
        !   logging event spanning-tree
        !   spanning-tree portfast
        ! end

        conf t
        int gi1/0/5
          dot1x pae authenticator
          authentication port-control auto
        end
        ```
    + ISE Config
        + Policy > Authentication > MAB > edit (Insert New Rule Below): Name=PEAP_WIRED_AUTH, Conditions=(Wired_802.1x), Allowed Protocols=PEAP_EAP_TLS, Use=INE_PKI_STORE
        + Policy > Authorization > MAB_DATA_VLAN: Conditions=Wired_MAB, Permissions=DATA_VLAN_90
    + PC-B" NIC > enable

+ Demo: Posture Config
    + ISE Config:
        + List of Posture Conditions: Policy > Policy Elements > Conditions > Posture: File Condition/Registry Condition/Application Condition/Service Condition/Compund Condition/AV Compund Condition/AS Compound Condition/Dictionary Simple Condition/Dictionary Compound Condition/
        + Policy > Policy Elements > Conditions > Posture > Application Conditions > Add: Name=APP_COND_ISO, Process Name=pPoerISO.exe, OS=Windows All > Save > Submit
        + Policy > Policy Elements > Conditions > Posture > Remediation > Add: Name=APP_REM_ISO, Remediation Type=Automatic, Program Installation Path=v:\Program Files\PoerISO\powerios.exe > Add > Submit
        + Policy > Policy Elements > Results > Posture > Requirements > default > edit: Name=POSTURE_TEST, OS=Windows All, Conditions=APP_COND_ISO, Remediation Action=APP_REM_ISO

+ Demo: Client Provision Policy
    + SW3 Config
        ```cfg
        show run | i aaa|rdius
        ! aaa new-model
        ! aaa authentication dot1x default group radius
        ! aaa authorization network default group radius
        ! aaa accounting dot1x default group radius
        ! aaa server radius dynamic-author
        !   client 172.16.3.100 server-key radiuskey
        ! aaa session-id common
        ! ip radius server-interface Loopback0
        ! radius-server host 172.16.3.100 key sw1radius
        ! radius vsa send accounting
        ! radius vsa send authentication
        ```
    + ISE ACL: Policy > Pilicy Elements > Results > Authorization > Authorization Profile > POST_UNK_PROFILE: Access Type=ACCESS_ACCEPT, DACL Name=POST_UNK_DACL, web redirection=(Client Provisioning (Posture) ACL POST_REDIR_ACL)
    + SW3 conf:
        ```cfg
        conf t
        ip access-list extended POST_REDIR_ACL
          permit udp any any eq bootps
          permit udp any host 172.16.20.100 eq 53
          permit tcp any host 172.16.3.100 eq 8443
          permit tcp any host 172.16.3.100 eq 8909
          permit tcp any host 172.16.3.100 eq 8905
          permit udp any host 172.16.3.100 eq 8909
          permit udp any host 172.16.3.100 eq 8905
          permit ip any any
        exit
        do show access-list POST_REDIR_ACL
        end
        show authentication sessions    ! 0A0A0A0A0A00000024028A282C
        clear authentication session 0A0A0A0A0A00000024028A282C
    + PC-B: IE (http://172.16.3.100) -> timeout
    + SW3 Verification:
        ```cfg
        show authentication sessions
        ! URL Redirect ACL=xACSACLx-IP-POST_UNK_DACL_56a2c225

        show ip access-lists xACSACLx-IP-POST_UNK_DACL_56a2c225
        ! Extended IP access list xACSACLx-IP-POST_UNK_DACL_56a2c225 (per user)
        !   10 permit udp any any eq bootps
        !   20 permit tcp any host 172.16.3.100 eq 8443
        !   30 permit tcp any host 172.16.3.100 eq 8905
        !   40 permit udp any host 172.16.3.100 eq 8905
        !   50 permit tcp any host 172.16.3.100 eq 8909
        !   60 permit udp any host 172.16.3.100 eq 8909
        !   70 permit upd any host 172.16.20.100 eq domain

        show ip access-list POST_REDIR_ACL
        ! Extended IP access list POST_REDIR_ACL
        !   10 permit udp any any eq bootps
        !   20 permit udp any host 172.16.20.100 eq 53
        !   30 permit tcp any host 172.16.3.100 eq 8443
        !   40 permit tcp any host 172.16.3.100 eq 8909
        !   50 permit tcp any host 172.16.3.100 eq 8905
        !   60 permit udp any host 172.16.3.100 eq 8909
        !   70 permit udp any host 172.16.3.100 eq 8905
        !   80 permit ip any any
        ```
    + PC-B: chrome (http://172.16.20.100) -> This page is not available
    + ISE Verification: Administration > Web Portal Management > Setting > General > Ports: Guest Portal and Client Provisioning Portal Settings=(HTTPS=8443)
    + PC-B requests received by ISE and response with GUI but not displayed properly on Browser
    + SW3:
        ```cfg
        conf t
        int gi1/0/5
          shut
          no shut
        ^Z
        show authentication sessions                    ! status=Authz Success
        show authentication sessions int gi1/0/5        ! PSOT_REDIR_ACL
        ```
    + PC-B: chrome (http://172.16.20.100) -> Not displaed; IE (http://172.16.20.100) -> This page can't be displayed.
    + ISE: 
        + Policy > Policy Elements > Results > Client Provisioning > Resources: NACAgent 4.9.0.52
        + Client Provision Tab: Rules=Windows, OS=Windows All, Results=NCAgent > Done
    + PC-B: IE (http://10.10.10.10) -> This page can't be displayed.; Chrome (http://172.16.20.100) -> Cannot be displayed
    + ISE: Posture Policy: Name=TEST_POLICY, OS=Windows All, Conditions=(), Requirements=POSTURE_TEST
    + SW3: `conf t, int gi1/0/5, shut, no shut, end` 
    + PC-B: Chrome (http://10.10.10.10) -> Cannot be displayed
    + Conclusion: No idea what happened, maybe ISE bug, Pkts returned w/o payload for GUI

+ Demo: CoA Messages
    + PC-B: Cisco NAC Agent > Discover Host=172.16.3.100 > Apply > ... > Full Network Access
    + SW3 Msgs: EPM-6-POLICY-APP-SUCCESS: ... | POLICY_NAME xACSACLx-IP-POST_COMP_DACL-256a2c31c
    + ISE (Create policy again that was not saved): Policy > Posture: Name=APP_POSTURE, OS=Windows All, Requirements=POSTURE_TEST > Save
    + PC-B: logoff > logon
    + SW3: expect to see Noncompliant status
        ```cfg
        ! EPM-6-APP_SUCCESS: ... | POLICY_NAME xACSACLx-IP-POST_UNK_DACL-56a2c225
        show authentication sessions int gi1/0/5
        ! ACS ACL=xACSACLx-IP-POST_UNK_DACL-56a2c225, URL Redirect ACL=POST_REDIR_CL
        ! URL Redirect=https://ISE1-12.inelab.local:8443/guestportal/getway?sessionId=0A0A0A0A0A0000003502F663F1&action=cpp
    + PC-B: ANC Agent > Temporary Network Access > Full Network Access
    + ISE: Operations > Authentication: Authentication Profiler=POST_COMP_PROFILE > details: Authorization Profile=POST_COMP_PROFILE, AuthorizationPolicyMatchedRule=POST_COMPLAINT, Posture status=Compliant




