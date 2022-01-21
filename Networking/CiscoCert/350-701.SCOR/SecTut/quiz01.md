# Quiz Set 1

## 01. Security Concepts

- <span style="color: blue; font-weight: bold;">Question 1</span>

  In which form of attack is alternate encoding, such as hexadecimal representation, most often observed?

  A. Smurf<br>
  B. distributed denial of service<br>
  C. cross-site scripting<br>
  D. rootkit exploit<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 2</span>

  Which flaw does an attacker leverage when exploiting SQL injection vulnerabilities?

  A. user input validation in a web page or web application<br>
  B. Linux and Windows operating systems<br>
  C. database<br>
  D. web page images<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 3</span>

  Which two prevention techniques are used to mitigate SQL injection attacks? (Choose two)

  A. Check integer, float, or Boolean string parameters to ensure accurate values.<br>
  B. Use prepared statements and parameterized queries.<br>
  C. Secure the connection between the web and the app tier.<br>
  D. Write SQL code instead of using object-relational mapping libraries.<br>
  E. Block SQL code execution in the web application database login.<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 4</span>

  Which two endpoint measures are used to minimize the chances of falling victim to phishing and social engineering attacks? (Choose two)

  A. Patch for cross-site scripting.<br>
  B. Perform backups to the private cloud.<br>
  C. Protect against input validation and character escapes in the endpoint.<br>
  D. Install a spam and virus email filter.<br>
  E. Protect systems with an up-to-date antimalware program.<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 5</span>

  Which two mechanisms are used to control phishing attacks? (Choose two)

  A. Enable browser alerts for fraudulent websites.<br>
  B. Define security group memberships.<br>
  C. Revoke expired CRL of the websites.<br>
  D. Use antispyware software.<br>
  E. Implement email filtering techniques.<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 6</span>

  Which two behavioral patterns characterize a ping of death attack? (Choose two)

  A. The attack is fragmented into groups of 16 octets before transmission.<br>
  B. The attack is fragmented into groups of 8 octets before transmission.<br>
  C. Short synchronized bursts of traffic are used to disrupt TCP connections.<br>
  D. Malformed packets are used to crash systems.<br>
  E. Publicly accessible DNS servers are typically used to execute the attack.<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 7</span>

  Which two preventive measures are used to control cross-site scripting? (Choose two)

  A. Enable client-side scripts on a per-domain basis.<br>
  B. Incorporate contextual output encoding/escaping.<br>
  C. Disable cookie inspection in the HTML inspection engine.<br>
  D. Run untrusted HTML input through an HTML sanitization engine.<br>
  E. Same Site cookie attribute should not be used.<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 8</span>

  What is the difference between deceptive phishing and spear phishing?

  A. Deceptive phishing is an attacked aimed at a specific user in the organization who holds a C-level role.<br>
  B. A spear phishing campaign is aimed at a specific person versus a group of people.<br>
  C. Spear phishing is when the attack is aimed at the C-level executives of an organization.<br>
  D. Deceptive phishing hijacks and manipulates the DNS server of the victim and redirects the user to a false webpage.<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 9</span>

  Which attack is commonly associated with C and C++ programming languages?<br>
  A. cross-site scripting<br>
  B. water holing<br>
  C. DDoS<br>
  D. buffer overflow<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 10</span>

  What is a language format designed to exchange threat intelligence that can be transported over the TAXII protocol?

  A. STIX<br>
  B. XMPP<br>
  C. pxGrid<br>
  D. SMTP<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 11</span>

  Which two capabilities does TAXII support? (Choose two)

  A. Exchange<br>
  B. Pull messaging<br>
  C. Binding<br>
  D. Correlation<br>
  E. Mitigating<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 12</span>

  Which two risks is a company vulnerable to if it does not have a well-established patching solution for endpoints? (Choose two)

  A. exploits<br>
  B. ARP spoofing<br>
  C. denial-of-service attacks<br>
  D. malware<br>
  E. eavesdropping<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 13</span>

  Which PKI enrollment method allows the user to separate authentication and enrollment actions and also provides an option to specify HTTP/TFTP commands to perform file retrieval from the server?

  A. url<br>
  B. terminal<br>
  C. profile<br>
  D. selfsigned<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 15</span>

  What are two rootkit types? (Choose two)

  A. registry<br>
  B. virtual<br>
  C. bootloader<br>
  D. user mode<br>
  E. buffer mode<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 16</span>

  Which form of attack is launched using botnets?

  A. EIDDOS<br>
  B. virus<br>
  C. DDOS<br>
  D. TCP flood<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 17<span style="color: blue; font-weight: bold;">

  Which threat involves software being used to gain unauthorized access to a computer system?

  A. virus<br>
  B. NTP amplification<br>
  C. ping of death<br>
  D. HTTP flood<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 18</span>

  Which type of attack is social engineering?

  A. trojan<br>
  B. phishing<br>
  C. malware<br>
  D. MITM<br>

  Answer:

## 02. Encryption

