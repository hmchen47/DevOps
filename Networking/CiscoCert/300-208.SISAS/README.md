# Implementing Cisco Secure Access Solutions - 300-208 SISAS

## INE Cisco CCNP Security 300-208 SISAS - Christian Matei

### [Course Introduction](./i00-Intro.md)

+ [CCNP Security Certification Goals](./i00-Intro.md#ccnp-security-certification-goals)
+ [About SISAS](./i00-Intro.md#about-sisas)
+ [Course Pre-Requisites](./i00-Intro.md#course-pre-requisites)
+ [Course Scope](./i00-Intro.md#course-scope)
+ [What is CCNP Security?](./i00-Intro.md#what-is-ccnp-security)
+ [What is SISAS?](./i00-Intro.md#what-is-sisas)
+ [Description](./i00-Intro.md#description)
+ [About CCNP Security Certification](./i00-Intro.md#about-ccnp-security-certification)
+ [Study Materials](./i00-Intro.md#study-materials)
+ [Logical Network Topologies](./i00-Intro.md#logical-network-topologies)



### [AAA and ISE Concepts](./i01-AAAISE.md)

+ [AAA Model](./i01-AAAISE.md#aaa-model)
+ [RADIUS and TACACS+](./i01-AAAISE.md#radius-and-tacacs)
+ [Cisco’s Authentication Servers](./i01-AAAISE.md#ciscos-authentication-servers)
+ [ISE Concepts](./i01-AAAISE.md#ise-concepts)
+ [ISE Management - Screenshots & References](./i01-AAAISE.md#ise-management)
+ [ISE Authentication Policies](./i01-AAAISE.md#ise-authentication-policies)


### [Authentication & Authorization - MAB](./i02-MAB.md)

+ [802.1X, MAB, and EAP Overview](./i02-MAB.md#8021x-mab-and-eap-overview)
+ [Network Access Authentication](./i02-MAB.md#network-access-authentication)
+ [MBA - MAC Authentication Bypass](./i02-MAB.md#mab--mac-authentication-bypass)
+ [MAB Configuration Steps on Supplicant](./i02-MAB.md#mab-configuration-steps-on-supplicant)
+ [MAB Configuration Steps on NAD](./i02-MAB.md#mab-configuration-steps-on-nad)
+ [MAB Configuration Steps on ISE](./i02-MAB.md#mab-configuration-steps-on-ise)
+ [MAB Verification and Troubleshooting](./i02-MAB.md#mab-verification-and-troubleshooting)
+ [ISE MAB Authentication](./i02-MAB.md#ise-mab-authentication)
+ [MAB and 802.1x Common Authorizations](./i02-MAB.md#mab-and-8021x-common-authorizations)
+ [MAB and EAP Common Authorizations](./i02-MAB.md#mab-and-eap-common-authorizations)
+ [Authorization Verification Troubleshooting](./i02-MAB.md#authorization-verification-troubleshooting)
+ [ISE 802.1x & MAB Authorization](./i02-MAB.md#ise-8021x--mab-authorization)
+ [ACL Authorization: dACL](./i02-MAB.md#acl-authorization-dacl)
+ [ACL Authorization: Filter-ID ACL](./i02-MAB.md#acl-authorization-filter-id-acl)
+ [ACL Authorization: Per-User ACL](./i02-MAB.md#acl-authorization-per-user-acl)
+ [MAC Authentication Bypass Deployment Guide](./i02-MAB.md#mac-authentication-bypass-deployment-guide)


### [Authentication & Authorization - EAP](./i03-EAP.md)

+ [IEEE 802.1X](./i03-EAP.md#ieee-8021x)
+ [Extensible Authentication Protocol (EAP)](./i03-EAP.md#extensible-authentication-protocol-eap)
+ [Common EAP Tunneled Methods](./i03-EAP.md#common-eap-tunneled-methods)
+ [Common EAP Non-Tunneled Methods](./i03-EAP.md#common-eap-non-tunneled-methods)
+ [802.1x Configuration Steps](./i03-EAP.md#8021x-configuration-steps)
+ [Deploying EAP](./i03-EAP.md#deploying-eap)
+ [EAP-FASTv1 Implementation](./i03-EAP.md#eap-fastv1-implementation)
+ [ISE Identity Sources](./i03-EAP.md#ise-identity-sources)
+ [Authentication Against AD](./i03-EAP.md#authentication-against-ad)
+ [Demo: AD Integration](./i03-EAP.md#demo-ad-integration)
+ [ISE Application Server](./i03-EAP.md#ise-application-server)
+ [Identity Prefix & Suffix Strip](./i03-EAP.md#identity-prefix--suffix-strip)
+ [User & Machine Authorization Policies](./i03-EAP.md#user--machine-authorization-policies)
+ [Deploying EAP TLS](./i03-EAP.md#deploying-eap-tls)
+ [Issuing Certificates on ISE](./i03-EAP.md#issuing-certificates-on-ise)
+ [Enrolling Users on a Certificate](./i03-EAP.md#enrolling-users-on-a-certificate)
+ [Importing CA Certificates](./i03-EAP.md#importing-ca-certificates)
+ [EAP-FASTv2 Chaining](./i03-EAP.md#eap-fastv2-chaining)



### [Phased Deployment](./i04-Deploy.md)

### [Layer 3 Authentication – HTTP / HTTPS](./i05-WebPortal.md)

+ [Layer 3 Authentication](./i05-WebPortal.md#layer-3-authentication)
+ [Phase 1 Configuration](./i05-WebPortal.md#phase-1-configuration)
+ [Phase 2 Configuratio](./i05-WebPortal.md#phase-2-configuration)
+ [ISE Guest Service](./i05-WebPortal.md#ise-guest-services)
+ [Web Portal Policy - Demo](./i05-WebPortal.md#web-portal-policy---demo)


### [EndPoint Profiling](./i06-Profiling.md)

+ [EndPoint Profiling](./i06-Profiling.md#endpoint-profiling-1)
+ [Profiling Policies](./i06-Profiling.md#profiling-policies)
+ [ISE Authorization Flow with Profiling](./i06-Profiling.md#ise-authorization-flow-with-profiling)
+ [Profiling Configuration](./i06-Profiling.md#profiling-configuration)
+ [Device Sensor Overview](./i06-Profiling.md#device-sensor-overview)


### [Posture Assessment](./i07-Posture.md)

+ [Posture Assessment Overview](./i07-Posture.md#posture-assessment-overview)
+ [Posture Services](./i07-Posture.md#posture-services)
+ [Posture Configuration](./i07-Posture.md#posture-configuration)


### [TrustSec](./i08-TrustSec.md)

+ [Layer 2 Encryption (MACSec)](./i08TrustSec.md#layer-2-encryption-macsec)
+ [Security Group Tags (SGT)](./i08TrustSec.md#security-group-tags-sgt)
+ [MACSec Implementation](./i08TrustSec.md#macsec-implementation)


## CBT Nuggets Cisco CCNP Security 300-208 SISAS - Keith Barker

+ [Identity Service Engine (ISE)](./c01-ISE.md)
+ [802.1x Wired](./c02-Wired.md)
+ [Using a Certificate Assigning by a CA](./c03-Cert.md)
+ [MAB and Troubleshooting](./c04-MAB.md)
+ [Network Access Manager (NAM)](./c05-NAM.md)
+ [Integrating ISE and AD](./c06-ISEAD.md)
+ [Authorization Policies, ISE, AD, and Rules](./c07-AuthZ.md)
+ [Web Based User Authentication](./c08-WBA.md)
+ [Posture Assessment](./c09-Posture.md)
    + [What is Posture?](./c09-Posture.md#what-is-posture)
    + [Planning and/or Updating NAC Files on the ISE Server](./c09-Posture.md#planning-and-or-updating-nac-files-on-the-ise-server)
    + [Providing NAC Agents from ISE](./c09-Posture.md#providing-nac-agents-from-ise)
    + [Enforcing Posture Requirements](./c09-Posture.md#enforcing-posture-requirements)
+ [ISE Profiling](./c10-Profiling.md)
+ [TrustSec](./c11-TrustSec.md)
    + [MACSec and TrustSec]((./c11-TrustSec.md#macsec-and-trustsec)
    + [Implementing TrustSec]((./c11-TrustSec.md#implementing-trustsec)
+ [ISE Personas](./c12-Personas.md)
+ [Sponsor Portal](./c13-Sponsor.md)
    + [Sponsor Portal with Guest Access](./c13-Sponsor.md#)
    + [Implementing a Sponsor Portal on ISE](./c13-Sponsor.md#)
+ [Bring Your Own Device (BYOD)](./c14-BYOD.md)





