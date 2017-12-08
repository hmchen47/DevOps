# Chapter 14. Tools for Cloud Infrastructure I (Configuration Management)

## Introduction and Learning Objectives
### Tools for Cloud Infrastructure: Configuration Management
When we have numerous systems (both Physical and VMs) to manage in different environments like Development, QA and Production, we want to do it in an automated way. At any point in time, we want to have consistent and desired state of systems and softwares installed on them. This is also referred as __Infrastructure as Code__.

__Configuration Management__ tools allow us to define the desired state of the systems in an automated way. In this section we will take a look at some of the Configuration Management tools available today, such as __Ansible, Chef, Puppet__, and __Salt__.

### Learning Objectives
By the end of this chapter you should be able to:

+ List tools used to configure and manage the Cloud Infrastructure.
+ Discuss and use configuration management tools (Ansible, Puppet, Chef, and Salt).


## Ansible
### Introduction to Ansible
Red Hat's [Ansible][ansi] is an easy-to-use, Open Source configuration management tool. It is an _agentless_ tool which works on top of __SSH__. __Ansible__ also automates cloud provisioning, application deployment, orchestration, etc.

### Nodes
To list the nodes which we want to manage in an inventory file, we must  do the following:
```yaml
[webservers]
www1.example.com
www2.example.com

[dbservers]
db0.example.com
db1.example.com
```

![image][img1]

Figure 14.1: Ansible Multi-Node Deployment Workflow (retrieved from [sysadmincasts.com][awndw])

The nodes can be grouped together as shown in Figure 14.1. Ansible also supports dynamic inventory files for cloud providers like AWS and OpenStack. The management node connects to these nodes with a password or it can do passwordless login, using SSH keys.

__Ansible__ ships with some [default set of modules][ansimod], like `packaging`, `network`, etc., which can be executed directly or via [__Playbooks__][playbook]. We can also create custom modules.

### Playbooks
[Playbooks][playbook] are Ansible’s configuration, deployment, and orchestration language. Below we provide an example of a playbook which performs different tasks based on roles:

```yaml
---
# This playbook deploys the whole application stack in this site. 
- name: apply common configuration to all nodes
  hosts: all
  remote_user: root

  roles:
    - common

- name: configure and deploy the webservers and application code
  hosts: webservers
  remote_user: root

  roles:
    - web

- name: deploy MySQL and configure the databases
  hosts: dbservers
  remote_user: root

  roles:
    - db
```
Sample tasks mentioned in the playbook are as following:
```yaml
---
# These tasks install http and the php modules.

- name: Install http and php etc
  yum: name={{ item }} state=present
  with_items:
   - httpd
   - php
   - php-mysql
   - git
   - libsemanage-python
   - libselinux-python

- name: insert iptables rule for httpd
  lineinfile: dest=/etc/sysconfig/iptables create=yes state=present regexp="{{ httpd_port }}" insertafter="^:OUTPUT "
              line="-A INPUT -p tcp  --dport {{ httpd_port }} -j  ACCEPT"
  notify: restart iptables

- name: http service state
  service: name=httpd state=started enabled=yes
```
The __Ansible Management__ node connects to nodes mentioned in the inventory file and runs the tasks mentioned in the playbook. A Management node can be installed on any *nix-based system like Linux, Mac OS X, etc. It can manage any node which supports SSH and Python 2.4 or later.

[Ansible Galaxy][ansigal] is a free site for finding, downloading, and sharing community-developed Ansible roles.

Ansible also has an enterprise product called [Ansible Tower][ansitow], which has a GUI interface, access control, central management, etc.

### Demo
In the following video we will see how we can use Ansible to install and configure Nginx on a CentOS system.  

[video][vid1]

### Benefits of Using Ansible
Some of the benefits of using Ansible are:

+ It is an easy-to-use Open Source configuration management tool.
+ It is an agentless tool.
+ It automates cloud provisioning, app deployment, orchestration, etc.
+ It provides consistent, reliable, and secure management.
+ It is supported by a large and active community of developers.
+ It has a low learning curve.
+ It provides role-based access control.
+ It is available for all major operating systems.

### References
+ https://www.ansible.com/
+ https://docs.ansible.com/


## Puppet
### Introduction to Puppet
__Puppet__ is an Open Source configuration management tool. It mostly uses the agent/master (client/server) model to configure the systems. The agent is referred to as the _Puppet Agent_ and the master is referred to as the _Puppet Master_. The Puppet Agent can also work locally and is then referred to as _Puppet Apply_.

Besides [Puppet][puppet], the company also has an enterprise product called [Puppet Enterprise][pupent] and provides services and training around that as well.

