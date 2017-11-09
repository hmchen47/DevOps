Chapter 12: User Environment
============================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Use and configure user accounts and user groups.
+ Use and set environment variables.
+ Use the previous shell command history.
+ Use keyboard shortcuts.
+ Use and define aliases.
+ Use and set file permissions and ownership.


# Section 1: Accounts, Users and Groups
## Identifying the Current User
As you know, Linux is a multi-user operating system; i.e., more than one user can log on at the same time. 

+ To list the currently logged-on users, type `who`
+ To identify the current user, type `whoami`

Giving who the `-a` option will give more detailed information.

## Basics of Users and Groups
All Linux users are assigned a unique user ID (__uid__), which is just an integer; normal users start with a uid of 1000 or greater.

Linux uses __groups__ for organizing users. Groups are collections of accounts with certain shared permissions. Control of group membership is administered through the `/etc/group` file, which shows a list of groups and their members. By default, every user belongs to a default or __primary group__. When a user logs in, the group membership is set for their primary group and all the members enjoy the same level of access and privilege. Permissions on various files and directories can be modified at the group level.

Users also have one or more group IDs (__gid__), including a default one which is the same as the user ID. These numbers are associated with names through the files `/etc/passwd` and `/etc/group`. Groups are used to establish a set of users who have common interests for the purposes of access rights, privileges, and security considerations. Access rights to files (and devices) are granted on the basis of the user and the group they belong to.

For example, `/etc/passwd` might contain  `george:x:1002:1002:George Metesky:/home/george:/bin/bash` and `/etc/group` might contain `george:x:1002`.

![image][img1]

## Adding and Removing Users
Distributions have straightforward graphical interfaces for creating and removing users and groups and manipulating group membership. However, it is often useful to do it from the command line or from within shell scripts. Only the root user can add and remove users and groups.

Adding a new user is done with __useradd__ and removing an existing user is done with __userdel__. In the simplest form, an account for the new user bjmoose would be done with:
```
$ sudo useradd bjmoose
```
Note that for __openSUSE__, useradd is not in the normal user's PATH, so the command should be:

`$ sudo /usr/sbin/useradd bjmoose`

which, by default, sets the home directory to `/home/bjmoose`, populates it with some basic files (copied from `/etc/skel`) and adds a line to `/etc/passwd` such as:
```
bjmoose:x:1002:1002::/home/bjmoose:/bin/bash
```
and sets the default shell to `/bin/bash`. Removing a user account is as easy as typing `userdel bjmoose`. However, this will leave the `/home/bjmoose` directory intact. This might be useful if it is a temporary inactivation. To remove the home directory while removing the account one needs to use the `-r` option to `userdel`.

Typing __id__ with no argument gives information about the current user, as in:
```
$ id
uid=1002(bjmoose) gid=1002(bjmoose) groups=106(fuse),1002(bjmoose)
```
If given the name of another user as an argument, id will report information about that other user.

![image][img2]

## Adding and Removing Groups
Adding a new group is done with __groupadd__:
```
$ sudo /usr/sbin/groupadd anewgroup
```
The group can be removed with __groupdel__:
```
$ sudo /usr/sbin/groupdel anewgroup
```
Adding a user to an already existing group is done with __usermod__. For example, you would first look at what groups the user already belongs to:
```
$ groups rjsquirrel
bjmoose : rjsquirrel
```
and then add the new group:
```
$ sudo /usr/sbin/usermod -a -G anewgroup rjsquirrel

$ groups rjsquirrel
turkey: rjsquirrel anewgroup
```
These utilities update `/etc/group` as necessary. Make sure to use the `-a` option, for append, so as to avoid removing already existing groups. `groupmod` can be used to change group properties, such as the Group ID (gid) with the `-g` option or its name with the `-n` option.

Removing a user from the group is somewhat trickier. The `-G` option to `usermod` must give a complete list of groups. Thus, if you do:
```
$ sudo /usr/sbin/usermod -G rjsquirrel rjsquirrel

$ groups rjsquirrel
rjsquirrel : rjsquirrel
```
only the rjsquirrel group will be left.

![image][img3]

