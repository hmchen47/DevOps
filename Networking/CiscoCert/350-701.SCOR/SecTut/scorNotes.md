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





