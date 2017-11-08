Chapter 07: Command Line Operations
===================================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Use the command line to perform operations in Linux.
+ Search for files.
+ Create and manage files.
+ Install and update software.

# Section 1: Command Line Mode Options
## Introduction to the Command Line
Linux system administrators spend a significant amount of their time at a __command line__ prompt. They often automate and troubleshoot tasks in this text environment. There is a saying, "graphical user interfaces make easy tasks easier, while command line interfaces make difficult tasks possible." Linux relies heavily on the abundance of command line tools. The command line interface provides the following advantages:

+ No GUI overhead.
+ Virtually every task can be accomplished using the command line.
+ You can script tasks and series of procedures.
+ You can sign into remote machines anywhere on the Internet.
+ You can initiate graphical applications directly from the command line.

## Some Basic Utilities
There are some basic command line utilities that are used constantly, and it would be impossible to proceed further without using some of them in simple form before we discuss them in more detail. A short list has to include:

+ `cat`: used to type out a file (or combine files)
+ `head`: used to show the first few lines of a file
+ `tail`: used to show the last few lines of a file
+ `man`: used to view documentation.

The screenshot shows elementary uses of these programs. Note the use of the `pipe` symbol (`|`) used to have one program take as input the output of another.

For the most part, we will only use these utilities in screenshots displaying various activities, before we discuss them in detail.

![image][img1]

## The Command Line
Most input lines entered at the shell prompt have three basic elements:

+ Command
+ Options
+ Arguments.

The __command__ is the name of the program you are executing. It may be followed by one or more __options__ (or switches) that modify what the command may do. Options usually start with one or two dashes, for example, `-p` or `--print`, in order to differentiate them from __arguments__, which represent what the command operates on.

However, plenty of commands have no options, no arguments, or neither. You can also type other things at the command line besides issuing commands, such as setting environment variables.

## sudo
All the demonstrations created have a user configured with `sudo` capabilities to provide the user with administrative (admin) privileges when required. `sudo` allows users to run programs using the security privileges of another user, generally `root` (superuser). The functionality of `sudo` is similar to that of `run as` in Windows.

On your own systems, you may need to set up and enable `sudo` to work correctly. To do this, you need to follow some steps that we will not explain in much detail now, but you will learn about later in this course. When running on __Ubuntu__, `sudo` is already always set up for you during installation. If you are running something in the __Fedora__ or __openSUSE__ families of distributions, you will likely need to set up `sudo` to work properly for you after the initial installation.

Next, you will learn the steps to setup and run `sudo` on your system.

## Steps for Setting Up and Running sudo
If your system does not already have `sudo` set up and enabled, you need to do the following steps:

1. You will need to make modifications as the administrative or superuser, `root`. While `sudo` will become the preferred method of doing this, we do not have it set up yet, so we will use `su` (which we will discuss later in detail) instead. At the command line prompt, type `su` and press Enter. You will then be prompted for the root password, so enter it and press Enter. You will notice that nothing is printed; this is so others cannot see the password on the screen. You should end up with a different looking prompt, often ending with ‘#’. For example: `$ su Password: #`
2. Now, you need to create a configuration file to enable your user account to use `sudo`. Typically, this file is created in the `/etc/sudoers.d/` directory with the name of the file the same as your username. For example, for this demo, let’s say your username is “student”. After doing step 1, you would then create the configuration file for “student” by doing this: `# echo "student ALL=(ALL) ALL" > /etc/sudoers.d/student`
3. Finally, some Linux distributions will complain if you do not also change permissions on the file by doing: `# chmod 440 /etc/sudoers.d/student`

That should be it. For the rest of this course, if you use `sudo` you should be properly set up. When using sudo, by default you will be prompted to give a password (your own user password) at least the first time you do it within a specified time interval. It is possible (though very insecure) to configure `sudo` to not require a password or change the time window in which the password does not have to be repeated with every `sudo` command.

## Using a Text Terminal on the Graphical Desktop
A __terminal emulator__ program emulates (simulates) a stand-alone terminal within a window on the desktop. By this, we mean it behaves essentially as if you were logging into the machine at a pure text terminal with no running graphical interface. Most terminal emulator programs support multiple terminal sessions by opening additional tabs or windows.

By default, on __GNOME__ desktop environments, the __gnome-terminal__ application is used to emulate a text-mode terminal in a window. Other available terminal programs include:

+ `xterm`
+ `rxvt`
+ `konsole`
+ `terminator`

![image][img2]

## Launching Terminal Windows
To open a terminal in __CentOS 7__:

+ Click `Applications->Utilities->Terminal`

To open a terminal in __openSUSE-Leap-42__ with __GNOME__:

+ Same action as __CentOS 7__

To open a terminal in __openSUSE-Leap-42__ with __KDE__:

+ Click on `System->Konsole`

To open a terminal in __Ubuntu 16.04 LTS__:

