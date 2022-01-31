# SCOR 350-701 Notes

## Security Concepts

- Malware and exploits
  - malware:
    - malicious software
    - any software intentionally designed to cause damage to a computer, server, client, or computer network
  - most popular types of malware
    - virus: 1) the most common type of malware; 2) attach malicious code to clean code; 3) wait to be run
    - ransomeware: infect computer and display message demanding a fee to be paid
    - spyware: 1) secretely record everything user enter, upload, download and store on computers or mobile devices; 2) keep itself hidden
  - expolit: a code taking advantage of a software a software vulnerability or security flaw
  - endpoint risks as company vulnerable: 1) malware; 2) expolit


- SQL injection
  - occurred when asking a user for input
  - mitigate: 1) check parameters to ensure actual values; 2) use prepared statements amd parameterized queries


- Buffer overflow
  - the volume of data exceeds the storage capacity of the memory buffer
  - write the data to the buffer overwrites adjacent memory locations
  - commonly associated w/ C/C++


- rootkit
  - a program providing maliciously privileged access to a computer
  - types: 1) kernel; 2) user mode; 3) bootloader; 4) Memory rootkits


- botnet
  - a collection of internet-connected devices infected by malware
  - unauthorized access
  - malicious activities including credentials leaks, unauthorized access, data theft and DDoS attacks


- DoS and DDoS
  - ping of death behavior: 1) sending malformed or oversized packets w/ ping command; 2) packets fragmented into groups of 8 octets


- Social engineering
  - phishing
    - a form of social engineering
    - sending fraudulent communications usually through email
  - goals: 1) steal sensitive data or login information; 2) install malware
  - types of phishing
    - deceptive: steal people’s personal data or login credentials in a legitmate company
    - spear: designed to get a single recipient to respond
  - mitigation: 1) browser alert; 2) email filtering
  - endpoint mitigation: 1) spam & virus filter; 2) up-to-date antimalware


- Cross Site Script (XSS): 
  - web application gathering malicious data
  - usually gathered in the form of a hyperlink
  - click on this link from another website, instant message, or simply simply just reading a web board or email message.
  - encode the malicious portion of the link to the site in HEX (or other encoding methods)
  - prevention: 1) sanitize user input; 2) limit use of user-provided data; 3) utilize the content security policy
  - preventive measures: 1) client-side scripts on a per-domain basis; 2) contextual output encoding/escaping


- TAXII/STIX
  - TAXII (Trusted Automated Exchange of Indicator Information)
    - a transport mechanism (data exchange) of cyber threat intelligence information in STIX format
    - used to author and exchange STIX documents among participants
    - capabilities: 1) push messaging; 2) pull messaging; 3) discovery <- automated exchange
  - STIX (Structured Threat Information eXpression)
    - a standardized language developed in a collaborative way to represent structured information about cyber threats
    - shared, stored, and otherwise used in a consistent manner


## Integrity and Privacy

- Digital Certificate & PKI
  - Trustpoint (Cisco)
    - an abstract container to hold a certificate in IOS
    - capable of storing two active certificates at any given time: 1) CA certificate; 2) ID certificate issued by CA
    - enrollment modes: 1) terminal - manual; 2) SCEP - over HTTP; 3) profile - authentication + enrollment (providing an option to specify HTTP/TFTP commands to perform file retrieval from the Server)


- Cryptography
  - symmetric key cipher
    - same secrete key used for both encryption and decryption
    - same secrete key used by both sender and receiver
    - suited to internal encryption
    - pros: 1) faster; 2) efficient
    - Data Encryption Standard (DES)
      - encrypt and decrypt in blocks (block cipher): 64 bits block size
      - key size: 56 bits
    - Triple DES (3DES):
      - using DES 3 times
      - 2 ways: 1) 1st & 3rd w/ the same key, 2nd w/ different key; 2) 3 different keys
    - Advanced Encryption Standard (AES)
      - successor of DES
      - encrypt and decrypt in blocks (block cipher): 128 bits block size
      - key size: 128, 192, or 256 -> AES-128, AES-192, or AES-256
  - asymmetric key
    - public key cryptography
    - using keypairs (a private key and a public key)
    - Diffie-Hellman
    - RSA
    - Elliptic Curve Cryptography (ECC): smaller key sizes, faster computation,as well as memory, energy and bandwidth savings


