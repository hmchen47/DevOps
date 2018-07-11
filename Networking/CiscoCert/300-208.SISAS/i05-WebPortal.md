# Layer 3 Authentication – HTTP / HTTPS

## Layer 3 Authentication

+ About Layer 3 Authentication
    + Performed through HTTP/HTTPS by redirecting users to a web portal
        + not supported for machine authentication, only for user authentication
    + Portal can reside on the NAD (switch, WLC)
        + Named __Local Web Authentication (LWA)__
        + Rarely implemented because it is decentralized
    + Portal can reside on the ISE
        + Named __Central Web Authentication (CWA)__
        + Widely deployed as it is centralized
    + User / supplicant requires IP address to complete the process
        + Starting with IOS code 12.2(55)SE, switch enforces by default an ACL on the port, which allows DHCP traffic, named Auth-Default-ACL
        + Otherwise static pre-authentication ACL needs to be deployed
    + In both LWA and CWA
        + Authentication is performed by the RADIUS server
    + It is supported for wired and wireless access
        + Not for VPN access yet
        + For VPN, both ISE and VPN gateway need to support it
    + Use-cases
        + Mainly deployed for visitors, guest services
        + Required for Bring Your Own Device implementation
            + Alternative to Enterprise Mobility Management solution
            + Supported only in CWA mode

+ Local Web Authentication
    + Enterprise assets will perform MAB or 802.1x in general
        + Also known as standalone web authentication
        + Makes use of authentication-proxy service via HTTP
        + MAB and 802.1x will thus also be enabled in most cases
        + LWA will be used as a fallback method on the switch port
            + Because you never know who connects on a switch port, employee or guest
            + Can be used as the single authentication method, but rarely deployed
    + Authorization restriction
        + Does not support VLAN assignment, mainly because CoA is not supported in this deployment
        + Per-user ACL not supported, instead use proxy-ACL
        + same concept, still uses VSA’s, but different ACL syntax
    + Message Flow: WLC with Local WebAuth Non-Posture Flow
    <a href="https://www.cisco.com/c/en/us/td/docs/security/ise/2-1/admin_guide/b_ise_admin_guide_21/b_ise_admin_guide_20_chapter_01110.html">
        <br/><img src="https://www.cisco.com/c/dam/en/us/td/i/300001-400000/370001-380000/373001-374000/373351.eps/_jcr_content/renditions/373351.jpg" alt="WLC with Local WebAuth Non-Posture Flow" width="600">
    </a>
    + Wired NAD with Local WebAuth Process
        1. Cisco ISE requires a login.html file with the HTML redirect to be uploaded to the NAD. This login.html file is returned to the browser of the guest device for any HTTPS request made.
        2. The browser of the guest device is redirected to the Guest portal where the guest’s login credentials are entered.
        3. After the Acceptable Use Policy (AUP) and change password are processed, both of which are optional, the Guest portal redirects the browser of the guest device to post the login credentials on the NAD.
        4. The NAD makes a RADIUS request to the Cisco ISE RADIUS server to authenticate and authorize the guest.

+ LWA Configuration Steps on Supplicant
    + No Configureation Required
        + Just a browser, because LWA is not a authentication protocol
        + It is just a web authentication method
        + There is no negotiation between supplicant and NAD
        + NAD just intercepts HTTP/HTTPS sessions from supplicantb and redirects user to the web portal
        + NAD requires a layer 3 address (SVI) for this to work
    + Device Requirements
        + IP address
        + DNS resolution required for redirection-URL

