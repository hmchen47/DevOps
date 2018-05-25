# EIGRP Lab - INE Getting Start with GNS3

+ Objectives
    + Create a topology of
        + 4 routers
        + Redundant paths
        + Serial and Ethernet links
    + Config EIGRP such that
        + All routers in the same Autonomous System
        + Two routers use EIGRP authentication
        + End-routers prefer slow-speed end-to-end paths
        + Wireshark captures EIGRP neighbourship pkts
        + Using snapshot to record different stages of config

    <br/><img src="./diagrams/EIGRP-ine.png" alt="EIGRP Lab" width="600">

+ GNS3 Lab
    + Build topology and adding annotation
        + Take 1st snapshot: 'topology'
        + Powwer on all routers
    + Addin IP addresses
        ```cfg
        # R1
        config terminal
        interface loopback 0
        ip address 11.11.11.1 255.255.255.0
        int s0/0
        ip addr 1.2.1.1 255.255.255.0
        no shut
        int f0/0
        ip addr 1.3.1.1 255.255.255.0
        no shut
        exit
        wr

        # R2
        conf t
        int s0/0
        ip addr 1.2.1.2 255.255.255.0
        no shut
        int s0/1
        ip addr 2.4.2.2 255.255.255.0
        no shut
        end
        wr

        # R3
        conf t
        int f0/0
        ip add 1.2.1.3 255.255.255.0
        no shut
        int f0/1
        ip add 3.4.3.3 255.255.255.0
        no shut
        end
        wr

        # R4
        conf t
        int s0/0
        ip add 2.4.2.4 255.255.255.0
        no shut
        int f0/0
        ip add 3.4.3.4 255.255.255.0
        no shut
        end
        wr
        ```
        + Verify the settings on all routers
            + Execute `show` cmd in config mode: `do show ...`
            + Links status: `show ip int br` -> associate links _UP/IP_
        
        + Take 2nd snapshot: 
            + Ensure all router running config are __SAVED__
            + Turn off all routers
            + take snapshot: 'ipaddr-config'

    + EIGRP Config w/ AS 100 & Observe pkts on the line btw R3 & R4
        ```config
        # R1
        conf t
        router eigrp 100
        network 11.11.11.0 0.0.0.255
        net 1.2.1.0 0.0.0.255
        net 1.3.1.0 0.0.0.255
        end 
        wr

        # R2
        conf t
        router eigrp 100
        net 1.2.1.0 0.0.0.255
        net 2.4.2.0 0.0.0.255
        end 
        wr

        # Enable Wireshark to capture pkts btw R3 & R4

        # R3
        conf t
        router eigrp 100
        net 1.3.1.0 0.0.0.255
        net 3.4.3.0 0.0.0.255
        end 
        wr

        # R4
        conf t
        router eigrp 100
        net 2.4.2.0 0.0.0.255
        net 3.4.3.0 0.0.0.255
        end 
        wr
        ```
        + Verify EIGRP settings
            + Route: `sh ip route` & `sh ip route eigrp`
            + Topology: `sh ip eigrp top all-links` & `sh ip eigrp nei`
            + Connectivity: R1> 'ping 44.44.44.4`
        + Take 3rd snapshot
            + turn off all router
            + snapshoot: 'eigrp-config'
    + Adding EIGRP Authentication
        ```cfg
        # R1
        conf t
        key chain ine
        key 1
        key-string ine
        int f0/0
        ip auth mode eigrp 100 md5
        ip auth key-chain eigrp 100 ine
        end
        wr

        # R3
        conf t
        key chain ine
        key 1
        key-string ine
        int f0/0
        ip auth mode eigrp 100 md5
        ip auth key-chain eigrp 100 ine
        end
        wr
        ```
        + Verify: `sh ip eigrp neighbor`
        + Snapshot: 'eigrp-auth'
    + EIGRP Path selection
        + Manipulating bandwdith and delay
        ```cfg
        # R1 - no effect
        sh ip route     # wnsure which route used
        sh ip eigrp route all-links     # check default delay
        
        conf t
        int s0/0
        delay 1
        do wr

        sh ip eigrp top     # which link used

        # R2 - no effect
        conf t
        int s0/0
        delay 1
        do wr

        # R1
        sh ip eigrp top     # no change yet
        conf t
        int f0/0
        delay 55555
        do wr

        # R4 - retunr still use fastEthernet
        sh ip route 

        ```
        + Verify
            + Link used: `sh ip eigrp top`
            + Connectivity w/ performance: `trace 44.44.44.4`
        + Snapshot: 'path-config'



