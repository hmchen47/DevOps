# TrustSec

## Layer 2 Encryption (MACSec)

+ Cisco TrustSec
    + Stands for Trusted Security
        + Consists of 802.1x, SGT and MACSec
        + SGT stands for Security Group Tags
        + MACSec stands for Mac Security (layer 2 encryption)
    + MACSec offers line-rate layer2 hardware-based encryption on a hop-by-hop basis
        + Host-to-switch
        + Switch-to-switch
    + MACSec is 802.1ae standard
        + GCM-AES-128 algorithm
        + EtherType value changed to 0x88e5
        + Supports SGT embedded inside CMD (Cisco Meta Data) – layer 2 header
    + MACsec Header Format
        <a href="https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/identity-based-networking-services/white-paper-c11-737544.html">
            <br/><img src="https://www.cisco.com/c/dam/en/us/products/collateral/ios-nx-os-software/identity-based-networking-services/white-paper-c11-737544.docx/_jcr_content/renditions/white-paper-c11-737544_4.jpg" alt="MACsec Header Format" width="450">
        </a>

+ MACSec Implementation Options
    + Host-to-switch (downlink)
        + Requires host to perform 802.1x authentication via EAP-TLS, PEAP or EAP-FAST
        + Native Windows supplicant does not support it
        + AnyConnect offers software based encryption
        + Negotiation and key derivation via MKA (MACsec Key Agreement) - Standard per the RFC 
    + Switch-to-switch (uplink)
        + Manual/static configuration
        + Negotiation and key derivation via SAP (Security Association Protocol) - Cisco proprietary based on 802.11i

+ MACsec Policy Enforcement
    + MACsec policy is enforced per port
        + __Must-not-secure__: do not negotiate MACsec
        + __Should-secure__ (default): negotiate MACsec, if failed allow clear-text traffic
        + __Must-secure__: negotiate MACsec, if failed do not allow clear-text traffic
    + Policy type received from ISE overrides locally configures settings on NAD
        + Local Should-Secure is overridden by ISE Must-Not-Secure
    + Based on host port mode, MACsec is
        + Fully supported with single-host and multi-domain
        + Partially supported with multiple-host, only first authenticated MAC address may negotiate MACsec
        + Not supported with multiple-authentication, because MACsec is point-to-point

+ MACsec Configuration Steps Supplicant 
    + Requires AnyConnect
    + Configure EAP-FAST with MacSec support

+ MACSec Key Agreement Protocol
    <a href="http://platinumway.biz/macsec-key-agreement-protocol#">
        <br/><img src="https://www.cisco.com/c/dam/en/us/products/collateral/ios-nx-os-software/identity-based-networking-services/deploy_guide_c17-663760.doc/_jcr_content/renditions/deploy_guide_c17-663760-05.jpg" alt="MACSec Key Agreement Protoco" width="450">
    </a>


+ MACsec Configuration Steps on NAD
    + Ensure 802.1x authentication requirements are configured
    + Enable MACsec on the switch port (downlink)
        + `macsec`
        + `mka default-policy`
    + Optionally define MACsec policies on switch port (downlink)
        + `authentication linksec policy`
        + `authentication event linksec fail action authorize vlan <vlan_nr>`
    + Enable MACsec on the switch port (uplink)
        + `cts manual`
        + `sap pmk <value> mode-list gcm-encrypt`

+ MACsec Configuration Steps on ISE
    + Ensure 802.1x authentication and authorizations are functional
    + Configure MACsec policy in the authorization profile

+ MACsec Verification and Troubleshooting
    + Verification
        + `show macsec summary`
        + `show macsec interface <if_nr>`
        + `show authentication session interface <if_nr>`
        + `show mka sessions interface <if_nr> detail`
        + `show mka default-policy detail`
        + `show cts interface summary`
        + `show cts interface if_nr>`
    + Troubleshooting
        + `debug radius authentication`
        + `debug macsec event`


## Security Group Tags (SGT)

