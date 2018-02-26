Chapter 3: Getting Started With Devops
======================================

# Learning Objectives
+ Get started with DevOps.
+ Explain the different kinds of Value Stream.
+ Discuss the tools that can be used to map a Value Stream.
+ Explain the concept of organizational change.
+ Enable transformation.
+ Review real-world use cases and reports from organizations undergoing DevOps transformations.
+ Discuss Conway's Law and its impact on organizational change.
+ Explain the concepts of Mindsets.

## Notes
+ Initialize Transformation Porcess
    + pick up a value stream
    + understanding organizational culture
    + Enable Transformation
+ Improvement Paradox
    + small enough for success and safe
    + large enough for furture improvements

# Section 1: Picking a Value Stream
## Picking a Value Stream (Part I)
### Notes
+ Types of Value Stream 
    + Legacy
    + Borwnfield
    + Greenfield
+ Types of legacy transformation
    + System of Records - core to services
    + System of Engagement - cx or employee facing stuff
+ Components of Risk Management (3Rs): reward, risk, resistance
+ 3R for Legacy Trasformation
    + leadership support is critical
    + look for innovators and early adopter
    + prior knowledge of DevOps helps
    + SOE better than SOR
    + build on success
+ The ETTO Principle
    + Efficiency: low investment, sufficient to achieve the goal
    + Thoroughness: w/o side-effect, intended outcomes
+ Simple Value Stream Analysis
    + value added time
    + wait time
    + elapsed time
+ Value Stream Analyssi from Lean software development
    + geta pencile nd pad
    + start w/ the cx' request
    + follow all the activities
    + sketch each activity as a process
    + draw a line at the botto w/ wait time and value added time

### Video
[video][vid1]

[vid1]: https://edx-video.net/LINLFS16/LINLFS162016-V003500_DTH.mp4

