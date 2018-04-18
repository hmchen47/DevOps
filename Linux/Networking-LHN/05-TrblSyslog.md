# Ch## ##  : Troubleshooting Linux with syslog

## syslog

+ syslog: a utility for tracking and logging all manner of system messages
+ Descriptive labels of syslog:
    + 1st: function (facility) of the application
    + 2nd: degree of severity of the message
+ Syslog Facilities

| Severity Level | Keyword | Description |
|----------------|---------|-------------|
| 0 | emergencies | System unusable |
| 1 | alerts | Immediate action required |
| 2 | critical | Critical condition |
| 3 | errors | Error conditions |
| 4 | warnings | Warning conditions |
| 5 | notifications | Normal but significant conditions |
| 6 | informational | Informational messages |
| 7 | debugging | Debugging messages |

### The /etc/rsyslog.conf File


### Activating Changes to the syslog Configuration File


### How to View New Log Entries as They Happen


### Logging syslog Messages to a Remote Linux Server


+ Configuring the Linux Syslog Server

+ Configuring the Linux Client


### Syslog Configuration and Cisco Network Devices


## Logrotate


### The /etc/logrotate.conf File


### Sample Contents of /etc/logrotate.conf


### The /etc/logrotate.d Directory


### Activating logrotate


### Compressing Your Log Files


## syslog-ng


### The /etc/syslog-ng/syslog-ng.conf file


+ Simple Server Side Configuration for Remote Clients


+ Figure ## -##  A Sample syslog-ng.conf File


+ Using syslog-ng in Large Data Centers


+ Figure ## -##  More Specialized syslog-ng.conf Configuration


### Installing and Starting syslog-ng


### Configuring syslog-ng Clients


+ Example ## -##  - Syslog-ng Sample Client Configuration


## Simple syslog Security