## The root Account
The __root__ account is very powerful and has full access to the system. Other operating systems often call this the __administrator__ account; in Linux, it is often called the __superuser__ account. You must be extremely cautious before granting full root access to a user; it is rarely, if ever, justified. External attacks often consist of tricks used to elevate to the root account.

However, you can use the __sudo__ feature to assign more limited privileges to user accounts:

+ Only on a temporary basis
+ Only for a specific subset of commands.

## su and sudo
When assigning elevated privileges, you can use the command `su` (switch or substitute user) to launch a new shell running as another user (you must type the password of the user you are becoming). Most often, this other user is __root__, and the new shell allows the use of elevated privileges until it is exited. It is almost always a bad (dangerous for both security and stability) practice to use su to become root. Resulting errors can include deletion of vital files from the system and security breaches.

Granting privileges using __sudo__ is less dangerous and is preferred. By default, sudo must be enabled on a per-user basis. However, some distributions (such as Ubuntu) enable it by default for at least one main user, or give this as an installation option.

In the chapter on Security that follows shortly, we will describe and compare __su__ and __sudo__ in detail.

## Elevating to root Account
To fully become root, one merely types `su` and then is prompted for the root password.

To execute just one command with root privilege type `sudo <command>`. When the command is complete, you will return to being a normal unprivileged user.

__sudo__ configuration files are stored in the `/etc/sudoers` file and in the `/etc/sudoers.d/` directory. By default, the `sudoers.d` directory is empty.

## User Startup Files
In Linux, the command shell program (generally __bash__)  uses one or more startup files to configure the user environment. Files in the `/etc` directory define global settings for all users, while initialization files in the user's __home__ directory can include and/or override the global settings.

The startup files can do anything the user would like to do in every command shell, such as:

+ Customizing the prompt
+ Defining command-line shortcuts and aliases
+ Setting the default text editor
+ Setting the path for where to find executable programs.

![image][img4]

## Order of the Startup Files
When you first login to Linux, `/etc/profile` is read and evaluated, after which the following files are searched (if they exist) in the listed order:

1. `~/.bash_profile`
2. `~/.bash_login`
3. `~/.profile`

where  `~/.` denotes the user's home directory. The Linux login shell evaluates whatever startup file that it comes across first and ignores the rest. This means that if it finds `~/.bash_profile`, it ignores `~/.bash_login` and `~/.profile`. Different distributions may use different startup files.

However, every time you create a new shell, or terminal window, etc., you do not perform a full system login; only a file named `~/.bashrc` file is read and evaluated. Although this file is not read and evaluated along with the login shell, most distributions and/or users include the `~/.bashrc` file from within one of the three user-owned startup files. For __Ubuntu, openSUSE__, and __CentOS__ , the user must make appropriate changes in `~/.bash_profile` to have it include  `~/.bashrc`.

The `.bash_profile` will have certain extra lines, which in turn will collect the required customization parameters from `.bashrc`.

Most commonly, users only fiddle with  `~/.bashrc`, as it is invoked every time a new command line shell initiates, or another program is launched from a terminal window, while the other files are read and executed only when the user first logs onto the system.

## Creating Aliases
You can create customized commands or modify the behavior of already existing ones by creating __aliases__. Most often, these aliases are placed in your `~/.bashrc` file so they are available to any command shells you create. __unalias__ removes an alias.

Typing `alias` with no arguments will list currently defined aliases.

Please note there should not be any spaces on either side of the equal sign and the alias definition needs to be placed within either single or double quotes if it contains any spaces.

![image][img5]

## Try-It-Yourself: Identify the Currently Logged-In User and User
To practice, click the link provided below.

[Identify the Currently Logged-In Users and Current User][login]

## Knowledge Check
1. Which of the following statements are true?

        A. su is safer to use than sudo.
        B. sudo is safer to use than su. 
        C. Normal userids have values of 1000 or greater. 
        D. Normal userids have valudes of 499 or less.


        Ans: B, C
        Explanation
        su is safer to use than sudo.
        Normal userids have values of 1000 or greater.

2. What are the advantages of startup files?

        A. They help the users change to the root account.
        B. They can set command-line shortcuts and aliases. 
        C. They can provide full access to the system.
        D. They can set the default text editor. 

        Ans: B, D
        Explanation
        The advantages of startup files are that they can set the command-line shortcuts and aliases and can set the default text editor.

