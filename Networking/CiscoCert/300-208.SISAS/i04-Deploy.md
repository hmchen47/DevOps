# Phase Deployment

+ Default Supplicant Network Access
    + When authentication enabled on a switch port facing a supplicant
        + By default all network access restricted before authentication
            + Only EAPOL traffic allowed
        + After authentication network access is granted per the authorization received from ISE
    + Default network access creates implementations issues
        + If something is miss-configured (can easily happen), users loose network access
    + Communication between Supplicant & Authenticator
        + MAB: no request needed
        + 802.1x: EAPOL only

+ Phased Deployment
    + Created by Cisco to easily implement MAB/802.1x
        + Minimizes network impact when EAP/802.1x is enabled
        + From users point of view, implementation is transparent
    + Three-phase model
        + __Monitor mode__
        + __Low impact mode__
        + __Closed mode__

+ Monitor Mode
    + Scope to test authentication functionality
    + Allow for transparent troubleshooting, without affecting users
    + EAP and MAB enabled on switch ports facing supplicants
    + Supplicants are granted full network access
        + Before authentication
        + After authentication (requires no authorization received from ISE)
        + After authentication, even if it fails
    + Enabled through `authentication open` command on switch port facing supplicant
    + Config Procedure:
        1. Config supplicant
        2. Config Authentication server
        3. NAD to enforce authentication 
            ```cfg
            authentication port-control [auto|force-authorized]
            mab
            ```
    + Even received Access Reject from ISE, NAD still allow to access network from connected devices

+ Demo: Monitoring Mode
    + SW3:
        ```cfg
        show authentication sessions
        ! Int=Gi1/0/5, Mac Addr=48f8.b32e.2532, Method=dot1x, Domain=Data,
        ! Status=Running, Session-ID=88015B0A000000C7111F68CE
        ! Msg: AUTHMGR-5-FAIL: Authorization failed or unapplied for client
        show ip access-lists int gi1/0/5    ! None
        show ip int gi1/0/5     ! Inbound access list is not set
        ```
    + PC-B: 
        + `ipconfig`: gateway=172.16.20.1
        + `ping 172.16.20.1`: Unreachable, not network access
    + SW3: 
        ```cfg
        show ip access-list
        ! Extended IP access list Auth-Default-ACL
        !   10 permit udp any range bootps 65347 any range bootpc 65348
        !   20 permit upd any any range bootps 65347
        !   30 deny ip any any
        ! These are default ACL.  When mab/802.1x enabled, the specific ACL applied on the ports
        ! --> Network access failed from supplicant
        
        show authentication sessions    ! Status=Authz Failed
        show run int gi1/0/5
        ! interface GigabitEthernet1/0/5
        !   switchport access vlan 90
        !   switchport mode access
        !   logging event spanning-tree
        !   authentication port-control auto
        !   dot1x pae authenticator
        !   spanning-tree portfast
        ! end

        conf t
        int gi1/0/5
          authentication open
        end
        show authentication sessions    ! status=Authz Failed
    + PC-B: `ping 172.16.20.1` - ok; `telnet 172.16.20.1` - ok

+ Low Impact Mode
    + Enabled once all users/supplicants have passed authentication
        + Scope to test authorization functionality
    + Keep the same configuration as in monitor mode
    + Restrict network access before authentication
        + Apply a static pre-authentication ACL on switch port facing supplicants
        + Optionally can use the default ACL named auth-default-acl
    + Authorization received from ISE
        + ACL in order to override the static pre-configured one

+ Closed Mode
    + Enabled once all users/supplicants have passes authorization
    + Disable monitor/low impact mode
        + Remove authentication open
        + Default network access behaviour
        + Prior to authentication only EAPOL traffic is allowed
    + Authorization is received from ISE
        + ACL in order to override the static pre-configured one
    + For users/supplicants to be granted network access
        + Supplicants need to pass authentication
        + Switch needs to successfully apply authorization received from ISE