+ LWA Configuration Steps on NAD
    + Enable AAA: `aaa new-model`
    + Configure login default authentication list: `aaa authentication login default group`
    + Define LWA profile: 
        + `ip admission name <auth_name> proxy http`
        + `fallback profile <profile_name>`
        + `ip admission <auth_name>`
    + Enable LWA on switch port facing the user
        + `authentication order webauth`
        + `authentication fallback <profile_name>`
    + Enable device tracking and HTTP/HTTPS server
        + `ip device tracking`
        + `ip http server`
        + `ip http secure-server`
    + Enforce authentication on switch port facing the supplicant: `authentication port-control auto`
    + Define RADIUS server settings: `radius-server host <IP> key <radius key>`
    + Optionally configure other global/interface level settings
        + RADIUS Service-Type will be Outbound
        + In most IOS codes, it is not being send in the RADIUS Access-Request message, without command `radius-server attribute 6 on-forlogin-auth`
        + `radius-server attribute 6 on-forlogin-auth`: Only if NAD to send Access-Request messages to RADIUS server, which including the command for outbound; for web authentication

+ LWA Configuration Steps on ISE
    + Configure RADIUS integration with NAD
    + Configure authentication policy
        + Possibly match on RADIUS Service-Type to make the policy unique
    + Configure authorization policy
    + Optionally integrate with External Servers for authentication
    + Otherwise define username/password in Local Users

+ Central Web Authentication Work Flow
    + Uses a two phase process
    + Phase 2 starts if user initiates HTTP / HTTPS traffic
    + Phase 1
        + Uses MAB authentication
        + MAB will fail, as ISE is not aware of client’s MAC address
        + ISE will be configured to authorize the client, even though it failed authentication
        + Continue action in authentication policy for failed authentication
        + Intermediate Authorization received from ISE will be
            + Redirect-ACL, in order to capture client’s HTTP / HTTP traffic for redirection
            + Redirect-URL, in order to redirect client to ISE portal
            + Optionally, ACL in order to restrict client’s network access
    + Phase 2
        + User is redirected to ISE’s web portal
        + It has to pass portal authentication via username/password
        + If authentication succeeds, ISE will send a RADIUS Change of Authorization (CoA) message to the NAD
        + As a result, NAD will perform a re-authentication of the client via MAB
        + Authentication will fail again, just like in Phase 1
        + Final authorization is received from ISE and applied by NAD on the port
        + Final authorization uses the special condition of `Network Access:Use Case Equals GuestFlow`
    + Procedure:
        <a href="https://www.juniper.net/documentation/en_US/junos/topics/concept/central-web-authentication-understanding.html">
        <br/><img src="https://www.juniper.net/techpubs/images/g043340.png" alt="Central Web Authentication Process" width="600">
        </a>
        1. A host connected to the switch (authenticator) initiates MAC RADIUS authentication.
        2. MAC RADIUS authentication fails. Instead of sending an Access-Reject message to the switch, the AAA server sends an Access-Accept message that includes a dynamic firewall filter and a CWA redirect URL.
        3. The host is allowed by the terms of the filter to send DHCP requests.
        4. The host receives an IP address and DNS information from the DHCP server. The AAA server initiates a new session that has a unique session ID.
        5. The host opens a Web browser.
        6. The authenticator sends the CWA redirect URL to the host.
        7. The host is redirected to the CWA server and is prompted for login  credentials.
        8. The host provides the username and password.
        9. After successful Web authentication, the AAA server sends a CoA message to udpate the filter or VLAN assignment applied on the controlled port, allowing the host to access the LAN.
        10. The authenticator responds with a CoA-ACK message and sends a MAC RADIUS authentication request to the AAA server.
        11. The AAA server matches the session ID to the appropriate access policy and sends an Access-Accept message to authenticate the host.


