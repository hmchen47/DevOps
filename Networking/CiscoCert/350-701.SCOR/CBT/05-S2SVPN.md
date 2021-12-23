# 05. Cisco Router Site-To-Site VPNs

Trainer: Keith Barker


## Introducing Site-To-Site VPNs

- Learning goal
  - configure IPsec site-to-site tunnels by using IKEv1 and crypto maps
  - verify IPsec site-to-site tunnels


## Planning for IPsec Site-To-Site

- Site-to-site IPsec VPN
  - topology:
    - site 1: R1 + PC1
    - site 2: R2 + PC2
  - sharing info and protecting the traffic btw 2 sites
  - encrypted traffic only btw R1 & R2, PC1 & PC2 unawaring the encryption


- Requirements to build the site-to-site IPsec VPN
  - using IKEv1 to establish IPsec VPN
  - IKE Phase 1
    - authentication:
      - how peers to prove each other authorized?
      - solutions: preshared key, digital signature
    - hashing: packet integrity
    - encryption: ASE recommended
    - DH group:
      - a way to generate keying material
      - how to generate the keys for R1 & R2 encryption and decryption
    - lifetime
  - IKE Phase 2
    - the IPsec tunnel
    - encryption
    - interesting traffic: what traffic will be encrypted
    - peers: R1 & R2
    - tunnel mode: encrypted the whole packet and adding an new IP header
    - keying material: recycling from phase 1 or generating a new pair (PFS)


## Designing a Site-To-Site VPN

- Designing IKE phase 1 security association
  - encryption: AES 256
  - hash: SHA 256
  - authentication: pre-sharedd key (Cisco!23)
  - DH group: group 5
  - lifetime: 5000 (sec)


- Designing IKE phase 2 security association (IPsec tunnel)
  - ACL: traffic btw 10.1.0.0/24 and 10.2.0.0/24
  - encryption: AES 128
  - hash: SHA 384, most commonly using HMAC (Hash-based Message Authentication Code)
  - peer: R1 & R2
  - mode: tunnel
  - PFS (optional): group 15


## Configuring an IKE Phase 1 Policy

- Verify basic info and reachability
  - ensure the connectivity of public network
  - R1 interfaces na reachability check

    ```bash
    R1# sh ip int br
    Interface           IP-Address  OK? Method  Status                Protocol
    GigabitEthernet0/0  unassigned  YES TFTP    administratively down down
    GigabitEthernet0/1  15.1.1.1    YES TFTP    up                    up
    GigabitEthernet0/2  unassigned  YES TFTP    administratively down down
    GigabitEthernet0/3  10.1.0.1    YES TFTP    up                    up

    R1# ping 25.2.2.2
    Sending 5, 100-byte ICMP Echos to 25.2.2.2, timeout is 2 seconds:
    !!!!!
    Success rate is 100 percent (5/5), round-trip min/avg/max = 4/6/11 ms
    ```

  - R1 & R2 reachability: `` $\to$ `!!!!!`
  - PC1 basic info and reachability check:

    ```bash
    PC1# ip addr
    ...
    82: eth0@if81: ...
      ...
      inet 10.1.0.51/24 scope global eth0
      ...
    
    PC1# route
    Kernel IP routing table
    Destination   Gateway   Genmask         Flags Metric  Ref   Use Iface
    default       10.10.1   0.0.0.0         UG    0       0       0 eth0
    10.1.0.0      *         255.255.255.0   U     0       0       0 eth0
    172.17.0.0    *         255.255.0.0     U     0       0       0 eth1

    pc1# traceroute 10.2.0.50
    traceroute to 10.2.0.50 (10.2.0.50), 30 hops max, 60 byte packets
     1  10.1.0.1  (10.1.0.1)    7.607 ms    12.278 ms 18.515 ms
     2  15.1.1.5  (15.1.1.5)    14.158 ms   21.355 ms 22.545 ms
     3  25.2.2.2  (25.2.2.2)    24.787 ms   26.037 ms 27.078 ms
     4  10.2.0.50 (10.2.0.50)   16.516 ms   18.765 ms 19.234 ms
    ```

    - PC1 interface

