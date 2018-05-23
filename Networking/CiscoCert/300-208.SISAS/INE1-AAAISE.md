# AAA and ISE Concepts

## AAA Terminology

+ What is AAA ?
    + AAA stands for
        + Authentication
        + Authorization
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
            + Access-list
            + Security Group Tag
            + Encryption
    + Accounting
        + Provides evidence of what you have done, like auditing
        + For network administration:
            + Typed commands for forensics analysis
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


## RADIUS vs. TACACS

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

+ TACACS+
    + Developed by Cisco
        + Mainly used for device administration
        + Developed by Cisco from original TACACS protocol (RFC1492)
        + Uses separate processes for authentication, authorization and accounting
        + Uses TCP port 49
        + Encrypts entire body of TACACS packet, leaves clear-text header
    + [RADIUS vs. TACACS](http://www.cisco.com/c/en/us/support/docs/security-vpn/remoteauthentication-dial-user-service-radius/13838-10.html)

+ Cisco’s Authentication Servers
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

## ISE Fundamentals

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
    + Built of three major roles, named personas
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
    + Authentication policies
        + Based on configured conditions each request matches a rule
            + Request is routed over to configured Identity Store or Identity Sequence
            + Identity is validated
            + If successful authentication, token is passed over to Authorization policies
                + Otherwise send Access-Reject or actions configured for authentication failure+ 
    + Authorization policies
        + Only processed if authentication passed
            + Successful or by the explicit “continue” action
        + Based on configured conditions each request matches a rule
            + On match, Access-Accept is issued and optional authorization attributes sent
                + ACL (dACL, filter-ID ACL, per-user ACL, airespace ACL)
                + dVLAN and voice VLAN permission
                + MACsec and URL Redirection (with Redirect-ACL)

+ ISE Authentication Policy: Authentication Policy format
    + If condition
        + Identify the RADIUS packet based on RADIUS attributes
    + Then allowed protocols
        + Which authentication protocol can be used by the supplicant
    + And validate credentials
        + Which identity source can be queried for authentication

+ ISE Authorization Policy: Authorization Policy format
    + If condition
        + Identify the RADIUS session or supplicant by profiling
    + And optionally if used identity store
        + Store of user credentials
    + Then apply authorization profile
        + User/device authorization




