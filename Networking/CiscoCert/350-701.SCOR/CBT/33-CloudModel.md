# 33. Cloud Service and Deployment Models

Trainer: Bart Castle


## Planning for loud Services

- Essential characteristics of could computing service by NIST
  - on-demand self-seervice: via API
  - broad network access
  - resource pooling: shared
  - rapid elasticity: vertical and horizontal scaling 
  - measured service: SLA, QoS


- Concerns of cloud services
  - CIA
    - confidentiality: who access the info
    - integrity: accuracy of info
    - availability: info available when needed
  - control
    - protective
    - detective
    - reactive


- Cloud Service model
  - tradeoff btw responsibility and control
  - different models w/ different separation of boundaries for responsibility and control 
  - management layer btw customer and provider
    - interface for customer to instruct provider what to perform
    - tools: command line tool, system development kit (SDK), management interface, etc.
  - layers of administrative control
    - control what customer implemented
    - control to instruct provider how to implement
  - right level of documentation required to comply w/ the auditorial requirement and government expectation

  <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('page')"
      src    = "img/33-cloudsrv.png"
      alt    = "Cloud service model"
      title  = "Cloud service model"
    />
  </figure>



## Plan for Infrastructure As A Service

- Infrastructure model
  - existing virtualized services: virtual machines, virtual storage, virtual networks, and virtualized containers for applications, etc.
  - security concern
  - cloud service model
    - provider: physical, servers / storage, hypervisor
    - customer: virtual network, operating system, runtime / middleware, applications, data and people



## Plan for Platform As A Service

- Platform model
  - cloud service provider
    - provider: physical network, servers / storage, hypervisor, virtual network, operating system, runtime / middleware
    - customer: applications, data and people
  - focusing on what the applications do
  - container:
    - data and application
    - docker, kubernetes, etc.
    - key concerns: platform diagnostic, portability, encapsulation
  - protability considerations
    - how to make libraries portable
    - how to make application portable w/ libraries
    - how to make interfaces working w/ service providers in terms of management perspective
  - reusable components
    - building blocks
    - APIs interacting w/ different layers offered by service provider
    - principles of web services, micro services, or container


## Plan for Software As A Service

- Software model
  - cloud service provider
    - provider: physical network, servers / storage, hypervisor, virtual network, operating system, runtime / middleware, applications
    - customer: data, people 
  - recommendation: starting w/ SaaS
  - security concerns
    - data: encryption
    - people: identity and access management
  - providers offerring high degree of isolation and separation btw different components and customers


## Plan for Cloud Deployment Models

- Deployment models
  - [The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf), NIST 800-145
  - private cloud
    - exclusive use by <span style="color: cyan; font-wight: bold;">a single organization</span>
    - owned, managed, and operated by the organization, a 3rd party, or some combination of them
    - existing on or off premises
  - community cloud
    - exclusive use by a specific community of consumers from organizations that have <span style="color: cyan; font-wight: bold;">shared concerns</span>, including mission, security requirements, policy, and compliance considerations
    - owned, managed, and operated by one of more of the organizations in the community, a 3rd party, or some combination of them
    - existing on or off premises
  - public cloud
    - open use by <span style="color: cyan; font-wight: bold;">the general public,/span>
    - owned, managed, and operated by a business, academic, or government organization, or some combination of them
    - existing <span style="color: cyan; font-wight: bold;">on the premises</span> of the cloud provider
  - hybrid cloud
    - a.k.a. multicloud, mixed cloud
    - a composition of two or more distinct cloud infrastructure (private, community, or public)
    - remaining unique entities but bound together by standardized or propriety technology that enables data and application portability
  
- Security of cloud service
  - security concerns
    - isolation
    - asset ownership
    - exclusively control
  - highest level of security w/ private cloud
    - better exclusively control
    - better granularity
    - higher QoS
  - tradoff: more customer control
    - more exclusivity
    - less resource sharing
    - less value proposition improved
  - level of security
    - private cloud: maximum control and exclusivity
    - public cloud: general public availability, hosted by a service provider
    - community cloud: shared or commion set of interest
    - hybrid cloud: multiple locations to deploy infrastructure
  - value:
    - SaaS > PaaS > IaaS
    - public & community > hybrid > private