+ What is SGT ?
    + A label / tag identifying a packet
    + How is it different than a VLAN tag ?
        + It is a tag used for security purposes
        + It identifies the context of the user, because it is assigned based on
            + How did the user access the network (How)
            + From which device did the user access the network (Where)
            + At what time did the user access the network (When)
            + Was the user’s device profiled (What)
            + What is the posture of the user’s machine (Who)
    + A tag associated to a user's pkts in the network is identified not only the but also the context of the user.
    + Layer 2 SGT Frame Format
    <a href="https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Borderless_Networks/Unified_Access/BYOD_Design_Guide/BYOD_Policy.html">
        <br/><img src="https://www.cisco.com/c/dam/en/us/td/i/200001-300000/290001-300000/293001-294000/293619.eps/_jcr_content/renditions/293619.jpg" alt="Layer 2 SGT Frame Format" width="600">
    </a><br/>

+ SGT Building Blocks
    + Classification
        + SGT assignment, always done at the network ingress point
        + Can be static or dynamic
    + Transport
        + Via inline tagging by the NAD
        + Via SXP protocol, a control-plane protocol
            + Used to propagate SGT across devices that do not support SGT inline tagging
            + Runs over TCP 64999
            + Connection can be unidirectional (speaker-listener)
            + Connection can be bidirectional, both devices can play both roles
            + GST Transport Mechanism
        <a href="https://www.slideshare.net/CiscoCanada/cisco-trustsec-security-group-tagging">
            <br/> <img src="https://image.slidesharecdn.com/policydefinedsegmentationwithtrustsec-robbleeker-140422114817-phpapp01/95/cisco-trustsec-security-group-tagging-27-638.jpg?cb=1398167397" alt="GST Transport Mechanism" width="600">
        </a>
    + Enforcement
        + Policy is applied via SGACL or SGFW

+ How does SGT help ?
    + Used to configure firewall rules: Restrict network access
    + Firewall rules
        + Configured on layer 3 switches, named SGACL
        + Configured on ASA firewall, named SGFW
        + Configured on IOS Zone-Based Firewall, named SGFW
    + Why is it better than regular firewall rules ?
        + The tag identifies much more than the user, it identifies the health state of the user/device
        + A user can have the same tag, regardless of point of connection, thus regardless of its IP address
        + In the BYOD context, a user may actually have 1-10 IP addresses assigned, which presents a scalability problem with firewall
    + Cisco Security Group Tag (SGT) w/ SGACL & SGFW
        <a href="http://netdesignarena.com/cisco-aci-trustsec-a-holistic-approach-for-secure-enterprise-networks/">
            <br/><img src="http://netdesignarena.com/wp-content/uploads/2016/12/SGT-768x296.png" alt="TrustySec" width="600">
        </a>


+ SGT Overview
    + SGT
        + Layer 2 tag, by default
        + Can be copied and carried in the layer 3 header by using ESP encapsulation
            + Helps keep the security tag across routing domains
    + SGT is dynamically assigned by ISE as part of the authorization policy
        + For authenticated endpoints
    + SGT is statically assigned by NAD
        + For non-authenticated endpoints, like servers
        + It can be assigned per VLAN, per IP, per subnet
    + SGT is always applied to the packet by the NAD
        + Requires both hardware and software capabilities


+ SGT Configuration Steps
    + Configure TrustSec (CTS) between ISE and NAD
    + Configure ISE dynamic SGT classification
    + Configure NAD static SGT classification
    + Configure SGACL on ISE
    + Configure SGACL and SGFW enforcement
    + Optionally configure SXP session between network devices


## MACSec Implementation

+ Topology:
    <br/><img src="./diagrams/sisas-net1.png" alt="Network Topology w/o Phone" width="450">

