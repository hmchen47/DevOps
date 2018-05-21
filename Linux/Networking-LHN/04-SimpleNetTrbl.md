# CH04: [Simple Network Troubleshooting](http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch04_:_Simple_Network_Troubleshooting)

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
    + Shutdowned Interface: w/o IP address and `UP` & `RUNNING`
        ```shell
        wlan0   Link encap:Ethernet  HWaddr 00:06:25:09:6A:D7
                BROADCAST MULTICAST  MTU:1500  Metric:1
                RX packets:2924 errors:0 dropped:0 overruns:0 frame:0
                TX packets:2287 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:100
                RX bytes:180948 (176.7 Kb)  TX bytes:166377 (162.4 Kb)
                Interrupt:10 Memory:c88b5000-c88b6000
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
    + DHCP client auto assign: `192.168.x.x`
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
+ Commands determining ARP values
    + `fconfig -a` or `ip a`: NIC's MAC address and the associated IP addresses
    + `arp -a`: MAC addresses in ARP table

## Using `ping` to Test Network Connectivity

+ Send ICMP echo pkts and wait for ICMP echo-reply response
+ Reasons w/o reponse:
    1. server/IP addr not existed
    2. server not response
    3. firewall/router blocking
    4. incorrect routing
    5. incorrect IP addr or subnet mask
+ `ping -c <num>`: limit ping counts
+ "Destination Host Unreachable" message
    + Directly connected host:
        + client/server down or disconnected
        + incorrect duplex settings, check with `ethtool`
        + incorrect cable type
        + wireless: check SSID or encryption keys
    + host on remote network: routing issue


## Using `telnet` to Test Network Connectivity

+ w/ TCP port 23
+ Other than default port: `telnet <ip> <port>`
+ Guidelines to identify problems:
    + Test connectivity from the remote PC or server
    + Test connectivity on the server itself - loopback & NIC IP addr
    + Test connectivity from another server on the same network as the target -> firewall blocking
+ Linux `telnet` Troubleshooting
    + Successful Connection: 
        + "Connected to" message; 
        + `ctrl-]` to break and `quit` to exit
    + Connection Refused Messages
        + application not enabled
        + firewall blocking and rejecting: `iptables status`
    + `telnet` Timeout or Hanging
        +  abort the attempted connection after waiting a predetermined time for a response
        + Reasons:
            + server not existed or down
            + firewall blocking but not rejecting
+ `telnet` Troubleshooting Using Windows
    + Screen Goes Blank - Successful Connection
    + "Connect Failed" Messages = Linux Connection refused messages
    + `telnet` Timeout or Hanging


## Testing Web sites with the `curl` and `wget` Utilities

+ Web performance test: TCP port80 response time
+ text-based web browser: `curl`
+ recursively downloaded text-based web browser: `wget`
+ Rapid TCP port 80 response time but slow `curl` or `wget` -> misconfig on Web server or applications
+ Using `curl`: 
    + display header or complete body of HTML code of a Web page
    + just header and status code: `-I`
    + eg. `curl -I www.linuxhomenetworking.com`
+ Using `wget`
    + no timestamps: `-N`
    + eg. `wget -N www.linuxhomenetworking.com`

## The `netstat` Command

+ determine whether slowness due to high traffic volume
+ list all TCP ports w/ listening: `netstat -an` (all & numeric)

    | `netstat` Option | Description |
    |--------|-------------|
    | `-l`, `–listening` | display listening server sockets |
    | `-a`, `–all` | display all sockets (default: connected) |
    | `-r`, `–route` | display routing table |
    | `–i`, `–interfaces` | display interface table |
    | `-g`, `–groups` | display multicast group memberships |
    | `-s`, `–statistics` | display networking statistics (like SNMP) |
    | `-M`, `–masquerade` | display masqueraded connections |
    | `-v`, `–verbose` | be verbose |
    | `-W`, `–wide` | don’t truncate IP addresses |
    | `-n`, `–numeric` | don’t resolve names |
    | `-e`, `–extend` | display other/more information |
    | `-p`, `–programs` | display PID/Program name for sockets |
    | `-o`, `–timers` | display timers |
    | `-F`, `–fib` | display Forwarding Information Base (default) |
    | `-C`, `–cache` | display routing cache instead of FIB |

+ `ss`: dump socket statistics, the substitute of the `netstat`; [`netstat` vs. `ss`](https://computingforgeeks.com/netstat-vs-ss-usage-guide-linux/)

    | `ss` Option | Description |
    |--------|-------------|
    | `–n`, `–numeric` | don’t resolve service names |
    | `-r`, `–resolve` | : resolve host hostnames. |
    | `-l`, `–listening` | display listening sockets |
    | `-o`, `–options` | show timer information |
    | `-e`, `–extended` | show detailed socket information |
    | `-m`, `–memory` | show socket memory usage |
    | `-p`, `–processes` | show process using socket |
    | `–s`, `–summary` | show socket usage summary |
    | `-N`, `–net` | switch to the specified network namespace name |
    | `-4`, `–ipv4` | display only IP version 4 sockets |
    | `-6`, `–ipv6` | display only IP version 6 sockets |
    | `–0`, `–packet` | display PACKET sockets |
    | `-t`, `–tcp` | display only TCP sockets |
    | `-S`, `–sctp` | display only SCTP sockets |
    | `-u`, ``–udp` | display only UDP sockets |
    | `-w`, ``–raw` | display only RAW sockets |
    | `-x`, `–unix` | display only Unix domain sockets |
    | `-f`, `–family=FAMILY` | display sockets of type FAMILY |
+ TCP: mostly permanent connections
+ HTTP: connection shutdown after a pre-defined inactive timeout or `time_wait` period
+ Number of established and time_wait TCP connections on server: 
    ```shell
    netstat -an | grep tcp | egrep -i 'established|time_wait' | wc -l
    ```


## The Linux `iptables` Firewall

+ default in Fedora and RedHat
+ General rules:
    + different Linux distributions use different daemon management systems: sysV and systemd are commond ones
    + daemon name needs to be known
+ Things to know for daemon
    + Start your daemons automatically on booting
    + Stop, start and restart during troubleshooting & modification
+ __DO NOT__ turn off `iptables` firewall feature


## Using `traceroute` to Test Connectivity

+ `traceroute`: sending UDP pkts w/ incremental TTL
+ Possible `traceroute` Messages

    | Symbol | Description |
    |--------------------|------------|
    | `***` | Expected 5 second response time exceeded.  |
    | `!H`, `!N`, or `!P` | Host, network or protocol unreachable |
    | `!X` or `!A` | Communication administratively prohibited. A router Access Control List (ACL) or firewall is in the way |
    | `!S` | Source route failed. Source routing attempts to force traceroute to use a certain path.|
    + Possible cause of `***`:
        + A router on the path not sending back the ICMP "time exceeded" messages
        + A router or firewall in the path blocking the ICMP "time exceeded" messages
        + The target IP address not responding
    + `!S`: might be due to a router security setting
+ `traceroute` Time Exceeded False Alarms
    + No response within a 5-second timeout interval: `*`
    + Some devices allow ICMP but not `traceroute` pkts
+ `traceroute` Internet Slowness False Alarm
    ```shell
    C:\>tracert 80.40.118.227
    1      1 ms     2 ms     1 ms  66.134.200.97
    2     43 ms    15 ms    44 ms  172.31.255.253
    3     15 ms    16 ms     8 ms  192.168.21.65
    4     26 ms    13 ms    16 ms  64.200.150.193
    5     38 ms    12 ms    14 ms  64.200.151.229
    6    239 ms   255 ms   253 ms  64.200.149.14
    7    254 ms   252 ms   252 ms  64.200.150.110
    8     24 ms    20 ms    20 ms  192.174.250.34
    9     91 ms    89 ms    60 ms  192.174.47.6
    10    17 ms    20 ms    20 ms  80.40.96.12
    11    30 ms    16 ms    23 ms  80.40.118.227
    Trace complete.
    ```
    + congestion at hops 6 and 7 where the `response time > 200ms`
    + Internet routing devices w/ very low priority to traceroute pkts
+ `traceroute` Dies At The Router Just Before The Server
    + bad default gateway
    + firewall blocking
    + server down, disconnected, or incorrect NIC config
+ Always Get a Bidirectional `traceroute`
    + try both from src to dst and dst to src
    + return path might not the same as forward path
+ ping and `traceroute` Troubleshooting Example
    + `ping` TTLs timeouts: routing loop
    + solution: resetting both routing processes at both ends
+ `traceroute` Web sites
    + looking glasses: traceroute servers for ISP subscribers
    + `traceroute.org` lists looking glasses
+ Possible Reasons For Failed Traceroutes
    + blocked or rejected by a router in the path
    + target server not existed
    + routing tables w/o route to dst network
    + target IP addr typographical error
    + routing loop
    + no proper return path - solution:
        + logon the last visible router
        + check routing table for next hop
        + logon the next hop
        + execute `traceroute` to dst
        + success: execute `traceroute` back to src -> identify the bad route in return path
        + fail: test routing table and hops to dst

## Using `MTR` To Detect Network Congestion

+ __Matt's traceroute (MTR)__: an application to repeat traceroute in real time
+ dynamically show the round-trip time to reach each hop along the traceroute path
+ not only visual which hop slow but also when they slow
+ good tool to detect intermittent congestion
+ best, worst and average round trip times in msec for the probe packets
+ run `mtr` extensive period of time as a monitor of communication path quality
+ installed in Fedora by default

    ```shell
    [root@bigboy tmp]# mtr 192.168.25.26
                    Matt's traceroute  [v0.52]
    Bigboy                                            Fri Feb 20 17:19:17 2004
    Keys:  D - Display mode    R - Restart statistics    Q - Quit
                                        Packets               Pings
    Hostname                           %Loss  Rcv  Snt  Last Best  Avg  Worst
    1. 192.168.1.1                       0%    17   17    32   10   15     32
    2. 192.168.2.254                     0%    17   17    12   11   18     41
    3. 192.168.3.15                      0%    17   17    23   14   18     25
    4. 192.168.18.35                     0%    16   16    24   23   29     42
    5. 192.168.25.26                     0%    16   16    23   21   26     37
    ```

## Viewing Packet Flows with `tcpdump`

+ one of the most popular packages for viewing the flow of packets through NIC
+ default on RedHat/Fedora
+ determine whether you are getting basic two-way communication
+ Reasons for lack of communications:
    + bad routing
    + faulty cabling
    + port not listening - app not running
    + firewall or ACL blocking

+ Possible `tcpdump` Switches

    | switch | Description |
    |--------|-------------|
    | `-c` | Stop after viewing count packets. |
    | `-i` | Listen on interface. If this is not specified, then the command will use the `lowest numbered interface that is UP |
    | `-w` | Dump the output to a specially formatted TCPdump dump file |
    | `-C` | Specifies the size the dump file must reach before a new one with a numeric `extension is created. |
    | `-t` | Don't print a timestamp at the beginning of each line |

+ Useful `tcpdump` Expressions

    | expression | Description| 
    |-------------|------------|
    | `host <host-address>` | View packets from the IP address host-address|
    | `icmp` | View icmp packets| 
    | `tcp port <port-number>` | View TCP packets with packets with either a source or | `destination TCP port of port-number| 
    | `udp port <port-number>` | View UDP packets with either a source or destination UDP port of port-number| 