<span style="color: cyan; font-weight: bold;">Quick summary</span>

Advanced Encryption Standard (AES) is a symmetric key cipher. This means the same secret key is used for both encryption and decryption, and both the sender and receiver of the data need a copy of the key. Symmetric keys are better suited to internal encryption. The advantage of symmetric systems like AES is their speed. Because a symmetric key algorithm requires less computational power than an asymmetric one, it’s faster and more efficient to run.

AES is also characterized as a block cipher. In this type of cipher, the information to be encrypted (known as plaintext) is divided into sections called blocks. The AES encryption algorithm encrypts and decrypts data in blocks of 128 bits (block size). It can do this using 128-bit, 192-bit, or 256-bit keys. AES using 128-bit keys is often referred to as AES-128, and so on.

AES is the successor of Data Encryption Standard (DES), which uses a block size of 64 bits and key size of 56 bits. Nowadays, AES is still considered secured if implemented properly.

Triple DES (3DES) – also known as Triple Data Encryption Algorithm (TDEA) – is a way of using DES encryption three times. But even Triple DES was proven ineffective against brute force attacks. AES was introduced in 2001 to replace 3DES.

Asymmetric cryptography (or “public key cryptography”) is a cryptographic system that uses keypairs (a private key and a public key). The public key is shared widely, while the private key must be kept
completely secret.

- <span style="color: blue; font-weight: bold;">Question 1</span>

  Which two key and block sizes are valid for AES? (Choose two)

  A. 64-bit block size, 112-bit key length<br>
  B. 64-bit block size, 168-bit key length<br>
  C. 128-bit block size, 192-bit key length<br>
  D. 128-bit block size, 256-bit key length<br>
  E. 192-bit block size, 256-bit key length<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 2</span>

  Which two descriptions of AES encryption are true? (Choose two)

  A. AES is less secure than 3DES.<br>
  B. AES is more secure than 3DES.<br>
  C. AES can use a 168-bit key for encryption.<br>
  D. AES can use a 256-bit key for encryption.<br>
  E. AES encrypts and decrypts a key three times in sequence.<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 3</span>

  Which algorithm provides encryption and authentication for data plane communication?

  A. AES-GCM<br>
  B. SHA-96<br>
  C. AES-256<br>
  D. SHA-384<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 4</span>

  Elliptic curve cryptography is a stronger more efficient cryptography method meant to replace which current encryption technology?

  A. 3DES<br>
  B. RSA<br>
  C. DES<br>
  D. AES<br>

  Answer:

## 03. VPNs

<span style="color: cyan; font-weight: bold;">Quick summary</span>

**DMVPN** provides full meshes connectivity with simple configuration of hub and spoke. DMVPN forms IPsec tunnel over dynamically/statically addresses spokes.

**GETVPN** (Group Encrypted Transport VPN) is a tunnel-less VPN technology meant for private networks like MPLS VPN or Private WAN where we use a single SA (Security Association) for all routers in a group. It is scalable for any-to-any connectivity and encryption.

**FlexVPN** uses a new key management protocol – IKEv2

DMVPN, FlexVPN and GETVPN comparison:

<figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 500px;"
    onclick= "window.open('page')"
    src    = "img/300-DMVPN_FlexVPN_GETVPN_comparison.jpg"
    alt    = "Comparisons of DMVPN, FlexVPN, and GETVPN"
    title  = "Comparisons of DMVPN, FlexVPN, and GETVPN"
  />
</figure>

- <span style="color: blue; font-weight: bold;">Question 1</span>

  What is the result of running the `crypto isakmp key ciscXXXXXXXX address 172.16.0.0` command?

  A. authenticates the IKEv2 peers in the 172.16.0.0/16 range by using the key ciscXXXXXXXX<br>
  B. authenticates the IP address of the 172.16.0.0/32 peer by using the key ciscXXXXXXXX<br>
  C. authenticates the IKEv1 peers in the 172.16.0.0/16 range by using the key ciscXXXXXXXX<br>
  D. secures all the certificates in the IKE exchange by using the key ciscXXXXXXXX<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 2</span>

  Which technology must be used to implement secure VPN connectivity among company branches over a private IP cloud with any-to-any scalable connectivity?

  A. DMVPN<br>
  B. FlexVPN<br>
  C. IPsec DVTI<br>
  D. GET VPN<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 3</span>

  Which two conditions are prerequisites for stateful failover for IPsec? (Choose two)

  A. Only the IKE configuration that is set up on the active device must be duplicated on the standby device; the IPsec configuration is copied automatically<br>
  B. The active and standby devices can run different versions of the Cisco IOS software but must be the same type of device.<br>
  C. The IPsec configuration that is set up on the active device must be duplicated on the standby device<br>
  D. Only the IPsec configuration that is set up on the active device must be duplicated on the standby device; the IKE configuration is copied automatically.<br>
  E. The active and standby devices must run the same version of the Cisco IOS software and must be the same type of device.<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 4</span>

  Which VPN technology can support a multivendor environment and secure traffic between sites?

  A. SSL VPN<br>
  B. GET VPN<br>
  C. FlexVPN<br>
  D. DMVPN<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 5</span>

  A network engineer is configuring DMVPN and entered the `crypto isakmp key cisc0380739941 address 0.0.0.0` command on hostA. The tunnel is not being established to hostB. What action is needed to authenticate the VPN?

  A. Change isakmp to ikev2 in the command on hostA.
  B. Enter the command with a different password on hostB.
  C. Enter the same command on hostB.
  D. Change the password on hostA to the default password.

  Answer:

