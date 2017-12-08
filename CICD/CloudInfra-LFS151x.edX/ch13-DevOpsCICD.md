# Chapter 13. DevOps and CI/CD

## Introduction and Learning Objectives
### DevOps and CI/CD
Every industry thrives for better quality and faster innovation. The IT industry is no exception and has to address numerous challenges, like the following:

+ It must quickly go from business idea to market.
+ It must lower the failure rate for new releases.
+ It must have a shorter lead time between fixes.
+ It must have a faster mean time to recovery.

Over the last decade or so, we gradually shifted from the [Waterfall Model][water] to [Agile Software Development][agile], in which teams deliver working software in smaller and more frequent increments. In this process, the IT operation (Ops) teams were unintentionally left behind, which put a lot of pressure on them, due to high end-to-end deployment rates. By putting the Ops teams in the loop from the very beginning of the development cycle, we can reduce this burn-out and can take advantage of their expertise in the continuous integration.

The collaborative work between Developers and Operations is referred to as __DevOps__. DevOps is more of a mindset, a way of thinking, versus a set of processes implemented in a specific way.

Besides __Continuous Integration (CI)__, DevOps also enable __Continuous Deployment (CD)__, which can be seen as the next step of CI. In CD, we deploy the entire application/software automatically, provided that all the tests' results and conditions have met the expectations.

Some of the software used in the CI/CD domain are __Jenkins, Drone, Travis__ and __Shippable__, which we will explore in this chapter.

### Learning Objectives
By the end of this chapter you should be able to:

+ Explain the concept of __DevOps__.
+ Discuss about __Continuous Integration__ and __Continuous Deployment__.
+ Run automated tests in the cloud.
+ Deploy a sample application on the cloud.


## CI/CD: Jenkins
### Introduction to Jenkins
[Jenkins][jenkins] is one of the most popular and used tools for doing any kind of automation. It is an Open Source automation system which can provide __Continuous Integration__ and __Continuous Deployment__. It is written in Java.

[CloudBees][cloudbee] is one of the primary sponsors for the Jenkins Open Source project. CloudBees provides [different products based on top of Jenkins][jprod].

### Jenkins Functionality
__Jenkins__ can build Freestyle, Apache Ant, and Apache Maven-based projects. We can also extend the functionality of Jenkins, using [plugins][jplug]. Currently, Jenkins supports more than 1000 plugins in different categories, like _Source Code Management, Slave Launchers, Build tools, External tools/site integration_, etc.

Jenkins also has the functionality to build a pipeline, which allows us to to define an entire application lifecycle. __Pipeline__ is most useful for doing Continuous Deployment.  According to the [Jenkins documentation][jdoc], Pipeline's _functionality_ is:

+ __Durable__: Pipelines can survive both planned and unplanned restarts of your Jenkins master.
+ __Pausable__: Pipelines can optionally stop and wait for human input or approval before completing the jobs for which they were built.
+ __Versatile__: Pipelines support complex real-world CD requirements, including the ability to fork or join, loop, and work in parallel with each other.
+ __Extensible__: The Pipeline plugin supports custom extensions to its DSL (domain scripting language) and multiple options for integration with other plugins."

The flowchart below illustrates a sample deployment using the __Pipeline Plugin__:

![image][img1]

Figure 13.1: Jenkins Pipeline (by Jenkins/[CC BY-SA 4.0][bysa4], retrieved from [jenkins.io][jpipe])

Jenkins can be hosted on-premise, on the cloud, or we can just use it as SaaS.

### Demo
In the following demo we will see how we can use Jenkins to run unit tests.

[video][vid1]

### Benefits of Using Jenkins
Among the benefits of using Jenkins are:

+ It is an Open Source automation system.
+ It supports Continuous Integration and Deployment.
+ It is extensible through plugins.
+ It can be easily installed, configured, and distributed.

### References
+ https://jenkins.io/
+ https://wiki.jenkins-ci.org


## CI/CD: Drone
### Introduction to Drone
[__Drone__][drone] provides both hosted and on-premise solutions to do __Continuous Integration__ for projects hosted on __Github__ and __BitBucket__.

### Testing with Drone
Once the project is linked with Drone, it allows you to choose the programming language of the project and add run commands to trigger the tests.

While running the test, Drone will first clone the project's repository locally and then run the tests. For example, after cloning the Python project, it will run the following commands to trigger the tests:

+ pip install -r requirements.txt --use-mirrors
+ cd wsgi
+ py.test

Drone supports the following languages:

+ C / C++
+ Dart
+ Go
+ Haskell
+ Groovy
+ Java
+ Node.js
+ PHP (Beta)
+ Python (Beta)
+ Ruby (Beta)
+ Scala.

While setting up the build, one can also choose the Database to use and set the environment variables. The Database and environment variables will be used while running the build.

### Deploying Applications with Drone
Once the tests are passed, we can ask Drone to deploy the application as well. Currently, it supports the following deployment methods:

+ Heroku
+ AppEngine (Beta)
+ dotCloud (Beta)
+ SSH
+ Amazon S3 (Beta).

### Demo
In the following demo we will see how we can use Drone for unit testing.

[video][vid2]

### Benefits of Using Drone
Some of the benefits of using Drone are:

+ It is a hosted and on-premise solution to do Continuous Integration. 
+ It is free for public projects.
+ It enables us to automatically build, test, and deploy projects.
+ It uses Docker containers to build and test code.
+ It is integrated with GitHub, Bitbucket, and Google Code, as well as other third-party services.

