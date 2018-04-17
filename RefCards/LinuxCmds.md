# Linux Command Reference Cards

## Networking

| Command | Description | Link |
|---------|-------------|------|
| `ifconfig -a` | list all interfaces; up/down interfaces; NIC errors; MAC & IP addresses | [Testing NIC](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic); [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors); [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess) |
| `ip addr`; `ip a` | list all interfaces; up/down interfaces; MAC & IP addresses | [Testing NIC](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic); [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess)  |
| `mii-tool` | Link status output (older version) | [Testing Link Status](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic) |
| `ethtool` |  Link status output (newer version) | [Testing Link Status](../Linux/Networking-LHN/04-SimpleNetTrbl.md#testing-nic) |
| `ip -s link`; `ip -s a` | NIC error output | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors) |
| `ethtoll -S` | NIC error output - detailed report | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors) |
| `netstat -i` | NIC error output - limited report | [NIC Errors](../Linux/Networking-LHN/04-SimpleNetTrbl.md#viewing-nic-errors) |
| `arp -a` | MAC address of ARP table | [MAC & IP addr](../Linux/Networking-LHN/04-SimpleNetTrbl.md#how-to-see-mac-addressess) |
| `ping -c <num> <ip/fqdn>` | limit ping counts | [Connectivity w/ ping](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-ping-to-test-network-connectivity) |
| `telnet <ip> <port>` | Connectivity test; remote session; default: TCP port 23 | [Connectivy w/ telnet](../Linux/Networking-LHN/04-SimpleNetTrbl.md#using-telnet-to-test-network-connectivity) |