3. Which command is used to create an alias, cdtmp, for cd /tmp?

        Explanation
        The alias cdtmp='cd /tmp' command is used to create an alias cdtmp for the cd /tmp command.

## Lab 1: Deploying aliases
Typing long commands and filenames over and over gain gets rather tedious, and leads to a lot of trivial errors, such as typos.

Deploying aliases allows us to define shortcuts to alleviate the pain of all of this typing.

Suppose you are a member of a project team that works in a common, shared directory for your project. This directory is located in `/home/staff/RandD/projects/projectX/src`.

When you are working on Project X, you often need to create and modify your files in this directory. It does not take too long before typing in:
```
cd /home/staff/RandD/projects/projectX/src
```
gets tedious.

Define and use an alias named projx to do the above cd command for you.

Click [the link][lab1] to view a solution to the Lab exercise.


# Section 2: Environment Variables
__Environment variables__ are quantities that have specific values which may be utilized by the command shell, such as __bash__, or other utilities and applications. Some environment variables are given preset values by the system (which can usually be overriden), while others are set directly by the user, either at the command line or within startup and other scripts. 

An environment variable is actually just a character string that contains information used by one or more applications. There are a number of ways to view the values of currently set environment variables; one can type `set`, `env`, or `export`. Depending on the state of your system, `set` may print out many more lines than the other two methods.
```bash
$ set
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:expand_aliases:extglob:extquote:force_fignore:histappend:
   interactive_comments:progcomp:promptvars:sourcepath
BASH_VERSION='4.2.46(1)-release'
BASH_ALIASES=()
...

$ env
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
GPG_AGENT_INFO=/run/user/1000/keyring/gpg:0:1
TERM=xterm-256color
SHELL=/bin/bash
...

$ export
.....
declare -x COLORTERM=gnome-terminaldeclare -x COLUMNS="85"
declare -x CSCOPE_EDITOR="/usr/local/bin/cscope_emacs"
declare -x CVS_RSH="ssh"
...
```
[image a][img6]

[image b][img7]

[image c][img8]


## Setting Environment Variables
By default, variables created within a script are only available to the current shell; child processes (sub-shells) will not have access to values that have been set or modified. Allowing __child processes__ to see the values requires use of the `export` command.

| Task | Command |
|------|---------|
| Show the value of a specific variable | `echo $SHELL` |
| Export a new variable value | `export VARIABLE=value` (or `VARIABLE=value; export VARIABLE`) |
| Add a variable permanently | 1. `Edit ~/.bashrc and add the line export VARIABLE=value` |
|   | 2. `Type source ~/.bashrc` or just `. ~/.bashrc` (dot `~/.bashrc`); or just start a new shell by typing  `bash` |

## The HOME Variable
`HOME` is an environment variable that represents the home (or login) directory of the user. __cd__ without arguments will change the current working directory to the value of `HOME`. Note the tilde character (`~`) is often used as an abbreviation for `$HOME`. Thus, `cd $HOME` and `cd ~` are completely equivalent statements.

Show the value of the HOME environment variable, then change directory (cd) to /bin
```
$ echo $HOME
/home/me
$ cd /bin
```
Where are we? Use print (or present) working directory (pwd) to find out. As expected, /bin
```
$ pwd
/bin
```
Change directory without an argument . . .
```
$ cd
```
. . . takes us back to HOME as you can now see
```
$ pwd
/home/me
```

## The PATH Variable
`PATH` is an ordered list of directories (the path) which is scanned when a command is given to find the appropriate program or script to run. Each directory in the path is separated by colons (__`:`__). A null (empty) directory name (or `./`) indicates the current directory at any given time.

+ `:path1:path2`
+ `path1::path2`

In the example `:path1:path2`, there is a null directory before the first colon (`:`). Similarly, for `path1::path2` there is a null directory between `path1` and `path2`.

To prefix a private bin directory to your path:
```
$ export PATH=$HOME/bin:$PATH
$ echo $PATH
/home/me/bin:/usr/local/bin:/usr/bin:/bin/usr
```
## The PS1 Variable and the Command Line Prompt
__Prompt Statement (PS)__ is used to customize your prompt string in your terminal windows to display the information you want. 

