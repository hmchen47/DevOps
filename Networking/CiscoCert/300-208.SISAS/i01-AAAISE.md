# AAA and ISE Concepts

## AAA Model

+ What is AAA?
    + AAA stands for
        + Authentication (AuthN)
        + Authorization (AuthZ)
        + Accounting
    + AAA can be used for multiple purposes
        + Network Device administration
        + Network Access (wired, wireless, VPN)
    + Authentication
        + Provide identification of who you are
        + Various options: username and password , certificates
    + Authorization
        + Defines what you are allowed to do
        + For network administration:
            + privilege-level
            + Allowed commands
        + For network access:
            + VLAN
            + Access-list (ACL)
            + Security Group Tag (SGT)
            + Encryption
    + Accounting
        + Provides evidence of what you have done, like auditing
        + For network administration: Typed commands for forensics analysis
        + For network access:
            + Session statistics for billing
            + Session identification (MAC address, IP address, username)
            + Session state (connected or disconnected)

+ AAA Model: Three-party authentication model
    + Supplicant / end-client
        + Device requesting access
        + Speaks with the authenticator
    + Authenticator
        + Device enforcing the authentication , known as NAD
        + Bridges information between supplicant and authentication server
    + Authentication Server
        + Device performing the authentication
        + Connected to identity sources: username/password, PKI
        + Can behave like a proxy towards another authentication server

        <br/><img src="https://upload.wikimedia.org/wikipedia/commons/1/1f/802.1X_wired_protocols.png" alt="802.1X authentication" width="450">


+ AAA Protocols
    + Between supplicant and authenticator
        + For device administration
            + console
            + Telnet / SSH
            + HTTP / HTTPS
        + For network access
            + EAPOL
            + HTTP / HTTPS
    + Between authenticator and authentication server
        + RADIUS
        + TACACS+


## RADIUS and TACACS+

+ RADIUS
    + IETF standard (RFC2865)
        + Has additional RFC’s for specific features
        + Combines authentication and authorization in one process
        + Uses UDP port 1645/1812 for authentication
        + Uses UDP port 1646/1813 for accounting
        + Initial ports of 1645/1646 were also used by datametrics service
        + RADIUS key with MD5 used to hide the user’s password
    + Performs its scope via RADIUS attributes
        + IETF standard defined
        + Vendor Specific Attributes (VSA’s)

+ TACACS+: Developed by Cisco
    + Mainly used for device administration
    + Developed by Cisco from original TACACS protocol (RFC1492)
    + Uses separate processes for authentication, authorization and accounting
    + Uses TCP port 49
    + Encrypts entire body of TACACS packet, leaves clear-text header

