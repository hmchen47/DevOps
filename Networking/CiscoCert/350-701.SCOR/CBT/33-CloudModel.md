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


- References
  - [The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf)



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




## Plan for Cloud Deployment Models



