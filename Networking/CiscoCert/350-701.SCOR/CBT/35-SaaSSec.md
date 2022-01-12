# 35. Planning for and Securing Cloud Software-as-a-Service

Trainer: Bart Castle


## Planning for Software-as-a-Service Security

- Key factors to select cloud computing services
  - following value vs. risk equation
    - high value and low risk $\to$ probably not cloud computing service
    - solution: picking the appropriate service model, infrastructure, platform, and services
  - starting w/ SaaS
    - consider Software as a Serice (SaaS) as the first selection
    - tradoffs: responsibility and control


- Security concerns of SaaS
  - people:
    - authentication and authorization
    - example: tokens, SAML, AOuth, etc.
  - data: encryption
  - Cisco solutions
    - Dual
    - ISE
  - Cloud Access Security Broker (CASB)
    - Cisco CloudLock
    - highly integrated tools to monitor, maintain, and control SaaS
  - Email and DNS security



## Federating Identities with SAML, OAuth, and OpenID

- Identity management
  - people and data: authn & authz
  - federating identity: sharing identity w/ different systems
  - directory:
    - old fashion used in organization
    - a collection of identities and permission properties
    - example: MS AD
  - other solutions
    - Secure Assertion Markup Language (SAML)
    - OAuth
    - OpenID


- Secure Assertion Markup Language (SAML)
  - an umbrella standard covering federation, identity management and single sign-on (SSO)
  - providing single-sign-on (SSO) service
  - typically used for domain-based computer
  - roles
    - service provider
    - users (client= browser)
    - identity provider (IDP)
  - SAML workflow

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
        onclick= "window.open('https://www.mandsconsulting.com/federated-sso-a-primer-saml-oauth-2-0-openid-connect/')"
        src    = "https://www.mandsconsulting.com/wp-content/uploads/Mutually-Human-SAML-2.0-Flow.jpg"
        alt    = "Federated single sign-on (or SSO) is a modern way to solve the problem of having multiple logins between different services and applications"
        title  = "Federated single sign-on (or SSO) is a modern way to solve the problem of having multiple logins between different services and applications"
      />
    </figure>
  
  - advantage: feature-rich mechanism, not only authn & authz
  - disadvantage: complexity


- Open Authorization (OAuth)
  - an authentication protocol allowing to approve one application interacting with another on your behalf without giving away your password
  - an open standard for access delegation, commonly used as a way for Internet users to grant websites or applications access to their information on other websites but without giving them the passwords
  - delegation permission, in particular, authorization
  - roles
    - client (mobile / web app)
    - resource owner
    - authorization server
    - resource server
  - response from authorization server most likely including identity property
  - OAuth workflow

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
        onclick= "window.open('https://bit.ly/338ccJR')"
        src    = "https://bit.ly/3GmB4f2"
        alt    = "Interaction between the four roles of the OAuth protocol flow"
        title  = "Interaction between the four roles of the OAuth protocol flow"
      />
    </figure>

  - example: twitter using facebook account to login
  - OPenID:
    - providing an identity assertion
    - an open standard that organizations use to authenticate users



## Cisco Zero-Trust for the Workforce

- Zero-trust security overview
  - offering a comprehensive solution to secure all access across your applications and environment
  - a strategic approach to security that centers on the concept of eliminating trust from an organization's network architecture
  - traditional, trust anything within corporate network
  - layers
    - workplace security:
      - Cisco SD-Access
      - protecting general ingress, egress points or endpoints
    - workload security
      - Cisco Tetration
      - tools to control what happen in managing and rasing visibility of workload
      - examples: virtual machines, physical devices or containers
    - workforce
      - Cisco Duo & AnyConnect
      - Duo working w/ other identity system
      - authenticating users using existing on-premises or cloud-based directory credentials
      - AnyConnect + Duo to provide zero-trust


- Duo authentication options
  - multifactor authentication (MFA)
  - single-sign-on service (SSO): hosted - Cisco cloud env.
  - dual access gateway (DAG): on-premise, able to work w/ IDP, SAML, OAuth
  - network access gateway (NAG)


- Demo: Stealthwatch cloud w/ Duo
  - login Stealthwatch
  - redirect to `sign-on.security.cisco.com`
  - login page shown
    - SecureX username
    - OAuth w/ Cisco or MS account
  - using MS account > Duo Security: MFA


## Cisco Cloudlock Access Security Broker

- Cloud Access Security Broker (CASB)
  - Cisco solution: Cloudlock
  - providing visibility and control over data and threats in the cloud to meet enterprise security requirements
  - a control point to secure cloud services
  - typically unifying a number of security measures used across the cloud to make detection, management, and enforcement much easier to deploy and control
  - security concerns for people and data
    - clients: mobile app & browser
    - APIs to provide the common interfaces
    - CASB sending queries to API of clients
  - <span style="color: cyan;">layers of control</span>
    - behavior: user activities on data focused operations
    - data loss prevention (DLP): what, when and who to share data
    - OAuth:
      - potential exploit
      - sharing w/ other organization's account
      - able to catch what has been shared
  - [Cisco Cloudlock: Secure Cloud Data](https://learn-umbrella.cisco.com/i/785943-cisco-cloudlock-secure-cloud-data)



## Securing DNS with Cisco Umbrella and OpenDNS




## Securing Communications with Cisco Email Security



