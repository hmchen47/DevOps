# Quiz Set 2


## 05. Python & API

- <span style="color: blue; font-weight: bold;">Question 1</span>

  Which API is used for Content Security?

  A. NX-OS API<br>
  B. IOS XR API<br>
  C. OpenVuln API<br>
  D. AsyncOS API<br>

  Answer: D


- <span style="color: blue; font-weight: bold;">Question 2</span>

  Which two request of REST API are valid on the Cisco ASA Platform? (Choose two)

  A. put<br>
  B. options<br>
  C. get<br>
  D. push<br>
  E. connect<br>

  Answer: A C

  Explanation

    The ASA REST API gives you programmatic access to managing individual ASAs through a Representational State Transfer (REST) API. The API allows external clients to perform CRUD (Create, Read, Update, Delete) operations on ASA resources; it is based on the HTTPS protocol and REST methodology.
    All API requests are sent over HTTPS to the ASA, and a response is returned.

    Request Structure

    Available request methods are:
    GET – Retrieves data from the specified object.
    PUT – Adds the supplied information to the specified object; returns a 404 Resource Not Found error if the object does not exist.
    POST – Creates the object with the supplied information.
    DELETE – Deletes the specified object.
    PATCH – Applies partial modifications to the specified object.

    Reference: https://www.cisco.com/c/en/us/td/docs/security/asa/api/qsg-asa-api.html


- <span style="color: blue; font-weight: bold;">Question 3</span>

  Refer to the exhibit.

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('https://www.securitytut.com/scor/python-api')"
      src    = "503-Python_script_DNA_Center_API.jpg"
      alt    = "Python Script w/ DNA Center API"
      title  = "Python Script w/ DNA Center API"
    />
  </figure>

  What is the result of this Python script of the Cisco DNA Center API?

  A. adds authentication to a switch
  B. adds a switch to Cisco DNA Center
  C. receives information about a switch

  Answer: B


- <span style="color: blue; font-weight: bold;">Question 4</span>

  Refer to the exhibit.

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('https://www.securitytut.com/scor/python-api')"
      src    = "504-Cisco_security_appliance_API.jpg"
      alt    = "Python Script w/ Security Appliance API"
      title  = "Python Script w/ Security Appliance API"
    />
  </figure>

  What does the API do when connected to a Cisco security appliance?

  A. get the process and PID information from the computers in the network
  B. create an SNMP pull mechanism for managing AMP
  C. gather network telemetry information from AMP for endpoints
  D. gather the network interface information about the computers AMP sees

  Answer: D

  Explanation

    The call to API of “https://api.amp.cisco.com/v1/computers” allows us to fetch list of computers across your organization that Advanced Malware Protection (AMP) sees.

    Reference: https://api-docs.amp.cisco.com/api_actions/details?api_action=GET+%2Fv1%2Fcomputers&api_host=api.apjc.amp.cisco.com&api_resource=Computer&api_version=v1



## 06. Firewall & Intrusion Prevention

- <span style="color: blue; font-weight: bold;">Question 1</span>

  Which feature requires a network discovery policy on the Cisco Firepower Next Generation Intrusion Prevention System?

  A. Security Intelligence<br>
  B. Impact Flags<br>
  C. Health Monitoring<br>
  D. URL Filtering<br>

  Answer: B


- <span style="color: blue; font-weight: bold;">Question 2</span>

  Which two deployment model configurations are supported for Cisco FTDv in AWS? (Choose two)

  A. Cisco FTDv configured in routed mode and managed by an FMCv installed in AWS<br>
  B. Cisco FTDv with one management interface and two traffic interfaces configured<br>
  C. Cisco FTDv configured in routed mode and managed by a physical FMC appliance on premises<br>
  D. Cisco FTDv with two management interfaces and one traffic interface configured<br>
  E. Cisco FTDv configured in routed mode and IPv6 configured<br>

  Answer: A C


- <span style="color: blue; font-weight: bold;">Question 3</span>

  Which option is the main function of Cisco Firepower impact flags?

  A. They alert administrators when critical events occur.<br>
  B. They highlight known and suspected malicious IP addresses in reports.<br>
  C. They correlate data about intrusions and vulnerability.<br>
  D. They identify data that the ASA sends to the Firepower module.<br>

  Answer: C


- <span style="color: blue; font-weight: bold;">Question 4</span>

  On Cisco Firepower Management Center, which policy is used to collect health modules alerts from managed devices?

  A. health policy<br>
  B. system policy<br>
  C. correlation policy<br>
  D. access control policy<br>
  E. health awareness policy<br>

  Answer: A


- <span style="color: blue; font-weight: bold;">Question 5</span>

  Which license is required for Cisco Security Intelligence to work on the Cisco Next Generation Intrusion Prevention System?

  A. control<br>
  B. malware<br>
  C. URL filtering<br>
  D. protect<br>

  Answer: D


- <span style="color: blue; font-weight: bold;">Question 6</span>

  Which two are valid suppression types on a Cisco Next Generation Intrusion Prevention System? (Choose two)

  A. Port<br>
  B. Rule<br>
  C. Source<br>
  D. Application<br>
  E. Protocol<br>

  Answer: B C


- <span style="color: blue; font-weight: bold;">Question 7</span>

  Which feature is configured for managed devices in the device platform settings of the Firepower Management Center?

  A. quality of service<br>
  B. time synchronization<br>
  C. network address translations<br>
  D. intrusion policy<br>

  Answer: B


- <span style="color: blue; font-weight: bold;">Question 8</span>

  Which information is required when adding a device to Firepower Management Center?

  A. username and password<br>
  B. encryption method<br>
  C. device serial number<br>
  D. registration key<br>

  Answer: D


- <span style="color: blue; font-weight: bold;">Question 9</span>

  Which two deployment modes does the Cisco ASA FirePower module support? (Choose two)

  A. transparent mode<br>
  B. routed mode<br>
  C. inline mode<br>
  D. active mode<br>
  E. passive monitor-only mode<br>

  Answer: C E

  Explanation

    You can configure your ASA FirePOWER module using one of the following deployment models:

    You can configure your ASA FirePOWER module in either an inline or a monitor-only (inline tap or passive) deployment.

    Reference: https://www.cisco.com/c/en/us/td/docs/security/asa/asa92/asdm72/firewall/asa-firewall-asdm/modules-sfr.html


- <span style="color: blue; font-weight: bold;">Question 10</span>

  The Cisco ASA must support TLS proxy for encrypted Cisco Unified Communications traffic. Where must the ASA be added on the Cisco UC Manager platform?

  A. Certificate Trust List<br>
  B. Endpoint Trust List<br>
  C. Enterprise Proxy Service<br>
  D. Secured Collaboration Proxy<br>

  Answer: A


## 07. Email & Web




## 08. Cloud Security





