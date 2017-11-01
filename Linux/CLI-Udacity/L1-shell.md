Get Into the Shell
==================

# Virtual Machine
A virtual machine (VM) is a computer program that simulates a computer. The VM software we're using in this course is called __VirtualBox__. When you set up your virtual machine you installed Linux on the VM, making Linux the __guest operating system__. The operating system (OS) that's installed directly on your physical computer is called the __host OS__.

We use a virtual machine in this course to ensure that everyone is working in an identical environment with the correct programs installed, but there are many other reasons programmers use VMs.

__VMs isolate programming projects__ from everything else on a programmer's computer. The programmer can configure the guest OS by installing programs and customizing settings without disrupting their day-to-day environment.

__VMs are also used to simulate the environment that software will be deployed to.__ Most developers use Windows or Mac OS, but often deploy their code to servers running Linux. Using a Linux VM lets programmers run code on their target platform, without leaving the comfort of their preferred host OS.

## Vagrant
Vagrant is a program that makes VMs more convenient to use. For example when you ran `vagrant up` Vagrant created a VM, installed a guest OS, and configured the guest OS. Vagrant did all of this automatically by following instructions in the Vagrantfile. Automating this process saves time and ensures consistent results.

Vagrant also makes it easy to edit files that are in the VM from programs installed on the host OS. We won't use this feature in this class, but it's very helpful in other Udacity courses and on the job.

## Command Line Interface
Programmers encounter many different command line interfaces (__CLI__s) in their work. Any computer interface where the user enters textual commands and gets textual responses is a CLI. While CLIs vary significantly, proficiency in one will give you a head start learning another. In this class we mostly work with the Linux command line interface in a VM, but in order to access that you need to use your host OS's command line interface. Other command line interfaces you might encounter as a developer are your browser's tools and Python's interactive interpreter.

[!picture1](https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57d744b9_devtoolscli/devtoolscli.png)

A screenshot of Chrome Developer Tools' console, which is a sort of command line interface with your browser.
[!picture2](https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57d74547_pythoncli/pythoncli.png)

Different programming languages will have different Command Line Interfaces (CLIs). A screenshot of an interactive Python session on the command line using the Python CLI. Instead of using a software program with a more standard visual user interface, many programmers often use the command line with a CLI as shown above.


# Your own Linux box
To learn the Linux shell, you need a Linux machine to run it on. But we can't really ship a new Linux computer to every one of you. So instead you will set up a Linux virtual machine (VM) on your own computer.

You'll be using the [VirtualBox](https://www.virtualbox.org/wiki/Downloads) application to run the virtual machine, and the [vagrant](https://www.vagrantup.com/) software to configure it.

This virtual-machine setup is very similar to the ones you will use in later Udacity courses on the Linux platform. So when you get to those courses, you will not need to re-install this software.

Setting the virtual machine up is not complicated, but it will take some time when your computer downloads the Linux OS. Follow the instructions below to set it up before proceeding on in this course.

## What's a virtual machine?
A virtual machine is a program that runs on your Windows or Mac computer, and that can run a different operating system inside it. In this case, you'll be running an Ubuntu Linux server system.

1. Install Git
    + You can skip this step if you are not running Windows, but many other courses use Git, so you may want to install it now.
    + Download Git from [git-scm.com](http://git-scm.com/downloads). Install the version for your operating system.
    + On Windows, Git will provide you with the Git Bash terminal program, which you will use to run and connect to your Linux VM.

2. Find your terminal program
    To take this course you will need to use a terminal program, which presents the shell user interface and lets you log in to your Linux VM.
    + Windows: Use the `Git Bash` program, which is installed with Git (above).
    + Mac OS X: Use the `Terminal` program, located in your `Applications/Utilities` folder.
    + Linux: Use any terminal program (e.g. `xterm` or `gnome-terminal`).

3. Install VirtualBox
    VirtualBox is the software that actually runs the VM. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

    Ubuntu 14.04 Note: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

4. Install Vagrant
    Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from [vagrantup.com](https://www.vagrantup.com/downloads.htm). Install the version for your operating system.

    Windows Note: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

5. Download the VM configuration file
    Make a new folder to keep your workspace for this course. You might call it Shell, but whatever name you pick is OK. Keep track of what folder you created it in (for instance, Desktop).

    In the Supporting Materials section of this page, below, you'll find a link to the configuration file, called [Vagrantfile](https://www.udacity.com/api/nodes/4713348570/supplemental_media/vagrantfile/download). Download this file into the new folder you just created.

6. Run the virtual machine!
    Open your terminal program. Type this shell command and press Enter:
        `cd Desktop/Shell`  
    (If your new folder is called something other than "Shell", or is located somewhere other than "Desktop", change those.)

    Then start the VM by running the command `vagrant up`.

    This will make your system download the Linux OS and start up the virtual machine. Unfortunately, this will take a long time on most network connections. Fortunately, you only have to do it once, and the same Linux OS image will work for later Udacity courses too.

    Once it is done, run the command `vagrant ssh`.

And you will be logged in to the virtual machine and ready to do the course exercises!
    The Udacity VM is the official shell for this class, but if your computer already has a Unix* shell you can use it if you prefer.

    Caveat: Your computer's own shell may differ from the VM in unanticipated ways, and may not have all the programs installed which the VM provides. The recommended environment is the VM.

* if you're running Linux or Mac OS X for instance


