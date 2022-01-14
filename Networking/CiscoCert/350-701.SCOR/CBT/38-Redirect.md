# 38. Capture and Redirection Methods

Trainer: Keith Barker


## Introduction to Capture and Redirection Methods

- Learning goals
  - capture and redirect web traffic
  - policy based routing
  - WSA and WCCP


## Capture and Redirection Overview

- Capturing and redirecting web traffic
  - web security appliance (WAS) connected in inside zone to examine the web traffic
  - explicit forwarding
    - computer configured to forward web traffic to WSA
    - configured manually 
    - automatic: proxy auto-config file (PAC), group policy object (GPO)
  - capture and redirect web traffic
    - network devices in the path of network to capture and redirect the web traffic
    - options
      - PBR: policy base routing
      - WCCP: web cache communication protocol


## Policy Based Routing (PBR) Overview

- Policy based routing overview
  - via access control list (ACL)
  - route map: if TCP:443 then forward to WSA
  - applied to interfaces in default gateway


## PBR Configuration and Testing




## WCCP Overview and Planning




## WSA Configuration for WCCP




## IOS Configuration for WCCP




## Testing WCCP




## Traffic Redirection Summary



