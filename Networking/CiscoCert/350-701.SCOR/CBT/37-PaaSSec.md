# 37. Planning for and Securing Cloud Platform-as-a-Service

Trainer: Bart Castle


## Securing Cloud Platform-as-a-Service

- PaaS security
  - container
  - orchestrating containers
  - OWASP
  - micros-segmentation
  - Tetration
  - AppDynamic



## Plan for Containers

- Container overview
  - efficiency, sharing resources, and abstraction
  - software parts of virtual machines: OS and Apps
  - hardware parts of virtual machines: computing resources, including CPU, memory, storage, and network
  - focused on software parts, in particular, Apps
  - abstraction layer providing shared libraries
  - only focusing on Apps
  - components in container environment
    - container (image), e.g., docker
    - registry: a safe structured place to store images
    - orchestration
  - cloud service provider offering all 3 components


## Secure Container Images and Registries

- Securing container images and registries
  - container image: OS image + library image + apps image
  - able to be a source control mechanism
  - docker
    - a docker file or docker-compose
    - including installation of OS and software, configuration, network
  - container **checkin** to registry
  - registry:
    - a structure storage location similar to DB
    - info: what the image is, who able to use, security, encryption, control, and authentication
    - highly secured
    


- AWS Lambda
  - AWS container
  - functions:
    - capability of the container
    - runtime requirements
  - developers adding their own code


- Demo: AWS container
  - a Lambda in YAML or JSON formate, e.g., YAML file

    ```yaml
    AWSTemplateFormatVersion: '2010-09-09'
    Description: Simple calculator app
    Transform: AWS::Serverless-2016-10-31
    Resource:
      calcFunction:
        Type: AWS::Serverless::Function
        Properties:
          Handler: src/handlers/calc.handler
          Runtime: nodejs12.x
          MemorySize: 128
          Timeout: 100
          Description: A Lambda function which performs some calculations
    ```

  - CLI exec: `sam local invoke -e ./event/calcEvent.json`
    - pulling image from amazon or local to run `nodejs12.x`
    - display info about he container, execution summary, and result
  

