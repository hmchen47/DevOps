# Linux Command Reference Cards

## General

| Command | Description | Link |
|---------|-------------|------|
| `whois [ip | fqdn]` | administrative info | [Identification](../Linux/Networking-LHN/04-SimpleNetTrbl.md#determining-the-source-of-an-attack) |
| `last [-num]` | a listing of last logged in users | [Identification](../Linux/Networking-LHN/04-SimpleNetTrbl.md#who-has-used-my-system) |
| `who` | who currently logged in | [Identification](../Linux/Networking-LHN/04-SimpleNetTrbl.md#who-has-used-my-system) |
| `grep [opt] <str> [file...]` | print lines matching a pattern; option: e=pattern(greexp), f=FILE | [View New Log Entries](../Linux/Networking-LHN/05-TrblSyslog.md#how-to-view-new-log-entries-as-they-happen) |
| `tar -[cxvfz] <file>` | archive/extract files; c=create, x=extract, v=verbose, f=filename, z=compress | [tar Files](../Linux/Networking-LHN/06-SWInstall.md#installing-software-using-tar-files) |

## System

| Command | Description | Link |
|---------|-------------|------|
| `chkconfig` | used to activate and deactivate services | [chkconfig](https://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-services-chkconfig.html) |
| `chkconfig --list` | Displayed all services and their current start-up status in each run-level configuration | [List RPMs](../Linux/Networking-LHN/06-SWInstall.md#how-to-list-installed-rpms) |
| `chkconfig <pkg> {on|off}` | Enable/disable at boot time w/ `syscinit` | [Auto `yum`](../Linux/Networking-LHN/06-SWInstall.md#automatic-updates-with-yum) |
| `systemctl {enable|disable} <daemon>.service` | Enable/Disable at boot time w/ `systemd` | [Auto `yum`](../Linux/Networking-LHN/06-SWInstall.md#automatic-updates-with-yum) |
| `service <daemon> {start|stop}` | Start/Stop a daemon w/ `sysvinit` | [Auto `yum`](../Linux/Networking-LHN/06-SWInstall.md#automatic-updates-with-yum) |
| `systemctl {start|stop} <daemon>.service` | Start/stop a daemon w/ `systemd` | [Auto `yum`](../Linux/Networking-LHN/06-SWInstall.md#automatic-updates-with-yum) |
| `update-rc.d` | view and configure which DEBs will start at boot time | [DEB Installation](../Linux/Networking-LHN/06-SWInstall.md#installing-software-from-deb-files) |



## Hardware 

| Command | Description | Link |
|---------|-------------|------|
| `mount /mnt/<dev>` | Mount device to /mnt/ | [CD-ROMs or DVDs](../Linux/Networking-LHN/06-SWInstall.md#how-to-install-rpms-manually) |
| `eject cdrom` | unmount CDROM | [CD-ROMs or DVDs](../Linux/Networking-LHN/06-SWInstall.md#how-to-install-rpms-manually) |
| `umount /mnt` | unmount device | [CD-ROMs or DVDs](../Linux/Networking-LHN/06-SWInstall.md#how-to-install-rpms-manually) |


## Networking

### Configuration

| Command | Description | Link |
|---------|-------------|------|
| `ifconfig <if> <ip> netmask <mask> up` | configure IP address of an interface; `<if:x>`=sub-interface=virtual interface | [Configure IP Address](../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-your-nics-ip-address) |
| `ip addr add <ip>/<mask> dev <if>` | configure IP address of an interface; `<if:x>`=sub-interface=virtual interface | [Configure IP Address](../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-your-nics-ip-address) |
| `ipup <if>` & `ipdown <if>` | Activate & deactivate interface | [Configure IP Address](../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-your-nics-ip-address) |
| `route add default gw <ip> <if>` | Config default gateway | (../Linux/Networking-LHN/03-LinuxNet.md#how-to-change-your-default-gateway) |
| `ip route add default via <ip> <if>` | Config default gateway | (../Linux/Networking-LHN/03-LinuxNet.md#how-to-change-your-default-gateway) |
| `route add -net <net> netmask <mask> gw <ip> <if>` | Add route | [Configure Gateways](../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-two-gGateways) |
| `ip route add <net>/<mask> via <gwip> dev <if>` | Add route | [Configure Gateways](../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-two-gGateways) |
| `route add -host <ip> gw <ip> <if>` | add a route to an individual server | [Add Routes](../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-two-gGateways) |
| `ip route add <ip> via <gwip> dev <if>` | add a route to an individual server | [Add Routes](../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-two-gGateways) |
| `route del -net <net> netmask <mask> gw <ip> <if>` | [Delete Routes] | [Delete Route](../Linux/Networking-LHN/03-LinuxNet.md#how-to-delete-a-route) |
| `ip route del <net>/<mask> via <gwip> dev <if>` | [Delete Routes] | [Delete Route](../Linux/Networking-LHN/03-LinuxNet.md#how-to-delete-a-route) |
| `mii-tool -F <opt> <if>` | Configure NIC's Speed Parameters | [NIC Speed & Duplex](../Linux/Networking-LHN/03-LinuxNet.md#changing-nic-speed-and-duplex) |
| `ethtool -s <if> [speed 10|100|1000] [duplex full|half [autoneg on|off]` | | Configure NIC's Speed Parameters | [NIC Speed & Duplex](../Linux/Networking-LHN/03-LinuxNet.md#changing-nic-speed-and-duplex) |

### Troubleshooting

| Command | Description | Link |
|---------|-------------|------|
| `ifconfig -a` | list all interfaces; up/down interfaces; NIC errors; MAC & IP addresses | [Testing NIC](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic); [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors); [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess) |
| `ip addr`; `ip a` | list all interfaces; up/down interfaces; MAC & IP addresses | [Testing NIC](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic); [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess)  |
| `mii-tool -v <if>` | Link status output (older version) | [Testing Link Status](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic) |
| `ethtool <if>` |  Link status output (newer version) | [Testing Link Status](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic) |
| `ip -s a`; `ip -s link` | NIC error output | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors) |
| `ethtoll -S` | NIC error output - detailed report | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors) |
| `arp -a` | MAC address of ARP table | [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess) |
| `ping -c <num> <ip/fqdn>` | limit ping counts | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-ping-to-test-network-connectivity) |
| `telnet <ip> <port>` | Connectivity test; remote session; default: TCP port 23 | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-telnet-to-test-network-connectivity) |
| `curl -I <fqdn>` | text based web browser; display web page header and status code | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-web-sites-with-the-curl-and-wget-utilities) |
| `wget -N <fqdn>` | recursively download web pages w/o timestamps | | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-web-sites-with-the-curl-and-wget-utilities) |
| `netstat -<opt>` | network connections, routing tables, interface statistics, masquerade connections, and multicast memberships; opt: a=all, l=listening, i=interface, r=route, v=verbose, t=tcp, u=udp, p=pid, n=numeric, s=statistics | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors); [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#the-netstat-command) |
| `ss -<opt>` | network connections, routing tables, interface statistics, masquerade connections, and multicast memberships; opt: l=listening, r=resolve, v=verbose, t=tcp, u=udp, p=process, w=RAW socket, s=summary | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#the-netstat-command) |
| `traceroute <ip>` | route packets trace to network host | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-traceroute-to-test-connectivity) |
| `mtr <ip>` | repeat `traceroute` in real time | [Congestion](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-mtr-to-detect-network-congestion) |
| `tcpdump -<opt> [<expr>]` | viewing the flow of packets through NIC; __opt__: c=count, i=interface, w=dump file, C=file size, t=no timestamp, n=no DNS; __expr__: host,icmp, tcp, udp, port | [Packet Flow](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-packet-flows-with-tcpdump) |
| `tshark -<opt> [<expr>]` | Fedora Linux Wireshark RPM | [Packet Flow](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-packet-flows-with-tshark) |
| `nslookup <fqdn> | <ip>` | used to get associated IP addr for given domain and vice versa | [DNS](../Linux/Networking-LHN/04-SimpleNetTrbl.md#basic-dns-troubleshooting) |
| `host <fqdn> | <ip>` | newer cmd used to get associated IP addr for given domain and vice versa | [DNS](../Linux/Networking-LHN/04-SimpleNetTrbl.md#basic-dns-troubleshooting) |
| `nmap <-opt>` | determine all the TCP/IP ports on which a remote server is listening | [Port Scanning](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-nmap) |
| `nc [-l] [<ip>] [<port>]` | create a TCP socket over which to transfer data | [Bandwidth](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-netcat-to-test-network-bandwidth) |
| `netstat -nr`, `route -n`, `ip route`, `ip r` | Display current routing table | [Routing Table](../Linux/Networking-LHN/02-LinuxNet.md#how-to-view-current-routing-table) |

## syslog

| Command | Description | Link |
|---------|-------------|------|
| `tail -f <logfile>` | Display new log entries to scroll on the screen; logfile: /var/log/syslog, /var/log/messages | [View New Log Entries](../Linux/Networking-LHN/05-TrblSyslog.md#how-to-view-new-log-entries-as-they-happen) |
| `logrotate -f [FILE]` | activate log rotation, no FILE = `/etc/logrotate.conf` | [Logrotate](../Linux/Networking-LHN/05-TrblSyslog.md#logrotate) |


## Software Installation

| Command | Description | Link |
|---------|-------------|------|
| `rpm [-Uvh]` | RedHat Package Manager; U=Updating, v=verbose, h=list of hash # characters | [CD-ROMs or DVDs](../Linux/Networking-LHN/06-SWInstall.md#how-to-install-rpms-manually) |
| `rpmbuild --rebuild <pkg>.src.rpm` | Install source RPM | [CD-ROMs or DVDs](../Linux/Networking-LHN/06-SWInstall.md#how-to-install-rpms-manually) |
| `rpm -q[lp] [<pkg>]` | query/list installed RPM files, q=query, l=associated files, p=package | [List RPMs](../Linux/Networking-LHN/06-SWInstall.md#how-to-list-installed-rpms) |
| `rpm -qf <filename>` | `filename` in which RPM | [List RPMs](../Linux/Networking-LHN/06-SWInstall.md#how-to-list-installed-rpms) |
| `rpm -e <pkg>` | Uninstall PRM package | [List RPMs](../Linux/Networking-LHN/06-SWInstall.md#how-to-list-installed-rpms) |
| `yum –y install <pkg>` | Install package | [Auto `yum`](../Linux/Networking-LHN/06-SWInstall.md#automatic-updates-with-yum) |
| `yum update` | Update all packages | [Automate `yum` Manually](../Linux/Networking-LHN/06-SWInstall.md#how-to-automate-yum-manually) |
| `dpkg --install <pkg>` | Debian/Ubuntu package installation | [DEB Installtaion](../Linux/Networking-LHN/06-SWInstall.md#installing-software-from-deb-files) |
| `dpkg --list` | List installed packages | [DEB Installation](../Linux/Networking-LHN/06-SWInstall.md#installing-software-from-deb-files) |
| `dpkg --listfiles <pkg>` | List files for previous installed DEBs | [DEB Installation](../Linux/Networking-LHN/06-SWInstall.md#installing-software-from-deb-files) |
| `dpkg --contents <pkg>` | List files in DEB files | [DEB Installation](../Linux/Networking-LHN/06-SWInstall.md#installing-software-from-deb-files) |
| `dpkg --search <file>` | List files the DEB package to which a file belongs | [DEB Installation](../Linux/Networking-LHN/06-SWInstall.md#installing-software-from-deb-files) |
| `dpkg --remove <pkg>` | Uninstall DEB package | [DEB Installation](../Linux/Networking-LHN/06-SWInstall.md#installing-software-from-deb-files) |
| `apt-get {update|upgrade} [-y]` | Update or upgrade DEB packages | [Auto DEBs](../Linux/Networking-LHN/06-SWInstall.md#automatic-deb-udates-with-apt---get) |