- Implementing IKE Phase 1 on R1
  - isakmp policy number: lower number taking priority

  ```bash
  R1# sh run | section crypto

  R1# sh crypto isakmp policy
  Global IKE policy
  Default protection suite
          encryption algorithm:   DES - Data Encryption Standard (56 bit keys).
          hash algorithm:         Secure Hash Standard
          authentication method:  Rivest-Shamir-Adleman Signature
          Diffie-Hellman group:   #1 (768 bit)
          lifetime:               86400 seconds, no volume limit

  ! config IKEv1 phase 1
  R1# conf t
  R1(config)# crypto isakmp policy 5
  R1(config-isakmp)# authentication pre-share
  R1(config-isakmp)# hash sha512
  R1(config-isakmp)# do sh crypto isakmp policy
  Global IKE policy
  Protection suite of priority 5
          encryption algorithm:   DES - Data Encryption Standard (56 bit keys).
          hash algorithm:         Secure Hash Standard 2 (256 bit)
          authentication method:  Pre-Shared Key
          Diffie-Hellman group:   #1 (768 bit)
          lifetime:               86400 seconds, no volume limit
  Default protection suite
          encryption algorithm:   DES - Data Encryption Standard (56 bit keys).
          hash algorithm:         Secure Hash Standard
          authentication method:  Rivest-Shamir-Adleman Signature
          Diffie-Hellman group:   #1 (768 bit)
          lifetime:               86400 seconds, no volume limit

  R1(config-isakmp)# encryption aes 256
  R1(config-isakmp)# group 5
  R1(config-isakmp)# lifetime 
  R1(config-isakmp)# sh crypto isakmp policy
  Global IKE policy
  Protection suite of priority 5
          encryption algorithm:   AES - Advanced Encryption Standard (256 bit keys).
          hash algorithm:         Secure Hash Standard 2 (256 bit)
          authentication method:  Pre-Shared Key
          Diffie-Hellman group:   #5 (1536 bit)
          lifetime:               5000 seconds, no volume limit

  ! config pre-shared key
  R1(config-isakmp)# exit
  R1(config)# crypto isakmp key Cisco!23 address 25.2.2.2 ! specified iface
  R1(config)# crypto isakmp key Cisco!23 address 0.0.0.0  ! all ifaces
  
  R1# sh crypto isakmp key
  Keyring      Hostname/Address                            Preshared Key
  default      0.0.0.0        [0.0.0.0        ]            Cisco!23
  ```

  - apply same config on R2



## Configuring an IKE Phase 2 (IPsec) Policy

- IMplement IKEv1 Phase 2 on R1
  - create transfor set for IKEv1 phase 2
  - crypto map sequence number: used ti identify if multiple crypto maps used for different sites
  - crypto map not enabled on any interface

  ```bash
  ! config transform set
  R1# conf t
  R1(config)# crypto ipsec transform-set Demo-SET esp-aes 128 esp-sha384-hmac
  R1(cfg-crypto-trans)# mode tunnel
  R1(cfg-crypto-trans)# exit

  ! config crypto ACL
  R1(config)# ip access-list extended Crypto-ACL
  R1(config-ext-nacl)# permit ip 10.1.0.0 0.0.255.255 10.2.0.0 0.0.255.255
  R1(config-ext-nacl)# exit

  ! config crypto map
  R1(config)# crypto map Demo-MAP 10 ipsec-isakmp
  R1(config-crypto-map)# match address Crypto-ACL
  R1(config-crypto-map)# set peer 25.2.2.2
  R1(config-crypto-map)# set transform-set Demo-SET
  R1(config-crypto-map)# set pfs group15
  R1(config-crypto-map)# exit
  R1(config)# do sh crypto map
  Crypto Map "Demo-MAP" 10 ipsec-isakmp
          Peer = 25.2.2.2
          Extended IP access list Crypto-ACL
              access-list Crypto-ACL permit ip 10.1.0.0 0.0.255.255 10.2.0.0 0.0.255.255
          Security association lifetime: 4608000 kilobytes/3600 seconds
          PFS (Y/N): Y
          DH group:  group15
          Transform sets={ 
                  Demo-SET:    { esp-aes esp-sha384-hmac  }, 
          }
          Interfaces using crypto map Demo-MAP:
  ```



## Enabling the IPsec Policy




## Protocol Analysis IPsec





