# Quiz set 3


## 09. Identity Services Engine

- <span style="color: #008888; font-weight: bold;">Question 1</span> 
  
  An administrator wants to ensure that all endpoints are compliant before users are allowed access on the corporate network. The endpoints must have the corporate antivirus application installed and be running the latest build of Windows 10. What must the administrator implement to ensure that all devices are compliant before they are allowed on the network? 
  
  A. Cisco Identity Services Engine and AnyConnect Posture module<br>
  B. Cisco Stealthwatch and Cisco Identity Services Engine integration<br>
  C. Cisco ASA firewall with Dynamic Access Policies configured<br>
  D. Cisco Identity Services Engine with PxGrid services enabled<br>
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 2</span>
  
  An engineer must force an endpoint to re-authenticate an already authenticated session without disrupting the endpoint to apply a new or updated policy from ISE. Which CoA type achieves this goal? 
  
  A. Port Bounce<br>
  B. CoA Terminate<br>
  C. CoA Reauth<br>
  D. CoA Session Query<br>
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 3</span>
  
  Which two probes are configured to gather attributes of connected endpoints using Cisco Identity Services Engine? (Choose two)
  
  A. RADIUS<br>
  B. TACACS+<br>
  C. DHCP<br>
  D. sFlow<br>
  E. SMTP<br>
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 4</span>
  
  Which ID store requires that a shadow user be created on Cisco ISE for the admin login to work?
  
  A. RSA SecureID<br>
  B. Internal Database<br>
  C. Active Directory<br>
  D. LDAP<br>
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 5</span>
  
  An engineer used a posture check on a Microsoft Windows endpoint and discovered that the MS17-010 patch was not installed, which left the endpoint vulnerable to WannaCry ransomware. Which two solutions mitigate the risk of this ransom ware infection? (Choose two)
  
  A. Configure a posture policy in Cisco Identity Services Engine to install the MS17-010 patch before allowing access on the network.<br>
  B. Set up a profiling policy in Cisco Identity Service Engine to check and endpoint patch level before allowing access on the network.<br>
  C. Configure a posture policy in Cisco Identity Services Engine to check that an endpoint patch level is met before allowing access on the network.<br>
  D. Configure endpoint firewall policies to stop the exploit traffic from being allowed to run and replicate throughout the network.<br>
  E. Set up a well-defined endpoint patching strategy to ensure that endpoints have critical vulnerabilities patched in a timely fashion.<br> 
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 6</span>
  
  Which feature of Cisco ASA allows VPN users to be postured against Cisco ISE without requiring an inline posture node?
  
  A. RADIUS Change of Authorization<br>
  B. device tracking<br>
  C. DHCP snooping<br>
  D. VLAN hopping<br>
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 7</span>
  
  What two mechanisms are used to redirect users to a web portal to authenticate to ISE for guest services? (Choose two)
  
  A. multiple factor auth<br>
  B. local web auth<br>
  C. single sign-on<br>
  D. central web auth<br>
  E. TACACS+<br>
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 8</span>
  
  For which two conditions can an endpoint be checked using ISE posture assessment? (Choose two)
  
  A. Windows service<br>
  B. computer identity<br>
  C. user identity<br>
  D. Windows firewall<br>
  E. default browser<br>
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 9</span>

  Which compliance status is shown when a configured posture policy requirement is not met?
  
  A. compliant<br>
  B. unknown<br>
  C. authorized<br>
  D. noncompliant<br>
  
  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 10</span>
  
  Which benefit is provided by ensuring that an endpoint is compliant with a posture policy configured in Cisco ISE?
  
  A. It allows the endpoint to authenticate with 802.1x or MAB.<br>
  B. It verifies that the endpoint has the latest Microsoft security patches installed.<br>
  C. It adds endpoints to identity groups dynamically.<br>
  D. It allows CoA to be applied if the endpoint status is compliant.<br>
  
  Answer:<br><br> 


## 10. Layer 2 Security

