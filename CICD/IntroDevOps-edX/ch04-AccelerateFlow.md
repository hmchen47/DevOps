Chapter 4: The First Way - Accelerate Flow
==========================================

# Learning Objectives
+ Discuss the concept and goals of the First Way.
+ Explain the difference between shortening lead time and reducing bottlenecks.
+ Explain the difference between continuous integration, continuous delivery, and continuous deployments.
+ Discuss the eight principles of continuous delivery.
+ Explain the importance of everything being managed and controlled by source control.
+ Discuss the concepts of Infrastructure as Code and immutable infrastructure.
+ Discuss automated testing.
+ Explain the patterns for live deployments, otherwise called "zero downtime deployments".


# Section 1: Continuous Delivery Patterns and Practices
## Notes
+ The First Way = Continuous Delivery
    + continuous delivery patterns and practices
    + the deployment pipeline
    + creating consistency in the pipeline
    + automated testing
    + deployment strategies (zero downtime release)
+ Principle of the First Way
    + create automated and repeatable environments at each stage of th epipeline
    + apply automated testing at every stage of the pipeline
    + increase flow and shorten lead times
    + global optimization vs local optimization
+ Steps to Increase Value and Flow
    1. define value precisely from the perspective of the end customer
    2. identify the entire value stream for each product or product family and eliminate waste
    3. make the remaining value-creating steps flow
    4. design and provide what the customer wants only when the customer wants it
    5. pursue perfection
+ Termonologies:
    + __Continuous Integration__: the process of integrating components of a feature, application or service
    + __Continuous Delivery__: use continuous integration to create installable artifcats (packages) that can be deployed
    + __Continuous Deployment__: the process of deploying a feature, application or service to production
+ Continuous Delivery
    + the build phase
    + typically integrated by a code commit
    + typically builds asre done from trunk
    + the process happens every time someone commits code
    + code is compiled and libraries are built
    + builds trigger package, artifact and image creation
+ Principles of Continuous Delivery
    + depolying changes to production
    + release vs deploy
    + system, performance and load testing
    + fast deploys help learn faster
    + installation, configuration and orchestration

## Video
[video][vid1]

[vid1]: https://edx-video.net/LINLFS162016-V008900_DTH.mp4

