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

+ config file - defines which file to write the messages: `/etc/rsyslog.conf`
+ Fedora old version: `/etc/syslog.conf`
+ Two column entry:
    + 1st: the facilities and severities of messages to expect
    + 2nd: files to which they should be logged
+ Examples
    + all messages of severity "info" and above are logged, but none from the `mail`, `cron` or authentication facilities/subsystems:  
    `*.info;mail.none;authpriv.none;cron.none           /var/log/messages`
    + all debug severity messages; except `auth`, `authpriv`, `news` and `mail`; are logged to the `/var/log/debug` file  
        ```script
        *.=debug;\
            auth,authpriv.none;\
            news.none;mail.none     -/var/log/debug
       ```
    + caching mode to receive only info, notice and warning messages except for the `auth`, `authpriv`, `news` and `mail` facilities; logged to `/var/log/messages`  
        ```script
        *.=info;*.=notice;*.=warn;\
            auth,authpriv.none;\
            cron,daemon.none;\
            mail,news.none          -/var/log/messages
       ```
+ Additionally log for certain application independent of the `syslog.conf` file
    + Files:
        ```
        /var/log/maillog             : Mail
        /var/log/httpd/access_log    : Apache web server page access logs
        ```
    + Directories:
        ```
        /var/log
        /var/log/samba                      : Samba messages
        /var/log/mrtg                       : MRTG messages
        /var/log/httpd                      : Apache webserver messages
        ```

### Activating Changes to the syslog Configuration File

+ daemon: `rsyslog`
+ Auto start at booting
+ modification of config file -> restart daemon


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