+ Click the Ubuntu icon and type `terminal` in the Search box.

If the __nautilus-open-terminal__ package is installed on any but some of the most recent __GNOME__-based distributions, you can always open a terminal by right-clicking anywhere on the desktop background and selecting Open in `Terminal`. This may work even if the package is not installed.

You can also hit `Alt-F2` and type in either __gnome-terminal__ or __konsole__, whichever is appropriate.

Distributions seem to bury opening up a command line terminal and the place in menus will vary in the desktop GUI as versions evolve. It is a good idea to figure out how to "pin" the terminal icon to the panel, 
which might mean adding it to "favorites" on __GNOME__ systems.

## Switching Between the GUI and the Command Line
The customizable nature of Linux allows you to drop (temporarily or permanently) the graphical interface, or to start it up after the system has been running.

Most Linux distributions give an option during installation (or even have differing versions of the install media) between desktop (with __X__) and server (usually without __X__).

Linux production servers are usually installed without __X__ and even if it is installed, usually do not launch it during system start up. Removing __X__ from a production server can be very helpful in maintaining a lean system which can be easier to support and keep secure.

![image][img3]

## Virtual Terminals
__Virtual Terminals (VT)__ are __console__ sessions that use the entire display and keyboard outside of a graphical environment. Such terminals are considered "virtual" because although there can be multiple active terminals, only one terminal remains visible at a time. A VT is not quite the same as a command line terminal window; you can have many of those visible at once on a graphical desktop.

One virtual terminal (usually number one or seven) is reserved for the graphical environment, and text logins are enabled on the unused VTs. __Ubuntu__ uses VT 7, but __CentOS/RHEL__ and openSUSE use VT 1 for the graphical display.

An example of a situation where using the VTs is helpful is when you run into problems with the graphical desktop. In this situation, you can switch to one of the text VTs and troubleshoot.

To switch between the VTs, press `CTRL-ALT-corresponding function key` for the VT. For example, press `CTRL-ALT-F6` for VT 6. (Actually, you only have to press the `ALT-F6` key combination if you are in a VT not running X and want to switch to another VT.)

![image][img4]

## Turning Off the Graphical Desktop
Linux distributions can start and stop the graphical desktop in various ways. The exact method differs from distribution and among distribution versions. For the newer systemd-based distributions, the display manager is run as a service, you can stop the GUI desktop with the `systemctl` utility and most distributions will also work with the `telinit` command, as in:

+ `sudo systemctl stop gdm` (or `sudo telinit 3`)

and restart it (after logging into the console) with:

+ `sudo systemctl start gdm` (or `sudo telinit 5`)

On Ubuntu, substitute `lightdm` for `gdm`.

## Knowledge Check
1. Which key combination would allow you to switch from the GUI to the text virtual terminal 4?

    A. CTRL-SHIFT-F4
    B. CTRL-ALT-SHIFT-SUPER-F4
    C. CTRL-ALT-F4
    D. CTRL-SHIFT-F4

    Ans: C
    Explanation
    The CTRL-ALT-F4 allows you to switch from the GUI to the text virtual terminal 4.

2. Assuming you are not the root user, which of the following commands would turn off the graphical desktop, depending on your specific Linux distribution?

    A. sudo telinit 3 
    B. sudo systemctl stop gdm 
    C. init 3
    D. sudo systemctl stop lightdm 

    Ans: A, B, D
    Explanation
    The exact method of bringing down the graphical interface is indeed Linux distribution dependent. The 3 methods will work depending on what display manager you are using and other factors.

## Lab 1: Killing the Graphical User Interface
From within a graphical terminal (gnome-terminal, konsole, etc), kill the current graphical desktop.

Your method will depend on your distribution, your greeter program (gdm, lightdm, kdm) and whether you have a systemd, SysVinit Upstart system.

Restart the GUI from the console.

Click [the link][lab1] to view a solution to the Lab exercise.

# Section 2: Basic Operations
## Basic Operations
In this section, we will discuss how to accomplish basic operations from the command line. These include how to log in and log out from the system, restart or shutdown the system, locate applications, access directories, identify the absolute and relative paths, and explore the filesystem.

![image][img5]

## Logging In and Out
An available text terminal will prompt for a username (with the string __login:__) and password. When typing your password, nothing is displayed on the terminal (not even a * to indicate that you typed in something), to prevent others from seeing your password. After you have logged into the system, you can perform basic operations.

Once your session is started (either by logging into a text terminal or via a graphical terminal program), you can also connect and log into remote systems via the __Secure Shell (SSH)__ utility. For example, by typing `ssh username@remote-server.com`, SSH would connect securely to the remote machine and give you a command line terminal window, using passwords (as with regular logins) or cryptographic keys (a topic we will not discuss) to prove your identity.