## Virtual Private Networks

- IPsec
  - Phase 1: ISAKMP
    - modes: 1) main - 6 msgs; 2) quick - 4 msgs
    - preshared authentication 
      - global configuration mode
      - syntax: `crypto isakmp key enc-type-digit keystring {(address peer-address [mask]) | (ipv6 ipv6-address/ ipv6-prefix) | (hostname hostname)} [no-xauth]`
      - `enc-type-digit`: whether the password to be used is encrypted or unencrypted, 0 - unencrypted, 6 - encrypted
      - `keystring`: preshared key
      - `address`/`ipv6`: remote peer ISAKMP IP/IPv6 address
      - `hostname`: FQDN of the peer
      - same command on two end devices
      - debug msg: 'ISAKMP:(1002): retransmitting phase 1 MM_KEY_EXCH...' $\to$ sign of key mismatch
  - phase 2: IPsec
  - stateful failover
    - enable a router to continue processing and forwarding IPsec packets after outage occurs
    - two identical routers: 1) same type of device; 2) have the same CPU and memory; 3) either no encryption accelerator or identical encryption accelerators
    - duplicate IKE and IPsec configuration on active decvice on standby device


- HHS, TLS & DTLS
  - DTLS
    - UDP based
    - used for delay sensitive applications (voice and video)
    - strongest throughput performance


- DMVPN
  - full meshed connectivity
  - simple hub and spoke configuration
  - forming IPsec tunnel over dynamically/statically addresses spokes
  - tunneled VPN: IKEv1 (ISAKMP) & IKEv2


- FlexVPN
  - tunneled VPN: IKEv2
  - a standards-based solution interoperating with non-Cisco IKEv2 implementations
  - same as DMVPN
    - point-to-point GRE tunnels
    - spoke-to-spoke connectivity achieved with NHRP redirect message
    - IOS routers w/ the same NHRP code
    - Cisco’s proprietary technologies


- GETVPN (Group Encrypted Transport VPN)
  - a trunnel-less VPN
  - private IP transport, such as MPLS VPN or private WAN
  - single SA for all routers in a group
  - scalable for any-to-any connectivity and encryption
  - eliminate point-to-point tunnels and their associated overlay routing
  - group SA: group members (GMs) sharing a common security association (SA)


## Software Defined Network (SDN)

- SDN architecture
  - centralized architecture to control networking devices in one device
  - SDN controller
    - global view of the network
    - using common management protocols to monitor and configure the network devices
  - northbound interfact (NBI)
    - intent API
    - SDN controller communicating w/ network service applications, the management solution
    - applications for network services, including network virtualization, dynamic virtual network provisioning, firewall monitoring, user identity management and access policy control
    - usually RESTful APIs used to communicate between the SDN Controller and the services and applications running over the network
  - southbound interface (SBI)
    - SDN controller communicating w/ network devices via API
    - usually OpenFlow and NETCONF to communicate w/ network devices
  - eastbound interface (EBI)
  - wetbound interface (WBI)


- AsyncOS API
  - for Cisco Security Management appliances
  - a representational state transfer (REST) based set of operations
  - providing secure and authenticated access to the Security Management appliance reports, report counters, tracking, quarantine, and configuration
  - a role based system: the scope of API queries defined by the role of the user
  - Cisco Content Security Management Appliance -> Cisco Secure Email and Web Manager


- REST API
  - a.k.a. RESTful API
  - an application programming interface (API or web API) that conforms to the constraints of REST architectural style and allows for interaction with RESTful web services
  - request methods
    - `GET` − Provides a read only access to a resource.
    - `POST` − Used to create a new resource.
    - `DELETE` − Used to remove a resource.
    - `PUT` − Used to update a existing resource or create a new resource.
  - request methods for ASA REST API: 1) get; 2) put; 3) post; 4) delete; 5) patch


- Cisco device APIs
  - DNA Center API to add device: `post /dna/intent/api/v1/network-device`
  - AMP API to get computer info: `get https://api.amp.cisco.com/v1/computers`


## Cloud Concepts and Solutions

- Cisco DNA Center
  - the command and control center for Cisco DNA–based networks
  - helping IT to optimize network performance to dynamically meet business intent
  - features: 1) policy; 2) automation; 3) assurance