- <span style="color: #008888; font-weight: bold;">Question 1</span>

  Which IPS engine detects ARP spoofing?

  A. Atomic ARP Engine<br>
  B. Service Generic Engine<br>
  C. ARP Inspection Engine<br>
  D. AIC Engine<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 2</span>

  What is a characteristic of Dynamic ARP Inspection?

  A. DAI determines the validity of an ARP packet based on valid IP to MAC address bindings from the DHCP snooping binding database.<br>
  B. In a typical network, make all ports as trusted except for the ports connecting to switches, which are untrusted<br>
  C. DAI associates a trust state with each switch.<br>
  D. DAI intercepts all ARP requests and responses on trusted ports only.<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 3</span>

  What is a characteristic of traffic storm control behavior?

  A. Traffic storm control drops all broadcast and multicast traffic if the combined traffic exceeds the level within the interval.<br>
  B. Traffic storm control cannot determine if the packet is unicast or broadcast.<br>
  C. Traffic storm control monitors incoming traffic levels over a 10-second traffic storm control interval.<br>
  D. Traffic storm control uses the Individual/Group bit in the packet source address to determine if the packet is unicast or broadcast.<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 4</span>

  A malicious user gained network access by spoofing printer connections that were authorized using MAB on four different switch ports at the same time. What two catalyst switch security features will prevent further violations? (Choose two)

  A. DHCP Snooping<br>
  B. 802.1AE MacSec<br>
  C. Port security<br>
  D. IP Device track<br>
  E. Dynamic ARP inspection<br>
  F. Private VLANs<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 5</span>

  Which command enables 802.1X globally on a Cisco switch?

  A. `dot1x system-auth-control`<br>
  B. `dot1x pae authenticator`<br>
  C. `authentication port-control aut`<br>
  D. `aaa new-model`<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 6</span>

  Which RADIUS attribute can you use to filter MAB requests in an 802.1 x deployment?

  A. 1<br>
  B. 2<br>
  C. 6<br>
  D. 31<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 7</span>

  A network administrator configures Dynamic ARP Inspection on a switch. After Dynamic ARP Inspection is applied, all users on that switch are unable to communicate with any destination. The network administrator checks the interface status of all interfaces, and there is no err-disabled interface. What is causing this problem?

  A. DHCP snooping has not been enabled on all VLANs.<br>
  B. The `ip arp inspection limit` command is applied on all interfaces and is blocking the traffic of all users.<br>
  C. Dynamic ARP Inspection has not been enabled on all VLANs<br>
  D. The `no ip arp inspection trust` command is applied on all user host interfaces<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 8</span>

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

    A. `authentication open`<br>
    B. `dotlx reauthentication`<br>
    C. `cisp enable`<br>
    D. `dot1x pae authenticator`<br>

    Answer:<br><br> 



## 11. Secure Network Access

