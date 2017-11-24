Chapter 08: Finding Linux Documentation
======================================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Use different sources of documentation.
+ Use the __man__ pages.
+ Access the GNU __info__ system.
+ Use the __help__ command and `--help` option.
+ Use other documentation sources.


# Section 1: Documentation Sources
## Introduction to Linux Documentation Sources
Whether you are an inexperienced user or a veteran, you will not always know (or remember) the proper use of various Linux programs and utilities: what is the command to type, what options does it take, etc. You will need to consult help documentation regularly. Because Linux-based systems draw from a large variety of sources, there are numerous reservoirs of documentation and ways of getting help. Distributors consolidate this material and present it in a comprehensive and easy-to-use manner.

Important Linux documentation sources include:

+ The __man__ pages (short for manual pages)
+ GNU __Info__
+ The `help` command and `--help` option

Other Documentation Sources, e.g. https://www.gentoo.org/doc/en/ or https://help.ubuntu.com/community/CommunityHelpWiki

## Knowledge Check
Which of the following are sources of Linux documentation? 
(Select the answer that matches.)

    A. MSDN network
    B. The man pages 
    C. https://www.gentoo.org/doc/en/ 
    D. The Congressional Record

    Ans: B, C
    Explanation
    Sources of Linux documentation include the man pages and https://www.gentoo.org/doc/en/


# Section 2: The man pages
The __man pages__ are the most often-used source of Linux documentation. They provide in-depth documentation about many programs and utilities, as well as other topics, including configuration files, system calls, library routines, and the kernel. They are present on all Linux distributions and are always at your fingertips.  (__man__ is actually an abbreviation for __manual__.)

Typing `man` with a topic name as an argument retrieves the information stored in the topic's __man pages__. Some Linux distributions require every installed program to have a corresponding __man__ page, which explains the depth of coverage. The __man__ pages infrastructure was first introduced in the early UNIX versions of the early 1970s.

__man__ pages are often converted to:

+ Web pages (See http://man7.org/linux/man-pages/ )
+ Published books
+ Graphical help
+ Other formats.

## man
The `man` program searches, formats, and displays the information contained in the man pages. Because many topics have a lot of information, output is piped through a  pager program such as `less` to be viewed one page at a time; at the same time, the information is formatted for a good visual display.

When no options are given, by default one sees only the dedicated page specifically about the topic. You can broaden this to view all pages containing a string in their name by using the `-f` option. You can also view all pages that discuss a specified subject (even if the specified subject is not present in the name) by using the `–k` option.

`man –f` generates the same result as typing `whatis`.

`man –k` generates the same result as typing `apropos`.

## Manual Chapters
The __man pages__ are divided into nine numbered chapters (1 through 9). Sometimes, a letter is appended to the chapter number to identify a specific topic. For example, many pages describing part of the __X Window__ API are in chapter 3X.

The chapter number can be used to force __man__ to display the page from a particular chapter; it is common to have multiple pages across multiple chapters with the same name, especially for names of library functions or system calls.

With the `-a` parameter, __man__ will display all pages with the given name in all chapters, one after the other.
```
$ man 3 printf 
$ man -a printf
```

![image][img1]

## Knowledge Check
1. What is displayed when running man with no options other than the topic as an argument?

        A. All man pages in sequence with the given name in all chapters
        B. The manual page for the given topic correct
        C. The man pages with a word in the name
        D. The man pages discussing the subject

        Ans: B
        Explanation
        With no options, man displays the manual page for the given topic.

2. What does the man –k command display?

        A. All man pages in sequence with the given name in all chapters
        B. The man pages with a word in the name
        C. The manual page for the given topic
        D. A list of the man pages discussing the subject 

        Ans: D
        Explanation
        The man –k command displays a list of the man pages discussing the subject.

3. What does the man –a command display?

        A. All man pages in sequence with the given name in all chapters 
        B. The man pages with a word in the name
        C. The manual page for the given topic
        D. The man pages discussing the subject

        Ans: A
        Explanation
        The man –a command displays all man pages in sequence with the given name in all chapters.

## Lab 1: Working with man
1. Finding man pages
    
    From the command line, bring up the man page for man itself. Scroll down to the EXAMPLES section.

2. Finding man Pages by Topic

    What man pages are available that document file compression?

3. man Pages by Section

    From the command line, bring up the man page for the printf library function. In which manual page section are library functions found?

Click [the link][lab1] to view a solution to the Lab exercise.

# Section 3: GNU Info
The next source of Linux documentation is the __GNU Info System__.

This is the __GNU__ project's standard documentation format (__info__) which it prefers as an alternative to __man__. The __info__ system is more free-form and supports linked subsections.

Functionally, the __GNU Info System__ resembles man in many ways. However, topics are connected using links (even though its design predates the World Wide Web). Information can be viewed through either a command line interface, a graphical help utility, printed or viewed online.

## Command Line Info Browser
Typing `info` with no arguments in a terminal window displays an index of available topics. You can browse through the topic list using the regular movement keys: `arrows`, `Page Up`, and `Page Down`.

You can view help for a particular topic by typing `info <topic name>`. The  system then searches for the topic in all available info files.

Some useful keys are: `q` to quit, `h` for help, and `Enter` to select a menu item.

![image][img2]

## info Page Structure
The topic which you view in the __info__ page is called a __node__.

Nodes are similar to sections and subsections in written documentation. You can move between nodes or view each node sequentially. Each node may contain __menus__ and linked subtopics, or __items__.

Items can be compared to Internet hyperlinks. They are identified by an asterisk (*) at the beginning of the item name. Named items (outside a menu) are identified with double-colons (::) at the end of the item name. Items can refer to other nodes within the file or to other files. The table lists the basic keystrokes for moving between nodes.

| Key | Function |
|-----|----------|
| `n` | Go to the next node |
| `p` | Go to the previous node |
| `u` | Move one node up in the index |

## Knowledge Check
1. What does info <topic> show?

        A. Shows the list of all pages involving the topic
        B. Requests you type in information about the topic
        C. Shows the info page for the specified topic 
        D. Searches the internet for information on the topic

        Ans: C
        Explanation
        <topic> shows the info page for the specified topic.

2. What does the info command (with no arguments) show?

        A. Shows the index of topics 
        B. Searches the Internet for information
        C. Shows the info page for the currently running Linux kernel
        D. Prints out every info page

        Ans: A
        Explanation
        The info command (with no arguments) shows the index of topics.

3. What are the topics in info pages called?

        A. Items
        B. Nodes 
        C. Sections
        D. Menus

        Ans: B
        Explanation
        The topics in info pages are called nodes.

## Lab 2: Working with info
From the command line, bring up the info page for cpio. Bring up the tutorial.

Click [the link][lab2] to view a solution to the Lab exercise.


# Section 4: The --help Option and Help Command
## Introduction to the --help Option
Another important source of Linux documentation is use of the `--help` option.

Most commands have an available short description which can be viewed using the `--help` or the `-h` option along with the command or application. For example, to learn more about the man command, you can run the following command: 

`$ man --help`

The `--help` option is useful as a quick reference and it displays information faster than the __man__ or __info__ pages.

![image][img3]

## The help Command
Some popular commands (such as `echo`), when run in a __bash__ command shell, silently run their own built-in versions of system programs or utilities, because it is more efficient to do so. (We will discuss command shells in great detail later.) To view a synopsis of these built-in commands, you can simply type help.

For these built-in commands, __help__ performs the same basic function as the `-h` and `--help` arguments (which we will discuss shortly) perform for stand-alone programs.

The next screen covers a demonstration on how to use man, info, and the help option.

![image][img4]

## Using man, info, and the help Option
Click below to view the demonstration on how to use man, info and the help option.

[video][vid1]

## Knowledge Check
1. Which of the following are the built-in help options that can be used for quick references?

        A. -h 
        B. --help 
        C. /help
        D. help --

        Ans: A, B
        Explanation
        The -h and –-help are the built-in help commands which can be used for quick references.

2. Which command displays a short synopsis of built-in shell commands?

        Explanation
        The help command displays a short synopsis of built-in shell commands.

## Lab 3: Working with Command Line help
List the available options for the mkdir command, in more than one way.

Click [the link][lab3] to view a solution to the Lab exercise.

# Section 5: Other Documentation Sources
In addition to the man pages, the GNU Info System, and the help command, there are other sources of Linux documentation, some examples of which are shown here.

![image][img5]

## Desktop Help Systems
All Linux desktop systems have a graphical help application. This application is usually displayed as a question-mark icon or an image of a ship’s life-preserver. These programs usually contain custom help for the desktop itself and some of its applications, and will often also include graphically rendered __info__ and __man__ pages.

You can also start the graphical help system from a graphical terminal using the following commands:

+ GNOME: `gnome-help` or `yelp`
+ KDE: `khelpcenter`

![image][img6]

## Package Documentation
Linux documentation is also available as part of the package management system. Usually, this documentation is directly pulled from the upstream source code, but it can also contain information about how the distribution packaged and set up the software.

Such information is placed under the `/usr/share/doc` directory in a subdirectory named after the package, perhaps including the version number in the name.

![image][img7]

## Online Resources
There are many places to access online Linux documentation, and a little bit of searching will get you buried in it. The following site has been well reviewed by other users of this course and offers a free, downloadable command line compendium under a Creative Commons license:

+ LinuxCommand.org: http://linuxcommand.org/tlcl.php

You can also find very helpful documentation for each distribution. Each distribution has its own user-generated forums and wiki sections. Here are just a few links to such sources:

+ Ubuntu: https://help.ubuntu.com/
+ CentOS: https://www.centos.org/docs/
+ OpenSUSE: http://en.opensuse.org/Portal:Documentation
+ GENTOO: http://www.gentoo.org/doc/en

Moreover, you can use online search sites to locate helpful resources from all over the Internet, including blog posts, forum and mailing list posts, news articles, and so on.

## Knowledge Check
1. Which of the following types of documentation can be accessed through /usr/share/doc?

        A. man pages
        B. Package Documentation 
        C. info pages
        D. Internet resources

        Ans: B
        Explanation
        Software package documentation can be accessed through /usr/share/doc.

2. Which of the following commands might be used to start the GNOME graphical help system?

        A. gnome-help 
        B. gnome-info
        C. yelp correct
        D. pleasehelpme

        Ans: A
        Explanation
        You can use gnome-help and/or yelp depending on your exact choice of Linux distribution.

## Lab 4: Working with Graphical Help Systems
Find the graphical help system on your desktop, and try to locate within it the man pages for `printf`. This may be difficult, so do not waste too much time before looking at the suggestions below. 

If you have been unable to find the man pages this way, we can not give a unique solution to this; it varies from one Linux distribution to another, and one version to the next, but you should be able to hunt and find out where this is located and get familiar with the interface.

In earlier Linux distributions this was a rather easy task. Those days are gone for some desktops today.

If you are having trouble finding this on recent GNOME desktops, you are not alone. For some reason, clicking on Documentation->Help only brings up documentation about GNOME itself, using the yelp browser.

However, if at the command line you type something like

student:/tmp> `yelp man:cat`

it will indeed bring up the man page for cat. However, you can not type something like man:ls in the location bar and have it work, unless you hit `CTRL-l` first! Whether this is a bug or a feature is not exactly clear, but it being a bug seems more likely. Once you are in the page, clicking on links to get other man pages works just fine.

The same mechanism works to get __info__ pages as well.


# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ The main sources of Linux documentation are the __man pages__, __GNU Info__, the __help__ options and command, and a rich variety of online documentation sources. 
+ The `man` utility searches, formats, and displays __man pages__.
+ The __man pages__ provide in-depth documentation about programs and other topics about the system, including configuration files, system calls, library routines, and the kernel.
+ The __GNU Info__ System was created by the __GNU__ project as its standard documentation. It is robust and is accessible via command line, web, and graphical tools using `info`.
+ Short descriptions for commands are usually displayed with the `-h` or `--help` argument.
+ You can type `help` at the command line to display a synopsis of built-in commands.
+ There are many other help resources both on your system and on the Internet.



[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003300_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004700_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/645da92bedb356a690fc07bd87813b46/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch07_screen07.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d7c774dd6b4b262495a16a57aed417a5/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/infoubuntu.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f9d86b387589f5e13d24cc7e88272e61/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/manhelp.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/79040611925a7890d2337fb896445e08/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/helpbash.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d4be6c97491354162222dd6068f4ba04/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch07_screen23.jpg
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/288c9d4693bd83b71d9dc91fec893900/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch07_screen24.jpg
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/dcab137a19a95616557b1c49f0754419/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/usrsharedoc.png

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-man.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-info.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-cmdhelp.html

