# Chapter 9. Microservices

## Introduction and Learning Objectives
### Microservices
According to Wikipedia, 

> "__Microservices__ are small, independent processes that communicate with each other to form complex applications which utilize language-agnostic APIs. These [services][svc] are small building blocks, highly [decoupled][decop] and focused on doing a small task, facilitating a [modular][modul] approach to [system-building][system].  The microservices architectural style is becoming the standard for building continuously deployed systems."

In this chapter, we will focus on microservices and their role in today's cloud environment.

### Learning Objectives
By the end of this chapter you should be able to:

+ Explain the concept of microservices.
+ Discuss the benefits and challenges of using microservices.


## Microservices
### The Technological Advancement towards Microservices
Over the last decade, building the right kind of tooling around virtualization and cloud management has accelerated the adoption and consumption of cloud technologies. Below we provide some relevant examples:

+ With the launch of Amazon Web Services (AWS) in 2006, we can get compute resources on demand from the web or the command-line interface. 
+ With the launch of [Heroku][heroku] in 2007, we can deploy a locally-built application in the cloud with just a couple of commands.
+ With the launch of [Vagrant][vagrant] in 2010, we can easily create reproducible development environments.

With tools like the ones above in hand, software engineers and architects started to move away from large monolith applications, in which an entire application is managed via one code-base. Having one code-base makes the application difficult to manage and scale.

Over the years, with different experiments, we evolved towards a new approach, in which a single application is deployed and managed via a small set of services. Each service runs its own process and communicates with other services via lightweight mechanisms like REST APIs. Each of these services is independently deployed and managed. Technologies like containers and unikernels are becoming default choices for creating such services.

![image][img1]

Figure 9.1: Monoliths and Microservices 

### How to Break a Monolith into Microservices
We have been designing applications for decades and have a very good understanding of modularizing the code. In simpler terms, we can create a microservices environment by extending those modules into individual services. Though there is no rule of thumb to follow every time we break a monolith into microservices, there are some approaches that we can look at:

+ If you have a complex monolith application, then it is not advisable to rewrite the entire application from scratch. Instead, you should start carving out services from the monolith, which implement the desired functionalities for the code we take out from the monolith. Over time, all or most functionalities will be implemented in the microservices architecture.
+ We can split the monoliths based on the business logic, front-end (presentation), and data access. In the microservices architecture it is recommended to have a local database for individual services and. If the services need to access the database from other services, then we can implement an event-driven communication between these services. 
+ As mentioned earlier, we can split the monolith based on the modules of the monolith application and each time we do it, our monolith shrinks. 

Also, if we need a new functionality while we are converting the monolith to microservices, then we should create a microservice instead of adding more code to the monolith. 

### Benefits of Microservices
Next, we will highlight some of the benefits of microservices:

+ __No language or technology lock-in__

    As each service works independently, we can choose any language or technology to develop it. We just need to make sure its API end points return the expected output.

+ __Easy Deployment__

    Each service in a microservice can be deployed independently.

+ __Updating and Scaling__
    
    We do not have to take an entire application down just to update or scale a component. Each service can be updated or scaled independently. This gives us the ability to respond faster.

+ __No cascading failure__
    
    If one service fails, then its failure does not have a cascading effect. This helps in debugging as well.

+ __The ability to reuse__
    
    Once the code of a service is written, it can be used in other projects, where the same functionality is needed.

### Challenges and Drawbacks of Microservices
Just like any other technology, there are also challenges and disadvantages to using microservices:

+ Choosing the right service size
    
    While breaking the monolith application or creating microservices from scratch, it is very important to choose the right functionality for a service. For example, if we create a microservice for each function of a monolith, then we would end up with lots of small services, which would bring unnecessary complexity. 

+ __Deployment__

    We can easily deploy a monolith application. However, to deploy a microservice, we need to use a distributed environment such as Kubernetes. 

+ __Testing__

    With lots of services and their inter-dependency, sometimes it becomes challenging to do end-to-end testing of a microservice.  

+ __Inter-service communication__

    Inter-service communication can be very costly if it is not implemented correctly. There are options such as message passing, RPC, etc., and we need to choose the one that fits our requirement and has the least overhead. 

+ __Managing Databases__

    When it comes to the microservices' architecture, we may decide to implement a database local to a microservice. But, to close a business loop, we might require changes on other related databases. This can create problems (e.g. partitioned databases). 

+ __Monitoring__

    Monitoring individual services in a microservices environment can be challenging.  This challenge is being addresses, and a new set of tools, like [sysdig][sysdig] or [Datadog][datadog], is being developed to monitor and debug microservices. 

Even with the above challenges and drawbacks, deploying microservices makes sense when applications are complex and continuously evolving.

### References
+ https://en.wikipedia.org/wiki/Microservices
+ http://12factor.net/


## Knowledge Check
1. Does each service in a microservice architecture have to be programmed in the same programming language?

        Ans: No

2. Do we need to bring down all the services in order to update one service in the microservice architecture?

        Ans: No


[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c8353742b159161f64edbcbabce031a6/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig9.1-Monoliths-Microservices.png

[wiki]: https://en.wikipedia.org/wiki/Microservices
[svc]: https://en.wikipedia.org/wiki/Service_(systems_architecture)
[decop]: https://en.wikipedia.org/wiki/Coupling_(computer_programming)
[modul]: https://en.wikipedia.org/wiki/Modularity
[system]: https://en.wikipedia.org/wiki/System
[heroku]: http://heroku.com/
[vagrant]: https://www.vagrantup.com/
[sysdig]: http://www.sysdig.org/
[datadog]: https://www.datadoghq.com/


