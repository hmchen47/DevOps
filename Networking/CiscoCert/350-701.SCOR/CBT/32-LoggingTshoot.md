# 32. Troubleshoot Network Problems using Logging

Trainer: Keith Barker


## Introduction to Troubleshooting using Logging

- Learning goal
  - logging
  - logging config
  - debugging
  - troubleshoot w/ logging



## Logging Overview

- Logging overview
  - display types
    - console: line console 0
    - monitor:
      - terminal lines, `line vty 0-15`
      - displaying log message at terminal lines, `terminal monitor`
    - buffer: storing on buffer
  - logging severity level:
    - 0: Emergencies - device unusable
    - 1: alerts - immediate action required
    - 2: critical - conditional critical
    - 3: error - error condition
    - 4: warnings - warning condition
    - 5: notifications - normal but important event
    - 6: informational - informational messages
    - 7: debugging - debug message
  - verify system logging settings
    
    ```text
    R1# show logging
    Syslog logging: enabled (0 messages dropped, 0 messages rate-limited,
                    0 flushes, 0 overruns, xml disabled, filtering disabled)
    No Active Message Discriminator.
    No Inactive Message Discriminator.
        Console logging: level debugging, 70 messages logged, xml disabled,
                        filtering disabled
        Monitor logging: level debugging, 0 messages logged, xml disabled,
                        filtering disabled
        Buffer logging:  level debugging, 40 messages logged, xml disabled,
                        filtering disabled
        Logging Exception size (8192 bytes)
        Count and timestamp logging messages: disabled
        Persistent logging: disabled
    No active filter modules.
        Trap logging: level informational, 74 message lines logged
            Logging Source-Interface:       VRF Name: 
    ```

  - config log messsage
    - sequence of log messages from different devices able to help debug
    - adding timestamp, date stamp, msec, etc.

    ```text
    R1# config t
    R1(config)# exit
    R1#
    %SYS-5-CONFIG I: Configured from console by console
    ```


## Configuring Logging




## Conditional Debugging




## Troubleshoot Network Problems using Logging



