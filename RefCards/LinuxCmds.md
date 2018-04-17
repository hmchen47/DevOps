# Linux Command Reference Cards

## Networking

| Command | Description | Link |
|---------|-------------|------|
| `ifconfig -a` | list all interfaces; up/down interfaces; NIC errors; MAC & IP addresses | [Testing NIC](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic); [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors); [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess) |
| `ip addr`; `ip a` | list all interfaces; up/down interfaces; MAC & IP addresses | [Testing NIC](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic); [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess)  |
| `mii-tool` | Link status output (older version) | [Testing Link Status](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic) |
| `ethtool` |  Link status output (newer version) | [Testing Link Status](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic) |
| `ip -s a`; `ip -s link` | NIC error output | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors) |
| `ethtoll -S` | NIC error output - detailed report | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors) |
| `netstat -i` | NIC error output - limited report | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors) |
| `arp -a` | MAC address of ARP table | [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess) |
| `ping -c <num> <ip/fqdn>` | limit ping counts | [Connectivity w/ ping](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-ping-to-test-network-connectivity) |
| `telnet <ip> <port>` | Connectivity test; remote session; default: TCP port 23 | [Connectivity w/ telnet](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-telnet-to-test-network-connectivity) |
| `curl -I <fqdn>` | text based web browser; display web page header and status code | [Connectivity w/ curl & wget](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-web-sites-with-the-curl-and-wget-utilities) |
| `wget -N <fqdn>` | recursively download web pages w/o timestamps | | [Connectivity w/ curl & wget](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-web-sites-with-the-curl-and-wget-utilities) |
| `netstat -<opt>` | network connections, routing tables, interface statistics, masquerade connections, and multicast memberships; opt: a=all, l=listening, i=interface, r=route, v=verbose, t=tcp, u=udp, p=pid, n=no resolve name | [Connectivity w/ netstat](../Linux/Networking-LHN/04-SimpleNetTrbl.md#the-netstat-command) |
| `ss -<opt>` | network connections, routing tables, interface statistics, masquerade connections, and multicast memberships; opt: l=listening, r=resolve, v=verbose, t=tcp, u=udp, p=process, w=RAW socket, s=summary | [Connectivity w/ netstat](../Linux/Networking-LHN/04-SimpleNetTrbl.md#the-netstat-command) |
| `traceroute <ip>` | route packets trace to network host | [Connectivity w/ traceroute](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-traceroute-to-test-connectivity) |
| `mtr <ip>` | repeat `traceroute` in real time | [Congestion w/ mtr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-mtr-to-detect-network-congestion) |
| `tcpdump -<opt> [<expr>]` | viewing the flow of packets through NIC; __opt__: c=count, i=interface, w=dump file, C=file size, t=no timestamp, n=no DNS; __expr__: host,icmp, tcp, udp, port | [Packet Flow](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-packet-flows-with-tcpdump) |
| `tshark -<opt> [<expr>]` | Fedora Linux Wireshark RPM | [Packet Flow](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-packet-flows-with-tshark) |