- Firepower Threat Denfence Virtual (FTDv)
  - the virtualized component of the Cisco NGFW solution The FTDv 
  - providing next-generation firewall services, including stateful firewalling, routing, VPN, Next-Generation Intrusion Prevention System (NGIPS), Application Visibility and Control (AVC), URL filtering, and Advanced Malware Protection (AMP)
  - managing the FTDv w/ FMC (either FMCv or physical FMC)
  - register and communicate with the FMC on the Management interface
  - FTDv for AWS
    - run as a guest in the AWS environment
    - interface requirements:
      - management interfaces: 2; one for FMC and one for diagnostics
      - traffic interface: 2 used to connect inside hosts to the public network


- ASAv on AWS
  - same software as physical Cisco ASAs
  - able to be deployed in the public AWS cloud
  - features:
    - Support for Amazon EC2 C5 instances
    - Deployment in the Virtual Private Cloud (VPC)
    - Enhanced networking (SR-IOV) where available
    - Deployment from Amazon Marketplace
    - Maximum of 4 vCPUs per instance
    - <span style="color: #bb6600;">User deployment of L3 networks</span>
    - <span style="color: #bb6600;">Routed mode (default)</span>


## Firwalls, IPS, EPP, and DER

- Firepower
  - devices
    - Classic devices run next-generation IPS (NGIPS) software: 1) Firepower 7000 & 8000; 2) NGIPSv; 3) ASA w/ Firepower services
    - Firepower Threat Defense Devices
  - features
    - appliance and System Management Features
    - features for Detecting, Preventing, and Processing Potential Threats
    - integration with External Tools

- Cisco ASA FirePOWER module
  - known as the ASA SFR, providing next-generation Firewall services, including
    - Next Generation Intrusion Prevention System (NGIPS)
    - Application Visibility and Control (AVC)
    - URL filtering
    - Advanced Malware Protection (AMP)
  - redirect traffic to the SFR module
    - 1\. select the traffic to redirect w/ ACL
    - 2\. create class-map to match the traffic
    - 3\. specify the deployment mode: passive (monitor-only) or inline (normal)
    - 4\. specify a location to apply the policy: `service-policy global_policy global` for global config


- Firepower Management Center (FMC)
  - an integrated suite of network security and traffic management products, deployed either on purpose-built platforms or as a software solution
  - typical deployment - multiple traffic-sensing managed devices installed on network segments monitor traffic for analysis and report to a manager:
    - Firepower Management Center
    - Firepower Device Manager
    - Adaptive Security Device Manager (ASDM)
  - network discovery & identity policies:
    - logging discovery and identity data allows you to take advantage of many features in the Firepower System
    - collect host, application, and user data for traffic on your network
  - network discovery policy
    - control how the system collects data on your organization’s network assets and which network segments and ports are monitored
    - multidomain deployment: each leaf domain has an independent network discovery policy
    - perform host and application detection
  - identity policy
    - realm: connection between the FMC and the user accounts on the servers you monitor
    - A realm consists of one or more LDAP or Microsoft Active Directory servers that share the same directory credentials.
  - impact flag: evaluating the impact of an intrusion on your network by <span style="trxt-decoration: underline;">correlating</span> intrusion data, network discovery data, and vulnerability information
  - health policy
    - using the health monitor to create a health policy (collection of tests)
    - configured health test criteria for several health modules (tests)
    - control which health modules against each of your appliances
    - configure the specific limits used in the tests run by each module
  - platform settings policy / platform service policy
    - a shared set of features or parameters that define the aspects of a managed device
    - likely to be similar to other managed devices in your deployment, such as time settings and external authentication
    - configure multiple managed devices at once
  - [add a device to the FMC](https://bit.ly/3GrpP4t)
    - web user interface: 1) Devices > Device Management; 2) 'Add' menu > Device; 3) Host = IP address or the hostname of the device added; 4) Display Name = name for the device; 5) <span style="color: #bb6600;">Registration Key</span> = the same registration key used when you configured the device to be managed by the FMC; 6) multidomain deployment, assign the device to a leaf Domain; 7) ... 
    - CLI:
      - register the device to a FireSIGHT Management Center using the `configure manager add` command
      - syntax: `configure manager add {hostname | IPv4_address | IPv6_address | DONTRESOLVE} reg_key [nat_id]`
  - application layer preprocessors
    - providing application layer protocol decoders that normalize specific types of packet data into formats that the intrusion rules engine can analyze
    -preprocessors: DEC/RPC, DNS, FTP/Telnet, HTTP, Sun RPC, <span style="color: #bb6600;">SIP</span>, GTP, IMAP, POP, SMTP, SSH, <span style="color: #bb6600;">SSL</span>


