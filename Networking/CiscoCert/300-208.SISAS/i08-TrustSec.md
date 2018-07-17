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





