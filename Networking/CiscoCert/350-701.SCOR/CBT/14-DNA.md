# 14. DNA Center Foundations

Trainer: Knox Hutchinson


## Introducing DNA Center

- Learning goals
  - DNA center
  - Workflows
  - DNA center API


## What DNA Center Does

- DNA center overview
  - a new SDN solution
  - targeting at large enterprise
  - goal: simplify how to deploy, operate, and optimize a network infrastructure


- DNA software architecture
  - intent-based networking
  - example: group A members not allowed to communicated w/ group B members
  - intent-base infrastructure:
    - wireless access, switch, router, extended nodes
    - these devices capable of deploying business intent
    - running on IOS-XE, in general, Catalyst 9K devices
  - systems
    - DNA center appliance, standalone appliance
    - interacting w/ users
    - redundancy: 3x minimum
    - working closely w/ ISE, an AD like + network devices info
    - able to integrate w/ IPAM solution, IP addressing and services of network devices
  - platforms: APIs
    - assurance: enabling every point on the network to become a sensor, sending continuous streaming telemetry on application performance and user connectivity in real time
    - ML/AI feature to identify suspicious or abnormal issues
    - historical view and search for issues

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" width=300
        src   = "img/14-dna.png"
        alt   = "Cisco DNA SDN solution"
        title = "Cisco DNA SDN solution"
      >
    </a>
    <a href="https://bit.ly/3zhdcqH" ismap target="_blank">
      <img style="margin: 0.1em;" width=400
        src   = "https://bit.ly/3mJ1KPd"
        alt   = "Cisco DNA Center"
        title = "Cisco DNA Center"
      >
    </a>
  </div>



## What an SD-Access Fabric Does

- SD-access fabric overview
  - deploying intent, e.g., 
    - Group A users not allowing to access Group B users (bi-directional)
    - Group B permits to access servers in Group C
  - DNA center implements the intent across the entire network
  - the deployment based on SD-access
  - macro-segmentation: separting the whole campus based on the virtual networks
  - micro-segmentation
    - more granuar segmentation within a virtual network
    - multiple groups existed within a virtual network
    - policies existed within a virtual network
    - example: IT VN containing of Domain Admin, HelpDesk, Payroll servers
    - HelpDesk unable to access Payroll servers but Domain Admin able to 


- Example: 3 buildings
  - Bldg A, B, and C having 2 floors
  - Bldg A 1st fl w/ Group A while 2nd fl w/ Group B
  - Group A users accessing network w/ 802.1x via username and password
  - ISE handling the access authentication and passing the permission to DNA center
  - DNA center based on Group A users' privilege and placing them into a virtual network
  - the virtual network fully functional and completely isolated from other networks
  - Group B users accessing the network and placing into different virtual network
  - VRFs used to achieve the purpose
    - similar to VLAN
    - a layer 3 routing technology
    - users in different VRF isolated from each other
  - Group A members able to migrate or roam to any part of campus but still maintaining the same IP address and participating in the same virtual network $\to$ using LISP and VXLAN
  - same for Group B members


- Example: macro-segmentation w/ DNA center
  - Cisco DNA center: tabs - DESIGN, POLICY, PROVISION, ASSURE, PLATFORM
  - POLICY tab > subtabs - Cgroup-Based Access Control, IP Based Access Control, Application, Traffic Copy, Virtual Network
  - Virtual Network subtab: folders - DEFAULT_VN, INFRA_VN, HR+VN, IT_VN, IoT_VN > HR_VN folder 
  - Create or Modify Virtual Network by selecting Available Scalable Group > tabs - Available Scalable Groups (able to sync Group Names form ISE), Groups in the Virtual Networks


- Example: micro-segmentation w/ DNA center
  - Group Based Access Control: Policies, Scalable Groups, Access Groups > Policies
  - Policies: MiniMap - grid cells w/ Source & Destination as vertical and horizontal axes (Groups)
    - icons: Filter, Deploy, Refresh
    - actions: Permit, Deny, Custom, Default
    - hover anc click on a cell > Change Contract
    - Create Policy: Policy Status = Enabled; Contract = Change Contract > 'Change Contract' link
    - Change Contract: fields - Name, Description, Policies Referencing > click on the selected entry, e.g., Deny IP, Deny_IP_log, Permit IP, Permit_IP_log, AllowWeb, AllowDHCPDNS, DenyRemoteService



## The Four Workflows of DNA Center




## The DNA Center Platform APIs




## Summarizing DNA Center