- <span style="color: blue; font-weight: bold;">Question 6</span>

  Refer to the exhibit.

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 500px;"
      onclick= "window.open('page')"
      src    = "img/306-site_to_site_VPN_isakmp.jpg"
      alt    = "Log messages of Site-to-Site CPN"
      title  = "Log messages of Site-to-Site CPN"
    />
  </figure>

  A network administrator configured a site-to-site VPN tunnel between two Cisco IOS routers, and hosts are unable to communicate between two sites of VPN. The network administrator runs the debug crypto isakmp sa command to track VPN status. What is the problem according to this command output?

  A. hashing algorithm mismatch<br>
  B. encryption algorithm mismatch<br>
  C. authentication key mismatch<br>
  D. interesting traffic was not applied<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 7</span>

  What is a difference between FlexVPN and DMVPN?

  A. DMVPN uses IKEv1 or IKEv2, FlexVPN only uses IKEv1<br>
  B. DMVPN uses only IKEv1 FlexVPN uses only IKEv2<br>
  C. FlexVPN uses IKEv2, DMVPN uses IKEv1 or IKEv2<br>
  D. FlexVPN uses IKEv1 or IKEv2, DMVPN uses only IKEv2<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 8</span>

  Which protocol provides the strongest throughput performance when using Cisco AnyConnect VPN?

  A. TLSv1.2<br>
  B. TLSv1.1<br>
  C. BJTLSv1<br>
  D. DTLSv1<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 9</span>

  What is a commonality between DMVPN and FlexVPN technologies?

  A. FlexVPN and DMVPN use IS-IS routing protocol to communicate with spokes<br>
  B. FlexVPN and DMVPN use the new key management protocol<br>
  C. FlexVPN and DMVPN use the same hashing algorithms<br>
  D. IOS routers run the same NHRP code for DMVPN and FlexVPN<br>

  Answer:

## 04. Software Defined Network (SDN)

<span style="color: blue; font-weight: bold;">SDN Quick Summary</span>

Most traditional devices use a distributed architecture, in which each control plane is resided in a networking device. Therefore they need to communicate with each other via messages to work correctly.

In contrast to distributed architecture, centralized (or controller-based) architectures centralizes the control of networking devices into one device, called SDN controller. The SDN controller has a global view of the network, and it uses common management protocols to monitor and configure the network devices. An example of SDN is Cisco ACI.

As we took the control planes off networking devices but not data planes so we need a way to communicate with them. So we put a southbound interface (SBI) at the bottom of SDN controller for this task. An SBI communicates with the devices via an application programming interface (API).

<figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 300px;"
    onclick= "window.open('https://www.securitytut.com/scor/software-defined-network-sdn')"
    src    = "img/400-SDN_controller_based_architecture.jpg"
    alt    = "Architecture of SDN Controller"
    title  = "Architecture of SDN Controller"
  />
</figure>

Now, in turn, the networking administrators and SDN applications want to control the controller! So the controller need a **northbound interface** (NBI) to communicate with us. The NBI applications included various network services, including network virtualization, dynamic virtual network provisioning, firewall monitoring, user identity management and access policy control.

<figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 150px;"
    onclick= "window.open('https://www.securitytut.com/scor/software-defined-network-sdn')"
    src    = "img/403-Southbound_Northbound_APIs.jpg"
    alt    = "API - Southbound and Northbound"
    title  = "API - Southbound and Northbound"
  />
</figure>

SDN northbound APIs are usually RESTful APIs used to communicate between the SDN Controller and the services and applications running over the network. OpenFlow and NETCONF are Southbound APIs used for most SDN implementations.

- <span style="color: blue; font-weight: bold;">Question 1</span>

  The main function of northbound APIs in the SDN architecture is to enable communication between which two areas of a network?

  A. SDN controller and the cloud<br>
  B. management console and the SDN controller<br>
  C. management console and the cloud<br>
  D. SDN controller and the management solution<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 2</span>

  Which two features of Cisco DNA Center are used in a Software Defined Network solution? (Choose two)

  A. accounting<br>
  B. assurance<br>
  C. automation<br>
  D. authentication<br>
  E. encryption<br>

  Answer:

- <span style="color: blue; font-weight: bold;">Question 3</span>

  Which functions of an SDN architecture require southbound APIs to enable communication?
  A. SDN controller and the network elements
  B. management console and the SDN controller
  C. management console and the cloud
  D. SDN controller and the cloud

  Answer:
