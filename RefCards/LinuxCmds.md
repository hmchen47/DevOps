# Linux Command Reference Cards

## General

| Command | Description | Link |
|---------|-------------|------|
| `whois [ip | fqdn]` | administrative info | [Identification](../Linux/Networking-LHN/04-SimpleNetTrbl.md#determining-the-source-of-an-attack) |
| `last [-num]` | a listing of last logged in users | [Identification](../Linux/Networking-LHN/04-SimpleNetTrbl.md#who-has-used-my-system) |
| `who` | who currently logged in | [Identification](../Linux/Networking-LHN/04-SimpleNetTrbl.md#who-has-used-my-system) |

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
| `ping -c <num> <ip/fqdn>` | limit ping counts | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-ping-to-test-network-connectivity) |
| `telnet <ip> <port>` | Connectivity test; remote session; default: TCP port 23 | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-telnet-to-test-network-connectivity) |
| `curl -I <fqdn>` | text based web browser; display web page header and status code | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-web-sites-with-the-curl-and-wget-utilities) |
| `wget -N <fqdn>` | recursively download web pages w/o timestamps | | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-web-sites-with-the-curl-and-wget-utilities) |
| `netstat -<opt>` | network connections, routing tables, interface statistics, masquerade connections, and multicast memberships; opt: a=all, l=listening, i=interface, r=route, v=verbose, t=tcp, u=udp, p=pid, n=no resolve name | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#the-netstat-command) |
| `ss -<opt>` | network connections, routing tables, interface statistics, masquerade connections, and multicast memberships; opt: l=listening, r=resolve, v=verbose, t=tcp, u=udp, p=process, w=RAW socket, s=summary | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#the-netstat-command) |
| `traceroute <ip>` | route packets trace to network host | [Connectivity](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-traceroute-to-test-connectivity) |
| `mtr <ip>` | repeat `traceroute` in real time | [Congestion](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-mtr-to-detect-network-congestion) |
| `tcpdump -<opt> [<expr>]` | viewing the flow of packets through NIC; __opt__: c=count, i=interface, w=dump file, C=file size, t=no timestamp, n=no DNS; __expr__: host,icmp, tcp, udp, port | [Packet Flow](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-packet-flows-with-tcpdump) |
| `tshark -<opt> [<expr>]` | Fedora Linux Wireshark RPM | [Packet Flow](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-packet-flows-with-tshark) |
| `nslookup <fqdn> | <ip>` | used to get associated IP addr for given domain and vice versa | [DNS](../Linux/Networking-LHN/04-SimpleNetTrbl.md#basic-dns-troubleshooting) |
| `host <fqdn> | <ip>` | newer cmd used to get associated IP addr for given domain and vice versa | [DNS](../Linux/Networking-LHN/04-SimpleNetTrbl.md#basic-dns-troubleshooting) |
| `nmap <-opt>` | determine all the TCP/IP ports on which a remote server is listening | [Port Scanning](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-nmap) |
| `nc [-l] [<ip>] [<port>]` | create a TCP socket over which to transfer data | [Bandwidth](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-netcat-to-test-network-bandwidth) |






