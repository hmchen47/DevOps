# 06. Cisco Point-To-Point GRE over IPsec VPNs

Trainer: Keith Barker


## Introduction to P2P GRE over IPsec VPNs

- Learning goal
  - GRE tunneling protocol
  - the configuration and verification of Cisco Remote Access VPNs
  - the use of AnyConnect
  - the configuration and verification of Cisco Remote Access VPNs
  - the use of AnyConnect


## Overview of GRE over IPsec VPNs

- Issues of IPsec tunnel
  - originally designed for site-to-site IPsec VPN
  - no logical IP address w/ S2S IPsec tunnel
  - not supporting broadcast and multicast
  - unable to use routing protocols


- Generic Routing Encapsulation (GRE)
  - a protocol for encapsulating data packets to set up a direct network connection
  - creating GRE tunnel to enable
    - network address space associated to the tunnel
    - carrying other protocols other than IP only
    - broadcast and multicast w/ the address space
    - running routing protocols
  - packet format

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
        onclick= "window.open('https://ipcisco.com/lesson/gre-tunnel-overview-ccnp/')"
        src    = "https://ipcisco.com/wp-content/uploads/gre-header-1.jpg"
        alt    = "GRE Header"
        title  = "GRE Header"
      />
    </figure>

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://blog.51sec.org/2016/10/cisco-ios-router-configuration-ipsec.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=160
        src   = "https://thenetworkology.files.wordpress.com/2013/07/ipsec-over-gre.png"
        alt   = "IpSec ove GRE"
        title = "IpSec ove GRE"
      >
    </a>
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=160
        src   = "https://thenetworkology.files.wordpress.com/2013/07/gre-over-ipsec2.png"
        alt   = "GRE ove IPsec"
        title = "GRE ove IPsec"
      >
    </a>
  </div>

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://blog.51sec.org/2016/10/cisco-ios-router-configuration-ipsec.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=110
        src   = "https://www.firewall.cx/images/stories/gre-ipsec-tunnel-transport-1.gif"
        alt   = "IpSec ove GRE packet format"
        title = "IpSec ove GRE packet format"
      >
    </a>
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=110
        src   = "https://www.firewall.cx/images/stories/gre-ipsec-tunnel-transport-2.gif"
        alt   = "GRE ove IPsec packet format"
        title = "GRE ove IPsec packet format"
      >
    </a>
  </div>


## P2P GRE Tunnel Design

- Designing GRE tunnel
  - create tunnel btw R1 & R2
  - tunnel address space: 10.12.12.0/24
  - use EIGRP as routing protocol
    - autonomous system: 1
    - network: 10.0.0.0/8 



## P2P GRE Tunnel Implementation

- Implementing P2P GRE tunnel on R1

  ```bash
  ! verify interface config
  R1# sh ip int br
  Interface           IP-Address  OK? Method  Status                Protocol
  GigabitEthernet0/0  unassigned  YES TFTP    administratively down down
  GigabitEthernet0/1  15.1.1.1    YES TFTP    up                    up
  GigabitEthernet0/2  unassigned  YES TFTP    administratively down down
  GigabitEthernet0/3  10.1.0.1    YES TFTP    up                    up

  ! create tunnel intf 0 w/ Ip addr
  R1# conf t
  R1(config)# int tunnel 0
  R1(config-if)# ip addr 10.12.12.1 255.255.255.0
  R1(config-if)# tunnel source 15.1.1.1
  R1(config-if)# tunnel destination 25.2.2.2
  R1(config-if)# do show run int tun 0
  Current configuration : 115 bytes
  ! 
  interface Tunnel0
   ip address 10.12.12.1 255.255.255.0
   tunnel source 15.1.1.1
   tunnel destination 25.2.2.2
  end
  ```


- Implementing P2P GRE tunnel on R2

  ```bash
  R2# conf t
  R2(config)# int tunnel 0
  R2(config-if)# ip addr 10.12.12.2 255.255.255.0
  R2(config-if)# tunnel source 25.2.2.2
  R2(config-if)# tunnel destination 15.1.1.1
  R1(config-if)# do show run int tun 0
  Current configuration : 115 bytes
  ! 
  interface Tunnel0
   ip address 10.12.12.2 255.255.255.0
   tunnel source 25.2.2.2
   tunnel destination 15.1.1.1
  end
  ```


