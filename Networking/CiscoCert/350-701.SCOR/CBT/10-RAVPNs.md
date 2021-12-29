# 10. Cisco Remote Access VPNs

Trainer:: Keith Barker


## Introduction to RA VPNs

- Learning goals
  - options for remote access
  - configurations of Cisco Remote Access VPNs
  - verifications of Cisco Remote Access VPNs
  - the use of AnyConnect


## RA VPN Overview

- RV VPN concept
  - PC: end user
  - R1: router for corporate HQ network
  - security options
    - IPsec
    - SSL/TLS
  - push:
    - pushing policy from R1 to PC
    - authentication
    - routing
    - firewall
    - restrictions
  - split tunneling: corporate traffic route to R1 while other traffic via Internet
  - Cisco AnyConnect client software


## FlexVPN IPsec RA VPNs

- Components of FlexVPN IPsec RA VPNs
  - IKEv2 sa
    - encryption
    - authentication
    - PRF
    - encryption
  - IPsec sa
    - transform set
    - profile
  - AAA method
    - authentication: local authentication w/ certificate on R1 or Radius server in 10.1.0.0/24
    - authorization policy
  - addresses range of users
  - virtual template: used to provide configuration for dynamically created virtual-access interfces


## FlexVPN RA Design

- Design of FlexVPN RA
  - local certificate authority (CA) on R1
  - AAA method on R1
  - IP address range: 10.67.83.51-100
  - DNS server: 10.5.5.5
  - virtual template:
    - create logical interface for client
    - defined as part of FlexVPN config on R1
    - example: loopback intf 100 w/ 11.11.11.11/32
    - tunnel mode: IPsec
    - IPsec tunnel protection


## Setting CA Services in IOS

- Config CA on R1

  ```bash
  ! config domain name
  R1# conf t
  R1(config)# ip domain name ogit.online

  ! create RAS key
  R1(config)# crypto key generate rsa general-keys modulus 2048
  The name for th ekeys will be: R1.ogit.online
  % The key modulus size is 2048 bits
  % Generating 2048 bit RSA keys, keys will be non-exportable...
  %SSH-5-ENABLE: SSH 1.99 has been enabled

  ! issue certificate
  R1(config)# ip http server
  R1(config)# crypto pki server CA
  R1(ca-server)# issue-number CN=ca.ogit.online O=Training C=BT
  R1(ca-server)# grant auto
  %PKI-6-CS_GRANT_AUTO: All enrollment requests will ne automatically granted.
  R1(ca-server)# no shutdown
  Password: *****
  Re-enter password: *****
  % Generating 1024 bit RSA keys, keys will be non-exportale
  % Certificate Server enabled.
  %PKI-6-CA_ENABLED: Certificate server now available

  ! config to trust point w/ the CA
  R1(ca-server)# exit
  R1(config)# crypto pki trustpoint LOCAL-CA
  R1(ca-trustpoint)# enrollment utl http://1.1.1.1:80
  R1(ca-trustpoint)# do show ip int brief
  Interface             IP-Address    OK? Method  Status                Protocol
  GigabitEthernet0/0    unassigned    YES TFTP    administratively down down
  GigabitEthernet0/1    15.1.1.1      YES TFTP    up                    up
  GigabitEthernet0/2    unassigned    YES TFTP    administratively down down
  GigabitEthernet0/3    10.1.0.1      YES TFTP    up                    up
  Loopback0             1.1.1.1       YES manual  up                    up

  R1(ca-trustpoint)# revocation-check none
  R1(ca-trustpoint)# exit

  ! config to create certificate w/ the CA
  R1(config)# crypto pki authenticate LOCAL-CA
  Certificate has the following attributes:
       Fingerprint MD5: 0F6F3B03 9334DFD1 C6E41CA3 B8F0398C
      Fingerprint SHA1: C0888440 9B2124CB A2288462 8D76D071 8FCAA416
  
  % Do you accept this certificate? [yes/no]: yes
  Trustpoint CA certificate accepted.

  ! verify
  R1(config)# do show crypto pki cert
  CA Certificate
    Status: Available
    Certificate Serial Number (hex): 01
    Certificate Usage: Signature
    Issuer:
      cn=ca.ogit.online O=Training C=CBT
    Subject: 
      cn=ca.ogit.online O=Training C=CBT
    Validity Date:
      start date: 21:56:28 UTC Sep 27 2020
      end   date: 21:56:28 UTC Sep 27 2023

  ! enroll self to use the certificate
  R1(config)# crypto pki enroll LOCAL-CA
  %
  % Start certificate enrollment ...
  % Create a challenge password. You will need to verbally provide this
    password to tge CA administrator in order to revoke your certificate.
    For security reason your password will not be saved in the configuration.
    Please make a not of it.
  
  Password: *****
  Re-enter password: *****

  % The subject name in the certificate will include: R1.ogit.online
  % Include the router serial number in the subject name? [yes/no]: yes
  % The serial number in the certificate will be: 9YM0EOOC1QT8ODJJ6XJYL
  % Include an IP address in the subject name? [no]: yes
  Enter the Interface name or IP Address[]: 15.1.1.1
  Request certificate from CA: [yes/no] yes
  % Certificate request sent to Certificate Authority
  % The 'show crypto pki certificate verbose LOCAL-CA' command will show the fingerprints.

  R1# shoe crypto pki cert
  Certificate
    Status: Available
    Certificate Serial Number (hex): 02
    Certificate Usage: General Purpose
    Issuer:
      cn=ca.ogit.online O=Training C=CBT
    Subject:
      Name: R1.ogit.online
      IP Address: 15.1.1.1
      Serial Number: 9YM0EOOC1QT8ODJJ6XJYL
      ipaddress=15.1.1.1+hostname=R1.ogit.online+serialNumber=9YM0EOOC1QT8ODJJ6XJYL
    Validity Date:
      start date: 22:05:10 UTC Sep 27 2020
      end   date: 22:05:10 UTC Sep 27 2023
    Associated Trustpoints: LOCAL-CA
    
    CA Certificate
    Status: Available
    Certificate Serial Number (hex): 01
    Certificate Usage: Signature
    Issuer:
      cn=ca.ogit.online O=Training C=CBT
    Subject: 
      cn=ca.ogit.online O=Training C=CBT
    Validity Date:
      start date: 21:56:28 UTC Sep 27 2020
      end   date: 21:56:28 UTC Sep 27 2023
    Associated Trustpoints: LOCAL-CA
  ```

## Configuring FlexVPN RA




## AnyConnect Profile Editor




## Testing and Verifying the RA VPN




## Flex VPN RA Summary



