# CH04: Simple Network Troubleshooting

## Introduction

#### Sources of Network Slowness

#### Sources of a Lack of Connectivity

#### Doing Basic Cable and Link Tests

## Testing Your NIC

### Viewing Your Activated Interfaces

### Viewing All Interfaces

#### DHCP Considerations

### Testing Link Status from the Command Line

#### Link Status Output from `mii-tool`

#### Link Status Output from `ethtool`

### Viewing NIC Errors

#### `ifconfig` Error Output

#### `ethtool` Error Output

### `netstat` Error Output

#### Possible Causes of Ethernet Errors

## How to See MAC Addresses

## Using `ping` to Test Network Connectivity

## Using `telnet` to Test Network Connectivity

#### Linux `telnet` Troubleshooting

#### Successful Connection

#### Connection Refused Messages

#### `telnet` Timeout or Hanging

#### `telnet` Troubleshooting Using Windows

#### Screen Goes Blank - Successful Connection

#### "Connect Failed" Messages

#### `telnet` Timeout or Hanging

## Testing Web sites with the `curl` and `wget` Utilities

#### Using `curl`

#### Using `wget`

## The `netstat` Command

## The Linux `iptables` Firewall

#### How to Configure `iptables` Rules

## Using `traceroute` to Test Connectivity

#### Sample `traceroute` Output

#### Possible `traceroute` Messages

#### Table 4-1: `traceroute` Return Code Symbols

#### `traceroute` Time Exceeded False Alarms

#### `traceroute` Internet Slowness False Alarm

#### `traceroute` Dies At The Router Just Before The Server

#### Always Get a Bidirectional `traceroute`

#### ping and `traceroute` Troubleshooting Example

#### `traceroute` Web sites

#### Possible Reasons For Failed Traceroutes

## Using `MTR` To Detect Network Congestion

## Viewing Packet Flows with `tcpdump`

#### Table 4-2 : Possible `tcpdump` Switches

#### Table 4-3 : Useful `tcpdump` Expressions

#### Analyzing `tcpdump` files

#### Common Problems with `tcpdump`

##Viewing Packet Flows with `tshark`

#### Table 4-4 : Possible `tshark` Switches

#### Table 4-5 : Useful `tshark` Expressions

## Basic DNS Troubleshooting

#### Using `nslookup` to Test DNS

#### Using `nslookup` to Check Your Web site Name

#### Using `nslookup` To Check Your IP Address

#### Using `nslookup` to Query a Specific DNS Server

#### Using the host Command to Test DNS

## Using `nmap`

#### Table 4-6 Commonly Used NMAP Options

## Using `netcat` to Test Network Bandwidth

## Determining the Source of an Attack

## Who Has Used My System?

### The `last` Command

### The `who` Command