+ RADIUS CoA
    + Per RADIUS RFC
        + Request is always initiated by the NAD
        + NAD is the RADIUS client and ISE is the RADIUS server
    + CoA is a RADIUS extension defined in RFC 3576
        + Allows the RADIUS server to initiate a RADIUS request
        + Uses UDP 1700 per Cisco, can be changed to UDP 3799 for RFC compliance
    + CoA common uses-cases
        + Central Web Authentication
        + Profiling and Posture assessment
        + External triggers like SIEM and MDM/EEM
    + CoA messages are reliable (always acknowledged)
        + NAS issues a CoA-Request
        + NAD replies with CoA-ACK or CoA-NAK
    + CoA common instructions
        + Request the NAD to re-authenticate the endpoint
        + Request the NAD to terminate the session (port bounce)
    + CoA instructions use Cisco AV Pair
        + `subscriber:command=disable-host-port` for port shutdown
        + `subscriber:command=bounce-host-port` for port bounce
        + `subscriber:command=reauthenticate` for re-authentication
    + CoA makes use of the RADIUS session-ID
        + Cisco VSA, part also of the URL Redirect
        + Session-ID is a HEX value generated by NAD when issuing the RADIUS authentication request
    + RADIUS Remote Network Element Configuration
        <a href="https://www.juniper.net/documentation/software/aaa_802/imsaaa11/sw-imsaaa-admin/html/Overview7.html">
        <br/><img src="https://www.juniper.net/documentation/software/aaa_802/imsaaa11/sw-imsaaa-admin/html/RADIUS-remote-network-element-configuration.gif" alt="RADIUS Remote Network Element Configuration"  width="600">
        </a>
    + NAD: SW3
        ```cfg
        show authentication sessions
        ! int=Gi1/0/5,  Mac Addr=48f8.b32e.2532, Method=dot1x, Domain=Data,
        ! Status=Running, Session-ID=88015B0A000000C7111F68CE
        

+ CWA Configuration Steps on Supplicant
    + No config required
        + Just an ISE supported browser, because CWA is not a authentication protocol
        + It is just a web authentication method
        + There is no negotiation between supplicant and NAD
        + NAD just intercepts HTTP/HTTPS sessions from supplicant and redirects user to the web portal
            + NAD requires a layer 3 address (SVI) for this to work
    + Device Requirements
        + IP address
        + DNS resolution required for redirection-URL

+ CWA Configuration Steps on NAD
    + Enable AAA: `aaa new-model`
    + Configure 802.1x default authentication list: `aaa authentication dot1x default group`
    + Configure authorization list, as Phase 1 always includes authorization: `aaa authorization network default group`
    + Enable MAB on switch port facing the supplicant: `mab [eap]`
    + Enforce authentication on switch port facing the supplicant: `authentication port-control auto`
    + Enable device tracking and HTTP/HTTPS server
        + `ip device tracking`
        + `ip http server`
        + `ip http secure-server`
    + Define RADIUS server settings: `radius-server host <IP> key <radius key>`
    + Configure CoA with the same RADIUS server: 
        + `aaa server radius dynamic-author`
        + `client <server_ip> server-key <string>`
    + Configure the redirect ACL on the switch (allow DHCP, DNS and ISE access on TCP port 8443)
    + Optionally configure other global/interface level settings

+ CWA Configuration Steps on ISE
    + Configure RADIUS integration with NAD
        + also for CoA
    + Configure authentication policy
        + MAB authentication rule to pass, even though authentication fails
    + Configure authorization policy for Phase1
        + Redirect-URL and Redirect-ACL
    + Configure authorization policy for Phase2
        + Optional, just Access-Accept is enough
    + Optionally integrate with External Servers for authentication
        + Otherwise define username/password as Guest Account

+ CWA Verification and Troubleshooting
    + Verification
        + `show authentication session`
        + `show authentication interface <if_number>`
        + `show aaa servers`
    + Troubleshooting
        + `show authentication session interface <if_number>`
        + `show epm session ip`
        + `show ip access-list interface`
        + `debug radius authentication`
        + `debug aaa coa`

## Phase 1 Configuration

+ Demo: Config CWA - Phase 1
    + Clear previous config on PC-B: Turn off 802.1x
        + run `service.msc` > Cisco AnyConnect > Stop
        + Verification: AnyConnect > Networks=Service Unavailable
    + SW3: 
        ```cfg
        show run int gi1/0/5
        ! interface GigabitEthernet1/0/5
        !   switchport access vlan 90
        !   switchport mode access
        !   logging event spanning-tree
        !   authentication open
        !   authentication port-control auto
        !   dot1x pae authenticator
        !   spanning-tree portfast
        ! end
        conf t
        int gi1/0/5
          no authentication open
          no dot1x pae wuthenticator
          mab
        exit

        ip http server
        ip http secure-server
        do show ip device tracking  ! Enabled
        
        aaa server radius dynamic-author
          do show run | i radius
          ! aaa authentication dot1x default group radius
          ! aaa authorization network default group radius
          ! aaa server radius dynamic-author
          ! ip radius source-interface Loopback0
          ! radius-server host 172.16.3.100 key radiuskey
          ! radius-server vsa send authentication

          client 172.16.3.100 server-key radiuskey
        exit
        int gi1/0/5
          shut
        exit
        ```
    + ISE Config:
        + Remove PC-B MAC addr from Endpoint MAC Store -> was manually added to test MAB w/ PC-B
        + Administration > Remove Linksys-Device > delete
        + Policy > Authentication > MAB (default entry): Conditions=(Wired_MAB OR Wireless_MAB), Allowed Protocols=Default Network Access, use=Internal Endpoints (edit: use=Internal Endpoints, If user not found = Contimue) [ behave like authentication is successful, continue inspecting authorization policies)]
        + Policy > Policy Elements > Results > Authorization > downloadable ACL > Add: Name=CWA_PHASE1_DACL, Content=(permit udp any any eq bootps, permit udp any host 172.16.20.100 eq 53, permit tcp any any eq 80, permit tcp any any eq 443, permit tcp any host 172.16.3.100 eq 8443) [dns=53, http=80, https=443, web portal=172.16.3.100] > Save > Submit
        + Policy > Authorization > Profiled Non Cisco IP Phone > edit (Insert New Rule Below): Name=CWA_PHASE1_PROFILE, Conditions=(Network Access:AuthenticationStatus Equals UnknownUser), Permission=CWA_PHASE1_PROFILE > Save
    + Verification:
        +  SW3: 
            ```cfg
            conf t
            int gi1/0/5
              shut
              no shut
            exit
            ip access-list extended CWA_REDIRECT_ACL
              permit tcp any any eq 80
              permit tcp any any eq 443
            exit
            int gi1/0/5
              shut
              no shut
            end
            
            show authentication sessions int gi1/0/5
            ! methpd=mab, status=Authz Success, Status=Authz Success, Authorized By=Authentication Server
            ! ACS ACL=xACSACLx-IP-CWA_PHASE1_DACL-56a17dd7, URL Redirect=CWA_REDIRECT_ACL, 
            ! URL Redirect=https://ISE1-12.inelab,local:8443/guestportal/gateway?session-Id=88015B0A000000CB117A5C91&action=cwa
            
            show ip access-lists CWA_REDIRECT_ACL
            ! Extended IP access list xACSACLx-IP-CWA_PHASE1_DACL-56a17dd7
            !   10 permit tcp any any eq 80
            !   20 permit tcp any any eq 443

            show ip access-list xACSACLx-IP-CWA_PHASE1_DACL-56a17dd7
            ! Extended IP access list xACSACLx-IP-CWA_PHASE1_DACL-56a17dd7
            !   10 permit udp any any eq bootps
            !   20 permit udp any host 172.16.3.100 eq domain
            !   30 permit tcp any any eq www
            !   40 permit tcp any any eq 443
            !   50 permit tcp any host 172.16.3.100 eq 8443

            show epm session ip 172.16.30,101
            ! Asmission feature=DOT1X, ACS ACL=xACSACLx-IP-CWA_PHASE1_DACL-56a17dd7
            ! URL_Redirect_ACL=CWA_REDIRECT_ACL, 
            ! URL Redirect=https://ISE1-12.inelab,local:8443/guestportal/gateway?session-Id=88015B0A000000CB117A5C91&action=cwa
            ```
        + PC-B: 
            + `nslookup`:- default network unknown
            + `ipconfig /all`: ip = 172.16.20.101, DNS server=172.16.20.100
            + `nslookup ise1-12.inelab.local`: addr = 172.16.3.100
            + IE (http://172.16.3.101): ok




## Phase 2 Configuration



## ISE Guest Services



## Bring Your Own Device (BYOD)



## Wi-Fi Deployments



## Portal Policy




