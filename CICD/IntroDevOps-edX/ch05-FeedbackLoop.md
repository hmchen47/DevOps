Chapter 5: The Second Way, [Amplify Feedback Loops
==================================================


# Learning Objectives
+ Discuss the concept and goals of the Second Way.
+ Explain the meaning of creating a service reliability culture.
+ Decouple the definitions of service and their implications both for the external customers and internal objectives.
+ Discuss the balance between reliability and risk.
+ Discuss the origin and practice of Google’s Service Reliability Engineering team structure.
+ Explain the origins, definitions and aspects of feedback loops.
+ Discuss the meta-principles of monitoring via alerting, trending, and anomaly detection.
+ Monitor a service from all aspects of the service delivery.
+ Discuss complexity as it relates to the Second Way.
+ Outline how the use of ChatOps can help provide fast and effective feedback.


# Section 1: Creating a Service Reliability Culture
## Creating a Service Reliability Culture (Part I)
### Notes
+ Service Reliability Culture
    + Availability
    + Latency
    + Performance
    + Change Management
    + Monitoring
    + Emergency Response
    + Capacity Planning
+ Core Conflcit of Dev & OPs
    + Operations don't really know the code base
    + The operation teams knows least about the code typically has the responsibility of its launch

### Video
[video][vid1]

[vid1]: https://edx-video.net/LINLFS162016-V008500_DTH.mp4

### Recommended Resources
+ [Site Reliability Engineering: How Google Runs Production Systems](http://shop.oreilly.com/product/0636920041528.do)


## Creating a Service Reliability Culture (Part II)
### Notes
+ Service Levels
    + Service Level Agreements (SLA)
    + Service Level Objectives (SLO)
    + Service Level Indicators (SLI)
+ Service Level Agreements (SLA)
    + between the business and the customers
    + typically a financial contract
    + can be MTTR & MTBF based
    + not all service has an explicit SLA
+ Service Level Objectives (SLO)
    + Definition
        + Typically the basis of SLAs
        + between the service and the system
        + typically target based
        + all services should have an SLO
        + determine actions to take on missed SLOs
    + Picking Targets
        + Try and keep the sample
        + Don't over design
        + Let them envolve
        + Will learn over time
+ Service Level Indicators (SLI)
    + Definition:
        + Quantaative measure of a service
        + Used as indicators of the SLOs
        + Monitor SLIs and compare to SLOs
    + Eamples:
        + Latency
        + Errors
        + Availability
        + Throughput
+ Generalized Indicators
    + Management By Objectives (MBO)
    + Key Performance Indicators (KPI)
    + Objective and Key Results (OKR)

### Video
[video][vid2]

[vid2]: https://edx-video.net/LINLFS162016-V008400_DTH.mp4


## Creating a Service Reliability Culture (Part III)
### Notes
+ Risk & Failure
    + myth: 100 reliability
        + all systems go down
        + not all service equal
    + manage by service\
    + manageing reliability = manageing risk
    + managing risk = cost
+ The Cost of Reliability - tradeoff
    + High availability systems
    + Opportunity cost

### Video
[video][vid3]

[vid3]: https://edx-video.net/LINLFS162016-V008300_DTH.mp4

### Recommended Resources
+ USENIX 2014 - Ben Treynor Sloss, [Keys to SRE](https://www.youtube.com/watch?v=n4Wf14e2jxQ)


## Creating a Service Reliability Culture (Part IV)
### Notes
+ Site Reliability Engineers
    + title created by Google in 2003
    + No NOC
    + team focuses on reliability -> Service + Engineering
+ Google Pratices
    + Hire only coder
    + Have an SLA for your service
    + Measure and report performance against the SLA
    + Use Error Budgets and gate launches on them
    + Common satffing pool for SRE and Develoeprs
    + Excess Operational work overflow to the Development team
    + Cap SRE operational load at 50%
    + Shae 5% of Ops w/ the Dev team
    + On-call team: >= 8 for single location and >=6/site for multiple locations
    + Aim for a maximum of 2 events / oncall shift
    + Do a postmortem for every event
    + Postmortem: blameless and focusing on process and technology
+ Error Budget
    + DON'T for Google SRE
        + Access launch
        + Avoid outage
        + Set release policy
    + Theory: 100% reliability is a wrong target for bascially everything
    + Service objective -1 is the unavailability service's error budget -> resolve the dev (create new) ops (protect the infrastructure) conflict
    + Dev teams self police
    + The service team gets to take SLA-1 feature/risk velocity
+ LRR/HRR:
    + Launch Readiness Review (LRR)
        + Sign-off before any service goes life
        + ZDevelop-er managed state
    + Handoff Readiness Review (HRR)
        + Sign-off for a service at high acceptance
        + Operations managed state
    + The Service Handbook
        + process to put a service back to developer managed status
+ Google and Operational Work
    + SRE operational work: 50%
    + SRE imporovement work: 50%
    + operational work = on-call + interrupt driven work
    + Types of work
        + Software engineering: developing and design
        + System engineering: configuration system (sysadmin work)
        + Toil: manual, not repeated work
        + Overhead: administration, HR and training
    + Goals:
        + create good moral
        + create positive career growth
        + Create clearer communication
        + Unset bad precedents
        + Keep good failth
    + Areas for further Investigation
        + On call support
        + Create positive career
        + emergency response
        + incident management
        + outages

### Video
[video][vid4]

[vid4]: https://edx-video.net/LINLFS162016-V008200_DTH.mp4

### Recommended Resources
+ [Site reliability Engineering](http://shop.oreilly.com/product/0636920041528.do)


## Creating a Service Reliability Culture (Part V)
### Notes
+ NASA Stories
    + Margaret Hamilton: Pre-launch document to save Applo 13
    + Gene Kranz: book for emergency reponse gto Applo 13
    + Diane Vaughan: 
        + Therory of the Normalization of Deviance
        + blind sport/outcome bias
        + Challenger launch decision

### Video
[video][vid5]

[vid5]: https://edx-video.net/LINLFS162016-V008600_DTH.mp4

### Recommended Resources
+ Wired, [Her Code Got Humans on the Moon - And Invented Software Itself](https://www.wired.com/2015/10/margaret-hamilton-nasa-apollo/)
+ Gene Kranz, [Failure Is Not an Option: Mission Control From Mercury to Apollo 13 and Beyond](https://www.amazon.com/Failure-Not-Option-Mission-Control/dp/1439148813)
+ Diane Vaughan, [The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA](https://www.amazon.com/Challenger-Launch-Decision-Technology-Deviance/dp/0226851761)
+ Steven Spear, [The High-Velocity Edge: How Market Leaders Leverage Operational Excellence to Beat the Competition](https://www.amazon.com/High-Velocity-Edge-Operational-Excellence-Competition/dp/0071741410)


## Creating a Service Reliability Culture (Part VI)
### Notes
+ Concepts of Anomaly Response:
    + Coputers do not resolve outages ... people do
    + Trade-offs under pressure
    + Cognition in the wild
        + An outage is not a detective story
        + With each step, the story changes
    + Need to see what's happening with incomplete info
    + Tools don't always make things better
+ Internet Service are Opaque
    + Network layer architectures
    + Varability in network performance
    + Interdependent and decoupled services
    + Internet based distributed computing
    + Geographically distributed communication
    + Open Internet facing interactions
+ Challenges
    + Team work
    + Communciation
    + Diagnosis
    + Decision making
    + Coordination
    + Improvisation
    + Tooling
+ Dynamic Fault Management
    + Cascading effects
    + Temporary changes and time pressure
    + Multiple Interleaved tasks
    + Multiple interacting goals
    + Need to revise assessments as new evidence comes in
+ Model of reasoning in Anomaly Response

### Video
[video][vid6]

[vid6]: https://edx-video.net/LINLFS162016-V008700_DTH.mp4


### Recommended Resources
+ John Allspaw and Paul Hammond, [10+ Deploys Per Day](https://www.youtube.com/watch?v=LdOe18KhtT4)
+ John Allspaw, [Trade-Offs Under Pressure: Heuristics and Observations of Teams Resolving Internet Service Outages](https://drive.google.com/file/d/0Bx50LgK_RXNmUTRDSUhyam9ranM/view)
+ John Allspaw, [Incident Response: Trade-offs Under Pressure](https://www.infoq.com/presentations/incident-response)
+ Amazon.com, [Summary of the AWS Service Event in the US East Region](https://aws.amazon.com/message/67457/)


## Creating a Service Reliability Culture (Part VII)
### Notes
+ Heuristic Approaches for Abnomaly Response
    + 1st Heuristic: Look for correlation btw the behavior and any recent changes made in the software
    + 2nd Heuristic: Widen the search to any potential contributors imaged
    + 3rd Heuristic: Validate hypothesis that most easily come to mind
    + 4th Heuristic: Rely on peer review of changes more than automated testing
+ Furthyer Research
    + Distributed cognition
    + Plan and situated actions
    + Directed attention and alert design
    + Expertise

### Video
[video][vidy]

[vidy]: https://edx-video.net/LINLFS162016-V008800_DTH.mp4


# Section 2: Fast Feedback
## Fast Feedback (Part I)
### Notes
+ Fast Feedback
    + Design for Failure
    + Adaptive stsrems - Feedback Loops
    + Developer managed services
    + Contigency, peer review and pairing
    + Embedded engineers
+ Activities for Design for Failure w/ High Performance Organizations
    + MTTR over MTBF
    + Game Days
    + Chaos Monkey(s)
    + Fault Injection
+ Game Days
    + Reduces MTTR
    + Reduces MTBF
+ Netflix Simian Army
    + Chaos Monkey (Hosts)
    + Chaos Gorilla (Data Center)
    + Latency Monkey (Inject Latency)
    + Conformity Monkey (Best Practice)
    + Security Monkey (Security Violations)
+ Fault Injection Testing (FIT)
    + Limit the blast ratio of the failure
    + Telemetry of path of the filaure
    + Dependency telemetry
+ Deploys - Upgrading Live Services
    + Rolling upgrades
    + Canary
    + Blue-Green Deploys
    + Toggling features
+ Methodologies for Fast Feedback
    + A/B testing
    + Dark deploys
    + Inject Deployment Metrics in Monitoring

### Video
[video][vidz]

[vidz]: https://edx-video.net/LINLFS162016-V009300_DTH.mp4

### Recommended Resources
+ Jesse Robbins, Kripa Krishnan, John Allspaw, and Tom Limoncelli, [Resilience Engineering: Learning to Embrace Failure](http://queue.acm.org/detail.cfm?id=2371297)
+ Jez Humble, Joanne Molesky, and Barry O'Reilly, [Lean Enterprise](https://www.amazon.com/Lean-Enterprise-Performance-Organizations-Innovate/dp/1449368425)
+ Gene Kim, Jez Humble, Patrick Debois, and John Willis, [The DevOps Handbook](https://www.amazon.com/DevOps-Handbook-World-Class-Reliability-Organizations/dp/1942788002)
+ Jesse Robbins, [GameDay: Creating Resiliency Through Destruction](https://www.youtube.com/watch?v=zoz0ZjfrQ9s)
+ John Allspaw, [Fault Injection in Production: Making the Case for Resilience Testing](http://queue.acm.org/detail.cfm?id=2353017)
+ The Netflix Tech Blog, [The Netflix Simian Army](http://techblog.netflix.com/2011/07/netflix-simian-army.html)
+ The Netflix Tech Blog, [FIT: Failure Injection Testing](http://techblog.netflix.com/2014/10/fit-failure-injection-testing.html)

### Extra Resources
+ Tom Limoncelli, [The Practice of Cloud System Administration, vol 2](https://www.amazon.com/Practice-Cloud-System-Administration-Distributed-ebook/dp/B00N7N2CRQ)


## Fast Feedback (Part II)
### Notes
+ System Thinking
    + Look at system as a whole
    + Global Efficiency vs Local Efficiency
    + Feedback loops vs cause-and-effect
    + Trends not target
    + The system is greather than the sum of parts
+ Feedback Originates from System Theory
    + Accelerating Loop - Amplifies behavior
    + Diminishing Loop - Suppresses behavior
    + Balancing Loop - Toward a stable goal
    + Thrashing Loop - Oscilating between states
+ Impacts on Feedback
    + Delay in feedback increases drift
    + Limit options
    + Increases processing effort
+ Designing Delivery
    + Design for failure
    + Designing for services, not just software
    + Minimizing latency and maximizing feedback
    + Designing for failure and operating to learn
    + Using operations as input to design to learn
    + Seeking empathy
+ Developers wear Pager - Google
    + 1st call: dev rotation team
    + 2nd call: VP of Engineering
    + 3rd call: CTO
+ Developers Operate the Service
    + Launch
    + Monitor
    + Guidance from operations

### Video
[video][vid7]

[vid7]: https://edx-video.net/LINLFS162016-V009100_DTH.mp4

### Recommended Resources
+ Peter Senge, [The Fifth Discipline: The Art & Practice of The Learning Organization](https://www.amazon.com/Fifth-Discipline-Practice-Learning-Organization/dp/0553456342)
+ Donella Meadows, [Thinking in Systems](https://www.amazon.com/Thinking-Systems-Donella-H-Meadows/dp/1603580557)
+ InfoQ - Dan North, [Making a Sandwich - Effective Feedback Techniques](https://www.infoq.com/presentations/feedback-models-techniques)
+ Jeff Sussna, [Designing Delivery: Rethinking IT in the Digital Service Economy](http://shop.oreilly.com/product/0636920033080.do)


## Fast Feedback (Part III)
### Notes
+ Contigency
    + Some release need contigency reviews
    + Go/No Go for major releases
    + Universal agreement for launch
+ Practice: Esty 10 Minutes Review
    + Teams
        + Product
        + Development
        + Operations
        + Design
        + Communit
        + Support
    + Taks
        + When will it be launched
        + Who is launching it
        + Has it been in production yet
        + Can it be dark, feature or percentage launched
        + Is it new infrastructure
        + Has an on/off switch
        + All parties available at launch time
        + Contigency checklist
+ Peer Review
    + All changes are peer reviewed
    + Everyone monitors the commit logs
    + High risk changes should include an SME (Suject Matter Expert)
    + Break up larger changes into smaller ones
+ Pairing Programming
    + Pair programming for everything
    + Pair programming is slower but decreases bugs up to 70~80%
    + Spread knowledge
    + Great for training
    + Setup pair times
    + Need a cluture that value pair programming
+ Embedded Engineers
    + Operations in Development
    + Development in Operations

### Video
[video][vid8]

[vid8]: https://edx-video.net/LINLFS162016-V009200_DTH.mp4

### Recommended Resources
+ John Allspaw, [Go or No-Go: Operability and Contingency Planning at Etsy.com](http://www.slideshare.net/jallspaw/go-or-nogo-operability-and-contingency-planning-at-etsycom)


## Fast Feedback (Part IV)
### Notes
+ ChatOps
    + Definition (Atlassian): a collaboraton model that connect people, tools, process and autiomation into a transparent workflow
    + Origins
        + based on chat bot
        + GitHub use Hubot
        + putting tools in the middle of the conversation
    + Primary engines
        + Hubot (Node-based, Coffee-script)
        + Lita (Ruby)
        + Er (Python)
    + Chat Tools
        + Slack (w/ Hubot -> popular)
        + Compfile (37 signals)
        + Hipchat (Altassian)
+ Benefits of ChatOps
    + a multiuser terminal where everyone can see the conversation and the commands interoven
    + historical records of the commands and the conversaton
    + training tool - teaching by doing
    + tactical incident resolution - everyone gets to see the commands and the conversation
    + dynamically manage the on-call rotation
    + manage all aspects of the devops practices from one central place
    + mobile operations for free

### Video
[video][vid9]

[vid9]: https://edx-video.net/LINLFS162016-V009400_DTH.mp4

### Recommended Resources
+ Attlassian Blogs - Sean Regan, [What is ChatOps? A guide to its evolution, adoption, and significance](http://blogs.atlassian.com/2016/01/what-is-chatops-adoption-guide/)
+ Jesse Newland, [ChatOps at GitHub](https://www.youtube.com/watch?v=NST3u-GjjFw)
+ Jason Hand (VictorOps), [Real World ChatOps](https://www.youtube.com/watch?v=X9FLsMup0A0)
+ Jason Hand (VictorOps), [ChatOps Unplugged: A Beginner's Guide](https://www.youtube.com/watch?v=1srw4yjQcN0)
+ GitHub Blog, [Say Hello to Hubot](https://github.com/blog/968-say-hello-to-hubot)


# Section 3: Understanding Monitoring
## Understanding Monitoring (Part I)
### Notes
+ Culture of Causality
    + change --> 80% outages
    + ficguring out what changes --> 80% restoration times
    + looking for the most recent change first
+ Monitoring Mathodologies
    + Altering - emailo, web page, graph
    + Visualizaing - dashboard, change, graph
    + Collecting - how to collect, usage, diagonistic
    + Trending - direction, growing, shrinking
    + Learning - machine learning
+ Google's Four Golden Signals
    + Latency
    + Traffic
    + Errors
    + Saturation
+ Indicators of Service Stack
    + Business Indicators
    + Application Indicators
    + Infrastructure Indicators
    + User based Indicators
    + Deployment Indicators
+ Case Studies -the most important matric
    + Amazon: order rate
    + Facebook: packet loss for all layer and systems
    + Alaska Air: time, logistics, how fast to get into gate, door open

### Video
[video][vid0]

[vid0]: https://edx-video.net/LINLFS162016-V009700_DTH.mp4


### Recommended Resources
+ Kevin Behr, Gene Kim, George Spafford, [The Visible Ops Handbook](https://www.amazon.com/Visible-Ops-Handbook-Implementing-Practical/dp/0975568612)
+ Mike Brittain, [Tracking Every Release (Code as Craft Blog)](https://codeascraft.com/2010/12/08/track-every-release/)
+ Petr Lapukhov (Facebook), [Move Fast, Unbreak Things!](https://www.youtube.com/watch?v=zs2Zn9rW3Ow)
+ ChefConf 2016 - Veresh Sita, [Alaska Airlines](https://www.youtube.com/watch?v=mGJkhuRlvTo)


## Understanding Monitoring (Part II)
### Notes


### Video
[video][vida]

[vida]: https://edx-video.net/LINLFS162016-V009600_DTH.mp4


### Recommended Resources
+ Tom Limoncelli, [The Practice of Cloud System Administration](https://www.amazon.com/Practice-Cloud-System-Administration-Distributed/dp/032194318X)
+ James Turnbull, [The Art of Monitoring](https://www.amazon.com/Art-Monitoring-James-Turnbull-ebook/dp/B01GU387MS)
+ Gene Kim, Jez Humble, Patrick Debois, John Willis, [The DevOps Handbook](https://www.amazon.com/DevOps-Handbook-World-Class-Reliability-Organizations/dp/1942788002)
+ [Site Reliability Engineering: How Google Runs Production Systems](http://shop.oreilly.com/product/0636920041528.do)
+ iSixSigma Blog, [Variation - The Root of All Process Evil](https://www.isixsigma.com/tools-templates/variation/variation-root-all-process-evil/)
+ [The Flaw of Averages](http://www.flawofaverages.com/)
+ Michael Kopp, [Why Averages Suck and Percentiles are Great](http://apmblog.dynatrace.com/2012/11/14/why-averages-suck-and-percentiles-are-great/)
+ [Khan Academy](https://www.khanacademy.org/)


## Understanding Monitoring (Part III)
### Notes


### Video
[video][vidb]

[vidb]: https://edx-video.net/LINLFS162016-V009800_DTH.mp4

### Recommended Resources
+ Theo Schlossnagle, [Adaptive Availability for Quality of Service](https://www.infoq.com/presentations/time-series-database)
+ Theo Schlossnagle, [Adaptive Availability](http://www.slideshare.net/postwait/adaptive-availability)

## Understanding Monitoring (Part IV)
### Notes


### Video
[video][vidc]

[vidc]: https://edx-video.net/LINLFS162016-V009500_DTH.mp4

### Recommended Resources
+ Jason Dixon, [Monitoring with Graphite](https://www.amazon.com/dp/1491916435)
+ James Turnbull, [The Art of Monitoring](https://www.amazon.com/Art-Monitoring-James-Turnbull-ebook/dp/B01GU387MS)
+ Varun Chandola, Arindam Banerjee, & Vipin Kumar, [Anomaly Detection: A Suervey](http://www-users.cs.umn.edu/~banerjee/papers/09/anomaly.pdf)
+ The Netflix Tech Blog, [RAD, Outlier Detection on Big Data](http://techblog.netflix.com/2015/02/rad-outlier-detection-on-big-data.html)
+ David Goldberg, [Statistical Anomaly Detection](http://www.ebaytechblog.com/2015/08/19/statistical-anomaly-detection/)
+ David Golberg, Yinan Shan, [The Importance of Features for Statistical Anomaly Detection](https://www.usenix.org/sites/default/files/conference/protected-files/hotcloud15_slides_goldberg.pdf)


# Section 4: Understanding Complexity
## Understanding Complexity (Part I)
### Notes


### Video
[video][vidd]

[vidd]: https://edx-video.net/LINLFS162016-V010100_DTH.mp4

### Recommended Resources
+ Eliyahu Goldratt, [Beyond the Goal: Theory of Constraints](https://www.amazon.com/dp/B000ELJ9NO)
+ Gene Kim, Kevin Behr, George Spafford, [The Phoenix Project](https://www.amazon.com/Phoenix-Project-DevOps-Helping-Business/dp/0988262592)
+ Eliyahu Goldratt, [The Goal](https://www.amazon.com/Goal-Process-Ongoing-Improvement/dp/0884271951)
+ Gene Kim, Jez Humble, Patrick Debois, John Willis, [The DevOps Handbook](https://www.amazon.com/The-DevOps-Handbook-World-Class-Organizations/dp/1942788002)
+ Mark Burgess, [In Search of Certainty: The science of our information infrastructure](https://www.amazon.com/Search-Certainty-science-information-infrastructure/dp/1492389161)
+ Jeff Sussna, [Designing Delivery: Rethinking IT in the Digital Service Economy](http://shop.oreilly.com/product/0636920033080.do)
+ Jeff Sussna, [From Cybernetics to DevOps and Beyond (DevOps Days Belgium, 2014)](https://vimeo.com/114017635)
+ David Snowden, Mary Boone, [A Leader's Framework for Decision Making](https://hbr.org/2007/11/a-leaders-framework-for-decision-making)
+ [Cognitive Edge](http://cognitive-edge.com/)


## Understanding Complexity (Part II)
### Notes


### Video
[video][vide]

[vide]: https://edx-video.net/LINLFS162016-V009900_DTH.mp4


### Recommended Resources
+ Mike Nygard, [Release It!: Design and Deploy Production-Ready Software](https://www.amazon.com/Release-Production-Ready-Software-Pragmatic-Programmers/dp/0978739213)
+ DevOps Cafe, [Episode 50: Adrian Cockcroft](http://devopscafe.org/show/2014/7/22/devops-cafe-episode-50-adrian-cockcroft.html)
+ Martin Fowler, [CircuitBreaker](http://martinfowler.com/bliki/CircuitBreaker.html)
+ Ben Christensen, [Introducing Hystrix for Resilience Engineering (The Netflix Tech Blog)](http://techblog.netflix.com/2012/11/hystrix.html)


## Understanding Complexity (Part III)
### Notes


### Video
[video][vidf]

[vidf]: https://edx-video.net/LINLFS162016-V010000_DTH.mp4

### Recommended Resources
+ Mark Burgess, [Thinking in Promises: Designing Systems for Cooperation](https://www.amazon.com/Thinking-Promises-Mark-Burgess/dp/1491917873)
+ Mark Burgess, [In Search of Certainty: The science of our information infrastructure](https://www.amazon.com/Search-Certainty-science-information-infrastructure/dp/1492389161)
+ Jeff Sussna, [Designing Delivery: Rethinking IT in the Digital Service Economy](http://shop.oreilly.com/product/0636920033080.do)
+ John Willis, [Promise Theory for Dummies](https://www.youtube.com/watch?v=y3yplqTFywY)


# Summary
## Notes


## Video
[video][vidh]

[vidh]: https://edx-video.net/LINLFS162016-V010300_DTH.mp4


# Knowledge Check
Q01. Which of the following statements best explains the primary difference between an SLA and an SLO, as described in the course? Please select the correct answer.
    a. An SLA is based between the internal service team and the system in which it operates and an SLO is based between the business and the customer.
    b. An SLA is based between the internal service team and the system in which it operates and an SLO is based on the organizational chart.
    c. An SLA is based between the business and the customer and an SLO is based between the internal service team and the system in which it operates.
    d. An SLA is based between the developers and the customer and an SLO is based between the operations team and the customer.

    Ans: c

Q02. What was Diane Vaughan’s significant contribution, as discussed in this chapter? Please select the correct answer.
    a. She studied the NASA Challenger disaster and coined the concept of “Deviance of Normalization”.
    b. She studied under Sydney Dekker, and co-authored “Drift into Failure”.
    c. She studied the NASA Challenger disaster and coined the concept of “Normalization of Deviance”.
    d. She studied under John Allspaw and coined the concept of “Normalization of Deviance”.
    unanswered

    Ans: c

Q03. Which of the statements below is True? Please select the correct answer.
    a. Accelerating Loop - Accelerates suppressive behavior, and Diminishing Loop - Diminishes feedback
    b. Balancing Loop - Moves towards an unstable goal, and Thrashing Loop - Oscillates between states
    c. Accelerating Loop - Amplifies behavior, and Diminishing Loop - Diminishes feedback
    d. Accelerating Loop - Amplifies behavior, and Diminishing Loop - Suppresses behavior

    Ans: d


Q04. Which of the following is not one of the five layers of a monitoring stack, as discussed in this chapter? Please select the correct answer.
    a. Business indicators
    b. Application indicators
    c. Infrastructure indicators
    d. CPU utilization
    e. Deployment indicators

    Ans: d


Q05. Given the following vector, "X=c(2,4,4,4,5,5,7,9)", what is the Mean, Median and Standard Deviation? Please select the correct answer.
    a. Mean=5, Median=4.5, Standard Deviation=2.1
    b. Mean=4, Median=4.5, Standard Deviation=1.5
    c. Mean=5, Median=5, Standard Deviation=2.1
    d. Mean=4, Median=4.5, Standard Deviation=1.5

    Ans: a


Q06. In the 68-95-99.7 Rule, which value would be 3 Sigma? Please select the correct answer.
    a. 68
    b. 65
    c. 99.9
    d. 99.7

    Ans: d


Q07. Who was the primary author of Cybernetics? Please select the correct answer.
    a. Sydney Dekker
    b. Jeff Sussna
    c. Norbert Weiner
    d. Gene Kim

    Ans: c


Q08. Which of the following is not part of Cynefin? Please select the correct answer.
    a. Obvious
    b. Correlated
    c. Complicated
    d. Chaotic
    e. Complex

    Ans: b

Q09. Which of the following open source projects is based on Mike Nygard's Circuit Breaker Patterns concept? Please select the correct answer.
    a. Nginx
    b. Hystrix
    c. Spring Boot
    d. Chaos Monkey

    Ans: b


Q10. Which of the following companies created ChatOps? Please select the correct answer.
    a. Etsy
    b. Netflix
    c. GitHub
    d. Atlassian

<<<<<<< HEAD
    Ans: c
=======
    Ans: 
>>>>>>> doch6

