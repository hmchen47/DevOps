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





## Testing and Verifying





## Switch Configuration Summary




