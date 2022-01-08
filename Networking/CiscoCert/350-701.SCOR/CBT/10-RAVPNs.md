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
  - [virtual interface template service](https://bit.ly/3sKSFt3)
    - a feature providing a generic service used to apply predefined interface configurations in creating and freeing virual access interface dynamically, as needed
    - used to provide configuration for dynamically created virtual-access interfaces
    - a logical entity - a configuration for a serial interface but not tied to a physical interface - applied dynamically as needed
    - one possible source of configuration information for virtual access interface
    - benefits
      - easy maintenance
      - scalability
      - consistency and configuration ease
      - efficient device operation
  - virtual access interface
    - virtual interfaces created, configured dynamically, used, and then free when no longer needed
    - able to clone from only one template


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

- Implementing FlexVPN RA on R1
  - too complex to memorize
  - focus on concept
  
  ```bash
  R1# conf t
  R1(config)# aaa new-model

  R1(config)# aaa authentication login a-eap-auth-local local
  R1(config)# aaa authorization network a-eap-author-grp local

  R1(config)# username admin privilege 15 secret Cisco!23

  R1(config)# ip local pool ACPOOL 10.67.83.51 10.57.83.100

  R1(config)# ip access-list standard split_tunnel
  R1(config-std-nacl)# permit 10.0.0.0 0.255.255.255

  R1(configstd-nacl)# crypto ikev2 authorization policy ikev2-auth-policy
  R1(config-ikev2-author-policy)# pool ACPOOL
  R1(config-ikev2-author-policy)# route set access-list split_tunnel
  R1(config-ikev2-author-policy)# dns 10.5.5.5
  R1(config-ikev2-author-policy)# exit

  R1(config)# crypto ikev2 proposal IKEv2-prop1
  R1(config-ikev2-proposal)# encryption aes-cbc-256
  R1(config-ikev2-proposal)# integrity sha256
  R1(config-ikev2-proposal)# group 14

  R1(config-ikev2-proposal)# crypto ikev2 policy IKEv2-pol
  R1(config-ikev2-policy)# proposal IKEv2-propl
  R1(config-ikev2-policy)# exit

  R1(config)# crypto ikev2 profile AnyConnect-EAP
  R1(config-ikev2-profile)# match identity remote key-id *$AnyConnectClient$*
  R1(config-ikev2-profile)# authentication local rsa-sig
  R1(config-ikev2-profile)# authentication remote anyconnect-eap aggregate
  R1(config-ikev2-profile)# pki trustpoint LOCAL-CA
  R1(config-ikev2-profile)# aaa authentication anyconnect-eap a-eap-authen-local
  R1(config-ikev2-profile)# aaa authorization group anyconnect-eap list a-eap-author-grp ikev2-auth-policy
  R1(config-ikev2-profile)# aaa authorization user anyconnect-eap cached
  R1(config-ikev2-profile)# virtual-template 100

  R1(config-ikev2-profile)# crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac
  R1(cfg-crypto-trans)# mode tunnel

  R1(cfg-crypto-trans)# crypto ipsec profile AnyConnect-EAP
  R1(ipsec-profile)# set transform-set TS
  R1(ipsec-profile)# set ikev2-profile AnyConnect-EAP

  R1(ipsec-profile)# interface loopback100
  R1(config-if)# ip address 11.11.11.11 255.255.255.255

  R1(config-if)# interface Virtual-Template100 type tunnel
  R1(config-if)# ip unnumbered Loopback100
  R1(config-if)# ip mtu 1400
  R1(config-if)# tunnel mode ipsec ipv4
  R1(config-if)# tunnel protection ipsec profile AnyConnect-EAP

  R1(config-if)# end
  ```



## AnyConnect Profile Editor

- AnyConnect VPN profile editor
  - downloaded from Cisco website
  - AnyConnect Profile Editor - VPN > folders - Preferences (Part 1), Preferences (Part 2), Backup Servers, Certificate Pinning, Certificate Matching, Certificate Enrollment, Mobile Policy, Server List
  - Preferences (Part 1) - Profile: Untitled > User Controllable = On, Minimize On Connect = On, Auto Reconnect = On, Auto Update = On
  - Server List - Profile: Untitled > fields - Hostname, Host Address, User Group, Backup Server List, SCEP, Mobile Settings, Certificate Pins > 'Add' button
    - Server List Entry > tabs - Server, Load Balancing Servers, SCEP, Mobile, Certificate Pinning
    - Servers > primary Server: Display Name (required) = 'Primary VPN Server', FQDN or IP Address = 15.1.1.1
    - Servers > Connection Information: Primary Protocols = IPsec, SAS gateway = Off, Auth Methgod During IKE Negotiation = EAP-AnyConnect
    - 'ok' button > entry - Hostname = Primary VPN Server, Host Address = 15.1.1.1, Backup Server List = -- Inherited --
  - File > 'Save As...' > '10.xml'
  - file location: `C:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\Profile\`
  - Preferences (Part 1): Windows VPN Establishment = AllowRemoteUsers $\gets$ remote users than local users, in particular RTP users


- Special setting for BypassDownloader
  - not supporting SSL $\implies$ BypassDownloader not working
  - change to  `<BypassDownloader>flase</BypassDownloader>` in `C:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\AnyConnectLocalPolicy.xml`
  - alternatively, `VPN Local Policy Editor` software
    - check 'Bypass Downloader' box


## Testing and Verifying the RA VPN

- Testing and Verify FlexVPN RA on PC
  - srv: 10.1.0.0, user: 10.1.0.50
  - exec Cisco AnyConnect Secure Mobility Client
  - select appropriate profile, 7 > 'Connect' button
  - Cisco AnyConnect | 7 > Username = admin, Password = ***** > 'Gear' icon
  - AnyConnect Secure Mobility Client > tabs - Preferences, Statistics, Route Details, Firewall, Message History
  - Statistics tab > Address Information: Client (Ipv4) = 10.67.83.52 (virtual server IP address), Server = 15.1.1.1
  - Route Details tab > Secure Routes (Ipv4): 10.0.0.0/8, 10.5.5.5/32; Non-Secured Routes (IPv4): 0.0.0.0/0
  - PC CLI: `route print` $\to$ Network Destination = 10.0.0.0, Netmask = 255.0.0.0, Gateway = On-link, Interface = 10.67.83.52, Metric = 257
  - PC CLI: `ping 10.1.0.50` $\to$ AnyConnect Secure Mobility Clint > observe the change - Statistics tab > Frames: Sent = 106, Receive = 10 (issue ping again)
  - PC CLI: `ping 10.2.0.50` $\to$ AnyConnect Secure Mobility Clint > observe the change - Statistics tab > w/o change


- Verify on R1

  ```bash
  R1# show ip in brief
  Interface           IP-Address  OK? Method  Status                Protocol
  GigabitEthernet0/0  unassigned  YES TFTP    administratively down down
  GigabitEthernet0/1  15.1.1.1    YES TFTP    up                    up
  GigabitEthernet0/2  unassigned  YES TFTP    administratively down down
  GigabitEthernet0/3  10.1.0.1    YES TFTP    up                    up
  Loopback0           1.1.1.1     YES manual  up                    up
  Loopback100         11.11.11.11 YES manual  up                    up
  Virtual-Access      11.11.11.11 YES manual  up                    up
  Virtual-Template100 11.11.11.11 YES manual  up                    down

  R1# show ip route
  Gateway of last resort is 15.1.1.5 to network 0.0.0.0

    O*    0.0.0.0/0 [1/0] via 15.1.1.5
          1.0.0.0/32 is subnetted, 1 subnets
    O        1.1.1.1 is directely connected, Loopback0
          10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
    C        10.1.0.0/24 is directly connected, GigabitEthernet0/3
    L        10.1.0.0/32 is directly connected, GigabitEthernet0/3
    O        10.2.0.0 [110/3] via 15.1.1.5, 01:58:13, GigabitEthernet0/1
    O        10.3.0.0 [110/2] via 15.1.1.5, 01:58:13, GigabitEthernet0/1
    S        10.67.83.52/32 is directly connected, Virtual-Access1
          11.0.0.0/32 is subnetted, 1 subnets
    C       11.11.11.11 is directely connected, Loopback100
          15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        15.1.1.0 is directly connected, GigabitEthernet 0/1
    L        15.1.1.1 is directly connected, GigabitEthernet 0/1
          25.0.0.0/24 is subnetted, 1 subnets
    O        25.2.2.0 [110/2] via 15.1.1.5 00:58:13, GigabitEthernet 0/1
    O     192.168.1.0/24 [110/2] via 15.1.1.5 00:58:13, GigabitEthernet 0/1

  R1# show crypto ikev2 sa
  Tunnel-id Local         Remote          fvrf/ivrf   Status
  1         15.1.1.1/4500 10.5.5.51/54643 none/none   READ
    Encr: AES-CBC, Keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:14, Auth sign: PSK, Auth verify: PSK
    Life/Active Time: 86400/563 sec

  R1# show crypto ikev2 sa detailTunnel-id Local         Remote          fvrf/ivrf   Status
  1         15.1.1.1/4500 10.5.5.51/54643 none/none   READ
    Encr: AES-CBC, Keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:14, Auth sign: PSK, Auth verify: PSK
    Life/Active Time: 86400/563 sec
    CE id: 1002, Session-id: 2
    Status Description: Negotiation done
    Local spi: 11FEB1839ECFF9F4       Remote spi: 902888ED4634E9EB
    Local id: 15.1.1.1
    Remote id: *$AnyConnectClient$*
    Remote EAP id: admin
    Local req msg id:   0             Remote req msg id:   26
    Local next msg id:  0             Remote next msg id:  26
    Local queue msg id: 0             Remote req queue id: 26
    Local window:       5             Remote window:       1
    DPD configured for 0 seconds, entry 0
    Fragmentation not configured.
    Dynamic Route Update: disabled
    Extended Authentication not configured.
    NAT-T is detected outside
    Cisco Trust Security SGT is disabled
    Assigned host addr: 10.67.83.52
    Initiator of SA : No

  R1# show crypto ipsec sa
  interface: Tunnel0
      Crypto map tag: Virtual-Access1-head-0, local addr 15.1.1.1

    protected vrf: (none)
    local Ident  (addr/mask/port/prot): (00.0.0.0/0.0.0.0/0/0)
    remote Ident (addr/mask/port/prot): (10.76.83.52/255.255.255.255/0/0)
    current-peer 10.5.5.51 port 54643
      PERMIT, flags={origin_is_acl}
    #pkts encaps: 12, #pkts encrypt: 12, #pkts digest: 12
    #pkts decaps: 120, #pkts decrypt: 120, #pkts verify: 120
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts errors 0, #recv errors 0

     local crypto endpt.: 15.1.1.1, remote crypto endpt.: 10.5.5.51
     plaintext mtu 1422, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
     current outbound spi: 0xD6F40E5C(3606318684)
     FPS (Y/N): N, DH group: none

     inbound esp sas:
      epi: 0x89ECD594(2213999764)
  ```    


## Flex VPN RA Summary

- Summary
  - headend VPN server
  - AnyConnect VPN Client



