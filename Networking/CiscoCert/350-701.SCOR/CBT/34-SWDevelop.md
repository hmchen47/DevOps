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




## Plan for DevOps




## Plan for DevSecOps



