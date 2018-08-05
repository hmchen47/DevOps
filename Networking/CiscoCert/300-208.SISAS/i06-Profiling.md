# Endpoint Profiling

## EndPoint Profiling

+ What is Profiling ?
    + Profiling
        + Allowing ISE to learn attributes about network connected endpoints
        + Assigning endpoint to appropriate identity groups base on profile
        + Groups can be used in authorization policy for smarter network access control decisions
        + Especially useful for devices that perform MAB, but not only
    + Two types of profiling
        + Static profiling: manually assigned to a group
        + Dynamic profiling: endpoint attributes are dynamically learned through the use of probes
    + By default, dynamic profiling is turned off
        + Endpoints are still automatically profiled based on MAC address
        + However, only device vendor can be detected, so it’s not very specific
    + Demo: ISE - Administration > Identity Management > Identities > Endpoints > Add: 
        + MAC Address=48:f8:3b:2e:25:32
        + Static Assignment (Specific group added, but not shown in Authorization policy): Policy Assignment=Apple-iPad, ...
        + Static Group Assignment (Able to be used in Authorization Policy): Identity Group Assignment=Cisco-IP-Phone
        + If both selected, device auto detected

+ Dynamic Profiling
    + Automatic fingerprinting of the endpoint based on several probes
        + ISE: listen for probes
        + NAD: send probes
    + RADIUS, highly recommended
        + Inspects RADIUS attributes from the Access Request
        + Inspects RADIUS accounting for IP-MAC binding, required for NMAP scanning or DNS resolution of endpoint
        + Used also for IOS Device sensor feature, supported starting with 15.0(2) on switches and 7.2.110.0 on WLC

+ Most Commonly Used Probes
    + HTTP
        + ISE interprets HTTP messages from CWA or SPAN
        + Gathers __User-Agent__ from HTTP packet, used to identify the _operating system_ on the device
            + Crucial for mobile device profiling
    + DHCP
        + ISE interprets DHCP messages from DHCP-Relay or SPAN
        + Gathers __User-Agent__ from DHCP packet, used to identify the _operating system_ on the device
        + Gathers DHCP __hostname__: Important for _mobile device profiling_
        + Useful only in DHCP environments

+ Less Commonly Used Probes
    + NMAP
        + TCP/UDP port scanning for operating system detection
    + SNMP query send by ISE
        + Used only in case NAD does not support device sensor
        + Triggered by RADIUS accounting or SNMP trap
        + Reads CDP/LLDP/ARP/MAC data
    + DNS resolution performed by ISE
        + Reverse DNS query for PTR records to get the FQDN of the endpoint
        + Query initiated only if device profiles through other probes: RADIUS, DHCP, HTTP, SNMP
        + Not primary tool
    + Netflow samples
        + Detects abnormal traffic (profiled printer making skype calls on the Internet)

+ Profiling Flow
    <a href="https://www.slideshare.net/Cisco_Mobility/wireless-lan-security-policy-and-deployment-best-practices">
        <br/><img src="https://image.slidesharecdn.com/v1brkewn-2021c2securitypolicybestpractices-111214120915-phpapp02/95/wireless-lan-security-policy-and-deployment-best-practices-23-728.jpg?cb=1324564339" alt="Device Profiling" width="450">
    </a>


## Profiling Policies

+ Profiling Policies
    + ISE has a large database of built-in profiling policies
        + Can profile many devices out-of-the-box, given that enough data is received from probes
        + Additional policies can be manually configured, or you can edit the built-in ones
        + Logical profile is a container with associated profiling policies
    + ISE has a built-in hierarchy for device profiling, in the form of parent-child, for example
        + Parent policy is named Apple-Device
        + Child policy attached to the parent policy can be Apple-iPad or Apple-iPhone
    + Profiling policies are built on a set of conditions for device identification
        + In order to be profiled as Apple-iPad, conditions for both parent and child policy need to be satisfied

