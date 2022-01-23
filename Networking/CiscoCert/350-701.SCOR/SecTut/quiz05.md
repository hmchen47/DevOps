# Quiz Set 5


## 17. Security Products & Solutions

<span style="color: blue; font-weight: bold;">Quick summary</span>

- StealWatch: performs security analytics by collecting network flows via NetFlow
- ESA: email security solution which protects against email threats like ransomware, business email compromise, phishing, whaling, and many other email-driven attacks
- AMP for Endpoints (AMP4E): provides malware protection on endpoints
- Umbrella: provides DNS protection by blocking malicious destinations using DNS
- Firepower Threat Defense (FTD): provides a comprehensive suite of security features such as firewall capabilities, monitoring, alerts, Intrusion Detection System (IDS) and Intrusion Prevention System (IPS).
- Cisco Cloudlock: Secure your cloud users, data, and applications with the cloud-native CASB and cloud cybersecurity platform. Cisco Cloudlock provides visibility and compliance checks, protects data against misuse and exfiltration, and provides threat protections against malware like ransomware.

**Cisco SteathWatch**

Stealthwatch is the visibility and security analytics solution that collects and analyzes network data from the existing network infrastructure. Stealthwatch analyzes industry standard NetFlow data from Cisco and other vendors Routers, Switches, Firewalls, and other network devices to detect advanced and persistent security threats such as internally spreading malware, data leakage, botnet command and control traffic and network reconnaissance.

The Cisco Identity Services Engine (ISE) solution supplements Stealthwatch NetFlowbased behavioral threat detection data with contextual information such as user identity, user authorization level, device-type, and posture. Together Stealthwatch and Cisco ISE present network security analysts with a view integrating NetFlow data and contextual information enabling the security analyst to detect and discern the potential severity of threats in a timely, efficient, and cost-effective manner.

Stealthwatch components include:
- Stealthwatch Management Console: security management system that allows network administrators to define, configure, and monitor multiple distributed Stealthwatch Flow Collectors from a single location. It uses graphical representations of network traffic, identity information, customized summary reports, and integrated security and network intelligence for comprehensive analysis.
- Flow Collector: leverages enterprise telemetry such as NetFlow, IPFIX (Internet Protocol Flow Information Export), and other types of flow data from existing infrastructure such as routers, switches, firewalls, endpoints, and other network infrastructure devices. The Flow Collector can also receive and collect telemetry from proxy data sources, which can be analyzed by the cloud-based, multilayered machine learning engine, Cognitive Intelligence, for deep visibility into both web and network traffic.
- Flow Sensor (optional): produces telemetry for segments of the switching and routing infrastructure that can’t generate NetFlow natively. It also provides visibility into the application layer data and provides additional security context to enhance the Stealthwatch security analytics. It can analyze encrypted traffic.
- UDP Director: simplifies the collection and distribution of network and security data across the enterprise. It helps reduce the processing power on network routers and switches by receiving essential network and security information from multiple locations and then forwarding it to a single data stream to one or more destinations.

<figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick= "window.open('https://www.securitytut.com/scor/security-products-solutions')"
    src    = "img/1700-SteathWatch_Components.jpg"
    alt    = "StealthWatch Components"
    title  = "StealthWatch Components"
  />
</figure>

Stealthwatch offers different deployment models:
- On-premises as a hardware appliance or a virtual machine called Stealthwatch Enterprise
- Cloud-delivered as a software-as-a-service (SaaS) solution called Stealthwatch Cloud.

Cisco Stealthwatch Cloud: Available as an SaaS product offer to provide visibility and threat detection within public cloud infrastructures such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).

**Cisco Cognitive Threat Analytics** helps you quickly detect and respond to sophisticated, clandestine attacks that are already under way or are attempting to establish a presence within your environment. The solution automatically identifies and investigates suspicious or malicious web-based traffic. It identifies both potential and confirmed threats, allowing you to quickly remediate the infection and reduce the scope and damage of an attack, whether it’s a known threat campaign that has spread across multiple organizations or a unique threat you’ve never seen before.

<figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick= "window.open('https://www.securitytut.com/scor/security-products-solutions')"
    src    = "img/1700-Cognitive-Threat-Analytics-Health-Status.jpg"
    alt    = "Cognitive Threat Analytics Health Status"
    title  = "Cognitive Threat Analytics Health Status"
  />
</figure>


- <span style="color: blue; font-weight: bold;">Question 1</span>

  How does Cisco Stealthwatch Cloud provide security for cloud environments?

  A. It delivers visibility and threat detection.<br>
  B. It prevents exfiltration of sensitive data.<br>
  C. It assigns Internet-based DNS protection for clients and servers.<br>
  D. It facilitates secure connectivity between public and private networks.<br>

  Answer: 
  

