# 19. Configure and Verify Cisco DHCP Snooping

Trainer: Keith Barker


## Introducing DHCP Snooping

- Learning goals
  - benefits of DHCP snooping
  - trusted and untrusted ports
  - enable switch to verify IP and MAC addresses before receiving frames

## Why is DHCP Snooping Needed

- Benefits of DHCP snooping
  - topology: assplied Trust port on g3/3
  - DHCP DORA process
    - Discover (broadcast): client sending out DHCP server request
    - Offer (unicast): DHCP server offerring service
    - Request (broadcast): client sending request for DHCP service
    - Acknowledgement (unicast): server replying to the request

    <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
      <a href="url" ismap target="_blank">
        <img style="margin: 0.1em;" height=200
          src   = "img/19-dhcpsnoop.png"
          alt   = "Example network topology of DHCP"
          title = "Example network topology of DHCP"
        >
      </a>
      <a href="https://www.skillsire.com/read-blog/432_how-dora-works-dora-process-in-details.html" ismap target="_blank">
        <img style="margin: 0.1em;" height=200
          src   = "https://3.bp.blogspot.com/-UDogKDJ2F18/VA4XshuOdzI/AAAAAAAAA8c/8AKzt8-W_w0/s1600/DHCP-DORA-jpg.jpg"
          alt   = "DHCP DORA process"
          title = "DHCP DORA process"
        >
      </a>
    </div>

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

- config DHCP snooping


## Adding Source Guard to a Switch




## Applying DHCP Snooping in Production




## Review of Configure and Verify Cisco DHCP Snooping




## Configure and Verify Cisco DHCP Snooping