- Config EIGRP on R1 & R2

  ```bash
  R2# show ip route
  Gateway of last resort is not set

  s*    0.0.0.0 [1/0] via 25.2.2.5
        10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
  C        10.2.0.0/24 is directly connected, GigabitEthernet0/3
  L        10.2.0.1/32 is directly connected, GigabitEthernet0/3
  C        10.12.12.0/24 is directly connected, Tunnel0
  L        10.12.12.1/32 is directly connected, Tunnel0
        25.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
  C        25.2.2.0/24 is directly connected, GigabitEthernet0/2
  L        25.2.2.2/32 is directly connected, GigabitEthernet0/2

  ! config EIGRP
  R2# conf t
  R2(config)# router eigrp 1
  R2(config-router)# no auto-summary
  R2(config-router)# net 10.0.0.0 0.255.255.255
  R2(config-router)# end

  R2#sh ip eigrp interfaces 
  EIGRP-IPv4 Interfaces for AS(1)
                          Xmit Queue   Mean   Pacing Time   Multicast    Pending
  Interface        Peers  Un/Reliable  SRTT   Un/Reliable   Flow Timer   Routes
  Gi0/3              0        0/0         0       0/1            0           0
  Tu0                0        0/0         0       6/6            0           0
  ```

  ```bash
  ! config EIGRP
  R1# conf t
  R1(config)# router eigrp 1
  R1(config-router)# no auto-summary
  R1(config-router)# net 10.0.0.0 0.255.255.255
  R1(config-router)# end

  R1# show ip route eigrp
  Gateway of last resort is not set

        10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
  D        10.2.0.0/24 [90/26880256] via 10.12.12.2 00:00:09, Tunnel0
  ```


## P2P GRE Tunnel Verification

- Verifying P2P GRE tunnel
  - capture packets on A - PC1 (10.1.0.50), B - Cloud, and C - PC2 (10.2.0.50)
  - PC1 browsing PC2, 10.2.0.50, and reflash a couple of time to generate traffic
  - pkt on A: src=PC1, dst=PC2, prot=HTTP, info=GET / HTTP/1.1
    - L3: IPv4 $\to$ Identification: 0x7f18 (32536)
    - L4: TCP, SrcPort: 36276, Dst Port: 80
  - pkt on B: src=PC1, dst=PC2, prot=HTTP, info=GET / HTTP/1.1
    - L3: IPv4, Src: 15.1.1.1, Dst: 25.2.2.2 $\to$ Protocol: Generic Routing Encapsulation (47)
    - Generic Routing Encapsulation (IP)
    - L3: IPv4, Src: PC1, Dst=PC2 $\to$ Identification: 0x7f18 (32536)
    - L4: TCP, SrcPort: 36276, Dst Port: 80
  - pkt on C: src=PC1, dst=PC2, prot=HTTP, info=GET / HTTP/1.1
    - L3: IPv4 $\to$ Identification: 0x7f18 (32536)
    - L4: TCP, SrcPort: 36276, Dst Port: 80



## IPsec Tunnel Protection Design

- Planning of IPsec tunnel
  - IKE phase 1
    - encryption: aes 256
    - hashing: SHA 256
    - authentication: pre-shared key (PSK)
    - DH group: group 5
    - lifetime: 5000
  - IKE phase 2
    - enccryption: aes 128
    - hashing: HMAC SHA 384
  - interesting traffic
    - crypto map w/ crypto ACL fpr port 47
    - tunnel protection profile into tunnel interface (recommended)


## IPsec Virtual Tunnel Interface Configuration

- Config IKE phase 1 on R1

  ```bash
  R1# conf t
  R1(config)#crypto isakmp policy 7
  R1(config-isakmp)#encryption aes 256
  R1(config-isakmp)#hash sha256
  R1(config-isakmp)#authentication pre-share
  R1(config-isakmp)#group 5
  R1(config-isakmp)#lifetime 5000
  R1(config-isakmp)# exit

  R1(config)#do show crypto isakmp policy  
  Global IKE policy
  Protection suite of priority 7
          encryption algorithm:   AES - Advanced Encryption Standard (256 bit keys).
          hash algorithm:         Secure Hash Standard 2 (256 bit)
          authentication method:  Pre-Shared Key
          Diffie-Hellman group:   #5 (1536 bit)
          lifetime:               5000 seconds, no volume limit

  ! config pre-shared key
  R1(config)#crypto isakmp key Cisco!23 address 0.0.0.0
  R1(config)#do sh crypto isakmp key
  Keyring      Hostname/Address                            Preshared Key
  default      0.0.0.0        [0.0.0.0        ]            Cisco!23
  ```
  

