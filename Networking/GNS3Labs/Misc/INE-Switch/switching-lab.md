# Switching Lab - INE Getting Start with GNS3

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
        int f0/0.4
            encapulation dto1q 4
            ip addr 1.2.4.1 1.2.4.1 255.255.255.0
        int f0/0.5
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
        ip route 1.2.4.0 255.255.255.0 2.3.2.1
        ip route 1.2.5.0 255.255.255.0 3.2.3.1
        int f0/0.2
            enc dot 2
            ip add 2.3.2.1 255.255.255.0
        int f0/0.3
            enc dot 3
            ip add 3.2.3.1 255.255.255.0
        int f0/0
            no shut
        do sh ip int br
        do sh ip route
        do wr

        # R2
        conf t
        int f1/0
            ip add 2.3.2.2 255.255.255.0
            no shut
        int f0/1
            ip add 3.2.3.2 255.255.255.0
            no shut
        int f0/0.2
            enc dot 4
            ip add 1.2.4.2 255.255.255.0
        inf f0/0.5
            enc dot 5
            ip add 1.2.5.2 255.255.255.0
        int f0/0.2
            enc dot 4
            ip add 1.2.4.2 255.255.255.0
        int f0/0.3
            enc dot 5
            ip add 1.2.5.2 255.255.255.0
        int f0/0
            no shut
        do sh ip in tbr
        do wr
        ```
        + Verify: R2 & R3 connecctivity
        