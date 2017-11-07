Chapter 09: Processes
=====================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Describe what a process is and distinguish between types of processes.
+ Enumerate process attributes.
+ Manage processes using `ps` and `top`.
+ Understand the use of load averages and other process metrics.
+ Manipulate processes by putting them in __background__ and restoring them to __foreground__.
+ Use `at`, `cron`, and `sleep` to schedule processes in the future or pause them.


# Section 1: Introduction to Processes and Process Attributes
## What Is a Process?
A __process__ is simply an instance of one or more related __tasks__ (__threads__) executing on your computer. It is not the same as a __program__ or a __command__; a single program may actually start several processes simultaneously. Some processes are independent of each other and others are related. A failure of one process may or may not affect the others running on the system.

Processes use many system resources, such as memory, CPU (central processing unit) cycles, and peripheral devices, such as printers and displays. The operating system (especially the kernel) is responsible for allocating a proper share of these resources to each process and ensuring overall optimum utilization.

![image][img1]

## Process Types
A terminal window (one kind of command shell) is a process that runs as long as needed. It allows users to execute programs and access resources in an interactive environment. You can also run programs in the __background__, which means they become __detached__ from the shell.

Processes can be of different types according to the task being performed. Here are some different process types, along with their descriptions and examples:

| Process Type | Description | Example |
|--------------|-------------|---------|
| Interactive Processes | Need to be started by a user, either at a command line or through a graphical interface such as an icon or a menu selection. | `bash`, `firefox`, `top` |
| Batch Processes | Automatic processes which are scheduled from and then disconnected from the terminal. These tasks are queued and work on a FIFO (First In, First Out) basis | `updatedb` |
| Daemons | Server processes that run continuously. Many are launched during system startup and then wait for a user or system request indicating that their service is required. | `httpd`, `xinetd`, `sshd` |
| Threads | Lightweight processes. These are tasks that run under the umbrella of a main process, sharing memory and other resources, but are scheduled and run by the system on an individual basis. An individual thread can end without terminating the whole process and a process can create new threads at any time. Many non-trivial programs are multi-threaded. | `firefox`, `gnome-terminal-server` |
| Kernel Threads | Kernel tasks that users neither start nor terminate and have little control over. These may perform actions like moving a thread from one CPU to another, or making sure input/output operations to disk are completed. | `kthreadd`, `migration`, `ksoftirqd` |

## Process Scheduling and States
A critical kernel function called the __scheduler__ constantly shifts processes on and off the CPU, sharing time according to relative priority, how much time is needed and how much has already been granted to a task. 

When a process is in a so-called __running__ state, it means it is either currently executing instructions on a CPU, or is waiting to be granted a share of time (a __time slice__) so it can execute. All processes in this state reside on what is called a __run queue__ and on a computer with multiple CPUs, or cores, there is a run queue on each.

However, sometimes processes go into what is called a __sleep__ state, generally when they are waiting for something to happen before they can resume, perhaps for the user to type something. In this condition, a process is sitting on a __wait queue__.

There are some other less frequent process states, especially when a process is terminating. Sometimes, a child process completes, but its parent process has not asked about its state. Amusingly, such a process is said to be in a __zombie__ state; it is not really alive, but still shows up in the system's list of processes.

![image][img2]

## Process and Thread IDs
At any given time, there are always multiple processes being executed. The operating system keeps track of them by assigning each a unique __process ID (PID)__ number. The PID is used to track process state, cpu usage, memory use, precisely where resources are located in memory, and other characteristics.

New PIDs are usually assigned in ascending order as processes are born. Thus, PID 1 denotes the __init__ process (initialization process), and succeeding processes are gradually assigned higher numbers.

The table explains the PID types and their descriptions:

| ID Type | Description |
|---------| ------------|
| Process ID (PID) | Unique Process ID number |
| Parent Process ID (PPID) | Process (Parent) that started this process. If the parent dies, the PPID will refer to an adoptive parent; on recent kernels, this is kthreadd which has PPID=2. |
| Thread ID (TID) | Thread ID number. This is the same as the PID for single-threaded processes. For a multi-threaded process, each thread shares the same PID, but has a unique TID. |

## Terminating A Process
At some point, one of your applications may stop working properly. How might you terminate it?

To terminate a process, you can type `kill -SIGKILL <pid>` or `kill -9 <pid>`. Note however, you can only kill your own processes; those belonging to another user are off limits, unless you are root.

