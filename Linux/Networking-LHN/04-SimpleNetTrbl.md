# CH04: Simple Network Troubleshooting

## Introduction

+ Sources of Network Slowness
    + NIC duplex and speed incompatibilities
    + Network congestion
    + Poor routing
    + Bad cabling
    + Electrical interference
    + An overloaded server at the remote end of the connection
    + Misconfigured DNS

+ Sources of a Lack of Connectivity
    + Slowness --> lost connectivity
        + Additional sources of disconnections
            + power failures
        + shutdown on remote server or app

+ Doing Basic Cable and Link Tests
    + NIC's "link" light -> connection functioning correctly if on
    + wrong cable type
    + Other sources:
        + bad cable
        + switch/router power down
        + improper plugged cable
    + tool: battery-operated cable tester

## Testing NIC

+ Viewing Your Activated Interfaces: `ifconfig` or `ip addr`
+ Viewing All Interfaces: `ifconfig -a` or `ip addr` or `ip a`
    + Shut Down Interface
        ```shell
        wlan0   Link encap:Ethernet  HWaddr 00:06:25:09:6A:D7
                BROADCAST MULTICAST  MTU:1500  Metric:1
                ...
        ```
    + Active Interface
        ```shell
        wlan0   Link encap:Ethernet  HWaddr 00:06:25:09:6A:D7
                inet addr:216.10.119.243  Bcast:216.10.119.255
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:2924 errors:0 dropped:0 overruns:0 frame:0
                TX packets:2287 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:100
                RX bytes:180948 (176.7 Kb)  TX bytes:166377 (162.4 Kb)
                Interrupt:10 Memory:c88b5000-c88b6000
        ```
+ DHCP Considerations
    + DHCP client auto assign: `192.168.x.x
    + check IP addr if failed to communicate w/ DHCP server

### Testing Link Status from the Command Line

+ Link Status Output from `mii-tool`
    ```shell
    $ mii-tool -v

    eth0: 100 Mbit, full duplex, link ok
        product info: Intel 82555 rev 4
        basic mode:   100 Mbit, full duplex
        basic status: link ok
        capabilities: 100baseTx-FD 100baseTx-HD 10baseT-FD 10baseT-HD
        advertising:  100baseTx-FD 100baseTx-HD 10baseT-FD 10baseT-HD flow-control
        link partner: 100baseTx-HD
    ```
+ Link Status Output from `ethtool`
    ```shell
    $ ethtool eth0

    Settings for eth0:
            Supported ports: [ TP MII ]
            Supported link modes:   10baseT/Half 10baseT/Full
                                    100baseT/Half 100baseT/Full
            Supports auto-negotiation: Yes
            Advertised link modes:  10baseT/Half 10baseT/Full
                                    100baseT/Half 100baseT/Full
            Advertised auto-negotiation: No
            Speed: 100Mb/s
            Duplex: Full
            Port: MII
            PHYAD: 1
            Transceiver: internal
            Auto-negotiation: off
            Supports Wake-on: g
            Wake-on: g
            Current message level: 0x00000007 (7)
            Link detected: yes
    ```

### Viewing NIC Errors

+ `ifconfig` Error Output: number of overrun, carrier, dropped packet and frame errors
+ `ip -s link` or `ip -s a` Error Output: number of overrun, carrier, dropped packet and frame errors
+ `ethtool` Error Output: `-S` for detailed report
+ `netstat` Error Output: `-i` for limited report
+ Possible Causes of Ethernet Errors
    + __Collisions__ 
        + Signifies when the NIC card detects itself and another server on the LAN attempting data transmissions at the same time.
        + Normal: $< 0.1\%$ of all frames sent
    + __Single Collision__: Ethernet frame went through after only one collision
    + __Multiple Collision__: attempt multiple times before successfully sending the frame
    + __CRC Errors__: 
        + Frames sent but w/ corrupted in transit
        + electrical noise: CRC error but not many collisions
        + chk: correct type of cable; undamaged cable; securely fastened
    + __Frame Errors__: 
        + incorrect CRC and non-integer number of bytes
        + chk: collisions; bad Ethernet device
    + __FIFO and Overrun Errors__: 
        + unable of handing data to its memory buffers
        + chk: sign of excessive traffic
    + __Length Errors__: 
        + incorrect frame length
        + chk: incompatible duplex settings
    + __Carrier Errors__:
        + NIC card losing its link connection to the hub or switch
        + chk: faulty cabling or interfaces

## How to See MAC Addresses

+ check ARP table
+ Possible casues of lack of communications:
    + server disconnected
    + faulty cabling
    + NIC disable or server down
    + firewall for remote server
+ Commands for ARP values
    + 

## Using `ping` to Test Network Connectivity

## Using `telnet` to Test Network Connectivity

+ Linux `telnet` Troubleshooting

+ Successful Connection

+ Connection Refused Messages

+ `telnet` Timeout or Hanging

+ `telnet` Troubleshooting Using Windows

+ Screen Goes Blank - Successful Connection

+ "Connect Failed" Messages

+ `telnet` Timeout or Hanging

## Testing Web sites with the `curl` and `wget` Utilities

+ Using `curl`

+ Using `wget`

## The `netstat` Command

## The Linux `iptables` Firewall

+ How to Configure `iptables` Rules

## Using `traceroute` to Test Connectivity

+ Sample `traceroute` Output

+ Possible `traceroute` Messages

+ `traceroute` Return Code Symbols

+ `traceroute` Time Exceeded False Alarms

+ `traceroute` Internet Slowness False Alarm

+ `traceroute` Dies At The Router Just Before The Server

+ Always Get a Bidirectional `traceroute`

+ ping and `traceroute` Troubleshooting Example

+ `traceroute` Web sites

+ Possible Reasons For Failed Traceroutes

## Using `MTR` To Detect Network Congestion

## Viewing Packet Flows with `tcpdump`

+ Table 4-2 : Possible `tcpdump` Switches

+ Table 4-3 : Useful `tcpdump` Expressions

+ Analyzing `tcpdump` files

+ Common Problems with `tcpdump`

##Viewing Packet Flows with `tshark`

+ Table 4-4 : Possible `tshark` Switches

+ Table 4-5 : Useful `tshark` Expressions

## Basic DNS Troubleshooting

+ Using `nslookup` to Test DNS

+ Using `nslookup` to Check Your Web site Name

+ Using `nslookup` To Check Your IP Address

+ Using `nslookup` to Query a Specific DNS Server

+ Using the host Command to Test DNS

## Using `nmap`

+ Table 4-6 Commonly Used NMAP Options

## Using `netcat` to Test Network Bandwidth

## Determining the Source of an Attack

## Who Has Used My System?

### The `last` Command

### The `who` Command