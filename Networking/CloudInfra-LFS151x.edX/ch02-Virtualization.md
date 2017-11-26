# Chapter 2. Virtualization


## Introduction and Learning Objectives
### Virtualization
According to Wikipedia,

>"In computing, virtualization refers to the act of creating a virtual (rather than actual) version of something, including virtual computer hardware platforms, operating systems, storage devices, and computer resources." 

Virtualization can be offered on different hardware and software layers, like CPU (Central Processing Unit), Disk, Memory, Filesystems, etc. In this chapter, we will look at some examples of creating Virtual Machines (VMs) after emulating the different kind of hardware to install a Guest OS on that.

Virtual Machines are created on top of a __Hypervisor__ , which runs on top of the Host Machine's Operating System. With Hypervisors, we emulate hardware like CPU, Disk, Network, Memory and install Guest Machines on it. We can create multiple Guest Machines with different Operating Systems on a __Hypervisor__ . For example, we can take a Linux Machine running on bare-metal and, after setting up the __Hypervisor__ , we can create multiple Guest Machines with __Linux__ and __Windows__ Operating Systems. Some examples of hypervisors are:

+ __KVM__
+ __Xen__
+ __VMWare__
+ __VirtualBox__
+ __Hyper-V__.

We can find support for hardware virtualization in all recent CPUs, as it is important to share the host system's processor resources with multiple Guest Operating Systems in a safe and efficient way. Most of the recent CPUs will also support Nested Virtualization, which enables us to have a VM inside a VM.

Next, let's take a look at a few examples on how to create VMs on top of different hypervisors.

### References
+ https://en.wikipedia.org/wiki/Hypervisor
+ https://en.wikipedia.org/wiki/Virtualization
+ https://en.wikipedia.org/wiki/Virtualization#Nested_virtualization

### Learning Objectives
By the end of this chapter you should be able to:

+ Describe the different types of Virtualization.
+ Explain how Hypervisors can be used to create Virtual Machines. 
+ Create and configure Virtual Machines automatically, using KVM, VirtualBox, and Vagrant. 


## KVM
### Introduction to KVM
According to linux-kvm.org, 

"KVM for (Kernel-based Virtual Machine) is  a full virtualization solution for Linux on x86 hardware."

It is part of the main-line Linux Kernel. It is ported for S/390, PowerPC, IA-64 and ARM as well.

![KVM][img1](Figure 2.1: A High-Level Overview of the KVM/QEMU Virtualization Environment (by V4711, licensed under [CC BY-SA 4.0][bysc4], retrieved from [Wikipedia][wikikvm]))

### Features
__KVM__ is an Open Source software. It supports various Guest OSes, like __Linux__, __Windows__, __Solaris__, etc. 

KVM does not perform any emulation itself, but it exposes the `/dev/kvm` interface, by which an external userspace host can do emulation. [QEMU][qemu] is one such host. 

### Demo
In this video, we will show how you can create a Virtual Machine instance on the __KVM Hypervisor__ using `virt-manager`.

[video][vid1]

### Benefits of Using __KVM__
Some of the benefits of using __KVM__ are:

+ It is an Open Source solution, and, as such, free to customize
+ Using __KVM__ is efficient from a financial perspective as well, due to the lower costs associated with it
+ It is highly scalable
+ __KVM__ employs advanced security features, utilizing __SELinux__. It provides __MAC (Mandatory Access Control)__ security between Virtual Machines. __KVM__ has received awards for meeting common government and military security standards  and for allowing open virtualization for homeland security projects.

### References
+ http://www.linux-kvm.org/
+ https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine


## VirtualBox
### Introduction to VirtualBox
[VirtualBox][vbox] is an __x86__ and __AMD64/Intel64__ virtualization product from __Oracle__, which runs on __Windows__, __Linux__, __Macintosh__, and __Solaris__ hosts and supports [Guest OSes][guest] from Windows, Linux families, and others, like __Solaris__, __FreeBSD__, __DOS__, etc.

It is an easy-to-use multi-platform Hypervisor. It is not part of the mainline kernel. So, to use it on __Linux__, we have to compile and insert the respective kernel module. 

__Virtual Box__ is distributed under the __GNU General Public License (GPL) version 2__.

### Demo
In this video, we will show you how to create a Virtual Machine instance on __VirtualBox__.

[video][vid2]

### Benefits of Using VirtualBox
Some of the benefits of using __VirtualBox__ are:

+ It is an Open Source solution.
+ It is free to use.
+ It runs on __Linux, Windows, OS X, Solaris__.
+ It is an easy-to-use multi-platform Hypervisor.

### References
+ https://www.virtualbox.org/


## Vagrant
### Introduction to Vagrant
Using Virtual Machines in a development environment has numerous benefits:

+ Reproducible environment
+ Management of multiple projects in their restricted environment
+ Sharing the environment with other teammates
+ Keeping the development and deployment environments in sync
+ Running the same VM on different OSes, with a Hypervisor like __VirtualBox__. 

Configuring and sharing one VM is easy, but, when we have to deal with multiple VMs for the same project, doing everything manually can be tiresome. [Vagrant][vagr] by __Hashicorp__ helps us automate the setup of one or more VMs by providing an end-to-end life-cycle using the vagrant command line. __Vagrant__ is a cross-platform tool. It can be installed on __Linux__, __Mac-OSX__, and __Windows__. We have to use different providers, depending on the OS. It has recently added support for __Docker__, which can help us manage __Docker__ containers.


