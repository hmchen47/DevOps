# Identity Services Engine (ISE)

+ Create a Lab and Practice
    + Windows Server with AD
    + Identity Services Engine (ISE) [version 1.2]
    + Cisco AnyConnect uite (NAM _ VPN)
    + Cisco Switch
    + Client PCs

+ Identity Services Engine (ISE)
    + AD Implemented - Hacker
        + Backtrack
        + Kali Linux
    + Prevent dynamic negotiation with VLAN trunk
    + 802.1X Components
        + Supplicant: supply credentials
        + Authenticator/NAD
        + Authentication Server: ACS (Access Control Server), ISE 1.2

+ Installing ISE:
    + VMWare Workstation / ESXi
    + 200GB+ (Thin Provision - dynamic allocation)
    + 4GB RAM
    + IP = 192.168.1.117
    + username=admin, pwd = Nugget!23

+ ISE GUI
    + Administration -> Administration Persona, PAN (Administration Node)
        + Systems: 
            + Deployment - Profiling Configuration: Netflow, DHCP, DHCPSPAN, HTTP, RADIUS, Network Scan (NMAP), DNS, SNMPQUERY, SNMPTRAP
            + Licensing
            + Certificates
            + Logging
            + Maintenance
            + Backup and Restore
            + Admin Access
            + Settings: Client Provisioning, Endpoint Protection Service, FIPS Mode, Alarm Settings, _Posture_, _Profiling_, _Protocols_, Proxy, Security Groups Access, _SMTP Server_ , System Time, Policy Set
        + Network Resources
            + Network Device
            + Network Device Groups
            + External RADIUS Servers
            + RADIUS Server Sequences
            + SGA AAA Servers
            + NAC Managers
            + MDM (Mobile Device Manager)
        + Identity Management
            + Identities: Users, Endpoints, Latest Manual Network Scan Results
            + Groups
            + External Identity Sources: Certificate Authentication Profile, Active Directory, LDAP, RADIUS Token, RSA SecureID
            + Identity Source Sequences
            + Settings
        + Web Portal Management
            + Sponsor Group Policy
            + Sponsor Groups
            + Settings
                + General: Portal Theme, Ports, Purge
                + Sponsors: Authentication Source, Language Template
                + My Devices
                + Guest: Detail Policy, Guest Role Configurations, Language Template, Multi-portal Configurations, Portal Policy, Password Policy, Time Policy, Username Policy
    + Policy -> Policy Service Persona, PSN (Policy Service Node)
        + Authentication
        + Authorizations
        + Profiling
        + Posture
        + Client Provisioning
        + Security Group Access
            + Egress Policy: Source Tree, Destination Tree, Matrix
            + Network Device Authorization
        + Policy Elements
            + Dictionaries
            + Conditions
            + Results
                + Authentication
                + Authorization: Authorization Profiles, Downloadable ACLs, Inline Posture Node Profiles
                + Profiling: Profiling Policies, Logical Policies
                + Posture: Remediation Actions (AS, AV, file, launch program, link, Windows server update service, Windows update), Requirements
                + Client Provisioning - Resource: Cisco Site, Local disk, ISE Posture Agent Profile, Native Supplicant Profile
                + Security Group Access: Security Group ACLs, Security Groups, Security Group Mappings

    + Operations -> Monitoring and Troubleshooting, MnT Persona
        + Authentications
        + Reports
        + Endpoint Protection Source
        + Troubleshoot
            + Diagnostic Tools
            + Download Logs

+ Admin Portal
    <a href="https://www.cisco.com/c/en/us/td/docs/security/ise/1-2/user_guide/ise_user_guide/ise_ui_intro.html">
        <br/><img src="https://www.cisco.com/c/dam/en/us/td/i/300001-400000/300001-310000/303001-304000/303287.tif/_jcr_content/renditions/303287.jpg" alt="Admin portal" width="450">
    </a>
    | Item | Name | Functions |
    |------|------|-----------|
    | 1 | Menu Bar | Access tools for viewing, monitoring, and managing different Cisco ISE options: <br/>  • Home: Access the dashboard, which is a real-time view of all the services running in the Cisco ISE network. <br/> • __Operations__: Access tools for monitoring real-time alarms and live authentications, querying historical data through reports, and troubleshooting network services. <br/> • __Policy__: Access tools for managing network security in the areas of authentication, authorization, profiling, posture, and client provisioning. <br/>       • __Administration__: Access tools for managing Cisco ISE nodes, licenses, certificates, network devices, users, endpoints, and guest services. |
    | 2 | Top Right Panel | View the connected Cisco ISE node. Click the appropriate options to edit account information, log out, and provide feedback to Cisco. |
    | 3 | Search | Search for endpoints and display their distribution by profiles, failures, identity stores, location, device type, and so on. |
    | 4 | Setup Assistant | Access wizard to create a basic configuration to demonstrate Cisco ISE feature functionality in your network. |
    | 5 | Context-Sensitive Help | Access help for the currently displayed page. |
    | 6 | Help | Access the complete Cisco ISE online Help system and the Task Navigator, which provides visual guides for navigating through procedures whose tasks span multiple screens. |
    | 7 | Notifications | Hover the mouse cursor over this option to view a summary of notifications. |

+ Demo: ISE Basic Settings
    + Create Group: Administration > Network Resources-Network Device Groups > Groups > All Location > Add: Name=Nuglabs-Vegas
    + Add Network Device: Administration > Network Resources-Network Device > Add: Name=SW1, IP=192.168.1.121/32, Location=Nugget-Vegas, Authentication Settings=(Shared Secret=Nugget!23) > Submit
    + Create User: Administration > Identity Management > Identities > Users > Add: Name=it-bob, pwd=Nugget!23

+ Demo: Switch Basic Settings - SW1
    ```cfg
    show ip int brief | exclude unasssigned
    ! Vlan 1 = 192.168.1.121

    ping 192.168.1.121  ! Basic connectivity
    conf t
    aaa new-model
    aaa authentication login default eanble
      enable secret Nugget!23
    radius server ISE
      address ipv4 192.168.1.117 auth-port 1812 acct-port 1813
      key Nugget!23
    exit

    radius-server vsa send authentication
    radius-server vsa send accounting

    ip device tracking
    end

    debug radius
    test aaa group ISE-group bob Nugget!23 new-code
    ! RADIUS(00000000): Request timeout
    ```

+ Demo: TRBL
    + ISE Network Device IP Address: Administration > Network Resource - Network Devices > SW1: IP = 192.168.1.121
    + SW1 Verification: `ping 192.168.1.117` - Failed
    + ISE CLI: user=admin, pwd=Nugget!23 > `ping 192.168.1.121` - ok
    + SW1 Verification: 
        ```cfg
        ping 192.168.1.117                                  ! Connectivity w/ ISE ok
        test aaa group ISE-group bob Nugget!23 new-code     ! User successfully authenticated
        ```
    






