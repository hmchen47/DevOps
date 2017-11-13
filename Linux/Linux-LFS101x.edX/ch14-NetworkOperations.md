Chapter 14: Network Operations
==============================

# Introduction/ Learning Objectives
[videp[]vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Explain basic networking concepts, including types of networks and addressing issues.
+ Configure network interfaces and use basic networking utilities, such as __ifconfig, ip, ping, route__ & __traceroute__.
+ Use graphical and non-graphical browsers, such as __Lynx, w3m, Firefox, Chrome__ and __Epiphany__.
+ Transfer files to and from clients and servers using both graphical and text mode applications, such as __Filezilla, ftp, sftp, curl__ and __wget__.


# Section 1: Network Addresses and DNS
## Introduction to Networking
A network is a group of computers and computing devices connected together through communication channels, such as cables or wireless media. The computers connected over a network may be located in the same geographical area or spread across the world.

A network is used to:

+ Allow the connected devices to communicate with each other
+ Enable multiple users to share devices over the network, such as printers and scanners
+ Share and manage information across computers easily.

Most organizations have both an internal network and an Internet connection for users to communicate with machines and people outside the organization. The Internet is the largest network in the world and is often called "the network of networks".

## IP Addresses
Devices attached to a network must have at least one unique network address identifier known as the __IP (Internet Protocol)__ address. The address is essential for routing __packets__ of information through the network.

Exchanging information across the network requires using streams of small packets, each of which contains a piece of the information going from one machine to another. These packets contain __data buffers__ together with __headers__ which contain information about where the packet is going to and coming from, and where it fits in the sequence of packets that constitute the stream. Networking protocols and software are rather complicated due to the diversity of machines and operating systems they must deal with, as well as the fact that even very old standards must be supported.

## IPv4 and IPv6
There are two different types of __IP addresses__ available: __IPv4__ (version 4) and __IPv6__ (version 6). __IPv4__ is older and by far the more widely used, while __IPv6__ is newer and is designed to get past the limitations of the older standard and furnish many more possible addresses.

__IPv4__ uses 32-bits for addresses; there are only $4.3$ billion unique addresses available. Furthermore, many addresses are allotted and reserved, but not actually used. __IPv4__ is considered inadequate for meeting future needs because the number of devices available on the global network has increased enormously in recent years.

__IPv6__ uses 128-bits for addresses; this allows for $3.4 X 10^38$ unique addresses. If you have a larger network of computers and want to add more, you may want to move to __IPv6__, because it provides more unique addresses. However, it can be complex to migrate to __IPv6__; the two protocols do not always inter-operate well. Thus, moving equipment and addresses to IPv6 requires significant effort and has not been quite as fast as was originally intended. We will discuss __IPv4__ more than __IPv6__ as you are more likely to deal with it.

![image][img1]

## Decoding IPv4 Addresses
A 32-bit IPv4 address is divided into four 8-bit sections called octets.

Example:
```
IP address →        172  .  16  .     31  .    46
Bit format →     10101100.00010000.00011111.00101110
```
(Octet is just another word for __byte__.) 

__Network addresses__ are divided into five classes: A, B, C, D, and E. Classes A, B, and C are classified into two parts: __Network addresses (Net ID)__ and __Host address (Host ID)__. The Net ID is used to identify the network, while the Host ID is used to identify a host in the network. Class D is used for special multicast applications (information is broadcast to multiple computers simultaneously) and Class E is reserved for future use. In this section you will learn about classes A, B, and C.

![image][img2]

## Class A Network Addresses
Class A addresses use the first octet of an IP address as their Net ID and use the other three octets as the __Host ID__. The first bit of the first octet is always set to zero. So you can use only 7-bits for unique network numbers. As a result, there are a maximum of 126 Class A networks available (the addresses 0000000 and 1111111 are reserved). Not surprisingly, this was only feasible when there were very few unique networks with large numbers of hosts. As the use of the Internet expanded, Classes B and C were added in order to accommodate the growing demand for independent networks.

Each Class A network can have up to 16.7 million unique hosts on its network. The range of host address is from 1.0.0.0 to 127.255.255.255.

Note: The value of an octet, or 8-bits, can range from 0 to 255. 

![image][img3]

## Class B Network Addresses
Class B addresses use the first two octets of the IP address as their Net ID and the last two octets as the Host ID. The first two bits of the first octet are always set to binary 10, so there are a maximum of 16,384 (14-bits) Class B networks. The first octet of a Class B address has values from 128 to 191. The introduction of Class B networks expanded the number of networks but it soon became clear that a further level would be needed.

Each Class B network can support a maximum of 65,536 unique hosts on its network. The range of host address is from 128.0.0.0 to 191.255.255.255.

![image][img4]

## Class C Network Addresses
Class C addresses use the first three octets of the IP address as their Net ID and the last octet as their Host ID. The first three bits of the first octet are set to binary 110, so almost 2.1 million (21-bits) Class C networks are available. The first octet of a Class C address has values from 192 to 223. These are most common for smaller networks which don't have many unique hosts.

Each Class C network can support up to 256 (8-bits) unique hosts. The range of host address is from 192.0.0.0 to 223.255.255.255.

![image][img5]

## IP Address Allocation
Typically, a range of IP addresses are requested from your Internet Service Provider (ISP) by your organization's network administrator. Often, your choice of which class of IP address you are given depends on the size of your network and expected growth needs.

You can assign IP addresses to computers over a network manually or dynamically. When you assign IP addresses manually, you add __static__ (never changing) addresses to the network. When you assign IP addresses dynamically (they can change every time you reboot or even more often), the __Dynamic Host Configuration Protocol (DHCP)__ is used to assign IP addresses.

![image][img6]

## Name Resolution
__Name Resolution__ is used to convert numerical IP address values into a human-readable format known as the __hostname__. For example, 140.211.169.4 is the numerical IP address that refers to the __linuxfoundation.org__ hostname. Hostnames are easier to remember. 

Given an IP address, you can obtain its corresponding hostname. Accessing the machine over the network becomes easier when you can type the __hostname__ instead of the IP address.

You can view your system’s hostname simply by typing `hostname` with no argument.

Note: If you give an argument, the system will try to change its hostname to match it, however, only root users can do that.

The special hostname __localhost__ is associated with the IP address `127.0.0.1`, and describes the machine you are currently on (which normally has additional network-related IP addresses).

## Using Domain Name System (DNS) and Name Resolution Tools
__Domain Name System (DNS)__ translates Internet domain and host names to IP addresses.

Click below to view a demonstration on how to use DNS and name resolution tools.

[video][vid1]

Configuration files and commands:

+ `/etc/hosts`: file that associates IP addresses with hostnames, one line per IP address
+ `/etc/resolv.conf`: resolver configuration file contains information that is read by the resolver routines the first time they are invoked by a process. 
+ `host [server]`: convert names to IP addresses and vice versa
+ `nslookup server`: query Internet domain name servers
+ `dig server`: domain information groper, a flexible tool for interrogating DNS name servers.

## Try-It-Yourself: Using Domain Name System (DNS) and Name Resolution Tools
To practice, click the link provided below.

[Using Domain Name System (DNS) and Name Resolution Tools][dns]


# Section 2: Networking Configuration and Tools
## Network Configuration Files
Network configuration files are essential to ensure that interfaces function correctly. They are located in the `/etc` directory tree. However, the exact files used have historically been dependent on the particular Linux distribution and version being used.

For __Debian__ family configurations, the basic network configuration files could be found under `/etc/network/`, while for __Fedora__ and __SUSE__ family systems one needed to inspect `/etc/sysconfig/network`. 

Modern systems emphasize the use of __Network Manager__, which we briefly discussed when we considered graphical system administration, rather than try to keep up with the vagaries of the files in `/etc`. While the graphical versions of __Network Manager__ do look somewhat different in different distributions, the __nmtui__ utility (shown in the screenshot) varies almost not at all, as does the even more sparse __nmcli (command line interface)__ utility. If you are proficient in the use of the GUIs, by all means, use them. If you are working on a variety of systems, the lower level utilities may make life easier.

![image][img7]

## Network Interfaces
Network interfaces are a connection channel between a device and a network. Physically, network interfaces can proceed through a __network interface card (NIC)__, or can be more abstractly implemented as software. You can have multiple network interfaces operating at once. Specific interfaces can be brought up (activated) or brought down (de-activated) at any time.

Information about a particular network interface or all network interfaces can be reported by the __ifconfig__ utility, which you may have to run as the superuser, or at least, give the full path, i.e., `/sbin/ifconfig`, on some distributions. Similar information can be obtained with __`ip`__, a newer utility with far more capabilities, but uglier output for humans. Some new Linux distributions do not install the older __net-tools__ package to which __ifconfig__ belongs and you may have to install it to use it.

## The ip Utility
To view the IP address:
```
$ /sbin/ip addr show
```
To view the routing information:
```
$ /sbin/ip route show
```
__ip__ is a very powerful program that can do many things. Older (and more specific) utilities such as __ifconfig__ and __route__ are often used to accomplish similar tasks. A look at the relevant man pages can tell you much more about these utilities.

## ping
__ping__ is used to check whether or not a machine attached to the network can receive and send data; i.e., it confirms that the remote host is online and is responding.

To check the status of the remote host, at the command prompt, type `ping <hostname>`.

ping is frequently used for network testing and management; however, its usage can increase network load unacceptably. Hence, you can abort the execution of ping by typing `CTRL-C`, or by using the `-c` option, which limits the number of packets that ping will send before it quits. When execution stops, a summary is displayed.

## route
A network requires the connection of many nodes. Data moves from source to destination by passing through a series of routers and potentially across multiple networks. Servers maintain __routing tables__ containing the addresses of each node in the network. The __IP Routing protocols__ enable routers to build up a forwarding table that correlates final destinations with the next hop addresses.

One can use the route utility or the newer `ip route` command to view or change the IP routing table to add, delete, or modify specific (static) routes to specific hosts or networks. The table explains some commands that can be used to manage IP routing:

| Task | Command |
|------|---------|
| Show current routing table | $ `route –n` or `ip route` |
| Add static route | $ `route add -net address` or `ip route add`  |
| Delete static route | $ `route del -net address` or `ip route del` |

## traceroute
__traceroute__ is used to inspect the route which the data packet takes to reach the destination host, which makes it quite useful for troubleshooting network delays and errors. By using __traceroute__, you can isolate connectivity issues between hops, which helps resolve them faster.

To print the route taken by the packet to reach the network host, at the command prompt, type `traceroute <address>`.

## Try-It-Yourself: Using ping, route, and traceroute
To practice, click the link provided below.

[Using ping, route, and traceroute][prtr]

## More Networking Tools
Now, let’s learn about some additional networking tools. Networking tools are very useful for monitoring and debugging network problems, such as network connectivity and network traffic.

| Networking Tools | Description |
|------------------|-------------|
| `ethtool` | Queries network interfaces and can also set various parameters such as the speed. |
| `netstat` | Displays all active connections and routing tables. Useful for monitoring performance and troubleshooting. |
| `nmap` | Scans open ports on a network. Important for security analysis |
| `tcpdump` | Dumps network traffic for analysis. |
| `iptraf` | Monitors network traffic in text mode. |
| `mtr` | Combines functionality of ping and traceroute and gives a continuously updated display. |
| `dig` | Tests DNS workings. A good replacement for host and nslookup. |

[video][vid2]

## Try-It-Yourself: Using Network Tools
To practice, click the link provided below.

[Using ethtool and netstat][ethn]

## Knowledge Check
1. How would you change your system's hostname to LFstudent?

        Explanation
        sudo hostname LFstudent will change the hostname. Note one has to use sudo.

2. Which command checks whether a host is online?

        A. ping 
        B. route
        C. traceroute
        D. netstat

        Ans: A
        Explanation
        The ping command checks whether a host is online.

# Section 3: Browsers
## Graphical and Non-Graphical Browsers
Browsers are used to retrieve, transmit, and explore information resources, usually on the World Wide Web. Linux users commonly use both graphical and non-graphical browser applications.

The common graphical browsers used in Linux are:

+ Firefox
+ Google Chrome
+ Chromium
+ Epiphany
+ Opera.

Sometimes, you either do not have a graphical environment to work in (or have reasons not to use it) but still need to access web resources. In such a case, you can use non-graphical browsers, such as the following:

| Non-Graphical Browsers | Description |
|------------------------|-------------|
| `lynx` | Configurable text-based web browser; the earliest such browser and still in use. |
| `links` or `elinks` | Based on lynx. It can display tables and frames. |
| `w3m` | Another text-based web browser with many features. |

## wget
Sometimes, you need to download files and information, but a browser is not the best choice, either because you want to download multiple files and/or directories, or you want to perform the action from a command line or a script. __wget__ is a command line utility that can capably handle the following types of downloads:

+ Large file downloads
+ Recursive downloads, where a web page refers to other web pages and all are downloaded at once
+ Password-required downloads
+ Multiple file downloads.

To download a webpage, you can simply type `wget <url>`, and then you can read the downloaded page as a local file using a graphical or non-graphical browser.

![image][img8]

## curl
Besides downloading, you may want to obtain information about a URL, such as the source code being used. __curl__ can be used from the command line or a script to read such information. __curl__ also allows you to save the contents of a web page to a file, as does wget.

You can read a URL using `curl <URL>`. For example, if you want to read `http://www.linuxfoundation.org` , type `curl http://www.linuxfoundation.org`.

To get the contents of a web page and store it to a file, type `curl -o saved.html http://www.mysite.com`. The contents of the main index file at the website will be saved in saved.html.

## Try-It-Yourself: Using wget and curl
To practice, click the link provided below.

[Using wget and curl][wget]

## Knowledge Check
1. Which of the following are graphical browsers used in Linux?

        A. lynx
        B. Mozilla Firefox 
        C. konqueror 
        D. Google Chrome 

        Ans: B, C, D
        Explanation
        Mozilla FireFox, konqueror and Google Chrome are graphical browsers used in Linux.

2. Which of the following are command line utilities that can be used to download webpages?

        A. wget 
        B. ssh
        C. curl 
        D. Epiphany

        Ans: A, C
        Explanation
        curl and wget are command line utilities that can be used to download webpages.


# Section 4: Transferring Files
## FTP (File Transfer Protocol)
When you are connected to a network, you may need to transfer files from one machine to another. __File Transfer Protocol (FTP)__ is a well-known and popular method for transferring files between computers using the Internet. This method is built on a client-server model. FTP can be used within a browser or with stand-alone client programs.

FTP is one of the oldest methods of network data transfer, dating back to the early 1970s.  As such, it is considered inadequate for modern needs, as well as being intrinsically insecure. However, it is still in very widespread use and when security is not a concern (such as with so-called __anonymous FTP__) it still makes sense.

## FTP Clients
__FTP clients__ enable you to transfer files with remote computers using the FTP protocol. These clients can be either graphical or command line tools. Filezilla, for example, allows use of the drag-and-drop approach to transfer files between hosts. All web browsers support FTP, all you have to do is give a URL like : `ftp://ftp.kernel.org` where the usual `http://` becomes `ftp://`.

Some command line FTP clients are:

+ ftp
+ sftp
+ ncftp
+ yafc (Yet Another FTP Client).

FTP has fallen into disfavor on modern systems, as it is intrinsically insecure, since passwords are user credentials that can be transmitted without encryption and are thus prone to interception. Thus, ftp.kenel.org has recently been slated for removal in favor of use of `rsync` and web browser `https` access for example. As an alternative, __sftp__ is a very secure mode of connection, which uses the __Secure Shell (ssh)__ protocol, which we will discuss shortly. __sftp__ encrypts its data and thus sensitive information is transmitted more securely. However, it does not work with so-called anonymous FTP (guest user credentials).

## Connecting to an FTP server
Click below to view a demonstration on how to connect to an FTP server using command line ftp client.

[video][vid3]

## Try-It-Yourself: Connecting to an FTP server
To practice, click the link provided below.

[Connecting to an FTP server][ftp]

## SSH: Executing Commands Remotely
__Secure Shell (SSH)__ is a cryptographic network protocol used for secure data communication. It is also used for remote services and other secure services between two devices on the network and is very useful for administering systems which are not easily available to physically work on, but to which you have remote access.

To login to a remote system using your same user name you can just type `ssh some_system` and press Enter. ssh then prompts you for the remote password.  You can also configure ssh to securely allow your remote access without typing a password each time.

If you want to run as another user, you can do either `ssh -l someone some_system` or `ssh someone@some_system`. To run a command on a remote system via __SSH__, at the command prompt, you can type  `ssh some_system my_command`.  

![image][img9]

## Copying Files Securely with scp
![image][imga]

We can also move files securely using __Secure Copy (scp)__ between two networked hosts. scp uses the SSH protocol for transferring data.

To copy a local file to a remote system, at the command prompt, type `scp <localfile> <user@remotesystem>:/home/user/` and press Enter.

You will receive a prompt for the remote password. You can also configure scp so that it does not prompt for a password for each transfer.

## Knowledge Check
1. Why is FTP use no longer considered up to modern standards? Pick all answers that apply.

        A. It transmits unencrypted passwords which can be intercepted. 
        B. It uses TCP/IP as a transmission protocol.
        C. It does not work with many operating systems.
        D. It is more than 40 years old and contains a lot of historical baggage. 

        Ans: A, D
        Explanation
        FTP is insecure because it uses unencrypted passwords, and it is very old and full of ancient baggage.

2. Which of the following are valid commands to use with ssh?

        A. ssh -l haskell eddie.com 
        B. ssh root@eddie.com yum -y update 
        C. ssh -l haskell@eddie.com whoami
        D. ssh -l haskell eddie.com whoami 

        Ans:  A, B, D
        Explanation
        Users and target addresses can be specified in a number of ways with ssh.

## Lab 1: Network Troubleshooting
Troubleshooting network problems is something that you will often encounter if you haven't already. We are going to practice some of the previously discussed tools, that can help you isolate, troubleshoot and fix problems in your network.

The Solution file contains a step-by-step procedure for exercising many of the tools we have studied. Please repeat the steps, substituting your actual network interface names, alternative network addresses and web sites, etc.

Click [the link][lab1] to view a solution to the Lab exercise.

Solution:
```
Troubleshooting network problems is something that you will often encounter if you haven't already. We are going to practice some of the previously discussed tools, that can help you isolate, troubleshoot and fix problems in your network.

Suppose you need to perform an Internet search, but your web browser can not find google.com, saying the host is unknown. Let's proceed step by step to fix this.

First make certain your network is properly configured. If your Ethernet device is up and running, running ifconfig should display something like:
student:/tmp> /sbin/ifconfig
 eno167777 Link encap:Ethernet  HWaddr 00:0C:29:BB:92:C2
          inet addr:192.168.1.14  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:febb:92c2/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3244 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2006 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:4343606 (4.1 Mb)  TX bytes:169082 (165.1 Kb)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b) 
On older systems you probably will see a less cryptic name than eno167777, like eth0, or for a wireless connection, you might see something like wlan0 or wlp3s0. You can also show your IP address with:
student:/tmp> ip addr show
 1: lo:  mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eno16777736:  mtu 1500 qdisc pfifo_fast state \
    UP group default qlen 1000
    link/ether 00:0c:29:bb:92:c2 brd ff:ff:ff:ff:ff:ff
p    inet 192.168.1.14/24 brd 192.168.1.255 scope global dynamic eno16777736
       valid_lft 84941sec preferred_lft 84941sec
    inet 192.168.1.15/24 brd 192.168.1.255 scope global secondary dynamic eno16777736
       valid_lft 85909sec preferred_lft 85909sec
    inet6 fe80::20c:29ff:febb:92c2/64 scope link
       valid_lft forever preferred_lft forever
      
Does the IP address look valid? Depending on where you are using this from, it is most likely a Class C IP address; in the above this is 192.168.1.14
If it does not show a device with an IP address, you may need to start or restart the network and/or NetworkManager. Exactly how you do this depends on your system. For most distributions one of these commands will accomplish this:

student:/tmp> sudo systemctl restart NetworkManager
student:/tmp> sudo systemctl restart network
student:/tmp> sudo service NetworkManager restart
student:/tmp> sudo service network restart
      
If your device was up but had no IP address, the above should have helped fix it, but you can try to get a fresh address with:
student:/tmp> sudo dhclient eth0
      
substituting the right name for the Ethernet device.
If your interface is up and running with an assigned IP address and you still can not reach google.com, we should make sure you have a valid hostname assigned to your machine, with hostname:
student:/tmp> hostname
 openSUSE
      
It is rare you would have a problem here, as there is probably always at least a default hostname, such as localhost.
When you type in a name of a site such as google.com, that name needs to be connected to a known IP address. This is usually done employing the DNS sever (Domain Name System)
First, see if the site is up and reachable with ping:

student:/tmp> sudo ping -c 3 google.com
PING google.com (216.58.216.238) 56(84) bytes of data.
64 bytes from ord31s22-in-f14.1e100.net (216.58.216.238): icmp_seq=1 ttl=51 time=21.7 ms
64 bytes from ord31s22-in-f14.1e100.net (216.58.216.238): icmp_seq=2 ttl=51 time=23.8 ms
64 bytes from ord31s22-in-f14.1e100.net (216.58.216.238): icmp_seq=3 ttl=51 time=21.3 ms

--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
rtt min/avg/max/mdev = 21.388/22.331/23.813/1.074 ms
      
Note:
We have used sudo for ping; recent Linux distributions have required this to avoid clueless or malicious users from flooding systems with such queries.
We have used -c 3 to limit to 3 packets; otherwise ping would run forever until forcibly terminated, say with CTRL-C.
If the result was:
 ping: unknown host google.com
      
It is likely that something is wrong with your DNS set-up. (Note on some systems you will never see the unknown host message, but you will get a suspicious result like:
student:/tmp> sudo ping l89xl28vkjs.com
 PING l89xl28vkjs.com.site (127.0.53.53) 56(84) bytes of data.
64 bytes from 127.0.53.53: icmp_seq=1 ttl=64 time=0.016 ms
...
      
where the 127.0.x.x address is a loop feeding back to the host machine you are on. You can eliminate this as being a valid address by doing:
student:/tmp> host l89xl28vkjs.com
Host l89xl28vkjs.com not found: 3(NXDOMAIN)
      
whereas a correct result would look like:
student:/tmp> host google.com
 google.com has address 216.58.216.206
google.com has IPv6 address 2607:f8b0:4009:80b::200e
google.com mail is handled by 20 alt1.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
google.com mail is handled by 30 alt2.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
      
The above command utilizes the DNS server configured in /etc/resolv.conf on your machine. If you wanted to override that you could do:
host 8.8.8.8
 8.8.8.8.in-addr.arpa domain name pointer google-public-dns-a.google.com.
student@linux:~> host google.com 8.8.8.8
Using domain server:
Name: 8.8.8.8
Address: 8.8.8.8#53
Aliases:

google.com has address 216.58.216.110
google.com has IPv6 address 2607:f8b0:4009:804::1002
...\
      
where we have used the publicly available DNS server provided by Google itself. (Using this or another public server can be a good trick sometimes if your network is up but DNS is ill; in that case you can also enter it in resolv.conf.)
Note that there is another file, /etc/hosts, where you can associate names with IP addresses, which is used before the DNS server is consulted. This is most useful for specifying nodes on your local network.

You could also use the dig utility if you prefer:

student:/tmp> dig google.com
; <<>> DiG 9.9.5-rpz2+rl.14038.05-P1 <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29613
;; flags: qr rd ra; QUERY: 1, ANSWER: 11, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 1c20 , udp: 1280
;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             244     IN      A       173.194.46.67
google.com.             244     IN      A       173.194.46.65
google.com.             244     IN      A       173.194.46.71
google.com.             244     IN      A       173.194.46.73
google.com.             244     IN      A       173.194.46.69
google.com.             244     IN      A       173.194.46.68
google.com.             244     IN      A       173.194.46.64
google.com.             244     IN      A       173.194.46.72
google.com.             244     IN      A       173.194.46.70
google.com.             244     IN      A       173.194.46.66
google.com.             244     IN      A       173.194.46.78

;; Query time: 22 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Mon Apr 20 08:58:58 CDT 2015
;; MSG SIZE  rcvd: 215
      
Suppose host or dig fail to connect the name to an IP address. There are many reasons DNS can fail, some of which are:
The DNS server is down. In this case try pinging it to see if it is alive (you should have the IP address in /etc/resolv.conf.
The server can be up and running, but DNS may not be currently available on the machine.
Your route to the DNS server may not be correct.
How can we test the route? Tracing the route to one of the public name server we mentioned before:
student@linux:~> sudo traceroute 8.8.8.8
 traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  192.168.1.1 (192.168.1.1)  0.405 ms  0.494 ms  0.556 ms
 2  10.132.4.1 (10.132.4.1)  15.127 ms  15.107 ms  15.185 ms
 3  dtr02ftbgwi-tge-0-6-0-3.ftbg.wi.charter.com (96.34.24.122)
                                                          15.243 ms  15.327 ms  17.878 ms
 4  crr02ftbgwi-bue-3.ftbg.wi.charter.com (96.34.18.116)  17.667 ms  17.734 ms  20.016 ms
 5  crr01ftbgwi-bue-4.ftbg.wi.charter.com (96.34.18.108)  22.017 ms  22.359 ms  22.052 ms
 6  crr01euclwi-bue-1.eucl.wi.charter.com (96.34.16.77)  29.430 ms  22.705 ms  22.076 ms
 7  bbr01euclwi-bue-4.eucl.wi.charter.com (96.34.2.4)  17.795 ms  25.542 ms  25.600 ms
 8  bbr02euclwi-bue-5.eucl.wi.charter.com (96.34.0.7)  28.227 ms  28.270 ms  28.303 ms
 9  bbr01chcgil-bue-1.chcg.il.charter.com (96.34.0.9)  33.114 ms  33.072 ms  33.175 ms
10  prr01chcgil-bue-2.chcg.il.charter.com (96.34.3.9)  36.882 ms  36.794 ms  36.895 ms
11  96-34-152-30.static.unas.mo.charter.com (96.34.152.30)  42.585 ms  42.326 ms  42.401 ms
12  216.239.43.111 (216.239.43.111)  28.737 ms 216.239.43.113 (216.239.43.113)
                                                            24.558 ms  23.941 ms
13  209.85.243.115 (209.85.243.115)  24.269 ms 209.85.247.17 (209.85.247.17)
   25.758 ms 216.239.50.123 (216.239.50.123)  25.433 ms
14  google-public-dns-a.google.com (8.8.8.8)  25.239 ms  24.003 ms  23.795 ms
      
Again, this should likely work for you, but what if you only got the first line in the traceroute output?
If this happened, most likely your default route is wrong. Try:

student:/tmp> ip route show
efault via 192.168.1.1 dev eno16777736  proto static  metric 1024
192.168.1.0/24 dev eno16777736  proto kernel  scope link  src 192.168.1.14
      
Most likely this is set to your network interface and the IP address of your router, DSL, or Cable Modem. Let's say that it is blank or simply points to your own machine. Here's your problem! At this point, you would need to add a proper default route and run some of the same tests we just did.
Note, an enhanced version of traceroute is supplied by mtr, which runs continuously (like top). Running it with the --report-cycles option to limit how long it runs:

student:/tmp> sudo mtr --report-cycles 3 8.8.8.8
                             My traceroute  [v0.85]
c7 (0.0.0.0)                                           Mon Apr 20 09:30:41 2015
Unable to allocate IPv6 socket for nameserver communication: Address family not supported
              by protocol                  Packets               Pings
 Host                                Loss%   Snt   Last   Avg  Best  Wrst StDev
                                      0.0%     3    0.3   0.3   0.2   0.3   0.0
 2. 10.132.4.1                        0.0%     3    6.3   7.1   6.3   8.4   0.7
 3. dtr02ftbgwi-tge-0-6-0-3.ftbg.wi.  0.0%     3    6.2   7.5   6.2  10.0   2.1
 4. dtr01ftbgwi-bue-1.ftbg.wi.charte  0.0%     3    8.9   8.5   6.2  10.4   2.0
 5. crr01ftbgwi-bue-4.ftbg.wi.charte  0.0%     3    8.9   9.7   8.9  10.4   0.0
 6. crr01euclwi-bue-1.eucl.wi.charte  0.0%     3   16.5  17.4  14.2  21.5   3.7
 7. bbr01euclwi-bue-4.eucl.wi.charte  0.0%     3   23.5  22.0  18.2  24.2   3.2
 8. bbr02euclwi-bue-5.eucl.wi.charte  0.0%     3   18.9  22.7  18.1  31.1   7.2
 9. bbr01chcgil-bue-1.chcg.il.charte  0.0%     3   22.9  23.0  22.9  23.1   0.0
10. prr01chcgil-bue-2.chcg.il.charte  0.0%     3   21.4  24.1  20.8  30.2   5.2
11. 96-34-152-30.static.unas.mo.char  0.0%     3   22.6  21.9  20.0  23.3   1.6
12. 216.239.43.111                    0.0%     3   21.2  21.7  21.2  22.0   0.0
13. 72.14.237.35                      0.0%     3   21.2  21.0  19.8  21.9   1.0
14. google-public-dns-a.google.com    0.0%     3   26.7  23.0  21.0  26.7   3.2
      
Hopefully, running through some of these commands helped. It actually helps to see what the correct output for your system looks like. Practice using these commands; it is very likely that you will need them someday.
```

## Lab 2: Non-graphical Browsers
There are times when a graphical browser is not available, but you need to look up or download a resource. In this exercise, we are going to experiment with using non-graphical web browsers. 

The Solution file contains a step-by-step procedure for exercising the tools discussed. Please repeat the steps, substituting web sites, etc.

Click [the link][lab2] to view a solution to the Lab exercise.

Solution:
```
We have discussed non-graphical browsers:

+ lynx
+ links and elinks
+ w3m

There are times when you will not have a graphical window interface running on your Linux machine and you need to look something up on the web or download a driver (like a graphics driver in order to bring up a graphical window interface). So, it is a good idea to practice using a non-graphical web browser to do some work.
With links, you can use your mouse to click on the top line of the screen to get a menu. In this case, we want to go to google.com (or your favorite search engine), so you can just type g to go to a typed-in URL.

Pressing the TAB key will move your cursor to the OK button. You can then press the ENTER key.

You should now be at google.com (or your favorite search engine). Use the down-arrow key to move through the choices until you reach the blank line used to enter your search query. Now type Intel Linux graphics drivers in the search box. Use the down-arrow key to move you to the Google Search button. With that highlighted, press the ENTER key.

Use your down-arrow key to move to the entry: Intel(R) Graphics Drivers for Linux - Download Center. It may take several presses of the down-arrow key. You can press the space-bar to move down the page or the â€˜bâ€™ key to move back up the page if needed. Once this line is highlighted, press the ENTER key. You will now go to the Intel Graphics Driver for Linux page. If you want, you can read the page. Remember, the space-bar will page you down the page while the â€˜bâ€™ key will move you back up the page. The Page Down and Page Up keys will do the same thing if you prefer. Find the URL under the line

URL Location:
      
Position your cursor at this line using the up-arrow or down-arrow key. Press the ENTER key to go to this location.
Page down this page until you see the line:

Latest Releases
      
If you move your cursor with the arrow keys, find the latest version (with the most recent release date) under this section. If using your arrow-keys, you should highlight Release Notes. Press the ENTER key.
This has installers for versions of Ubuntu and Fedora, along with the source code. You will need to page down a page or two depending on the size of your screen.

Select one of the installers, perhaps for the version of Linux that you are running, or just a random one, and press the ENTER key.

You should see a text dialog box with choices of what to do. Save the package wherever you want to.

You can now quit your non-graphical browser. If you used links, then click on the top line of the screen, select the File drop-down menu item, and click on Exit. Confirm that you really want to exit Links. You should now see your shell prompt.
```

# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ The __IP (Internet Protocol)__ address is a unique logical network address that is assigned to a device on a network.
+ __IPv4__ uses 32-bits for addresses and __IPv6__ uses 128-bits for addresses.
+ Every IP address contains both a network and a host address field.
+ There are five classes of network addresses available: A, B, C, D & E.
+ __DNS (Domain Name System)__ is used for converting Internet domain and host names to IP addresses.
+ The `ifconfig` program is used to display current active network interfaces.
+ The commands `ip addr show` and `ip route show` can be used to view IP address and routing information.
+ You can use `ping` to check if the remote host is alive and responding.
+ You can use the `route` utility program to manage IP routing.
+ You can monitor and debug network problems using networking tools.
+ __Firefox, Google Chrome, Chromium__, and __Epiphany__ are the main graphical browsers used in Linux.
+ Non-graphical or text browsers used in Linux are __Lynx, Links__, and __w3m__.
+ You can use `wget` to download webpages.
+ You can use `curl` to obtain information about URLs.
+ __FTP (File Transfer Protocol)__ is used to transfer files over a network.
+ `ftp`, `sftp`, `ncftp`, and `yafc` are command line FTP clients used in Linux.
+ You can use `ssh` to run commands on remote systems.




[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009300_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003100_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004400_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005400_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fa98328f7ff2e180a79cead9ee3e433f/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch11_screen05.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/610943ad6bb219df591ec8659288e630/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch11_screen06.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1867a1e02d2827251e50b65a03bcaa1b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch11_screen07.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7e40d0c228a2ac28dd4e1e9af18ba3ce/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch11_screen08.jpg
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/376a6fe8144e0d5799f331a803e1d33d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch11_screen09.jpg
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/303c5dc5b32edde05f599cac40512b7d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch11_screen10a.jpg
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/30ad387df9ee4d04b71b8a402855df8c/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/nmtui.png
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f9257ce80f059db96201deb30d8ac8b1/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/wgethrel7.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b19e7547d1f707f6ba4b134c31f43a31/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch11_screen37.jpg
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/83970c9d6a9a9462fe7463ada6b79e45/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch11_screen38.jpg

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-network.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-browsers.html

[dns]: https://learningmate.s3-us-west-2.amazonaws.com/LFS01/Chapter11/screen14/index.html
[prtr]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingping/index.html
[ethn]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingethtool/index.html
[wget]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingwgetcurl/index.html
[ftp]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingftp/index.html