+ Example: 

    ```shell
    tcpdump -i wlan0 icmp tcpdump: listening on wlan0

    21:48:58.927091 smallfry > bigboy.my-site.com: icmp: echo request (DF)
    21:48:58.927510 bigboy.my-site.com > smallfry: icmp: echo reply
    21:48:58.928257 smallfry > bigboy.my-site.com: icmp: echo request (DF)
    21:48:58.928365 bigboy.my-site.com > smallfry: icmp: echo reply
    ...
    ```
    + 1st col: timestamp
    + 2ns col: src and dst IP addr/FQDN
    + 3rd col: pkt type
    + 4th col: pkt info

+ Analyzing `tcpdump` files
    + dump Ethernet frame into file: `-w`
    + analyze dump file with `Wireshark`

+ Common Problems with `tcpdump`
    + auto resolve DNS -> slow
    + stop DNS resolve: `-n`

## Viewing Packet Flows with `tshark`

+ Fedora Linux wireshark RPM
+ used to call `tethereal`
+ mimic `tcpdump` in many ways but `tshark` w/a number of advantages
    + dumping data to files w/ given size limit
    + ring buffer: limit the total number of files by overwriting
    + ore intuitive output but same dump file format
+ Possible `tshark` Switches

    | switch | Description |
    |--------|-------------|
    | `-c` | Stop after viewing count packets. |
    | `-i` | Listen on interface. If not specified, use the lowest numbered UP interface |
    | `-w` | Dump the output to a specially formatted TCPdump dump file |
    | `-C` | Specifies dump file size to create new w/ numeric extension |
    | `-b` | Ring buffer size when selecting `-C` |

