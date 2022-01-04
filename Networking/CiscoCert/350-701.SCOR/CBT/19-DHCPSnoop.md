# 19. Configure and Verify Cisco DHCP Snooping

Trainer: Keith Barker


## Introducing DHCP Snooping

- Learning goals
  - benefits of DHCP snooping
  - trusted and untrusted ports
  - enable switch to verify IP and MAC addresses before receiving frames

## Why is DHCP Snooping Needed

- DHCP DORA process
  - Discover (broadcast): client sending out DHCP server request
  - Offer (unicast): DHCP server offerring service
  - Request (broadcast): client sending request for DHCP service
  - Acknowledgement (unicast): server replying to the request


- DHCP snooping
  - config to accept DHCP type messages on switch
  - config DHCP service on Vlan 30
  - L2 switch blocking unauthorized DHCP servers from distributing IP addresses to clients
  - port categories
    - truested:
      - a.k.a Trusted Source or Trusted interface
      - DHCP server messages trusted
    - untrusted
      - a.k.a Untrusted Source or Untrusted interface
      - DHCP server messages not trusted
      - default setting
  - router w/o DHCP snooping feature
  - DHCP server messages w/ DHCP Option 82 - Agent Information Option


## The Recipe for DHCP Snooping

- Commands for DHCP snooping
  - enable DHCP snooping: `SW(config)# ip dhcp snooping`
  - enable DHCP snooping on a particular VLAN: `SW(config)# ip dhcp snooping vlan 20`
  - confing a trusted port: `SW(config-if)# ip dhcp snoop trust`
  - option 82 not allowed w/ `SW(config)# no ip dhcp snooping info option`



## Building and Implementing DHCP Snooping in PT

- Demo: config DHCP snooping

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('page')"
      src    = "img/19-dhcpdemo.png"
      alt    = "Demo network topology for DHCP snooping"
      title  = "Demo network topology for DHCP snooping"
    />
  </figure>

  ```bash
  SW# show vlan brief
  ! all ports on native vlan

  SW# conf t
  SW(config)# ip dhcp snooping
  
  SW(config)# do show ip dhcp snooping
  DHCP snooping is configured on the following VLANs:
  none
  Insertion of option 82 is enabled
  Option 82 on untrusted port is not allowed
  Verification of hwaddr field is enabled
  Interface         Trusted   Rate Limited (pps)
  ----------------  -------   ------------------

  SW(config)# ip dhcp snooping vlan 1
  SW(config)# do show ip dhcp snooping
  Switch DHCP snooping is enabled
  DHCP snooping is configured on the following VLANs:
  1
  Insertion of option 82 is enabled
  Option 82 on untrusted port is not allowed
  Verification of hwaddr field is enabled
  Interface         Trusted   Rate Limited (pps)
  ----------------  -------   ------------------

  SW(config)# no ip dhcp snooping information option
  SW(config)# do show ip dhcp snooping
  Switch DHCP snooping is enabled
  DHCP snooping is configured on the following VLANs:
  1
  Insertion of option 82 is disabled
  Option 82 on untrusted port is not allowed
  Verification of hwaddr field is enabled
  Interface         Trusted   Rate Limited (pps)
  ----------------  -------   ------------------

  SW(config)# int f0/1
  SW(config-if)# ip dhcp snooping trust
  SW(config)# do show ip dhcp snooping
  Switch DHCP snooping is enabled
  DHCP snooping is configured on the following VLANs:
  1
  Insertion of option 82 is disabled
  Option 82 on untrusted port is not allowed
  Verification of hwaddr field is enabled
  Interface         Trusted   Rate Limited (pps)
  ----------------  -------   ------------------
  FastEthernet0/1   yes       unlimited
  ```

- Demo: verify DHCP operations
  - packet tracer to conduct the demo
  - bootup PC1 and observe interfaces connected to DHCP Good and DHCP Bad
  - check IP address of PC1 & PC2 $\gets$ both from DHCP Good server

  ```bash
  SW# show ip dhcp binding
  MacAddress          IpAddress     Lease (sec)   Type
  ----------          ------------  -----------   -------
  00:D0:FF:B1:3D:16   10.16.20.2    86400         dhcp-snooping
  00:DC:CF:61:E3:90   10.16.20.3    86400         dhcp-snooping
  Total number of bindings: 2
  ```



## Adding Source Guard to a Switch




## Applying DHCP Snooping in Production




## Review of Configure and Verify Cisco DHCP Snooping




## Configure and Verify Cisco DHCP Snooping



