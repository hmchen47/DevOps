# 48. Configure a Switch for 802.1X

Trainer: Keith Barker


## Introduction to Switch Configuration for 802.1X

- Learnign goals
  - AAA config
  - port config


## Configure Global AAA Parameters

- Demo: config AAA on switch
  - `aaa authentication login default local`: use local user to authenticate, here `admin`
  - `address ipv4 192.168.1.105 auth-port 1812 acct-port 1813`: explicitly presents ports used
  - `automate-tester username testuser`: auto test periodically
  - `aaa server radius dynamic-author`: CoA
  - `dot1x system-auth-control`: allow to do 802.1z authentication
  - `ip device tracking`: tracking the alive
  
  ```text
  ! verify hardware & OS support
  SW# show version
  <...truncated...>
  Switch  Ports Model         SW Version    SW Image
  ------  ----- -----         ----------    ----------
  *    1  9     WS-C3560-8pc  15.0(2)SE11   C3560-IPSERVICESK9-M

  SW# show users
        Line    User    Host(s)   Idle      Location
  *  1  vty 0   admin   idle      00:00:00  192.168.1.151

  SW# show ssh
  Connection  Version Mode  Encryption  Hmac      State             Username
  0           2.0     IN    aes256-cbc  hmac-sha1 Session started   admin
  0           2.0     IN    aes256-cbc  hmac-sha1 Session started   admin

  SW# conf t
  SW(config)# username admin privi 15 secret Cisco!23

  ! config AAA
  SW(config)# aaa new-model
  SW(config)# aaa authentication login default local
  SW(config)# aaa authentication dot1x default group radius
  SW(config)# aaa authorization network default group radius
  SW(config)# aaa accounting dot1x default start-stop group radius

  ! config RADIUS server
  SW(config)# radius server Demo-ISE
  SW(config-radius-server)# address ipv4 192.168.1.105 auth-port 1812 acct-port 1813
  SW(config-radius-server)# key Cisco!23
  SW(config-radius-server)# automate-tester username testuser
  SW(config-radius-server)# exit

  ! group name for RADIUS servers
  SW(config)# aaa group server radius Demo-Group
  SW(config-sg-radius)# server name Demo-ISE
  SW(config-sg-radius)# exit

  ! retrial limit
  SW(config)# radius-server dead-criteria time 3 tries 3
  SW(config)# radius-server deadtime 15
  SW(config)# aaa server radius dynamic-author
  SW(config-local-da-radius)# client 192.168.1.133
  SW(config-local-da-radius)# server-key Cisco!23
  SW(config-local-da-radius)# exit

  ! allow to send vendor specific attribute
  SW(config)# ip radius source-interface g0/1
  SW(config)# radius-server vsa send authentication
  SW(config)# radius-server vsa send accounting

  ! allow tracking and 802.1x authn
  SW(config)# dot1x system-auth-control
  SW(config)# ip device tracking
  SW(config)# end

  SW# wr
  ```


## Port Configuration

- Demo: config port for 802.1X
  - `authentication host-mode [single-host | multi-auth | multi-domain | multi-host]`:
    - config interface switchport 802.1x host mode
    - `single-host`: default mode, allowing a single host to to be authenticated
    - `multi-auth`: multiple devices allowed to independently authenticate through the same port
    - `multi-domain`: allowing one host fro the data domain and one from voice domain, i.e., IP phone
    - `multi-host`: the first device to authenticate will open the port and all other devices able to use the port
  - `authentication violation [protect | replace | restrict | shutdown]`
    - `protect`: drop packets w/o syslog
    - `replace`: remove the current session and initiate authentication w/ the new host
    - `restrict`: generating syslog
    - `shutdown`: disable the port
  - `authentication open`: a fallback solution in lab env to allow traffic if failed
  - `dot1x pae authenticator`: enable 802.1x authentication on the port w/ default parameters
  - `authentication port-control auto`:
    - unauthorized state until authenticated w/ authentication server
    - authorized after authentication

    ```text
    SW# conf t
    SW(config)# vlan 10,20,30,80,999

    ! config almost all interfaces
    SW(config-vlan)# int range f0/1-8
    SW(config-if-range)# switchport host
    SW(config-if-range)# switchport access vlan 999

    ! authentication config
    SW(config-if-range)# authentication priority dot1x mab
    SW(config-if-range)# authentication order dot1x mab
    SW(config-if-range)# authentication event fail action next-method
    SW(config-if-range)# authentication event server dead action authorize vlan 10
    SW(config-if-range)# authentication event server alive action reinitialize
    SW(config-if-range)# authentication host-mode multi-domain
    SW(config-if-range)# authentication violation restrict
    SW(config-if-range)# authentication open

    ! MAB config
    SW(config-if-range)# mab
    SW(config-if-range)# dot1x pae authenticator
    SW(config-if-range)# dot1x timeout tx-period 5
    SW(config-if-range)# authentication port-control auto
    SW(config-if-range)# end

    SW# wr
    SW# show int status
    Port      Name      Status        VLan    Duplex  Speed  Type
    Fa0/1               connected     999     a-full   auto  10/100BaseTX
    Fa0/2               notconnected  999       auto   auto  10/100BaseTX
    Fa0/3               notconnected  999       auto   auto  10/100BaseTX
    <...truncated...>

    %AUTHMGR-5-START: Starting 'dot1x' for client ...
    %DOT1X-5-FAIL: Authentication failed for client ...
    %AUTHMGR-7-RESULT: Authentication result 'no-response' from 'dot1x' ...
    %AUTHMGR-7-FAILOVER: Failing over from 'dot1x' for client ...
    %AUTHMGR-5-START: Starting 'mab' for client ...
    %AUTHMGR-7-RESULT: Authentication result 'no-response' from 'mab' ...
    %AUTHMGR-7-FAILOVER: Failing over from 'mab' for client ...
    %AUTHMGR-7-NOMOREMETHODS: Exhausted all authentication methods for client ...
    ```



