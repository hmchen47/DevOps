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

- <span style="color: blue; font-weight: bold;">Question 1</span>

  Which IPS engine detects ARP spoofing?

  A. Atomic ARP Engine<br>
  B. Service Generic Engine<br>
  C. ARP Inspection Engine<br>
  D. AIC Engine<br>

  Answer: A


- <span style="color: blue; font-weight: bold;">Question 2</span>

  What is a characteristic of Dynamic ARP Inspection?

  A. DAI determines the validity of an ARP packet based on valid IP to MAC address bindings from the DHCP snooping binding database.<br>
  B. In a typical network, make all ports as trusted except for the ports connecting to switches, which are untrusted<br>
  C. DAI associates a trust state with each switch.<br>
  D. DAI intercepts all ARP requests and responses on trusted ports only.<br>

  Answer: A


- <span style="color: blue; font-weight: bold;">Question 3</span>

  What is a characteristic of traffic storm control behavior?

  A. Traffic storm control drops all broadcast and multicast traffic if the combined traffic exceeds the level within the interval.<br>
  B. Traffic storm control cannot determine if the packet is unicast or broadcast.<br>
  C. Traffic storm control monitors incoming traffic levels over a 10-second traffic storm control interval.<br>
  D. Traffic storm control uses the Individual/Group bit in the packet source address to determine if the packet is unicast or broadcast.<br>

  Answer: A


- <span style="color: blue; font-weight: bold;">Question 4</span>

  A malicious user gained network access by spoofing printer connections that were authorized using MAB on four different switch ports at the same time. What two catalyst switch security features will prevent further violations? (Choose two)

  A. DHCP Snooping<br>
  B. 802.1AE MacSec<br>
  C. Port security<br>
  D. IP Device track<br>
  E. Dynamic ARP inspection<br>
  F. Private VLANs<br>

  Answer: A E


- <span style="color: blue; font-weight: bold;">Question 5</span>

  Which command enables 802.1X globally on a Cisco switch?

  A. dot1x system-auth-control<br>
  B. dot1x pae authenticator<br>
  C. authentication port-control aut<br>
  D. aaa new-model<br>

  Answer: A


- <span style="color: blue; font-weight: bold;">Question 6</span>

  Which RADIUS attribute can you use to filter MAB requests in an 802.1 x deployment?

  A. 1<br>
  B. 2<br>
  C. 6<br>
  D. 31<br>

  Answer: C

  Explanation

  Because MAB uses the MAC address as a username and password, you should make sure that the RADIUS server can differentiate MAB requests from other types of requests for network access. This precaution will prevent other clients from attempting to use a MAC address as a valid credential. Cisco switches uniquely identify MAB requests by setting Attribute 6 (Service-Type) to 10 (Call-Check) in a MAB Access-Request message. Therefore, you can use Attribute 6 to filter MAB requests at the RADIUS server.

  Reference: https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/identity-based-networking-services/config_guide_c17-663759.html


- <span style="color: blue; font-weight: bold;">Question 7</span>

  A network administrator configures Dynamic ARP Inspection on a switch. After Dynamic ARP Inspection is applied, all users on that switch are unable to communicate with any destination. The network administrator checks the interface status of all interfaces, and there is no err-disabled interface. What is causing this problem?

  A. DHCP snooping has not been enabled on all VLANs.<br>
  B. The ip arp inspection limit command is applied on all interfaces and is blocking the traffic of all users.<br>
  C. Dynamic ARP Inspection has not been enabled on all VLANs<br>
  D. The no ip arp inspection trust command is applied on all user host interfaces<br>

  Answer: A

  Explanation

  Dynamic ARP inspection (DAI) is a security feature that validates ARP packets in a network. It intercepts, logs, and discards ARP packets with invalid IP-to-MAC address bindings. This capability protects the network from certain man-in-the-middle attacks. After enabling DAI, all ports become untrusted ports.

  DHCP snooping is enabled on a per-VLAN basis. By default, the feature is inactive on all VLANs. You can enable the feature on a single VLAN or a range of VLANs.

  Reference: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst6500/ios/12-2SX/configuration/guide/book/snoodhcp.html

  For example, in order to activate DHCP snooping on VLAN 2, we use the following command:

  ```texy
  SW1(config)#ip dhcp snooping vlan 2
  ```


- <span style="color: blue; font-weight: bold;">Question 8</span>

    Refer to the exhibit.

    ```text
    SwitchA(config)#interface gigabitethernet1/0/1
    SwitchA(config-if)#dot1x host-mode multi-host
    SwitchA(config-if)#dot1x timeout quiet-period 3
    SwitchA(config-if)#dot1x timeout tx-period 15
    SwitchA(config-if)#authentication port-control auto
    SwitchA(config-if)#switchport mode access
    SwitchA(config-if)#switchport access vlan 12
    ```

    An engineer configured wired 802.1x on the network and is unable to get a laptop to authenticate. Which port configuration is missing?

    A. authentication open<br>
    B. dotlx reauthentication<br>
    C. cisp enable<br>
    D. dot1x pae authenticator<br>

    Answer: D



## 11. Secure Network Access




## 12. Exfiltration Techniques