`PS1` is the primary prompt variable which controls what your command line prompt looks like. The following special characters can be included in `PS1`:

+ `\u` - User name
+ `\h` - Host name
+ `\w` - Current working directory
+ `\!` - History number of this command
+ `\d` - Date

They must be surrounded in single quotes when they are used, as in the following example:
```bash
$ echo $PS1
$
$ export PS1='\u@\h:\w$ '
me@example.com:~$ # new prompt
me@example.com:~$
```
To revert the changes:
```bash
me@example.com:~$ export PS1='$ '
$
```
An even better practice would be to save the old prompt first and then restore, as in:

`$ OLD_PS1=$PS1`

change the prompt, and eventually change it back with:
```bash
$ PS1=$OLD_PS1
$
```

## The SHELL Variable
The environment variable `SHELL` points to the user's default command shell (the program that is handling whatever you type in a command window, usually __bash__) and contains the full pathname to the shell:
```bash
$ echo $SHELL
/bin/bash
$
```

[image][img9]


## Knowledge Check
1. Which of the following is a commonly used environment variable?

        A. HOMEDIR
        B. SECRET_PASSWORD
        C. GROUP
        D. HOME 

        Ans: D
        Explanation
        HOME is a commonly used environment variable.

2. Which of the following environment variables is used to specify the prompt string?

        A. EXPORT
        B. PS1correct
        C. ENV
        D. SHELL

        Explanation
        The environment variable PS1 is used to specify the prompt string.

3. Which of the following will set your bash prompt to include the current working directory?

        A. export PS1='\w$ '
        B. export PS1='\u@\h:\d$ '
        C. export PS1='$ '
        D. echo $PS1

        Ans: A
        Explanation
        Typing export PS1='\w$' will set your bash prompt to include the current working directory.

## Lab 2: Adding /tmp to Your Path
Create a small file, `/tmp/ls` , which contains just the line:

`echo HELLO, this is the phony ls program.`

Then, make it executable by doing:

`$ chmod +x /tmp/ls`

1. Append `/tmp` to your path, so it is searched only after your usual path is considered. Type `ls` and see which program is run: `/bin/ls` or `/tmp/ls?`
2. Pre-pend `/tmp` to your path, so it is searched before your usual path is considered. Once again, type ls and see which program is run: `/bin/ls` or `/tmp/ls?`
What are the security considerations in altering the path this way?

Click [the link][lab2] to view a solution to the Lab exercise.

## Lab 3: Changing the Command Line Prompt
It is nice to have your current working directory as part of your prompt so that a quick glance will give you some information without typing pwd every time.

If you often work on multiple computers, especially if you network from one into another with `ssh`, it is very convenient to have the computer name be part of your prompt.

+ Put your current working directory in your command line prompt.
+ Put your computer (machine) name in your prompt.
+ Put both your current directory and computer name in your prompt.

How can you make this persistent, so that whenever you start a __bash__ command shell, this is your prompt? 

Click [the link][lab3] to view a solution to the Lab exercise.


# Section 3: Recalling Previous Commands
bash keeps track of previously entered commands and statements in a __history__ buffer; you can recall previously used commands simply by using the __Up__ and __Down__ cursor keys. To view the list of previously executed commands, you can just type `history` at the command line.

The list of commands is displayed with the most recent command appearing last in the list. This information is stored in `~/.bash_history`.

## Using History Environment Variables
Several associated environment variables can be used to get information about the history file. 

+ `HISTFILE`: The location of the history file. 
+ `HISTFILESIZE`: The maximum number of lines in the history file (default 500). 
+ `HISTSIZE`: The maximum number of commands in the history file. 
+ `HISTCONTROL`: How commands are stored. 
+ `HISTIGNORE`: Which command lines can be unsaved.

For a complete description of the use of these environment variables, see `man bash`.

## Finding and Using Previous Commands
Specific keys to perform various tasks:

| Key | Usage |
|-----|-------|
| `Up/Down arrow keys` | Browse through the list of commands previously executed |
| `!!` (Pronounced as bang-bang) | Execute the previous command |
| `CTRL-R` | Search previously used commands |

If you want to recall a command in the history list, but do not want to press the arrow key repeatedly, you can press __CTRL-R__ to do a reverse intelligent search.