## User and Group IDs
Many users can access a system simultaneously, and each user can run multiple processes. The operating system identifies the user who starts the process by the Real User ID (__RUID__) assigned to the user.

The user who determines the access rights for the users is identified by the Effective UID (__EUID__). The EUID may or may not be the same as the RUID.

Users can be categorized into various groups. Each group is identified by the Real Group ID, or __RGID__. The access rights of the group are determined by the Effective Group ID, or __EGID__. Each user can be a member of one or more groups.

Most of the time we ignore these details and just talk about the User ID (__UID__).

![image][img3]

## More About Priorities
At any given time, many processes are running (i.e., in the run queue) on the system. However, a CPU can actually accommodate only one task at a time, just like a car can have only one driver at a time. Some processes are more important than others, so Linux allows you to set and manipulate process __priority__. Higher priority processes are granted more time on the CPU.

The priority for a process can be set by specifying a __nice value__, or __niceness__, for the process. The lower the nice value, the higher the priority. Low values are assigned to important processes, while high values are assigned to processes that can wait longer. A process with a high nice value simply allows other processes to be executed first. In Linux, a nice value of -20 represents the highest priority and 19 represents the lowest. (This does sound kind of backwards, but this convention, the nicer the process, the lower the priority, goes back to the earliest days of UNIX.)

You can also assign a so-called __real-time priority__ to time-sensitive tasks, such as controlling machines through a computer or collecting incoming data. This is just a very high priority and is not to be confused with what is called __hard real time__ which is conceptually different, and has more to do with making sure a job gets completed within a very well-defined time window.

![image][img4]

## Knowledge Check
1. Which of the below choices points to server processes that get initialized during system startup and then wait for a user or system request indicating that work needs to be done?

        A. Batch Processes
        B. Daemons 
        C. Nice Processes
        D. Interrupt Handlers

        Ans: B
        Explanation
        Daemons are the server processes that get initialized during a system startup and then wait for a user or system request indicating that their service is required.

2. Which of the following is scheduled to run and then disconnected from the terminal?

        A. interactive process
        B. batch process 
        C. kernel threads
        D. threads

        Ans: B
        Explanation
        The batch process is scheduled and disconnected from the terminal.

3. What are possible states of a process?

        A. Running 
        B. gitated
        C. Sleeping (Waiting) 
        D. Nice

        Ans: A, C
        Explanation
        Both Running and Sleeping are possible states of a process.

4. Which of the following is the unique identifier for a process?

        A. PID 
        B. PPID
        C. TID
        D. UID

        Ans: A
        Explanation
        PID is the unique identifier for a process.

5. Identify the correct statements.

        A. High priority jobs have higher nice value.
        B. High priority jobs have lower nice value. 
        C. Low priority jobs have higher nice value. 
        D. Low priority jobs have lower nice value.

        Ans: B, C
        Explanation
        High priority jobs have lower nice value and low priority jobs have higher nice value.


# Section 2: Process Metrics and Process Control
## Load Averages
__Load average__ is the average of the __load number__ for a given period of time. It takes into account processes that are:

+ Actively running on a CPU.
+ Considered runnable, but waiting for a CPU to become available.
+ Sleeping: i.e., waiting for some kind of resource (typically, I/O) to become available.

Note that Linux differs from other UNIX-like operating systems in that it includes the sleeping processes. Furthermore, it only includes so-called __uninterruptible__ sleepers, those which cannot be awakened easily.

The load average can be viewed by running `w`, `top` or `uptime`.

![image][img5]

## Interpreting Load Averages
The load average is displayed using three different sets of numbers, as shown in the following example:

![image][img6]

The last piece of information is the average load of the system. Assuming our system is a single-CPU system, the three load average numbers are interpreted as follows:

+ `0.45`: For the last minute the system has been 45% utilized on average.
+ `0.17`: For the last 5 minutes utilization has been 17%.
+ `0.12`: For the last 15 minutes utilization has been 12%.

If we saw a value of 1.00 in the second position, that would imply that the single-CPU system was 100% utilized, on average, over the past 5 minutes; this is good if we want to fully use a system. A value over 1.00 for a single-CPU system implies that the system was over-utilized: there were more processes needing CPU than CPU was available.

