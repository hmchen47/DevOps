Chapter 2: Understanding the Value Stream
=========================================

# Learning Objectives
+ Explain the differences between high-performance organizations and low-performance organizations.
+ Explain the patterns of high-performance organizations.
+ Discuss the basic principles of Continuous Delivery.
+ Discuss the influences and patterns for DevOps.

# Section 1: Analyzing the Technology Value Stream
## The Three Ways of DevOps - The Value Stream
### Notes 1
+ The Value Stream:
    + 1st def: the sequence of activities an organization undertakes to delivery upon a customer request
    + 2nd def: the sequence of acticities required to design, produce and deliver a service to a customer
+ Workflow (flow) 
    + the work of a value stream
    + the waste (Muda) of the work
    + the evenness (Mura) of the work
+ Lead Time
    + the time that a process of the value stream from start to finish
    + the time from the request to end delivery
    + what the customer sees
+ Cycle Time
    + how often a part or product actually is completed by a process
    + time time from a work begin based on request to the item delivered
    + mechanical measure of process capacity
+ Types of Lead Time
    + design lead time - design and development
        + typically new work
        + uncertain estimates
        + outcomes w/ high variability
    + deployment lead time - test and oepration
        + repeatable process (automated)
        + process times should be predictable
        + outcomes have lower variability

### Video1
[video][vid0]

[vid0]: https://edx-video.net/LINLFS16/LINLFS162016-V002200_DTH.mp4

### Notes 2
+ value stream map
    + how things work (runner)
    + the work (button) - observing
+ How to reduce development lead time
    + small batch
    + reduce WIP
    + single piece flow
    + reduce bottleneck (TOC)
    + optimize globally

### Video2
[video][vid00]

[vid00]: https://edx-video.net/LINLFS16/LINLFS162016-V002300_DTH.mp4

