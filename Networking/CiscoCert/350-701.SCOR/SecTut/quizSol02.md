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




## 07. Email & Web




## 08. Cloud Security