### References
+ https://drone.io/


## CI/CD: Travis CI
### Introduction to Travis CI
[Travis CI][travis] is a hosted, distributed CI solution for projects hosted only on GitHub.

To run the test with CI, first we have to link our GitHub account with Travis and select the project (repository) for which we want to run the test. In the project's repository we have to create a `.travis.yml` file, which defines how our build should be executed step-by-step.

### Executing Build with Travis
A typical build with Travis consists of two steps:

+ __install__: to install any dependency or pre-requisite.
+ __script__: to run the build script.

We can also add other optional steps, including the deployment steps. Following are all the build options one can put in a `.travis.yml` file.

+ `before_install`
+ `install`
+ `before_script`
+ `script`
+ `after_success` or `after_failure`
+ OPTIONAL `before_deploy`
+ OPTIONAL `deploy`
+ OPTIONAL `after_deploy`
+ `after_script`

### Travis Characteristics
Travis supports different databases, like MYSQL, RIAK, memcached, etc. We can also use docker during the build.

Travis supports most languages. A detailed list of the languages supported can be found [here][lang].

After running the test, we can deploy the application in many cloud providers, such as Heroku, AWS Codedeploy, Cloud Foundry, OpenShift, etc. A detailed list of providers is available [here][tdep].

### Demo
Next, we will show you how to do automated builds and run tests against them using Travis CI.

[video][vid3]

### Benefits of Using Travis CI
Some of the benefits of using Travis CI are:

+ It is a hosted, distributed solution, integrated with GitHub.
+ It can be easily setup and configured.
+ It is free for Open Source projects.
+ It supports testing for different versions of the same runtime. 

### References
+ https://travis-ci.com/
+ https://docs.travis-ci.com/user/customizing-the-build/


## CI/CD: Shippable
### Introduction to Shippable
__Shippable__ provides __Continuous Integration__ and __Continuous Delivery Pipeline__ for projects hosted on Github, BitBucket and on-premise repositories, like GitHub Enterprise.

Other than hosted solutions, Shippable also allows you to setup an on-premise host as a build server.

Shippable runs all the builds inside a Docker container, which are called __minions__. Shippable has minions for all the different combinations of programming languages and versions they support. But, if you are already doing development with Docker, you can either use your own image or build a new one, while doing the CI.

### Testing with Shippable
Similar to Travis, to run CI tests with Shippable we have to create a configuration file inside the project's source code repository which we want to test, called shippable.yml.

![image][img2]

Figure 13.2: The shippable.yml Structure (by Shippable, Inc., retrieved from [shippable.com][shipable])

### Programming Languages Supported by Shippable
Currently, Shippable supports the following programming languages for CI:

+ Clojure
+ Go
+ Java
+ Node.js
+ PHP
+ Python
+ Ruby
+ Scala

### Deploying Applications with Shippable
If the application is __Dockerized__, then we can take advantage of the __Continuous Delivery Pipeline__ of Shippable. This allows us to deploy the application on container services like Amazon ECS and Google Container Engine. Support to other deployment endpoints, like Microsoft Azure and Red Hat's Openshift v3, is coming soon. Continuous Delivery Pipeline makes the deployment cloud agnostic and allows the possibility to migrate to a different cloud at will.

### Demo
The following demo will show how we can use Shippable to do automated testing for our projects.

[video][vid3]

### Benefits of Using Shippable
Some of the benefits of using Shippable are:

+ It supports both GitHub and Bitbucket.
+ Builds are faster, as it runs inside of Docker.
+ It supports builds against multiple runtimes, environment variables, and platforms.
+ It supports on-premise systems for builds.

### References
+ http://docs.shippable.com/ci_configure/
+ http://docs.shippable.com/pipelines_overview/


## Knowledge Check
1. Do DevOps have well-defined rules that everyone must follow? 

        Ans: No

2. Which of the following solutions uses only containers to provide CI/CD? Please select all answers that apply.

        A. Drone
        B. Travis
        C. Jenkins
        D. Shippable

        Ans: A, D

3. Is Continuous Deployment an optional step after doing Continuous Integration?

        Ams: Yes


[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V002800_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V002900_DTH.mp4
[vid3]: https://edx-video.net/LINLFS15/LINLFS152016-V004300_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a5a50fb48bc49ae00bd8df6bcf47203e/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_13.1-Jenkins_Pipeline.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a1a26989ad0b17e71b3dda66a5376a0d/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_13.1-The_shippable.yml_Structure.png

[bysa4]: https://creativecommons.org/licenses/by-sa/4.0/
[jpipe]: https://jenkins.io/images/pipeline/realworld-pipeline-flow.png
[water]: https://en.wikipedia.org/wiki/Waterfall_model
[agile]: https://en.wikipedia.org/wiki/Agile_software_development
[jenkins]: https://jenkins-ci.org/2.0/
[cloudbee]: https://www.cloudbees.com/
[jplug]: https://wiki.jenkins-ci.org/display/JENKINS/Plugins
[jprod]: https://www.cloudbees.com/products
[jdoc]: https://jenkins.io/doc/pipeline/
[bysa4]: https://creativecommons.org/licenses/by-sa/4.0/
[jpipline]: https://jenkins.io/images/pipeline/realworld-pipeline-flow.png
[drone]: https://drone.io/
[travis]: https://travis-ci.com/
[lang]: https://docs.travis-ci.com/user/language-specific/
[tdep]: https://docs.travis-ci.com/user/deployment
[shipable]: http://docs.shippable.com/images/ci_yml_structure.png



