# MAB and Troubleshooting

+ 802.1X MAC Authentication Bypass (MAB): Authentication for non 802.1X devices
    + Authentication based on MAC address
    + No periodic re-authentication
    + MAB best practice: Source Guard, DAI, DHCP Snooping
    + RADIUS Service type 6 enabled on NAD
    + Priority of authentication methods on NAD

+ Authentication Based on MAC Address
    <a href="https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Security/TrustSec_1-99/MAB/MAB_Dep_Guide.html#wp392152">
        <br/><img src="https://www.cisco.com/c/dam/en/us/td/i/200001-300000/210001-220000/214001-215000/214360.eps/_jcr_content/renditions/214360.jpg" alt="High-Level MAB Sequence" width="350"> &nbsp;
    </a>
    <a href="https://colinzhong.blogspot.com/2015/04/cisco-trustsec-ise-part-5-mab-mac.html">
        <img src="https://lh6.googleusercontent.com/avDx3vTt_XrPs-_S9Dw-r2MqP-rxT6simTEPjGOnc0f321EeM1tlokazQ4CwefCLQ8k0f0qWC62Iu4oki5AcZNZ8xd7EZGDxisIKChqx0wyEM9tRV2HnygVIMiJSC1wwjJ9UMrs3GStvOEZd" alt="MAB Authentication Process" width="425">
    </a>
    + port security - hard coded
    + MAB: ISE identify the MAC address one of the endpoint
    + dot1x and mab: coexisted with order
    + MAB re-authenticate with link up and down

+ MAB as a Failover Mechanism for Failed Non-IEEE/IEEE Endpoints
    <a href="https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Security/TrustSec_1-99/MAB/MAB_Dep_Guide.html#wp392152">
        <br/><img src="https://www.cisco.com/c/dam/en/us/td/i/200001-300000/210001-220000/214001-215000/214362.eps/_jcr_content/renditions/214362.jpg" alt="MAB as Fallback Mechanism for Non-IEEE 802.1X Endpoints" width="350"> &nbsp;
        <img src="https://www.cisco.com/c/dam/en/us/td/i/200001-300000/210001-220000/214001-215000/214363.eps/_jcr_content/renditions/214363.jpg" alt="MAB as a Failover Mechanism for Failed IEEE Endpoints" width="410">
    </a>


+ MAB Best practices
    <a href="https://cenkercetin.com/ip-source-guard-sistemi/">
        <br/><img src="https://cenkercetin.com/wp-content/uploads/2010/09/cisco-integrated-security.png" alt="IP SOURCE GUARD SİSTEMİ" width="450">
    </a>
    + Source Guard: validate source IP address
    + DHCP Snooping: DHCP -> IP address
    + DAI: Dynamic ARP Inspection

+ Radius Service Type 6
    + Used for MAB to info w/ MAC address
    + May or May not enabled by default, check mode/version docs (cisco.com/go/fn)

