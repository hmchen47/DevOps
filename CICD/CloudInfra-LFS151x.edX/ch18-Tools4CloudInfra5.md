# Chapter 18. Tools for Cloud Infrastructure V (Debugging, Logging, and Monitoring for Containerized Applications)

## Introduction and Learning Objectives
### Tools for Cloud Infrastructure: Debugging, Logging and Monitoring for Containerized Applications
When we experience problems in Development or Production, we resort to debugging, logging and monitoring tools to find the root cause of the problem. Some of the tools which we should be familiar with are:

+ __strace__
+ __SAR (System Activity Reporter)__
+ __tcpdump__
+ __GDB (GNU Project Debugger)__
+ __syslog__
+ __Nagios__
+ __Zabbix__.

We can use the same tools on bare metal and VMs, but containers bring interesting challenges:

+ Containers are ephemeral, so, when they die, all the metadata (e.g. logs) gets deleted as well, unless we store them in some other location.
+ Containers do not have kernel space components.
+ We want to have a container's footprint as low as possible. Installing debugging and monitoring tools increases the footprint size.
+ Collecting per container statistics, debugging information individually and then analyzing data from multiple containers is a tedious process.

It would be helpful to do debugging, logging and monitoring via external tools, instead of collecting them from individual containers. We can do this because each container runs as a process on the Host OS, which has complete control of that process. Once we have collected the data from all the containers which are running on a system or in a cluster like __Kubernetes__ or __Swarm__, we can do a logical mapping and get a system/cluster wide view.

Below are some of the tools which we can use for containerized applications:

+ __Debugging__: Docker CLI, Sysdig
+ __Logging__: Docker CLI, Docker Logging Driver
+ __Monitoring__: Docker CLI, Sysdig, cAdvisor/Heapster, Prometheus, Datadog, New Relic.

### Native Docker Features for Debugging
Docker has some built-in command line options which can help with Debugging, Logging and Monitoring:

+ Debugging:
    - `docker inspect`
    - `docker logs`
+ Logging: 
    - `docker logs`
    - [Docker Logging Drivers][doclog] - With the logging driver we can choose a Docker daemon wide or per container logging policy. Depending on the policy, Docker forwards the logs to the corresponding drivers. Docker supports the following drivers: __jsonfile, syslog, journald, gelf (Graylog Extended Log Format), fluentd, awslogs, splunk__. Once the logs are saved in a central location, we can use the respective tools to get the insights.
+ Monitoring:
    - `docker stats`
    - `docker top`.

### Learning Objectives
By the end of this chapter you should be able to:

+ Describe and use debugging, logging and monitoring tools for containerized applications.


## Sysdig
### Introduction to Sysdig
__Sysdig__ is an Open Source tool which captures low-level system information from the running Linux instance.  According to [sysdig.org][sysdig], __sysdig__ is

> "_strace + tcpdump + htop + iftop + lsof + awesome sauce_".

The collected information can be saved, on which we can then apply filters and do further analysis.

It is the general purpose tool for Linux, but it offers native support for containers. It is scriptable in __Lua__ and includes a command line interface and a powerful interactive UI, `csysdig`, that runs on the terminal.

__Sysdig__ inserts a kernel module inside the running Linux kernel, from which it can capture system calls and OS events. This allows it to have rich feature sets.

### What Sysdig Can Do from the Command Line (Examples)
Next we provide some examples that give you an idea of what sysdig can do from the command line:

See the top processes in terms of network bandwidth usage:

> `$ sudo sysdig -c topprocs_net`

View the CPU usage of the processes running inside the apache container:

> `$ sudo sysdig -pc -c topprocs_cpu container.name=apache`

View the top files in terms of I/O bytes inside the apache container:

> `sudo sysdig -pc -c topfiles_bytes container.name=apache`

Show the directories that the user "root" visits:

> `$ sudo sysdig -p"%evt.arg.path" "evt.type=chdir and user.name=root"`

You can find more examples in the [documentation][digdoc].

### Features
__Sysdig__ also offers a paid solution called __Sysdig Cloud__, which allows systems to directly upload the collected information to the cloud. To enable collection and upload, we need to install and enable an agent on each of the nodes. Sysdig has native support to many applications, infrastructure and container technologies:

+ Docker
+ Kubernetes
+ Mesos
+ AWS
+ Google Cloud Platform.

Once the __Sysdig Agent__ starts sending data on the Sysdig Cloud, we can do:

+ Real time monitoring
+ Historial replay
+ Dynamic topology creation
+ Intelligent alerting.

### Benefits of Sysdig
Some of the benefits of sysdig are:

+ It is an Open Source tool which captures low-level system information from the running Linux instance.
+ It is the general purpose tool for Linux.
+ It offers native support for containers.
+ It is easy to install and use.
+ It is built to run in production, minimizing performance overhead and the risk of crashes.
+ It is flexible and can be extended with Lua scripts.

### References
+ http://www.sysdig.org/
+ http://www.sysdig.org/wiki/sysdig-examples/#containers
+ https://sysdig.com/product/


## cAdvisor & Heapster
### Introduction to cAdvisor
[__cAdvisor (Container Advisor)__][cadv] is an Open Source tool to collect resource usage and performance characteristics for the host system and running containers. It collects, aggregates, processes, and exports information about running containers. As of now, it has native support for Docker and should also support other container runtimes out of the box.

