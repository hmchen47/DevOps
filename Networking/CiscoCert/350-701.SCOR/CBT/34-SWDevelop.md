# 34. Planning for Software Development Methodologies

Trainer: Bart Castle



## Software and App Development Methodologies

- Software development methodologies
  - waterfall
  - agile
  - CI/CD
  - DevOps
  - DevSecOps


## Plan for Waterfall Method

- Software development lifecycle (SDLC)
  - planning
  - define requirements
  - design & prototyping
  - software development
  - testing
  - deployment
  - operations & maintenance


- Waterfall method overview
  - linear approach: move to next step until the current one completed
  - any change in the cycle $\to$ back to the requirements
  - five basic steps
    - requirements
      - stakeholder createing demand
      - demand translated into requirements
      - deliverables:
        - document to capture requirements
        - context: use cases, etc. to linerate the requirements
    - design
      - creating specifications according requirements
      - aspects of specs
        - physical - components, e.g., CPU, memory, network, and storage
        - logical - relations btw components and how to put them together
    - implementation
      - coding according specs
      - unit test
    - verification
      - testing: out of development environment
      - sign off to accept for release
    - maintenance
      - operating
      - measured w/ SLAs or metrics in requirements
  - disadvantages
    - ridgid: any change back to the begining of the procedure
    - long development time



## Plan for Lean and Agile Methods

- ITIL Services Lifecycle
  - Service Strategy
  - Service Design
  - Service Transition
  - Service Operation
  - Continuous Service Improvement

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://www.helpsystems.com/solutions/optimization/itil-version-3" ismap target="_blank">
      <img style="margin: 0.1em;" height=250
        src   = "img/34-itilv1.png"
        alt   = "ITIL Lifecycle v1"
        title = "ITIL Lifecycle v1"
      >
    </a>&nbsp;&nbsp;
    <a href="https://pdca.edchen.org/itil-v3-0-framework-illustrated/" ismap target="_blank">
      <img style="margin: 0.1em;" height=250
        src   = "img/34-itilv3.png"
        alt   = "ITIL Lifecycle v3"
        title = "ITIL Lifecycle v3"
      >
    </a>
  </div>


- Agile/Lean method
  - dynamic approach to adopt changes
  - ITIL: a service management framework
    - small changes
    - feed feedback
  - waterfall still valid but embedded and iterated
  - principles
    - <span style="color: cyan; font-weight: bold;">individual & interactions</span> over process and tools
    - <span style="color: cyan; font-weight: bold;">working software</span> over comprehensive docs
    - <span style="color: cyan; font-weight: bold;">responding to change</span> over following a plan
    - <span style="color: cyan; font-weight: bold;">customer collaboration</span> over contract negotiation
  - feedback from customer resulting in software changes


## Plan for Kanban and Scrum Teams

- Kanban and Scrum overview
  - reslation:
    - lean: business level
    - agile: IT level
    - kanban & scrum: team level
    - extreme programming: developer level
  - kanban - visualization
    - dynamic
    - timeline flex
    - no roles
  - scrum
    - sprint: a week in general but depend on nature of project
    - plan: ready to action
    - implement
    - deliver
  - extreme programming



## Continuous Integration, Deployment, and Delivery

- CI/CD overview
  - major components: source control, build, test, and deploy
  - source control
    - commit: saving source code
    - versioning: history
    - branch: variation
    - merge: combination back to original flow
    - pull request: validation & review
  - build
    - components of applications: general shared library, application code itself, 3rd party components
    - compile: generate executable
    - package: bundle required components together, container
  - test
    - interacting w/ other system, e.g., web client
    - test agents: automatic as much as possible
  - deploy:
    - deliverable: deliver the component to production environment
    - probably part of the larger components as input of anther test and deploy
  - combining different software components probably forming another thread of test and deploy


## Understand CICD Pipelines in Action

- CI/CD demo w/ AWS
  - Cloudformation
    - Infrastructure-as-a-Code
    - model, provision, and manage AWS and third-party resources
    - users creating a template that describes all the AWS resources that you want
    - CloudFormation taking care of provisioning and configuring those resources for you
  - Cloudformation template
    - [original](https://s3.us-west-2.amazonaws.com/cloudformation-templates-us-west-2/AutoScalingMultiAZWithNotifications.template)
    - [local version](src/34-AutoScalingMultiAZWithNotifications.templat)

    ```json
    {
      "AWSTemplateFormatVersion" : "2010-09-09",

      "Description" : "AWS CloudFormation Sample Template AutoScalingMultiAZWithNotifications: Create a multi-az, load balanced and Auto Scaled sample web site running on an Apache Web Serever. The application is configured to span all Availability Zones in the region and is Auto-Scaled based on the CPU utilization of the web servers. Notifications will be sent to the operator email address on scaling events. The instances are load balanced with a simple health check against the default web page. **WARNING** This template creates one or more Amazon EC2 instances and an Application Load Balancer. You will be billed for the AWS resources used if you create a stack from this template.",

      "Parameters" : {

        "VpcId" : { 
          "Type" : "AWS::EC2::VPC::Id",
          "Description" : "VpcId of your existing Virtual Private Cloud (VPC)",
          "ConstraintDescription" : "must be the VPC Id of an existing Virtual Private Cloud."
        },

        "Subnets" : {
          "Type" : "List<AWS::EC2::Subnet::Id>",
          "Description" : "The list of SubnetIds in your Virtual Private Cloud (VPC)",
          "ConstraintDescription" : "must be a list of at least two existing subnets associated with at least two different availability zones. They should be residing in the selected Virtual Private Cloud."
        },
      ...
    }
    ```

  - change code and validate w/ `cfn-lint`
    - `cfn-lint`: [AWS CloudFormation Linter](https://github.com/aws-cloudformation/cfn-lint)
    - correct code and validate again
  - source control w/ GitHub
    - commit code to repository: `git commit -a`
    - push to repository: `git push --set-upstream origin demoBranch`
    - 'compare and pull request' in repository > comments about the change > 'Create Pull Request' button
  - test and deploy
    - validaton integrating w/ GitHub
    - after validation > 'Merge pull request' button > confirm merge


## Plan for DevOps

- DevOps overview
  - traditional:
    - silos: business, developer, operations teams
    - developer -> operations -> business -> developer -> ...
    - gaps btw languages, tools, culture, etc.
  - DevOps
    - culture
      - developer adopting changes
      - operations providing stability
      - breaking down silos
      - business team pulling inputs into the collaboration team
    - process
    - tools
    - feedback
  - principle: automation on development and control


## Plan for DevSecOps

- DevSecOps overview
  - applying security control, principle, and expection to the highly automatic system
  - principles: IaaC, control, testing
  - Infrastructure as a Code:
    - template to computer resources
    - management
    - source code
      - admin user account
      - policy
      - firewall rules, e.g. control only SSH
    - how to translate the source code into actions
  - control
    - notification, mitigation
    - automic the process
  - fuzzing testing
    - randomizing the testing
    - injecting possible bad data to realize what happen to system 



