# 03. Components of Cryptography

Trainer: Keith Barker


## Introduction to Components of Cryptography

- Learning goals
  - suite of cryptography tools
  - purpose of tools
  - applying tools to protect data integrity, confidentiality


## Data Integrity

- Hash
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
    - secrete key: the element making the hash only calculateable by the devices both having the key
    - select a message digest algorithm = SHA512 > 'COMPUTE HMAC' button



## Data Privacy

- Encryption
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



## SSL and TLS



## Public Key Infrastructure (PKI)



## IPsec



## Authentication



## Components of Cryptography Summary