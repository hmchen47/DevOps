# Quiz set 3


## 09. Identity Services Engine

- <span style="color: blue; font-weight: bold;">Question 1</span> An administrator wants to ensure that all endpoints are compliant before users are allowed access on the corporate network. The endpoints must have the corporate antivirus application installed and be running the latest build of Windows 10. What must the administrator implement to ensure that all devices are compliant before they are allowed on the network? A. Cisco Identity Services Engine and AnyConnect Posture module<br>
  B. Cisco Stealthwatch and Cisco Identity Services Engine integration<br>
  C. Cisco ASA firewall with Dynamic Access Policies configured<br>
  D. Cisco Identity Services Engine with PxGrid services enabled<br> Answer: A


- <span style="color: blue; font-weight: bold;">Question 2</span> An engineer must force an endpoint to re-authenticate an already authenticated session without disrupting the endpoint to apply a new or updated policy from ISE. Which CoA type achieves this goal? A. Port Bounce<br>
  B. CoA Terminate<br>
  C. CoA Reauth<br>
  D. CoA Session Query<br> Answer: C


- <span style="color: blue; font-weight: bold;">Question 3</span> Which two probes are configured to gather attributes of connected endpoints using Cisco Identity Services Engine? (Choose two) A. RADIUS<br>
  B. TACACS+<br>
  C. DHCP<br>
  D. sFlow<br>
  E. SMTP<br> Answer: A C


- <span style="color: blue; font-weight: bold;">Question 4</span> Which ID store requires that a shadow user be created on Cisco ISE for the admin login to work? A. RSA SecureID<br>
  B. Internal Database<br>
  C. Active Directory<br>
  D. LDAP<br> Answer: C


- <span style="color: blue; font-weight: bold;">Question 5</span> An engineer used a posture check on a Microsoft Windows endpoint and discovered that the MS17-010 patch was not installed, which left the endpoint vulnerable to WannaCry ransomware. Which two solutions mitigate the risk of this ransom ware infection? (Choose two) A. Configure a posture policy in Cisco Identity Services Engine to install the MS17-010 patch before allowing access on the network.<br>
  B. Set up a profiling policy in Cisco Identity Service Engine to check and endpoint patch level before allowing access on the network.<br>
  C. Configure a posture policy in Cisco Identity Services Engine to check that an endpoint patch level is met before allowing access on the network.<br>
  D. Configure endpoint firewall policies to stop the exploit traffic from being allowed to run and replicate throughout the network.<br>
  E. Set up a well-defined endpoint patching strategy to ensure that endpoints have critical vulnerabilities patched in a timely fashion.<br> Answer: A C Explanation A posture policy is a collection of posture requirements, which are associated with one or more identity groups, and operating systems. We can configure ISE to check for the Windows patch at Work Centers > Posture > Posture Elements > Conditions > File. In this example, we are going to use the predefined file check to ensure that our Windows 10 clients have the critical security patch installed to prevent the Wanna Cry malware. <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
      onclick= "window.open('page')"
      src    = "img/0905-ISE_Win10_patch.png"
      alt    = "ISE Windows 10 Patch Management"
      title  = "ISE Windows 10 Patch Management"
    />
  </figure> Reference: https://community.cisco.com/t5/security-documents/ise-posture-prescriptive-deployment-guide/ta-p/3680273


- <span style="color: blue; font-weight: bold;">Question 6</span> Which feature of Cisco ASA allows VPN users to be postured against Cisco ISE without requiring an inline posture node? A. RADIUS Change of Authorization<br>
  B. device tracking<br>
  C. DHCP snooping<br>
  D. VLAN hopping<br> Answer: A


- <span style="color: blue; font-weight: bold;">Question 7</span> What two mechanisms are used to redirect users to a web portal to authenticate to ISE for guest services? (Choose two) A. multiple factor auth<br>
  B. local web auth<br>
  C. single sign-on<br>
  D. central web auth<br>
  E. TACACS+<br> Answer: B D


- <span style="color: blue; font-weight: bold;">Question 8</span> For which two conditions can an endpoint be checked using ISE posture assessment? (Choose two) A. Windows service<br>
  B. computer identity<br>
  C. user identity<br>
  D. Windows firewall<br>
  E. default browser<br> Answer: A D


- <span style="color: blue; font-weight: bold;">Question 9</span> Which compliance status is shown when a configured posture policy requirement is not met? A. compliant<br>
  B. unknown<br>
  C. authorized<br>
  D. noncompliant<br> Answer: D Explanation Posture is a service in Cisco Identity Services Engine (Cisco ISE) that allows you to check the state, also known as posture, of all the endpoints that are connecting to a network for compliance with corporate security policies. A posture policy is a collection of posture requirements that are associated with one or more identity groups and operating systems. Posture-policy requirements can be set to mandatory, optional, or audit types in posture policies.
  - If a mandatory requirement fails, the user will be moved to Non-Compliant state
  - If an optional requirement fails, the user is allowed to skip the specified optional requirements and the user is moved to Compliant state This question did not clearly specify the type of posture policy requirement (mandatory or optional) is not met so the user can be in Non-compliant or compliant state. But “noncompliant” is the best answer here. Reference: https://www.cisco.com/c/en/us/td/docs/security/ise/1-3/admin_guide/b_ise_admin_guide_13/b_ise_admin_guide_sample_chapter_010111.html


- <span style="color: blue; font-weight: bold;">Question 10</span> Which benefit is provided by ensuring that an endpoint is compliant with a posture policy configured in Cisco ISE? A. It allows the endpoint to authenticate with 802.1x or MAB.<br>
  B. It verifies that the endpoint has the latest Microsoft security patches installed.<br>
  C. It adds endpoints to identity groups dynamically.<br>
  D. It allows CoA to be applied if the endpoint status is compliant.<br> Answer: B



## 10. Layer 2 Security




## 11. Secure Network Access




## 12. Exfiltration Techniques