- Firepower Next-Generation IPS (NGIPS) threat appliance
  - providing network visibility, security intelligence, automation and advanced threat protection
  - operating in-line via Fail-To-Wire/Bypass network modules
  - security intelligence
    - TALOS Security Intelligence and Research Group:
    - vulnerability-focused IPS rules
    - embedded IP-, URL-, and DNS-based security intelligence
  - security automation
    - correlate intrusion events with your network’s vulnerabilities
    - analyze network’s weaknesses
    - recommends the appropriate security policies
  - features:
    - IPS rules: identify and block attack traffic
    - integrated defence: against advanced malware by advanced analysis of network and endpoint activity
    - sandboxing: using behavioral indicators to identify zero-day amd evasive attacks
  - suppression
    - suppressing intrusion event notification
    - useful for eliminating false positives
    - types: 1) a specific IP address or range of IP addresses; 2) a specific rule or preprocessor
  - traffic profile
    - a graph of network traffic based on connection data collected over a profiling time window (PTW)
    - presumably representing normal network traffic
    - detecting abnormal network traffic by evaluating new traffic against the profile 


- Firepower Threat Defence Devices
  - a next-generation firewall (NGFW) w/ NGIPS capabilities
  - features including site-to-site and remote access VPN, robust routing, NAT, clustering, and other optimizations in application inspection and access control


- ASA FirePOWER module
  - next-generation firewall services, including Next-Generation IPS (NGIPS), Application Visibility and Control (AVC), URL filtering, and Advanced Malware Protection (AMP)
  - single or multiple context mode, and in routed or transparent mode
  - deployment models:
    - inline mode: actual traffic is sent to the ASA FirePOWER module; configure **inline interface pairs**
    - monitor-only (inline tap or passive): a copy of the traffic is sent to the ASA FirePOWER module


- ASA in Cisco Unified Communications
  - Cisco UC proxy: terminate and reoriginate connections between a client and server
  - deliver a range of security functions such as traffic inspection, protocol conformance, and policy control to ensure security for the internal network
  - solutions:
    - TLS proxy:
      - decryption and inspection of Cisco Unified Communications encrypted signaling
      - store certificate trustpoints for the server and the client
    - Mobility Proxy: secure connectivity btw Cisco Unified Mobility Advantage server and Cisco Unified Mobile Communicator clients
    - Presence Federation Proxy: secure connectivity btw Cisco Unified Presence servers and Cisco/Microsoft Presence servers


- ASA
  - modes: transparent and routed
  - bridge group in transprent mode
    - group interfaces together in a bridge group to maximize the use of security contexts
    - configure multiple bridge groups, one for each network
    - each bridge group requires a management IP address
    - up to 4 interfaces are permitted per bridge–group (inside, outside, DMZ1, DMZ2)


- NetFlow
  - providing a set of IP services, including network traffic accounting, usage-based network billing, network planning, security, Denial of Service monitoring capabilities, and network monitoring
  - NetFlow Secure Event Logging (NSEL)
    - providing a stateful, IP flow tracking method that exports only those records that indicate significant events in a flow
    - flow-export actions: `flow-export event-type`
    - significant events: flow-create, flow-teardown, and flow-denied (excluding those flows denied by EtherType ACLs)
  - configure NetFlow on Cisco ASA 5500 Series firewall
    - 1\. Configuring NSEL **Collectors**: `flow-export destination interface-name [ipv4-address | hostname] udp-port`
    - 2\. Defines the **class map** that identifies traffic for which NSEL events need to be exported
    - 3\. Defines the **policy map** to apply flow-export actions to the defined classes
    - 4\. Adds or edits the service policy globally


- IOS zone-based firewall
  - A zone must be configured before interfaces can be assigned to the zone.
  - An interface can be assigned to only one security zone.