## Rebooting and Shutting Down
The preferred method to shut down or reboot the system is to use the `shutdown` command. This sends a warning message and then prevents further users from logging in. The `init` process will then control shutting down or rebooting the system. It is important to always shut down properly; failure to do so can result in damage to the system and/or loss of data.

The `halt` and `poweroff` commands issue `shutdown -h` to halt the system; reboot issues `shutdown -r` and causes the machine to reboot instead of just shutting down. Both rebooting and shutting down from the command line requires superuser (root) access.

When administering a multiuser system, you have the option of notifying all users prior to shutdown, as in:

`$ sudo shutdown -h 10:00 "Shutting down for scheduled maintenance."`

## Locating Applications
Depending on the specifics of your particular distribution's policy, programs and software packages can be installed in various directories. In general, executable programs should live in the `/bin, /usr/bin, /sbin, /usr/sbin` directories, or under `/opt`.

One way to locate programs is to employ the `which` utility. For example, to find out exactly where the diff program resides on the filesystem:

`$ which diff`

If which does not find the program, `whereis` is a good alternative because it looks for packages in a broader range of system directories:

`$ whereis diff`

as well as locating __source__ and __man__ files packaged with the program.

## Accessing Directories
When you first log into a system or open a terminal, the default directory should be your __home directory__; you can print the exact path of this by typing `echo $HOME`. (Many Linux distributions actually open new graphical terminals in `$HOME/Desktop`.) The following commands are useful for directory navigation:

| Command | Result |
|----------|---------|
| `pwd` | Displays the present working directory |
| `cd ~` or `cd` | Change to your home directory (short-cut name is ~ (tilde))|
| `cd ..` | Change to parent directory (..)|
| `cd -` | Change to previous directory (- (minus)) |

Note: The next two screens cover a demonstration and a Try-It-Yourself activity. You can view a demonstration and practice the Try-It-Yourself activity.

## Accessing Directories (video)
Click below to view a demonstration on how to login and accessing directories using the command prompt.

[video][vid1]

## Try-It-Yourself: Accessing Directories Using Command Prompt
To practice, click the link provided below.

[Accessing Directories Using Command Prompt][cpad]

## Understanding Absolute and Relative Paths
There are two ways to identify paths:

+ __Absolute pathname__: An absolute pathname begins with the root directory and follows the tree, branch by branch, until it reaches the desired directory or file. Absolute paths always start with /.
+ __Relative pathname__: A relative pathname starts from the present working directory. Relative paths never start with /.

Multiple slashes (/) between directories and files are allowed, but all but one slash between elements in the pathname is ignored by the system. `////usr//bin` is valid, but seen as `/usr/bin` by the system.

Most of the time, it is most convenient to use relative paths, which require less typing. Usually, you take advantage of the shortcuts provided by: `.` (present directory), `..` (parent directory) and `~` (your home directory).

For example, suppose you are currently working in your home directory and wish to move to the `/usr/bin` directory. The following two ways will bring you to the same directory from your home directory:

+ Absolute pathname method: `$ cd /usr/bin`
+ Relative pathname method: `$ cd ../../usr/bin`

In this case, the absolute pathname method is less typing.

![image][img6]

## Exploring the FileSystem
Traversing up and down the filesystem tree can get tedious. The `tree` command is a good way to get a bird’s-eye view of the filesystem tree. Use `tree -d` to view just the directories and to suppress listing file names.

The following commands can help in exploring the filesystem:

| Command | Usage |
|---------|-------|
| `cd /` | Changes your current directory to the root (/) directory (or path you supply) |
| `ls` | List the contents of the present working directory|
| `ls –a` | List all files including hidden files and directories (those whose name start with . ) |
| `tree` | Displays a tree view of the filesystem |

## Hard File Links
The __ln__ utility is used to create hard links and (with the `-s` option) soft links, also known as __symbolic links__ or __symlinks__. These two kinds of links are very useful in UNIX-based operating systems.

Suppose that file1 already exists. A hard link, called file2, is created with the command:

`$ ln file1 file2`

Note that two files now appear to exist. However, a closer inspection of the file listing shows that this is not quite true.

`$ ls -li file1 file2`

![image][img7]

The `-i` option to `ls` prints out in the first column the __inode number__, which is a unique quantity for each file object. This field is the same for both of these files; what is really going on here is that it is only __one__ file but it has more than one name associated with it, as is indicated by the __2__ that appears in the `ls` output. Thus, there was already another object linked to __file1__ before the command was executed.

Hard links are very useful and they save space, but you have to be careful with their use, sometimes in subtle ways. For one thing, if you remove either __file1__ or __file2__ in the example, the __inode object__ (and the remaining file name) will remain, which might be undesirable, as it may lead to subtle errors later if you recreate a file of that name.

If you edit one of the files, exactly what happens depends on your editor; most editors, including `vi` and `gedit`, will retain the link by default, but it is possible that modifying one of the names may break the link and result in the creation of two objects.