## Recommended Resources
+ James Womack and Daniel Jones, [How to Root Out Waste and Pursue Perfection](https://hbr.org/1996/09/how-to-root-out-waste-and-pursue-perfection)
+ Jez Humble and David Farley, [Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912)
+ Thomas A. Limoncelli, [The Practice of Cloud System Administration: Designing and Operating Large Distributed Systems, Volume 2](https://www.amazon.com/Practice-Cloud-System-Administration-Distributed/dp/032194318X)
+ Jennifer Davis and Katherine Daniels, [Effective DevOps: Building a Culture of Collaboration, Affinity, and Tooling at Scale](https://www.amazon.com/Effective-DevOps-Building-Collaboration-Affinity/dp/1491926309)


# Section 2: The Deployment Pipeline
## Notes
+ The Deployment Pipeline
    + Visibility: all stages are visible to everyone responsible for delivery of the service
    + Feedback: designed "gates" to eliminate downstream defects
    + Continually Deploy: any patch, update or new feature can be automated for delivery, deploy and releaase
+ High Performaers: SDLC for everything
    ![diagram](./SDLC4Everyone.PNG)
+ DevOps Release Pipeline Overview
    ![diagram](https://pdn.pega.com/sites/pdn.pega.com/files/images/PRPC/articles/1272951/pipeline-overview-update-1-31-17.png)
+ DevOps & Tools 
    ![diagram](http://milindtech.com/wp-content/uploads/2016/02/DevOps-Milind-Tech-2.jpg)

## The Deployment Pipeline (Part I)
### Notes
+ Continuous Delivery Process

    ![diagram](https://upload.wikimedia.org/wikipedia/commons/7/74/Continuous_Delivery_process_diagram.png)
+ Service Delivery Platform Design Patterns

    ![diagram](http://dev2ops.org/wp-content/uploads/2012/09/Service-Delivery-Platform-Elements2-e1348178561602.png)
    + Build phase
        + source repository
        + Build console
    + Package Repository
        + Build artifacts
        + + Store & Retrieve
    + Deployment Phase
        + Pre-production (stage)
        + Production

### Video
[video][vid2]

[vid2]: https://edx-video.net/LINLFS16/LINLFS162016-V005500_DTH.mp4


### Recommended Resource
+ Tom Limoncelli, [The Practice of System and Network Administration](https://www.amazon.com/Practice-System-Network-Administration-Second/dp/0321492668)
+ Jez Humble and David Farley, [Continuous Delivery](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912)
+ Damon Edwards and John Willis, [Better, Faster AND Cheaper. How?](https://www.youtube.com/watch?v=j9fC4raB-bA)

## The Deployment Pipeline (Part II)
### Notes
+ Source Control
    + local: __Git__, Team Foundaton Server, Perforce
    + cloud: __GitHub__, Bit Bucket, GitLab
+ Bill Console:
    + __Jenkins__
    + __Travis CI__
    + Bamboo
    + Circle CI
    + Team City
    + Shippable
+ Reposiory Managers
    + __Nexus__ (Java)
    + __Docker Hub__
    + __Artifact__
    + __Docker Trust Registry__
    + Google container Registry
+ Operation Console
    + __Rundeck__
    + Asgard - Netflix
    + Marathon - Messo
    + Spainker - Netflix
    + Weave Scope
+ Automation
    + CFengine (Ruby)
    + Puppet (CFe3ngine extension)
    + Chef (CFEngine extension)
    + Ansible (YAML)
    + Docker Compose (YAML)
    + Cloud Foundation (Amazon)
    + TerraForm
+ Infrastructure Management
    + VMWare
    + Public Cloud: AWS, GCE, Azure
    + Private Cloud: OpenStack, CloudStack
    + Container: Doecker, rkt, LXC
    + Orchestration: Swarm, Messo, Kubernetes

### Video
[video][vid3]

[vid3]: https://edx-video.net/LINLFS16/LINLFS162016-V005600_DTH.mp4


### Recommended Resource
+ Damon Edwards, [what is a Service Delivery Platform?](https://vimeo.com/46125904)

## The Deployment Pipeline (Part III)
### Notes
+ Vagrant Concepts:
    + Host & Guest (Desktop & VMs)
    + Provider & Provisioner
    + Boxes (abstration for images)
    + vagrantfile (Ruby)
    + Synched Folders
+ Vagrant Commands: vagrant [cmd]
    + up
    + reload
    + suspend
    + resume
    + destory
    + halt
    + ssh

### Video
[video][vid4]

[vid4]: https://edx-video.net/LINLFS16/LINLFS162016-V005700_DTH.mp4


### Recommended Resource
+ Mitchell Hashimoto, [Vagrant: Up and Running](https://www.amazon.com/Vagrant-Up-Running-Mitchell-Hashimoto/dp/1449335837)


## The Deployment Pipeline (Part IV)
### Notes
+ Build Phase Example
    + update code from source control (if existing)
    + service is coded (if new)
    + run a local build in your developemnt enviroinment
    + service code is committed to the source repository
    + artifacts are tagged and packaged
    + packages are registered in a repository
+ Cimmit Phase
    + files are uploaded to the source repository
    + all source code should be working code
    + code should have full coverage unit code
    + committed source should not break the build
    + pre-sumbmit checks (bugs, lint, code styles)
    + automated trigger of the build stage
+ Build Phase
    + compling code
    + invoke build tools (ANT, Maven, Mercury, IVY, Make)
    + build time dependencies
    + creating and/or converting images
    + running funcational/unit tests
    + automated trigger of integration and acceptance testing
+ Packages/Artifacts
    + compiled executable
    + components
    + libraries
    + Tar's and/or compressed binaraies
+ Package/Artifact Repository
    + managing the distribution of packages or artifaccts
    + all packages/artifacts must be dependencies from source
    + cryptographically hashed or digitally signed
    + manages security access management
    + invoked vunlnerability scanning
    + provide usage reporting

### Video
[video][vid5]

[vid5]: https://edx-video.net/LINLFS162016-V006000_DTH.mp4


### Recommended Resource
+ Botchagalupe, [Immutable Delivery (The Agile Admin)](https://theagileadmin.com/2015/11/24/immutable-delivery/)


## The Deployment Pipeline (Part V)
### Notes
+ Deploy Phase
    + promotion
    + provisioning
    + installation
    + configuration
    + orchestration
+ Promotion - moving btw stages
    + candidate release are selected
    + versions are selected and worked
    + tagging strategies
    + multiple repostories strategies
+ Tagging Strategies
    + marked "Production"
    + marked "Latest"
    + pinning
+ Multiple Repositories Strategies
    + development
    + testing
    + production
+ Provisioning
    + Bare metal provisioning
    + Virtual image provisioning
    + Cloud provisioning
    + Container provisioning
+ Installation
    + Internally written installers
    + Before and after scripts
    + System level packages (RPM/YUM, DEB/APT)
+ Configuration Management (Non Immutable)
    + Install the service
    + Infrastructure as Code
    + Desired State Configuration
    + Convergence
    + CFEngine, Chef, Puppet, Ansible
+ Virtualization Sprawl: a phenomenon that occurs when the number of VMs on a network reaches a point where the administrator can no longer manage them effectively

### Video
[video][vid6]

[vid6]: https://edx-video.net/LINLFS16/LINLFS162016-V005900_DTH.mp4


# Section 3: Creating Consistency in the Pipeline
## Creating Consistency in the Pipeline (Part I)
### Notes
+ Continuous Delivery Anti-Patterns
    + incongruent testing and production environment
    + testing takes too long
    + manual regression and acceptance tests
    + high technical debt
    + slow and hard to change
    + hight MTTR
+ Consistent Pipeline Challenges
    + Snowflakes: server hugger, repeatable
    + Sprwal: strategy for image cataloging
    + Drift: out of sync
    + Documentation
+ Pets vs Cattle
+ Consistent Environments in all Stages
    + goal is to create consistent environments
    + all elements of the pipeline should be disposable and reproducible
    + all environment should look like production
    + decrease variability between elements in the pipeline
    + repeatability increases speed rebuilding environments
    + reduced erros related to inconsistence
    + increases security related to inconsistence
+ Version Control Everything
    + keep a history of all changes
    + can easy check differences between versions
    + can erstore and rebuild all elements
    + everything can be versioned and tagged
    + all changes ae visible and audited for everyone
    + changes can be automated
+ What should be in version control
    + application code
    + configuration scripts
    + configuration management DSL code
    + image build scripts
    + meta definitions
    + automated tests, test scripts nad test DSL code
    + documentation, procedures, release notes
    + templates
    + database schema abstration, DNS and firewall definitions
    + network definitions
+ Google's SysOps Death Squads
    + Only 2 Linux versions at any given time
    + rolled off old version as new version introduced
    + identify deprecated server versions 
    + help owner depreciate and/or pressure until marked done

### Video
[video][vid7]

[vid7]: https://edx-video.net/LINLFS162016-V006100_DTH.mp4


### Recommended Resources
+ Netflix - Jason Chan, [Real World Cloud Application Security](https://vimeo.com/54157394)
+ Randy Bias, [Pets vs. Cattle: The Elastic Cloud Story](http://cloudscaling.com/blog/cloud-computing/pets-vs-cattle-the-elastic-cloud-story/)


## Creating Consistency in the Pipeline (Part II)
### Notes
+ Why Order Matters
    + Divergence

        ![divergence](http://www.infrastructures.org/papers/turing/images/divergence.png)
    + Convergence

        ![convergence](http://www.infrastructures.org/papers/turing/images/convergence.png)
    + Congruence

        ![congruence](http://www.infrastructures.org/papers/turing/images/congruence.png)
+ Why Order Matetrs
    + Circular dependencies
    + Right Command Wrong Order
    + Right Package Wrong Order

### Video
[video][vid8]

[vid8]: https://edx-video.net/LINLFS162016-V006200_DTH.mp4


### Recommended Resources
+ Steve Traugott, [Why Order Matters: Turing Equivalence in Automated Systems Administration](http://www.infrastructures.org/papers/turing/turing.html)


## Creating Consistency in the Pipeline (Part III)
### Notes
+ Consistent Infrastructure
    + Bare Metal provisioning
    + Virtual machine provisioning
    + Cloud provisioning
    + Container provisioning
+ Bare Metal (BM) Provisioning
    + Products
        + kickstart
        + cobbler
        + FAI (Fully Automatic Installation)
        + Foremen
        + Razor
        + MAAS
        + Ironic
        + RackN - Digital Rebar
    + Characteristics
        + BM scripts or DSL in version control
        + BM scripts --> configuration management process
        + BM & CM tools integrated
+ Virtual Machine Provisioning
    + Virtual Machine
        + Type 1 Hypervisor (on top of BM): VMWare ESX/vSphere, XEN, HyperV
        + Type 2 Hypervisor (on top of OS): KVM, VMWare Workstation, Oracle VirtualBox, Xhyve (Hyperkit-Docker)
    + Characteristics:
        + VM images build scripts, meta and templates -< version control\
        + VM images reproducible from source
        + CM tools automate VM provisioning
        + Image strategies (Bake-large but fast vs Fry-small but slow)
    + Desktop VMs
        + Vagrant
        + Docker toolbox
        + Docker for Mac
        + Docker for Windows
+ Cloud Provisioning
    + Public Cloud (IaaS)
        + Amazon (AWS)
        + Google (GCE)
        + Microsoft (Azure)
        + Rackspace
        + Digital Ocean
    + Provate Cloud (IaaS)
        + Openstack
        + Cloudstack
        + VMWare vCloud
        + Microsoft (Azure)
    + Characteristics
        + Cloud image build scripts, meta and templates --> version control
        + Clould images reducible from source (version control)
        + CM tools automate cloud provisioning
        + Cloud-init/user-data/cloud-config file format
        + Image strategies (Bake vs Fry)

### Video
[video][vid9]

[vid9]: https://edx-video.net/LINLFS162016-V006300_DTH.mp4


### Recommended Resources
+ Rob Hirschfeld, [Digital Rebar Quick Start to K8s](https://www.youtube.com/watch?v=bn4LLNtPF6c)
+ Abe Hassan Blog, [baked servers vs fried servers](http://if.andonlyif.net/blog/2012/10/baked-servers-vs-fried-servers.html)
+ [Cloudinit](http://cloudinit.readthedocs.io/en/latest/)
+ [Cloudinit on RedHat](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux_OpenStack_Platform/4/html/End_User_Guide/user-data.html)


## Creating Consistency in the Pipeline (Part IV)
### Notes
+ Container Provisioing 
    + Types 
        + Type 1 Hypervisor
        + Type 2 Hypervisor
        + Linux Container
        
            ![diagram](https://image.slidesharecdn.com/realizinglinuxcontainerslxc-140311110026-phpapp02/95/realizing-linux-containers-lxc-4-638.jpg?cb=1394535785)
    + Products
        + Docker
        + rkt (Rocket)
        + LXD
        + LXC (Native Linux Conatiners)
        + Microsoft (ACS)
        + Google (GCS)
    + Characteristics
        + Container image build scripts, meta and templates --> version control
        + Container images reproducible from source
        + CM tools not used inside of a running container
        + Configuration files and meta shared by container host
        + Container works well w/ Immutable Delivery Models
    + Infrastructure image portability
        + conversions between different infrastructures
        + conversions between different stages in the pipeline
        + directory structures and shared files

### Video
[video][vid0]

[vid0]: https://edx-video.net/LINLFS162016-V006400_DTH.mp4


### Recommended Resources
+ IBM - Boden Russel, [Realizing Linux Container (LXC) - Building Blocks, Underpinning & Motivations](https://www.slideshare.net/BodenRussell/realizing-linux-containerslxc)


## Creating Consistency in the Pipeline (Part V)
### Notes
+ Consistently Operatiing System Environment Patterns
    + scripted environments
    + infrastructue as code
    + immutable infrastructure
    + immutable delivery
+ Scripted Environments
    + Pros
        + easier to build
        + lower learning curve
        + language consistency
        + easy to change
    + Cons
        + environment abstractions are harder to code
        + typically lower reusability
        + harder to provide data driven models
        + cloud cause inconsistent environments builds
        + no really self-documentaing
        + cloud lead to local improvements and not global
        + no really good testing interfaces
+ Interfrastructure as Code
    + Characteristics
        + Infrastructure primitives defind as DSL
        + highly parameterized
        + desired stated based
    + Principles
        + Moduality
        + Composibility
        + Extensibility
        + Flexibility
        + Repeatability
        + Declaration
        + Abstraction
        + Idempotence
        + Convergency
    + pros:
        + powerful abstraction DSLs
        + self documenting
        + high reusability code/modules
        + easy to provide data driven models
        + generally more consistent than scripted patterns
        + most major CM's hae good testing abstration


### Video
[video][vida]

[vida]: https://edx-video.net/LINLFS162016-V006800_DTH.mp4


### Recommended Resources
+ Kief Morris, [Infrastructure as Code](http://shop.oreilly.com/product/0636920039297.do)


## Creating Consistency in the Pipeline (Part VI)
### Notes
+ Interfrastructure as Code
    + Cons
        + abstraction DSL's have higher learning curve
        + complex edge case scenarios/failures
        + script/shell primitives are used often
        + point and time divergent
        + integration interface are more complex
        + infrastructure is bult Just in Time (JIT)
        + slower to provision
        + builds are convergent not congruent
    + Solutions
        + CFEngine
        + Puppet
        + Chef
        + Ansible
        + Salt

### Video
[video][vidb]


[vidb]: https://edx-video.net/LINLFS162016-V006700_DTH.mp4


## Creating Consistency in the Pipeline (Part VII)
### Notes
+ Immutable Infrastructure
    + Immutable Configuration Management
        + deploy the immutable imaqge from an artifacts repository
        + uses a meta layering tool to converge a service or a cluster
    + Orchestration
        + Virtual servers: OpenStack, CloudStack
        + Cloud: Amazpn AWS, Google (GCE), Microsoft (Azure)
    + Pros
        + less variation than infrastructure as code
        + faster to provision than infrastructure as code
        + typically use infrastructure as code to build
        + build into the CI processes
    + Cons
        + more variation than Immutable Delivery model
        + need a good model for image management
        + slower to provision than Immutable Delivery model
        + might still need Infrastructure as Code abstraction
        + not immutable from the developers prespective

### Video
[video][vidc]

[vidc]: https://edx-video.net/LINLFS162016-V006500_DTH.mp4


### Recommended Resources
+ The Netflix Tech Blog, [Building with Legos](http://techblog.netflix.com/2011/08/building-with-legos.html)
+ Kief Morris, [ImmutableServer](http://martinfowler.com/bliki/ImmutableServer.html)


## Creating Consistency in the Pipeline (Part VIII)
### Notes
+ 4V - Toyota Supply Chain Management
    + Variety (increase): determinging your variety of offerings based on operational efficiecny and marketing demand
    + Velocity (increase): maintain a steady flow through all processes of the supply chain
    + Varability (decrease): manage inconsistentcies carefully to reduce cost and improve quality
    + Visibility (increase): ensure the transparency of all processes to enable continuous learning and improvement
+ Fields on Velocity
    + developer flow
    + integration flow
    + development flow

### Video
[video][vidd]

[vidd]: https://edx-video.net/LINLFS162016-V006600_DTH.mp4


### Recommended Resources
+ John Willis, [Docker and the Three Ways of DevOps](https://www.docker.com/sites/default/files/WP_Docker%20and%20the%203%20ways%20devops_07.31.2015%20(1).pdf)
+ Gartner, [Assessing Docker and Containers for Five Software Delivery Use Cases](https://www.gartner.com/doc/3038125/assessing-docker-containers-software-delivery)
+ DOES15, [Joshua Corman and John Willis - Immutable Awesomeness](https://www.youtube.com/watch?v=FV9X0xj6fFw)
+ Steve Traugott, [Why Order Matters: Turing Equivalence in Automated Systems Administration](http://www.infrastructures.org/papers/turing/turing.html)
+ DockerCon2014 - Michael Bryzek, [Immutable Infrastructure with Docker and EC2](https://www.youtube.com/watch?v=GaHzdqFithc]


## Creating Consistency in the Pipeline (Part IX)
### Notes
+ Onfiguration Management - Container Model
    + Immutable Delivery model
    + Orchestration for provisioning
    + Meta layer
+ Orchestration Tools - Containers
    + Docker Swarm
    + Mesos
    + Kubernetes
+ Pros of Immutable Delivery
    + least variation pattern
    + faster provision model
    + fit well w/ microservices architectures
    + really no need for infrastructure as code
    + binary consistency from desktop to production
    + buils into the CI process
+ Cons of Immutable Delivery
    + DSL abstraction not as mature as Infrastructure as Code
    + smaller changes are harder to manage
    + debugging is harder
    + need a good model for image management
    + not all delivery models fit well

### Video
[video][vide]

[vide]: https://edx-video.net/LINLFS162016-V006600_DTH.mp4


### Recommended Resources
+ GlueCon 2015 - Jerome Petazzoni, [Immutable Infrastructure with Docker and Containers](http://www.slideshare.net/jpetazzo/immutable-infrastructure-with-docker-and-containers-gluecon-2015)
+ Jared Diamond, [Guns, Germs, and Steel: The Fates of Human Societies](https://www.amazon.com/Guns-Germs-Steel-Fates-Societies/dp/0393317552)
+ [socketplane/docker-ovs](https://github.com/socketplane/docker-ovs/blob/master/Dockerfile)


# Section 4: Automated Testing
## Automated Testing (Part I)
### Notes
+ The First Way (Continuous Delivery)
    + build quality in as early as possible
    + find bugs as early as possible
    + everything gets tested
    + if it hurts, bring the pain forward
    + create fast feedback
    + version control tests
    + continuous testing ensures continuous improvements
+ The Principles for Testing
    1. Change the adersarial mindset to a collaboration mindset
    2. Change the 'dev then ops' mindset to 'dev and test'
    3. Instead of having test team, you have an everyone test team
    4. Test early, test often and shorten the feedback loop
    5. Test should have reasonable expecttions
    6. Fix bugs when you find them
    7. Reduce test documentation, automate the expectation
    8. Done meanss release
    9. Test implement vs Implement Test
+ Testing Methodologies
    + Test Driven Development (TDD)
    + Acceptance Test Driven Development (ATDD)
    + Behaviour Driven Development (BDD)

### Video
[video][vidf]

[vidf]: https://edx-video.net/LINLFS162016-V007200_DTH.mp4


### Recommended Resources
+ Elisabeth Hendrickson, [Agile Testing: Nine Principles and Six Concrete Practices for Testing on Agile Teams](http://testobsessed.com/wp-content/uploads/2011/04/AgileTestingOverview.pdf)
+ [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development)


## Automated Testing (Part II)
### Notes
+ Test Driven Development (TDD)

    ![diagram](https://lh4.ggpht.com/-duxfZvz3yZg/UHaLmc6U-KI/AAAAAAAABg8/mtkdfrdVvfk/image_thumb3.png?imgmax=800)
    + RED: write a test based on the requriements; make it fail
    + GREEN: write a small piece of code to make it pass
    + REFACTOR: refactor the code by improving it w/o changing the behavior and repeat
+ Benefits of TDD
    + prevent scope creep
    + create design issues early
    + create cleaner code
    + build trust w/ other service owners
    + create a consistent rhythm
+ Acceptance Test Driven Development (ATDD)
    Business stack holders
    + Discuss
    + Distill: collaborate
    + Develop: TDD
    + Demostrate: shoe nre feature -> get feedback


### Video
[video][vidg]

[vidg]: https://edx-video.net/LINLFS162016-V007100_DTH.mp4


### Recommended Resources
+ Eric Evans, [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)
+ Dan North, [What's in a Story?](https://dannorth.net/whats-in-a-story/)
+ James Wickett, [Hands-on GauntIt: Security Testing for Developers](https://leanpub.com/hands-on-gauntlt)
+ Petr Lapukhov (Facebook), [Move Fast, Unbreak Things!](https://www.youtube.com/watch?v=zs2Zn9rW3Ow)


## Automated Testing (Part III)
### Notes
+ Agile Testing Pyramid

    ![diagram](https://www.symbio.com/wp-content/uploads/2015/01/Screen-Shot-2015-06-09-at-11.51.06-AM.png)
+ Build Phase Tests
    + Unit Tests
    + Acceptance Tests
    + Integration Tests
    + User Acceptance Tests
+ Automating the Tests
    + automated tests ae always running
    + every commit
    + nightly functional testing
    + smoke testing
    + stability testing
    + performance testing
    + zero configuation
+ Unit Tests
    + testing the source code by class or fucntion
    + typically done at commit or before commit
    + typically 'mokcs' are created for interface call
    + typically created by developer
    + develop intention checking
    + should be run on every change
    + unit test should be fast
    + clear results
    + TDD based

### Video
[video][vidh]

[vidh]: https://edx-video.net/LINLFS162016-V007000_DTH.mp4


### Recommended Resources
+ [Open Mic 2: Continuous Deployment and Operations Dashboards at kaChing (Wealthfront)](https://vimeo.com/14830327)


## Automated Testing (Part IV)
### Notes
+ Acceptance Tests
    + testing multiple classes or fucntions
    + should verify a user story
    + should be written before code
    + checks for regressions
    + tests what the customer expects
    + specification written in Domain Specific Language (DSL)
    + run after the build and all unit tests have passed
+ Integration Tests
    + testing integration w/ other applications and services
    + all code and modules are tested as a group
    + tests are systems wide view of the service
    + tests real interface not 'mocks'
    + integration tests are typically more expensive
    + run after build, all unit tests and acceptance have passed
+ User Acceptance Tests (Manual)
    + testing done by customers
    + ensure the applications or service meets the requirements
    + catch defects from a customer's perspective

### Video
[video][vidi]

[vidi]: https://edx-video.net/LINLFS162016-V007400_DTH.mp4


## Automated Testing (Part V)
### Notes
+ Deploy Phase Tests
    + System Testing
    + Performance Testing
    + Load Testing
    + Security Testing
    + Configuration Management Testing
+ System Testing
    + precondition for realease before turned on in production
    + testing of external interface
    + synethetic testing, emulation of user iteractions
    + tests can be emulated from APIs, consoles, web devices, mobile & even from laser printer
+ Performance Testing
    + tests the speed and latency of a service
    + can test against customer's SLA
    + performacne regression tests
+ Load Testing
    + test how much load a serveice can handle
    + test involve increasing traffic to fix maximum load
    + perofrmance regression load tests
+ Security Testing
    + SQL Injection
    + Cross siteScripting
    + Unprotected redirects
    + Unsafe file access
    + Version-specific issues
    + Symbol Dos
    + Remote code extension

### Video
[video][vidj]

[vidj]: https://edx-video.net/LINLFS162016-V007500_DTH.mp4


### Recommended Resources
+ [Open Mic 2: Continuous Deployment and Operations Dashboards at kaChing (Wealthfront)](https://vimeo.com/14830327)


## Automated Testing (Part VI)
### Notes
+ Tools
    + Unit Testing
        + JUnit (Java)
        + JTest (Java)
        + CUnit (C)
        + RSpec (Ruby)
        + Google Test
        + Parasoft
        + Visual Studio
    + Load and Performance Testing
        + Apache Bench
        + Apache JMeter
        + HP LoadRunner
        + Rational Performance Tester
        + Selenium
        + Neoload
        + SOASTA - synthetic user testing
    + BDD Testing
        + Cucumber (Ruby)
        + Cactus (Python)
        + JBehave (Java)
        + SpecFlow (Cucumber for .Net)
    + Security Testing
        + Brakeman
        + Gauntlet
        + Nmap
        + OWASP
    + Configuration Management Testing
        + Chef
            + ChefSpec (Unit)
            + Test Kitchen (Integration)
            + Cucumber-Chef (BDD)
            + Food Critic (Lint)
        + Puppet
            + rspec-puppet (Unit)
            + Test Kitchen (Integration)
            + Beaker (Integration)
            + Puppet-Lint (Lint)

### Video
[video][vidk]

[vidk]: https://edx-video.net/LINLFS162016-V009000_DTH.mp4


### Recommended Resources
+ Eran Messeri, [What goes wrong when thousands of engineers share the same continuous build?](http://gotocon.com/dl/goto-aar-2013/slides/EranMesseri_WhatGoesWrongWhenThousandsOfEngineersShareTheSameContinuousBuild.pdf)
+ [Intuit Prepares for Tax Day Filing Surge with SOASTA (case study)](http://www.soasta.com/wp-content/uploads/2015/12/Intuit_CS.pdf)


# Section 5: Deployment Strategies (Zero Downtime Release)
## Deployment Strategies (Part I)
### Notes
+ General Patterns and Constraints
    + changing data in the release can be more difficult
    + Orchestrated release rollback can be more difficult
    + best time to to reply is during production
    + log deployment activities
    + don't delete old files
    + use warmup methodologies
+ Upgrading Live Services
    + Rolling upgrades
    + Canary
    + Phased roll-outs
    + Proportional shedding
    + Blue-Green Deployment
    + Toggling features

### Video
[video][vidl]

[vidl]: https://edx-video.net/LINLFS162016-V007800_DTH.mp4

### Recommended Resources
+ Tom Limoncelli, [The Practice of Cloud System Administration Book](https://www.amazon.com/Practice-Cloud-System-Administration-Distributed/dp/032194318X)


## Deployment Strategies (Part II)
### Notes
+ Rolling Upgrades
    + servers are removed from service and upgrade one at a time
    + the process is completed when all the serversare updated
    + During the upgrade there is a temporary reduction in capacity
    + server is first drained by removing from load balancer
+ Canary
    + similar to rolling upgrade but to a subset of servers
    + apply skome, performane and load tests
    + if no problem arise, add more subsets
    + server is first drained by removing from the load balancer
    + can also be done by percentage of servers
    + able to combine w/ other rollout strategies
    + designed to find defect release
+ Phased Roll-Outs
    + partitioned by user or groups
    + categorized by risk tolerance
    + if no problems arise, add more subsets
    + sometimes internal employees can be the first roll-out group
    + power user or meta communities roll-outs
+ Proportional Shedding
    + a new service is built on new server
    + the load balancers shed small percentages of traffic to the new service
    + the percentage is increased is no issue are found
    + the old service is turned off when all traffic is moved to the new service w/ no errors
    + bare metal this can be expensive, cloud makes this more economical
+ Blue-Green Deploy
    + similar to proportaional shedding accept you duplicate the applications not the services
    + Green is the live service
    + Blue is domant and requires limited resources
    + when the release goes live, the two are swapped
    + rolling back is easier to do
    + very popular technique
+ Toggling Features
    + a.k.a. __feature flags__
    + flags ae set in the code that can turn on or off a feature
    + allow a developer to continuously deploy new code decoupled from a release
    + distributed key value stores like zookeeper, etcd, and consul cba be used for frature toggle
    + features can be gradually introduced or be point and time released

### Video
[video][vidm]

[vidm]: https://edx-video.net/LINLFS162016-V008100_DTH.mp4


## Deployment Strategies (Part III)
### Notes
+ Amazon Cloud Deploy
    + Actions:
        + cloud w/o restrictions on the number of servers
        + entire copy of running fleet -> upgrade, perfromance tests, etc.,w/o toching the live service
        + flip the load balancer to point to the new fleet
        + deply flip in seond
        + rollbaclk in seconds
    + Results
        + 75% reduction in outages triggerd by software deploys
        + 90% reductionin outage minutes triggered by software deploys
        + ~0.001% of software deployments cause an outage
        + Instantaneous automated rollback
        + reception in compplexity
+ Dark Launch of Facebook Chat

### Video
[video][vidn]

[vidn]: https://edx-video.net/LINLFS162016-V008000_DTH.mp4

### Recommended Resources
+ John Allspaw and Paul Hammond, [10+ Deploys Per Day](https://www.youtube.com/watch?v=LdOe18KhtT4)
+ Eugene Letuchy, [Facebook Chat](https://www.facebook.com/note.php?note_id=14218138919&id=9445547199&index=0)


# Summary
## Notes
+ The First Way Principles
    + create automated and repeatable environment at each stage of the pipeline
    + apply automated testing at every stage of the pipeline
    + increase flow and shorten lead times
    + global optimzation vs local optimization
+ Comtinuous Integration: integrating components of a feature, application or service
+ Continuous Delivery: the continuous integration to create installable artifacts (packages) that cabn be deployed
+ Continuous Deployment: the process of deploying a feature, application or service to production
+ Principle of Continuous Delivery
    1. Create a repeatable, reliabile process for releasing software
    2. Automated almost everything
    3. Keep everything in version control
    4. If it hurts, do it more frequently and bring the pain forward.
    5. Build quality in
    6. Done means released
    7. Everybody is responsible for the delivery process.
    8. Continuous improvement
+ The Deployment Pipeline:
    + Visibility: all the stages of the pipeline are visible to everyone responsible for the delivery of the service
    + Feedback: each stage in the pipeline has designed "gates" created to eliminate downstream defects
    + Continuous Deploy: the design of the pipeline is such that any patch, update or new feature can be automated for delivery, deploy and releases.
+ Consistent Pipeline Challenges
    + Snowflake
    + Sprawl
    + Drift
    + Documentation
+ Pets vs Cattles
+ Version Control Everything
    + kee a history of all changes
    + can restore and rebuild all elements
    + everything can be versioned and tagged
    + all changes are visible and audited for everyone
    + Changes can be automated
+ Order matters
+ Providers of Consistent Infeastructure
    + Bare Metal provisoning
    + Virtual Machine Provisioning
    + Cloud Provisioning
    + Container Provisioning
+ Consistent Operating System Environment Patterns
    + Scripted environments
    + Infrastructure as Code
    + Immutable Infrastructure
    + Immutable Delivery
+ Automated Testing
    + Test Driven Development (TDD)
    + Acceptance Test Driven Development (ATDD)
    + Behavior Deiven Development (BDD)
    + Automated Tests (Build & Deploy)
    + Tools
+ Agile Testing Pyramid: UI/Integration Tests/Automated Unit Test
+ Deployment Strategies: Upgrading
    + Rolling upgrades
    + Canary
    + Phased Roll-Outs
    + Proportional Shedding
    + Blue-Green Deployment
    + Toggle Features
    

## Video
[video][vido]

[vid0]: https://edx-video.net/LINLFS162016-V007900_DTH.mp4

# Knowledge Check
Q1. Which of the following best describes the idea of reducing bottlenecks? Please select the correct answer.

    a. Lean
    b. The Theory of Constraints
    c. Agile
    d. DevOps

    Ans: b

Q2. What is the primary difference between Continuos Delivery and Continuous Deployment? Please select the correct answer.

    a. Continuous Deployment can be deployed to production and Continuous Delivery is deployed into production
    b. Continuous Delivery can be deployed to production and Continuous Deployment is deployed into production
    c. Continuous Delivery can be deployed to test and Continuous Deployment is deployed into production
    d. Continuous Delivery can be deployed to production and Continuous Deployment is deployed into test

    Ans: b

Q3. What is the difference between Test-Driven Development (TDD) and Behavior-Driven Development (BDD)? Please select the correct answer.

    a. TDD is where developers write the code first, before testing, and BDD is where tests are designed to test how the code works versus how it behaves
    b. TDD is where developers write the code first, before testing, and BDD is where tests are designed to test how the code behaves versus how it works
    c. TDD is where developers write tests first, before coding, and BDD is where tests are designed to test how the code works versus how it behaves
    d. TDD is where developers write tests first, before coding, and BDD is where tests are designed to test how the code behaves versus how it works

    Ans: d


Q4. The following three items are considered types of zero downtime deployment patterns: rolling upgrades, canary, blue-green deployments. 

    Ans: True


Q5. Which of the following statements best describes the concept of "pets versus cattle"? Please select the correct answer.

    a. "Pets" are like treating your infrastructure like pets (not giving servers' names) and "Cattle" is like treating your infrastructure as cattle (giving your servers' names)
    b. "Pets" are like treating your infrastructure like pets (never logging into them) and "Cattle" is like treating your infrastructure as cattle (giving your servers' names)
    c. "Pets" are like treating your infrastructure like pets (giving servers' names) and "Cattle" is like treating your infrastructure as cattle (ephemeral infrastructure)

    Ans: c

