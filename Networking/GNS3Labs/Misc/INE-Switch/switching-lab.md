# Switching Lab - INE Getting Start with GNS3


## EtherSwitch Router [Switching Cmds](https://www.cisco.com/c/en/us/support/docs/interfaces-modules/network-modules/82156-ether-switch-nm-config.html#step1):

+ Create VLANs: `vlan database`, `vlan <#>`
+ Config VLANs: `intferace vlan <#>`, `ip add <ip> <mask>`, `ip helper-address <ip>`
    + `ip helper-address` cmd: configured on all the VLANs except VLAN 10 in order to obtain the IP address from the DHCP server to the devices located at these VLANs
    + Verification: `show vlan-switch`
+ Configure VTP, Trunk, Port Channel, and Spanning Tree
    + VTP Configuration: `vtp mode {client|server|transparent}`, `vtp domain <name>`
    + Spanning-Tree: `spanning-tree vlan <#> {root|priority|max-age}`, `spanning-tree vlan <#> root {primary|secondary}`
    + Trunk and Port Channel: `interface port-channel <#>`, `switchport mode trunk`, `switchport trunk encapsulation dot1q`, , `switchport trunk allowed vlan {<#-#,#>|add <#-#,#>|all|except <#-#,#>|none|remove <#-#,#>}`, `channel-group <#> mode on`
    + Verification: `show vtp status`, `show interface <if> trunk`, `show spanning-tree summary`
+ Configure Access Ports: `int <if>`
    + Switchport: `switchport mode access`, `switchport access vlan <#>`
    + Spanning tree: `spanning-tree {cost|priority|portfast|vlan}`
    + Verification: `show vtp status`, `show interface <if> trunk`, `show spanning-tree summary`
+ Configure the Voice Port: `int <if>`
    + Switchport: `switchport mode access`, `switchport access vlan <#>` `switchport voice vlan <#>`
    + Spanning tree: `spanning-tree {cost|priority|portfast|vlan}`
    + Verification: `show vtp status`, `show interface <if> trunk`, `show spanning-tree summary`
+ Configure Quality of Service (QoS)
    + WRR-Queue: `wrr-queue cos-map <queue-number> <cos values separated by space>`, `wrr-queue bandwidth <Weight of Queue1> <Weight of Queue2>[ <Weight of Queue3> <Weight of Queue4> ...]`
    + QoS Verification: `show wrr-queue bandwidth`, `show wrr-queue cos-map`, `show mls qos maps dscp-cos`
+ Configure the Port to Trust CoS: `int <if>`
    + Cos: `mls qos trust cos`, `mls qos cos override`
+ Configure Policer:
    + ACL: `ip access-list {standard|extended} <name>`, `{permit|deny} <proto> {src IP|any|host} {dst IP|any|host|eq|gt|lt|neq|range} <action>`
    + Class map: `class-map <name>`, `match class <acl-name>`
    + Policy map: `policy-map <name>`, `class <cls-name>`
    + Apply to interface: `int <if>`, `service-policy input <pol-name>`
    + Verification: `show policy-map`
+ Cisco `interface range` cmd
    + Syntax: `interface range {{e|f|gi} slot/interface - interface} [, {{e|f|gi} slot/interface - interface}...]`
    + e.g., `interface range fastethernet 5/1 - 5, gigabitethernet 1/1 - 2`

## Configuting Cisco [EtherSwitch VLAN & VTP](https://www.cisco.com/c/en/us/td/docs/ios/interface/configuration/guide/ir_ft1636nm.html#wp1434381)

+ Config VLANs (privilege mode): `vlan database`, `vlan <id>`, `exit`
    + Verify: `show vlan name VLAN<#>`, `show vlan-switch brief`