+ Profiling Policies Settings
    + Minimum Certainty Factor
        + How sure is ISE about endpoint being identified
        + Integer value which needs to be met in order for endpoint to be assigned to be profile policy
    + Associated CoA type
        + When endpoint is profiled and assigned to a specific group, do you want CoA to be performed
    + Rules
        + Each rule is a condition matching on collected endpoint attributes
        + Each rule as an associated action, most commonly being to increase the Certainty Factor
            + NMAP SCAN is an alternative action
    + Demo: ISE - Policy > Profiling > Profiling Policies > Apple Device: Name=Apple Device, Minimum Certainty Factor = 10, Exception Action = None
    + Demo CoA?
        + Procedure: 1) Creating profile; 2) Implement 802.1x for IP Phone
        + Conditions: 1) Phone connected to SW; 2) Profiling data sends to ISE
    + Demo: Rules - Policy > Profiling Policies > Apple-Device: 
        + Rule=(if Apple-DeviceRule1-SCAN then Take Network Scan Action, if Apple-DeviceRule1Check1 then Certainty Factor Increases 10)
        + Apple-DeviceRule1Check1: Expression=MAC:OUI CONTAINS Apple
    + Demo: Rule Child Policy - Policy > Profiling Policies > Apple-Device > Apple-iPhone
        + Name=Apple-iPhone, Minimum Certainty Factor=20
        + Ruless=(if Apple-iPhoneRule2Check1 then Certainty Factor Increases 20, if Apple-i{honeRule1Check1 then Certainty Factor Increases 20})
        + Apple-iPhoneRule2Check1 Expression=DHCP:hostname CONTAINS iPhone
        + Apple-i{honeRule1Check1 Expression=IP:User-Agent CONTAINS iPhone

+ Profiling Result
    + It can happen that the device is authorized by ISE before being accurately profiled
    + Thus, usually CoA is also deployed with profiling
        + Allows to change device authorization after being profiled
    + In general, by deploying ISE in phases, all devices will be profiled before going to Closed Mode
    + Because of profiling, CoA is triggered when
        + Endpoint profiled for 1st time
        + Endpoint statically assigned to a group
        + Endpoint removed from ISE database
        + Endpoint dynamically changed identity group membership

## ISE Authorization Flow with Profiling

+ ISE Authorization Flow with Profiling
    + How AAA order of processing is changed
        + Endpoint Authentication
        + Initial Authorization Policy pushed (endpoint not profiled yet)
        + Profiling data is received or asked for
        + Device is profiled and assigned to a identity group
        + ISE triggers CoA requesting endpoint re-authentication
        + Endpoint Authentication
        + Final authorization matching the conditions for the identity group
    + Because authorization rules are processed top-down
        + Order of rules is very important

+ Profiling Configuration Steps on NAD
    + Configure RADIUS accounting to ISE: `aaa accounting dot1x default start-stop group <grp>`
    + Configure NAD to relay _endpoint IP address_ in RADIUS Access- Request message, requires device tracking to be enabled: `radius-server attribute 8 include-in-access-req`
    + Configure DHCP-Relay: `ip helper-address <ise_ip>`
    + Configure NAD to relay _endpoint DHCP class attribute_ in RADIUS Access-Request message: `radius-server attribute 25 access-request include`
    + Configure NAD to send Netflow samples and SNMP traps to ISE

+ Profiling Configuration Steps on ISE
    + Ensure that Enable Profiling Service check box is selected on the PSN (default)
    + Enable Profiling Probes
        + Activates interpretation of probe messages
    + Enable CoA for Profiling
    + Optionally, tune the profiler conditions and policies
        + Configure authorization policies using as condition the profiled endpoints
    + Most deployments use a separate physical port on ISE to receive data from probes
        + Probes may send hug amount of data, especially if SPAN is used
        + SPAN is, in general not recommended for performance
        + It leaves a dedicated port just for regular RADIUS authentication

+ NAD 802.1x Port Modes
    + Single Host (default)
        + Single MAC address allowed in data domain
        + Second MAC address results in violation action
    + Multi Domain
        + Single MAC address allowed per domain (voice and data)
        + Second MAC address for each domain results in violation action
    + Multiple Authentication
        + Single MAC address allowed in voice domain
        + Multiple MAC addresses allowed in data domain
            + VLAN authorization possible, single VLAN supported
    + Multiple Host
        + Only first MAC address is required to authenticate
        + No ACL and Redirect URL support

## Profiling Configuration

+ Topology
    <br/><img src="./diagrams/sisas-net0.png" alt="Network with IP Phone" width="600">
    + SW3: DHCP Server
    + SW1: Default Gateway for IP Phone & PC-A

+ Demo: Profiling
    + SW1 Config:
        ```cfg
        show run int vlan80
        ! interface VLAN 80
        !   ip address 136.1.80.8 255.255.255.0
        !   ip helper-address 10.10.10.10
        ! end

        conf t
        int vlan80
          ip helper-address 172.16.3.100 255.255.255.0
        end
        show run int f1/0/5
        ! interface VLAN 80
        !   ip address 136.1.80.8 255.255.255.0
        !   ip helper-address 10.10.10.10       - SW3 
        !   ip helper-address 172.16.3.100      - ISE -> Profiling
        ! end

    + ISE Config
        + Persona: Administration > Deployment > ISE1-12 > Persona: Policy Service=(Enable session service, Enable Profiling Service)
        + CoA: Administration > System Setting > Profiling: CoA Type=Reauth > Save
        + Profiling: Administration > Deployment > ISE1-12 > Profiling Configuration Tab: DHCP=(Interface=Gi1/0/5) > Save

    + SW1 Verification:
        ```cfg
        show run int f1/0/5
        ! interface FastEthernet1/0/5
        !   switchport access vlan 81
        !   switcport mode access
        !   switchport voice vlan 80
        !   logging event spanning-tree
        !   spanning-tree portfast
        ! end

        conf t
        int f1/0/5
          shut
        end
        ! No action taken
    + SW3 Verification 
        ```cfg
        show ip dhcp binding
        ! 136.1.80.101  0100.036b.3c35.f0   automatic
        ! 172.16.20.101 0148.f8b3.3e25.32   automatic
        clear ip dhcp binding 136.1.80.101
        show ip dhcp binding
        ! 172.16.20.101 0148.f8b3.3e25.32   automatic
        ! expect to get IP Phone address back later

    + Verification
        + SW1: `conf t; int f1/0/5; shut; no shut; ^Z`
        + SW3: `show ip dhscp inding` - 172.16.20.101, 136.1.80.101
        + ISE: Administration > Identity Management > Identities > Endpoints > Cisco-IP-Phone: IP addr=136.1.80.102 (different from .101) > delete
        + SW1: `conf t; int f1/0/5; shut; no shut; exit`
        + ISE: Administration > Identity Management > Identities > Endpoints > Cisco-IP-Phone > Refresh: IP Addr=138.1.80.102
    + Why not `.101`?: IP Phone sent request w/ old `.101` address to DHCP server and ISE, but get NACK from DHCP Server and got new IP address `.102` eventually,.  However, ISE already got `.101`

+ Disable Default Rules in Production Environment
    + AuthN Policy: Policy > Authentication > Default
    + AuthZ Policy: Policy > Authorization > Default: Condition=(PermitAccess)
    + Default rules allowing any types of Radius traffic
    + Authorization Default rules used in Monitor/Low Impact Mode, but not Closed Mode

+ Demo: Hierarchy Rule and Certainty Factors
    + SW1: `show run | i radius|aaa` - None
    + ISE Config
        + Profiling: Policy > Profiling > Profiling Policies > Cisco Devices > Cisco-IP-Phone > Cisco-IP-Phone-7960
            + Cisco Devices: Minimum Certainty Facor=10, Rules=(if Cisco-DeviceRule3Check1 then Certainty Factor Increases 10), Expression=MAC:OUI CONTAINS Scientific Atlanta
            + Cisco-IP-Phone: Minimum Certainty Factor=20, Rules=(if CiscoIPPhoneDHCPClassIdentifier then Certainty Factor Increases 20), Expression=DHCP:dhcp-class-identifier CONTAINS Cisco Systems, Inc. IP Phone
            + Cisco-IP-Phone-7960: Minimum Certainty Factor=70, Rules=(if CiscoIPPhone7960 then Certainty Factor Increases 70), Expression=CDP:cdpCachePlatform CONTAINS Cisco IP Phone 7960
        +Identity:  Administration > Identity Management > Identities > Endpoints > Cisco-IP-Phone: EndpointPolicy=Cisco-IP-Phone, EndpointProfilerServer=ISE1-12.inelab.local, EndpointSource=DHCP Probe, Identity Group=Cisco-IP-Phone, MAC Address=00:03:68:3c:35:f0, __dhcp-class-identifier=Cisco Systems, Inc. IP Phone CP-7960__
        + AuthZ Policy: Policy > Authorization > Profiled Cisco Ip Phone: Condition=Cisco-IP-Phone, Permissions=Cisco_IP_Phones > Edit: Conditions=(Endpoint Identity Group > Profiled > Cisco-IP-Phone)
            + Cisco-IP-Phone is a general profile than a specific one
            + Endpoint Identity Group used as a condition
        + Each profiling policy manually configures ISE to make Authorization Policy visible for that Identity Group
        + Parent Profiling: Policy > Profiling > Profiling Policies > Cisco-Ip-Phone: Create an Identity Group for the Policy = Yes
        + Child Profiling: Policy > Profiling > Profiling Policies > Cisco-Ip-Phone > Cisco-IP-Phone-7960: Create an Identity Group for the Policy = Yes (was No) > Save
        + AuthZ Policy: Policy > Authorization > Profiled Cisco IP Phones: Conditions=(Endpoint Identity Groups > Profiled > Cisco-IP-Phone-7960)

+ Demo: Authenticate IP Phone
    + Procedures:
        1. Config SWS1 to authenticate IP Phone to ISE with MAB
        2. Ensure Authentication & Authorization policies to authenticate IP Phone
    + ISE Config
        + AuthN Policy: Policy > Authentication > MAB: Conditions=(Wired_MAB OR Wireless_MAB), Allowed Protocols=Default Network Access, use=Internal Endpoints
        + Profile: Policy > Policy Elements > Results > Authentication > Authentication Profile > Cisco_IP_Phone: Common Tasks=(DACL=PERMIT_ALL_TRAFFIC, Voice Domain Permission)
    + SW1:
        ```cfg
        conf t
        aaa new-model
        aaa authentication dot1x default group
        aaa group server radius ISE_RADIUS
          server-private 172.16.3.100 key sw1radius
          ip radius source-interface Loopback0
        exit
        do show run | b aaa group
        ! aaa group server radius ISE_RADIUS
        !   server-private 172.16.3.100 auth-port 1645 acct-port 1646 key sw1radius
        !   iip radius source-interface loopkback 0
        ! end
        aaa authentication dot1x default group ISE_RADIUS
        aaa authorization network default group ISE_RADIUS
        radius server vsa send authentication
        do show run int f1/0/5
        ! interface FastEthernet 1/0/5
        !   switchport access vlan 81
        !   switchport mode access
        !   switchport voice vlan 80
        !   logging event spanning-tree
        !   spanning-tree portfast
        ! end
        int f1/05
          mab
        ^Z
        show mac address-table int f1/0/5
        ! 80 0003.6b3c.35f0 DYNAMIC f1/0/5  - voice
        ! 81 0003.6b3c.35f0 DYNAMIC f1/0/5  - data: phone
        ! 81 48f8.b32e.2423 DYNAMIC f1/0/5  - data: PC-A

        conf t
        int f1/0/5
          authentication port-control auto
          shut
          no shut
        end
        do show mac address-table int f1/0/5
        ! 80 0003.6b3c.35f0 DYNAMIC f1/0/5  - voice

        ! AUTHMGR-7-RESULT: Authentication result 'server dead' from 'amb' for client

    + PC-A: 
        + NIC > Properties > Authentication > disable IEEE 802.1x authentication
        + `ifconfig /all` - Mac addr=18:f8:3b:2e:24:23 & lost connection to ISE

    + SW3: `debug radius authentication; conf t; int f1/0/5; shut; no shut; end`
    + ISE: Administration > Network Resource - Network Device > Add: Name=SW1, IP 10.8.8.8/32, Authentication settings=(shared secret=sw1radius) > Submit
    + SW1: 
        ```cfg
        test aaa group ISE_SERVER peap-user Cisco123! legacy
        ! RADIUS(00000000): started 5 sec timeout 
        ! No Radius connectivity
        
        ping 172.16.3.100   ! ok
        show run | b aaa group
        ! aaa group server radius RADIUS
        !   server_private 172.16.3.100 auth-port 1645 acct-port 1646 key sw1radius
        !   ip radius source-interface lo0
        ! end
        ! aaa authentication dot1x default group ISE_RADIUS
        ! aaa authorization network default group ISE_RADIUS
        ! aaa session-id common
        ! switch 1 provision ws-c3750-24p
    + ISE: Operations > Authentication > Last Error Entry > details: Event=Radius Request dropped, Failure Reason=Could not locate Network Device ot AAA client, NAS IP Address=136.1.83.8 (sw1 source ip, not lo0)
    + SW1:
        + config ignoring `ip radius source-interface lo0` 
        ```cfg
        conf t
        aaa group server radius ISE_RADIUS
          ip radius source-interface lo0
          no server-private 172.16.3.100 auth-port 1645 acct-port 1646 key sw1radius
          server-private 172.16.3.100 auth-port 1645 acct-port 1646 key sw1radius
        end
        test aaa group ISE_RADIUS peap-user Cisco123! legacy        ! timeout

        conf t
        aaa group server radius ISE_RADIUS
          no server-private 172.16.3.100 auth-port 1645 acct-port 1646 key sw1radius
          server 172.16.3.100
        exit
        radius-server host 172.16.3.100 key sw1radius
        ^Z

        test aaa group ISE_RADIUS peap-user Cisco123! legacy        ! timeout

        conf t
        no aaa group server radius ISE_RADIUS
        no aaa authentication dot1x default group ISE_RADIUS
        no aaa authorization network default group ISE_RADIUS
        aaa group server radius ISE
          server host 172.16.3.100
        exit
        radius-server host 172.16.3.100 key sw1radius
        ip radius source-interface lo0
        exit

        test aaa group ISE_RADIUS peap-user Cisco123! legacy
        ! User was successfully authenticated
        ```
    + Reason: bug on Naming, ISE_RADIUS not working

+ Demo: Multi-Domain
    + SW1:
        ```cfg
        conf t
        aaa authentication dot1x default group ISE
        aaa authorization network default group ISE
        do debug radius authentication
        int f1/0/5
          shut
          no shut
        end
        ! RADIUS: Cisco AVpair="ip:ineacl#2=permit udp any host 172.16.20.100 eq 53"
        ! RADIUS: Cisco AVpair="ip:ineacl#3=permit tcp any any eq 80"
        ! RADIUS: Cisco AVpair="ip:ineacl#4=permit tcp any any eq 8443"
        ! RADIUS: Cisco AVpair="ip:ineacl#5=permit tcp any host 172.16.3.10"
        ! WRONG ACL
        ```
    + ISE: 
        + Policy > Authorization > Profiled Cisco IP Phone (2nd entry)
        + Administration > Identity Management > Identities > Endpoints > Cisco IP Phone

    + SW1:
        ```cfg
        show authentication sessions
        ! interface=f1/0/5, MAC=48f8.b32e.2423, method=mab, Domain=DATA, 
        ! Status=Authz Failed, Session ID=8801530800000002142D1F0C
        show authentication sessions int f0/1/5
        ! User-Name=48-F8-B3-2E-24-23, Oper host mode=single-host, method=mab, status=Authc Success
        ```
    + Single Host mode not allow any host on voice domain
    + SW1: 
        ```cfg
        conf t
        int f1/0/5
          authentication host-mode multi-domain
          do debug radius authentication 
        exit
        ^Z
        ! ...
        udebug all
        ! RADIUS(00000005): Send Access-Request to 172.16.3.100 id 1645/19
        ! RADIUS: Service Type=Call Check
        ! RADIUS: Calling-Station-ID="00-03-6B-3C-35-F0"
        ! RADIUS: Received from ID 1645/19 172.16.3.100:1645 Access-Accept
        ! RADIUS: Cisco AVpair="device-traffic-class=Voice"
        ! RADIUS: Cisco AVpair="ACS CiscoSecure-Defined-ACL=#ACSACL#-IP-PERMIT_ALL_TRAFFIC-51ef7db1"

        show authentication sessions
        ! f1/0/5    48f8.b32e.2423  mab DATA    Authz Failed    880153080000002142D1F0C
        ! f1/0/5    0003.6b3c.35f0  mab VOICE   Authz Success   88015380000000314301948

        show authentication sessions int f1/0/5
        ! ignore Data portion
        ! Domain=Voice, User-Name=00-03-6b-3c-35-f0
        ! ACS ACL=xACSACLx-IP-PERMIT_ALL_TRAFFIC-51ef7db1

        show ip access-lists int f1/0/5
        ! access list is Auth-Default-ACL

        ip device tracking
        ip device tracking probe interval 30
        ip device tracking probe use-vsi
        epm logging 
        int f1/0/5
          shut
          no shut
        end
        ! EPM-6-POLICY_REQ: ... | EVENT APPLY
        ! EPM-6-AUTH_ACL: POLICY AUTH-Default-ACL
        ! EPM-6-AAA: POLICY xACSACLx-IP-PERMIT_ALL_TRAFFIC-51ef7db1 | EVENT DOWNLOAD-REQUEST
        ! EPM-6-AAA: POLICY xACSACLx-IP-PERMIT_ALL_TRAFFIC-51ef7db1 | EVENT DOWNLOAD-SUCCESS
        ! EPM-6-IPEVENT: IP 0.0.0.0 ...
        ! EPM-6-POLICY_APP_SUCCESS: ...

        show ip device tracking all
        ! IP=136.1.80.104, MAC=0003.6b3c.35f0, vlan=80, state=ACTIVE

        show ip access-lists int f1/0/5     ! permit ip any any
        ping 136.1.80.104                   ! ok
        show authentication sessions
        ! User-Name=00-03-6b-3c-35-f0, Oper host mode=multi-domain


## Device Sensor Overview

+ IOS Device Sensor Overview
    + Scales profiling service on ISE
    + Highly recommended to be deployed
    + Less data with more details for ISE to interpret
    + The NAD gathers endpoint attributes through CDP, LLDP and DHCP
        + CDP and LLDP need to be enabled on the NAD
    + Sends the collected endpoint attributes to ISE through RADIUS accounting messages
        + Uses Cisco AV pairs

+ DHCP Device Sensor Configuration Steps
    + Configure a list of DHCP options to be collected: 
        + `device-sensor filter-list dhcp list <list_name>`
        + `option name host-name`
        + `option name client-identifier`
        + `option name client-fqdn`
        + `option name class-identifier`
    + Activate the DHCP sensor option: `device-sensor filter-spec dhcp include list <list_name>`

+ CDP Device Sensor Configuration Steps
    + Configure a list of CDP TLV’s to be collected
        + `device-sensor filter-list cdp list <list_name>`
        + `tlv name device-name`
        + `tlv name capabilities-type`
        + `tlv name platform-type`
    + Activate the CDP sensor option
        + `device-sensor filter-spec cdp include list <list_name>`

+ LLDP Device Sensor Configuration Steps
    + Configure a list of LLDP TLV’s to be collected
        + `device-sensor filter-list lldp list <list_name>`
        + `tlv name port-id`
        + `tlv name system-name`
        + `tlv name system-capabilities`
    + Activate the LLDP sensor option: `device-sensor filter-spec lldp include list <list_name>`

+ Device Sensor Common Configuration
    + Enable RADIUS accounting
        + `aaa accounting dot1x default start-stop group`
        + `aaa accounting update newinfo`
        + `radius-server vsa send accounting`
    + Globally activate IOS sensor
        + `device-sensor accounting`
        + `device-sensor notify all-changes`
    + Globally activate CDP and LLDP
        + `cdp run`
        + `lldp run`

+ Device Sensor Verification
    + Verify probe functionality
        + `show lldp`
        + `show cdp`
        + `show device-sensor cache all`
    + Verify collected data per endpoint
        + `show device-sensor cache mac <mac_address>`
    + Verify that collected data is being sent to ISE
        + `show aaa method-lists accounting`
        + `debug radius accounting`


+ Demo:
    + ISE: enable Radius Accounting <br/>
        Administration > Deployment > ISE1-12 > Profiling Configuration Tab: Radius enable > Save
    + SW3:
        ```cfg
        show run | i aaa
        ! aaa new-model
        ! aaa authentication dot1x default group radius
        ! aaa authorization network default group radius
        ! aaa accounting dot1x default group fdfd
        ! aaa server radius dynamic-author
        ! aaa session-id commom

        conf t
        no aaa accounting dot1x default group fdfd
        aaa accounting dot1x default group radius
        radius-server vsa send accounting
        aaa accounting update newinfo
        ^Z
        show cdp        ! Active
        show lldp       ! Active

        conf t
        device-sensor notify all-changes

        ! CDP device sensors
        device-sensor filter-list cdp CDP_SENSOR
          tlv name device-name
          tlv name capabilities-type
          tlv name platform-type
        exit
        device-sensor filter-spec cdp include list CDP_SENSOR

        ! LLCP Device sensors
        device-sensor filter-list lldp LLDP_SENSOR
          tlv name port-id
          tlv name system-name
          tlv name system-capabilities
        exit
        device-sensor filter-spec lldp include list LLDP_SENSOR

        ! DHCP device sensors
        device-sensor filter-list dhcp DHCP_SENSOR
          option name hostname
          option name client-identifier
          option name client-qfdn
          option name class-identifier
        exit
        device-sensor filter-spec dhcp include list DHCP_SENSOR

        do show run int gi/1/0/5
        ! interface GigabitEthernet1/0/5
        !   switchport access vlan 90
        !   switchport mode access
        !   logging event spanning-tree
        !   authentication open
        !   authentication port-control auto
        !   dot1x pae authenticator
        !   spanning-tree portfast
        ! end

        do show logging
        ! console logging: level debugging
        ! monitor logging: level informational
        ! Buffer logging: level debugging

        debug radius accounting
        ```
    + Verification
        + SW3:
            ```cfg
            conf t
            int gi1/0/5
              shut
              authentication port-control force-authorized
              no shut
            exit

            show device-sensor cache all    ! port gi1/0/5
            ! cdp 1: device-name; cdp 4: capabilities-type; cdp 6: platform-type

            show run int vlan90
            ! interface vlan 90
            !   ip address 17.16.20.1 255.255.255.0

            show ip dhcp binding    ! 136.1.80.104, 172.16.20.101
            clear ip dhcp binding 172.16.20.101
            show ip dhcp binding    ! 136.1.80.104
            conf t
            int f1/0/5
              shut
              no shut
            end

            show ip dhcp binding    ! 136.1.80.104
            ```
        + PC-B: NIC -> identifying

    + TRBL
        + SW3:
            ```cfg
            conf t
            int gi1/0/5
              no dot1x authenticator
              no authentication open
              shut
              authentication port-control force-authorized
              no shut
            end
            ! restart PC-B, NIC keeps showing identifying

            ! Remove DHCP capability
            show run | i dhcp
            ! ip dhcp exclude-address 136.1.80.1 136.1.80.100
            ! ip dhcp exclude-address 136.1.81.1 136.1.81.100
            ! ip dhcp exclude-address 172.16.20.1 172.16.20.100
            ! ip dhcp pool VLAN80-PHONE
            ! ip dhcp pool VLAN81-PC-A
            ! ip dhcp pool VLAN90-PC-B

            conf t
            no device-sensor filter-spec dhcp include list DHCP_SENSOR
            do show ip dhcp binding     ! 136.1.80.104, 172.16.20.101
            device-sensor filter-spec dhcp include list DHCP_SENSOR
              option name hostname
              option name client-identifier
              option name client-qfdn
              option name class-identifier
            exit
            
            show device-sensor cache all
            ! dhcp 60: class-identifier; dhcp 12: host-name; dhcp 61: client-identifier
            ! cdp 4: capabilities-type; cdp 6: platform-type; cdp 2: device-name
        + ISE: Administration > Identity Management > Identities > Endpoints > Not showing
        + SW3:
            ```cfg
            conf t
            no device-sensor accounting
            device-sensor accounting
            no device-sensor notify all-change
            device-sensor notify all-change
            aaa accounting update periodic 1
            end
        + ISE: Administration > System > Deployment > ISE1-12 > Profiling Configuration Tab: RADIUS, DHCP
        + SW3: 
            ```cfg
            clear ip dhcp binding 172.16.2.101
            conf t
            int f1/0/5
              shut 
              no shut
            exit
            int f1/0/5
              shut
              no shut
            exit
    + DHCP device sensor: new feature -> bug