## Recommended Resources
+ Karen Martin, Mike Osterling, "[Value Stream Mapping: How to Visualize Work and Align Leadership for Organizational Transformation](https://www.amazon.ca/Value-Stream-Mapping-Organizational-Transformation/dp/0071828915)"
+ Damon Edwars, [DevOps Kaizen: Practical Steps to Start & Sustain a Transformation](https://www.slideshare.net/dev2ops/devops-kaizen-practical-steps-to-start-sustain-a-transformation)

## Extra Resources
+ Mike Rother,‎ John Shook, [Learning to See: Value Stream Mapping to Add Value and Eliminate Muda](https://www.amazon.ca/Learning-See-Stream-Mapping-Eliminate/dp/0966784308)
+ Damon Edwards, [Support and Initiate a DevOps Transformation](https://www.slideshare.net/dev2ops/support-and-initiate-a-devops-transformation)
+ Steven Smith, [The Satir Change Model](https://stevenmsmith.com/ar-satir-change-model/)

# Section 2: The Three Ways of DevOps
### Notes
+ The First Way - Accelerate Flow
    + --> (right to left)
    + system thinking - global/local optimization
    + increased visibility
    + Just in Time (JIT)
    + shorten lead time
+ The Second Way - Amplify Feedback
    + <-- (left to right)
    + shorten feedback loops
    + learn faster
    + fix defects faster
    + embedded knowledge
+ The Third Way - Continuous Learning
    + full cycle (iterative)
    + continual experiemntation
    + learniung from failure
    + repetition and practice
    + increase resilience

### Notes
[video][vidx]

[vidx]: https://edx-video.net/LINLFS16/LINLFS162016-V002800_DTH.mp4

## Recommended Resources
+ [The Three Ways: The Principles Underpinning DevOps](http://itrevolution.com/the-three-ways-principles-underpinning-devops/)
+ [A Personal Reinterpretation of The Three Ways](http://itrevolution.com/a-personal-reinterpretation-of-the-three-ways/)
+ [Docker and the Three Ways of DevOps Part 1: The First Way - Systems Thinking](https://blog.docker.com/2015/05/docker-three-ways-devops/)
+ [Docker and the Three Ways of DevOps](https://www.docker.com/sites/default/files/WP_Docker%20and%20the%203%20ways%20devops_07.31.2015%20(1).pdf)

# Section 3: The First Way - Flow
## The First Way - Flow (Part I)
### Notes
+ Maximize flow (the work)
    + make work visible
    + reduce batch size
    + limit WIP
    + eliminate wate
    + reduce bottleneck
+ Visiable Storyboard
    + Scrum
    + Scrumban
    + Kanban
+ Kanban Board
    + basic: card wall, activities, work items
    + advanced: two tierd, swim lanes, WIP limit, blockers

### Video
[video][vid1]

[vid1]: https://edx-video.net/LINLFS16/LINLFS162016-V001700_DTH.mp4

### Recommanded Resources
+ [David Anderson Kanban At Q Con](http://www.slideshare.net/deimos/david-anderson-kanban-at-q-con)
+ [Kanbans and DevOps: Resource Guide for “The Phoenix Project” (Part 2)](http://itrevolution.com/resource-guide-for-the-phoenix-project-kanbans-part-2/)

### Extra Resources
+ Jim Benson, [Personal Kanban: Mapping Work|Navigating Life](https://www.amazon.com/Personal-Kanban-Mapping-Work-Navigating/dp/1453802266/ref=_1_1?s=books&ie=UTF8&qid=1466121877&sr=1-1&keywords=jim+benson) 
+ David J. Anderson, [Kanban: Successful Evolutionary Change for Your Technology Business](https://www.amazon.com/Kanban-Successful-Evolutionary-Technology-Business/dp/0984521402)

## The First Way - Flow (Part II)
### Notes
+ Samll Batches Principles
    + faster feedback
    + mean time to detect is faster
    + mean time to resolve is faster
    + reduce risk
    + lss overhead
+ Single Piece Flow (1 x 1 flow)
    + no inventory reduces cycle time
    + smoother workflow
    + catch error earlier
    + create learning opportunities
+ Samll Batch & Single Piece Flow in Software
    + small piece of code (e.g. feature)
    + chick in w/ source control
    + merge into trunk
    + testing
    + deployment

### Video
[video][vid2]

[vid2]: https://edx-video.net/LINLFS16/LINLFS162016-V001600_DTH.mp4

### Recommanded Resources
+ Thomas A. Limoncelli, [The Small Batches Principle](https://queue.acm.org/detail.cfm?id=2945077)
+ Gemba Academy, [Watch This One Piece Flow vs. Mass Production Envelope Stuffing Lean Thinking Simulation](https://www.youtube.com/watch?v=Dr67i5SdXiM)
+ John Allspaw and Jess Robins, [Web Operations: Keeping the Data on Time (Chapter 4)](https://www.amazon.com/Web-Operations-Keeping-Data-Time/dp/1449377440)

### Extra Resources
+ Eric Reis, [The Lean Startup: How Today’s Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses](https://www.amazon.com/Lean-Startup-Entrepreneurs-Continuous-Innovation/dp/0307887898)


## The First Way - Flow (Part III)
### Notes
+ Limiting WIP
    + cognitive work - creaive solution
    + interruptions - reducing
    + context switching - reduce
    + multitasking - prevent
    + handoffsm - reduce
+ Purpose
    + regulate flow
    + reduce multitasking
    + emergent
+ WIP Limit Implementation - Queues & Buffers

### Video
[video][vid3]

[vid3]: https://edx-video.net/LINLFS16/LINLFS162016-V001800_DTH.mp4

### Recommanded Resources
+ [David Anderson Kanban at Q Con](http://www.slideshare.net/deimos/david-anderson-kanban-at-q-con)
+ [DOES15 - Dominica DeGrandis - The Shape of Uncertainty](https://www.youtube.com/watch?v=Gp05i0d34gg)

## The First Way - Flow (Part IV)
### Notes
+ Lean Principles
    + eliminate waste
    + amplify learning
    + describe as late as possible
    + deliver as fast as possible
    + empower the team
    + build integrity in
    + see the whole
+ Types of wate
    + Muda (unproductive)
    + Mura (inconsistent)
    + Muri (unreasonable)
+ Seven Wastes
    + transport
    + inventory
    + motion
    + waiting
    + overproduction
    + over processing
    + defects
+ Lean Software Development (Principles)
    + eliminate wate
    + build quality in
    + create knowledge
    + defer commitment
    + deliver fast
    + respect people
    + optimize the whole

### Video
[video][vid4]

[vid4]: https://edx-video.net/LINLFS16/LINLFS162016-V001900_DTH.mp4

### Recommanded Resources
+ [Lean software development](https://en.wikipedia.org/wiki/Lean_software_development)

### Extra Resources
+ [Lean Software Development: An Agile Toolkit](https://www.amazon.com/Lean-Software-Development-Agile-Toolkit/dp/0321150783)

## The First Way - Flow (Part V)
### Notes
+ Procedure to eliminate TOC
    1. identify the system constraints
    2. decide how to expolit them
    3. subordinate everything elese to the above decision
    4. elevate the system constraints
    5. repeate step 1~4 if required
+ Way to Smooth Bottlenecks
    + WIP limit
    + Queues
    + Buffers

### Video
[video][vid5]

[vid5]: https://edx-video.net/LINLFS16/LINLFS162016-V002100_DTH.mp4

### Recommanded Resources
+ [Theory of Constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)

### Extra Resources
+ [Beyond the Goal: Eliyahu Goldratt Speaks on the Theory of Constraints (Your Coach in a Box)](https://www.amazon.com/Beyond-Goal-Eliyahu-Goldratt-Constraints/dp/1596590238)


# Section 4: The Second Way - Feedback Loops
## The Second Way - Feedback Loops (Part I)
### Notes
+ Accelerate Feedback
    + telemetry
    + fault injection
    + safety culture
    + fast feedback
+ Telemetry
    + monitoring
        + legacy: HP Openview, IBM Tivoli, BMC Patrol
        + open source: Nagio, Zenoss, Sensu (Nagio + Python)
        + SaaS: DataDog, NewRelic, SignalFX
    + logging: Splunk, Loggly, ELK (ElasticSearch, Logstash, Kibana)
    + analytics: Graphite, Riemann, Hadoop/Spark

### Video 
[video][vid6]

[vid6]: https://edx-video.net/LINLFS16/LINLFS162016-V002500_DTH.mp4

### Recommanded Resources
+ Toufic Boubez, [Simple math for anomaly detection](http://www.slideshare.net/tboubez/simple-math-for-anomaly-detection-toufic-boubez-metafor-software-monitorama-pdx-20140505)
+ Toufic Boubez, [Some Simple Math for Anomaly Detection](https://vimeo.com/95069158)

### Extra Resources
+ James Turnbull, [The Art of Monitoring](https://www.artofmonitoring.com/)
+ Jason Dixon, [Monitoring with Graphite Tracking Dynamic Host and Application Metrics at Scale](http://shop.oreilly.com/product/0636920035794.do)
+ [Monitorama’s Videos](https://vimeo.com/monitorama/videos/)

## The Second Way - Feedback Loops (Part II)
### Notes
+ Purpose of Fault Injection: reduce MTBF & MTTR
+ Examples of Fault Injection
    + GameDay: reduce MTBF; reduce MTTR
    + Netflix Simian Army
        + Chaos Monkey (Hosts)
        + Chaos Gorilla (Data Center)
        + Latency Monkey (Inject Latency)
        + Comformity Monkey (best practice)
        + Security Monkey (Security violations)
    + FIT (Fault Injection Testing) - Netflix
        + limit blast ratio of the failure
        + telemetry of path of the failure
        + dependency telemetry

### Video
[video][vid7]

[vid7]: https://edx-video.net/LINLFS16/LINLFS162016-V002600_DTH.mp4

### Recommanded Resources
+ Jesse Robbins, [GameDay: Creating Resiliency Through Destruction](https://www.youtube.com/watch?v=zoz0ZjfrQ9s)
+ Jesse Robbins, Kripa Krishnan, John Allspaw, and Tom Limoncelli, [Resilience Engineering: Learning To Embrace Failure](http://queue.acm.org/detail.cfm?id=2371297)
+ John Allspaw, [Fault Injection in Production - making the case for resilience testing](http://queue.acm.org/detail.cfm?id=2353017)
+ [The Netflix Simian Army](http://techblog.netflix.com/2011/07/netflix-simian-army.html)
+ [FIT: Failure Injection Testing](http://techblog.netflix.com/2014/10/fit-failure-injection-testing.html)


## The Second Way - Feedback Loops (Part III)
### Notes
+ Safety Culture: loose taxonomy of DevOps - ICE
    + Inclusivity
        + Diversity
        + Relationship
        + Team Culture
        + Team Cohesion
    + Complexity
        + Cybernetic feedback loop - CAMS
        + Cynefin framewwork: simple, complicated, complex, chaotic
    + Empathy
        + Dev ... Ops
        + Embedded Engineers
        + Blameless postmortems

### Video
[video][vid8]

[vid8]: https://edx-video.net/LINLFS16/LINLFS162016-V002700_DTH.mp4

### Recommanded Resources
+ Dave Zwieback, [DevOps keeps it cool with ICE](http://radar.oreilly.com/2015/01/devops-keeps-it-cool-with-ice.html)
+ Dave Snowden, [The Cynefin Framework](https://www.youtube.com/watch?v=N7oz366X0-8)
+ John Allspaw and Jesse Robbins, [Web Operations: Keeping the Data on Time (Chapter 7)](https://www.amazon.com/Web-Operations-Keeping-Data-Time/dp/1449377440)
+ Jeff Sussna, [Empathy: The Essence of DevOps](http://blog.ingineering.it/post/72964480807/empathy-the-essence-of-devops)

### Extra Resources
+ Jennifer Davis and Katherine Daniels, [Effective DevOps](https://www.safaribooksonline.com/library/view/effective-devops/9781491926291/)
+ Christina Maslach, [Reversing Burnout](http://graphics8.nytimes.com/packages/pdf/business/06.BURNOUT.FINAL.pdf)
+ [Botchagalupe on Burnout](https://github.com/botchagalupe/my-presentations)


## The Second Way - Feedback Loops (Part IV)
### Notes
+ Features for live upgrade
    + rolling upgrades
    + canary - a pattern for rolling out releases to a subset of users or servers
    + blue green deploy - identical envs w/ diff apps (e.g. versions)
    + toggling feature - on/off switch
+ [Toyota Production System - Lean Thinkng](http://www.getbusymedia.com/wp-content/uploads/2012/03/toyota21.jpg)

### Video
[video][vid9]

[vid9]: https://edx-video.net/LINLFS16/LINLFS162016-V002900_DTH.mp4

### Recommanded Resources
+ [Feature flags, dark launches, and canary releases for all: LaunchDarkly, first year in review](http://blog.launchdarkly.com/feature-flags-dark-launches-and-canary-releases-for-all-launchdarkly-first-year-in-review/)
+ [Feature flags and canary, dark, and A/B releases](http://www.pragmaticdevops.com/2014/05/continuous-delivery/feature-flags-and-canary-dark-and-ab-releases/)
+ [How does Easy manage development and operations?](https://codeascraft.com/2011/02/04/how-does-etsy-manage-development-and-operations/)

### Extra Resources
+ Tom Limoncello, [The Practice of Cloud System Administration: Designing and Operating Large Distributed Systems, Volume 2](https://www.amazon.com/Practice-Cloud-System-Administration-Distributed/dp/032194318X)


# Section 5: The Third Way - Culture of Continual Experimentation and Learning
## The Third Way - Culture of Continual Experimentation and Learning (Part I)
### Notes
+ 2015 State of DevOps Report
    + 30x deployments
    + 200x shorter lead times
    + 60x less failure
    + 166x shorter MTTR
+ A Typology of Organization Culture - R. Westrum
    ![culture](https://cdn-images-1.medium.com/max/2000/1*WhJ9IvNkRleAaFCqKN83pg.png)

### Video
[video][vida]

[vida]: https://edx-video.net/LINLFS16/LINLFS162016-V003000_DTH.mp4

### Recommanded Resources
+ Bethany Macri, [Morgue: Helping Better Understand Events by Building a Post Mortem Tool](https://vimeo.com/77206751)


## The Third Way - Culture of Continual Experimentation and Learning (Part II)
### Notes
+ Toyota: an organization defined primarily by the unique behavior routines it continually teaches to all its members
+ Learning Organizaton
    + Invisible: Culture -> Behavior -> Habbit -> Autonomic
    + Visible (Scientific Thinking): Scientific Method -> Depersonalized -> Non-Blameful -> Non Deterministics => Deming Cycle PDCA
+ Toyota Kata
    ![kata](https://kaizeninstituteindia.files.wordpress.com/2014/02/p2.png?w=768)
    + Improving Kata
        ![improvment](https://image.slidesharecdn.com/toyotakata-100207234813-phpapp01/95/toyota-kata-11-638.jpg?cb=1374427899)
    + Coaching Kata
        ![coaching](https://kaizeninstituteindia.files.wordpress.com/2014/02/i18.png?w=768)

### Video
[video][vidb]

[vidb]: https://edx-video.net/LINLFS16/LINLFS162016-V003100_DTH.mp4

+ [The Improvement Kata Pattern](https://www.slideshare.net/mike734/introduction-to-the-improvement-kata)

## The Third Way - Culture of Continual Experimentation and Learning (Part III)
### Notes
+ Capabilities of High Velocity Edge
    1. seeing problem s as they occur
    2. swarming and solving problems as they are seen to build new knowledge
    3. spreading new knowledge throughout the organization
    4. learning by developing
+ Change management Model - John Kotter
    ![Diagram](https://www.scrumalliance.org/getattachment/Community/Articles/Newly-Submitted/Change-Management-Models/fig-2-(2).jpg.aspx)

### Video
[video][vidc]

[vidc]: https://edx-video.net/LINLFS16/LINLFS162016-V003200_DTH.mp4

### Recommanded Resources
+ Mike Rother, [Introduction to the Improvement Kata](http://www.slideshare.net/mike734/introduction-to-the-improvement-kata)
+ DOES15, [Courtney Kissler & Jason Josephy - Mindsets and Metrics and Mainframes... Oh My!](https://www.youtube.com/watch?v=88_y1YFsRig)
+ DOES15, [Steven Spear - Creating High Velocity Organizations](https://www.youtube.com/watch?v=onwhZwroQHs)
+ [How Many Times Do You Pull the Andon Cord Each Day](https://blog.gembaacademy.com/2008/04/08/how_many_times_do_you_pull_the_andon_cord_each_day/)

### Extra Resources
+ [Botchagalupe presentations](https://gist.github.com/botchagalupe/984acf7b7ffeeb287ffe)
+ John Kotter & Dan Cohen, [The Heart of Change: Real-Life Stories of How People Change Their Organizations](https://www.amazon.com/Heart-Change-Real-Life-Stories-Organizations/dp/1422187330)
+ Velocity NYC 2013 - Andrew Clay Shafer, [There Is No Talent Shortage](https://www.youtube.com/watch?v=P_sWGl7MzhU)
+ Drake Baer, [How Changing One Habit Helped Quintuple Alcoa's Income](http://www.businessinsider.com/how-changing-one-habit-quintupled-alcoas-income-2014-4)

# Summary
## Notes:
+ Value Stream
    + Definitions
    + Lead Time & Cycle Time
    + DevOps Value Stream - Lead Time
        + Design Lead Time
            1. create an idea
            2. add work to the backlog
            3. create a user story
            4. implement as code
        + Deployment Lead Time = Cycle Time
            5. check into version control
            6. deploy into production
            7. validate the customer experience
    + Value Streaming Mapping - Damon Edwards, DOT solution
+ The Three Ways of DevOps
    + The first way - accelerating flow: max flow
        + make work visible
        + reduce batch size
        + limit WIP
        + eliminate waste
        + reduce bottleneck
    + The second way - feedback loops
        + telemetry
        + fault injection
        + safety culture
        + fast feedback
    + The third way - continuous learning
        + a typology of organizational culture
        + Toyota Kata - Mike Rother
        + Deming Methodologies: cycle, system thinking, scientific thinking
        + 5th discipline - Peter Senge
        + The Hear of Change - J. Kotter

## Video
[Vido][vidd]

[vidd]: https://courses.edx.org/courses/course-v1:LinuxFoundationX+LFS161x+2T2016/courseware/03573d7b3e074966a56e9651adb1e0c8/00c4c518e74c49bf8eba839822f910cc/?activate_block_id=block-v1%3ALinuxFoundationX%2BLFS161x%2B2T2016%2Btype%40sequential%2Bblock%4000c4c518e74c49bf8eba839822f910cc

# Knowledge Check
Q1. Which of the following is considered part of the Cycle Time? 

    Ans: Check into version control, deploy into production, and validate the custoner experience

Q2. Which of the following is not a way of reducing Lead Time?

    Ans: optimize locally 
    
    [make work visible, reduce batch size, limit WIP, eliminate wast (1x1 flow), reduce bottleneck (system thinking)]

Q3. What does PDCA stand for and who is its author? Please select the correct answer.

    a. Plan-Do-Check-Act/Deming
    b. Plan-Do-Change-Act/Deming
    c. Plan-Do-Check-Act/Rother
    d. Plan-Do-Change-Act/Rother

    Ans: a

Q4. The Three Ways of DevOps are: the First Way - Accelerate Flow, the Second Way - Amplify Feedback, and the Third Way - Continuous Integration. 

    Ans: False

    The Three Ways of DevOps are: the First Way - Accelerate Flow, the Second Way - Amplify Feedback Loops, and the Third Way - Culture of Continuous Experimentation and Learning.

Q5. Which of the following is a popular tool in DevOps to help manage Flow and make work visible??

    a. Scrum
    b. Chef
    c. Puppet
    d. Kanban

    Ans: d

