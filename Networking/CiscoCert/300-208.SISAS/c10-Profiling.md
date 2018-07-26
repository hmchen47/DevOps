# ISE Profiling

+ ISE Profiler Service: What are you?
    + Why profile?
    + Methods for Discovery

+ Purpose of Profile
    1. handy - exact picture what connecting to network
    2. Authorization policy - Identity Groups

+ Demo: NAD Basic Configuration Validation
    ```cfg
    show run | include radius|Nugget!23
    ! aaa group server radius ISE-group
    ! aaa authentication login default enable
    ! aaa authentication login FREE none
    ! aaa authentication dot1x default group radius
    ! aaa authorization network default group radius
    ! aaa accounting dot1x default start-stop group radius
    ! aaa server radius dynamic-aothor
    !   client 192.168.1.117 server-key Nugget!23
    ! ip radius source-interface vlan1
    ! radius-server attribute 6 on-for-login-auth
    ! radius-server attribute 8 radius-access-in-request
    ! radius-server attribute 25 access-request include
    ! radius-server dead-criteria time 30 tries 3
    ! radius-server vsa send accounting
    ! radius-server vsa send authentication
    ! radius server ISE
    !   key Nugget!23
    ```

+ Demo: Device connected to Network <br/>
    Administration > Identity Management > Identities > Endpoints > Windows7Workstation: Identity Group=Workstation, Matched Policy=Windows 7 Workstation, Total Certainty Factor=60, OUI=Dell Inc., MAC=A4:DB:B1:B1:50:13, User-Agent=Mozilla/5.0 (Windows NT 6.1; wow64;Trident 7.0;rv:11.0) like Gecko

+ Demo: Create Profile to Identity <br/>
    Administration > System-Deployment > ISE (Edit Node) >
    + General Session Tab: 
        + Administration=(Role=STANDALONE -> PRIMARY)
        + Policy Service=(Enable session service, Enable __profiling service__)
    + Profiling Configuration Tab:
        + NetFlow: port=9996
        + DHCP: port=67, `ip helper`, DHCP probe
        + DHCPSPAN: DHCP scan probe
        + HTTP: port=80, set in ISE
        + RADIUS: Radius session attributes + CDP & LLDP from IOS sensor
        + NMAP: scanning endpoints for open ports and OS, Manual Scan subnet=(192.168.1.0/24 > Run Scan) > click to see latest scan results (Administration > Identity Management Endpoints)
        + DNS: timeout=2, Desc=DNS probe perform a DNS lookup for the FQDN
        + SNMPQUERY: Retries=2, Timeout=1000, EventTimeout=30, Desc=details of network devices including interfaces, CDP, LLDP, and ARP
        + SNMPTRAP: 

+ Demo: ISE:
    + Endpoint scan results: Administration Identity Management > Identities > Endpoints: HP-Devo=ices (hdDevice Descr=HP LaserJet Professional p1102w), Windows 7 Workstation
    + Ensure SNMP Settup Correctly: Administration > Network Resources > Network Devices > SW1: Authentication Settings=(Protocol=RADIUS, Shared secret), SNMP Settings=(SNMP Versin=3, ...)
    + Specify what key or string for specifying a SNMP setting: Administration > System - Settings > Profiling:
        + No CoA
        + Port Bounce
        + Reauth
    
+ Demo: Policy Profile Validation
    + Policy > Profiling: select appropriate profile (Filter existed), e.g., Microsoft Workstation: Minimum Certainty Factor=10, Network Scan (SNMP) Action=Common Port and OS scan, Create an identity group for the policy=yes, 
    + Home page: Profiled Endpoints=2
    + Operations > Reports > Endpoints and Users ? Profiled Endpoints Summary (Time Range=Last 7 days) > Run > Summary: Policy=((HP-Device, Windows 7 Workstation) > Details on Windows-Workstation: detailed info
    + Administration > System - Licenses > ISE: License Type=Base-Eval (54 days), Advanced/Plus - Eval (54 days), Base (Active/Allowed)=2/100









