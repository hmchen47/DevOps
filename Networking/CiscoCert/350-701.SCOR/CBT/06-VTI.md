# 06. Cisco Point-To-Point GRE over IPsec VPNs

Trainer: Keith Barker


## Introduction to P2P GRE over IPsec VPNs

- Learning goal
  - describe the configuration and verification of Cisco Remote Access VPNs
  - describe the use of AnyConnect
  - demo the configuration and verification of Cisco Remote Access VPNs
  - demo the use of AnyConnect


## Overview of GRE over IPsec VPNs

- Issues of IPsec tunnel
  - originally designed for site-to-site IPsec VPN
  - no logical IP address w/ S2S IPsec tunnel
  - not supporting broadcast and multicast
  - unable to use routing protocols


- Generic Routing Encapsulation (GRE)
  - a protocol for encapsulating data packets to set up a direct network connection
  - creating GRE tunnel to enable
    - network address space associated to the tunnel
    - carrying other protocols other than IP only
    - broadcast and multicast w/ the address space
    - running routing protocols
  - packet format

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
        onclick= "window.open('https://ipcisco.com/lesson/gre-tunnel-overview-ccnp/')"
        src    = "https://ipcisco.com/wp-content/uploads/gre-header-1.jpg"
        alt    = "GRE Header"
        title  = "GRE Header"
      />
    </figure>

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://blog.51sec.org/2016/10/cisco-ios-router-configuration-ipsec.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=160
        src   = "https://thenetworkology.files.wordpress.com/2013/07/ipsec-over-gre.png"
        alt   = "IpSec ove GRE"
        title = "IpSec ove GRE"
      >
    </a>
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=160
        src   = "https://thenetworkology.files.wordpress.com/2013/07/gre-over-ipsec2.png"
        alt   = "GRE ove IPsec"
        title = "GRE ove IPsec"
      >
    </a>
  </div>

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="http://blog.51sec.org/2016/10/cisco-ios-router-configuration-ipsec.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=110
        src   = "https://www.firewall.cx/images/stories/gre-ipsec-tunnel-transport-1.gif"
        alt   = "IpSec ove GRE packet format"
        title = "IpSec ove GRE packet format"
      >
    </a>
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=110
        src   = "https://www.firewall.cx/images/stories/gre-ipsec-tunnel-transport-2.gif"
        alt   = "GRE ove IPsec packet format"
        title = "GRE ove IPsec packet format"
      >
    </a>
  </div>



## P2P GRE Tunnel Design




## P2P GRE Tunnel Implementation




## P2P GRE Tunnel Verification




## IPsec Tunnel Protection Design




## IPsec Virtual Tunnel Interface Configuration




## IPsec Static VTI Verification