### Recommended Resources
+ Erik Hollnagel, [The ETTO Principle - Efficiency-Thoroughness Trade-Off](http://erikhollnagel.com/ideas/etto-principle/index.html)


## Picking a Value Stream (Part II)
### Notes
+ Value Stream Mapping - D. Edwards
    ![diagram](https://image.slidesharecdn.com/dod-rome2012-culture-121014173650-phpapp02/95/you-cant-change-culture-but-you-can-change-behavior-devopsdays-rome-2012-55-728.jpg?cb=1350236860)
+ Waste Analysis - Seven Wastes of Software
    1. Partially done work --> Inventory
    2. Extra features --> Overproduction
    3. Relearning --> Extra Processing
    4. Handoffs --> Transportation
    5. Delays --> Waiting
    6. Task switching --> Motion
    7. Defects --> Defects

### Video
[video][vid2]

[vid2]: https://edx-video.net/LINLFS16/LINLFS162016-V003600_DTH.mp4

### Recommended Resources
+ [Damon Edwards presentation](https://vimeo.com/69079272)
+ Erik Hollnagel, [The ETTO Principle - Efficiency-Thoroughness Trade-Off](http://erikhollnagel.com/ideas/etto-principle/index.html)

### Extra Resources
+ Mike Rother, [Learning to See: Value Stream Mapping to Add Value and Eliminate MUDA](https://www.amazon.com/Learning-See-Stream-Mapping-Eliminate/dp/0966784308?ie=UTF8&hvadid=30911744901&hvdev=c&hvexid=&hvnetw=g&hvpone=60.00&hvpos=1t1&hvptwo=&hvqmt=b&hvrand=8624445624253798359&ref=pd_sl_3hk32rzq94_b&tag=googhydr-20)
+ Karen Martin and Mike Osterling, [Value Stream Mapping: How to Visualize Work and Align Leadership for Organizational Transformation](https://www.amazon.com/Value-Stream-Mapping-Organizational-Transformation/dp/0071828915)

## Picking a Value Stream (Part III)
### Notes
+ Nordstom: value stream workshop --> manual formas bottleneck
+ Ticketmaster - Transformation Patterns
    + Empathy: 
        + breath customer oxygen
        + everyone is a fan
    + Empowerment: 
        + teams deploy their own code
        + four in a box
        + self service everything
    + Metrics
        + Business metrics --> system metrics
        + outcomes over output
        + democratize the data

### Video
[video][vid3]

[vid3]: https://edx-video.net/LINLFS16/LINLFS162016-V003700_DTH.mp4

### Recommended Resources
+ Paula Thrasher, [Three Steps to Change: Lessons from Battling Bureaucracy (DOES15](https://www.youtube.com/watch?v=Hen6lk3J_ss)
+ Courtney Kissler, [Nordstrom-Transforming to a Culture of Continuous Improvement (DOES14)](https://www.youtube.com/watch?v=0ZAcsrZBSlo)
+ Jody Mulkey, [DevOps in the Enterprise: A Transformation Journey](https://www.youtube.com/watch?v=USYrDaPEFtM)


## Picking a Value Stream (Part IV)
### Notes
+ Target API Enablement Team:
    + Days in stead of months
    + Took over operations responsibilities
    + Reduce handoffs
    + Agile not waterfall
    + Insource work
    + Single sourth of truth
    + Design a decouple architecture
    + Brought in Kafka & Cassandra

### Video
[video][vid4]

[vid4]: https://edx-video.net/LINLFS16/LINLFS162016-V003400_DTH.mp4

### Recommended Resources
+ DOES15 - Heather Mickman & Ross Clanton, [(Re)building an Engineering Culture: DevOps at Target](https://www.youtube.com/watch?v=7s-VbB1fG5o)


## Picking a Value Stream (Part V)
### Notes
+ Target DevOps Dojo:
    + dedicated space @ HQ
    + coaches & subject matter experts (SMEs)
    + Goal: create an engineering culture
+ Workship format
    + Challenges: 30 days experience; Agile, Lean, DevOps
    + Flashbuilds: 1~3 days events; new features, solve a specific problem
    + Open Labs: 90 min sessions; Q&A, Inspiration
+ Results:
    + Outcomes: consistency, velocity, founfation
    + Personel: team building, confidence, collaboration
+ Less Learned
    + MVP's Rock
    + Signed commitments
    + Collaborate with facilities
    + Don't overly focus on one area
    + Get comfortable w/ uncomfortable
+ Advise:
    + Don't wait to start
    + Be exclusively inclusive
    + Empower change agents
    + Unlearn what have learned
    + Connect and share experience internally and externally

### Video
[video][vid5]

[vid5]: https://edx-video.net/LINLFS16/LINLFS162016-V003800_DTH.mp4 

### Recommended Resources
+ DOES15 - Heather Mickman & Ross Clanton, [(Re)building an Engineering Culture: DevOps at Target](https://www.youtube.com/watch?v=7s-VbB1fG5o)


## Picking a Value Stream (Part VI)
### Notes
+ Brownfield Calssification
    + Adding a new feature to ledgacy
    + Altering fncationality of a service
    + Up=grading a core service of a ledgacy application
+ Strangler Applications for Brownfield
    + Event interception
    + Asset capture
    + Ledgacy Test Automation (ATDD)
+ Strangler Patterns for Ledgacy
    + Specflow tests for the ledgacy applications
    + Once they went sufficient coverage they port over to the modern system w/ very low risk
    + Then they can compare test results against the modern system
    + They fail if the results are not identical 
    + Catches missing business logic between systems
+ CSG - Case Study
    + Challenges:
        + Pressure to make SORs / SOEs
        + Demand for speed and quality 
        + Customer & Customer's customer expecations
        + Organizationa nd Technical debt
    + Solutions:
        + Holistic incident visibility
        + Team dependency visibility
        + Team shared KPIs
        + Double loop learning
        + Cross functional teams
        + Ledgacy Test Automation (ATDD)
+ ATDD for Unimodal Test
    + Improve velocity & quality
    + Reduce risk of change
    + Strangle the complexity
    + Go see and Role rotation
    + Telemetry and shared understanding
+ Benefits in Increased Developer Time
    + Planning time reduced
    + Environmental setup time reduced
    + Code builds reduced
    + Support reduced
    + Testing reduced
    + Feature development increased

### Video
[video][vid6]

[vid6]: https://edx-video.net/LINLFS16/LINLFS162016-V004000_DTH.mp4

### Recommended Resources
+ Martin Fowler, [Strangler Application](http://www.martinfowler.com/bliki/StranglerApplication.html)
+ [Acceptance test-driven development](https://en.wikipedia.org/wiki/Acceptance_test%E2%80%93driven_development)
+ DOES15 - Scott Prugh & Erica Morrison, [Conway & Taylor Meet the Strangler (v2.0)](https://www.youtube.com/watch?v=tKdIHCL0DUg)
+ DOES14 - Scott Prugh - CSG, [DevOps and Lean in Legacy Environments](https://www.youtube.com/watch?v=f4et0EGvKXA)

## Picking a Value Stream (Part VII)
### Notes
+ Types of Work - Standard Work Input (TPP)
    + Project (business value)
    + Changes
    + Operations
    + Unplanned

### Video
[video][vid7]

[vid7]: https://edx-video.net/LINLFS16/LINLFS162016-V005100_DTH.mp4

### Recommended Resources
+ DOES15 - Carmen DeArdo, [How DevOps Is Enabling Lean Application Development](https://www.youtube.com/watch?v=sL7wHJj25DA)


## Picking a Value Stream (Part VIII)
### Notes
+ NI - Greenfield
    + Constraints: 
        + not existing IT systems
        + not existing tools
        + security first
        + automation first
    + Everything was new, simultanrously develop
        + product
        + team
        + process
        + systems
        + code
        + operations
        + system automation

### Video
[video][vid8]

[vid8]: https://edx-video.net/LINLFS16/LINLFS162016-V004200_DTH.mp4

### Recommended Resources
+ Ernest Mueller, James Wickett, Karthik Gaekwad, [The Story of DevOps at National Instruments](https://vimeo.com/62931927)
+ DOES15 - Ernest Mueller, [DevOps Transformations at National Instruments](https://www.youtube.com/watch?v=6Ry40h1UAyE)


# Section 2: Understanding Organizational Change
## Notes
+ Organizational Goals
    + The pipeline is everyone's responsibility
    + Focus on making more generalist
    + Fund servers not projects
    + Encourage loose coupling
    + Smaller teams
    + High Trust and low blame
    + Make work visible

## Understanding Organizational Change (Part I)
### Notes
+ Individual level
    + I/T/E-shape individuals
    + Mindsets
    + Motivation
    + Intent
+ I/T/E-Shaped Individuals

    | Feature | I-Shaped | T-Shaped | E-Shaped |
    | ------- | -------- | -------- | -------- |
    | Type | Specialist | Generalist | High Impact Individual |
    | Deep Skill | one | one | a few |
    | broad Skill | none | a few | a few |
    | Bottleneck | creator | helper | remover |
    | Downstream Waste | creator | remover | remover |

### Video
[video][vid9]

[vid9]: https://edx-video.net/LINLFS16/LINLFS162016-V004300_DTH.mp4

## Understanding Organizational Change (Part II)
### Notes
+ Mindsets
    + Fixed
        + fixed belief
        + outcome based
        + belief that Intelligence and Talent are fixed traits
    + Growth
        + alternative belief
        + Effort based
        + belief that abailities can be developed through dedication and hard work

### Video
[video][vid0]

[vid0]: https://edx-video.net/LINLFS16/LINLFS162016-V004400_DTH.mp4

### Recommended Resources
+ Kelly McGonigal, [How to make stress your friend](https://www.ted.com/talks/kelly_mcgonigal_how_to_make_stress_your_friend?language=en)
+ Carol S. Dweck, [Mindset: The New Psychology of Success](https://www.amazon.com/Mindset-Psychology-Carol-S-Dweck/dp/0345472322)
+ Kelly McGonigal, [The Upside of Stress: Why Stress Is Good for You, and How to Get Good at It](https://www.amazon.com/Upside-Stress-Why-Good-You/dp/1101982934)

## Understanding Organizational Change (Part III)
### Notes
+ Motivation
    + Intrinsic: personal reward
        + Autonomy
        + Sense of achievement
        + Passion
    + Extrinsic: external reward and punishment
        + Pay increase
        + Promotion
        + Bonouses
+ Overjustification Effect
    + Extrinsic reqard can decrease an individual intrinsic motivation
    + Individuals might pay more attention to the extrinsic rewards instead of their instrinsic motivations
    + Reinforces extrinsic motivation mindsets
    + Effort over outcome based extrinsic rewards are less influenced by Overjustification Effect
+ Motivation Suggestions
    + Use incentives appropriately
    + Chanllenge midsets
    + Visualize the effort not the success
    + Intent based motivation
    + The effort not the outcome
+ Mindset Change
    + create leaders at every level
    + Traditional leadership paradox
    + Leader-Leader vs. Leader-Follower
+ Leader Model- Captain Marguet Four Point Leader
    + Control - given control, not taken control
    + Compentence - provide the tool to be technically competent
    + Clarity - give clear, open and honest goals
    + Courage - trust the Leader-Leader model
+ Start with Why Golden Circle with Human Braon 
    ![diagram](http://healthydealer.com/wp-content/uploads/2017/12/Human-Brain-and-Motivation.jpg)

### Video
[video][vida]

[vida]: https://edx-video.net/LINLFS16/LINLFS162016-V005200_DTH.mp4

### Recommended Resources
+ David Marquet, [Turn the Ship Around! How to Create Leaders at Every Level](https://www.youtube.com/watch?v=iiwUqnvY1l0)
+ Simon Sinek, [How Great Leaders Inspire Action](https://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action?language=en)


## Understanding Organizational Change (Part IV)
### Notes
+ Team Level
    + Conway's Law
    + Technology Adoption Curve
    + Organizational Structures
    + The Schneider Culture Model Assessment
+ Conway's Law:
    + Def: system constrained to produce designs which are copies of the __communciation structures__ of the organization
    + Example: 
        + COBOL compiler w/ 5 develoeprs --> 5 phases
        + ALGO compiler w/ 3 developers --> 3 phases
        + Eric Raymond: 4 groups working on compiler --> 4 pass compiler
+ Conway's Law & DevOps:
    + refactor organization to improve systems
    + how teams are orgined will effect service delivery
    + use Conway's Law for ourselves advantages
    + understand teanm boundaries for service optimization
+ Inverse Conway Maneuver
    + Break down silos that constraint the team's ability to collaborative effective
    + Samll teams (two pizza teams)
    + Colocate teams
    + Work from trunk
+ Hacking Conway's Law
    + SOA
    + Bounded contest (Domain Driven Design)
    + Loosely coupled service oriented architectures w/ bounded context

### Video
[video][vidb]

[vidb]: https://edx-video.net/LINLFS16/LINLFS162016-V004700_DTH.mp4

### Recommended Resources
+ Abhimanyu Ghoshal, [Two-pizza teams: Werner Vogels on Amazon's secrets for innovation at TNV Europe Conference](http://thenextweb.com/insider/2015/04/23/two-pizza-teams-werner-vogels-on-amazons-secrets-for-innovation-at-tnw-europe-conference/)
+ Sam Newman, [Building Microservices](http://samnewman.io/books/building_microservices/)


## Understanding Organizational Change (Part V)
### Notes
+ Technology Adotion Curve
    ![diagram](http://www.jumpassociates.com/wp-content/uploads/2016/08/The-Technology-Adoption-Curve.png)
    + Innovator:
        + typically risk takers
        + have financial or scial capital to take risk
        + higher failure tolerance
        + tren to be good internal champions
    + Early Adaptor
        + similar characteristics of innovators
        + opinion learship
        + more discreet in adoption choices
        + tend to be more centralized than innovators
+ Strategies to be innovator or early adoptors
    + Look for gate keepers
    + Identify champions
    + Identify and manage resistors
    + Defuse cynicism
+ Types of Leaders
    + Opinion leaders - credibility
    + Network leader - Influence
    + Hierarchical leader - Support

### Video
[video][vidc]

[vidc]: https://edx-video.net/LINLFS16/LINLFS162016-V004600_DTH.mp4


## Understanding Organizational Change (Part VI)
### Notes
+ Types of Organizational Structures
    + Functional oriented - optimized for cost
        + designed around expertise
        + hierarchical in structure --> silos
        + defferent teams for systems, networking, security and database
        + more handoffs and longer lead times
        + lead to local optimization
        + lead to bottleneck
    + Matrix oriented - hybrid
        + bridge expertise and speed
        + dotted line cross functional alignment
        + complicated structures
        + can lead to a lack of ownership
    + Market Oriented - optimized for speed
        + fast structure
        + small teams
        + highly coordinated and collaborated
        + tight coordination
        + less handoffs and shorter lead times
        + globally optimized
        + cross functional w/ less bottlenecks
+ The Second Toyota
    + decisive factor: how people act and react
    + success factor: developing capability and habits in its people
    + Paradox - Toyota is Functional oriented - prerequisites
        + high trus
        + transparent workflow
        + managed WIP
        + shared goals
        + generate and accumulate knowledge

### Video
[video][vidd]

[vidd]: https://edx-video.net/LINLFS16/LINLFS162016-V004900_DTH.mp4


## Understanding Organizational Change (Part VII)
### Notes
+ The Schneider Culture Model Assessment
    ![diagram](http://agilitrix.com/wp-content/uploads/2011/03/Schneider-Culture-Model-1024x751.jpg)
    + Collaboration cultre: success by working together
    + Control culture: success by keeping control
    + Competence culture: success by being the best
    + Cultivation culture: success by fulfilling a vision
+ Culture Change Rule - Dpn't fight stupod, make more awesome, Jessie Robbins
    + start small, build trust and safety
    + create champions
    + use metric to gain confidence
    + celebrate success
    + exploit compelling events

### Video
[video][vide]

[vide]: https://edx-video.net/LINLFS16/LINLFS162016-V005000_DTH.mp4

### Recommended Resources
+ Pedro Canahuati, [Growing from the Few to the Many: Scaling the Operations Organization at Facebook](https://www.infoq.com/presentations/scaling-operations-facebook)
+ Velocity 2012 - Jesse Robbins, [Changing Culture & Being a Force for Awesome](https://www.youtube.com/watch?v=OU8ihx3nT6I)


## Understanding Organizational Change (Part VIII)
### Notes
+ NUMMI
    + GM & Toyota join venture
    + GM: mass production, Taylorism, extrinsic motivation
    + TPS: 
        + teamwork
        + kaizen
        + intrinsic
        + kata
    + It was the system taht make it bad, not the people

### Video
[video][vidf]

[vidf]: https://edx-video.net/LINLFS16/LINLFS162016-V004800_DTH.mp4

### Recommended Resources
+ [561: NUMMI 2015 - This American Life](http://www.thisamericanlife.org/radio-archives/episode/561/nummi-2015)


# Section 3: Enabling Transformation
## Enabling Transformation (Part I)
### Notes

### Video
[video][vidg]

[vidg]: https://edx-video.net/LINLFS16/LINLFS162016-V005300_DTH.mp4

## Enabling Transformation (Part II)
### Notes

### Video
[video][vidh]

[vidh]: https://edx-video.net/LINLFS162016-V011800_DTH.mp4

### Recommedned Resources
+ Jennifer Davis and Katherine Daniels, [Effective DevOps: Building a Culture of Collaboration, Affinity and Tooling at Scale](https://www.amazon.com/Effective-DevOps-Building-Collaboration-Affinity/dp/1491926309)
+ John Kotter, [The Heart of Change: Real-Life Stories of How People Change Their Organizations](https://www.amazon.com/Heart-Change-Real-Life-Stories-Organizations/dp/1422187330)


# Summary
## Notes

## Video
[video][vidi]

[vidi]: https://edx-video.net/LINLFS16/LINLFS162016-V005400_DTH.mp4

# Knowledge Check
Q1. Which type of value stream is associated with the Strangler Pattern?

    a. Legacy
    b. Brownfield
    c. Greenfield

    Ans: b

Q2. Which of the following tools is used to map out value streams?

    a. Value Stream Marketing
    b. Value Stream Mapping
    c. Value Stream Management
    d. Value Stream Map

    Ans: b

Q3. Which of the following statements best describes Conway's Law?

    a. Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.
    b. Organizations which design systems copy the designs of the communication structures of these organizations.
    c. Organizations which decouple systems are constrained to produce designs which are copies of the communication structures of these organizations.
    unanswered

    Ans: a

Q4. Which of the following examples best describes a growth mindset?

    Ans: alternative belief, effort based, developed abilities through dedicationa nd hard work

Q5. Which of the following best describes the significance of the NUMMI story?

    a. The same workers can change their habits in a transformative culture
    b. Plants managed by Toyota are better than plants managed by GM
    c. Culture does not matter when it comes to managing factories

    Ans: a

