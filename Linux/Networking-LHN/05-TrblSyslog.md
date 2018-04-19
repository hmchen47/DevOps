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

+ syslog reserves facilities "local0" through "local7" for log messages received from remote servers and network devices
+ Each network devices w/ its own log files for trbl

## Logrotate

+ The `/etc/logrotate.conf` File
    + rotation parameter: weekly or daily 
    + rotate parameter: number of copies of log files
    + create parameter: creating a new log file after each rotation
+ Sample Contents of /etc/logrotate.conf
    ```
    # rotate log files weekly
    #weekly

    # rotate log files daily
    daily

    # keep 4 weeks worth of backlogs
    #rotate 4

    # keep 7 days worth of backlogs
    rotate 7

    # create new (empty) log files after rotating old ones
    create
    ```
+ The `/etc/logrotate.d` Directory
    + Most Linux applications using syslog to put an additional configuration file in this directory
    + Verify new applications configure properly
    + e.g.
        ```
        /data/backups/*.tgz {
            daily
            rotate 30
            nocompress
            missingok
            notifempty
            create 0600 root root
        }
        ```
    + Debian / Ubuntu: `/etc/cron.daily/sysklogd` script reads the `/etc/rsyslog.conf` file
+ Activating logrotate: `logrotate -f` or `logrotate -f /etc/logrotate.d/syslog`
+ Compressing Your Log Files
    + activated by editing the `/etc/logrotate.conf` file w/ `compress` option
    + Example:
        ```
        # Activate log compression
        compress
        ```

## syslog-ng

+ `syslog-ng`: combine the features of logrotate and syslog
+ exclusive w/ `syslog`
+ config file: `/etc/syslog-ng/syslog-ng.conf`
+ Simple Server Side Configuration for Remote Clients
    ```
    options {

            # Number of syslog lines stored in memory before being written to files
            sync (0);

            # Syslog-ng uses queues
            log_fifo_size (1000);

            # Create log directories as needed
            create_dirs (yes);

            # Make the group "logs" own the log files and directories
            group (logs);
            dir_group (logs);

            # Set the file and directory permissions
            perm (0640);
            dir_perm (0750);

            # Check client hostnames for valid DNS characters
            check_hostname (yes);

            # Specify whether to trust hostname in the log message.
            # If "yes", then it is left unchanged, if "no" the server replaces
            # it with client's DNS lookup value.
            keep_hostname (yes);

            # Use DNS fully qualified domain names (FQDN) 
            # for the names of log file folders
            use_fqdn (yes);
            use_dns (yes);

            # Cache DNS entries for up to 1000 hosts for 12 hours
            dns_cache (yes);
            dns_cache_size (1000);
            dns_cache_expire (43200);

            };

    # Define all the sources of localhost generated syslog
    # messages and label it "d_localhost"
    source s_localhost {
            pipe ("/proc/kmsg" log_prefix("kernel: "));
            unix-stream ("/dev/log");
            internal();
    };
    
    # Define all the sources of network generated syslog
    # messages and label it "d_network"
    source s_network {
            tcp(max-connections(5000));
            udp();
    };

    # Define the destination "d_localhost" log directory
    destination d_localhost {
            file ("/var/log/syslog-ng/$YEAR.$MONTH.$DAY/localhost/$FACILITY.log");
    };

    # Define the destination "d_network" log directory
    destination d_network {
            file ("/var/log/syslog-ng/$YEAR.$MONTH.$DAY/$HOST/$FACILITY.log");
    };

    # Any logs that match the "s_localhost" source should be logged
    # in the "d_localhost" directory

    log { source(s_localhost);
        destination(d_localhost);
    };

    # Any logs that match the "s_network" source should be logged
    # in the "d_network" directory
    
    log { source(s_network);
        destination(d_network);
    };
    ```

+ Using syslog-ng in Large Data Centers
    ```
    options {

            # Number of syslog lines stored in memory before being written to files
            sync (100);
    };

    # Define all the sources of network generated syslog
    # messages and label it "s_network_1"
    source s_network_1 {
            udp(ip(192.168.1.201) port(514));
    };

    # Define all the sources of network generated syslog
    # messages and label it "s_network_2"
    source s_network_2 {
            udp(ip(192.168.1.202) port(514));
    };

    # Define the destination "d_network_1" log directory
    destination d_network_1 {
            file ("/var/log/syslog-ng/servers/$YEAR.$MONTH.$DAY/$HOST/$FACILITY.log");
    };

    # Define the destination "d_network_2" log directory
    destination d_network_2 {
            file ("/var/log/syslog-ng/network/$YEAR.$MONTH.$DAY/$HOST/$FACILITY.log");
    };

    # Define the destination "d_network_2B" log directory
    destination d_network_2B {
            file ("/var/log/syslog-ng/network/all/network.log");
    };

    # Any logs that match the "s_network_1" source should be logged
    # in the "d_network_1" directory

    log { source(s_network_1);
        destination(d_network_1);
    };

    # Any logs that match the "s_network_2" source should be logged
    # in the "d_network_2" directory

    log { source(s_network_2);
        destination(d_network_2);
    };

    # Any logs that match the "s_network_2" source should be logged
    # in the "d_network_2B" directory also

    log { source(s_network_2);
        destination(d_network_2B);
    };
    ```
+ Installing and Starting `syslog-ng`
    1. Uninstall `rsyslog` using the `rpm` command: `rpm -e --nodeps rsyslog`
    2. Install `syslog-ng` using `yum`: `yum -y install syslog-ng`
    3. Start the new `syslog-ng` daemon immediately and ensure starting on the next reboot: 
        + Systems using `sysvinit`: 
            ```shell
            chkconfig syslog-ng on
            service syslog-ng start
            ```
        + Systems using `systemd`:
            ```shell
            enable syslog-ng.service
            start syslog-ng.service
            ```
+ Configuring syslog-ng Clients
    ```shell
    source s_sys {
    file ("/proc/kmsg" log_prefix("kernel: "));
    unix-stream ("/dev/log");
    internal();
    };

    destination loghost { 
    udp("loghost.linuxhomenetworking.com"); 
    };

    filter notdebug { 
    level(info...emerg); 
    };

    log { 
    source(local);
    filter(notdebug);
    destination(loghost); 
    };
    ```

## Simple syslog Security

+ syslog server not filtering out messages from undesirable sources
+ Solution: implement the use of TCP wrappers or a firewall to limit the acceptable sources of messages