If we had more than one CPU, say a quad-CPU system, we would divide the load average numbers by the number of CPUs. In this case, for example, seeing a 1 minute load average of 4.00 implies that the system as a whole was 100% (4.00/4) utilized during the last minute.

Short-term increases are usually not a problem. A high peak you see is likely a burst of activity, not a new level. For example, at start up, many processes start and then activity settles down. If a high peak is seen in the 5 and 15 minute load averages, it may be cause for concern.

## Background and Foreground Processes
Linux supports __background__ and __foreground__ job processing. (A job in this context is just a command launched from a terminal window.) __Foreground__ jobs run directly from the shell, and when one foreground job is running, other jobs need to wait for shell access (at least in that terminal window if using the GUI) until it is completed. This is fine when jobs complete quickly. But this can have an adverse effect if the current job is going to take a long time (even several hours) to complete.

In such cases, you can run the job in the __background__ and free the shell for other tasks. The background job will be executed at __lower priority__, which, in turn, will allow smooth execution of the interactive tasks, and you can type other commands in the terminal window while the background job is running. By default, all jobs are executed in the foreground. You can put a job in the background by suffixing `&` to the command, for example: `updatedb &`

You can either use `CTRL-Z` to suspend a foreground job or `CTRL-C` to terminate a foreground job and can always use the `bg` and `fg` commands to run a process in the background and foreground, respectively.

![image][img7]

## Managing Jobs
The __jobs__ utility displays all jobs running in __background__. The display shows the job ID, state, and command name, as shown here.

`jobs -l` provides the same information as jobs, including the PID of the background jobs.

The background __jobs__ are connected to the terminal window, so, if you log off, the jobs utility will not show the ones started from that window.

![image][img8]

## Knowledge Check
1. The _____ shortcut is used to terminate a foreground process.

        A. CTRL-C 
        B. CTRL-Z
        C. ALT-C
        D. ALT-Z

        Ans: A
        Explanation
        CTRL-C is used to terminate a foreground process

2. Choose the correct statements related to 'CTRL-Z'.

        A. It is used to suspend the foreground processes. 
        B. It is used to suspend the background processes.
        C. It is used to reinitiate the foreground processes.
        D. It is used to reinitiate the background processes.

        Ans: A
        Explanation
        CTRL-Z is used to suspend a foreground process.

3. Which command is used to bring the process to the foreground?

        A. bg
        B. Sleep
        C. fg 
        D. &

        Ans: C
        Explanation
        The fg command is used to bring the process to the foreground.

4. Which command is used to enumerate the background processes running in the current terminal session?

        A. sleep
        B. fg
        C. jobs 
        D. bg

        Ans: C
        Explanation
        The jobs command is used to enumerate the background processes running in the current terminal session.

## Lab 1: Getting uptime and Load Averages
Ascertain how long your system has been up. 

Display its load averages.

Click [the link][lab1] to view a solution to the Lab exercise.

## Lab 2: Background and Foreground Jobs
We are going to launch a graphical program from a terminal window, so that one can no longer type in the window. gedit is an easy choice, but you can substitute any other program that does this.

The Solution file contains a step-by-step procedure for putting jobs in background, bringing them back to foreground, etc. Please repeat the steps, substituting the program you are using if it is not gedit.

Click [the link][lab2] to view a solution to the Lab exercise.


# Section 3: Listing Processes: ps and top
## The ps Command (System V Style)
`ps` provides information about currently running processes keyed by __PID__. If you want a repetitive update of this status, you can use `top` or other commonly installed variants, such as `htop` or `atop`, from the command line, or invoke your distribution's graphical system monitor application.

`ps` has many options for specifying exactly which tasks to examine, what information to display about them, and precisely what output format should be used.

Without options, ps will display all processes running under the current shell. You can use the `-u` option to display information of processes for a specified username. The command `ps -ef` displays all the processes in the system in full detail. The command `ps -eLf` goes one step further and displays one line of information for every __thread__ (remember, a process can contain multiple threads).

[image][img9]

## The ps Command (BSD Style)
`ps` has another style of option specification, which stems from the BSD variety of UNIX, where options are specified without preceding dashes. For example, the command `ps aux` displays all processes of all users. The command `ps axo` allows you to specify which attributes you want to view.

The screenshot shows a sample output of `ps` with the `aux` and `axo` qualifiers.

![image][imga]

## Using ps
Click below to view a demonstration on how to use ps  with various options.

[video][vid1]

