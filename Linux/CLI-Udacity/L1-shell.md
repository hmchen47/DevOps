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
    Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can [download it](](https://www.vagrantup.com/downloads.htm)) from vagrantup.com. Install the version for your operating system.

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


# In the VM or out of the VM?
We've set this course's exercises up to work in the virtual machine (VM) that you set up using the vagrant program. If you get logged out of the VM, you may end up typing shell commands in to your regular operating system instead of to the Linux system that we've set up for the course. Some commands won't work, and some files probably won't be where the course expects them to be.

## Getting logged out
If you type the command `exit` into the shell, or if you type `Control-D`, you will see a message like this:
> logout  
> Connection to 127.0.0.1 closed.

This just means that you got logged out. After logging out, you won't be in the VM any more.

To get back into the VM, use the command `vagrant ssh`.

## If `vagrant ssh` doesn't work
If you get a message like this:
> VM must be running to open SSH connection. Run `vagrant up`
> to start the virtual machine.

This means that the VM program is not running, for instance because you rebooted your computer. This is just fine and it doesn't mean you've lost any work. Just run `vagrant up` to bring the VM back up, then `vagrant ssh` to log in.

This will not take as long as the first time you ran it, because it won't need to download the Linux OS.

## If vagrant up doesn't work
If you get a message like this:
> A Vagrant environment or target machine is required to run this
> command. Run `vagrant init` to create a new Vagrant environment. Or,
> get an ID of a target machine from `vagrant global-status` to run
> this command on. A final option is to change to a directory with a
> Vagrantfile and to try again.

That means that __vagrant__ can't find the configuration file you downloaded. Go back to [the instructions](https://classroom.udacity.com/courses/ud595/lessons/4597278561/concepts/47133485700923), check to be sure that you did step 5, and then do step 6 again.

## Multiple terminals
If you open up more than one terminal window, only the one(s) that you ran `vagrant ssh` in will be connected to your Linux OS for this course. The others will be connected to your regular OS.

(It's actually really normal for Linux users to have to carefully keep track of which terminal windows are connected to which machines. Don't panic. Just look for whether "vagrant" appears on the command line.)

## Commands That Work
Here is the command that Philip asks you to run: `curl http://udacity.github.io/ud595-shell/stuff.zip -o things.zip`

# Quiz: The Terminal Interface
If you'd like to use the cowsay program outside of the VM, on your own computer, you can install it like this:
+ Ubuntu and Debian users: `sudo apt-get install cowsay`
+ Redhat and CentOS users: `sudo yum install cowsay`
+ OS X users: `brew install cowsay` (This requires the homebrew, a third party package manager for OS X, [http://brew.sh/](http://brew.sh/))
+ Arch Linux users: `sudo pacman -S cowsay`

Note: You typically need to be a “superuser” to install new software, that’s why these install commands begin with the sudo command . You can learn more about sudo in our [Configuring Linux Web Servers](https://www.udacity.com/course/configuring-linux-web-servers--ud299) course or on [Wikipedia](https://en.wikipedia.org/wiki/Sudo).


# The Terminal Vs The Shell
## Different shells
Unix and Linux programmers over the years have written many different shell programs. You can read more about them on Wikipedia: the original Bourne shell or sh; the __C shell__ or `csh`; the __Korn shell__ or `ksh`; the __Z shell__ or `zsh`; as well as the `bash` shell that this course uses.

Different systems may have different shells installed by default. Most Linux systems, and Mac OS X, default to `bash` for interactive shells. However, the most common default shell for scripting (shell programming) is classic `sh`. BSD Unix systems usually default to `sh` or `ksh`.

Almost everything in this course will work the same in any of these shell programs. The exception is one of the file matching (globbing) syntaxes at the end of Lesson 3.

## Some commands
+ `date`: display the time, not just the date
+ `expr`: simple calculator, ex. `expr 2 + 2` ==> 4
+ `echo`: the shell's print command.
+ `uname`: what operating system you're running on.
+ `host`: a handy interface to the Domain Name System (DNS).
+ `bash --version`: version option with bash
+ `history`: commands used

# Difference between shell command and Python or JavaScript language