+ [TACACS+ and RADIUS Comparison](https://www.cisco.com/c/en/us/support/docs/security-vpn/remote-authentication-dial-user-service-radius/13838-10.html?dtid=osscdc000283): TACACS+ vs RADIUS Traffic
    <br/><img src="https://www.cisco.com/c/dam/en/us/support/docs/security-vpn/remote-authentication-dial-user-service-radius/13838-10-01.gif" alt="TACACS+ Traffic Example" width="350"> &nbsp;&nbsp;
    <img src="https://www.cisco.com/c/dam/en/us/support/docs/security-vpn/remote-authentication-dial-user-service-radius/13838-10-02.gif" alt="RADIUS Traffic Example" width="350">


## Cisco’s Authentication Servers

+ Access Control System (ACS)
    + Supports both TACACS+ and RADIUS
    + Mainly used for TACACS+
+ Identity Services Engine (ISE – NGN RADIUS)
    + Supports RADIUS with Change of Authorization (CoA)
    + TACACS+ supported in ISE 2.0
    + Mainly used for RADIUS
    + Additional features not supported by ACS
        + Profiling , posture assessment
        + Web portal services

## ISE Concepts

+ What is ISE ?
    + Provides a scalable and unified network access policy platform
    + Centralized network access policy for any device, from anywhere, at anytime
        + Wired access
        + Wireless access
        + VPN access
    + Implements a flexible policy-based model
        + Rule-based approach for authentication and authorization
        + Rules are composed of conditions and results

+ ISE Personas
    + It supports both physical and virtual environments
    + Built of three major roles, named __personas__
        + PSN (Policy Service Node)
            + Responsible for network access request processing
                + RADIUS, posture, profiling, web redirection, guest portal
        + PAN (Policy Administration Node)
            + Responsible for all configurations
                + Conditions, results, policies, external identity store integration
        + MnT (Monitoring and Troubleshooting Node)
            + Collects logs from PAN, PSN, NAD

+ ISE Deployment Modes
    + All personas residing on the same entity
    + Personas are distributed for scalability or design requirements
        + Multiple PSN’s
        + 2 PAN’s (one active, one standby)
        + 2 MnT’s (one active, one standby)

+ ISE Architecture
    + Everything circles around two types of policies
        + Authentication policies, processed first
        + Authorization policies, processed second
    + Inbound AAA request flow
        + Authentication policy matching
            + Single or rule-based policy
                + Single model does not allow defining conditions
        + Rules are processed top-down until first match
            + Action “drop” means play dead, no RADIUS message sent back to NAD
            + Action “continue” means act like authentication was successful, inspect authorization policies
        + Authorization policy matching
            + Standard and exception policies
                + Exception policies are processed before standard policies
            + Rules are processed top-down until first match by default
                + Optionally multiple-rules can be matched with actions being combined
                    + Access-Accept takes precedence over Access-Reject
    + Authentication policies <br/>
        Based on configured conditions each request matches a rule
        + Request is routed over to configured Identity Store or Identity Sequence
        + Identity is validated
        + Actions: 
            + Success: token passed over to Authorization policies
            + Failed: send Access-Reject or actions configured
    + Authorization policies
        + Only processed if authentication passed
            + Successful or by the explicit “continue” action
        + Based on configured conditions each request matches a rule: On match, Access-Accept is issued and optional authorization attributes sent
            + ACLs (dACL, filter-ID ACL, per-user ACL, airespace ACL)
            + ddata VLAN and voice VLAN permission
            + MACSec and URL Redirection (with Redirect-ACL)
    + ISE Communication Model
         <a href="http://thenetworksurgeon.com/cisco-identity-services-engine-part-1-overview/">
            <br/><img src="http://thenetworksurgeon.com/wp-content/uploads/2013/10/ISE_Communication.png" alt="ISE Communication Model" width="450">
         </a>

+ ISE Authentication Policy: Authentication Policy format
    + If _condition_: Identify the RADIUS packet based on RADIUS attributes
    + Then _allowed protocols_: Which authentication protocol can be used by the supplicant
    + And _validate credentials_: Which identity source can be queried for authentication

+ ISE Authorization Policy: Authorization Policy format
    + If _condition_: Identify the RADIUS session or supplicant by profiling
    + And optionally if used _identity store_: Store of user credentials
    + Then apply _authorization profile_:  User/device authorization

+ ISE Feature Flow
    <a href="https://smbitsolutions.wordpress.com/2012/07/12/cisco-identity-services-engine/">
        <br/><img src="https://smbitsolutions.files.wordpress.com/2012/07/image017.jpg" alt="ISE Feature Flow" width="600">
    </a>

## ISE Management 

+ [Basic Cisco ISE 2.3 VM Installation](https://zigbits.tech/zigbits-cisco-ise-2-3-blog-series-episode-01-basic-cisco-ise-2-3-vm-installation/)

+ Sample Screenshot w/ ISE 2.3
    <br/><img src="https://i2.wp.com/zigbits.tech/wp-content/uploads/2017/11/ZBISE02-2-26.png" alt="Server Certificate" width="800">


+ General GUI
    + Home: Statistics
        + Summary
        + Alarms
        + Profiler Activity
        + Authentications
    + Operations: Monitoring & Troubleshooting (MnT)
        + Authentication
        + Reports -> Most shown in Home page
        + Endpoint Protection Services
        + Troubleshooting: Diagnostic Tools & Download Logs
    + Policy: Authentication & Authorization Policies
        + Authentication conditions & results
        + Authorization conditions & results
        + Posture
        + Profiling
        + Client Provisioning
        + Security Group Access: Egress  Policy & Network Device Authentication
        + Policy Elements: Dictionaries, Conditions, Results
    + Administration
        + System: Deployment, Licensing, Certificates, Logging, Maintenance, Backup & Restore, Admin Access, Settings
        + Network Resources: Network Devices, Network Device Groups, External RADIUS Servers, RADIUS Server Sequences, SGA AAA Servers, NAC Managers, MDM
        + Free Service: Profiler
        + Identity Management: Identities, Groups, External Identity Sources, Identity Source Sequences, Settings
        + Web Portal Management: Sponsor Group Policy, Sponsor Groups, Settings

## ISE Authentication Policies

+ Policy > Authentication Policy
    + Default: Rule-based (entry list)
        + MAB policy: 1st
        + Dot1x: 2nd
        + Default Rule (if no match): 3rd
    + Build Authentication Policy - Simple
        + Network Access Service: what protocol supplicant can use
        + Identity Source: which identify store does ISE validate supplicant credential, eg. local db, RADIUS, etc.
    + Policy Type
        + Simple: no condition allowed
        + Rule-based fields:
            + Rule name
            + if condition (Policy > Policy Elements > AuthN: )
            + then allowed protocols (Policy > Policy Elements > Conditions: )
            + Use: results (credentials - Identity Store/Identity Sequence)