## Testing and Verifying

- Demo: verify 802.1X config
  - change settings on PC
    - Network adaptor > Properties > Authentication tab: Enable IEEE 802.1X authentication = Off > 'Ok' button
    - `authentication open` allowing the access though still authentication failed
      - a great way for stage testing
      - remove before put into production
  - verify on SW

    ```text
    SW# authentication session interface f0/1
                Interface:  FastEthernet0/1
              MAC Address:  5882.a899.5c81
               IP Address:  10.80.0.12
                User-Name:  bob
                   Status:  Authz Failed
    <...truncated...>

    SW# show int status
    Port      Name      Status        VLan    Duplex  Speed  Type
    Fa0/1               connected     999     a-full   auto  10/100BaseTX
    <...truncated...>
    ! still in vlan 999
    ```

  - modify the username and password
    - Network adaptor > Properties > Authentication tab: Enable IEEE 802.1X authentication = On
    - 'Advanced Settings' button > 802.1X settings > 'Save credentials' button
    - Save Credentials: username = b0b, password = `****` > 'Ok' button
  - verify msgs on SW

    ```text
    %AUTHMGR-5-START: Starting 'dot1x' for client ...
    %DOT1X-5-SUCCESS: Authentication successful for client ...
    %AUTHMGR-7-RESULT: Authentication result 'success' from 'dot1x' ...
    %AUTHMGR-5-VLANASSIGN: VLAN 80 to Interface Fa0/1 ...
    %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan80,change state to up
    %AUTHMGR-5-SUCCESS: Authorizarion succeeded for client ...

    SW# authentication session interface f0/1
                Interface:  FastEthernet0/1
              MAC Address:  5882.a899.5c81
               IP Address:  10.80.0.10
                User-Name:  bob
                   Status:  Authz Success
                    <...truncated...>
                  ACS ACL:  xACSACLx-IP-NOICMP-TELNET-5f152814
                    <..truncated...>
    Runnable method list:
            Method    State
            dot1x     Authc Success
            mab       Failed over

    SW# show access-list
    Extended IP access list AUth-Default-ACL-OPEN
        10 permit ip any any (77 matches)
    Extended IP access list xACSACLx-IP-NOICMP-TELNET-5f152814 (per-user)
        10 deny icmp any any
        20 deny tcp any any eq telnet

    SW# show vlan brief
    VLAN Name           Status    Ports
    ---- -------------- --------- -----------------------------
    1    default        active    
    10   VLAN0010       active    
    20   VLAN0020       active
    30   VLAN0030       active
    80   VLAN0040       active    Fa0/1
    999  VLAN0999       active    Fa0/2, ..., Fa0/8
    <...truncated...>

    SW# show int status
    Port      Name      Status        VLan    Duplex  Speed  Type
    Fa0/1               connected     80      a-full   auto  10/100BaseTX
    <...truncated...>
    ```

  - verify RADIUS log on ISE
    - Operations tab > RADIUS > Live Logs
    - the 1st entry - Identity = bob, Status = Session > 'Detail' icon
    - Overview: Username = bob, Authentication Policy = Our-Site1-Switch-Policy-Set>>Our-auth-dot1x, Authorization Policy = Our-Site1-Switch-Policy-Set>>ISE-OPS, Authorization Result = ISE-Operations



## Switch Configuration Summary

- Summary
  - config AAA
  - config port