- <span style="color: blue; font-weight: bold;">Question 2</span>

  What are two Detection and Analytics Engines of Cognitive Threat Analytics? (Choose two)

  A. data exfiltration<br>
  B. command and control communication<br>
  C. intelligent proxy<br>
  D. snort<br>
  E. URL categorization<br>

  Answer: 
  

- <span style="color: blue; font-weight: bold;">Question 3</span>

  Which network monitoring solution uses streams and pushes operational data to provide a near real-time view of activity?

  A. SNMP<br>
  B. SMTP<br>
  C. syslog<br>
  D. model-driven telemetry<br>

  Answer: 
  

- <span style="color: blue; font-weight: bold;">Question 4</span>

  What provides visibility and awareness into what is currently occurring on the network?

  A. CMX<br>
  B. WMI<br>
  C. Prime Infrastructure<br>
  D. Telemetry<br>

  Answer: 
  

- <span style="color: blue; font-weight: bold;">Question 5</span>

  What can be integrated with Cisco Threat Intelligence Director to provide information about security threats, which allows the SOC to proactively automate responses to those threats?

  A. Cisco Umbrella<br>
  B. External Threat Feeds<br>
  C. Cisco Threat Grid<br>
  D. Cisco Stealthwatch<br>

  Answer: 


- <span style="color: blue; font-weight: bold;">Question 6</span>

  Which solution combines Cisco IOS and IOS XE components to enable administrators to recognize applications, collect and send network metrics to Cisco Prime and other third-party management tools, and prioritize application traffic?

  A. Cisco Security Intelligence<br>
  B. Cisco Application Visibility and Control<br>
  C. Cisco Model Driven Telemetry<br>
  D. Cisco DNA Center<br>

  Answer: 


- <span style="color: blue; font-weight: bold;">Question 7</span>

  Which two activities can be done using Cisco DNA Center? (Choose two)

  A. DHCP<br>
  B. Design<br>
  C. Accounting<br>
  D. DNS<br>
  E. Provision<br>

  Answer: 


- <span style="color: blue; font-weight: bold;">Question 8</span>

  What must be used to share data between multiple security products?

  A. Cisco Rapid Threat Containment<br>
  B. Cisco Platform Exchange Grid<br>
  C. Cisco Advanced Malware Protection<br>
  D. Cisco Stealthwatch Cloud<br>

  Answer: 


- <span style="color: blue; font-weight: bold;">Question 9</span>

  Which Cisco product is open, scalable, and built on IETF standards to allow multiple security products from Cisco and other vendors to share data and interoperate with each other?

  A. Advanced Malware Protection<br>
  B. Platform Exchange Grid<br>
  C. Multifactor Platform Integration<br>
  D. Firepower Threat Defense<br>

  Answer: 
  

- <span style="color: blue; font-weight: bold;">Question 10</span>

  What is a feature of the open platform capabilities of Cisco DNA Center?

  A. intent-based APIs<br>
  B. automation adapters<br>
  C. domain integration<br>
  D. application adapters<br>

  Answer: 


- <span style="color: blue; font-weight: bold;">Question 11</span>

  What is the function of the Context Directory Agent?

  A. maintains users’ group memberships<br>
  B. relays user authentication requests from Web Security Appliance to Active Directory<br>
  C. reads the Active Directory logs to map IP addresses to usernames<br>
  D. accepts user authentication requests on behalf of Web Security Appliance for user identification<br>

  Answer: 
  


## 18. 18. Drag Drop

- <span style="color: blue; font-weight: bold;">Question 1</span>

  Drag and drop the Firepower Next Generation Intrusion Prevention System detectors from the left onto the correct definitions on the right.

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.securitytut.com/scor/drag-drop-questions')"
      src    = "img/1801-Firepower_detectors.jpg"
      alt    = "Firepower Detector"
      title  = "Firepower Detector"
    />
  </figure>

  Answer:
  

- <span style="color: blue; font-weight: bold;">Question 2</span>

  Drag and drop the capabilities from the left onto the correct technologies on the right.

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.securitytut.com/scor/drag-drop-questions')"
      src    = "img/1802-Security_Applications.jpg"
      alt    = "Security Applications"
      title  = "Security Applications"
    />
  </figure>

  Answer:


- <span style="color: blue; font-weight: bold;">Question 3</span>

  Drag and drop the descriptions from the left onto the correct protocol versions on the right.

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.securitytut.com/scor/drag-drop-questions')"
      src    = "img/1803-IKE_protocol_versions.jpg"
      alt    = "Security Applications"
      title  = "Security Applications"
    />
  </figure>

  Answer:


- <span style="color: blue; font-weight: bold;">Question 4</span>

  Drag and drop the steps from the left into the correct order on the right to enable AppDynamics to monitor an EC2 instance in Amazon Web Services.

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://www.securitytut.com/scor/drag-drop-questions')"
      src    = "img/1804-AppDynamics_monitor_EC2.jpg"
      alt    = "AppDynamics Monitor EC2"
      title  = "AppDynamics Monitor EC2"
    />
  </figure>

  Answer:


