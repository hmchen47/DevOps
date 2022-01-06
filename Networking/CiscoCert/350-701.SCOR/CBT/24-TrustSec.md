# 24. Configure Cisco TrustSec

Trainer: Keith Barker


## Introduction to TrustSec

- Learning goals
  - TrustSec
  - group ACLs
  - TrustSec policies
  - config TrustSec
  - verify TrustSec
  - SGT eXchange protocol (SXP)


## TrustSec Overview

- TrustSec overview
  - Device A connected to SW-A w/ MAB or 802.1x
  - identity of user authenticated via ISE
  - security group
    - used for authentication
    - a logical group w/ members
  - security group associated w/ a security group tag (SGT), a number
  - example: 3 security groups
    - ISE-admin w/ STG = 18
    - ISE-Ops w/ STG = 19
    - PCB-PCs w/ tag = 20
  - frames w/ a security group traversing across network including STG
  - able to control frames btw groups and within group
  - ISE able to implement policies btw security groups

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="url" ismap target="_blank">
      <img style="margin: 0.1em;" height=200
        src    = "img/24-trustsec.png"
        alt    = "Example network for TrustSec"
        title  = "Example network for TrustSec"
      >
    </a>
    <a href="https://www.routexp.com/2019/05/introduction-to-secure-group-tagging-sgt.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=160
        src   = "https://bit.ly/32Nfp1j"
        alt   = "Secure Group Tagging"
        title = "Secure Group Tagging"
      >
    </a>
  </div>



## TrustSec Security Groups

- Demo: create TrustSec security groups on ISE
  - Work Centers tab > TrustSec: subtabs - Overview, Components, TrustSec Policy, Policy Sets, SXP, Troubleshoot, Reports, Settings
  - Components subtab > folders - Security Groups, IP SGT Static Mapping, Security Group ACLs, Network Devices, TrustSec Servers > Security Groups
  - Security Groups: fields - Icon, Name, SGT (Dec/Hex), Description; Icons - Edit, Add, Import, Export, Trash, Push, Verify Deploy
    - entry: Name = Auditors, SGT = 9
    - entry: Name = BYOD, SGT = 15
  - 'Add' icon > Security Groups List > New Security Group: Name = ISE_Admin, SGT = 16 > 'Submit' button
  - 'Add' icon > Security Groups List > New Security Group: Name = ISE_Ops, ST = 17 > 'Submit' button
  - 'Add' icon > Security Groups List > New Security Group: Name = PCB_PCs, ST = 18 > 'Submit' button


## Security Group ACLs




## TrustSec Policies




## Configure Network Devices for TrustSec




## ISE and NAD TrustSec Integration




## Verify TrustSec




## SGT eXchange Protocol (SXP)