+ Demo: 
    + PC-B: EAP-FAST
    + ISE Config
        + Policy > Authentication > WIRED_EAP_FAST_AUTH: Condition=Wired_802.1x, Allow Protocol=EAP_FAST, use=INEAD
        + Policy > Authorization > POST_UNKNOWN > edit (Insert New Rule bove): Name=EAP_MACSEC, Conditions=Wired_802.1x, Permissions=PermitAccess
    + PC-B: 
        + run `services.msc` > AnyConnect Network Access Manager > Properties: startup=autiomatic > Apply > Start --> lost connection
        + NIC (which won't be controlled by AnyConnect) > Properties > disable Cisco AnyConnect Network Access Manager Filter Driver > ok
        + Restart AnyConnect Network ccess Manager service
        + Open AnyConnect > Networks=wired > Networks > Add: Media=wired, Name=EAP_MACSec, Security=802.1x, 802.1x Configuration=(Password, EAP-FAST) > ok
        + AnyConnect > Networks=EAP_MACSEC: user=ldapuser, pwd=Cisco123! -> Authentication Filed
    + SW3: 
        ```cfg
        show run int gi1/0/5
        ! interface GigabitEthernet1/0/5
        !   switchport access vlan 90
        !   switchport mode access
        !   logging event spanning-tree
        !   authentication port-control auto
        !   dot1x pae authenticator
        !   spanning-tree portfast
        ! end

        show authentication sessions    ! Status=Authz Success
        ```
    + ISE Verification: Operations > Authentications: No entry w/ Identity=ldapuser but anonymous
    + PC-B: 
        + AnyConnect > Networks=EAP_MACSEC (was wired) -> Not able to connect
        + logoff > logon
        + AnyConnect > Networks=EAP_MACSEC 
    + SW3 Msgs: 
        + AUTHMGR-5-FAIL: Authentication failed or unapplied for client
        + AUTHMGR-7-RESULT: Authentication result 'fail' from 'dot1x' for client
    + PC-B: AnyConnect Profile Editor - Network Access Manager > File > Open: configuration.xml > Networks=EAP_CHAINING:
        + Media Type: Name=EAP_CHAINING, Wired (802.3) network
        + Security Level: Authentication network
        + Connection type: User connection
        + User Auth: EAP-FAST
            + Settings: disable validate server identity, enable fast reconnection
            + Inner Method: Authenticate using a password=(EAP-MSCAHPv2, EAP-GTC)
            + Use PACs
        + Credentials: Use Single Sign On Credentials
        + File > Save As: configuration.xml
    + PC-B: 
        + Verifcation: Network Access Manager Profile Editor > File > Open: configuration.xml > Networks=EAP_CHAINING: checking existence and configuration > Cancel
        + AnyConnect > Networks=EAP_CHAINING --> Fail to connect
    + ISE: 
        + Verification: Operations > Authentications: Identity=anonymous (ldapuser expected, authentication failed) > details: Event=Endpoint concluded several failed authentications of the same scenarios, username=anonymous, Failure Reason=Fail to negotiate EAP beacuse EAP-FAST not allowed in the Allowed Protocols
        + Policy > Authentication > PEAP_EAP_TLE, use=INE_PKI_STORE > move below WIRED_EAP_FAST_AUTH > Save
        + Authentication Rule PEAP_WIRED_AUTH matched first and WIRED_EAP_FAST_AUTH never hit -> resolved by reorder them
    + PC-B: AnyConnect > Networks=EAP_CHAINING: user=ldapuser, pwd=Cisco123! -> still Failed
    + SW3: `conf t; int gi1/0/5; shut; not shut; ^Z` -> Msg still showing authentication failed
    + ISE: 
        + Policy > Authentication: correct rule order
        + Policy > Policy Elements > Results > Authentication > Allowed Protocols > EAP_FAST: Allow EAP-FAST=EAP-FAST (Inner Method: Allow EAP-MSCHAPv2, Allow EAP_TGC, use PACs), Enable EAP Chaining -> everything looks ok
    + SW3: msg -> still failed
    + ISE: 
        + Operations > Authentications > Identity=anonymous > details: AllowProtocolMatchedRule=PEAP_WORED_AUTH -> expect WIRED_EAP_FAST_AUTH
        + Policy > Authentications > disable PEAP_WIRED_AUTH
    + PC-B: AnyConnect > Networks=EAP_CHAINING: user=ldapuser, pwd=Cisco123! -> Authentication Failed
    + ISE: Policy > Authentications: delete PEAP_WIRED_AUTH
    + PC-B: AnyConnect > Networks=EAP_CHAINING: user=ldapuser, pwd=Cisco123! -> Authentication Failed
    + ISE: 
        + Operations > Authentications: Identity=anonymous -> same error message
        + Restart ISE
        + Operations > Authentications: Identity=ldapuser > details: AuthorizationPolicyMatchRule=EAP_CHAINING
    + SW3
        ```cfg
        show run int gi1/0/5
        ! interface GigabitEthernet1/0/5
        !   switchport access valn 90
        !   switchport mode access
        !   logging event spanning-tree
        !   authentication port-control auto
        !   dot1x pae authenticator
        !   spanning-tree portfast
        ! end

        conf t
        int gi1/0/5
          macsec
          mka default-policy

        do show authentication sessions int gi1/0/5    
        ! status=Authz Success, Security Policy=Should Secure (default)

        authentication linksec policy should-secure     ! default setting

        do show run int gi1/0/5 
        ! interface GigabitEthernet1/0/5
        !   switchport access valn 90
        !   switchport mode access
        !   logging event spanning-tree
        !   authentication port-control auto
        !   macsec
        !   mka default-policy
        !   dot1x pae authenticator
        !   spanning-tree portfast
        ! end
        ```
    + ISE:
        + Policy > Policy Elements > Results > Authorization > Authorization Profiles > Add: Name=MACSEC, Access Type=ACCESS_ACCEPT, Common Tasks=(MACSec Policy=must-secure) > Submit
        + Policy > Authorization > EAP_MACSEC: Permissions=MACSEC > Save

    + PC-B: AnyConnect Profile Editor > Network Access Editor > Open: configure.xml > Networks=EAP_CHAINING > edit: 
        + Security elvel: Authentication network, key Management=MKA, Encryption=MACSec:AES-GCM-128
        + Connection Type: User Connection
        + User Auth: EAP-FAST, EAP-FAST Setting=(Enable Fast Reconnect), Authentication using a password=(EAP-MSCHAPv2, EAP-GTC)
        + > Done > Save As: configuration.xml
    + SW3:
        ```cfg
        conf t
        int gi1/0/5
          shut
          no shut
        end

        show authentication sessions int gi1/0/5 
        ! Security Policy=Must Secure (local config: default = should-secure)

        show macsec intgi1/0/5          ! Decrypt bytes 71595
        ! PC-B: ping 10.10.10.10
        show macsec intgi1/0/5          ! Decrypt bytes 96415

        show macsec summary     ! Int=Gi1/0/5, Transmit SG=1, Receive SG=1
        show mka sessions int gi1/0/5
        ! Int=Gi1/0/5, Peer-RxSCI=48f8.632e.2532/0000, PolicyNmae=*DEFAULT-POLICY*, Audit-Session-ID: 0A0A0A0A0A0000004103589AFE
        ! Port-ID=2, Local-TxSCI=4463.ca63.9985/0002, Key-srv=YES, Suatus=Secure, CKN=0264c94858246878DCF66ECE32BD26263

        show mka sessions int gi1/0/5 detail
        ! # of MACSec Capable Live Peer=1, # of MACSec Capable of Live Peer Responded=1, 
        ! Status=SECURE - secured MKA Session with MACSec, MACSec Desire=Yes
        ```
    + ISE: Operations > Authentication > Identity=ldapuser (last authentication entry) > detail: Event=Authentication Succeeded, Authorization Profile=MACSEC, Result: cisco-av-pair=(linksec-policy=msut-secure), MS-MPP-send-key=de:...:5d, MS-MPPE-Recv-Key=47:...:d8