### Puppet Agent
We need to install __Puppet Agent__ on each system we want to manage/configure with Puppet. Each agent:

+ Connects securely to _Puppet Master_ to get the series of instructions in a file referred to as the _Catalog File_.
+ Performs operations from the _Catalog File_ to get to the desired state.
+ Sends back the status to _Puppet Master_.

Puppet Agent can be installed on the following platforms:

+ Linux
+ Windows
+ Mac OSX.

### Puppet Master
Puppet Master can be installed only on *nix systems. It:

+ Compiles the _Catalog File_ for hosts based on the system, configuration, manifest file, etc.
+ Sends the _Catalog File_ file to agents when they query the master.
+ Has information about the entire environment, such as host information, metadata like authentication keys, etc.
+ Gathers the report from each agent and then prepares the overall report.

### The Catalog File
Puppet prepares a Catalog File based on the _manifest file_. A manifest file is created using the Puppet Code:
```ruby
user { 'nkhare':
  ensure     => present,
  uid        => '1001',
  gid        => '1001',
  shell      => '/bin/bash',
  home       => '/home/nkhare'
}
```
which defines and creates a user nkhare with:

+ UID/GID as 1001
+ The login shell is set to /bin/bash
+ The home directory is set to /home/nkhare.

A __manifest file__ can have one or more sections of code, like we exemplified above, and each of these sections of code can have a signature like the following:
```ruby
resource_type { 'resource_name'
  attribute => value
  ...
}
```
Puppet defines resources on a system as _Type_ which can be _file, user, package, service_, etc. They are well-documented in their documentation.

After processing the manifest file, Puppet Master prepares the Catalog File based on the target platform.

### Puppet Tools
Puppet also has nice tooling around it, like:

+ Centralized reporting (__PuppetDB__), which helps us generate reports, search a system, etc.
+ Live System management
+ __Puppet Forge__, which has ready-to-use modules for manifest files from the community.

### Demo
Next, we will see how we can use Puppet to configure a system to a given state.

[video][vid2]

### Benefits of Using Puppet
Some of the benefits of using Puppet are:

+ It is an Open Source configuration management tool.
+ It provides scalability, automation, and centralized reporting.
+ It is available on all major operating systems.
+ It provides role-based access control.

### References
+ https://puppet.com
+ https://docs.puppet.com/puppet/


## Chef
### Introduction to Chef
__Chef__ uses the client/server model to do the configuration management. The client is installed on each host which we want to manage and referred to as _Chef Client_. The server is referred to as _Chef Server_. Additionally, there is another component called __Chef Workstation__, which is used to:

+ Develop cookbooks and recipes.
+ Synchronize `chef-repo` with the version control system.
+ Run command line tools.
+ Configure policy, roles, etc.
+ Interact with nodes to do a on-off configuration.

![image][img2]

Figure 14.2 Chef Overview (by Chef Software, Inc./[CC BY-SA 3.0][bysa3], retrieved from [chef.io][chef])

### Chef Cookbook
A [Chef Cookbook][chefcook] is the basic unit of configuration which defines a scenario and contains everything that supports the scenario. Two of its most important components are:

+ [Recipes][chefrec]

    A recipe is the most fundamental unit for configuration, which mostly contains resources, resource names, attribute-value pairs, and actions.
    ```bash
    package "apache2" do
        action :install
    end

    service "apache2" do
        action [:enable, :start]
    end
    ```

+ [Attributes][chefattr]

    An attribute helps us define the state of the node. After each _chef-client_ run, the node's state is updated on the _Chef Server_.

[Knife][chefknif] provides an interface between a local `chef-repo` and the _Chef Server_.

### Supported Platforms
__Chef__ supports the following platforms for _Chef Client_:

+ *nix-based systems
+ Mac OS X
+ Windows
+ Cisco IOS XR and NX-OS.

_Chef Server_ is supported on the following platforms:

+ Red Hat Enterprise Linux
+ Ubuntu Linux.

__Chef__ also has a GUI built on top of _Chef Server_, which can help up running the cookbook from the browser, prepare reports, etc.

### Demo
Next, we will see how we can configure a system to a given state using Chef.

[video][vid2]

### Benefits of Using Chef
Some of the benefits of using Chef are:

+ Chef is an Open Source systems integration framework.
+ It provides automation, scalability, High Availability and consistency in deployment.
+ It is available for all major operating systems.
+ It provides role-based access control.
+ It provides real-time visibility with [Chef Analytics][chefana].

### References
+ https://docs.chef.io/


