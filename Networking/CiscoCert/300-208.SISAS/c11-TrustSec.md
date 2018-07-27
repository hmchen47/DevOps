# TrustSec 

## MACSec and TrustSec

+ Media Access Control Security )MACSec) and TrustSec: IEEE 802.1AE Standard and Cisco
    + Frame Format
    + Confidentiality (AES), Integrity Check Value (ICV)
    + Host to Switch: MACSec Key Agreement (MAK)
    + Switch to Switch: Security Association Protocol (SAP, Cisco)
    + TrustSec
        + Security Group Tag (SGT)
        + SGT Exchange Protocol (SXP)
        + Security Group ACL (SGACL)

+ MACSec
    + Frame Format
        <a href="https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/identity-based-networking-services/white-paper-c11-737544.html">
            <br/><img src="https://www.cisco.com/c/dam/en/us/products/collateral/ios-nx-os-software/identity-based-networking-services/white-paper-c11-737544.docx/_jcr_content/renditions/white-paper-c11-737544_4.jpg" alt="MACsec Header Format" width="350"> &nbsp;
        </a>
        <a href="https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Borderless_Networks/Unified_Access/BYOD_Design_Guide/BYOD_Policy.html">
            <img src="https://www.cisco.com/c/dam/en/us/td/i/200001-300000/290001-300000/293001-294000/293619.eps/_jcr_content/renditions/293619.jpg" alt="Layer 2 SGT Frame Format" width="290">
        </a>
        + 
        + Integrity Check Value (ICV): used to for integrity check of each MKPDU send between two CA
    + MACSec Key Agreement
        <a href="http://www.h3c.com.hk/technical_support___documents/technical_documents/switches/h3c_s12500_series_switches/configuration/operation_manual/h3c_s12500_cg-release7374-6w731/10/201506/872952_1285_0.htm#_Ref385235347">
            <br/><img src="http://www.h3c.com.hk/res/201506/03/20150603_2143879_image003_872952_1285_0.png" alt="MACsec interactive process in client-oriented mode" width="300">&nbsp;
        </a>
        <a href="http://www.h3c.com.hk/technical_support___documents/technical_documents/switches/h3c_s12500_series_switches/configuration/operation_manual/h3c_s12500_cg-release7374-6w731/10/201506/872952_1285_0.htm#_Ref385237557">
            <img src="http://www.h3c.com.hk/res/201506/03/20150603_2143880_image004_872952_1285_0.png" alt="MACsec interactive process in device-oriented mode" width="310">
        </a>

    + Security Association Protocol (SAP) <br/>
        Depending on your software version, crypto licensing, and link hardware support, SAP negotiation can use one of the following modes of operation:
        + Galois/Counter Mode (GCM)—Specifies authentication and encryption
        + GCM authentication (GMAC)—Specifies authentication and no encryption
        + No Encapsulation— specifies no encapsulation (clear text)
        + Null—Specifies encapsulation, no authentication and no encryption
        <a href="http://www.madari.co.il/2014/02/cisco-macsec.html">
            <br/><img src="http://1.bp.blogspot.com/-Duj6hBTwt_4/Uvd2Lcf_46I/AAAAAAAAG78/StZNnhHtMiM/s1600/macsec_howitworks.jpg" alt="Link Security" width="450">
        </a>

    + Feature:
        + hop-by-hop encryption
        + Encryption:
            <a href="https://infocenter.alcatel-lucent.com/public/7750SR150R4A/index.jsp?topic=%2Fcom.sr.interface%2Fhtml%2Finterfaces.html">
                <br/><img src="https://infocenter.alcatel-lucent.com/public/7750SR150R4A/topic/com.sr.interface/html/graphics/sw0119.gif" alt="802.1 AE LAN/WAN Modes and VLAN Encrypted/Clear" width="300">
            </a>

