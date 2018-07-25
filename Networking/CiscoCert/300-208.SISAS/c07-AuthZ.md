# Authorization Profiles, ISE, AD and Rules

+ 802.1x Authorization: ISE Leveraging AD Groups
    + DNS and copy run start
    + Adding a PC to a Domain
    + EAP Chaining
    + Authorize based on AD Groups

+ Demo: DNS on ISE
    + ISE CLI
        ```cfg
        copy start run      ! keep changes
        show start
        ! hostname ISE
        ! ip domain-name nuglab.com
        ! interface GigabitEthernet0
        !   ip address 192.168.1.117 255.255.255.0
        !   ipv6 address autoconfig
        ! ip name-server 192.168.1.123
        ! ip default-gateway 192.169.1.1
        ! clock timezone UTC
        ! ntp server time.nist.gov
        ! username admin password $...1 role admin
        ! max-ssh-session 5
        ! service sshd enable
        ```
    + AD Server: Server Manager > Tools > DNS=DNS Manager > SERVER1-ForwardLookupZones-1.168.192.in-addr=arpa: ise.nuglab.com, server1.nuglab.com, it-bob-pc.nuglab.com
    + PC: 
        + AnyConnect NAM Profile=Class Fast: Not editable from Network Details -> Created from Profile Editor
        + NAM Profile editor > Network > wired > edit: Name=wired, Media=Wired (802.3) Network, Security levle=Open, Connection Type=User > Save As: configuration.xml (auto load into AnyConnect at startup)
    + SW1: 
        ```cfg
        show authentication sessions            ! all ports with Authentication session
        show authentication sessions int gi0/7  ! port detail
        ```

+ Demo: Adding a PC to Domain <br/>
    Computer (rc) > Properties > Computer name, domain, and networking groups settings > Change Settings > Change: Computer Name-it-bob-pc, Member of Domain=nuglab.com

+ Demo: EAP Chaining
    + SW1: `dot1x reauthentication int gi0/7`
    + ISE Verification: Operations > Authentications > latest entry > Details: Identity Store=AD1, EAP Chaining result=No Chaining, username=it-bob
    + ISE Config
        + Protocol: Policy > Policy Elements > Results > Authentication > Allowed protocols >Default Network Access: Allowed Protocols=(..., EAP-FAST=(Enable 'Enable EAP Chaining'), ...) > Save
        + Verification: Operations > Authentications > record last entry time for later comparison with Identity=it-bob
    + SW1: `dot1x re-authenticate int gi0/7`
    + ISE Verification: Operations > Authentications > Refresh > last entry w/ Identity=(it-bob >> host.it-bob-pc) > Details: username=(it-bob,host/it-bob=pc), Use Case=EAP Chaining

+ Demo: Authorization based on AD Groups
    + ISE associating AD Group: Administration > Identity Management - External Identity Sources > Active Directory > AD1 > Groups > Add: (Select Group from Directory): Domain=nuglab.com, Filter=(Retrieve Groups=nuglab.com/Users/Domain Users > ok) [Changes on AD will refect here]
    + AD Server: Server Manager > Tools > AD Users and Computers > nuglab.com - Users (rc) > New > Group: Name=AD-Group-ISE, scope=Global, Type=Security > ok
    + ISE: Administration > Identity Management - External Identity Sources > Active Directory > AD1 > add (select Groups from Directory): nuglab.com/Users/AD-Group-ISE > ok > Save Configuration
    + PC: `ping 8.8.8.8` - ok

+ Demo: ACL to restict ping 8.8.8.8
    + Restrict with ACL for accessing 8.8.8.8 locally but no restriction on ISE authorization
    + SW1 Config:
        ```cfg
        conf t
        ip access-list extended SAMPLE-ACL
          deny icmp any host 8.8.8.8
          permit ip any any
        exit

        int gi0/7
          ip access-group SAMPLE-ACL in
        end
        ```
    + PC Verification: `ping 8.8.8.8` - timeout, `ping google.com` - ok
    + ISE DACL: 
        + Create DACL: Policy > Policy Elements > Results > Authorization > Downloadable ACLs (default: __DENY_ALL_TRAFFIC__ (deny ip any any), __PERMIT_ALL_TRAFFIC__ (permit ip any any)) > Add: Name=Our_ACL, Contents=(permit icmp any any) > Save
        + Profile: Policy > Policy Elements > Results > Authorization Profiles (default: __Blackhole_Wireless_Access, Cisco+IP_Phones, DenyAccess, Non_Cisco_IP_Phones, PermitAccess__) > Add: Name=PERMIT_ALL_TRAFFIC, VLAN=(ID/NAME=1) > Submit
        + AuthZ Policy: Policy > Authorizations (default: __Wireless Black List Default, Profiled Cisco IP Phones, Profile Non-Cisco IP Phones, Default__) > defalt >  Edit (Insert New Rule Above): Name=User and PC Authorized, Conditions=(Create New Condition > __Network Access:EAPChainingResult EQUALS User and Machine both succeeded__, Add Attribute/Value > __AD1:ExternalGroup EQUALS nuglab.com/Users/AD-GROUP-ISE), Permissions=(Standard > Our_Auth_Profile) > Done > Save
    + PC: `ping 8.8.8.8` - timeout
    + SW1 Config: `dot1x re-authentication int gi0/7` - push down DACL to NAD
    + PC: `ping 8.8.8.8` - ok
    + SW1: `show authentication sessions int gi0/7` - VLAN Policy=1, ACS ACL=xACSACLx-IP-PERMIT_ALL_TRAFFIC-537cb1d6
    + ISE: Operations > Authentication > top entry w/ Identity=xACSACLx-IP-PERMIT_ALL_TRAFFIC-537cb1d6 > Details








