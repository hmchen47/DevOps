# Ch03 : [Linux Networking](http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch03_:_Linux_Networking)

## How to Configure Your NIC's IP Address

+ Determining Your IP Address: 
    + cmd: `ifconfig -a` or `ip addr` or `ip a`
    + Info on interrupts, or CI bus ID, used by each card except IP and MAC addresses
    + If NIC card doesn't work because it shares both an interrupt and memory access address with some other device, check `/proc/interrupts` file to get a listing of all the interrupt IRQs used by the system: `cat /proc/interrupts`
+ Changing Your IP Address
    + cmd: `ifconfig <if> <ip> netmask <mask> up` or `ip addr add <ip>/<mask> dev <if>`
    + config file: `/etc/rc.local`
    + Fedora: `/etc/sysconfig/network-scripts/`
        + Fixed IP Address
            ```script
            #
            # File: ifcfg-eth0
            #
            DEVICE=eth0
            IPADDR=192.168.1.100
            NETMASK=255.255.255.0
            BOOTPROTO=static
            ONBOOT=yes
            #
            # The following settings are optional
            #
            BROADCAST=192.168.1.255
            NETWORK=192.168.1.0
            ```
        + Getting the IP Address Using DHCP
            ```script
            #
            # File: ifcfg-eth0
            #
            DEVICE=eth0
            BOOTPROTO=dhcp
            ONBOOT=yes
            ```
    + activate/deactivate: `ipup <if>` & `ipdown <if>`

### How DHCP Affects the DNS Server You Use

+ DHCP server: IP addr & desired DNS servers
+ `/etc/resolv.conf` commented out servers configuration lines

### Multiple IP Addresses on a Single NIC

+ child interface = IP alias: a virtual sub-interface
+ one of the most common ways of creating multiple IP addresses associated with a single NIC
+ Procedure to create IP alias: subif = `<if>:<#>`
    + Ensure real interface exists
    + Verify no same alias name
    + Create the virtual interface:  
        `ifconfig <subif> <ip> netmask <mask> up` or  
        `ip addr add <ip>/<mask> dev <if> label <subif>`
    + Create a `/etc/sysconfig/network-scripts/ifcfg-<subif>` for permanent setting
        ```
        DEVICE=wlan0:0
        ONBOOT=yes
        BOOTPROTO=static
        IPADDR=192.168.1.99
        NETMASK=255.255.255.0
        ```

### IP Address Assignment for a Direct PPPoE DSL Connection

+ Static IP addresses: config w/ ISP provided IP, netmask, broadcast address, and gateway
+ DHCP or dynamic IP address assignment
    1. Retain PPP authentication over Ethernet (PPPoE) username and password from ISP
    2. Download and install PPPoE RPM
    3. PPPOE configuration creates `ppp0`, a software-based virtual interface
    4. Make a backup copy of your `ifcfg-eth0` file: `cd /etc/sysconfig/network-scripts/; cp ifcfg-eth0 DISABLED.ifcfg-eth0`
    5. Edit `ifcfg-eth0` file to have no IP information and deactivated on boot time
        ```script
        DEVICE=eth0
        ONBOOT=no
        ```
    6. Shutdown your eth0 interface: `ifdown wth0`
    7. Run the `adsl-setup` config script: username, DNS server, password, non-root user, firewall (0-NONE), boot time
+ Some Important Files Created By `adsl-setup`: 
    + created `ifcfg-ppp0` file
        ```script
        USERCTL=yes
        BOOTPROTO=dialup
        NAME=DSLppp0
        DEVICE=ppp0
        TYPE=xDSL
        ONBOOT=yes
        PIDFILE=/var/run/pppoe-adsl.pid
        FIREWALL=NONE
        PING=.
        PPPOE_TIMEOUT=20
        LCP_FAILURE=3
        LCP_INTERVAL=80
        CLAMPMSS=1412
        CONNECT_POLL=6
        CONNECT_TIMEOUT=60
        DEFROUTE=yes 
        SYNCHRONOUS=no
        ETH=eth0
        PROVIDER=DSLppp0
        USER= bigboy-login@isp
        PEERDNS=no
        ```
    + duplicate `/etc/ppp/pap-secrets` and `/etc/ppp/chap-secrets` files with the username and password
