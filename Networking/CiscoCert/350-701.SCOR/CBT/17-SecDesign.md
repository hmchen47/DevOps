# 17. The Components of Network Security Design

Trainer: Keith Barker


## Intro to components of Network Security Design

- Learning goals
  - concept of network security design
  - components of network security design
  - network access control
  - end point security
  - firewalls and IPS
  - TrustSec and MACsec


## Network Access Control

- Network access control fundamentals
  - one of the most popular solution via 802.1x protocol
  - components
    - supplicant: client 
    - authenticator: switch or WLC
    - authentication server: AAA server
  - supplicant software in client trying to access network w/ username and password
  - switch / WLC authenticating locally $\to$ not scalable
  - solution: centralized management - AAA server, i.e., RADIUS server
  - Cisco solution: Identity Service Engine (ISE)
    - tabs - MONITOR, WLANs, CONTROLLER, WIRELESS, SECURITY, MANAGEMENT, COMMANDS
    - SECURITY tab > folders - AAA, Local EAp, Advanced EAp, Priority Order, Certificate, Access Control Lists, Wireless Protection Policies, Web Auth, TrustSec SXP, Local Policies, Advanced
  - 802.1x applied for wired and wireless connections

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('page')"
      src    = "img/17-nettopo.png"
      alt    = "Components of network security design"
      title  = "Components of network security design"
    />
  </figure>


- Demo: wired access control w/ ISE
  - SECURITY tab > AAA > RADIUS > Authentication > RADIUS Authentication Servers: fields - Network User, Management, Tunnel Proxy, Server Index, Server Address (Ipv4/Ipv6), Port, IPsec, Admin Status
    - entry: Server Addresses = 172.16.30.225
    - entry: Server Addresses = 172.16.30.225
  - WLANs tab > folder - WLANs, Advanced > WLANs: fields - WLAN ID, Type, Profile Name, WLAN, WLAN SSID, Admin Status, Security Policies > entry - WLAN ID = 1, Type = WLAN, Profile Name = AG-MAF-AP, Security Policies = [WAP2][Auth(802.1x)] > '1' link
  - WLANs > Edit 'AG-MAF-AP' > tabs: General, Security, QoS, Policy-Mapping, Advanced
    - General: Profile Name = AG-MAF-AP, Security Policies = [WAp2][Auth(802.1x)]
    - Security: tabs - Layer 2, Layer 3, AAA Server
      - Layer 2 Security = WPA + WPA2, MAC Filtering = Off, Fast Transition = Off; PMF (Protected Management Frame) = Disable; WPA + WPA2 pParemeters - WPA2 Policies = On, WPA2 Encryption = AES, TKIP; Authentication Key Management - 802.1x = Enable
      - AAA Servers: Authentication Servers = Enabled, 'IP:172.16.30.225, Port:1812', 'IP:172.16.30.226, Port:1812'; Accounting Servers = Enable, 'IP:172.16.30.225, Port:1813', 'IP:172.16.30.226, Port:1813'
  - POLICY tab > folders - Authentication, Authorization, Profiling, Posture, Client Provisioning > Authentication > Allowed Protocols
  - Allowed Protocols Services List > Deafult Network Access: Name = Default Network Access, Allowed Protocols - Process Host Lookup = On; Allow PAP/ASCII = On; Allow EAP-MD5 = On; Allow EAP-TLS = on; Allow PEAP = On -> PEAP Inner Method: Allow EAP-MS-CHAP2v2 = On, Allow EAP-TC = On, Allow EAP-TLS = On; Allow EAP-FAST = On -> EAP-FAST Inner Methods: Allow EAP-MS-CHAPv2 = On, ...


- MAC Authentication Bypass (MAB)
  - devices unable to interact w/ authenticator, e.g., printer
  - hard coded the MAC address of the system to access the network


- Web Authentication (Web Auth)
  - redirecting non-registered user to a web page
  - web page providing the opportunity to provide username and password dor login



## End Point Security





## Next Generation Firewalls and IPS





## TrustSec and MACsec




