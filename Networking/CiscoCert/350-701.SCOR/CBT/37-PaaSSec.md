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




## Open Web Application Security Project Controls




## OWASP Protective Controls Continued




## Cisco Zero-Trust Architecture Overview




## Securing Workloads with Cisco Tetration




## Visibility with Cisco AppDynamics