## Salt
### Introduction to Salt
[Salt][salt] is an Open Source configuration management system built on top of a remote execution framework. It uses the client/server model, where the server sends commands and configurations to all the clients in a parallel manner, which the clients run, returning back the status. 

### Salt Minions
Each client is referred to as a __Salt Minion__.

![image][img3]

Figure 14.3: Salt Minions (by SaltStack, Inc., retrieved from [saltstack.com][saltstack])

Minions can be installed on:

+ *nix-based systems
+ Windows
+ Mac OS X.

### Salt Masters
A server is referred to as a __Salt Master__. Multi-master is also supported.

![image][img4]

Figure 14.4: Salt Master (by SaltStack, Inc., retrieved from [saltstack.com][saltmst])

In a default setup, the __Salt Master__ and __Minions__ communicate over a high speed data bus, [ZeroMQ][zromq], which requires an agent to be installed on each minion. Salt also supports an agentless setup on top of SSH. The Salt Master and Minions communicate over a secure and encrypted channel.

### Other Components: Modules, Returners, Grains, Pillar Data
Remote execution is based on [Modules][mod] and [Returners][retrn].

__Modules__ provide basic functionality, like installing packages, managing files, managing containers, etc. All support modules are listed in the [Salt documentation][saltdoc]. We can also write custom modules.

With __Returners__, we can save a Minion's response on the Master or other locations. We can use default Returners or write custom ones.

All the information collected from Minions is saved on the Master. The collected information is referred to as __Grains__. Private information like cryptographic keys and other specific information about each minion which the Master has is referred to as __Pillar Data__. Pillar Data is shared between the Master and the individual Minion.

By combining __Grains__ and __Pillar Data__, the Master can target specific Minions to run commands on them. For example, we can query the hostname of all the nodes where the installed OS is "Fedora 23".

With the above tools and information in hand, the Master can easily setup a Minion with a specific state. This can also be referred to as Configuration Management. __Salt__ has different [State Modules][saltstat] to manage a state.

## Demo
Next, we will see how to configure a system to a given state, using Salt.

[video][vid3]

### Benefits of Using Salt
Some of the benefits of using Salt are:

+ It is an Open Source configuration management system.
+ It provides automation, High Availability and an event-driven infrastructure.
+ It provides role-based access control.
+ It supports agent and agentless deployments.
+ It is available for all major operating systems.

### References
+ https://docs.saltstack.com/en/latest/


## Knowledge Check
Which of the following configuration management tools is completely agentless? Please select the correct answer.

    A. Chef
    B. Puppet
    C. Salt
    D. None of the above

    Ans: D





[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V001800_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V004800_DTH.mp4
[vid3]: https://edx-video.net/LINLFS15/LINLFS152016-V003900_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a7b47422d685969d770e27b685fc6a9d/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_14.1_Ansible_Multi-Node_Deployment_Workflow.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a82b0b8035790de994975ce7903f3fac/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/chef_overview.svg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7079007d398c704b1860d105c15c400f/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_14.3_Salt_Minions.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/59319a69860ba7f652b4d8828e5cd83b/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig_14.4_-_Salt_Master.png

[ansi]: http://www.ansible.com/
[amnsw]: https://d1cg27r99kkbpq.cloudfront.net/static/extra/43-ansible-multi-node-deployment-workflow.png
[ansimod]: https://github.com/ansible/ansible-modules-core
[playbook]: http://docs.ansible.com/ansible/playbooks.html
[ansigal]: https://galaxy.ansible.com/
[ansitow]: https://www.ansible.com/tower
[pupet]: https://puppet.com/
[pupent]: https://puppet.com/product
[bysa3]: https://creativecommons.org/licenses/by-sa/3.0/
[chef]: https://docs.chef.io/_images/chef_overview.svg
[chefcook]: https://docs.chef.io/cookbooks.html
[chefrec]: https://docs.chef.io/recipes.html
[chefattr]: https://docs.chef.io/attributes.html
[chefknif]: https://docs.chef.io/knife.html
[chefana]: https://www.chef.io/analytics/
[salt]: http://saltstack.com/
[saltstack]: http://saltstack.com/wp-content/uploads/2015/05/minions.png
[slatmst]: http://saltstack.com/wp-content/uploads/2015/05/master.png
[zeromq]: http://zeromq.org/
[mod]: https://docs.saltstack.com/en/latest/ref/modules/all/index.html
[retrn]: https://docs.saltstack.com/en/latest/ref/returners/all/index.html
[saltdoc]: https://docs.saltstack.com/en/latest/ref/modules/all/index.html
[saltstat]: https://docs.saltstack.com/en/latest/ref/states/all/index.html