As you start typing, the search goes back in reverse order to the first command that matches the letters you have typed. By typing more successive letters, you make the match more and more specific.

The following is an example of how you can use the `CTRL-R` command to search through the command history:
```
$ ^R                                # This all happens on 1 line
(reverse-i-search)'s': sleep 1000   # Searched for 's'; matched "sleep"
$ sleep 1000                        # Pressed Enter to execute the searched command.
$
```

## Executing Previous Commands
The table describes the syntax used to execute previously used commands:

| Syntax | Task |
|--------|------|
| `!` | Sart a history substitution |
| `!$` | efer to the last argument in a line |
| `!n` | efer to the nth command line |
| `!strin` | Refer to the most recent command starting with string |

All history substitutions start with !. In the line `$ ls -l /bin /etc /var !$` refers to `/var`, which is the last argument in the line.

Here are more examples:

`$ history`

1. `echo $SHELL`
2. `echo $HOME`
3. `echo $PS1`
4. `ls -a`
5. `ls -l /etc/ passwd`
6. `sleep 1000`
7. `history`
```
$ !1                # Execute command #1 above
echo $SHELL
/bin/bash
$ !sl               # Execute the command beginning with "sl"
sleep 1000
$
```

## Keyboard Shortcuts
You can use keyboard shortcuts to perform different tasks quickly. The table lists some of these keyboard shortcuts and their uses.

| Keyboard Shortcut | Task |
| `CTRL-L` | Clears the screen |
| `CTRL-D` | Exits the current shell |
| `CTRL-Z` | Puts the current process into suspended background |
| `CTRL-C` | Kills the current process |
| `CTRL-H` | Works the same as backspace |
| `CTRL-A` | Goes to the beginning of the line |
| `CTRL-W` | Deletes the word before the cursor |
| `CTRL-U` | Deletes from beginning of line to cursor position |
| `CTRL-E` | Goes to the end of the line |
| `Tab`    | Auto-completes files, directories, and binaries |

## Knowledge Check
1. How would you find the name of a previously used command and easily rerun that command without having to type it at the prompt?

        A. Press the Down arrow key until you locate the command, and then press Enter to rerun the command.
        B. Press the Up arrow key until you locate the command, and then press Enter to rerun the command. 
        C. Use the history command to locate the command, and then press Enter to rerun the command.
        D. Press the Right arrow key until you locate the command, and then press Enter to rerun the command.

        Ans: B
        Explanation
        Keep pressing the Up arrow key until you locate the command, and then press Enter to rerun the command.

2. How would you run command 70 from your previous history in one step?

        Explanation
        Type !70.

3. Where does the shell store the command history?

        A. bash
        B. ~/.bash_history 
        C. /bin/bash
        D. /bin /etc /var

        Ans: B
        Explanation
        The shell stores history in the ~/.bash_history file.

## Lab 4: Command History
You have been busy working with your Linux workstation long enough to have typed in about 100 commands in one particular bash command shell.

At some point earlier, you used a new command, but the exact name has slipped your mind.

Or perhaps it was a pretty complicated command, with a bunch of options and arguments, and you do not want to go through the error prone process of figuring out what to type again.

How do you ascertain what the command was?

Once you find the command in your history, how do you easily issue the command again without having to type it all in at the prompt?

Click [the link][lab4] to view a solution to the Lab exercise.


# Section 4: File Permissions
## File Ownership
In Linux and other UNIX-based operating systems, every file is associated with a user who is the __owner__. Every file is also associated with a __group__ (a subset of all users) which has an interest in the file and certain rights, or permissions: read, write, and execute.

The following utility programs involve user and group ownership and permission setting: 

| Command | Usage |
|---------|-------|
| `chown` | Used to change user ownership of a file or directory |
| `chgrp` | Used to change group ownership |
| `chmod` | Used to change the permissions on the file, which can be done separately for __owner__, __group__ and the rest of the world (often named as __other__.) |

## File Permission Modes and chmod
Files have three kinds of permissions: read (__r__), write (__w__), execute (__x__). These are generally represented as in `rwx`. These permissions affect three groups of owners: user/owner (__u__), group (__g__), and others (__o__).

