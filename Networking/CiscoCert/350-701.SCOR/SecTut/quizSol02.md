# Quiz Set 2


## 05. Python & API

- <span style="color: #008888; font-weight: bold;">Question 1</span>

  Which API is used for Content Security?

  A. NX-OS API<br>
  B. IOS XR API<br>
  C. OpenVuln API<br>
  D. AsyncOS API<br>

  Answer: D

  Explanation

  Cisco Content Security Management Appliance -> Cisco Secure Email and Web Manager

  The AsyncOS API for Cisco Security Management appliances (or AsyncOS API) is a representational state transfer (REST) based set of operations that provide secure and authenticated access to the Security Management appliance reports, report counters, tracking, quarantine, and configuration. You can retrieve the Security Management appliance reporting, tracking, and quarantine data (for Email Security appliances) using the API.

  Reference: [Overview of AsyncOS API for Cisco Security Management Appliances](https://www.cisco.com/c/en/us/td/docs/security/security_management/sma/sma14-0/b_sma_api_guide_14_0/m_overview_of_sma_apis.html)


- <span style="color: #008888; font-weight: bold;">Question 2</span>

  Which two request of REST API are valid on the Cisco ASA Platform? (Choose two)

  A. put<br>
  B. options<br>
  C. get<br>
  D. push<br>
  E. connect<br>

  Answer: A C

  Explanation

  The ASA REST API gives you programmatic access to managing individual ASAs through a Representational State Transfer (REST) API. The API allows external clients to perform **CRUD** (Create, Read, Update, Delete) operations on ASA resources; it is based on the HTTPS protocol and REST methodology.
  
  All API requests are sent over HTTPS to the ASA, and a response is returned.

  Request Structure

  Available request methods are:
  - `GET` – Retrieves data from the specified object.
  - `PUT` – Adds the supplied information to the specified object; returns a 404 Resource Not Found error if the object does not exist.
  - `POST` – Creates the object with the supplied information.
  - `DELETE` – Deletes the specified object.
  - `PATCH` – Applies partial modifications to the specified object.

  Reference: [Cisco ASA REST API Quick Start Guide](https://www.cisco.com/c/en/us/td/docs/security/asa/api/qsg-asa-api.html)


- <span style="color: #008888; font-weight: bold;">Question 3</span>

  Refer to the exhibit.

  ```python
  def add_device_to_dnac(dnac_ip, device_ip, snmp_version, 
      snmp_ro_community, snmp_rw_community, snmpretry, 
      snmptimeout, cli_transport, username, password, 
      enable_password):
    device_object = {
      "ipAddress": [device_ip],
      "type": "NETWORK_DEVICE",
      "ComputeDevice": False,
      "snmpVersion": snmp_version,
      "snmpROCommunity": snm-_ro_community,
      "snmpRWCommunity": snmp_rw_community,
      "snmpRetyr": snmpretry,
      "snmpTimeout": snmptimeout,
      "cliTransport": cli_transport,
      "userName": username,
      "password": password,
      "enablePassword": enable_password
    }
    response = requests.post(
      "https://{}/dna/intent/api/v1/network-device".format(dnac_ip),
      data = json.dump(device_object),
      headers = {
        "X-Auth-Token": "{}".format(token),
        "Content-Type": 'application.json'
      },
      verify=Flase
    )
    return response.json
  ```

  <!-- <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('https://www.securitytut.com/scor/python-api')"
      src    = "img/0503-Python_script_DNA_Center_API.jpg"
      alt    = "Python Script w/ DNA Center API"
      title  = "Python Script w/ DNA Center API"
    />
  </figure> -->

  What is the result of this Python script of the Cisco DNA Center API?

  A. adds authentication to a switch<br>
  B. adds a switch to Cisco DNA Center<br>
  C. receives information about a switch<br>

  Answer: B

  Explanation

  Add Device: `post /dna/intent/api/v1/network-device`
  
  Reference: [Add Device](https://developer.cisco.com/docs/dna-center/#!add-device-1)


- <span style="color: #008888; font-weight: bold;">Question 4</span>

  Refer to the exhibit.

  ```python
  import requests

  client_id = 'a1b2c3d4e5f6g7h8i9j0'

  api_key = 'a1b2c3d4-e5f6-g7h8-k1l2m3n4o5q6i9j0'

  url = "https://api.amp.cisco.com/v1/computers"

  response = requests.get(url, auth=(client_id, api_key))

  response_json = response.json()

  for computer in response_json(['data]):
    network_address = computer['network_address']
    for network_interface in network_address:
      mac = network_interface.get('mac')
      ip = network_interface('ip')
      ipv6 = network_interface('ipv6')
      print(mac, ip , ipv6)
  ```

  What does the API do when connected to a Cisco security appliance?

  A. get the process and PID information from the computers in the network<br>
  B. create an SNMP pull mechanism for managing AMP<br>
  C. gather network telemetry information from AMP for endpoints<br>
  D. gather the network interface information about the computers AMP sees<br>

  Answer: D

  Explanation

  The call to API of “https://api.amp.cisco.com/v1/computers” allows us to fetch list of computers across your organization that Advanced Malware Protection (AMP) sees.

  Reference: [Cisco AMP for Endpoints API](https://api-docs.amp.cisco.com/api_actions/details?api_action=GET+%2Fv1%2Fcomputers&api_host=api.apjc.amp.cisco.com&api_resource=Computer&api_version=v1)

  <!-- <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.securitytut.com/scor/python-api')"
      src    = "img/0504-Cisco_security_appliance_API.jpg"
      alt    = "Python Script w/ Security Appliance API"
      title  = "Python Script w/ Security Appliance API"
    />
  </figure> -->


## 06. Firewall & Intrusion Prevention

- <span style="color: #008888; font-weight: bold;">Question 1</span>

  Which feature requires a network discovery policy on the Cisco Firepower Next Generation Intrusion Prevention System?

  A. Security Intelligence<br>
  B. Impact Flags<br>
  C. Health Monitoring<br>
  D. URL Filtering<br>

  Answer: B

  Explanation

  Alerting you by email, SNMP trap, or syslog when the system generates either an intrusion event with a specific impact flag, or a specific type of discovery event

  Reference: [Introduction to Network Discovery and Identity](https://www.cisco.com/c/en/us/td/docs/security/firepower/60/configuration/guide/fpmc-config-guide-v60/Introduction_to_Network_Discovery.html)


- <span style="color: #008888; font-weight: bold;">Question 2</span>

  Which two deployment model configurations are supported for Cisco FTDv in AWS? (Choose two)

  A. Cisco FTDv configured in routed mode and managed by an FMCv installed in AWS<br>
  B. Cisco FTDv with one management interface and two traffic interfaces configured<br>
  C. Cisco FTDv configured in routed mode and managed by a physical FMC appliance on premises<br>
  D. Cisco FTDv with two management interfaces and one traffic interface configured<br>
  E. Cisco FTDv configured in routed mode and IPv6 configured<br>

  Answer: A C

  Explanation

  The Firepower Threat Defense Virtual (FTDv) is the virtualized component of the Cisco NGFW solution. The FTDv provides next-generation firewall services, including stateful firewalling, routing, VPN, Next-Generation Intrusion Prevention System (NGIPS), Application Visibility and Control (AVC), URL filtering, and Advanced Malware Protection (AMP).

  You can manage the FTDv using the Firepower Management Center (FMC), a full-featured, multidevice manager on a separate server.

  The FTDv registers and communicates with the FMC on the Management interface that you allocated to the FTDv virtual machine.

  Reference: [About Firepower Threat Defense Virtual with Firepower Management Center](https://www.cisco.com/c/en/us/td/docs/security/firepower/quick_start/aws/ftdv-aws-gsg/m_managing_the_firepower_threat_defense_virtual_with_the_firepower_management_center.html#id_105951)

  Firepower Threat Defense Virtual interface requirements:
  - Management interfaces (2 — One used to connect the Firepower Threat Defense Virtual to the Firepower Management Center, second used for diagnostics; cannot be used for through traffic.
  - Traffic interfaces (2) — Used to connect the Firepower Threat Defense Virtual to inside hosts and to the public network.

  -> Answer B & D are incorrect

  Supported Features
  - Deployment in the Virtual Private Cloud (VPC).
  - Enhanced networking (SR-IOV) where available.
  - Deployment from Amazon Marketplace.
  - Maximum of four vCPUs per instance.
  - User deployment of L3 networks.
  - Routed mode (default).
  - Passive mode via ERSPAN.

  IPv6 is not currently supported -> Answer E is incorrect

  Reference: [Guidelines and Limitations for the FTDv and AWS](https://www.cisco.com/c/en/us/td/docs/security/firepower/quick_start/aws/ftdv-aws-gsg/m_getting-started-with-firepower-threat-defense-virtual-and-aws.html)


- <span style="color: #008888; font-weight: bold;">Question 3</span>

  Which option is the main function of Cisco Firepower impact flags?

  A. They alert administrators when critical events occur.<br>
  B. They highlight known and suspected malicious IP addresses in reports.<br>
  C. They correlate data about intrusions and vulnerability.<br>
  D. They identify data that the ASA sends to the Firepower module.<br>

  Answer: C

  Explanation

  Impact flags help you evaluate the impact an intrusion has on your network by correlating intrusion data, network discovery data, and vulnerability information.

  Reference: [Configuring Impact Flag Alerting](https://www.cisco.com/c/en/us/td/docs/security/firepower/610/configuration/guide/fpmc-config-guide-v61/external_alerting_with_alert_responses.html)


- <span style="color: #008888; font-weight: bold;">Question 4</span>

  On Cisco Firepower Management Center, which policy is used to collect health modules alerts from managed devices?

  A. health policy<br>
  B. system policy<br>
  C. correlation policy<br>
  D. access control policy<br>
  E. health awareness policy<br>

  Answer: A

  Explanation

  The health monitor on the Firepower Management Center tracks a variety of health indicators to ensure that the hardware and software in the Firepower System are working correctly. You can use the health monitor to check the status of critical functionality across your Firepower System deployment.

  You can use the health monitor to create a collection of tests, referred to as a _health policy_, and apply the health policy to one or more appliances. The tests, referred to as _health modules_, are scripts that test for criteria you specify. You can modify a health policy by enabling or disabling tests or by changing test settings, and you can delete health policies that you no longer need. You can also suppress messages from selected appliances by blacklisting them.

  A health policy contains configured health test criteria for several modules. You can control which health modules run against each of your appliances and configure the specific limits used in the tests run by each module.

  When you configure a health policy, you decide whether to enable each health module for that policy. You also select the criteria that control which health status each enabled module reports each time it assesses the health of a process.

  Reference: [Health Monitoring](https://www.cisco.com/c/en/us/td/docs/security/firepower/60/configuration/guide/fpmc-config-guide-v60/Health_Monitoring.html)


- <span style="color: #008888; font-weight: bold;">Question 5</span>

  Which license is required for Cisco Security Intelligence to work on the Cisco Next Generation Intrusion Prevention System?

  A. control<br>
  B. malware<br>
  C. URL filtering<br>
  D. protect<br>

  Answer: D
  
  Explanation

  Cisco Firepower Next-Generation IPS (NGIPS) threat appliances provide network visibility, security intelligence, automation and advanced threat protection. It uses industry-leading intrusion prevention capabilities and multiple techniques to detect even the most sophisticated network attacks and protect you against them. Cisco Firepower NGIPS threat appliances all offer the ability to operate in-line via Fail-To-Wire/Bypass network modules.

  Cisco Firepower NGIPS continuously discovers information about your network environment, including data about operating systems, mobile devices, files, applications and users. It then uses this information to build network maps and host profiles. This gives you the contextual information you need to make better decisions about intrusion events. And this information is also used as input to better enable the automation of key threat protection features.

  Cisco’s TALOS Security Intelligence and Research Group collects and correlates threats in real time using the largest threat detection network in the world. Their efforts result in vulnerability-focused IPS rules and embedded IP-, URL-, and DNS-based security intelligence for Firepower NGIPS.

  Security automation correlates intrusion events with your network’s vulnerabilities so you can focus on the threats that matter most. It also analyzes your network’s weaknesses and recommends the appropriate security policies to put in place.

  Cisco Firepower NGIPS threat appliances provide industry leading threat effectiveness against both known and unknown threats. Features include:
  - IPS rules that identify and block attack traffic that target vulnerabilities in your network
  - Tightly integrated defense against advanced malware incorporating advanced analysis of network and endpoint activity
  - Sandboxing technology that uses hundreds of behavioral indicators to identify zero-day and evasive attacks

  Reference: [Cisco Firepower NGIPS Data Sheet](https://www.cisco.com/c/en/us/products/collateral/security/ngips/datasheet-c78-742472.html)


- <span style="color: #008888; font-weight: bold;">Question 6</span>

  Which two are valid suppression types on a Cisco Next Generation Intrusion Prevention System? (Choose two)

  A. Port<br>
  B. Rule<br>
  C. Source<br>
  D. Application<br>
  E. Protocol<br>

  Answer: B C

  Explanation

  Intrusion Policy Suppression 
  
  You can suppress intrusion event notification when a specific IP address or range of IP addresses triggers a specific rule or preprocessor. This is useful for eliminating false positives. For example, if you have a mail server that transmits packets that look like a specific exploit, you might suppress event notification for that event when it is triggered by your mail server. The rule triggers for all packets, but you only see events for legitimate attacks.

  You can add suppressions from within the packet view of an intrusion event. You can also access suppression settings by using the right-click context menu on the intrusion rules editor page (Objects > Intrusion Rules) and on any intrusion event page (if the event was triggered by an intrusion rule).

  Reference: [Tuning Intrusion Policies Using Rules](https://www.cisco.com/c/en/us/td/docs/security/firepower/60/configuration/guide/fpmc-config-guide-v60/Tuning_Intrusion_Policies_Using_Rules.html#ID-2237-000007fe)


- <span style="color: #008888; font-weight: bold;">Question 7</span>

  Which feature is configured for managed devices in the device platform settings of the Firepower Management Center?

  A. quality of service<br>
  B. time synchronization<br>
  C. network address translations<br>
  D. intrusion policy<br>

  Answer: B

  Explanation

  A platform settings policy is a shared set of features or parameters that define the aspects of a managed device that are likely to be similar to other managed devices in your deployment, such as time settings and external authentication.

  A shared policy makes it possible to configure multiple managed devices at once, which provides consistency in your deployment and streamlines your management efforts. Any changes to a platform settings policy affects all the managed devices where you applied the policy. Even if you want different settings per device, you must create a shared policy and apply it to the desired device.

  Reference: [Platform Settings Policies](https://www.cisco.com/c/en/us/td/docs/security/firepower/640/configuration/guide/fpmc-config-guide-v64/platform_settings_policies_for_managed_devices.html#ID-2258-000006e8)


- <span style="color: #008888; font-weight: bold;">Question 8</span>

  Which information is required when adding a device to Firepower Management Center?

  A. username and password<br>
  B. encryption method<br>
  C. device serial number<br>
  D. registration key<br>

  Answer: D
  
  Explanation

  Step 5: In the Registration Key field, enter the same registration key that you used when you configured the device to be managed by the Firepower Management Center. The registration key is a one-time-use shared secret.

  Reference: [Device Management Basics](https://www.cisco.com/c/en/us/td/docs/security/firepower/610/configuration/guide/fpmc-config-guide-v61/device_management_basics.html)


- <span style="color: #008888; font-weight: bold;">Question 9</span>

  Which two deployment modes does the Cisco ASA FirePower module support? (Choose two)

  A. transparent mode<br>
  B. routed mode<br>
  C. inline mode<br>
  D. active mode<br>
  E. passive monitor-only mode<br>

  Answer: C E

  Explanation

  You can configure your ASA FirePOWER module using one of the following deployment models:

  You can configure your ASA FirePOWER module in either an **inline** or a **monitor-only** (inline tap or passive) deployment.

  Reference:
  - [ASA FirePOWER (SFR) Module](lhttps://www.cisco.com/c/en/us/td/docs/security/asa/asa92/asdm72/firewall/asa-firewall-asdm/modules-sfr.htm)
  - [Cisco ASA FirePOWER Module Quick Start Guide](https://www.cisco.com/c/en/us/td/docs/security/asa/quick_start/sfr/firepower-qsg.html)


- <span style="color: #008888; font-weight: bold;">Question 10</span>

  The Cisco ASA must support TLS proxy for encrypted Cisco Unified Communications traffic. Where must the ASA be added on the Cisco UC Manager platform?

  A. Certificate Trust List<br>
  B. Endpoint Trust List<br>
  C. Enterprise Proxy Service<br>
  D. Secured Collaboration Proxy<br>

  Answer: A

  Explanation

  For the Cisco Unified Presence solution, the ASA acts as a TLS proxy between the Cisco UP server and the foreign server. This allows the ASA to proxy TLS messages on behalf of the server that initiates the TLS connection, and route the proxied TLS messages to the client. The ASA stores certificate trustpoints for the server and the client, and presents these certificates on establishment of the TLS session.

  Reference: [Information About the ASA in Cisco Unified Communications](https://www.cisco.com/c/en/us/td/docs/security/asa/special/unified-communications/unified-communications-guide/information-about-asa-cisco-unified-communications.html)

  If you are connecting the trunk to a secure device, you must upload a certificate for the secure device to Unified Communications Manager.

  Reference: [TLS Setup](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/14_0/cucm_b_security-guide-1401/cucm_m_tls-setup.html)


- <span style="color: #008888; font-weight: bold;">Question 11</span>

  Which statement about the configuration of Cisco ASA NetFlow v9 Secure Event Logging is true?

  A. To view bandwidth usage for NetFlow records, the QoS feature must be enabled.<br>
  B. A sysopt command can be used to enable NSEL on a specific interface.<br>
  C. NSEL can be used without a collector configured.<br>
  D. A `flow-export event-type` must be defined under a policy.<br>

  Answer: D


- <span style="color: #008888; font-weight: bold;">Question 12</span>

  Which feature is supported when deploying Cisco ASAv within AWS public cloud?

  A. multiple context mode<br>
  B. user deployment of Layer 3 networks<br>
  C. IPv6<br>
  D. clustering<br>

  Answer: B

  Explanation

  The ASAv on AWS supports the following features:
  - Support for Amazon EC2 C5 instances, the next generation of the Amazon EC2 Compute Optimized instance family.
  - Deployment in the Virtual Private Cloud (VPC)
  - Enhanced networking (SR-IOV) where available
  - Deployment from Amazon Marketplace
  - Maximum of four vCPUs per instance
  - User deployment of L3 networks
  - Routed mode (default)

  Note: The Cisco Adaptive Security Virtual Appliance (ASAv) runs the same software as physical Cisco ASAs to deliver proven security functionality in a virtual form factor. The ASAv can be deployed in the public AWS cloud. It can then be configured to protect virtual and physical data center workloads that expand, contract, or shift their location over time.

  Reference: [Deploy the ASAv On the AWS Cloud](https://www.cisco.com/c/en/us/td/docs/security/asa/asa96/asav/quick-start-book/asav-96-qsg/asav-aws.html)


- <span style="color: #008888; font-weight: bold;">Question 13</span>

  Which statement describes a traffic profile on a Cisco Next Generation Intrusion Prevention System?

  A. It allows traffic if it does not meet the profile.<br>
  B. It defines a traffic baseline for traffic anomaly deduction.<br>
  C. It inspects hosts that meet the profile with more intrusion rules.<br>
  D. It blocks traffic if it does not meet the profile.<br>

  Answer: B

  Explanation

  A traffic profile is a graph of network traffic based on connection data collected over a profiling time window (PTW). This measurement presumably represents normal network traffic. After the learning period, you can detect abnormal network traffic by evaluating new traffic against your profile.

  Reference: [Traffic Profiling](https://www.cisco.com/c/en/us/td/docs/security/firepower/60/configuration/guide/fpmc-config-guide-v60/Creating_Traffic_Profiles.html)


- <span style="color: #008888; font-weight: bold;">Question 14</span>

  Which statement about IOS zone-based firewalls is true?

  A. An unassigned interface can communicate with assigned interfaces<br>
  B. Only one interface can be assigned to a zone.<br>
  C. An interface can be assigned to multiple zones.<br>
  D. An interface can be assigned only to one zone.<br>

  Answer: D

  Explanation

  Router network interfaces’ membership in zones is subject to several rules that govern interface behavior, as is the traffic moving between zone member interfaces:
  - A zone must be configured before interfaces can be assigned to the zone.
  - <span style="color: #bb6600;">An interface can be assigned to only one security zone.</span>
  - All traffic to and from a given interface is implicitly blocked when the interface is assigned to a zone, except traffic to and from other interfaces in the same zone, and traffic to any interface on the router.
  - Traffic is implicitly allowed to flow by default among interfaces that are members of the same zone.
  - In order to permit traffic to and from a zone member interface, a policy allowing or inspecting traffic must be configured between that zone and any other zone.
  - The self zone is the only exception to the default deny all policy. All traffic to any router interface is allowed until traffic is explicitly denied.
  - Traffic cannot flow between a zone member interface and any interface that is not a zone member. Pass, inspect, and drop actions can only be applied between two zones.
  - Interfaces that have not been assigned to a zone function as classical router ports and might still use classical stateful inspection/CBAC configuration.
  - If it is required that an interface on the box not be part of the zoning/firewall policy. It might still be necessary to put that interface in a zone and configure a pass all policy (sort of a dummy policy) between that zone and any other zone to which traffic flow is desired.
  - From the preceding it follows that, if traffic is to flow among all the interfaces in a router, all the interfaces must be part of the zoning model (each interface must be a member of one zone or another).
  - The only exception to the preceding deny by default approach is the traffic to and from the router, which will be permitted by default. An explicit policy can be configured to restrict such traffic.

  Reference: [Zone-Based Policy Firewall Design and Application Guide](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/98628-zone-design-guide.html)


- <span style="color: #008888; font-weight: bold;">Question 15</span>

  What is a characteristic of Cisco ASA Netflow v9 Secure Event Logging?

  A. It tracks flow-create, flow-teardown, and flow-denied events.<br>
  B. It provides stateless IP flow tracking that exports all records of a specific flow.<br>
  C. It tracks the flow continuously and provides updates every 10 seconds.<br>
  D. Its events match all traffic classes in parallel.<br>

  Answer: A

  Explanation

  The ASA and ASASM implementations of NetFlow Secure Event Logging (NSEL) provide a stateful, IP flow tracking method that exports only those records that indicate significant events in a flow.

  The significant events that are tracked include flow-create, flow-teardown, and flow-denied (excluding those flows that are denied by EtherType ACLs).

  Reference: [NetFlow Secure Event Logging (NSEL)](https://www.cisco.com/c/en/us/td/docs/security/asa/asa92/configuration/general/asa-general-cli/monitor-nsel.html)


- <span style="color: #008888; font-weight: bold;">Question 16</span>

  Which CLI command is used to register a Cisco FirePower sensor to Firepower Management Center?

  A. `configure system add <host><key>`<br>
  B. `configure manager <key> add host`<br>
  C. `configure manager delete`<br>
  D. `configure manager add <host><key>`<br>

  Answer: D


- <span style="color: #008888; font-weight: bold;">Question 17</span>

  Which policy is used to capture host information on the Cisco Firepower Next Generation Intrusion Prevention System?

  A. Correlation<br>
  B. Intrusion<br>
  C. Access Control<br>
  D. Network Discovery<br>

  Answer: D

  Explanation

  The Firepower System uses network discovery and identity policies to collect host, application, and user data for traffic on your network. You can use certain types of discovery and identity data to build a comprehensive map of your network assets, perform forensic analysis, behavioral profiling, access control, and mitigate and respond to the vulnerabilities and exploits to which your organization is susceptible.

  You can configure your network discovery policy to perform host and application detection.

  Reference: [Introduction to Network Discovery and Identity](https://www.cisco.com/c/en/us/td/docs/security/firepower/640/configuration/guide/fpmc-config-guide-v64/introduction_to_network_discovery_and_identity.html)


- <span style="color: #008888; font-weight: bold;">Question 18</span>

  Which ASA deployment mode can provide separation of management on a shared appliance?

  A. DMZ multiple zone mode<br>
  B. transparent firewall mode<br>
  C. multiple context mode<br>
  D. routed mode<br>

  Answer: C

  Explanation

  You can partition a single ASA into multiple virtual devices, known as security contexts. Each context acts as an independent device, with its own security policy, interfaces, and administrators. Multiple contexts are similar to having multiple standalone devices.

  Reference: [Multiple Context Mode](https://www.cisco.com/c/en/us/td/docs/security/asa/asa97/configuration/general/asa-97-general-config/ha-contexts.html#ID-2171-0000019c)


- <span style="color: #008888; font-weight: bold;">Question 19</span>

  Refer to the exhibit. What is a result of the configuration?

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('page')"
      src    = "img/0619-ACL_DMZ.jpg"
      alt    = "text"
      title  = "text"
    />
  </figure>

  A. Traffic from the DMZ network is redirected<br>
  B. Traffic from the inside network is redirected<br>
  C. All TCP traffic is redirected<br>
  D. Traffic from the inside and DMZ networks is redirected<br>

  Answer: D

  Explanation

  The purpose of above commands is to redirect traffic that matches the ACL “redirect-acl” to the Cisco FirePOWER (SFR) module in the inline (normal) mode. In this mode, after the undesired traffic is dropped and any other actions that are applied by policy are performed, the traffic is returned to the ASA for further processing and ultimate transmission.

  The command “`service-policy global_policy global`” applies the policy to all of the interfaces.

  Reference: [Install and Configure a FirePOWER Services Module on an ASA Platform](https://www.cisco.com/c/en/us/support/docs/security/asa-firepower-services/118644-configure-firepower-00.html)


- <span style="color: #008888; font-weight: bold;">Question 20</span>

  Which policy represents a shared set of features or parameters that define the aspects of a managed device that are likely to be similar to other managed devices in a deployment?

  A. Group Policy<br>
  B. Access Control Policy<br>
  C. Device Management Policy<br>
  D. Platform Service Policy<br>

  Answer: D

  Explanation

  Cisco Firepower deployments can take advantage of platform settings policies. A platform settings policy is a shared set of features or parameters that define the aspects of a managed device that are likely to be similar to other managed devices in your deployment, such as time settings and external authentication. Examples of these platform settings policies are time and date settings, external authentication, and other common administrative features.

  A shared policy makes it possible to configure multiple managed devices at once, which provides consistency in your deployment and streamlines your management efforts. Any changes to a platform settings policy affects all the managed devices where you applied the policy. Even if you want different settings per device, you must create a shared policy and apply it to the desired device.

  For example, your organization’s security policies may require that your appliances have a “No Unauthorized Use” message when a user logs in. With platform settings, you can set the login banner once in a platform settings policy.

  Reference: [Platform Settings Policies](https://www.cisco.com/c/en/us/td/docs/security/firepower/620/configuration/guide/fpmc-config-guide-v62/platform_settings_policies_for_managed_devices.html)

  Therefore the answer should be “Platform Settings Policy”, not “Platform Service Policy” but it is the best answer here so we have to choose it.


- <span style="color: #008888; font-weight: bold;">Question 21</span>

  Which two tasks allow NetFlow on a Cisco ASA 5500 Series firewall? (Choose two)

  A. Enable NetFlow Version 9.<br>
  B. Create an ACL to allow UDP traffic on port 9996.<br>
  C. Apply NetFlow Exporter to the outside interface in the inbound direction.<br>
  D. Create a class map to match interesting traffic.<br>
  E. Define a NetFlow collector by using the flow-export command.<br>

  Answer: D E

  Explanation

  In order to configure NetFlow on Cisco ASA 5500 Series firewall, we need the following minimum steps:

  - 1\. Configuring NSEL <span style="color: #bb6600;">Collectors</span>:
    `flow-export destination interface-name [ipv4-address | hostname] udp-port`
    For example: `hostname (config)# flow-export destination inside 209.165.200.225 2002`
    - The `destination` keyword indicates that a NSEL collector is being configured. 
    - The `interface-name argument` is the name of the ASA and ASA Services Module interface through which the collector is reached. 
    - The `ipv4-address` argument is the IP address of the machine running the collector application. 
    - The `hostname` argument is the destination IP address or name of the collector. 
    - The `udp-port` argument is the UDP port number to which NetFlow packets are sent.
    (-> Therefore we only need to let the firewall know the IP address that the NetFlow “Collector” will be running on. We don’t need to apply the NetFlow Exporter to any interface -> Answer C is not correct)
  - 2\. Defines the <span style="color: #bb6600;">class map</span> that identifies **traffic** for which NSEL events need to be exported.
  - 3\. Defines the <span style="color: #bb6600;">policy map</span> to apply **flow-export actions** to the defined classes.
  - 4\. Adds or edits the <span style="color: #bb6600;">service policy</span> globally.

  An example of configuring NetFlow is shown below (using minimum configuration):

  ```text
  ASA(config)# flow-export destination inside 10.254.254.234 2055
  // Note: “inside” is the interface name of ASA through which the collector is reached
  ASA(config)# policy-map global_policy
  ASA(config-pmap)# class class-default
  ASA(config-pmap-c)# flow-export event-type all destination 10.254.254.234
  ASA(config)# service-policy global_policy global
  ```

  Reference: [Configuring Network Secure Event Logging (NSEL)](https://www.cisco.com/c/en/us/td/docs/security/asa/asa84/configuration/guide/asa_84_cli_config/monitor_nsel.html#23742)


- <span style="color: #008888; font-weight: bold;">Question 22</span>

  A mall provides security services to customers with a shared appliance. The mall wants separation of management on the shared appliance. Which ASA deployment mode meets these needs?

  A. routed mode<br>
  B. transparent mode<br>
  C. multiple context mode<br>
  D. multiple zone mode<br>

  Answer: C


- <span style="color: #008888; font-weight: bold;">Question 23</span>

  What is a characteristic of Firepower NGIPS inline deployment mode?

  A. ASA with Firepower module cannot be deployed.<br>
  B. It cannot take actions such as blocking traffic.<br>
  C. It is out-of-band from traffic.<br>
  D. It must have inline interface pairs configured.<br>

  Answer: D


- <span style="color: #008888; font-weight: bold;">Question 24</span>

  An engineer wants to generate NetFlow records on traffic traversing the Cisco ASA. Which Cisco ASA command must be used?

  A. `flow-export destination inside 1.1.1.1 2055`<br>
  B. `ip flow monitor input`<br>
  C. `ip flow-export destination 1.1.1.1 2055`<br>
  D. `flow exporter`<br>

  Answer: A

  Explanation

  The syntax of this command is: `flow-export destination interface-name [ipv4-address | hostname] udp-port`

  This command is used on Cisco ASA to configure <span style="color: #bb6600;">Network Secure Event Logging (NSEL) collector</span> to which NetFlow packets are sent. The destination keyword indicates that a NSEL collector is being configured.
  - The `interface-name` argument is the name of the ASA and ASA Services Module interface through which the collector is reached.
  - The `ipv4-address` argument is the IP address of the machine running the collector application.
  - The `hostname` argument is the destination IP address or name of the collector.
  - The `udp-port` argument is the UDP port number to which NetFlow packets are sent.

  You can configure a maximum of five collectors. After a collector is configured, template records are automatically sent to all configured NSEL collectors.

  Reference: [Configuring Network Secure Event Logging (NSEL)](https://www.cisco.com/c/en/us/td/docs/security/asa/asa84/configuration/guide/asa_84_cli_config/monitor_nsel.html)


- <span style="color: #008888; font-weight: bold;">Question 25</span>

  How many interfaces per bridge group does an ASA bridge group deployment support?

  A. up to 2<br>
  B. up to 4<br>
  C. up to 8<br>
  D. up to 16<br>

  Answer: B

  Explanation

  Each of the ASAs interfaces need to be grouped into one or more bridge groups. Each of these groups acts as an independent transparent firewall. It is not possible for one bridge group to communicate with another bridge group without assistance from an external router.

  As of 8.4(1) upto 8 bridge groups are supported with 2-4 interface in each group. Prior to this only one bridge group was supported and only 2 interfaces.

  Up to 4 interfaces are permitted per bridge–group (inside, outside, DMZ1, DMZ2)


- <span style="color: #008888; font-weight: bold;">Question 26</span>

  Which two application layer preprocessors are used by Firepower Next Generation Intrusion Prevention System? (Choose two)

  A. packet decoder<br>
  B. SIP<br>
  C. modbus<br>
  D. inline normalization<br>
  E. SSL<br>

  Answer: B E

  Explanation

  Application layer protocols can represent the same data in a variety of ways. The Firepower System provides application layer protocol decoders that normalize specific types of packet data into formats that the intrusion rules engine can analyze. Normalizing application-layer protocol encodings allows the rules engine to effectively apply the same content-related rules to packets whose data is represented differently and obtain meaningful results.

  Reference: [Application Layer Preprocessors](https://www.cisco.com/c/en/us/td/docs/security/firepower/60/configuration/guide/fpmc-config-guide-v60/Application_Layer_Preprocessors.html#ID-2244-0000080c)

  FirePower uses many preprocessors, including DNS, FTP/Telnet, SIP, SSL, SMTP, SSH preprocessors.


## 07. Email & Web

<span style="color: blue; font-weight: bold;">Quick summary</span>

Cisco Email Security includes advanced threat protection capabilities to detect, block, and remediate threats faster; prevent data loss; and secure important information in transit with end-to-end encryption.

With Cisco Email Security customers can:
- Detect and block more threats with superior threat intelligence from Talos.
- Combat ransomware hidden in attachments that evade initial detection with Cisco Advanced Malware Protection (AMP) and Cisco Threat Grid.
- Drop emails with risky links automatically or block access to newly infected sites with real-time URL analysis to protect against phishing and BEC.
- Prevent brand abuse and sophisticated identity-based email attacks with Cisco Domain Protection (CDP) and Cisco Advanced Phishing Protection (CAPP) services.
- Protect sensitive content in outgoing emails with Data Loss Prevention (DLP) and easy-to-use email encryption, all in one solution.
- Provide user behavior training with Cisco Security Awareness to help users work smarter and safer.
- Gain maximum deployment flexibility with a cloud, virtual, on-premises, or hybrid deployment or move to the cloud in phases.



- <span style="color: #008888; font-weight: bold;">Question 1</span>

  Which two features of Cisco Email Security can protect your organization against email threats? (Choose two)

  A. Time-based one-time passwords<br>
  B. Data loss prevention<br>
  C. Heuristic-based filtering<br>
  D. Geolocation-based filtering<br>
  E. NetFlow<br>

  Answer: B D

  Explanation

  Protect sensitive content in outgoing emails with Data Loss Prevention (DLP) and easy-to-use email encryption, all in one solution.

  Cisco Email Security appliance can now handle incoming mail connections and incoming messages from specific geolocations and perform appropriate actions on them, for example:
  - Prevent email threats coming from specific geographic regions.
  - Allow or disallow emails coming from specific geographic regions.

  Reference: [Getting Started with Cisco Email Security](https://www.cisco.com/c/en/us/td/docs/security/esa/esa11-0/user_guide_fs/b_ESA_Admin_Guide_11_0/b_ESA_Admin_Guide_chapter_00.html)


- <span style="color: #008888; font-weight: bold;">Question 2</span>

  Why would a user choose an on-premises ESA versus the CES solution?

  A. Sensitive data must remain onsite.<br>
  B. Demand is unpredictable.<br>
  C. The server team wants to outsource this service.<br>
  D. ESA is deployed inline.<br>

  Answer: A


- <span style="color: #008888; font-weight: bold;">Question 3</span>

  Which two features are used to configure Cisco ESA with a multilayer approach to fight viruses and malware? (Choose two)

  A. Sophos engine<br>
  B. white list<br>
  C. RAT<br>
  D. outbreak filters<br>
  E. DLP<br>

  Answer: A D

  Explanation

  Cisco ESA uses a multilayer approach to fight viruses and malware:
  - The first layer of defense consists of outbreak filters, which the appliance downloads from Cisco SenderBase. They contain a list of known bad mail servers. 
  - The second layer of defense is using antivirus signatures to scan quarantined emails, to ensure that they do not carry viruses into the network.
  - Cisco ESA also scans outbound emails to provide antivirus protection

  Reference: [Newer Cisco Validated Design Guides Available](https://www.cisco.com/c/dam/en/us/td/docs/solutions/CVD/Aug2013/CVD-EmailSecurityUsingCiscoESADesignGuide-AUG13.pdf)


- <span style="color: #008888; font-weight: bold;">Question 4</span>

  What is the purpose of the Decrypt for Application Detection feature within the WSA Decryption options?

  A. It decrypts HTTPS application traffic for unauthenticated users.<br>
  B. It alerts users when the WSA decrypts their traffic.<br>
  C. It decrypts HTTPS application traffic for authenticated users.<br>
  D. It provides enhanced HTTPS application detection for AsyncOS.<br>

  Answer: D

  Explanation

  Decryption policies define the handling of HTTPS traffic within the web proxy:
  - When to decrypt HTTPS traffic.
  - How to handle requests that use invalid or revoked security certificates.
  
  You can create decryption policies to handle HTTPS traffic in the following ways:
  - Pass through encrypted traffic
  - Decrypt traffic and apply the content-based access policies defined for HTTP traffic. This also makes malware scanning possible. -> Answer D is the best answer
  - Drop the HTTPS connection
  - Monitor the request (take no final action) as the web proxy continues to evaluate the request against policies that may lead to a final drop, pass through, or decrypt action.

  Reference: [Create Decryption Policies to Control HTTPS Traffic](https://www.cisco.com/c/en/us/td/docs/security/wsa/wsa11-7/user_guide/b_WSA_UserGuide_11_7/b_WSA_UserGuide_11_7_chapter_01011.html)


- <span style="color: #008888; font-weight: bold;">Question 5</span>

  Which two statements about a Cisco WSA configured in Transparent mode are true? (Choose two)

  A. It can handle explicit HTTP requests.<br>
  B. It requires a PAC file for the client web browser.<br>
  C. It requires a proxy for the client web browser.<br>
  D. WCCP v2-enabled devices can automatically redirect traffic destined to port 80.<br>
  E. Layer 4 switches can automatically redirect traffic destined to port 80.<br>

  Answer: D E

  Explanation

  The WSA can be configured for "**transparent**" or "**forward proxy**" mode. 
  - transport mode: the WSA will respond to both transparent and explicit HTTP requests (explicit - ONLY responds to explicit HTTP requests)
  - forward proxy mode: WSA, as a web proxy, will have two sets of TCP sockets per client request

  WSA HTTP proxy obtains the client's request can be defined as one of two ways: Transparently or Explicitly.
  - Transparent
    - Layer 4 Switch (PBR): A Layer 4 switch is used to redirect based on destination port 80
    - WCCP: A WCCP v2 enabled device (typically a router, switch, PIX, or ASA) redirects port 80
    - Bridged mode: Dual NICs, virtually paired. Traffic goes in one NIC and out the other (not available)
  - Explicitly
    - Browser Configured: Client browser is explicitly configured to use a proxy
    - .PAC file configured: Client browser is explicitly configured to us a .PAC file, which in turn, references the proxy

  Reference: [Difference between Transparent and Forward proxy mode](https://www.cisco.com/c/en/us/support/docs/security/web-security-appliance/117940-qa-wsa-00.html)


- <span style="color: #008888; font-weight: bold;">Question 6</span>

  Which action controls the amount of URI text that is stored in Cisco WSA logs files?

  A. Configure the `datasecurityconfig` command<br>
  B. Configure the `advancedproxyconfig` command with the HTTPS subcommand<br>
  C. Configure a small log-entry size.<br>
  D. Configure a maximum packet size.<br>

  Answer: B

  Handle personally identifiable information with care: If you choose to decrypt an end-user’s HTTPS session, the Web Security appliance access logs and reports may contain personally identifiable information. The Administrator can configure how much URI text is stored in the logs using the `advancedproxyconfig` CLI command and the HTTPS subcommand. You can log the entire URI, or a partial form of the URI with the query portion removed. However, even when you choose to strip the query from the URI, personally identifiable information may still remain.

  Reference: [Create Decryption Policies to Control HTTPS Traffic](https://www.cisco.com/c/en/us/td/docs/security/wsa/wsa11-0/user_guide/b_WSA_UserGuide/b_WSA_UserGuide_chapter_01110.html#con_1230713)


- <span style="color: #008888; font-weight: bold;">Question 7</span>

  An engineer is configuring a Cisco ESA and wants to control whether to accept or reject email messages to a recipient address. Which list contains the allowed recipient addresses?

  A. SAT<br>
  B. BAT<br>
  C. HAT<br>
  D. RAT<br>

  Answer: D

  Explanation

  Each and every listener associated w/ two tables
  - HAT (Host Access Table)
  - RAT (Remote Access Table)


- <span style="color: #008888; font-weight: bold;">Question 8</span>

  Which two services must remain as on-premises equipment when a hybrid email solution is deployed? (Choose two)

  A. DDoS<br>
  B. antispam<br>
  C. antivirus<br>
  D. encryption<br>
  E. DLP<br>

  Answer: D E

  Explanation

  Cisco Hybrid Email Security is a unique service offering that combines a cloud-based email security deployment with an appliance-based email security deployment (on premises) to provide maximum choice and control for your organization. The cloud-based infrastructure is typically used for inbound email cleansing, while the on-premises appliances provide granular control – protecting sensitive information with data loss prevention (DLP) and encryption technologies.

  Reference: [Cisco  Cloud/Hybrid  Secure  Email  Overview](https://www.cisco.com/c/dam/en/us/td/docs/security/ces/overview_guide/Cisco_Cloud_Hybrid_Email_Security_Overview_Guide.pdf)


- <span style="color: #008888; font-weight: bold;">Question 9</span>

  Which Talos reputation center allows you to track the reputation of IP addresses for email and web traffic?

  A. IP Blacklist Center<br>
  B. File Reputation Center<br>
  C. AMP Reputation Center<br>
  D. IP and Domain Reputation Center<br>

  Answer: D

  Explanation

  Talos’ <span style="color: #bb6600;">IP and Domain Data Center</span> is the world’s most comprehensive real-time threat detection network. The data is made up of daily security intelligence across millions of deployed web, email, firewall and IPS appliances. Talos detects and correlates threats in real time using the largest threat detection network in the world spanning web requests, emails, malware samples, open-source data sets, endpoint intelligence, and network intrusions. The <span style="color: #bb6600;">Email and Web Traffic Reputation Center</span> is able to transform some of Talos’ data into actionable threat intelligence and tools to improve your security posture.


- <span style="color: #008888; font-weight: bold;">Question 10</span>

  Which proxy mode must be used on Cisco WSA to redirect TCP traffic with WCCP?

  A. transparent<br>
  B. redirection<br>
  C. forward<br>
  D. proxy gateway<br>

  Answer: A

  Explanation

  There are two possible methods to accomplish the redirection of traffic to Cisco WSA: <span style="color: #bb6600;">transparent proxy mode</span> and <span style="color: #bb6600;">explicit proxy mode</span>.

  In a <span style="color: #bb6600;">transparent proxy</span> deployment, a WCCP v2-capable network device redirects all TCP traffic with a destination of port 80 or 443 to Cisco WSA, without any configuration on the client. The transparent proxy deployment is used in this design, and the Cisco ASA firewall is used to redirect traffic to the appliance because all of the outbound web traffic passes through the device and is generally managed by the same operations staff who manage Cisco WSA.

  In an <span style="color: #bb6600;">explicit proxy</span> deployment, a client application, such as a web browser, is configured to use an HTTP proxy, such as Cisco WSA. 

  Reference: [Web Security Using Cisco WSA - Technology Design Guide](https://www.cisco.com/c/dam/en/us/td/docs/solutions/CVD/Aug2013/CVD-WebSecurityUsingCiscoWSADesignGuide-AUG13.pdf)


- <span style="color: #008888; font-weight: bold;">Question 11</span>

  After deploying a Cisco ESA on your network, you notice that some messages fail to reach their destinations. Which task can you perform to determine where each message was lost?

  A. Configure the `trackingconfig` command to enable message tracking.<br>
  B. Generate a system report.<br>
  C. Review the log files.<br>
  D. Perform a trace.<br>

  Answer: A

  Explanation

  Message tracking helps resolve help desk calls by giving a detailed view of message flow. For example, if a message was not delivered as expected, you can determine if it was found to contain a virus or placed in a spam quarantine — or if it is located somewhere else in the mail stream.

  Reference: [User Guide for AsyncOS 12.0 for Cisco Email Security Appliances - GD (General Deployment)](https://www.cisco.com/c/en/us/td/docs/security/esa/esa12-0/user_guide/b_ESA_Admin_Guide_12_0/b_ESA_Admin_Guide_12_0_chapter_011110.html)


- <span style="color: #008888; font-weight: bold;">Question 12</span>

  What is the primary benefit of deploying an ESA in hybrid mode?

  A. You can fine-tune its settings to provide the optimum balance between security and performance for your environment<br>
  B. It provides the lowest total cost of ownership by reducing the need for physical appliances<br>
  C. It provides maximum protection and control of outbound messages<br>
  D. It provides email security while supporting the transition to the cloud<br>

  Answer: D

  Explanation

  Cisco Hybrid Email Security is a unique service offering that facilitates the deployment of your email security infrastructure both on premises and in the cloud. You can change the number of on-premises versus cloud users at any time throughout the term of your contract, assuming the total number of users does not change. This allows for deployment flexibility as your organization’s needs change.


- <span style="color: #008888; font-weight: bold;">Question 13</span>

  What is the primary role of the Cisco Email Security Appliance?

  A. Mail Submission Agent<br>
  B. Mail Transfer Agent<br>
  C. Mail Delivery Agent<br>
  D. Mail User Agent<br>

  Answer: B

  Explanation

  Cisco Email Security Appliance (ESA) protects the email infrastructure and employees who use email at work by filtering unsolicited and malicious email before it reaches the user. Cisco ESA easily integrates into existing email infrastructures with a high degree of flexibility. It does this by acting as a Mail Transfer Agent (MTA) within the email-delivery chain. Another name for an MTA is a mail relay.

  Reference: [Email Security Using Cisco ESA Deployment Guide](https://www.cisco.com/c/dam/en/us/td/docs/solutions/SBA/February2013/Cisco_SBA_BN_EmailSecurityUsingCiscoESADeploymentGuide-Feb2013.pdf)


- <span style="color: #008888; font-weight: bold;">Question 14</span>

  Which technology is used to improve web traffic performance by proxy caching?

  A. WSA<br>
  B. Firepower<br>
  C. FireSIGHT<br>
  D. ASA<br>

  Answer: A


- <span style="color: #008888; font-weight: bold;">Question 15</span>

  In which two ways does a system administrator send web traffic transparently to the Web Security Appliance? (Choose two)

  A. configure Active Directory Group Policies to push proxy settings<br>
  B. configure policy-based routing on the network infrastructure<br>
  C. reference a Proxy Auto Config file<br>
  D. configure the proxy IP address in the web-browser settings<br>
  E. use Web Cache Communication Protocol<br>

  Answer: B E


## 08. Cloud Security

<span style="color: blue; font-weight: bold;">Cloud Quick Summary</span>

<span style="color: blue;">Types of clouds</span>

There are 4 types of cloud:
- <span style="color: #bb6600">Private Cloud</span>: cloud that is dedicated solely to one organization. Advantages of Private Clouds are high security, Regulatory compliance, Flexibility to respond to changing needs. Drawbacks of private cloud are cost, mobile difficulty,
- <span style="color: #bb6600">Public Cloud</span>: cloud that is delivered via the Internet and shared across organizations. Examples of public clouds are Amazon Web Services, Microsoft Azure, and Google Cloud Platform. Advantages of public cloud are lower costs, Freedom from maintenance. Drawbacks of public cloud are Lack of security, minimal technical control
- <span style="color: #bb6600">Hyrid Cloud</span>: any environment that uses both public and private clouds. Confidential operations like financial reporting, for example, can be run on a private cloud. High-volume, less sensitive workloads like web-based email – or even temporary workloads such as development and test – can run on a public cloud.
- <span style="color: #bb6600">Community Cloud</span>: a recent variation on the private cloud model that can be only accessible by group of organizations. It shares the infrastructure between several organizations from a specific community. It may be managed internally by organizations or by the third-party.

<span style="color: blue;">Cloud services</span>

There are 3 main types of as-a-Service solutions: SaaS, PaaS and IaaS
- <span style="color: #bb6600;">SaaS (Software as a Service)</span>: SaaS uses the web to deliver applications that are managed by a third-party vendor and whose interface is accessed on the clients’ side. Most SaaS applications can be run directly from a web browser without any downloads or installations required, although some require plugins.
- <span style="color: #bb6600;">PaaS (Platform as a Service)</span>: are used for applications, and other development, while providing cloud components to software. What developers gain with PaaS is a framework they can build upon to develop or customize applications. PaaS makes the development, testing, and deployment of applications quick, simple, and cost-effective. With this technology, enterprise operations, or a third-party provider, can manage OSes, virtualization, servers, storage, networking, and the PaaS software itself. Developers, however, manage the applications. PaaS provides everything except applications.
- <span style="color: #bb6600;">IaaS (Infrastructure as a Service)</span>: self-service models for accessing, monitoring, and managing remote datacenter infrastructures, such as compute (virtualized or bare metal), storage, networking, and networking services (e.g. firewalls). Instead of having to purchase hardware outright, users can purchase IaaS based on consumption, similar to electricity or other utility billing.

<figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://www.securitytut.com/scor/cloud-questions')"
    src    = "img/0800-Cloud_Computing_SaaS_PaaS_IaaS.jpg"
    alt    = "Cloud Computing: SaaS, PaaS, & IaaS"
    title  = "Cloud Computing: SaaS, PaaS, & IaaS"
  />
</figure>


- <span style="color: #008888; font-weight: bold;">Question 1</span>

  Which technology reduces data loss by identifying sensitive information stored in public computing environments?

  A. Cisco SDA<br>
  B. Cisco Firepower<br>
  C. Cisco HyperFlex<br>
  D. Cisco Cloudlock<br>

  Answer: D

  Explanation

  Cisco Cloudlock is a cloud-based Cloud Access Security Broker (CASB) and cloud cybersecurity platform that helps organizations securely leverage use of applications in the cloud.  Cisco Cloudlock delivers visibility and control for  cloud application environments across users, data, and applications.  Depending upon the applicable Cisco Cloudlock subscription, customers may be afforded the right on an opt-in basis to access and use Cisco Umbrella features as part of  their Cisco Cloudlock subscription, including by way of example, DNS monitoring, Umbrella App Discovery and Umbrella Cloud Malware.

  The core functionality of Cisco Cloudlock covers the following four use cases:
  - Data Loss Prevention (DLP)
  - User and Entity Behavior Analytics (UEBA)
  - Apps Firewall (Apps Firewall)
  - App Discovery (App Discovery)

  Reference: [Offer Description: Cisco Cloudlock](https://www.cisco.com/c/dam/en_us/about/doing_business/legal/OfferDescriptions/cisco-cloudlock-offer-description.pdf)


- <span style="color: #008888; font-weight: bold;">Question 2</span>

  Which deployment model is the most secure when considering risks to cloud adoption?

  A. Public Cloud<br>
  B. Hybrid Cloud<br>
  C. Community Cloud<br>
  D. Private Cloud<br>

  Answer: D


- <span style="color: #008888; font-weight: bold;">Question 3</span>

  In which cloud services model is the tenant responsible for virtual machine OS patching?

  A. IaaS<br>
  B. UCaaS<br>
  C. PaaS<br>
  D. SaaS<br>

  Answer: A

  Explanation

  Only in On-site (on-premises) and IaaS we (tenant) manage O/S (Operating System).

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
      onclick= "window.open('https://www.securitytut.com/scor/cloud-questions')"
      src    = "img/0803-iaas_paas-saas-compare.png"
      alt    = "Cloud Computing: SaaS, PaaS, & IaaS"
      title  = "Cloud Computing: SaaS, PaaS, & IaaS"
    />
  </figure>


- <span style="color: #008888; font-weight: bold;">Question 4</span>

  Which cloud service model offers an environment for cloud consumers to develop and deploy applications without needing to manage or maintain the underlying cloud infrastructure?

  A. PaaS<br>
  B. XaaS<br>
  C. IaaS<br>
  D. SaaS<br>

  Answer: A

  Explanation

  Cloud computing can be broken into the following three basic models:

  - Infrastructure as a Service (IaaS): IaaS describes a cloud solution where you are renting infrastructure. You purchase virtual power to execute your software as needed. This is much like running a virtual server on your own equipment, except you are now running a virtual server on a virtual disk. This model is similar to a utility company model because you pay for what you use.
  - Platform as a Service (PaaS): PaaS provides everything except applications. Services provided by this model include all phases of the system development life cycle (SDLC) and can use application programming interfaces (APIs), website portals, or gateway software. These solutions tend to be proprietary, which can cause problems if the customer moves away from the provider’s platform.
  - Software as a Service (SaaS): SaaS is designed to provide a complete packaged solution. The software is rented out to the user. The service is usually provided through some type of front end or web portal. While the end user is free to use the service from anywhere, the company pays a peruse fee.

  Reference: CCNP and CCIE Security Core SCOR 350-701 Official Cert Guide


- <span style="color: #008888; font-weight: bold;">Question 5</span>

  What does the Cloudlock Apps Firewall do to mitigate security concerns from an application perspective?

  A. It allows the administrator to quarantine malicious files so that the application can function, just not maliciously.<br>
  B. It discovers and controls cloud apps that are connected to a company’s corporate environment.<br>
  C. It deletes any application that does not belong in the network.<br>
  D. It sends the application information to an administrator to act on.<br>

  Answer: B


- <span style="color: #008888; font-weight: bold;">Question 6</span>

  Which solution protects hybrid cloud deployment workloads with application visibility and segmentation?

  A. Nexus<br>
  B. Stealthwatch<br>
  C. Firepower<br>
  D. Tetration<br>

  Answer: D

  Explanation

  Cisco Tetration offers holistic workload protection for multicloud data centers by enabling a zero-trust model using segmentation. This approach allows you to identify security incidents faster, contain lateral movement, and reduce your attack surface.

  Reference: [Hybrid Cloud Workload Protecction](https://www.cisco.com/c/en_sg/products/data-center-analytics/tetration-analytics/index.html)


- <span style="color: #008888; font-weight: bold;">Question 7</span>

  In a PaaS model, which layer is the tenant responsible for maintaining and patching?

  A. hypervisor<br>
  B. virtual machine<br>
  C. network<br>
  D. application<br>

  Answer: D


- <span style="color: #008888; font-weight: bold;">Question 8</span>

  On which part of the IT environment does DevSecOps focus?

  A. application development<br>
  B. wireless network<br>
  C. data center<br>
  D. perimeter network<br>

  Answer: A


- <span style="color: #008888; font-weight: bold;">Question 9</span>

  What is the function of Cisco Cloudlock for data security?

  A. data loss prevention<br>
  B. controls malicious cloud apps<br>
  C. detects anomalies<br>
  D. user and entity behavior analytics<br>

  Answer: A



