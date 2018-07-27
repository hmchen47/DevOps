# Web Base User Authentication

+ Web Authentication: When an 802.1x Supplicant isn't available
    + Switch Configuration: CoA, Base and Redirect ACLs
    + ISE Config
        + dACL
        + Profiles
        + Policies

+ Switch Configuration for WebAuth: SW1
    ```cfg
    hostname SW1
    
    aaa group server radius ISE-group
    server name ISE

    aaa authentication login default enable
    aaa authentication login FREE none
    aaa authentication dot1x default group radius
    aaa authorization network default group radius
    aaa accounting dot1x default start-stop group radius

    ! CoA
    aaa server radius dynamic-aothor
      client 192.168.1.117 server-key Nugget!23

    ip domain name nuglab.com

    ip device tracking

    dot1x system-auth-control

    interface GigabitEthernet0/7
      switchport mode access
      ip access-group SAMPLE-ACL in
      authentication host-mode multi-auth
      authentication open
      authentication order mab dot1x
      authentication priority dot1x mab
      authentication port-control auto
      authentication periodic
      authentication timer reauthentication server
      mab
      dot1x pae authenticator
      dot1x timeout tx-period 10
      spanning-tree portfast
    exit

    interface GigabitEthernet0/8
      switchport access vlan 10
      switchport mode access
      ip access-group SAMPLE-ACL in
      authentication host-mode multi-auth
      authentication open
      authentication order mab dot1x
      authentication priority dot1x mab
      authentication port-control auto
      authentication periodic
      authentication timer reauthentication server
      mab
      dot1x pae authenticator
      dot1x timeout tx-period 10
      spanning-tree portfast
    exit

    interface valn 1
      ip address 192.168.1.121 255.255.255.0
    exit

    ip access-list extended REDIRECT
      permit tcp any any eq www
      permit tcp any any 443
    exit

    ip access-list extended SAMPLE-ACL
      deny icmp any host 8.8.8.8
      permit ip any any
    exit

    ip radius source-interface vlan1

    radius-server attribute 6 on-for-login-auth
    radius-server attribute 8 radius-access-in-request
    radius-server attribute 25 access-request include
    radius-server dead-criteria time 30 tries 3
    radius-server vsa send accounting
    radius-server vsa send authentication

    radius server ISE
      address ipv4 192.168.1.117 auth-port 1812 acct-port 1813
      key Nugget!23
    exit

+ ISE Web Portal: Administration > Web Portal Management > Settings >
    + General > Portal Theme (color, logs, etc.)
    + Guest > Multi-Portal Configurations > Default Guest Portal
    + Guest > Multi-Portal Configurations > Add: Name=Our_Captive_Portal, Operation Tab=(Guest Portal Policy Config=First login), Authentication Tab=(Identity Store Sequence=Use_AD_the_Local) > Submit

+ ISE - Customized ACL
    + Production env. DACL: Policy > Policy Elements > Results > Authorization > Downloadable ACLs > Add: Name=Waiting_for_WebAuth, DACL=(permit udp any any eq bootps, permit udp any any 53, permit icmp any any echo, permit icmp any any echo-reply, permit tcp ny any eq 80, permit tcp any any 443, permit ip any host 192.168.1.117)  > Submit
    + Lab env. DACL for testing: Policy > Policy Elements > Results > Authorization > Downloadable ACLs > Add: AD_Users_via_WebAuth, DACL=(permit ip any any) > Submit

+ Demo: Authorization Profile <br/>
    Policy > Policy Elements > Authorization > Authorization Profiles >
    + Add: Name=You_Must_WebAuth, Tasks=(Web Redirection (CWA, DRW, MDM, NSP, CPP)=(Centeralized Web Auth=REDIRECT, Redirect=Manual, Value=Our_Captive_Portal)) > Submit
    + Add: Name=AD_Users_Who_WebAuth, Tasks=(DACL Name=AD_Users_via_WebAuth) > Submit

+ Demo: Policy for WebAuth <br/>
    Policy > Authorization > default > edit (Insert New Rule Above): Name=AD User who Web Authed, Conditions=(AD1:ExternalGroups EQUALS nuglab.com/Users/Domain users, Network Access:UseCase EQUALS Guest Flow), Permissions=(AD_Users_who_WebAuth) > Done > Save

+ Demo: Verification
    + ISE: Operations > Authentications > Error Entries > Details: gi0/8 down
    + SW1:
        ```cfg
        conf t
        int gi0/8
          shut

        ! AUTHMGR-5-SUCCESS: Authorization result 'success' from 'mab' for client

        do show authentication sessions int gi0/8
        ! MAC=c8bc.c897.005c, IP=10.10.10.51, User-Name=C8-BC-C8-97-00-5C, URL ACL=REDIRECT
        ! URL Redirect=https://ise.nuglab.com:8443/guestportal/gateway?sessionId=...&portal=Our_Captive_Profile&action=cwa
        ! ACS ACL=xACSACLx-IP-Waiting_for_WebAuth-5436e367
        ```
    + ISE: 
        + Operations > Authentications > Identity=C8:BC:C8:97:00:5C, Status=ok, Authorization Profile=You_Must_WebAuth
        + Operations > Authentications > Identity=xACSACLx-IP-Waiting_for_WebAuth-5436e367
    + PC: IE (http://www.google.com) > Security Certificate Issue (due to redirect gi0/8 not trust certificate yet) > Continue > Redirect to https://ise.nuglab.com:8443/guestportal/gateway?sessionId=...&portal=Our_Captive_Profile&action=cwa, user=it-bob, pwd=Nuget!23
    + ISE Verification: Operations > Authentications > Refresh > Authorization Profile = AD_User_who_WebAuth, Identity=xACSACLx-IP-Waiting_for_WebAuth-5436e367
    + SW1: `show authentication sessions int gi0/8` - ACS ACL=xACSACLx-IP-Waiting_for_WebAuth-5436e367 (Updated ACL), User-Name=it-bob