## The Process Tree
`pstree` displays the processes running on the system in the form of a __tree diagram__ showing the relationship between a process and its parent process and any other processes that it created. Repeated entries of a process are not displayed, and threads are displayed in curly braces.

## top
While a static view of what the system is doing is useful, monitoring the system performance live over time is also valuable. One option would be to run `ps` at regular intervals, say, every two minutes. A better alternative is to use `top` to get constant real-time updates (every two seconds by default), until you exit by typing `q`. `top` clearly highlights which processes are consuming the most CPU cycles and memory (using appropriate commands from within `top`.)

![image][imgb]

### First Line of the top Output
The first line of the top output displays a __quick summary__ of what is happening in the system, including:

+ How long the system has been up
+ How many users are logged on
+ What is the load average.

The __load average__ determines how busy the system is. A load average of 1.00 per CPU indicates a fully subscribed, but not overloaded, system. If the load average goes above this value, it indicates that processes are competing for CPU time. If the load average is very high, it might indicate that the system is having a problem, such as a runaway process (a process in a non-responding state).

[image][imgc]

### Second Line of the top Output
The second line of the `top` output displays the total __number of processes__, the number of running, sleeping, stopped, and zombie processes. Comparing the number of running processes with the load average helps determine if the system has reached its capacity or perhaps a particular user is running too many processes. The stopped processes should be examined to see if everything is running correctly.

[image][imgd]

### Third Line of the top Output
The third line of the `top` output indicates how the __CPU time__ is being divided between the users (`us`) and the kernel (`sy`) by displaying the percentage of CPU time used for each.

The percentage of user jobs running at a lower priority (niceness - `ni`) is then listed. Idle mode (`id`) should be low if the load average is high, and vice versa. The percentage of jobs waiting (`wa`) for I/O is listed. Interrupts include the percentage of hardware (`hi`) vs. software interrupts (`si`). Steal time (`st`) is generally used with virtual machines, which has some of its idle CPU time taken for other uses.

[image][imge]

### Fourth and Fifth Lines of the top Output
The fourth and fifth lines of the top output indicate __memory usage__, which is divided in two categories:

+ Physical memory (RAM) – displayed on line 4.
+ Swap space – displayed on line 5.
+ Both categories display total memory, used memory, and free space.

You need to monitor memory usage very carefully to ensure good system performance. Once the physical memory is exhausted, the system starts using swap space (temporary storage space on the hard drive) as an extended memory pool, and since accessing disk is much slower than accessing memory, this will negatively affect system performance.

If the system starts using swap often, you can add more swap space. However, adding more physical memory should also be considered.

[image][imgf]

### Process List of the top Output
Each line in the process list of the top output displays information about a process. By default, processes are ordered by highest CPU usage. The following information about each process is displayed:

+ Process Identification Number (PID)
+ Process owner (USER)
+ Priority (PR) and nice values (NI)
+ Virtual (VIRT), physical (RES), and shared memory (SHR)
+ Status (S)
+ Percentage of CPU (%CPU) and memory (%MEM) used
+ Execution time (TIME+)
+ Command (COMMAND).

[image][imgg]

### Interactive Keys with top
Besides reporting information, `top` can be utilized interactively for monitoring and controlling processes. While `top` is running in a terminal window, you can enter single-letter commands to change its behavior. For example, you can view the top-ranked processes based on CPU or memory usage. If needed, you can alter the priorities of running processes or you can stop/kill a process.

The table lists what happens when pressing various keys when running top:

| Command | Output |
|---------|--------|
| `t` | Display or hide summary information (rows 2 and 3) |
| `m` | Display or hide memory information (rows 4 and 5) |
| `A` | Sort the process list by top resource consumers | 
| `r` | Renice (change the priority of) a specific processes |
| `k` | Kill a specific process |
| `f` | Enter the top configuration screen |
| `o` | Interactively select a new sort order in the process list |

## Using top
Click below to view a demonstration on how to use top.

[video][vid2]

## Knowledge Check
1. Which of the following can be used to view process information?

        A. top 
        B. pstree 
        C. which
        D. w

        Ans: A, B
        Explanation
        pstree and top can be used to view process information.

2. Which of the following describes things pstree can display?

        A. The relationship between parent and child processes 
        B. Recently terminated processes
        C. Repeated processes
        D. Threads in curly braces 

        Ans: A, D
        Explanation
        pstree displays the relationship between parent and child processes, and displays threads in curly braces.

