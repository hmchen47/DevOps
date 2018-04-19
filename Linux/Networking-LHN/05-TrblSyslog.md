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

+ Get new log entries to scroll on the screen as they occur:  
    `tail -f /var/log/messages` or `tail -f /var/log/syslog`
+ `grep` search for all occurrences of a string in a log file:  
    `grep string /var/log/messages | more`

### Logging syslog Messages to a Remote Linux Server

+ Configuring the Linux Syslog Server
    + Fedora: Syslog listens for remote messages only if `SYSLOGD`_OPTIONS w/ `-r`
        ```
        # Options to syslogd
        # -m 0 disables 'MARK' messages.
        # -r enables logging from remote machines
        # -x disables DNS lookups on messages received with -r
        # See syslogd(8) for more details

        SYSLOGD_OPTIONS="-m 0 -r"
        ```
    + Debian / Ubuntu systems
        ```
        # Options for start/restart the daemons
        #   For remote UDP logging use SYSLOGD="-r"
        #
        #SYSLOGD="-u syslog"
        SYSLOGD="-r"
        ```
    + restart `syslog` on the server for the changes
    + Verify w/ UDP port 514: `netstat -a | grep syslog` or `ss -anlp | grep syslog`
+ Configuring the Linux Client
    + Config procedure
        1. Determine IP addr or FQDN of remote server
        2. Add an entry in the `/etc/hosts` file w/ the format:  
            `IP-address    fully-qualified-domain-name    hostname    "loghost"`
        3. edit `/etc/rsyslog.conf` file to send the syslog messages to new `loghost` nickname  
            ```
            *.debug                           @loghost
            *.debug                           /var/log/messages
            ```
    + Verify w/ restart a daemon, such as `lpd`:
        + Linux client: `systemctl restart lpd.service`
        + Linux server: `tail /var/log/messages`

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