### Using cAdvisor
We can enable the __cAdvisor container__ to start collecting statistics with the following command:
```bash
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
```
and point the browser to `http://host_IP:8080` to get the live statistics. cAdvisor exposes its raw and processed statistics via a versioned remote REST API. It also supports exporting statistics for [InfluxDB][influx]. cAdvisor exposes container statistics as [Prometheus metrics][prome]. __Prometheus__ is an Open Source community-driven system and service monitoring toolkit.

### Introduction to Heapster
[__Heapster__][heap] enables Container Cluster Monitoring and Performance Analysis. It currently supports Kubernetes and CoreOS natively. __Heapster__ collects and interprets various signals, like compute resource usage, lifecycle events, etc., and exports cluster metrics via REST endpoints. [Kubedash][kubedash], a performance analytics UI for Kubernetes, uses those endpoints.

### Host System Resource Usage with cAdvisor
Figure 18.1 illustrates details about the processes on the Host system, as well as the CPU usage.

![image][img1]

Figure 18.1: Host System Resource Usage with cAdvisor

### Docker Host Specific Details with cAdvisor
Figure 18.2 shows the number of running containers, as well as details about Docker Engine and images.

[image][img2]

Figure 18.2 Docker Host Specific Details with cAdvisor

### References
+ https://github.com/google/cadvisor
+ https://github.com/kubernetes/heapster


## Fluentd
### Introduction to Fluentd
[Fluentd][fluen] is an "open source data collector, which lets us unify the data collection and consumption for a better use and understanding of data" (fluentd.org).

![image][img3]

Figure 18.1: Fluentd Architecture (by Treasure Data, Inc., retrieved from [fluentd.org][fluarch])

Fluentd tries to structure the data in json as much as possible. It supports more than [300 plugins][fluplug] to connect input sources to output sources, after doing filtering, buffering and routing.

### Docker Support for Fluentd
From version 1.8, Docker supports [logging drivers][logging] and Fluentd is one of them.

![image][img4]

Figure 18.2: Fluentd and Docker Integrated (by Treasure Data, Inc., retrieved from [fluentd.org][fluedoc])

We can either configure the logging driver for the Docker daemon or specify it while starting a container.

### Benefits of Using Fluentd
Some of the benefits of using Fluentd are:

+ It is an Open Source data collector.
+ It is simple, fast, and flexible.
+ It is performant and developer-friendly. 

### References
+ http://www.fluentd.org
+ http://www.fluentd.org/guides/recipes/docker-logging


## Datadog
### Introduction to Datadog
[Datadog][datadog] provides monitoring and analytics as a service for Development and OPs teams. Some of the systems, applications and services it connects to are:

+ Amazon EC2
+ Apache
+ Java
+ MySQL
+ CentOS.

A detailed [list of integration][dataint] can be found in the documentation it provides. We need to install an agent in the host system, which sends the data to the Datadog's server. Once the data is sent, we can:

+ Build an interactive dashboard.
+ Search and co-relate matrices and events.
+ Share the matrices and events.
+ Get alerting.

### Docker Containers: Kubernetes Monitoring with Datadog
Figure 18.3 illustrates valuable information about containers:

+ The number of nodes in the cluster
+ The running and stopped containers
+ The most resource-consuming pods
+ Docker logs, etc.

[image][img5]

Figure 18.3: Docker Containers - Kubernetes Monitoring with Datadog (by Datadog, Inc., retrieved from [datadoghq.com][datahq])

### Benefits of Using Datadog
Some of the benefits of using Datadog are:

+ It comes pre-integrated with well-known third-party applications.
+ It provides a seamless workflow, regardless of platform, location or language.
+ It configures information filtration to get only needed metrics.
+ It allows us to enable the system to send alerts or notifications when serious issues arise.
+ It offers tools for team collaboration.
+ It is scalable. 

### References
+ https://www.datadoghq.com/


## Knowledge Check
1. Sysdig requires a kernel component to capture different system calls and OS events. 

        Ans: True

2. cAdvisor is designed to collect cluster-wide resource usage and performance matrices. 

        Ans: False




[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f8b0ae96865f6ed850b3835677284e99/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/cAdvisor-Processes_on_the_Host_System_and_CPU_Usage.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a0b9de004ba2a255023ac4f75830d851/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/cAdvisor-Running_Containers__Docker_Engine__and_Images.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3b24605cc19767161db6060174f10553/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fluentd_Architecture.png
[img4]: http://www.fluentd.org/assets/img/recipes/fluentd_docker_integrated.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/efebb8041e7ea0a28033a4af45f03620/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Datadog-Kubernetes_Integration.png


[doclog]: https://docs.docker.com/engine/admin/logging/overview/
[sysdig]: http://www.sysdig.org/
[digdoc]: http://www.sysdig.org/wiki/sysdig-examples/#containers
[cadv]: https://github.com/google/cadvisor/
[influx]: https://influxdb.com/
[prome]: https://github.com/prometheus/prometheus
[heap]: https://github.com/kubernetes/heapster
[kubedash]: https://github.com/kubernetes/kubedash
[fluen]: http://www.fluentd.org/
[fluarch]: http://docs.fluentd.org/images/fluentd-architecture.png
[fluplug]: http://www.fluentd.org/plugins
[logging]: https://docs.docker.com/reference/logging/overview/
[fluedoc]: http://www.fluentd.org/assets/img/recipes/fluentd_docker_integrated.png
[datadog]: https://www.datadoghq.com/
[dataint]: https://www.datadoghq.com/product/integrations/
[datahq]: https://d33tyra1llx9zy.cloudfront.net/blog/images/2015-11-kubernetes-integration/1.png