- Config IKE phase 2 on R1
  
  ```bash
  R1(config)#crypto ipsec transform-set Demo-SET esp-aes 128 esp-sha384-hmac 
  R1(cfg-crypto-trans)#mode tunnel 
  R1(cfg-crypto-trans)#exit

  ! change tunnel encryption GRE to IPsec
  R1(config)# crypto ipsec profile Demo-IPsec-Profile 
  R1(ipsec-profile)# set transform-set Demo-SET
  R1(ipsec-profile)# exit
  ```


- Config IPsec within tunnel interface on R1
  - tunnel mode ipsec ipv4 = VTI

  ```bash
  R1(config)# int tunnel 0
  R1(config-if)#tunnel mode ipsec ipv4 
  R1(config-if)#tunnel protection ipsec profile Demo-IPsec-Profile
  R1(config-if)#end
  ```
  

- Config IKE phase 1, phase 2 and tunnel interface on R2

  ```bash
  R2# conf t
  ! IKE phase 1
  R2(config)# crypto isakmp policy 7
  R2(config-isakmp)# encryption aes 256
  R2(config-isakmp)# hash sha256
  R2(config-isakmp)# authentication pre-share
  R2(config-isakmp)# group 5
  R2(config-isakmp)# lifetime 5000
  R2(config-isakmp)# exit

  R1(config)#do show crypto isakmp policy  
  Global IKE policy
  Protection suite of priority 7
          encryption algorithm:   AES - Advanced Encryption Standard (256 bit keys).
          hash algorithm:         Secure Hash Standard 2 (256 bit)
          authentication method:  Pre-Shared Key
          Diffie-Hellman group:   #5 (1536 bit)
          lifetime:               5000 seconds, no volume limit

  ! config pre-shared key
  R2(config)# exit
  R2(config)#crypto isakmp key Cisco!23 address 0.0.0.0
  R2(config)#do sh crypto isakmp key
  Keyring      Hostname/Address                            Preshared Key
  default      0.0.0.0        [0.0.0.0        ]            Cisco!23

  ! IKE phase 2
  R2(config)# crypto ipsec transform-set Demo-SET esp-aes 128 esp-sha384-hmac 
  R2(cfg-crypto-trans)# mode tunnel 
  R2(cfg-crypto-trans)# exit

  ! change tunnel encryption GRE to IPsec
  R2(config)# crypto ipsec profile Demo-IPsec-Profile 
  R2(ipsec-profile)# set transform-set Demo-SET
  R2(ipsec-profile)# exit
  ```


- Verify connectivity and config
  - open browser on PC1 w/ URL = '10.2.0.50', refresh a couple time to generate traffic
  - verify crypto info on R1

    ```bash
    R1# show crypto engine connections active
    Crypto Engine Connections

       ID  Type    Algorithm      Encrypt  Decrypt LastSeqN IP-Address
        5  IPsec   AES+SHA384           0       23       23 15.1.1.1
        6  IPsec   AES+SHA384          25        0        0 15.1.1.1
     1001  IKE     SHA256+AES256        0        0        0 15.1.1.1
     1002  IKE     SHA256+AES256        0        0        0 15.1.1.1

    R1#show crypto isakmp sa
    IPv4 Crypto ISAKMP SA
    dst             src             state          conn-id status
    25.2.2.2        15.1.1.1        QM_IDLE           1002 ACTIVE
    15.1.1.1        25.2.2.2        QM_IDLE           1001 ACTIVE

    R1# show crypto ipsec sa
    interface: GigabitEthernet0/1
      Crypto map tag: Demo-MAP, local addr 15.1.1.1
    
    protected vrf: (none)
    local  ident (addr/mask/prot/port): (0.0.0.0/0.0.0.0/0/0)
    remote ident (addr/mask/prot/port): (0.0.0.0/0.0.0.0/0/0)
    current_peer 25.2.2.2 port 500
      PERMIT, flags = {origin_is_acl,}
      #pkts encaps: 39, #pkts encrypt: 39, #pkts digest: 39
      #pkts decaps: 36, #pkts decrypt: 36, #pkts verify: 36
      #pkts compressed: 0, #pkts decompressed: 0
      #pkts not compressed: 0, #pkts compr. failed: 0
      #pkts errros 0, #recv errors 0

       local crypto endpt.: 15.1.1.1, remote crypto endpt.: 25.2.2.2
       plaintext mtu 1422, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
       current outbound spi: 0xC2A77F2F(3265756975)
       FPS (Y/N): N, DH group: none

       inbound esp sas:
    ```


## IPsec Static VTI Verification