+ Simple Troubleshooting
    + `adsl-status`: determine the condition of connection
    + Activate interface: `ifup ppp0`
+ IP Address Assignment for a Cable Modem Connection: use DHCP to get IP addresses

## How to Activate/Shut Down Your NIC

+ activate and deactivate a NIC interface: `ifup <if>` & `ifdown <if>`
+ Corresponding `ifcfg` files for the interfaces in `/etc/sysconfig/network-scripts/` to work

## How to View Current Routing Table

+ Networks with a gateway of `0.0.0.0` usually directly connected to the interface
+ default gateway: a route with a destination of `0.0.0.0`
+ cmds: `netstat -nr`, `route -n`, `ip route`, or `ip r`
+ Examples
    + gateway with `255.255.255.255` usually added on DHCP servers
        ```shell
        Kernel IP routing table
        Destination     Gateway     Genmask         Flags MSS Window irtt Iface
        255.255.255.255 0.0.0.0     255.255.255.255 UH    40  0      0    wlan0 # DNS server
        192.168.1.0     0.0.0.0     255.255.255.0   U     40  0      0    wlan0
        127.0.0.0       0.0.0.0     255.0.0.0       U     40  0      0    lo
        0.0.0.0         192.168.1.1 0.0.0.0         UG    40  0      0    wlan0
        ```
    + multiple gateways handling traffic destined or different networks on different interfaces
        ```shell
        Kernel IP routing table
        Destination   Gateway       Genmask         Flags MSS Window irtt Iface
        ...
        172.16.69.192 0.0.0.0       255.255.255.192 U     40  0      0    eth1  # gateway for 172.16.69.192/26
        172.16.67.128 0.0.0.0       255.255.255.128 U     40  0      0    eth0  # gateway for 172.16.67.128/25
        172.160.0     172.16.67.135 255.255.0.0     UG    40  0      0    eth0  # route for 172.160.0.0/16
        172.16.0.0    172.16.67.131 255.240.0.0     UG    40  0      0    eth0  # route for 172.16.0.0/12
        127.0.0.0     0.0.0.0       255.0.0.0       U     40  0      0    lo    # localhost, loopback
        0.0.0.0       172.16.69.193 0.0.0.0         UG    40  0      0    eth1  # default gateway
        ```

## How to Change Your Default Gateway

+ Temporary Default Gateway Assignment: `route add default gw <ip> <if>` or `ip route add default via <ip> <if>`
+ Permanent Default Gateway Assignment
    + Debian: `/etc/network/interfaces`
    + Fedora: `/etc/sysconfig/network`
        ```script
        NETWORKING=yes
        HOSTNAME=bigboy
        GATEWAY=192.168.1.1
        ```
+ The `/etc/sysconfig/network-scripts/ifcfg-<interface>` file
    + `DEFROUTE` keyword: a default gateway
    + multiple NICs -> risk of inadvertently assigning more than one default gateway
    + Firewalls designed to block packets with irregular sequence numbers and unexpected origins could also obstruct data flow
+ Booting process: `route add` in `/etc/rc.d/rc.local`

## How to Configure Two Gateways

+ Typical scenarios for multiple router/firewalls:
    + default gateway: the router providing access to the Internet
    + the router access corporate network
+ Adding Temporary Static Routes
    + add new routes to server:  
        `route add -net <net> netmask <mask> gw <ip> <if>` or  
        `ip route add <net>/<mask> via <gwip> dev <if>`
    + add a route to an individual server:  
        `route add -host <ip> gw <ip> <if>` or  
        `ip route add <ip> via <gwip> dev <if>`
