# Security Fundamentals


## 01. Explain Common Threats Against On-premises and Cloud Environments


### Know Your Assets

- Assets
  - people: staffs including cybersecurity professionals
  - data: top security info
  - physical system


- Issues of assets
  - categories of assets: what types of assets, physical/software
  - responsibility:
    - who owns, maintain and use the assets
    - various names: owner, custodian, operators, administrator, end user, reader
  - sensitivity level


### Know Your Vulnerabilities

- Vulnerability sources
  - policy: people training
  - software: patch, e.g., operating systems
  - code design, protocol
  - network access
  - malware


### Know Your Threats

- Categories of threats
  - internal: people within an institute
  - external: black hat, white hat, gray hat, suicide hacker, script kiddie, cyber terrorist, state sponsored hacker, hacktivist


- Mitigation of threats
  - policies: stop people doing wrong thing, e.g., training
  - technical: NGFW, IDS/IPS, Web Content, email security, antivirus
  - physical: locks, keycard scanners, camera systems


### Virus, Worms, Trojan, and Malware

- Termonologies
  - virus
    - application, e.g., keylogger
    - replicate itself
  - worms
    - similar to virus
    - no end user to trigger but working on its own
  - trojans:
    - presenting itself as one application user needed
    - example: antivirus software


### Phishing and Social Engineering

- Vulnerability of people
  - phisinging: links in emails redirect to malicious websites
  - social engineering
    - research target company: dumpsters, websites, employees, tour company, etc.
    - choose victim: identify frustrated employees of target company
    - build relationship: develop relationship w/ target employee
    - exploit relationship: collect sensitive info and current technologies


### DDoS - Attacking Availability

- Denial od service (DoS) attacks
  - darknet:
    - internet where non-indexed w/ searching engine
    - requireing specific software to access
  - hacker as a service: taking down target website
  - ways to attack: social engineering, virus, etc.
  - typical attacks: TCP SYN requests, HTTP requests, Ping of death $\to$ buffer overflow


- Distributed Denial of Service (DDoS) attacks
  - botnet/zombie: infected computers around the world
  - flood the targets from these computers


### Spoofing and MitM Attacks

- MitM attacks
  - exfiltrate info


- spoofing attacks
  - known attacks: DNS, DHCP, MAC
  - redirect traffic by pretending as a real network service
  - mitigation: DAI, DHCP snooping


- CIA triad: principles of security infrastructure
  - confidentiality
  - integrity
  - availability




## 02. Compare Common Security Vulnerabilities


### Get to Know OWASP

