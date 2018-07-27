# ISE Personas

+ Identity Service Engine (ISE) Personas: The Faces of ISE
    + Administration
    + Policy Service
    + Monitoring and Troubleshooting
    + Inline Posture
    + Nodes and Roles

+ Personas
    + Node=ISE
    + Responsibility/Functions ISE providing/include Administration
    + Configuring in the authentication and authorization policies
    + ISE Server:
        + Single server: standalone node, responsible for administration persona and others
        + Multi-servers: primary and secondary implement policies in primary
    + PSN: Policy Service Node, persona for policy serviced
    + Administration Persona: config policy while PSN implement rep policy
    + Most likely having more than one PSN due to large network with many nodes and users
    + Multiple PSNs:
        + fault tolerance
        + load balancing
    + Multiple Monitoring
        + Primary & secodary - fault tolerance
        + all logs collected by once
    + Inline Posture
        + Network Admission Control
        + FW on a device
    + Personas
        + Synced by NTP
        + DNS correctly setup

+ ISE Persona Deployment 
  <a href="https://www.grandmetric.com/knowledge-base/design_and_configure/cisco-ise-deployment-models/">
      <br/><img src="https://www.grandmetric.com/wp-content/uploads/2017/08/Cisco-ISE-Depolyment-and-NAD-interaction.png" alt="Cisco ISE Deployment models" width="450">
  </a>

+ ISE Architecture and nomenclature:
    + __Node__ – Individual instance – Physical Appliance or Virtual Appliance
    + __Persona/Node Type__ – This one is often used interchangeable and determines the service provided by particular node:
        + __Administration (PAN)__ – Administration Node is a single point of ISE deployment configuration. This persona provides full access to administration GUI
        + __Policy Service (PSN)__ – Policy Service Node is a node that handles traffic between network devices and ISE (its IP is used as Radius for devices). To achieve radius traffic sharing you can scale the PSNs up.
        + __Monitoring (MnT)__ – monitoring node is responsible for logs aggregation across deployment.
    + __Role__ – Applies to Administration and Monitoring nodes.
        + Standalone – related to standalone deployment – node is not aware of each other and acts alone.
        + Primary – role in distributed deployment where for example administration persona is the primary for all configuration tasks.
        + Secondary – role in distributed deployment where for example administration persona is secondary for configuration tasks. Secondary GUI is available for configuration only when:
            + Primary fails and there is PAN Failover configured
            + Secondary is manually promoted to Primary

+ Inline Posture Persona:
    + Inline Posture node: 
        + a gatekeeper that enforces access policies and handles change of authorization (CoA) requests. 
        + positioned behind the network access devices on your network that are unable to accommodate CoA requests, such as wireless LAN controllers (WLCs) and VPN devices.
    + Inline Posture uses RADIUS proxy and URL redirect capabilities in the control plane to manage data plane traffic for endpoints.
    + Inline Posture Policy Enforcement Flow
        <a href="https://www.cisco.com/c/en/us/td/docs/security/ise/1-2/user_guide/ise_user_guide/ise_ipep_deploy.html#84523">
            <br/><img src="https://www.cisco.com/c/dam/en/us/td/i/200001-300000/280001-290000/281001-282000/281859.eps/_jcr_content/renditions/281859.jpg" alt="Inline Posture Policy Enforcement Flow" width="450">
        </a>
        1.	The endpoint initiates a .1X connection to the wireless network.
        2.	The WLC, which is a NAD, sends a RADIUS Access-Request message to the RADIUS server, which is usually the Policy Service node (in this illustration, the RADIUS Access-Request message is sent to the Inline Posture node).
        3.	The Inline Posture node, acting as a RADIUS proxy, relays the Access-Request message to the RADIUS server.
        4.	After authenticating the user, the RADIUS server sends a RADIUS Access-Accept message back to the Inline Posture node. <br/>There can be a number of RADIUS transactions between the Endpoint, WLC, Inline Posture node, and the Cisco ISE RADIUS server before the Access-Accept message is sent. The process described in this example has been simplified for the sake of brevity.
        5.	The Inline Posture node passes the Access-Accept message to the WLC, which in turn authorizes the endpoint access, in accordance with the profile that accompanied the message.
        6.	The proxied Access-Accept message triggers the Inline Posture node to send an Authorization-Only request to the Policy Service node to retrieve the profile for the session.
        7.	The Policy Service node returns an Access-Accept message, along with the necessary Inline Posture node profile.
        8.	If the access control list (ACL) that is defined in the profile is not already available on the Inline Posture node, the Inline Posture node downloads it from the Policy Service node using a RADIUS request (to the Cisco ISE RADIUS server).
        9.	The Cisco ISE RADIUS server sends the complete ACL in response. It is then installed in the Inline Posture data plane so that endpoint traffic passes through it.
        There may be a number of transactions before the complete ACL is downloaded, especially if the ACL is too large for one transaction.
        10.	As the endpoint traffic arrives at the WLC, the WLC sends out a RADIUS Accounting-Start message for the session to the Inline Posture node.
        The actual data traffic from the endpoint may arrive at the Inline Posture node untrusted side before the Accounting-Start message is received by the Inline Posture node. Upon receiving the RADIUS Accounting-Start message, the Inline Posture node learns the IP address of the endpoint involved in the session and associates the endpoint with the ACL, which is downloaded and installed earlier in the session. The initial profile for this client endpoint could be restrictive, to posture the client before being given full access.
        11.	Assuming the restrictive ACL allows access only to Cisco ISE servers, the endpoint is only allowed actions such as agent downloading and posture assessment over the data plane.
        12.	If the client endpoint is posture compliant (as part of the restricted communication with Cisco ISE services earlier), the Policy Service node initiates a RADIUS (CoA) with the new profile. Therefore, a new ACL is applied at the Inline Posture node for the session. The new ACL is installed immediately and applied to the endpoint traffic.
        13.	The endpoint is then capable of full access to the enterprise network, as a result of the new profile that was applied to the Inline Posture node.