+ Adding Permanent Static Routes
    + Added on a per interface basis in files located in the `/etc/sysconfig/network-scripts/`
    + Filename format: `route-ifname`, e.g., `route-wlan0` for interface `wlan0`
    + Script example: `10.0.0.0/8 via 192.168.1.254`
    + Verify with `/etc/sysconfig/network-scripts/ifup-routes <if>`

## How to Delete a Route

+ Temporary delete a route:  
    `route del -net <net> netmask <mask> gw <ip> <if>` or  
    `ip route del <net>/<mask> via <gwip> dev <if>`
+ Permanent delete route: delete associated entry from `/etc/sysconfig/network-scripts/route-<if>`

## Changing NIC Speed and Duplex

+ Linux automatically negotiating the speed and duplex by default
+ NICs with failed negotiation usually accompanied by many collision type errors being seen on the NIC when using the `ifconfig -a` command and only marginal performance
+ Using `mii-tool`
    + Many older NICs support only `mii-tool`
    + Cmd: `mii-tool -v <if>`
+ Setting NIC's Speed Parameters with `mii-tool`
    + cmd: `mii-tool -F <opt> <if>`
    + options: 100baseTx-FD, 100baseTx-HD, 10baseT-FD, or 10baseT-HD
+ Display by using `ethtool`: `ethtool <if>`
+ Setting Your NIC's Speed Parameters with `ethtool`
    + permanently set interface config script w/ `ETHTOOL_OPTS` variable
        ```script
        #
        # File: /etc/sysconfig/network-scripts/ifcfg-eth0
        #
        DEVICE=eth0
        IPADDR=192.168.1.100
        NETMASK=255.255.255.0
        BOOTPROTO=static
        ONBOOT=yes
        ETHTOOL_OPTS="speed 100 duplex full autoneg off"
        ```
    + cmd: `ethtool -s <if> [speed 10|100|1000] [duplex full|half [autoneg on|off]`
+ A Note About Duplex Settings
    + Fast Link Pulses (FLP): electronic signals to negotiate speed and duplex settings
    + NIC in auto-negotiation mode but not receiving FLPs
        + set full-duplex to half-duplex
        + set speed to the lowest config value

## How to Convert Your Linux Server into a Simple Router

+ Configuring IP Forwarding
    + Packet forwarding: enables packets to flow through the Linux box from one network to another
    + Activate `net.ipv4.ip_forward` in `/etc/sysctl.conf` with value = 1
    + Enabling packet forwarding only when you reboot at which time Linux will create a file in RAM memory-based /proc filesystem
    + Activte the feature by read `/etc/sysctl.conf`: `sysctl -p`
+ Configuring Proxy ARP
    + Proxy Arp: If there is no suitable router on its network, the server will then send out an ARP request for the MAC address of the remote server. Proxy ARP is configured to answer these types of ARP requests for remote networks
    + Disadvantage: One of the most common problems occurs if two routers are on the network configured for proxy ARP.  Either one will answer the local server's ARP request for the MAC address of the remote server
    + Generally not a good idea to configure proxy ARP on a router but default gateway
    + Some bridging mode firewalls need to have proxy ARP enabled to operate properly
    + Proxy ARP handled by files in the `/proc/sys/net/ipv4/conf/`
    + Activate or disable proxy ARP w/ `/etc/sysctl.conf`
        ```shell
        # File: /etc/sysctl.conf
        
        # Enables Proxy ARP on all interfaces
        net/ipv4/conf/all/proxy_arp   = 1
        
        # Enables Proxy ARP on interfaces eth1 and wlan0
        net/ipv4/conf/eth1/proxy_arp  = 1
        net/ipv4/conf/wlan0/proxy_arp = 1
        ```

## Configuring Your Server as a DNS Client

