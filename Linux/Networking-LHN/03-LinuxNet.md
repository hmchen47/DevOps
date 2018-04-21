# Ch03 : Linux Networking

## How to Configure Your NIC's IP Address

+ Determining Your IP Address: 
    + cmd: `ifconfig -a` or `ip addr` or `ip a`
    + Info on interrupts, or CI bus ID, used by each card except IP and MAC addresses
    + If NIC card doesn't work because it shares both an interrupt and memory access address with some other device, check /proc/interrupts file to get a listing of all the interrupt IRQs used by the system: `cat /proc/interrupts`
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

### Multiple IP Addresses on a Single NIC

### IP Address Assignment for a Direct PPPoE DSL Connection

+ Some Important Files Created By adsl-setup

+ Simple Troubleshooting

### IP Address Assignment for a Cable Modem Connection

## How to Activate/Shut Down Your NIC

## How to View Your Current Routing Table

## How to Change Your Default Gateway

### Temporary Default Gateway Assignment

### Permanent Default Gateway Assignment

+ The /etc/sysconfig/network file

+ The /etc/sysconfig/network-scripts/ifcfg-<interface> file

## How to Configure Two Gateways

### Adding Temporary Static Routes

### Adding Permanent Static Routes

## How to Delete a Route

## Changing NIC Speed and Duplex

### Using mii-tool

+ Setting Your NIC's Speed Parameters with mii-tool

### Using ethtool

+ Setting Your NIC's Speed Parameters with ethtool

+ A Note About Duplex Settings

## How to Convert Your Linux Server into a Simple Router

### Configuring IP Forwarding

### Configuring Proxy ARP

## Configuring Your Server as a DNS Client

## Configuring Your /etc/hosts File

### The loopback Interface's localhost Entry

## Debian / Ubuntu Network Configuration

### The /etc/network/interfaces File

+ The auto Stanza

+ The mapping Stanza

+ The iface Stanza

+ Creating Interface Aliases

+ Adding Permanent Static Routes

+ A complete /etc/network/interfaces file	