- <span style="color: #008888; font-weight: bold;">Question 1</span>

  Which SNMPv3 configuration must be used to support the strongest security possible?

    A.

    ```text
    asa-host(config)#snmp-server group myv3 v3 priv
    asa-host(config)#snmp-server user andy myv3 auth sha cisco priv des ciscXXXXXXXX
    asa-host(config)#snmp-server host inside 10.255.254.1 version 3 andy
    ```

    B.

    ```text
    asa-host(config)#snmp-server group myv3 v3 noauth
    asa-host(config)#snmp-server user andy myv3 auth sha cisco priv aes 256 ciscXXXXXXXX
    asa-host(config)#snmp-server host inside 10.255.254.1 version 3 andy
    ```

    C.

    ```text
    asa-host(config)#snmpserver group myv3 v3 noauth
    asa-host(config)#snmp-server user andy myv3 auth sha cisco priv 3des ciscXXXXXXXX
    asa-host(config)#snmp-server host inside 10.255.254.1 version 3 andy
    ```

    D.
    
    ```text
    asa-host(config)#snmp-server group myv3 v3 priv
    asa-host(config)#snmp-server user andy myv3 auth sha cisco priv aes 256 ciscXXXXXXXX
    asa-host(config)#snmp-server host inside 10.255.254.1 version 3 andy
    ```

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 2</span>

  Refer to the exhibit. Which command was used to generate this output and to show which ports are authenticating with dot1x or mab?

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('page')"
      src    = "img/1102-show_authentication_sessions.jpg"
      alt    = "Outout of show authentication sessions"
      title  = "Outout of show authentication sessions"
    />
  </figure>

  A. `show authentication registrations`<br>
  B. `show authentication method`<br>
  C. `show dot1x all`<br>
  D. `show authentication sessions`<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 3</span>

  What Cisco command shows you the status of an 802.1X connection on interface gi0/1?

  A. `show authorization status`<br>
  B. `show authen sess int gi0/1`<br>
  C. `show connection status gi0/1`<br>
  D. `show ver gi0/1`<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 4</span>

  Refer to the exhibit. What does the number 15 represent in this configuration?

  ```text
  snmp-server group SNMP v3 auth access 15
  ```

  A. privilege level for an authorized user to this router<br>
  B. access list that identifies the SNMP devices that can access the router<br>
  C. interval in seconds between SNMPv3 authentication attempts<br>
  D. number of possible failed attempts until the SNMPv3 user is locked out<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 5</span>

  Under which two circumstances is a CoA issued? (Choose two)

  A. A new authentication rule was added to the policy on the Policy Service node.<br>
  B. An endpoint is deleted on the Identity Service Engine server.<br>
  C. A new Identity Source Sequence is created and referenced in the authentication policy.<br>
  D. An endpoint is profiled for the first time.<br>
  E. A new Identity Service Engine server is added to the deployment with the Administration persona<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 6</span>

  Refer to the exhibit.

  ```text
  HQ_Router(config)#username admin5 privilege 5
  HQ_Router(config)#privilege interface level 5 shutdown
  HQ_Router(config)#privilege interface level 5 ip
  HQ_Router(config)#privilege interface level 5 description
  ```

  A network administrator configures command authorization for the admin5 user. What is the admin5 user able to do on HQ_Router after this configuration?

  A. set the IP address of an interface<br>
  B. complete no configurations<br>
  C. complete all configurations<br>
  D. add subinterfaces<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 7</span>

  A network engineer has entered the snmp-server user andy myv3 auth sha cisco priv aes 256 cisc0380739941 command and needs to send SNMP information to a host at 10.255.254.1. Which command achieves this goal?

  A. `snmp-server host inside 10.255.254.1 version 3 andy`<br>
  B. `snmp-server host inside 10.255.254.1 version 3 myv3`<br>
  C. `snmp-server host inside 10.255.254.1 snmpv3 andy`<br>
  D. `snmp-server host inside 10.255.254.1 snmpv3 myv3`<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 8</span>

  Which telemetry data captures variations seen within the flow, such as the packets TTL, IP/TCP flags, and payload length?

  A. interpacket variation<br>
  B. software package variation<br>
  C. flow insight variation<br>
  D. process details variation<br>

  Answer:<br><br> 



## 12. Exfiltration Techniques

- <span style="color: #008888; font-weight: bold;">Question 1</span>

  How is ICMP used an exfiltration technique?

  A. by flooding the destination host with unreachable packets<br>
  B. by sending large numbers of ICMP packets with a targeted hosts source IP address using an IP broadcast address<br>
  C. by encrypting the payload in an ICMP packet to carry out command and control tasks on a compromised host<br>
  D. by overwhelming a targeted host with ICMP echo-request packets<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 2</span>

  Which exfiltration method does an attacker use to hide and encode data inside DNS requests and queries?

  A. DNS tunneling<br>
  B. DNSCrypt<br>
  C. DNS security<br>
  D. DNSSEC<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 3</span>

  How is DNS tunneling used to exfiltrate data out of a corporate network?

  A. It corrupts DNS servers by replacing the actual IP address with a rogue address to collect information or start other attacks.<br>
  B. It encodes the payload with random characters that are broken into short strings and the DNS server rebuilds the exfiltrated data.<br>
  C. It redirects DNS requests to a malicious server used to steal user credentials, which allows further damage and theft on the network.<br>
  D. It leverages the DNS server by permitting recursive lookups to spread the attack to other DNS servers.<br>

  Answer:<br><br> 


- <span style="color: #008888; font-weight: bold;">Question 4</span>

  Which two characteristics of messenger protocols make data exfiltration difficult to detect and prevent? (Choose two)

  A. Outgoing traffic is allowed so users can communicate with outside organizations.<br>
  B. Malware infects the messenger application on the user endpoint to send company data.<br>
  C. Traffic is encrypted, which prevents visibility on firewalls and IPS systems.<br>
  D. An exposed API for the messaging platform is used to send large amounts of data.<br>
  E. Messenger applications cannot be segmented with standard network controls.<br>

  Answer:<br><br> 