3. Which of the following are displayed by top by default?

        A. PID 
        B. PR 
        C. UID
        D. USER 

        Ans: A, B, D
        Explanation
        The Process ID (PID), Priority (PR) and Process Owner (USER) are few of the items displayed by the top command.

4. What information does the second line of the top output display?

        A. user sessions
        B. stopped processes 
        C. steal time
        D. zombie processes 

        Ans: B, D
        Explanation
        The second line of the top output displays information about stopped and zombie processes.

5. Which key is used to sort the process list by top resource consumers when using top?

        A. S
        B. F
        C. K
        D. A

        Ans: D
        Explanation
        The A key is used to sort the process list by top resource consumers when using top.


# Section 4: Starting Processes in the Future
Suppose you need to perform a task on a specific day sometime in the future. However, you know you will be away from the machine on that day. How will you perform the task? You can use the `at` utility program to execute any non-interactive command at a specified time, as illustrated in the diagram:

![image][imgh]

## cron
__cron__ is a time-based scheduling utility program. It can launch routine background jobs at specific times and/or days on an on-going basis. __cron__ is driven by a configuration file called `/etc/crontab` (__cron table__), which contains the various shell commands that need to be run at the properly scheduled times. There are both system-wide crontab files and individual user-based ones. Each line of a crontab file represents a job, and is composed of a so-called __CRON expression__, followed by a shell command to execute.

The `crontab -e` command will open the crontab editor to edit existing jobs or to create new jobs. Each line of the crontab file will contain 6 fields:

| Field | Description | Values |
|-------|-------------|--------|
| MIN | Minutes | 0 to 59 |
| HOUR | Hour field | 0 to 23 |
| DOM | Day of Month | 1-31 |
| MON | Month field | 1-12 |
| DOW | Day Of Week | 0-6 (0 = Sunday) |
| CMD | Command | Any command to be executed |

Examples:

1. The entry "`* * * * * /usr/local/bin/execute/this/script.sh`" will schedule a job to execute `script.sh` every minute of every hour of every day of the month, and every month and every day in the week.

2. The entry "`30 08 10 06 * /home/sysadmin/full-backup`" will schedule a full-backup at 8.30am, 10-June, irrespective of the day of the week.

## sleep
Sometimes, a command or job must be delayed or suspended. Suppose, for example, an application has read and processed the contents of a data file and then needs to save a report on a backup system. If the backup system is currently busy or not available, the application can be made to __sleep (wait)__ until it can complete its work. Such a delay might be to mount the backup device and prepare it for writing.

`sleep` suspends execution for at least the specified period of time, which can be given as the number of seconds (the default), minutes, hours, or days. After that time has passed (or an interrupting signal has been received), execution will resume.

The syntax is:
```
sleep NUMBER[SUFFIX]...

where SUFFIX may be:
                1.   s for seconds (the default)
                2.   m for minutes
                3.   h for hours
                4.   d for days.
```
`sleep` and `at` are quite different; `sleep` delays execution for a specific period, while `at` starts execution at a later time.

![image][imgi]

## Knowledge Check
1. Which facility is used to schedule a periodically performed task?

        Explanation
        cron is used to schedule a frequently performed task.

2. The at utility is used to execute:

        A. Interactive programs at a specific time
        B. Non-interactive programs at a specific time 
        C. Interactive programs at periodic time intervals
        D. Non-interactive programs at periodic time intervals

        Ans: B
        Explanation
        The at utility is used to execute non-interactive programs at a specific time.

## Lab 3: Using at for Future Batch Processing
Schedule a very simple task to run at a future time from now. This can be as simple as running `ls` or `date` and saving the output. (You can use a time as short as one minute in the future.)

Note that the command will run in the directory from which you schedule it with at.

Do this:

+ From a short bash script.
+ Interactively.

Click [the link][lab3] to view a solution to the Lab exercise.