+ `/etc/resolv.conf` records DNS servers in all Linux distributions
+ DHCP: BOOTPROTO=dhcp directive in the interface configuration file
```script
#
# The /etc/sysconfig/network-scripts/ifcfg-<interface> file
#
DEVICE=p6p1
ONBOOT=yes
IPADDR=192.168.1.100
BOOTPROTO=none
NETMASK=255.255.255.0
TYPE=Ethernet
GATEWAY=192.168.1.1
DNS1=192.168.1.1
DNS2=192.168.1.5
IPV6INIT=no
USERCTL=no
DEFROUTE=yes
```

## Configuring Your `/etc/hosts` File

+ `/etc/hosts`: list of IP addresses and their corresponding server names
+ Server checking the file before referring DNS
+ limited entries: loopback interface, server's own hostname, and DNS server
+ e.g., `192.168.1.101  smallfry  tiny  littleguy`
+ The loopback Interface's localhost Entry
    + Usually the first entry
    + mapped to the name localhost.localdomain and localhost
    + e.g., `127.0.0.1     bigboy    localhost.localdomain    localhost` or `127.0.0.1     bigboy.my-site.com    localhost.localdomain    localhost`

## Debian / Ubuntu Network Configuration

+ The `/etc/network/interfaces` File - divided into stanzas
    + The auto Stanza: interfaces automatically initialized when the system boots up
    + The mapping Stanza: 
        + map configuration parameters for an interface depending on the output of a script
        + e.g., prompt when booting to ask at home or work with the mapping statement to configure IP addr
        + Hotplug configurations assigned on interface with a matching logical interface name
            ```script
            mapping hotplug
                script grep
                map eth0 ether0 # ether0 as logical name
                map eth1        # logical name as the phy name
            ```
    + The iface Stanza
        + the characteristics of a logical interface
        + Typically iface in the 1st line, then logical name, protocol, and type of addressing scheme
        + Protocol: TCP/IP, inet6 for IPv6, ipx, and loopback
        + Protocol characteristics: addresses, subnet masks, and default gateways
            ```script
            # The primary network interface
            auto eth1
            iface eth1 inet static
                    address 216.10.119.240
                    netmask 255.255.255.224
                    network 216.10.119.224
                    broadcast 216.10.119.255
                    gateway 216.10.119.241
                    dns-nameservers 216.10.119.241

            # The secondary network interface
            auto eth0
            iface eth0 inet dhcp
            ``` 
+ Creating Interface Aliases
    + created in the `/etc/network/interfaces`
    + format: `<if>:<sub-if-#>`
    ```script
    auto eth1:1
    iface eth1:1 inet static
        address 216.10.119.239
        netmask 255.255.255.224
    ```
+ Adding Permanent Static Routes
    + Appropriate `iface` stanza in `/etc/network/interfaces` w/ `up` option
    ```script
    # The primary network interface
    auto eth1
    iface eth1 inet static
            ...
            ...
            up route add -net 10.0.0.0 netmask 255.0.0.0 gw 216.10.119.225 eth1
    ```
+ A complete /etc/network/interfaces file
    ```script
    # 
    # Debian / Ubuntu 
    #
    # File: /etc/network/interfaces

    # The loopback network interface
    auto lo
    iface lo inet loopback

    # This is a list of hotpluggable network interfaces.
    # They will be activated automatically by the hotplug subsystem.
    mapping hotplug
            script grep
            map eth0 eth0
            map eth1 eth1

    # The primary network interface
    auto eth1
    iface eth1 inet static
            address 216.10.119.240
            netmask 255.255.255.224
            network 216.10.119.224
            broadcast 216.10.119.255
            gateway 216.10.119.241
            # dns-* options are implemented by the resolvconf package, if installed
            dns-nameservers 216.10.119.241
            wireless-key 98d126d5ac
            wireless-essid schaaffe

            up route add -net 10.0.0.0 netmask 255.0.0.0 gw 216.10.119.225 eth1

    auto eth1:1
    iface eth1:1 inet static
            address 216.10.119.239
            netmask 255.255.255.224

    # The secondary network interface
    auto eth0
    iface eth0 inet dhcp
    ```


