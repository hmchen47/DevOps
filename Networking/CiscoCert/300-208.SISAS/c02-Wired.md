# Implementing 802.1x Authentication - Wired

+ 802.1X Wired
    + Extensible Authentication Protocol (EAP) Framework
    + VLAN, ACL, Time-based, TrustSec
    + EAP-TLS, EAP-MSCHAPv2, EAP-FAST, LEAP, PEAP
    + Modes: Authenticator Port
        + Single-host - single MAC address only
        + Multi-host - Multiple host, authenticate with 1st MAC address
        + Multi-domain (MAD) - Voice + Data, one MAC address per domain
        + Multi-auth - AuthN for each MAC address

+ EAP Framework
    <a href="https://help.ubnt.com/hc/en-us/articles/115007253447-Intro-to-Networking-AAA-802-1X-EAP-RADIUS">
        <br/><img src="https://help.ubnt.com/hc/article_attachments/115025199848/Untitled_2.png" alt="802.1X Authentication End-to-End" width="450">
    </a>

    + Tunneled EAP
        <a href="http://apprize.info/network/ccnp_3/4.html">
            <br/><img src="http://apprize.info/network/ccnp_3/ccnp_3.files/image045.jpg" alt="Tunneled EAP" width="450">
        </a>

    +  VLAN: authentication -> allowed protocol
    + TrustSec: 
        + SGACLs
        + SGT/SXP

+ EAP Protocols
    + EAP-TLS: certificate
    + EAP-FAST: 
        + FAST=Flexible Authentication via Security Tunneling
        + EAP Chaining - EAP-FASTv2

+ Deployment Modes
    + Monitor mode - Open
    + Low Impact mode - ACL + Open
    + Close mode - ACL in production

+ MAB = Mac Address Authentication Bypass

+ Demo: SW1 AuthN & AuthZ config
    ```cfg
    ! Test basic connectivity to ISE 
    ping 192.168.1.117                              ! ok
    test aaa group ISE-group bob Nugget!23 new-code ! User successfully authenticated

    config terminal
    ! Use ISE server for dot1x authentication
    aaa authentication dot1x default group radius

    ! send accounting record to ISE
    aaa accounting dot1x default start-stop group radius

    ! including endpoint IP in authentication request
    radius-server attribute 8 radius-in-request-req

    ! enable dot1x
    dot1x system-auth-control

    default int gi0/7   ! Reset all settings on interface gi0/7, Prevent using in Production env.

    int gi0/7
      shutdown

      ! Access port and portfast
      switchport host

      do show run int gi0/7
      ! interface GigabitEthernet0/7
      !   switchport mode access
      !   shutdown
      !   spanning-tree portfast
      ! end

      ! mode: single-host, multi-auth, multi-host, multi-domain
      authentication host-mode multi-auth

      ! Open mode for testing - Easy
      authentication open

      ! Recurring authentication
      authentication periodic

      ! let server decide how often to re-authentication
      authentication timer reauthentication server

      ! Set port access entry to act as authenticator
      dot1x pae authenticator

      ! Supplicant retry timeout in sec
      dot1x timeout tx-period 10

      ! enable 802.1x control the port
      authentication port-control auto

      do debug radius authentication
      no shutdown

      do show int status
      ! gi0/7: status=not connected
    end

    show dot1x all
    ! Gi0/7: PAE=authenticator, OuterPeriod=60, SenderTimeout=0
    ! SuppTimeout=30, ReAuthMax=2, MAxReq=2, TxPeriod=10, PAE = Port Access Entity
    ```

+ Demo: 
    + PC access network
        + `services.msc` > WiredAutoConfig: status=started, Startup Type=Automatic
        + NIC: enable
    + SW1 Msgs:
        ```cfg
        ! DOT1X-5-FAIL: Authentication failed for client
        ! AUTHMGR-5-FAIL: Authorization failed or unapplied for client
        ```

+ PC TRBL
    + Wireshark > filter=eap > All requests
    + NIC > Properties > Authentication: check 'Enable IEEE 802.1x authentication', authentication method (outer method)=(MSCHAPv2, Settings=(uncheck 'Validate server certificate', authentication method (inner method)=(EAP-MSCHAPv2,Configure=(uncheck 'Disable automatically use my windows logon name and password -> for lab env. > ok) > ok), Additional Settings=(Authentication mode=User Authentication), Save Credential=(user=bib, pwd=Nugget!23) > ok) > ok
    + Wireshark > filter=eap:
        + Req EAP-TLS, Rsp=NAK
        + Req PEAP, Rsp=Client Hello (TLSv1)
        + TLSv1 Server Hello, Certificate (public key) Server Hello Done
        + TLSv1 (client): Client key exchange, ...
        + TLSv1 (server): Change cipher spec; Encrypted handshake messages
        + EAP: Response PEAP

+ Demo: SW1 Verification
    ```cfg
    ! RADIUS: User-Name=bob
    ! RADIUS: Framed-IP-Address=192.168.1.121

    show authentication session int gi0/7
    ! status=Authz Success, Session ID=0102030400000041011A0DD3 
    ! Oper host mode=multi-auth, IP=192.168.1.121, Domain=Data
    ! dot1x=Authz Success, User-Name=bob
    ```