+ TrustSec
    + SGT Value, e.g. SGT for Dept: Sales=1, HR=2, ENG=3, DEV=4
    + SGACL: Setup rules based on SGT Values, e.g. Deny SGT=4 pkts send to destination with SGT=2
    + Transport modes:
        <a href="https://www.slideshare.net/CiscoCanada/cisco-trustsec-security-group-tagging">
            <br/><img src="https://image.slidesharecdn.com/policydefinedsegmentationwithtrustsec-robbleeker-140422114817-phpapp01/95/cisco-trustsec-security-group-tagging-27-638.jpg?cb=1398167397" alt="SGT Transport Mechanism" width="450">
        </a>
    + SGT Exchange Protocol
        + DNS for SGTs
        + Associate IP with SGT, e.g. Subnet 40 -> SGT=1, Subnet 50 -> SGT=2




## Implementing TrustSec

+ TrustSec: CCentralized ACLs and Policies
    + ISE:
        + SGT password for NAD
        + SGT Groups
        + SGACLs (Create & Apply)
    + NAD:
        + AAA method list for CTS (Cisco TrustSec)
        + CTS and PAC credentials for NAD
        + Enforce Role-based (SGACL)

+ Demo: ISE Config
    + IEEE SGA AAA Server: Administration > Network Resources > SGA AAA > Server > ISE
    + NAD: Administration > Network Resources > Network Devices > SW2 (3750-x -> Support TrustSec) > Advanced TrustSec Settings: Device Authentication Settings=(use device ID for SGA Identification, pwd=Nugget!23), SGA Notifications and Updates=(Notify this device about SGA config changes), Device Config Deployment=(user=admin, pwd=Nugget!23)

+ Demo: Create Security Group with SGTs:
    + Policy > Policy Elements > Results > Security Group Access > Security Groups: SEC_NADs[2], SEC_SERER[3], SEC_USERS[4], UNKNOWN[0]
    + Role-Based ACL (RBACL): 
        + No source and destination in ACL - traffic between 2 SGTs
        + Policy > Policy Elements > Results > Security Group Access > Security Group ACLs (Deny_All, Deny_ICMP) > Deny_ICMP: Security Group ACL=(deny icmp, permit ip)
    + Policy > Policy Elements > Results > Security Group Access > Security Group Mappings > SEC_SERVERS: ip addr=8.8.8.8

+ Demo - Associate Security Group with SGT: Policy > Authorization > User and PC Authorization: Permissions=(Our_Author_profile, SEC_USERS)

+ Demo: NAD Adding for TrustSec - SW2
    ```cfg
    conf t
    radius-server host 192.1683.1.117 pac key Nugget!23
    aaa authorization network cts-author-list group radius  ! listt name=cts-author-list, serrver=radius
      cts credentials list cts-author-list 
    exit
    
    cts credential id SW2 password Nugget!23

    do show cts credentials         ! CTS pwd defined in keystore , device id=SW2
    do show cts password            ! I-ID=SW2, A-ID-Info=Identity Server Engine
    show cts environment-data
    ! Security Group Table: 
    ! 0-00=Unknown, 2-00=SEC_NADs, 3-00=SEC_SERVERS, 4-00=SEC_Users

    int gi1/0/12
      cts role-based enforcement 
    end

    cts refresh environment-data    ! update server info
    show cts environment-data
    ```

+ Demo: Apply SGACL <br/>
    + ISE: Policy > Security Group Access > Egress Policy > Matrix Tab: click on box with designated source and destination, e.g., src=SEC_USERS, dst=SEC_SERVERS, status=(enable Assigned SGACLs=Deny_ICMP) > Save
    + SW2: 
        ```cfg
        conf t
        int g1/0/12
          cts role-based enforcement 
        end
        ```
    + ISE Validation: Policy Authorization > Users and PC Authorization: Permissions=(Our_Auth_Profile , SEC_USERS)
    + SW2: `show authentication sessions int g1/0/12` - SGT=0004-0