### Managing Virtual Machines with Vagrant
Next, let's see how __Vagrant__ helps us manage Virtual Machines:

+ Vagrantfile

    It is a text file with the __Ruby__ syntax, which has all the information about configuring and provisioning a set of machines. It has details like the machine type, image, networking, provider-specific information, provisioner details, etc. We provide a sample __Vagrantfile__ below:
    ```ruby
    # -*- mode: ruby -*-
    # vi: set ft=ruby :

    Vagrant.configure(2) do |config|
    # Every Vagrant development environment requires a box. You can search for 
    # boxes at https://atlas.hashicorp.com/search.
    config.vm.box = "centos/7"

    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    config.vm.network "private_network", ip: "192.168.33.10"

    # config.vm.synced_folder "../data", "/vagrant_data"

    config.vm.provider "virtualbox" do |vb|
        # Customize the amount of memory on the VM:
        vb.memory = "1024"
    end

    config.vm.provision "shell", inline: <<-SHELL
            yum install vim -y
    SHELL
    end
    ```
    The `vagrant` command reads the configuration given in the configuration file and does different operations, like `up`, `ssh`, `destroy`, etc. The `vagrant` command also has sub-commands like box to manage __Box__ images, `rdp` to connect to VMs using __RDP (Remote Desktop Protocol)__, etc. A detailed list of commands is available at its [documentation][vdoc].

+ Boxes

    We need to provide an image in the __Vagrantfile__, which we can use to instantiate machines. In the example above, we have used centos/7 as the base image. If the image is not available locally, then it can be downloaded from a central repository like Atlas, which is the image repository provided by __Hashicorp__. We can version these images and use them depending on our need, by updating the __Vagrantfile__ accordingly.

+ Vagrant Providers

    [Providers][vagp] are the underlying engine/hypervisor used to provision a machine. By default, __Vagrant__ supports __VirtualBox__, __Hyper-V__ and __Docker__. We also have custom providers, like __KVM__, __AWS__, etc. VirtualBox is the default provider.

+ Synced Folders

    With the Synced Folder feature, we can sync a directory on the host system with a VM, which helps the user manage shared files/directories easily. For example, in the above example, if we un-comment the line below from __Vagrantfile__, then the `../data` folder from the current working directory of the host system would be shared with the `/vagrant_data` file on the VM.
    ```ruby
    # config.vm.synced_folder "../data", "vagrant_data"
    ```

+ Provisioning

    Provisioners allow us to automatically install software, make configuration changes, etc. after the machine is booted. It is a part of the `vagrant up` process. There are many types of provisioners available, such as __File, Shell, Ansible, Puppet, Chef, Docker__, etc. In the example below, we used Shell as the provisioner to install the vim package.
    ```ruby
    config.vm.provision "shell", inline: <<-SHELL
                yum install vim -y
    SHELL
    ```
+ Plugins

    We can use Plugins to extend the functionality of Vagrant. 

### Demo
In this video, we will see how we can automate the creation and deletion of Virtual Machines, using __Vagrant__.

[video][vid3]

### Benefits of Using Vagrant
Some of the benefits of using __Vagrant__ are:

+ It automates the setup of one or more VMs, which results in saved time and lower operational costs.
+ It is a cross-platform tool.
+ It provides support for Docker, thus helping us manage Docker containers.
+ It is easy to install.
+ It is very useful in multi-developer teams.

### References
+ https://www.vagrantup.com/docs/


## Knowledge Check
1. Which of the following do we have to emulate to create a Virtual Machine? Please select the correct answer.

        A. CPU
        B. Disk
        C. Network
        D. All of the above

        Ans: D
        Explanation
        In computing, virtualization generally refers to the emulation of something, backed by some real hardware or resources. For example, while creating Virtual Machines, we emulate the CPU, Hard Disk, Network, Memory, etc. to install a guest OS on it.

2. We can create a Microsoft Windows Virtual Machine on Linux. Please select the correct answer.

        Ans: True

3. We can provision and configure more than one Virtual Machine using Vagrant with a single Vagrantfile. Please select the correct answer.

        Ans: True

4. Which of following can be used as provisioner with Vagrant? Please select all the answers that apply.

        A. Shell
        B. Docker
        C. Ansible
        D. Jenkins

        Ans: A, B, C
        Note: Make sure you select all of the correct options—there may be more than one!




[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V000400_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V000500_DTH.mp4
[vid3]: https://edx-video.net/LINLFS15/LINLFS152016-V000600_DTH.mp4

[img1]: ./diagrams/Kernel-based_Virtual_Machine.svg

[bysc4]: http://creativecommons.org/licenses/by-sa/4.0/
[wikikvm]: https://upload.wikimedia.org/wikipedia/commons/4/40/Kernel-based_Virtual_Machine.svg
[qemu]: https://en.wikipedia.org/wiki/QEMU
[vbox]: https://www.virtualbox.org/
[guest]: https://www.virtualbox.org/wiki/Guest_OSes
[vagr]: https://www.vagrantup.com/
[vdoc]: https://www.vagrantup.com/docs/cli/
[vagp]: https://www.vagrantup.com/docs/providers/