- OWASP foundation
  - [Open Web Application Security Project](https://owasp.org/) (OWASP)
  - improving the security
  - some important projects
    - [OWASP Top 10](https://owasp.org/www-project-top-ten/): a standard awareness document for developers and web application security
    - [OWASP Cheat Sheet Series](https://owasp.org/www-project-cheat-sheets/): providing a set of simple good pracice guides for appplication developers and defenders to follow
    - [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/): the premier cybersecurity testing resource for web application developers and security professionals
    - [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/): attempting to detect publicly disclosed vulnerabilities contained within a project’s dependencies


### The SQL Injection’; SELECT * FROM table

- 3-tier application architecture
  - tiers: web, app, and db
  - typical data flow: web or mobile apps / Kiosk (frontend) $\leftrightarrow$ application server (backend) $\leftrightarrow$ SQL database
  - frontend: web browser
  - backend: analytics, customer support, shipping, etc.
  - SQL db: storing cell files w/ SQL


- SQL injection
  - code sending code to app server or db directly
  - malicious procedure
    - web input field w/ SQL code to query info, e.g. `SELECT * FROM Table`
    - possible SQL statements: `INSERT`, `DELETE`, `DROP`, etc.
    - retrieve/delete user's sensitive info or insert brough data
  - mitigation: backend validates the SQL statement


- Demo: SQL injection
  - resource: [SQL Injection exercise](https://www.hacksplaining.com/exercises/sql-injection#/start)
  - web input: email = `user@email.com` password = `password` $\to$ Unknown email or password

    ```shell
    Rendering login page.
    Checking supplied authentication details for user@email.com.
    Finding user in database.
    No such user, report this to the user (invalid credentials?).
    Rendering login page.
    ```

  - web input: email = `user@email.com` password = `password'` $\to$ An unexpected error occurred.
    - logs: The logs show a SQL syntax error. This indicates that the quote characterr messed somthing up in an unexpeccted way.

      ```shell
      Checking supplied authentication details for user@email.com.
      Finding user in database.
      An error occurred: PG::SyntaxError: ERROR: unterminated quoted string at or near 
        "'password'' limit 1" LINE 1: ...ers where email = 'user@email.com' and 
        password = 'password'... ^ : select * from users where email = 'user@email.com' 
        and password = 'password'' limit 1.
      Unable to login this user due to unexpected error.
      Rendering login page.
      ```

    - translated SQL code

      ```sql
      SELECT *
        FROM users
       WHERE email = 'user@email.com'
          AND pass  = 'password'' LIMIT 1
      ```
    
    - repeat the above input and observe the result
    - This behavior indicates that the application might be valuable to SQL INjection

      ```sql
      SELECT *
        FROM users
       WHERE email = 'user@email.com'
         AND pass  = 'password'' LIMIT 1
      ```

  - web input: email = `user@email.com` password = `' or 1=1--`
    - We successfully gained access to the application without having to guess the password using SQL Injection.

    ```sql
    SELECT *
      FROM users
     WHERE email = 'user@email.com'
       AND pass  = '' or 1=1--' LIMIT 1
    ```



### Cross-Site Scripting; var doCode{}

- Cross-site scripting
  - input field of web in 3-tier application w/ JS code, e.g., `<script> alert(); </script>`
  - JS code exected in web browser immediately
  - browser holding Cookie or token $\to$ probably sent to a malicious website
  - other possibilities: JS sending malicious data to server and DB 


- Demo: XSS attack
  - resource:
    - [Test Your XSS Skills Using Vulnerable Sites](https://bit.ly/3Eh9eix)
    - [Google XSS Game](https://xss-game.appspot.com/)
  - level 1:
    - input field: `<script>alert();</script>`
    - fire JS `alert` function 
    - related code snippet: [python code](src/02-l1-level.py)
  - level 2:
    - HTML code handling script text to handle script injection
    - input field: `<img src="" onerror="alert();" />`
    - sending JS code w/o `script` tag
    - related code snippets: [HTML](src/02-l2-index.html), [Python](src/02-l2-level.py), [JS](src/02-l2-post-store.js)



### Password Protection

- Password attacks
  - Infographic: Time it Takes a Hacker to Brute Force Your Password

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 450px;"
        onclick= "window.open('https://www.hivesystems.io/blog/are-your-passwords-in-the-green')"
        src    = "img/02-password.png"
        alt    = "The time it takes for a hacker to brute force your password - Hive Systems"
        title  = "The time it takes for a hacker to brute force your password - Hive Systems"
      />
    </figure>

  - dictionary attacks
    - dictionaries accessed w/ google search for download
    - password cheing: [have i been pwned?](https://haveibeenpwned.com/)
  - brute force attacks: using random number to try


- Password mitigation
  - policy
    - enforcing minimum number of characters, upper and lower cases, numbers, and symbols
    - period for password changes
    - not hard coding username and password
  - key vault:
    - apps login key vault
    - key vault returns password once key vault authenticated
  - environment variables for username and password
  - changing default username and password


### Plain-Text Protocols

- Demo: telnet as plain-text protocol
  - task:
    - telnet to a local router via telnet
    - wireshark to capture the traffic
  - topology: Pc <--> (e0/0) R1
  - launch Wireshark and start capturing traffic on the intf connected to the console
  - config R1

    ```shell
    R1$ sh ip int br

    Interface     IP-Address      OK? Method  Status                Protocol
    Ethernet0/0   10.10.21.153    YES manual  up                    up
    EThernet0/1   unassigned      YES unset   administratively down down
    ...

  - start a new session to connect to R1 from PC w/ telnet
    - Username = cisco, Password = cisco
  - Wireshark w/ filter = `telnet` 
    - entry w/ Source and Destination IP = 10.10.21.29
    - viewing the message with the packet
    - th username and password exposed
  - using SSH instead of telnet


- Demo: HTTP as plain-text protocol
  - app not designed to redirect HTTP to HTTPS web site
  - Azure and other cloud services providing a simple option to redirect the traffic


- Protocols to conquer plain-text protocols
  - telnet $\to$ SSH
  - SNMP $\to$ SNMPv3, Netconf/SSH, Restconf/HTTPS
  - HTTP $\to$ HTTPS



### The Buffer Overflow

- Buffer overflow attacks
  - web apps sending more data than the app server able to handle
  - embedded overflow data w/ JS/C/Java code to execute
  - one of the OWASP top 10


- Mitigation of buffer overflow
  - backend code working to prevent the issue
  - one simply solution by sending back a service denial response w/ buffer overflow message





## 03. Components of Cryptography



### Data Integrity

- Hash overview
  - verifying data integrity
  - example: ios image
    - verify downloaded  file in router: `R1# verify /md5 flash0:/vios-adventerprisesek9-m`
    - generate hash value and compare to the provided hash value in Cisco website
  - date sent to remote site and using hash to verify the data not been manipulated
  - [SHA256 Hash Generator](https://passwordsgenerator.net/sha256-hash-generator/)
    - paste text to input field > 'Generate' button > SHA256 Hash of the string
    - any change of text $\to$ the hash changed
  - [HMAC Generator / Tester Tool](https://freeformatter.com/hmac-generator.html)
    - paste text into input field
    - secret key: the element making the hash only calculateable by the devices both having the key
    - select a message digest algorithm = SHA512 > 'COMPUTE HMAC' button



### Data Privacy

- Encryption overview
  - locking & unlocking data
  - symmetrical encryption:
    - using the same key to encrypt and decrypt the data
    - algorithm current used: AES - 128, 192. 256
  - asymmetric encryption
    - key pair existed, mathematically related
    - encrypted w/ one key and decrypted w/ the other key
    - generally, private key and public key
    - provate key never sharing w/ other while public key sharing w/ world
    - public key sharing w/ digital certificate format
    - cons: computational intensive
  - Diffie-Hellman algorithm
    - one of the most popular symmetric algorithm
    - pre-shared key in general
    - typically dynamically generated



### SSL and TLS

- SSL/TLS overview
  - TLS: a successor of SSL
  - HTTPS using SSL/TLS
  - user w/ public key while server w/ private key
  - public key embedded in digital certificate
  - certificate from server signed by CA (Certificate Authority)
  - most likely the request w/ HTTP redirect to HTTPS and starting negotiation to validate the server and authenticate the end user


- Demo: HTTPS
  - network topology

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 400px;"
        onclick= "window.open('page')"
        src    = "img/03-netarch.png"
        alt    = "Example network topology"
        title  = "Example network topology"
      />
    </figure>
  
  - tasks: observe the behavior of HTTP and HTTPS
  - open web browser on PC1 to connect R2: `http://25.2.2.2` w/ user = admin, password = *** $\to$ browser indicating not a secure connection
  - using HTTPS instad: `https://25.2.2.2` w/ username and password $\to$ browser indicating a lock but still not secure due to the trust $\to$ digital certificate missing
  - observe the packet tracker in Wireshark
    - entry for HTTP request - src = 10.1.0.50, dst = 25.2.2.2, protocol = TCP $\to$ info readbale
    - entries for HTTPS transaction
      - src = 10.1.0.50, dst = 25.2.2.2, protocol = TLSv2, Info = Client Hello  
      - src = 25.2.2.2, dst = 10.1.0.50, protocol = TLSv2, Info = Server Hello, Certificate $\to$ payload containing certificate
      - src = 10.1.0.50, dst = 25.2.2.2, protocol = TLSv2, Info = Server Key Exchange, Server Hello Done $\to$ payload encrypted



### Public Key Infrastructure (PKI)

- Public Key Infrastructure (PKI) overview
  - TLS workflow: end user (user) and server (srv)
    - user sending request to access srv w/ HTTPS (port 443)
    - srv responding w/ digital certificate containing validate date, public key, etc.
    - how user knows the digital certificate a valid certificate? <span style="color: cyan;">signed</span>
  - signed digital certificate:
    - signed by a device that the browser of user PC $\to$ TRUST
    - Trust: user PC able to validate and signed by a Certificate Authority (CA)
  - how browser of user PC knows the CA? $\to$ preloaded on system
    - server generating public and private keys and then 
    - submit to CA to ask for its own digital certificate
    - once verified, CA issues a signed digital certificate


### IPsec

- IPsec overview
  - a suite of protocols to build VPN
  - purpose
    - privacy: encryption
    - data integrity: hashing algorithm - HMAC
  - methods
    - IKEv1: old version
    - IKEv2: more modular, more compatible
  

### Authentication

- Authentication overview
  - two main ways to authenticate peer
    - pre-shared key
    - digital certificate
  - pre-shared key:
    - both sides w/ same key
    - integrity (hashing): Hash-based Message Authentication Code (HMAC)
    - privacy (encryption/decryption): AES 128-256
  - RAS-signature (digital certificate)
    - both having its own certificate (possible same)




## 23. Network Infrastructure Device Hardening



### Device Hardening Overview

- Device hardening overview
  - the process to eliminate a means of attack by 
    - patching vulnerabilities
    - turning off non-essential services and 
    - configuring system with security controls
      - password management
      - file permissions and 
      - disabling unused network ports
  - improving security possibly broken 
    - management plane
    - control plane
    - data plane
  - management plane
    - protocols btw users and systems
    - e.g., SSH, SNMP, NetFlow, FTP. TFTP, AAA, NTP, Syslog, etc.
  - control plane
    - protocols btw devices
    - e.g., routing protocols, STP, MAC addresses
  - data plane: user traffic, end-to-end


### Cisco Guide to Harden IOS Devices

- Cisco device hardening guideline
  - [Cisco Guide to Harden Cisco IOS Devices](https://www.cisco.com/c/en/us/support/docs/ip/access-lists/13608-21.html)
  - Document ID: 13608
  - considerations for the document
    - not every solution perfect for every network
    - testing every plan before deploying


### Management Plane Hardening

- General Management Plane Hardening
  - password mgmt: TACACS+ + local user account
    - `algorithm-type [md5 | scrypt | sha256]`: algorithm to user for hashing the plaintext secret, type 9 password
    - `secret`: using type 5 password
  - enhanced password security
  - login password retry lockout
  - no Service Password-Recovery
  - disable Unused Services (*)
  - EXEC Timeout: timeout connection
  - keepalives for TCP Sessions
  - management Interface Use: create loopback intf w/ IP address
  - Memory Threshold Notifications
  - CPU Thresholding Notification (*)
  - Reserve Memory for Console Access
  - Memory Leak Detector
  - Buffer Overflow: Detection and Correction of Redzone Corruption
  - Enhanced Crashinfo File Collection
  - Network Time Protocol: authentication always
  - Disable Smart Install

  ```text
  ! local user account
  R1(config)# username admin1 privilege 15 password Cisco!23
  R1(config)# username admin1 privilege 15 secret Cisco!23
  R1(config)# username admin1 privilege 15 algorithm-type scrypt secret Cisco!23

  ! disable unused services
  R1# show control-plane host open-ports
  Active internet connections (servers and established)
  Prot        Local Address      Foreign Address             Service    State
   tcp                 *:23                  *:0              Telnet   LISTEN

  ! enable ssh & https
  R1(config)# line vty 0 4
  R1(config-line)# transport input ssh
  R1(config-line)# exit
  R1(config)# ip http secure-server
  R1(config)# end
  
  R1# show control-plane host open-ports
  Active internet connections (servers and established)
  Prot        Local Address      Foreign Address             Service    State
   tcp                 *:22                  *:0          SSH-Server   LISTEN
   tcp                 *:23                  *:0              Telnet   LISTEN
   tcp                *:443                  *:0        HTTPS-Server   LISTEN
   tcp                *:443                  *:0           HTTP CORE ESTABLIS
  ```


- Limit Access to the Network with Infrastructure ACLs
  - infrastructure ACL:
    - on edge routers
    - only allowing from certain admin computers to access management plane
    - specifying connections from hosts or networks that need to be allowed to network devices
    - all other traffic to the infrastructure is explicitly denied
  - ICMP Packet Filtering
  - Filter IP Fragments
  - ACL Support for Filtering IP Options
  - ACL Support to Filter on TTL Value


- Secure Interactive Management Sessions
  - Management Plane Protection
  - Control Plane Protection: very granularity to protect CPU, queue, threshold, etc.; control plane policing - less granularity to protect CPU
  - Encrypt Management Sessions
  - SSHv2 (*)
  - SSHv2 Enhancements for RSA Keys
  - Console and AUX Ports
  - Control vty and tty Lines
  - Control Transport for vty and tty Lines
  - Warning Banners


- Authentication, Authorization, and Accounting
  - TACACS+ Authentication
  - Authentication Fallback
  - Use of Type 7 Passwords: even type 9
  - TACACS+ Command Authorization
  - TACACS+ Command Accounting
  - Redundant AAA Servers


- Fortify the Simple Network Management Protocol
  - SNMP Community Strings
  - SNMP Community Strings with ACLs
  - Infrastructure ACLs
  - SNMP Views
  - SNMP Version 3: preferred
  - Management Plane Protection


- Logging Best Practices
  - Send Logs to a Central Location
  - Logging Level
  - Do Not Log to Console or Monitor Sessions
  - Use Buffered Logging (*)
  - Configure Logging Source Interface
  - Configure Logging Timestamps


- Cisco IOS Software Configuration Management
  - Configuration Replace and Configuration Rollback
  - Exclusive Configuration Change Access
  - Cisco IOS Software Resilient Configuration
  - Digitally Signed Cisco Software
  - Configuration Change Notification and Logging

  ```text
  R1# dir
  ! get the iso file name

  R1# show software authenticity file flash0:vios-adventerprisek9-m

  ! configuration rollback
  R1(config)# archive
  R1(config-archive)# path flash0:KB-Backup.cfg
  R1(config-archive)# maximum 10
  R1(config-archive)# time-period 2
  R1(config-archive)# write-memory
  R1(config-archive)# log config
  R1(config-archive-log-cfg)# end

  R1# dir 
  ! a copy of curren running config
  R1# write
  ! generate a startup config but also a copy of backup
  R1# configure replace flash0:KB-Backup.cfg-....
  ! replace current running config w/ the backup config
  ```




### Control Plane Hardening

- Primary considerations of control plane
  - routing protocols
  - authentication


- General Control Plane Hardening
  - consider to turn of the features
  - IP ICMP Redirects: suggesting better routes
  - ICMP Unreachables: hacker flooding to explore existence of subnets
  - Proxy ARP


- Limit CPU Impact of Control Plane Traffi
  - Understand Control Plane Traffic: drop pkts before impact CPU
  - Infrastructure ACLs (*)
  - Receive ACLs (*)
  - CoPP
  - Control Plane Protection
  - Hardware Rate Limiters


- Secure BGP
  - TTL-based Security Protections (*)
  - BGP Peer Authentication with MD5
  - Configure Maximum Prefixes
  - Filter BGP Prefixes with Prefix Lists (*)
  - Filter BGP Prefixes with Autonomous System Path Access Lists 


- Secure Interior Gateway Protocols
  - Routing Protocol Authentication and Verification with Message Digest 5
  - Passive-Interface Commands
  - Route Filtering
  - Routing Process Resource Consumption


- Secure First Hop Redundancy Protocols (FHRP)
  - including: HSRP, VRRP, GLBP
  - no authentication by default


### Data Plane Hardening

- General Data Plane Hardening
  - IP Options Selective Drop
  - Disable IP Source Routing
  - Disable ICMP Redirects
  - Disable or Limit IP Directed Broadcasts


- Filter Transit Traffic with Transit ACLs
  - ICMP Packet Filtering
  - Filter IP Fragments
  - ACL Support for Filtering IP Options


- Anti-Spoofing Protections (*)
  - Unicast RPF
  - IP Source Guard
  - Port Security
  - Dynamic ARP Inspection
  - Anti-Spoofing ACLs


- Limit CPU Impact of Data Plane Traffic
  - Features and Traffic Types that Impact the CPU
  - Filter on TTL Value
  - Filter on the Presence of IP Options
  - Control Plane Protection


- Traffic Identification and Traceback
  - NetFlow (*)
  - Classification ACLs


- Access Control with VLAN Maps and Port Access Control Lists
  - Access Control with VLAN Maps
  - Access Control with PACLs
  - Access Control with MAC


- Private VLAN Use
  - Isolated VLANs
  - Community VLANs
  - Promiscuous Ports
  - VRF-lite


### Device Hardening Checklist

- Management Plane
  - Passwords
    - Enable MD5 hashing (secret option) for enable and local user passwords
    - Configure the password retry lockout
    - Disable password recovery (consider risk)
  - Disable unused services
  - Configure TCP keepalives for management sessions
  - Set memory and CPU threshold notifications
  - Configure
    - Memory and CPU threshold notifications
    - Reserve memory for console access
    - Memory leak detector
    - Buffer overflow detection
    - Enhanced crashinfo collection
  - Use iACLs to restrict management access
  - Filter (consider risk)
    - ICMP packets
    - IP fragments
    - IP options
    - TTL value in packets
  - Control Plane Protection
    - Configure port filtering
    - Configure queue thresholds
  - Management access
    - Use Management Plane Protection to restrict management interfaces
    - Set exec timeout
    - Use an encrypted transport protocol (such as SSH) for CLI access
    - Control transport for vty and tty lines (access class option)
    - Warn using banners
  - AAA
    - Use AAA for authentication and fallback
    - Use AAA (TACACS+) for command authorization
    - Use AAA for accounting
    - Use redundant AAA servers
  - SNMP
    - Configure SNMPv2 communities and apply ACLs
    - Configure SNMPv3
  - Logging
    - Configure centralized logging
    - Set logging levels for all relevant components
    - Set logging source-interface
    - Configure logging timestamp granularity
  - Configuration Management
    - Replace and rollback
    - Exclusive Configuration Change Access
    - Software resilience configuration
    - Configuration change notifications


- Control Plane
  - Disable (consider risk)
    - ICMP redirects
    - ICMP unreachables
    - Proxy ARP
  - Configure NTP authentication if NTP is being used
  - Configure Control Plane Policing/Protection (port filtering, queue thresholds)
  - Secure routing protocols
    - BGP (TTL, MD5, maximum prefixes, prefix lists, system path ACLs)
    - IGP (MD5, passive interface, route filtering, resource consumption)
  - Configure hardware rate limiters
  - Secure First Hop Redundancy Protocols (GLBP, HSRP, VRRP)


- Data Plane
  - Configure IP Options Selective Drop
  - Disable (consider risk)
    - IP source routing
    - IP Directed Broadcasts
    - ICMP redirects
  - Limit IP Directed Broadcasts
  - Configure tACLs (consider risk)
    - Filter ICMP
    - Filter IP fragments
    - Filter IP options
    - Filter TTL values
  - Configure required anti-spoofing protections
    - ACLs
    - IP Source Guard
    - Dynamic ARP Inspection
    - Unicast RPF
    - Port security
  - Control Plane Protection (control-plane cef-exception)
  - Configure NetFlow and classification ACLs for traffic identification
  - Configure required access control ACLs (VLAN maps, PACLs, MAC)
  - Configure Private VLANs





