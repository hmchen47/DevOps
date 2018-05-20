# Linux Command Reference Cards

## General

| Command | Description | Link |
|---------|-------------|------|
| `whois [ip | fqdn]` | administrative info | [Identification][gen00] |
| `last [-num]` | a listing of last logged in users | [Identification][gen01] |
| `who` | who currently logged in | [Identification][gen01] |
| `grep [opt] <str> [file...]` | print lines matching a pattern; option: e=pattern(greexp), f=FILE | [View New Log Entries][gen02] |
| `tar -[cxvfz] <file>` | archive/extract files; c=create, x=extract, v=verbose, f=filename, z=compress | [tar Files][gen03] |


[gen00]: ../Linux/Networking-LHN/04-SimpleNetTrbl.md#determining-the-source-of-an-attack
[gen01]: ../Linux/Networking-LHN/04-SimpleNetTrbl.md#who-has-used-my-system
[gen02]: \(../Linux/Networking-LHN/05-TrblSyslog.md#how-to-view-new-log-entries-as-they-happen
[gen03]: ../Linux/Networking-LHN/06-SWInstall.md#installing-software-using-tar-files



## System

| Command | Description | Link |
|---------|-------------|------|
| `chkconfig` | used to activate and deactivate services | [chkconfig][sys000] |
| `chkconfig --list` | Displayed all services and their current start-up status in each run-level configuration | [List RPMs][sys001] |
| `systemctl {enable\|disable} <daemon>.service` | Enable/Disable at boot time w/ `systemd` | [Auto `yum`][sys002] |
| `service <daemon> {start|stop}` | Start/Stop a daemon w/ `sysvinit` | [Auto `yum`][sys002] |
| `systemctl {start\|stop} <daemon>.service` | Start/stop a daemon w/ `systemd` | [Auto `yum`][sys002] |
| `systemctl {start\|stop\|restart|status} <pkg>.service` | start/stop/restart/status daemon - Non-persistent w/ `systemd`| [Managing Daemons][sys004] |
| `service <pkg> {start\|stop\|restart\|status}` | start/stop/restart/status daemon - Non-persistent w/ `sysvinit`| [Managing Daemons][sys004] |
| `/etc/init.d/ <pkg> {start\|stop\|restart\|status}` | start/stop/restart/status daemon - Non-persistent w/ Init Script | [Managing Daemons][sys004] |
| `sysv-rc-conf  <pkg> {start\|stop\|restart\|status}` | start/stop/restart/status daemon - Non-persistent w/ `sysv-rc-conf` | [Managing Daemons][sys004] |
| `systemctl {enable\|disable\|is-enabled} <pkg>.service` | start/stop/status daemon - Persistent w/ `systemd` | [Managing Daemons][sys004] |
| `chkconfig <pkg> {on\|off}` | start/stop daemon - Persistent w/ `sysvinit` & Init script | [Managing Daemons][sys004] |
| `chkconfig --list` | status daemon - Persistent w/ `sysvinit` & Init script | [Managing Daemons][sys004] |
| `sysv-rc-conf  <pkg> {on\|off}` | start/stop daemon - Persistent w/ `sysv-rc-conf` | [Managing Daemons][sys004] |
| `sysv-rc-conf --list` | status daemon - Persistent w/ `sysv-rc-conf` | [Managing Daemons][sys004] |
| `sysv-rc-conf --level <#...> <pkg> on` | set a daemon to start only at given number(s) | [`sysv-rc-conf` Cmd][sys003] |
| `runlevel` | 
| `systemctl {enable\|disable\|isolate} <runlevel>.target` | Set/Change the default target group | [systemd][sys005] |
| `systemctl list-units --type=target` | List all active targets in the active target group | [systemd][sys005] |
| `ln -sf /lib/systemd/system/<runlevel>multi-user.target /etc/systemd/system/default.target` | Set the default target group | [Boot Process][sys005] |
| `init <runlevel>` | systemd system and service manager; 0 - halt/shutdown, 1- single user, 3 - multi-user w/ CLI, 5 - multi-user w/ GUI, 6 - reboot | [Shutdown & Reboot][sys006] |
| `shutdown -[y\|r\|h] <min>` | Fedora system shutdown or reboot; `h`: halt, `y`: no prompt, `r`: reboot, `<min>`=0: Now | [Shutdown & Reboot][sys006] |
| `reboot` | Fedora system reboot | [Shutdown & Reboot][sys006] |
| `exit` | force the system to exit runlevel 1 and revert to the default runlevel | [Shutdown & Reboot][sys006] |



[sys000]: https://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-services-chkconfig.html
[sys001]: ../Linux/Networking-LHN/06-SWInstall.md#how-to-list-installed-rpms
[sys002]: ../Linux/Networking-LHN/06-SWInstall.md#automatic-updates-with-yum
[sys003]: ../Linux/Networking-LHN/06-SWInstall.md#the-sysv---rc---conf-command
[sys004]: ../Linux/Networking-LHN/06-SWInstall.md#managing-daemons
[sys005]: ../Linux/Networking-LHN/07-BootProc.md#systemd
[sys006]: ../Linux/Networking-LHN/07-BootProc.md#system-shutdown-and-rebooting
[sys007]: ../Linux/Networking-LHN/07-BootProc.md#


## Hardware 

| Command | Description | Link |
|---------|-------------|------|
| `mount /mnt/<dev>` | Mount device to /mnt/ | [CD-ROMs or DVDs][hw00] |
| `eject cdrom` | unmount CDROM | [CD-ROMs or DVDs][hw00] |
| `umount /mnt` | unmount device | [CD-ROMs or DVDs][hw00] |


[hw00]: ../Linux/Networking-LHN/06-SWInstall.md#how-to-install-rpms-manually

## Networking

### Configuration

| Command | Description | Link |
|---------|-------------|------|
| `ifconfig <if> <ip> netmask <mask> up` | configure IP address of an interface; `<if:x>`=sub-interface=virtual interface | [Configure IP Address][net000] |
| `ip addr add <ip>/<mask> dev <if>` | configure IP address of an interface; `<if:x>`=sub-interface=virtual interface | [Configure IP Address][net000] |
| `ipup <if>` & `ipdown <if>` | Activate & deactivate interface | [Configure IP Address][net000] |
| `route add default gw <ip> <if>` | Config default gateway | [Gatway][net001] |
| `ip route add default via <ip> <if>` | Config default gateway | [Gateway][net001] |
| `route add -net <net> netmask <mask> gw <ip> <if>` | Add route | [Configure Gateways][net002] |
| `ip route add <net>/<mask> via <gwip> dev <if>` | Add route | [Configure Gateways][net002] |
| `route add -host <ip> gw <ip> <if>` | add a route to an individual server | [Add Routes][net002] |
| `ip route add <ip> via <gwip> dev <if>` | add a route to an individual server | [Add Routes][net002] |
| `route del -net <net> netmask <mask> gw <ip> <if>` | [Delete Routes] | [Delete Route][net003] |
| `ip route del <net>/<mask> via <gwip> dev <if>` | [Delete Routes] | [Delete Route][net003] |
| `mii-tool -F <opt> <if>` | Configure NIC's Speed Parameters | [NIC Speed & Duplex][net004] |
| `ethtool -s <if> [speed 10|100|1000] [duplex full|half [autoneg on|off]` | Configure NIC's Speed Parameters | [NIC Speed & Duplex][net004] |


[net000]: ../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-your-nics-ip-address
[net001]: ../Linux/Networking-LHN/03-LinuxNet.md#how-to-change-your-default-gateway
[net002]: ../Linux/Networking-LHN/03-LinuxNet.md#how-to-configure-two-gGateways
[net003]: ../Linux/Networking-LHN/03-LinuxNet.md#how-to-delete-a-route
[net004]: ../Linux/Networking-LHN/03-LinuxNet.md#changing-nic-speed-and-duplex



### Troubleshooting

| Command | Description | Link |
|---------|-------------|------|
| `ifconfig -a` | list all interfaces; up/down interfaces; NIC errors; MAC & IP addresses | [Testing NIC][trbl000]; [NIC Errors][trbl001]; [MAC & IP addr][trbl002] |
| `ip addr`; `ip a` | list all interfaces; up/down interfaces; MAC & IP addresses | [Testing NIC][trbl000]; [MAC & IP addr][trbl002]  |
| `mii-tool -v <if>` | Link status output (older version) | [Testing Link Status][trbl000] |
| `ethtool <if>` |  Link status output (newer version) | [Testing Link Status][trbl000] |
| `ip -s a`; `ip -s link` | NIC error output | [NIC Errors][trbl001] |
| `ethtoll -S` | NIC error output - detailed report | [NIC Errors][trbl001] |
| `arp -a` | MAC address of ARP table | [MAC & IP addr][trbl002] |
| `ping -c <num> <ip/fqdn>` | limit ping counts | [Connectivity][trbl003] |
| `telnet <ip> <port>` | Connectivity test; remote session; default: TCP port 23 | [Connectivity][trbl004] |
| `curl -I <fqdn>` | text based web browser; display web page header and status code | [Connectivity][trbl005] |
| `wget -N <fqdn>` | recursively download web pages w/o timestamps | | [Connectivity][trbl005] |
| `netstat -<opt>` | network connections, routing tables, interface statistics, masquerade connections, and multicast memberships; opt: a=all, l=listening, i=interface, r=route, v=verbose, t=tcp, u=udp, p=pid, n=numeric, s=statistics | [NIC Errors][trbl001]; [Connectivity][trbl006] |
| `ss -<opt>` | network connections, routing tables, interface statistics, masquerade connections, and multicast memberships; opt: l=listening, r=resolve, v=verbose, t=tcp, u=udp, p=process, w=RAW socket, s=summary | [Connectivity][trbl006] |
| `traceroute <ip>` | route packets trace to network host | [Connectivity][trbl007] |
| `mtr <ip>` | repeat `traceroute` in real time | [Congestion][trbl008] |
| `tcpdump -<opt> [<expr>]` | viewing the flow of packets through NIC; __opt__: c=count, i=interface, w=dump file, C=file size, t=no timestamp, n=no DNS; __expr__: host,icmp, tcp, udp, port | [Packet Flow][trbl009] |
| `tshark -<opt> [<expr>]` | Fedora Linux Wireshark RPM | [Packet Flow][trbl010] |
| `nslookup <fqdn> | <ip>` | used to get associated IP addr for given domain and vice versa | [DNS][trbl011] |
| `host <fqdn> | <ip>` | newer cmd used to get associated IP addr for given domain and vice versa | [DNS][trbl011] |
| `nmap <-opt>` | determine all the TCP/IP ports on which a remote server is listening | [Port Scanning][trbl012] |
| `nc [-l] [<ip>] [<port>]` | create a TCP socket over which to transfer data | [Bandwidth][trbl013] |
| `netstat -nr`, `route -n`, `ip route`, `ip r` | Display current routing table | [Routing Table][trbl014] |

[trbl000]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic)
[trbl001]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors)
[trbl002]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess)
[trbl003]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-ping-to-test-network-connectivity)
[trbl004]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-telnet-to-test-network-connectivity)
[trbl005]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-web-sites-with-the-curl-and-wget-utilities)
[trbl006]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#the-netstat-command)
[trbl007]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-traceroute-to-test-connectivity)
[trbl008]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-mtr-to-detect-network-congestion)
[trbl009]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-packet-flows-with-tcpdump)
[trbl010]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-packet-flows-with-tshark)
[trbl011]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#basic-dns-troubleshooting)
[trbl012]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-nmap)
[trbl013]: (../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-netcat-to-test-network-bandwidth)
[trbl014]: (../Linux/Networking-LHN/02-LinuxNet.md#how-to-view-current-routing-table)




## syslog

| Command | Description | Link |
|---------|-------------|------|
| `tail -f <logfile>` | Display new log entries to scroll on the screen; logfile: /var/log/syslog, /var/log/messages | [View New Log Entries][gen02] |
| `logrotate -f [FILE]` | activate log rotation, no FILE = `/etc/logrotate.conf` | [Logrotate][log00] |


[log00]: (../Linux/Networking-LHN/05-TrblSyslog.md#logrotate)


## Software Installation

| Command | Description | Link |
|---------|-------------|------|
| `rpm [-Uvh]` | RedHat Package Manager; U=Updating, v=verbose, h=list of hash # characters | [CD-ROMs or DVDs][hw00] |
| `rpmbuild --rebuild <pkg>.src.rpm` | Install source RPM | [CD-ROMs or DVDs][hw00] |
| `rpm -q[lp] [<pkg>]` | query/list installed RPM files, q=query, l=associated files, p=package | [List RPMs][ins000] |
| `rpm -qf <filename>` | `filename` in which RPM | [List RPMs][ins000] |
| `rpm -e <pkg>` | Uninstall PRM package | [List RPMs][ins000] |
| `yum –y install <pkg>` | Install package | [Auto `yum`][sys002] |
| `yum update` | Update all packages | [Automate `yum` Manually][ins001] |
| `dpkg --install <pkg>` | Debian/Ubuntu package installation | [DEB Installtaion][ins000] |
| `dpkg --list` | List installed packages | [DEB Installation][ins000] |
| `dpkg --listfiles <pkg>` | List files for previous installed DEBs | [DEB Installation][ins000] |
| `dpkg --contents <pkg>` | List files in DEB files | [DEB Installation][ins000] |
| `dpkg --search <file>` | List files the DEB package to which a file belongs | [DEB Installation][ins000] |
| `dpkg --remove <pkg>` | Uninstall DEB package | [DEB Installation][ins000] |
| `apt-get {update|upgrade} [-y]` | Update or upgrade DEB packages | [Auto DEBs](../Linux/Networking-LHN/06-SWInstall.md#automatic-deb-udates-with-apt---get) |

[ins000]: (../Linux/Networking-LHN/06-SWInstall.md#how-to-list-installed-rpms)
[ins001]: (../Linux/Networking-LHN/06-SWInstall.md#how-to-automate-yum-manually)
[ins002]: (../Linux/Networking-LHN/06-SWInstall.md#installing-software-from-deb-files)