+ Demo: Radius service type 6 on NAD
    ```cfg
    show run int gi0/7
    ! interface GigabitEthernet0/7
    !   switchport mode access
    !   authentication host-mode multi-auth
    !   authentication open
    !   authentication port-control auto
    !   authentication time reauthentication server
    !   dot1x pae authenticator
    !   dot1x timeout tx-period 10
    !   spanning-tree portfast
    ! end

    conf t
    radius-server attribute 6 on-for-login-auth

    int gi0/7
      switch port access vlan 10
      shut
      no shut
    end

    show authentication sessions int gi0/7
    ! User-Name=bob, status=AuthZ Success, IP=10.10.10.51, dot1x=Authc Success

+ Demo: PC Validateion
    + `ipconfig`: IP = (10.10.10.51 - wired, 192.168.1.120 - wireless)
    + `ping google.com` - ok
    + NIC > Properties > Authentication > disable 'Enable IEEE 802.1X authentication' > ok > disable > enable
    + `ping google.com` - ok

+ Demo: NAD (SW1) method list 
    ```cfg
    show authentication session int gi0/7
    ! dot1x=Running
    ! DOT1X-5-FAIL: Authentication failed for client

    show authentication sessions int gi0/7
    ! status=Authz Failed, dot1x=Failed Over

    conf t
    int gi0/7
      shut
      mab
      authentication order mab dot1x
      authentication priority dot1x mab     ! dot1 over mab
      do debug radius authentication
      no shut

    ! AUTHMGR-5-START: syarting 'mab' for client
    ! RADIUS: Service-Type=6 (Call Check), User-Name=a4badbb15013 (MAC)
    ! AUTHMGR-7-RESULT: Authentication result 'no-response' from 'mab' for client 
    !       (Not Config MAC in ISE as endpoint)
    ! AUTHMGR-5-START: Starting 'dot1x' for client
    ! AUTHMGR-7-RESULT: Authentication result 'no-response' from 'dot1x' for client
    !       (Supplicant not config as IEEE 802.1x)

    do show authentication sessions int gi0/7
    ! Status = AuthZ Failed, mab=Failed Over, dot1x=Failed Over
    ```

+ Demo: Config Endpoint with MAC
    + Verification: Operations > Authentications > last entry: Identity=A4:BA:DB:B1:50:13 > Details: User-Name=A4:BA:DB:B1:50:13 (used to create endpoint), Event=Endpoint concluded several failed authentication of the same scenario, Failure Reason=Subject not found in the applicable identity store(s) -> No user acct/MAC setup in ISE
    + Administration > Identity Management - Identities > Endpoints > Add: MAC Address=A4:BA:DB:B1:50:13 > Submit

+ Verification & TRBL
    + PC: NIC > disable > enable
    + SW1: AUTHMGR-7-FAILOVER: Failing over fro 'mab' for client -> Timeout
    + ISE Verification: Operations > Authentications > last error entry > Details: Username=A4:BA:DB:B1:50:13, IP=10.10.10.51, Authentication method=mab, Service Type=Call Check, Network Device=SW1, NAS IP=190.138.1.121, NAS Port ID=gi0/7, NAS Type Port=Ethernet
    + SW1 Validation
        ```cfg
        conf t
        int gi0/7
          shut
        end

        show run | inc radius
        ! ip radius service-interface vlan 1
        ! radius-server attribute 8 include-in-access-req
        ! radius-server dead-criteria time 30 tries 3
        ! radius-server vsa send authentication
        ! radius-server vsa send accounting
        ! radius server ISE

        conf t
        radius-server attribute 25 access-request include
        int gi0/7
          no shut
        end

        ! Still failed
        ```

+ Demo: Restart ISE
    + ISE CLI prompt: user=admin, pwd=Nugget!23
        ```cfg
        show application version ise    ! version=1.2.1.198
        show application status ise
        ! Min Disk Size=200GB, Current Disk Size=128G - ok not critical in lab env

        show ip route   ! ok
        reload
        ```
    + ISE Verification: Operations > Authentications > last successful entry: Identity=A4:BA:DB:B1:50:13 > Details: Event=Authentication Success, Identity Source=Internal Endpoints
    + SW1 Messages:
        ```cfg
        ! AUTHMGR-7-RESULT: Authentication result 'success' from 'mab' for client

        show authentication sessions int gi0/7
        ! Status=Authz Success, mab=Authx Success, dot1x=Not Run

        show run int gi0/7
        ! interface GigabitEthernet0/7
        !   switchport mode access
        !   authentication host-mode multi-auth
        !   authentication open
        !   authentication port-control auto
        !   authentication time reauthentication server
        !   dot1x pae authenticator
        !   dot1x timeout tx-period 10
        !   authentication order mab dot1x
        !   authentication priority dot1x mab ! turn on 802.1x of PC and EAPoL will kick in and take precedence
        !   spanning-tree portfast
        ! end

    + PC Verification Trigger
        + NIC > Properties > Authentication: enable 'IEEE 802.1x authentication', PEAP Setting=(Authentication method=EAP-MSCHAPv2, Configure=(disable 'Automatically use my Windows logon name and password > ok), Additional Settings=(Authentication mode=User Authentication, Saved Credentials=(user=bob, pwd=Nugget!23 > ok)))
    + SW1: 
        ```cfg
        ! AUTHMGR-7-RESULT: Authentication result 'success' from 'dot1x' for client

        show authentication sessions int gi0/7
        ! mab=not Run, dot1x=Authc Success
        ```