+ Useful `tshark` Expressions

    | Expression | Description |
    |--------|-------------|
    | `host <host-address>` | View packets from the IP address host-address |
    | `icmp` | View icmp packets |
    | `tcp port <port-number>` | View TCP packets either a src or dst TCP port |
    | `udp port <port-number>` | View UDP packets either a src or dst UDP port |

+ Example

    ```shell
    tshark -i eth0 tcp port 80 and host 192.168.1.100

    Capturing on eth0
    0.000000 192.168.1.102 -> 192.168.1.100 TCP 1442 > http [SYN] Seq=3325831828 Ack=0 Win=5840 Len=0
    0.000157 192.168.1.100 -> 192.168.1.102 TCP http > 1442 [SYN, ACK] Seq=3291904936 Ack=3325831829 Win=5792 Len=0
    0.000223 192.168.1.102 -> 192.168.1.100 TCP 1442 > http [ACK] Seq=3325831829 Ack=3291904937 Win=5840 Len=0
    ...
    ```

## Basic DNS Troubleshooting

+ Using `nslookup` to Test DNS
    + used to get associated IP addr for given domain and vice versa
    + query sent to DNS server for a response
    + failure caused by incorrect settings in `/etc/resolv.conf`
+ Using `nslookup` to Check Your Web site Name, eg., `nslookup www.linuxhomenetworking.com`
+ Using `nslookup` To Check Your IP Address, e.g., `nslookup 216.151.193.92`
+ Using `nslookup` to Query a Specific DNS Server, e.g., `nslookup www.linuxhomenetworking.com 68.87.96.3`
+ Using the `host` Command to Test DNS - newer cmd
    
    ```shell
    host 216.151.193.92
    host www.linuxhomenetworking.com
    host www.linuxhomenetworking.com 68.87.96.3
    ```

## Using `nmap`

+ determine all the TCP/IP ports on which a remote server is listening
+ a favorite tool of malicious surfers
+ Commonly Used NMAP Options

    | Argument | Description |
    |----------|-------------|
    | `-P0` | Nmap first attempts to ping a host before scanning it.  |
    | `-T` | Defines scanning period  |
    | `-O` | Detect the OS based on responses |
    | `-p` | Lists the TCP/IP port range to scan. |
    | `-s` | Defines scan methods |

## Using `netcat` to Test Network Bandwidth

+ used to create a TCP socket over which to transfer data
+ `netcat` = `nc`
+ signify the program to listen, and not talk
    + listening on TCP port: `nc -l <port>` and `nc <ip> <port>`
    + redirection: `nc -l 7777 > FC-6-i386-disc1.iso` and `nc -l 7777 > /dev/null`

## Determining the Source of an Attack

+ DoS type attacks: 
    + a large numbers of established connections
    + an excessive number of entries in firewall or Web server logs
+ `whois` w/ IP addr or FQDN to get administrative information

## Who Has Used My System?

+  The `last` Command
    + determine who has logged into system
    + e.g., `last [-<num>]`
+  The `who` Command
    + who currently logged in
    + e.g. `who`
    
