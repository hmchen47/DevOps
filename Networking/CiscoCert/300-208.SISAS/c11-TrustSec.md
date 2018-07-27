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






