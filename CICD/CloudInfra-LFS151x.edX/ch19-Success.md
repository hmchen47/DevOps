# Chapter 19. How to Be Successful in the Cloud

## Introduction and Learning Objectives
### Think Like a Startup, Act Like an Enterprise
With cloud computing's _pay-as-you-go_ and _software-defined everything_ models, startups now have a very low barrier to take an enterprise assignment. And, with Open Source tools and ecosystems built around them, startups can innovate and adapt very fast.

Any company, be it small or big, has to innovate fast, listen to customer feedback and then iterate over it. To do that, companies need to bring in DevOps practices and allow small teams to manage the entire lifecycle of their products, from Development to Support. Technologies like __Container as a Service__ and __Continuous Integration and Deployment__ allow small teams to have access of Development, QA and Deployment environments. This allows individual teams that work in an enterprise to work like startups, which is good for the business.

### Learning Objectives
By the end of this chapter, you should be able to:

+ Discuss what aspects of the cloud you need to know in order to develop your skill set and stay competitive.
+ Explain what challenges can individuals and companies face when transitioning to cloud technologies.

## Developing Skills
### Where Do We Go?
Nowadays, IT is becoming part of the business process. Due to the emergence of cloud technologies, DevOps, Microservices architecture, etc., each business is expected to respond to customer feedback sooner rather than later.

__Container technologies__ like Docker and their ecosystems are helping us standardize and streamline the way we package and deploy code. If we want to adopt the technologies we discussed in this course, we realize that Developers, QA and OPs cannot work in silos. To be efficient and successful, they have to work together and need to have basic knowledge about each others' workflows. This is very different from the traditional IT approach and has an initial steep learning curve. The bigger the company is, the bigger the challenge becomes.

### Developing The Necessary Skills Set
Though not everyone has to master all the topics we have discussed in this course, you should at least have a basic understanding of the following:

+ Different cloud offerings (__IaaS, PaaS, SaaS__), and cloud models (__Public, Private__, and __Hybrid__)
+ Container technologies like Docker, rkt, and their ecosystem
+ DevOps
+ Continuous Integration and Continuous Deployment
+ Software Defined Networking and Storage
+ Debugging, Logging, and Monitoring cloud applications.


## Challenges
### About Challenges
Once you decide to move to the cloud, you will inevitably face some challenges. Most of them you will encounter for the first time. In this section, we will talk about some of the challenges that you may encounter in your journey to the cloud.

### Choosing the Right Cloud Provider
There are different cloud providers like __Amazon AWS, Google Cloud Platform, Microsoft Azure, OpenStack__, etc. Each of them provides different services.

Similarly, there are different cloud models like Public, Private, and Hybrid. Each of them has their advantages and shortcomings. For example, the Hybrid model is useful when you want to keep your data on-premise and serve the request from Public clouds.

Companies have to spend a significant amount of time to evaluate different cloud providers and models in the beginning, as it effects the overall operations and costs.

### Choosing the Right Technology Stack
To avail fully of the benefits provided by the Cloud, we have to choose the right technology stack as well. For example, should we go for IaaS or PaaS solutions? Should we choose VMs or containers to deploy the applications? Most of these questions have multiple answers. As a company, you need to hire cloud architects who can make the right decision for you.

### Security Concerns
Security is one of the biggest concerns when moving towards the cloud. Companies worry about privacy, data access, accountability, account control, multi-tenancy, etc. For example, with 100% Public Cloud deployment, the entire data is managed on the cloud, which is not the preferred way for many companies and may not comply with regulations like [FISMA][fisma] (Federal Information Security Modernization Act) or [HIPAA][hipaa] (Health Insurance Portability and Accountability Act). In such cases, companies adopt the Hybrid Cloud approach.

Organizations like the [Cloud Security Alliance (CSA)][csa] “promote the use of best practices for providing security assurance within Cloud Computing, and to provide education on the uses of Cloud Computing to help secure all other forms of computing”.

Nowadays, there are many third-party tools available which can do security audits for applications deployed on the cloud.

### Cloud Cost Management
Studies say that, by moving to the cloud, an organization can save a good amount of money as compared to setting up on-premise solutions. One thing we have to be very careful with is to ensure that we know when this is true, and when it is not, for any given use-case. Most of the cloud providers can now predict and manage the cost based on usage, which can help companies keep track of their spending.

### Vendor Lock-In
Companies also worry about vendor lock-in when it comes to cloud computing. Cloud providers allow migration from other providers, but that is not an ideal solution. With containers becoming mainstream and using innovative solutions like __Docker Universal Control Plane, Nomad, Kubernetes__, etc. on top of them, we can deploy the applications across data-centers on top of different cloud providers. The use of containers definitely addresses part of the vendor lock-in problem.

### Resistance from Existing Employees
This is one of the biggest challenges companies are facing. With cloud technologies, the existing workflow is changing dramatically, and that is the need of the hour: to keep up with the business demands. A lot of the times, many IT employees resist learning new things and changing their ways, which is not good for the business. To avoid or minimize this problem, the top management of a company has to guide its employees through the change process of learning new technologies. On the other hand, as an employee, you should also be committed to continuous education and lifelong learning, as learning new things will help you stay relevant in a competitive and ever-changing industry.


## Knowledge Check
Q. Which of the following challenges are faced by an organization moving to the cloud? 

    Ans: Choosing the Right Cloud Provider, Choosing the Right Technology Stack, Security Concerns, Cloud Cost Management, Vendor Lock-In, Resistance from Existing Employees


[fisma]: https://www.dhs.gov/fisma
[hipaa]: https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act
[csa]: https://cloudsecurityalliance.org/