- Resources:
  - [Docker repository](https://hub.docker.com/)
  - [Amazon ECS Clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html)



## Orchestrating Containers

- Orchestrating containers
  - microservice: large apps abel to break into small components
  - different containsers running different tasks
  - scaleing up certain task w/ more same function containers
  - level of scaling
    - container
    - host
  - tools to corordinating these containers: docker swam, apache mesos, kubernets
  - components of Kubernetes: a cluster
    - master node (control plane)
      - admin
      - APIs
      - receiving calls
    - node:
      - a worker or a minor
      - a machine where containers (workloads) deployed
      - running a container `runtime` (runtime system - implementing portions of an execution mode)
      - below-mentioned components for communication w/ the primary for network config of these containers
    - pod
      - the basic scheduling unit
      - consisting of one or more containers
      - co-located on the same node
      - assigning a unique IP address

    <figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
        onclick= "window.open('https://en.wikipedia.org/wiki/Kubernetes')"
        src    = "https://upload.wikimedia.org/wikipedia/commons/b/be/Kubernetes.png"
        alt    = "Kubernetes architecture"
        title  = "Kubernetes architecture"
      />
    </figure>

  - AWS Fargate
    - a complete managed container orchestrating environment
    - AWS handling all nodes, pods, etc.
    - developers only focusing on code


## Open Web Application Security Project Controls

- [OWASP proactive controls - 2018](https://owasp.org/www-project-proactive-controls/)
  - define security requirement
    - documentation
    - risk sensitivity = asset + threats + vulnerabilities
    - use cases = stories
  - security frameworks and libraries
    - library inventory, e.g., AWS SDKs
    - monitoring, e.g., OpenID/SAML
  - secure database access
    - data in transit
    - input: what to send and how well validated
    - credentials and/or connector
  - encode and escape data
    - sending data to the next component or DB
    - syntax: structure of the data, e.g., CSV, XML, JSON, SQL
    - control characters: interpret correctly, e.g., `/`, `\`, etc.
  - validate all inputs
    - looking for 'good' patterns
    - looking for 'bad' patterns
  - implement digital identity
    - authn/authz
    - 1\. password
    - 2\. MFA
    - 3\. token
  - enforce access control
    - permissions
    - data implication: RW, RO
    - force validation
    - deny by default
    - no hard coding
    - log everything" logging for avilability
  - protect data everywhere
    - in-use
    - in-transit: SSH, SSL, TLS
    - at-rest: encryption key management
  - security logging and monitoring
    - visibility
    - log processsing: SIEM
    - monitoring:
      - KPI, KHI
      - agent: push to API
  - handle all errors and exceptions
    - expect failure
    - example: boolean value (true/false) $\neq$ 0



## Cisco Zero-Trust Architecture Overview

- Zero-trust architecture
  - key components: user/application authentication, device authentication, and trust
  - principles: establish trust, enforce zero-trust, verify through environment
  - establishing trust
    - endpoint trust
    - security devices to built trust
  - enforcing zero-trust architecture
    - enterprise security policy
    - reactive control
  - verifying everywhere
    - enforcing all individual sessions
    - all devices in the network

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://www.crowdstrike.com/cybersecurity-101/zero-trust-security/" ismap target="_blank">
      <img style="margin: 0.1em;" height=200
        src   = "https://www.crowdstrike.com/wp-content/uploads/2020/04/nist-zero-trust-framework-1536x720.png"
        alt   = "NIST Zero-trust framework"
        title = "NIST Zero-trust framework"
      >
    </a>
    <a href="https://www.cisco.com/c/en_hk/products/security/zero-trust.html" ismap target="_blank">
      <img style="margin: 0.1em;" height=180
        src   = "https://bit.ly/3I2wpzj"
        alt   = "Cisco Zero Trust Security"
        title = "Cisco Zero Trust Security"
      >
    </a>
  </div>

- Cisco zero-trust architecture
  - a shift of network defenses toward a more comprehensive IT security model
  - allowing organizations to restrict access controls to networks, applications, and environment without sacrificing performance and user experience
  - trusting no one
  - workplace
    - SD-Access & SD-WAN components
    - enterprise networking tools
    - appliances interacting w/ cloud-based VMs
    - purpose: establishing trusts
  - workload
    - Tetration: analytic engine for detection and enforcement
    - detection (dependencies): agent/sensor installed in VMs, not only VMs but also processes and firewall in VMs
    - enforcement: policy and rules, container
  - workforce
    - Duo and AnyConnect
    - Duo: authn & authz
    - AnyConnect: encpoints


## Securing Workloads with Cisco Tetration

- Micro-segmentation
  - a network security technique enabling security architects to logically divide the data center into distinct security segments down to the individual workload level
  - defining security controls and deliver services for each unique segment
  - perimeter containing VM, server, host (containers)
  - perimeter as macro-segmentation
  - VM as micro-segmentation
  - preventing attackers or threats from spreading or moving laterally in data centers, clouds, or campus networks


- Workload security on Tetration
  - agent/sensor
    - monitoring: system utilization, applications
    - enforcing rules
    - Stealthwatch monitoring only on traffic but not deep inspection while Tetration does
  - Tetration
    - context of the traffic
    - integrated w/ ISE & ASA
    - machine learning


- Demo: Tetration
  - folders - VISIBILITY, SEGMENTATION, SECURITY, PERFORMANCE, DATA PLATFORM, ALERTS, MAINTENANCE
  - segmentation: tabs - Conversations, Clusters, Policies, Provided Services, App View
    - workplace
    - complication of system, traffic, identity
    - application dependency mapping
  - security: folders - dashboard, Vulnerabilities, Forensics Analysis, Lookout Annotiation
    - Dashboard: scope security score
    - Vulnerabilities: high profile problems



## Visibility with Cisco AppDynamics