As a result, you have the following three groups of three permissions:
```
rwx: rwx: rwx
 u:   g:   o
```
There are a number of different ways to use __chmod__. For instance, to give the owner and others execute permission and remove the group write permission:
```bash
$ ls -l somefile
-rw-rw-r-- 1 coop coop 1601 Mar 9 15:04 somefile
$ chmod uo+x,g-w somefile
$ ls -l somefile
-rwxr--r-x 1 coop coop 1601 Mar 9 15:04 somefile
```
where `u` stands for user (owner), `o` stands for other (world), and `g` stands for group.

This kind of syntax can be difficult to type and remember, so one often uses a shorthand which lets you set all the permissions in one step. This is done with a simple algorithm, and a single digit suffices to specify all three permission bits for each entity. This digit is the sum of:

+ 4 if read permission is desired.
+ 2 if write permission is desired.
+ 1 if execute permission is desired.

Thus, `7` means `read/write/execute`, `6` means `read/write`, and `5` means `read/execute`.

When you apply this to the `chmod` command, you have to give three digits for each degree of freedom, such as in
```bash
$ chmod 755 somefile
$ ls -l somefile
-rwxr-xr-x 1 coop coop 1601 Mar 9 15:04 somefile
```

## Example of chown
Let's see an example of changing file ownership using chown, as shown in the screenshot to the right. First, we create two empty files using `touch`.

Notice it requires `sudo` to change the owner of `file2` to root.  The second `chown` command changes both owner and group at the same time!

Finally, only the superuser can remove the files. 

![image][imga]

## Example of chgrp
Now, let’s see an example of changing the group ownership using chgrp:

![image][imgb]

## Try-It-Yourself: Using chmod to Change File Permissions
To practice, click the link provided below.

[Using chmod to Change File Permissions][chfp]

## Knowledge Check
Which of the following permissions provides read and execute access?

    A. rwx
    B. r--
    C. rw-
    D. r-x 

    Ans: D
    Explanation
    The r-x permission provides read and execute access.


# Summary
You have completed this chapter. Let's summarize the key concepts covered:

+ Linux is a multi-user system.
+ To find the currently logged on users, you can use the `who` command.
+ To find the current user ID, you can use the `whoami` command.
+ The root account has full access to the system. It is never sensible to grant full root access to a user.
+ You can assign root privileges to regular user accounts on a temporary basis using the `sudo` command.
+ The __shell program (bash)__ uses multiple startup files to create the user environment. Each file affects the interactive environment in a different way. `/etc/profile` provides the global settings.
+ Advantages of startup files include that they customize the user's prompt, set the user's terminal type, set the command-line shortcuts and aliases, and set the default text editor, etc.
+ An environment variable is a character string that contains data used by one or more applications. The built-in shell variables can be customized to suit your requirements.
+ The `history` command recalls a list of previous commands, which can be edited and recycled.
+ In Linux, various keyboard shortcuts can be used at the command prompt instead of long actual commands.
+ You can customize commands by creating aliases. Adding an `alias` to `˜/.bashrc` will make it available for other shells.
+ File permissions can be changed by typing `chmod permissions filename`.
+ File ownership is changed by typing chown `owner filename`.
+ File group ownership is changed by typing `chgrp group filename`.


[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005200_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/03549a0189644137de64f426a69442c3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/etc_group_passwd.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1387735f26c0ae0b377390c4c9dd9e7a/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/useradd.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/388d78b23f2b6d93f8f39cbecf6194b1/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/newgroupsuse.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a61fd2656f3894d6f93397e755157b4b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch09_screen07.jpg
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/97491d062822787b87a74f33ea868847/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/aliassuse.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e856c871b455c209960ee4fbb39fcb39/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch09_screen13a.jpg
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e856c871b455c209960ee4fbb39fcb39/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch09_screen13b.jpg
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e856c871b455c209960ee4fbb39fcb39/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch09_screen13c.jpg
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6463fc485d188c592c952f3761eeb486/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch09_screen19.jpg
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d99d45386528584f3f861f182577fb1a/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/chownrhel7.png
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/2416814b8977e0048d01804a8319aace/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/chgrouprhel7.png

[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-path.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-prompt.html
[lab4]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-history.html

[login]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingwho/index.html
[chfp]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingchmod/index.html