+ Remove VLAN Database: `vlan database`, `no vlan <id>`, `exit`
+ Configuring VLAN Trunking Protocol (VTP)
    + VTP Server: `vlan database`; `vtp server`; `vtp domain <name>`; `vtp password <pwd>`; `exit`
    + VTP Client: `vlan database`; `vtp client``, `exit`
    + Disbaling VTP: `vlan datbase`; `vtp transparent`; `exit`
    + VTP version 2: `vlan database`; `[no] vtp v2-mode`; `exit`
    + Verify: `show vtp status`

## Configuring Cisco [EtherSwitch Spanning Tree](https://www.cisco.com/c/en/us/td/docs/ios/interface/configuration/guide/ir_ft1636nm.html#wp1434889)

+ Enabling Spanning Tree
    + cmd: `spanning-tree vlan <id>`
    + verify: `show spanning-tree vlan`
+ Configuring Spanning Tree Port Priority
    + Cmds: `int <if>`; `spanning-tree port-priority <pri>`; `spanning-tree vlan <id> port-priority <pri>`; `<pri>`= 1~255
    + Verify: `show spanning-tree int <if>`
+ Configuring Spanning Tree Port Cost
    + Cmds: `int <if>`; `spanning-tree cost <cost>`; `spanning-tree vlan <id> cost <cost>`; `<cost>`=1~65,535
    + Verify: `show spanning-tree vlan <id>`
+ Configuring the Bridge Priority of a VLAN
    + Cmds: `spanning-tree vlan <id> priority <pri>`
    + Verify: `show spanning-tree vlan bridge`
+ Configuring the Root Bridge & Disable Spanning Tree
    + Cmds: `spanning-tree vlan <id> root primary [hops [hello=time <sec>]]`, `no spanning-tree vlan <id>`
    + Verify: `show spanning-tree vlan <id>`

## Lab

+ Objectives
    + Create topology of
        + 3 routers & 3 switches
        + One Ethernet switch
        + 2 EtherSwitch Routers
    + Config the topology as shown in diagram
        + Port between both EtherSwitch Routers should have the same interface numbers (i.e. FasEthernet 1/2 connect to FastEthernet 1/2)
        + Cannot manually config LAN4 & 5 on the VTP client
        + Ensure that pkts sent btw R1 & R2 on VLAN5 traverse acrosse the 2 EtherSwitch Routers on the hightest number ports
        + Static routes must be used for end-to-end IP reachability

    <br/><img src="./switching-lab.png" alt="text" width="600">


+ Configurations
    + Building the physical topology
        + R1, R2, & R3: C3725
        + SW1: Ethernet Switch
            + Delete all defualt ports
            + add ports: port 1 - VLAN 2, port 2 - VLAN 3, port 3 - VLAN 1
        + ESW1, ESW2: EtherSwitch Router
    + Adding IP addresses and static routes
        ```cfg
        # R1
        conf t
        int f0/0.4      ! VLAN 4
            encapulation dto1Q 4
            ip addr 1.2.4.1 1.2.4.1 255.255.255.0
        int f0/0.5      ! VLAN 5
            enc dot1q 5
            ip addr 1.2.5.1 255.255.255.0
        int f0/0
            no shut
            end
        ip route 2.3.2.0 255.255.255.0 1.2.4.1
        ip route 3.2.3.0 255.255.255.0 1.2.5.1
        do sh ip int br
        do sh ip route
        do wr

        # R3
        conf t
        ip route 1.2.4.0 255.255.255.0 2.3.2.2
        ip route 1.2.5.0 255.255.255.0 3.2.3.2
        int f0/0.2      ! VLAN 2
            enc dot 2
            ip add 2.3.2.3 255.255.255.0
        int f0/0.3      ! VLAN 3
            enc dot 3
            ip add 3.2.3.3 255.255.255.0
        int f0/0
            no shut
        do sh ip int br
        do sh ip route
        do wr

        # R2
        conf t
        int f0/1        ! VLAN2
            ip add 2.3.2.2 255.255.255.0
            no shut
        int f1/0        ! VLAN3
            ip add 3.2.3.2 255.255.255.0
            no shut
        int f0/0.4      ! VLAN 4
            enc dot 4
            ip add 1.2.4.2 255.255.255.0
        int f0/0.5      ! VLAN 5
            enc dot 5
            ip add 1.2.5.2 255.255.255.0
        int f0/0
            no shut
        do sh ip int br
        do wr
        ```
        + Verify: R2 & R3 connecctivity
            + VLAN: `show vlan-switch`

    + Config VTP & VLANs on EtherSwitch Routers - C2691-ADVENTERPRISEK9-M, IOS 12.4(23)
        ```cfg
        # ESW2 - Get VLAN config from ESW-1
        vlan database
            vtp domain INE
            vtp client
            exit
        conf t
        int range f1/9 , f1/15
            switchport mode trunk
            no sut
        do wr

        # ESW1
        vlan database
            vtp domai INE
            vtp server
            vlan 4
            vlan 5
            exit
        conf t
        int range f1/9 , f1/15
            switchport mode trunk
        do wr
        ```
        + Verify:
            + VTP: `show int trunk`, `show vlan-switch`, `show spanning-tree {brief|int <if>|root|summary|vlan <#>}`
            <pre>
            ESW1#show interface trunk<br/>
            Port      Mode         Encapsulation  Status        Native vlan
            Fa1/9     on           <b style="color:darkred">802.1q         trunking</b>      1
            Fa1/15    on           <b style="color:darkred">802.1q         trunking</b>      1<br/>
            Port      Vlans <b>allowed on trunk</b>
            Fa1/9     1-1005
            Fa1/15    1-1005<br/>
            Port      Vlans allowed and <b>active</b> in management domain
            <b>Fa1/9     1,4-5</b>
            <b>Fa1/15    1,4-5</b><br/>
            Port      Vlans in spanning tree forwarding state and not pruned
            Fa1/9     1,4-5
            Fa1/15    none<br/>
            ESW1#show interfaces f1/9 switchport 
            Name: Fa1/9
            Switchport: Enabled
            Administrative Mode: trunk
            <b>Operational Mode: trunk</b>
            Administrative Trunking Encapsulation: dot1q
            Operational Trunking Encapsulation: dot1q
            [output ommited...]<br/>
            ESW1#show vlan-switch 
            VLAN Name                             Status    Ports
            ---- -------------------------------- --------- --------------------------
            1    default                          active    Fa1/0, Fa1/1, Fa1/2, Fa1/3
                                                            Fa1/4, Fa1/5, Fa1/6, Fa1/7
                                                            Fa1/8, Fa1/10, Fa1/11, Fa1/12
                                                            Fa1/13, Fa1/14
            <b style="color:darkred">4    VLAN0004                         active</b>  <-- ESW-2 learned from ESW-1
            <b style="color:darkred">5    VLAN0005                         active</b>  <-- ESW-2 learned from ESW-1
            </pre>

            + Connectivity: R1 - `ping 2.3.2.3`, `ping 3.2.4.3`
    + Troubleshooting:
        + EWS2: `sh run interface f1/0` -> no config
            ```cfg
            conf t
            int f1/0
                switch mode trunk
                no shut
            do wr
            ```
            + Connectivity: R1 - `ping 1.2.4.2`
        + ESW1: `sh run | s interface` --> 1/0 not configured
            ```cfg
            conf t
            int f1/0
                switchport mode trunk
                no shut
            do wr
            ```
            + Verify: `sh spanning-tree int f0/0`: listening->learning->forwarding
                <pre>
                ESW1#sh spanning-tree int f1/0
                Port 41 (FastEthernet1/0) of VLAN1 is <b style="color:darkred">forwarding</b>
                  Port path cost 19, Port priority 128, Port Identifier 128.41.
                  Designated root has priority 32768, address c004.2860.0000
                  Designated bridge has priority 32768, address c005.26e0.0000
                  Designated port id is 128.41, designated path cost 19
                  Timers: message age 0, forward delay 0, hold 0
                  Number of transitions to forwarding state: 1
                  BPDU: sent 742, received 0
                </pre>
        + R1: `show ip int br`=> ok; `sh ip route` => ok
        + ESW2: `show int f0/0 switchport`=> ok; `sh int trunk` => ok; `sh span vlan 4` => ok; `sh span vlan 5` => ok
            <pre>
            ESW1#show spanning-tree vlan 4<br/>
            VLAN4 is executing the ieee compatible Spanning Tree protocol
              Bridge Identifier has priority 32768, address c005.26e0.0001
              Configured hello time 2, max age 20, forward delay 15
              Current root has priority 32768, address c004.2860.0001
              Root port is 50 (FastEthernet1/9), cost of root path is 19
              Topology change flag not set, detected flag not set
            [output omitted...]<br/>
            Port 41 <b style="color:darkred">(FastEthernet1/0) of VLAN4 is forwarding</b>
            [output omitted...]<br/>
            Port 50 (FastEthernet1/9) of VLAN4 is <b style="color:darkred">forwarding</b>
              Port path cost 19, Port priority 128, Port Identifier 128.41.
              Designated root has priority 32768, address c004.2860.0001
              Designated bridge has priority 32768, address c005.26e0.0001
              Designated port id is 128.41, designated path cost 19
            [output omitted...]<br/>
              Port 56 (FastEthernet1/15) of VLAN4 is <b style="color:darkred">blocking</b>
              Port path cost 19, Port priority 128, Port Identifier 128.56.
            [output omitted...]
            </pre>
        + ESW1: `sh span vlan 4` => ok; `sh span vlan 5` => ok
        + R2: `sh ip intbr` => f0/0 down; 
            ```cfg
            conf t
            int f0/0 
                no shut
            do wr
            ```
        + R1: `ping 2.3.2.3`, `ping 3.2.3.3`
    + Modify STP for VLAN 5 w/ higher number ports (`f1/15`)
        + Situation: traffic between R1 & R2 across f1/9
        + Requireemnt: VLAN 5 traffic flows btw f1/15
        + Moving root bridge: 
            + `show spanning-tree vlan <#>` 
                <pre>
                ESW2#show spanning-tree vlan 5<br/>
                VLAN5 is executing the ieee compatible Spanning Tree protocol
                Bridge Identifier has priority 32768, address c004.2860.0001
                Configured hello time 2, max age 20, forward delay 15
                We are the  <b style="color:darkred">root of the spanning tree</b>
                Topology change flag not set, detected flag not set
                [output omitted...]
                </pre>
            + Not working -> the blocking port moves from ESW-2 to ESW-1 on the same link -> traffic still not flow on the link btw f1/15
        + Moving root port
            + Solution: bandwidth & cost
            + Solution 1: reduce cost or port priority on f1/15
                <pre>

                </pre>



