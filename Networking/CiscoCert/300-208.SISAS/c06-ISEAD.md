# Integrating ISE and AD

+ Using External Authentication: Leveraging Active Directory
    + Verify basic functionality and DNA
    + Join ISE to AD
    + Create and Use Identity source Sequence

+ ISE & AD
    + AD (Windows server 2012): DNS Server, CA, DC
    + Join ISE into Domain - Using AD as Identity Source
    + Sequence: AD + Local

+ Demo: PC Validation - EAP work correctly: AnyConnect > Network > Network Details > Managing Networks > Add: Name=test, wired, Security=802.1x, 802.1x Config=(password, EAP-FAST) > ok

+ Demo: SW1 Validation
    ```cfg
    show authentication sessions 
    ! Status=Authz Success, Session ID=010203040000000040001565c

    show authentication sessions int gi0/7
    ! mab=Not Run, dot1x=Authc Success

    conf t
    int gi0/7
      shut
      no shut
    end
    ! AUTHMGR-5-START: starting 'dot1x' for client
    ! AUTHMGR-7-RESULT: Authentication result 'Success' from 'dot1x' for client
    ```

+ Demo: ISE Verification
    + Operations > Authentications > top entry > Details: Event=Authentication Succeeded, Uername=bob, IP=192.168.1.120, Identity Store=Internal Users (on ISE), Authentication protocol = EAP-FAST(EAP-MSCHAPv2) [outer(innner)], Network Device=Sw1, NSA Port=GigabitEthernet0/7
    + Steps: (Tools for TRBL)
        + 15013 Selected Identity Store - Internal User
        + 24210 Looking up user in Internet User ID Store - bob
        + 24212 Found user in Internal users ID Store
        + 22037 Authentication passed
        + 11824 EAP-MSCHAP authentication attempted passed

+ Demo: ISE CLI Validation
    ```cfg
    ! Basic connectivity between ISE and AD
    ping 192.168.1.123              ! ok
    ping server1.nuglab.com         ! failed, DNS issue?

    conf t
    ip name server 192.168.1.123
    ! restart service automatically

    show application status ise     ! still initializing
    ! ...
    show application status ise     ! ISE application server is running
    ```

+ Demo: Join ISE into Domain
    + ISE Config: 
        + Create Identity store: Administration > Identity Management > External Identity Stores > Active Directory: Domain Name=nuglab.com, Identity Store Name=AD1 > Save
        + Validation: Administration > Identity Management > External Identity Stores > Active Directory > ise.nuglab.com: Status=Not Joined to Domain
        + Test Connectivity: Administration > Identity Management > External Identity Stores > Active Directory > ise.nuglab.com (checked) > Test Connection (Basic Test): user=administrator, pwd=Nugget!23 > Status=Success, pwd for user 'administrator' is correct > ok
        + Test Connectivity: Administration > Identity Management > External Identity Stores > Active Directory > ise.nuglab.com (checked) > Test Connection (Detailed Test): user=administrator, pwd=Nugget!23 > Status=Success, Ip=192.168.1.117, Not found in DNS > Close
        + Join Domain: Administration > Identity Management > External Identity Stores > Active Directory > ise.nuglab.com (checked) > Join: user=administrator, pwd=Nugget!23 > ok > Status = Successful
        + Refresh: Test Connectivity: Administration > Identity Management > External Identity Stores > Active Directory > ise.nuglab.com (checked) > Refresh > Status=Connected to server1.nuglab.com
    + Windows Server 2012
        + Server Manager > Tools > Active Directory Users and Computers > nuglab.com > Computers: Name=ise, Type=Computer
        + Server Manager > Tools > Active Directory Users and Computers > nuglab.com (rc) > New > User: logon name=bob@nuglab.com > Next > pwd=Nugget!23, Never Expired > Next

+ Demo: Create & Use Identity Store Sequence
    + Create sequence: Administration > Identity Management > Identity Store Sequences > Add: Name=Use_AD_then_Local, Search List=(AD1, Internal Users), Advanced Search List Settings=Treat as if the user was not found and proceed to the next store in the sequence 
    + Enforce as Policy: Policy > Authentication > Dot1x > edit: use=Use_AD_then_Local > Save

+ Verification
    + PC: AnyConnect > Network Profile=test
    + SW1: 
        ```cfg
        ! AUTHMGR-5-SUCCESS: Authorization succeeded for client

        show authentication session int gi0/7
        ! mab=Nor Run, dot1x=Authc Success
        ```
+ Demo: Which Identity Store used?
    + ISE: 
        + Operations > Authentications > Refresh > top entry > Details > Steps -> Internal user
        + Identity Source sequence=Use_AD_the_Local -> search list ok
        + AuthN Policy: Policy > Authentication > Dot1x: use=Use_AD_the_Local -> ok
    + SW1
        ```cfg
        conf t
        int gi0/7
          shut
          no shut
        end
        ```
    + ISE - Logging: Operations > Authentications > repeated count increased -> same issue
    + Caching issue: AD Server > Server Manager > Tools > AD Users and Computers > Users (rc) > New > Users: Name=it-bob > Next > pwd=Nugget!23, never expired > Next > Finish

    + Wipeout cache: AnyConnect (remove test and add again then using it-bob as user) > Network Repair 
    + SW1: `show authentication session int gi0/7` - dot1x=Authc Success
    + ISE: Operations > Authentications > Top Entry > Details: Steps - Selected Identity Store - AD1, User Authentication against Active Directory succeeded