## Soft (Symbolic) Links
__Soft__ (or __Symbolic links__ are created with the `-s` option as in:
```
$ ln -s file1 file3
$ ls -li file1 file3
```
![image][img8]

Notice __file3__ no longer appears to be a regular file, and it clearly points to __file1__ and has a different inode number.

Symbolic links take no extra space on the filesystem (unless their names are very long). They are extremely convenient, as they can easily be modified to point to different places. An easy way to create a shortcut from your __home__ directory to long pathnames is to create a symbolic link.

Unlike hard links, soft links can point to objects even on different filesystems (or partitions) which may or may not be currently available or even exist. In the case where the link does not point to a currently available or existing object, you obtain a __dangling__ link.

## Exploring the Filesystem
Click below to view a demonstration on how to explore the filesystem.

[video][vid2]

## Navigating the Directory History
The `cd` command remembers where you were last, and lets you get back there with `cd -`. For remembering more than just the last directory visited, use `pushd` to change the directory instead of `cd`; this pushes your starting directory onto a list. Using `popd` will then send you back to those directories, walking in reverse order (the most recent directory will be the first one retrieved with `popd`). The list of directories is displayed with the dirs command.

Note: The next screen provides a video demonstration of using navigation.

![image][img9]

Click below to view a demonstration on how to navigate the directory history using command prompt.

[video][vid3]

## Knowledge Check
1. Assuming you are the root user, which commands allow you to shut down your system without rebooting?

    A. halt 
    B. shutdown -r now
    C. poweroff 
    D. shutdown -h now 

    Ans: A, C, D
    Explanation
    The halt, poweroff, and shutdown -h now commands allow you to shut down the system, as root, without rebooting.

2. Which commands allow you to locate programs?

    A. whichis
    B. which 
    C. whichever
    D. whereis 

    Ans: B, D
    Explanation
    The which and whereis commands allow you to locate programs.

3. Which of the following are examples of an absolute path?

    A. /etc/passwd 
    B. ../passwd
    C. //etc/passwd 
    D. \\passwd

    Ans: A, C
    Explanation
    /etc/passwd and //etc/passwd are valid examples of an absolute path. The multiple slashes (//) are legal, but all but one is ignored.

## Lab 2: Locating Applications
Find out the location of the ip network utility.

Click [the link][lab2] to view a solution to the Lab exercise.

# Section 3: Working with Files
Linux provides many commands that help you with viewing the contents of a file, creating a new file or an empty file, changing the timestamp of a file, and removing and renaming a file or directory. These commands help you in managing your data and files and in ensuring that the correct data is available at the correct location.

In this section, you will learn how to manage files.

## Viewing Files
You can use the following utilities to view files:

| Command | Usage |
|---------|-------|
| `cat` | Used for viewing files that are not very long; it does not provide any scroll-back.|
| `tac` | Used to look at a file backwards, starting with the last line. |
| `less` | Used to view larger files because it is a paging program; it pauses at each screen full of text, provides scroll-back capabilities, and lets you search and navigate within the file. Note: Use `/` to search for a pattern in the forward direction and `?` for a pattern in the backward direction. (An older program named `more` is still used, but has fewer capabilities.) |
| `tail` | Used to print the last 10 lines of a file by default. You can change the number of lines by doing `-n 15` or just `-15` if you wanted to look at the last 15 lines instead of the default. |
| `head` | The opposite of tail; by default, it prints the first 10 lines of a file.|

Click below to view a demonstration on how to view files.

[video][vid4]

## touch and mkdir
__touch__ is often used to set or update the access, change, and modify times of files. By default, it resets a file's time stamp to match the current time.

However, you can also create an empty file using touch:

`$ touch <filename>`

This is normally done to create an empty file as a placeholder for a later purpose.

__touch__ provides several options, but here is one of interest:

+ The `-t` option allows you to set the date and time stamp of the file.

To set the time stamp to a specific time:

`$ touch -t 03201600 myfile`

This sets the `myfile` file's time stamp to 4 p.m., March 20th (03 20 1600).

__mkdir__ is used to create a directory.:

+ To create a sample directory named `sampdir` under the current directory, type `mkdir sampdir`.
+ To create a sample directory called `sampdir` under `/usr`, type `mkdir /usr/sampdir`.

Removing a directory is simply done with `rmdir`. The directory must be empty or it will fail. To remove a directory and all of its contents you have to do `rm -rf`, as we shall discuss.

## Removing a File
| Command | Usage |
|---------|-------|
| `mv` | Rename a file |
| `rm` | Remove a file |
| `rm –f` | Forcefully remove a file |
| `rm –i` | Interactively remove a file |

If you are not certain about removing files that match a pattern you supply, it is always good to run rm interactively (`rm –i`) to prompt before every removal.

## Renaming or Removing a Directory
__rmdir__ works only on empty directories; otherwise you get an error.

While typing `rm –rf` is a fast and easy way to remove a whole filesystem tree recursively, it is extremely dangerous and should be used with the utmost care, especially when used by root (recall that recursive means drilling down through all sub-directories, all the way down a tree). Below are the commands used to rename or remove a directory:

| Command | Usage |
|---------|-------|
| `mv` | Rename a directory |
| `rmdir` | Remove an empty directory |
| `rm -rf` | Forcefully remove a directory recursively |

## Modifying the Command Line Prompt
The __PS1__ variable is the character string that is displayed as the prompt on the command line. Most distributions set __PS1__ to a known default value, which is suitable in most cases. However, users may want custom information to show on the command line. For example, some system administrators require the user and the host system name to show up on the command line as in:

`student@quad32 $`

This could prove useful if you are working in multiple roles and want to be always reminded of who you are and what machine you are on. The prompt above could be implemented by setting the PS1 variable to: `\u@\h \$`

For example:
```
$ echo $PS1
\$
$ PS1="\u@\h \$ "
coop@quad64 $ echo $PS1
\u@\h \$ 
coop@quad64 $ 
```

## Working With Files and Directories at the Command Prompt
Click below to view a demonstration on how to find files in a directory.

[video][vid5]

## Try-It-Yourself: Working With Files and Directories Using the Command Prompt
To practice, click the link provided below.

[Working With Files and Directories Using the Command Prompt][cpfd]

## Knowledge Check
1. Using which command can you view an entire file with scroll-back?

    a. tail
    b. cat
    c. less 
    d. head

    Ans: C
    Explanation
    The less command is used to view the entire file with scroll-back.
2. Using which command you forcefully remove a directory recursively?

    A. rmdir
    B. rm –rf 
    C. rmdir –f
    D. mv –rf

    Ans: B
    Explanation
    The rm -rf command is used to forcefully remove a directory.

## Lab 3: Creating, Moving and Removing Files
Create an empty file named `exercise.txt` and move this file to the `/tmp` directory, using a relative pathname from your home directory. Then, delete this file using an absolute pathname.

Click [the link][lab3] to view a solution to the Lab exercise.


# Section 4: Searching for Files
## Standard File Streams
When commands are executed, by default there are three standard __file streams__ (or __descriptors__) always open for use: standard input (standard in or __stdin__), standard output (standard out or __stdout__) and standard error (or __stderr__).

| Name | Symbolic Name | Value | Example |
|------|---------------|-------|---------|
| standard input | `stdin` | 0 | keyboard |
| standard output | `stdout` | 1 | terminal |
| standard error | `stderr` | 2 | log file |

Usually, `stdin` is your keyboard, `stdout` and `stderr` are printed on your terminal; often, `stderr` is redirected to an error logging file. `stdin` is often supplied by directing input to come from a file or from the output of a previous command through a __pipe__. `stdout` is also often redirected into a file. Since `stderr` is where error messages are written, often nothing will go there.

In Linux, all open files are represented internally by what are called __file descriptors__. Simply put, these are represented by numbers starting at zero. `stdin` is file descriptor 0, `stdout` is file descriptor 1, and `stderr` is file descriptor 2. Typically, if other files are opened in addition to these three, which are opened by default, they will start at file descriptor 3 and increase from there.

On the next screen and in the chapters ahead, you will see examples which alter where a running command gets its input, where it writes its output, or where it prints diagnostic (error) messages. 

## I/O Redirection
Through the command __shell__ we can __redirect__ the three standard file streams so that we can get input from either a file or another command instead of from our keyboard, and we can write output and errors to files or send them as input for subsequent commands.

For example, if we have a program called `do_something` that reads from `stdin` and writes to `stdout` and `stderr`, we can change its input source by using the less-than sign ( `<` ) followed by the name of the file to be consumed for input data:

`$ do_something < input-file`

If you want to send the output to a file, use the greater-than sign ( `>` ) as in:

`$ do_something > output-file`

Because `stderr` is not the same as `stdout`, error messages will still be seen on the terminal windows in the above example.

If you want to redirect `stderr` to a separate file, you use stderr’s file descriptor number (__2__), the greater-than sign ( `>` ), followed by the name of the file you want to hold everything the running command writes to stderr:

`$ do_something 2> error-file`

A special shorthand notation can be used to put anything written to file descriptor 2 (`stderr`) in the same place as file descriptor 1 (stdout): `2>&1`

`$ do_something > all-output-file 2>&1`

bash permits an easier syntax for the above:

`$ do_something >& all-output-file`

## Pipes
The UNIX/Linux philosophy is to have many simple and short programs (or commands) cooperate together to produce quite complex results, rather than have one complex program with many possible options and modes of operation. In order to accomplish this, extensive use of __pipes__ is made; you can pipe the output of one command or program into another as its input.

In order to do this, we use the vertical-bar, `|`, (pipe symbol) between commands as in:
 
`$ command1 | command2 | command3`

The above represents what we often call a __pipeline__ and allows Linux to combine the actions of several commands into one. This is extraordinarily efficient because `command2` and `command3` do not have to wait for the previous pipeline commands to complete before they can begin hacking at the data in their input streams; on multiple CPU or core systems the available computing power is much better utilized and things get done quicker. In addition, there is no need to save output in (temporary) files between the stages in the pipeline, which saves disk space and reduces reading and writing from disk, which is often the slowest bottleneck in getting something done.

## Searching for Files
Being able to quickly find the files you are looking for will make you a much happier Linux user! You can search for files in your parent directory or any other directory on the system as needed.

We will now learn how to use the `locate` and `find` utilities, and how to use wildcards in bash.

## locate
The `locate` utility program performs a search through a previously constructed database of files and directories on your system, matching all entries that contain a specified character string. This can sometimes result in a very long list.

To get a shorter more relevant list, we can use the `grep` program as a filter; `grep` will print only the lines that contain one or more specified strings, as in: 

`$ locate zip | grep bin`

which will list all the files and directories with both "zip" and "bin" in their name . (We will cover grep in much more detail later.) Notice the use of `|` to pipe the two commands together.

`locate` utilizes the database created by another program, `updatedb`. Most Linux systems run this automatically once a day. However, you can update it at any time by just running `updatedb` from the command line as the root user.

![image][imga]

### Locating Files
Click below to view a demonstration on how to locate files using the command prompt.

[video][vid6]

### Try-It-Yourself: Locating Files
To practice, click the link provided below.

[Locating Files][lf]

## Wildcards and Matching File Names
You can search for a filename containing specific characters using wildcards.

| Wildcard | Result |
|----------|--------|
| `?` | Matches any single character |
| `*` | Matches any string of characters |
| `[set]` | Matches any character in the set of characters, for example [adf] will match any occurrence of "a", "d", or "f" |
| `[!set]` | Matches any character not in the set of characters |

To search for files using the `?` wildcard, replace each unknown character with `?`, e.g. if you know only the first 2 letters are 'ba' of a 3-letter filename with an extension of `.out`, type `ls ba?.out`.

To search for files using the `*` wildcard, replace the unknown string with `*`, e.g. if you remember only that the extension was .out, type `ls *.out`

### Using bash Wildcards to Search Files
Click below to view a demonstration on how to use bash Wildcards to search files.

[video][vid7]

### Try-It-Yourself: Using bash Wildcards with ls
To practice, click the link provided below.

[Locating Files Using bash Wildcards][wild]

## Finding Files
`find` is an extremely useful and often-used utility program in the daily life of a Linux system administrator. It recurses down the filesystem tree from any particular directory (or set of directories) and locates files that match specified conditions. The default pathname is always the present working directory.

For example, administrators sometimes scan for large __core__ files (which contain diagnostic information after a program fails) that are more than several weeks old in order to remove them. It is also common to remove files in `/tmp` (and other temporary directories, such as those containing cached files) that have not been accessed recently. Many distros use automated scripts that run periodically to accomplish such house cleaning.

![image][imgb]

### Using find
When no arguments are given, find lists all files in the current directory and all of its subdirectories. Commonly used options to shorten the list include `-name` (only list files with a certain pattern in their name), `-iname` (also ignore the case of file names), and `-type` (which will restrict the results to files of a certain specified type, such as `d` for directory, `l` for symbolic link, or `f` for a regular file, etc). 

Searching for files and directories named "gcc":

`$ find /usr -name gcc`

Searching only for directories named "gcc":

`$ find /usr -type d -name gcc`

Searching only for regular files named "gcc":

`$ find /usr -type f -name gcc`

### Using Advanced find Options
Another good use of find is being able to run commands on the files that match your search criteria. The `-exec` option is used for this purpose.

To find and remove all files that end with .swp:

`$ find -name "*.swp" -exec rm {} ’;’`

The `{}` (squiggly brackets) is a place holder that will be filled with all the file names that result from the find expression, and the preceding command will be run on each one individually.

Please note that you have to end the command with either `‘;’` (including the single-quotes) or `"\;"`. Both forms are fine.

One can also use the `-ok` option, which behaves the same as `-exec`, except that `find` will prompt you for permission before executing the command. This makes it a good way to test your results before blindly executing any potentially dangerous commands.

![image][imgc]

### Finding Files Based on Time and Size
It is sometimes the case that you wish to find files according to attributes, such as when they were created, last used, etc., or based on their size. Both are easy to accomplish.

To find files based on time:

`$ find / -ctime 3`

Here, `-ctime` is when the inode metadata (i.e., file ownership, permissions, etc.) last changed; it is often, but not necessarily, when the file was first created. You can also search for accessed/last read (`-atime`) or modified/last written (`-mtime`) times. The number is the number of __days__ and can be expressed as either a number (`n`) that means exactly that value, `+n`, which means greater than that number, or `-n`, which means less than that number. There are similar options for times in minutes (as in `-cmin`, `-amin`, and `-mmin`).

To find files based on sizes:

`$ find / -size 0`

Note the size here is in __512-byte blocks__, by default; you can also specify bytes (`c`), kilobytes (`k`), megabytes (`M`), gigabytes (`G`), etc. As with the time numbers above, file sizes can also be exact numbers (`n`), `+n` or `-n`. For details, consult the man page for find.

For example, to find files greater than 10 MB in size and running a command on those files:

`$ find / -size +10M -exec command {} ’;’`

### Finding Files In a Directory
Click below to view a demonstration on how to find files in a directory.

[video][vid8]

### Try-It-Yourself: Using find
To practice, click the link provided below.

[Using find][find]

## Knowledge Check
1. Which command is used to perform a database search of pathnames given the substring that is provided as a parameter?

    Explanation
    The locate program performs a database search of pathnames given the substring that is provided as a parameter to locate.

2. Which bash wildcard is used to match any single character?

    Explanation
    The ? bash wildcard is used to match any single character.


## Lab 4: Finding Directories and Creating Symbolic Links
Find the `init.d` directory, starting from `/`, and then create a symbolic link from within your home directory to this directory.

(Note that this SysVinit directory is no longer used much in systemd-based systems, but is kept for backwards compatibility reasons.)

Click [the link][lab4] to view a solution to the Lab exercise.


# Section 5: Installing Software
## Package Management Systems on Linux
The core parts of a Linux distribution and most of its add-on software are installed via the __Package Management System__. Each package contains the files and other instructions needed to make one software component work on the system. Packages can depend on each other. For example, a package for a web-based application written in PHP can depend on the PHP package.

There are two broad families of package managers: those based on __Debian__ and those which use __RPM__ as their low-level package manager. The two systems are incompatible, but provide the same features at a broad level. There are some other systems used by more specialized Linux distributions.

In this section, you will learn how to install, remove, or search for packages using the different package management tools.

## Package Managers: Two Levels
Both package management systems provide two tool levels: a low-level tool (such as `dpkg` or `rpm`) takes care of the details of unpacking individual packages, running scripts, getting the software installed correctly, while a high-level tool (such as `apt-get`, `yum`, or `zypper`) works with groups of packages, downloads packages from the vendor, and figures out dependencies.

Most of the time users need work only with the high-level tool, which will take care of calling the low-level tool as needed. Dependency tracking is a particularly important feature of the high-level tool, as it handles the details of finding and installing each dependency for you. Be careful, however, as installing a single package could result in many dozens or even hundreds of dependent packages being installed.

![image][imgd]

## Working With Different Package Management Systems
The __Advanced Packaging Tool (apt)__ is the underlying package management system that manages software on __Debian__-based systems. While it forms the backend for graphical package managers, such as the __Ubuntu Software Center__ and __synaptic__, its native user interface is at the command line, with programs that include `apt-get` and `apt-cache`.

__Yellowdog Updater Modified (yum)__ is an open source command-line package-management utility for __RPM__-compatible Linux systems, basically what we have called the __Fedora__ family. yum has both command line and graphical user interfaces. Recent __Fedora__ versions have replaced yum with a new utility called `dnf`, which has less historical baggage, has nice new capabilities and is mostly backwards compatible with `yum` for day-to-day commands.

`zypper` is a package management system for __openSUSE__ that is based on __RPM__. `zypper` also allows you to manage repositories from the command line. `zypper` is fairly straightforward to use and resembles yum quite closely.

To learn the basic packaging commands, click the link below:

[Basic Packaging Commands][bpc]

 | Operation | RPM | deb |
 |-----------|-----|-----|
 | Install package | `rpm -i foo.rpm` | `dpkg --install foo.deb` | 
 | Install package, dependencies | `yum install foo` | `apt-get install foo` | 
 | Remove package | `rpm -e foo.rpm` | `dpkg --remove foo.deb` | 
 | Remove package, dependencies | `yum remove foo` | `apt-get autoremove foo` | 
 | Update package | `rpm -U foo.rpm` | `dpkg --install foo.deb` | 
 | Update package, dependencies | `yum update foo` | `apt-get install foo` | 
 | Update entire system | `yum update` | `apt-get dist-upgrade` | 
 | Show all installed packages | `rpm -qa` or `yum list installed` | `dpkg --list` | 
 | Get information on package | `rpm -qil foo` | `dpkg --listfiles foo` | 
 | Show packages named foo | `yum list "foo"` | `apt-cache search foo` | 
 | Show all available packages | `yum list` | `apt-cache dumpavail foo` | 
 | What package is file part of? | `rpm -qf file` | `dpkg --search file` | 

Note: The next few screens cover the demonstrations of a member of each of the three Linux distribution families we cover in this course. You can view a demonstration for the distribution type of your choice.

## Managing Software Packages on Ubuntu
Click below to view a demonstration on how to manage software packages on __Ubuntu__.

[video][vid9]

## Managing Software Packages on CentOS
Click below to view a demonstration on how to manage software packages on __CentOS__.

[video][vida]

## Managing Software Packages on openSUSE
Click below to view a demonstration on how to manage Linux package on __openSUSE__.

[video][vidb]

## Knowledge Check
1. Which of the following are high-level package managers?

        A. dpkg
        B. apt 
        C. yum 
        D. zypper 

        Ans: B, C, D
        Explanation
        apt, yum, and zypper are high-level package managers.

2. Which of the following are low-level package managers?

        A. dpkg 
        B. apt
        C. yum
        D. rpm 

        Ans: A, D
        Explanation
        dpkg and rpm are low-level package managers.

## Lab 5: Installing and Removing Software Packages
Using the upper level package management system appropriate for your Linux distribution, do the following:

+ Install the dump package on your system.
+ Remove the dump package from your system.

NOTE: If dump is already installed (you will be told so when you try to install), then do things in opposite order, i.e., remove and then install.

Click [the link][lab5] to view a solution to the Lab exercise.


# Summary
You have completed this chapter. Let’s summarize the key concepts we covered:

+ __Virtual terminals (VT)__ in Linux are consoles, or command line terminals that use the connected monitor and keyboard.
+ Different Linux distributions start and stop the graphical desktop in different ways.
+ A terminal emulator program on the graphical desktop works by emulating a terminal within a window on the desktop.
+ The Linux system allows you to either log in via text terminal or remotely via the console.
+ When typing your password, nothing is printed to the terminal, not even a generic symbol to indicate that you typed.
+ The preferred method to shut down or reboot the system is to use the `shutdown` command.
+ There are two types of __pathnames__: absolute and relative.
+ An absolute pathname begins with the root directory and follows the tree, branch by branch, until it reaches the desired directory or file.
+ A relative pathname starts from the present working directory.
+ Using __hard__ and __soft__ (symbolic) links is extremely useful in Linux.
+ `cd` remembers where you were last, and lets you get back there with `cd -`.
+ `locate` performs a database search to find all file names that match a given pattern.
+ `find` locates files recursively from a given directory or set of directories.
+ `find` is able to run commands on the files that it lists, when used with the `-exec` option.
+ `touch` is used to set the access, change, and edit times of files, as well as to create empty files.
+ The __Advanced Packaging Tool (apt)__ package management system is used to manage installed software on __Debian__-based systems.
+ You can use the __Yellowdog Updater Modified (yum)__ open source command-line package-management utility for __RPM__-compatible Linux operating systems.
+ The `zypper` package management system is based on __RPM__ and used for __openSUSE__.



[viid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002200_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005500_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V006100_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002600_DTH.mp4
[vid4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V001200_DTH.mp4
[vid5]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005000_DTH.mp4
[vid6]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003900_DTH.mp4
[vid7]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V010300_DTH.mp4
[vid8]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002100_DTH.mp4
[vid9]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004100_DTH.mp4
[vida]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005100_DTH.mp4
[vidb]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004000_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6861da296abac83526d30c5e1ca0567b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/cmdutils.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8de9705c7b1a71d12ec2d5308478064e/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/commandall.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fdf3d8ddc3302ea1dbf406d4547b8655/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch06_screen06.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/cce9159be8b08390567dc02f1043cf92/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch06_screen07.jpg
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/678d889dcb1112024ef10815f9210a07/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch06_screen11.jpg
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c9a79bc0bfc23d476b1c89380ca90aad/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch06_screen19.jpg
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/aefe6c7fa6a198680e110ceae5c95c11/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lnubuntu.png
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/cea407ef8cfd36b34ede2a154959a98f/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lnsubuntu.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8cda89b4595a6b8dde4ba73674b88261/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/pushdcentos.png
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/db04248c7965e78a927a0fa8a42fc703/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/locatesuse.png
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/102046563ac484a6047300c801886837/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/findubuntu.png
[imgc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/cbdf6dc606a39eace7d669077837e628/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch06_screen41.jpg
[imgd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8c786acf21df4cc0c81d315e375896d4/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch06_screen60.jpg


[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-killgui.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-whereis.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-fileops.html
[lab4]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-find.html
[lab5]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-package.html

[cpad]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingcd/index.html
[cpfd]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingfilesdirs/index.html
[lf]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usinglocate/index.html
[wild]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usinglswildcards/index.html
[find]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingfind/index.html
[bpc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f478e1c28b54f5df1d53ef1bc855b2e3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/Basic_Packagaing_Commands.pdf