Solution: 
> 1. Create the file testat.sh containing:
>     ```
>     #!/bin/bash
>     date > /tmp/datestamp
>     ```
>     and then make it executable and queue it up with at:
>     ```
>     $ chmod +x testat.sh
>     $ at now + 1 minute -f testat.sh
>     ```
>     You can see if the job is queued up to run with atq:
>     $ atq
>     17	Wed Apr 22 08:55:00 2015 a student
>             
>     Make sure the job actually ran:
>     ```
>     $ cat /tmp/datestamp
>     Wed Apr 22 08:55:00 CDT 2015
>     ```        
>     What happens if you take the /tmp/datestamp out of the command? (Hint: type mail > if not prompted to do so!)
> 
> 2. Interactively it is basically the same procedure. Just queue up the job with:
>     ```
>     $ at now + 1 minute
>     at> date > /tmp/datestamp
>     CTRL-D
>     $ atq
>     ```

## Lab 4: Scheduling a Periodic Task with cron
Set up a cron job to do some simple task every day at 10 AM.

Click [the link][lab4] to view a solution to the Lab exercise.

Solution:
> Set up a cron job to do some simple task every day at 10 AM. Create a file named > `mycrontab` with the following content:
> ```
> 0 10 * * * /tmp/myjob.sh
> ```
> and then create /tmp/myjob.sh containing:
> ```
> #!/bin/bash
> echo Hello I am running $0 at $(date)
> ```
> and make it executable:
> ```
> $ chmod +x /tmp/myjob.sh
> ```
> Put it in the crontab system with:
> ```
> $ crontab mycrontab
> ```   
> and verify it was loaded with:
> ```
> $ crontab -l
>  0 10 * * * /tmp/myjob.sh
> $ sudo ls -l /var/spool/cron/student
> -rw------- 1 student student 25 Apr 22 09:59 /var/spool/cron/student
> $ sudo cat /var/spool/cron/student
> 0 10 * * * /tmp/myjob.sh
> ```
> Note you if don't really want this running every day, printing out messages like:
> Hello I am running /tmp/myjob.sh at Wed Apr 22 10:03:48 CDT 2015
>       
> and mailing them to you, you can remove it with:
> ```
> $ crontab -r
> ```
> If the machine is not up at 10 AM on a given day, anacron will run the job at a > suitable time.


# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ Processes are used to perform various tasks on the system.
+ Processes can be single-threaded or multi-threaded.
+ Processes can be of different types, such as interactive and non-interactive.
+ Every process has a __unique identifier (PID)__ to enable the operating system to keep track of it.
+ The __nice value__, or __niceness__, can be used to set priority.
+ `ps` provides information about the currently running processes.
+ You can use `top` to get constant real-time updates about overall system performance, as well as information about the processes running on the system.
+ __Load average__ indicates the amount of utilization the system is under at particular times.
+ Linux supports __background__ and __foreground__ processing for a job.
+ `at` executes any non-interactive command at a specified time.
+ `cron` is used to schedule tasks that need to be performed at regular intervals.



[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V006500_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004900_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V006900_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/219d348bf46fa4b3b8c83b3dbdf3fb31/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch16_screen03.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/49178932e74cb80a82c62db4fff8ce2a/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch16_screen05.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fbe122ffd13edf336ad978cddb953a7f/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch16_screen07.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fcc61556971b7cdefbafabf3d7abab22/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch16_screen08.jpg
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ca05a14d78d8e3bb26b519fe65047a66/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/wuptimesuse.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5ad78e82ed03efc7777fad630abed5dd/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/woutputrhel.png
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3ff2741d99789599c91efda5c5028150/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/bgfgrhel.png
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8dcff92dcec85e717944d972b96d6fcc/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/jobsrhel.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a910c16bb6f18c4d38e9ff123a6f5e02/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/ubuntupsef.png
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8cca52331523da587fab092df4bc7dba/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/psbsdrhel.png
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9eaf15c635ff33e0dbd318a36f295925/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/toprhel.png
[imgc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f70432d89645e43f5d72008706908bbc/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/toprhelline1.png
[imgd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/486c9e55bf24f2dca9f628f0a3362bcf/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/toprhelline2.png
[imge]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/49e0cb9bbb88ccb9cc6ff9c4f32bc243/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/toprhelline3.png
[imgf]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8ec74d523983230af0d3c4d4f1556dfb/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/toprhelline4-5.png
[imgg]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9eaf15c635ff33e0dbd318a36f295925/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/toprhel.png
[imgh]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/540b00f42196dd1805048b7ff9cbbdd9/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/atupdated.jpg
[imgi]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b9444a7d9db9ee97c557d2373530b24d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/sleepsuse.png

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-uptime.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-bgfg.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-at.html
[lab4]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-cron.html

