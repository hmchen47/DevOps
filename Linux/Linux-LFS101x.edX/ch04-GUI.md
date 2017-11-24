Chapter 04: Graphical Interface
===============================

# Introduction / Learning Objectives
[video][vid1]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Manage graphical interface sessions.
+ Perform basic operations using the graphical interface.
+ Change the graphical desktop to suit your needs.
 
# Section 1: Graphical Desktop
## Introduction
You can use either a Command Line Interface (__CLI__) or a Graphical User Interface (__GUI__) when using Linux. To work at the CLI, you have to remember which programs and commands are used to perform tasks, and how to quickly and accurately obtain more information about their use and options. On the other hand, using the GUI is often quick and easy. It allows you to interact with your system through graphical icons and screens. For repetitive tasks, the CLI is often more efficient, while the GUI is easier to navigate if you do not remember all the details or do something only rarely.

We will learn how to manage sessions using the GUI for the three Linux distribution families that we explicitly cover in this course: __CentOS__ (__Fedora__ family), __openSUSE__ (__SUSE__ family) and __Ubuntu__ (__Debian__ family). Since we are using the __GNOME__-based variant of __openSUSE__  rather than the __KDE__-based one, all are actually quite similar. If you are using __KDE__ (or other Linux desktops such as __XFCE__), your experience will vary somewhat from what is shown, but not in any intrinsically difficult way, as user interfaces have converged to certain well-known behaviors on modern operating systems. In subsequent sections of this course we will concentrate in great detail on the command line interface.

![image][img1]

## X Window System
Generally, in a Linux desktop system, the __X Window System__ is loaded as the final step in the boot process.

A service called the __display manager__ keeps track of the displays being provided, and loads the __X server__ (so-called because it provides graphical services to applications, sometimes called __X clients__). The display manager also handles graphical logins, and starts the appropriate desktop environment after a user logs in.

__X__ is a rather old system; it dates back to the mid 1980s and, as such, has certain deficiencies on modern systems (with security for example), as it has been stretched rather far from its original purposes. A newer system, known as __Wayland__ (see https://wayland.freedesktop.org/), is expected to gradually supersede it and was adopted as the default display system in __Fedora 25__.

![image][img2]

A __desktop environment__ consists of a `session manager`, which starts and maintains the components of the graphical session, and the `window manager`, which controls the placement and movement of windows, window title-bars, and controls.

Although these can be mixed, generally a `set of utilities`, session manager, and window manager are used together as a unit, and together provide a seamless desktop environment.

If the display manager is not started by default in the default runlevel, you can start __X__ a different way, after logging on to a text-mode console, by running `startx` from the command line. Or, you can start the display manager (`gdm`, `lightdm`, `kdm`, `xdm` etc.) manually from the command line. This differs from running `startx` as the display managers will project a sign in screen. We discuss them next.

![image][img3]

## GUI Startup
When you install a desktop environment, the __X__ display manager starts at the end of the boot process. This __X__ display manager is responsible for starting the graphics system, logging in the user, and starting the user’s desktop environment. You can often select from a choice of desktop environments when logging in to the system.

The default display manager for __GNOME__ is called `gdm`. Other popular display managers include __lightdm__ (used on __Ubuntu__) and __kdm__ (associated with __KDE__).

## GNOME Desktop Environment
__GNOME__ is a popular desktop environment with an easy to use graphical user interface. It is bundled as the default desktop environment for many distributions, including __Red Hat Enterprise Linux, Fedora, CentOS, SUSE Linux Enterprise__, and __Debian__. __GNOME__ has menu-based navigation and is sometimes an easy transition for at least some __Windows__ users. However, as you will see, the look and feel can be quite different across distributions, even if they are all using __GNOME__.

Another common desktop environment very important in the history of Linux and also widely used is __KDE__, which has often been used in conjunction with __SUSE__ and __openSUSE__. Other alternatives for a desktop environment include __Unity__ (from __Ubuntu__, based on __GNOME__), __XFCE__, and __LXDE__. As previously mentioned, most desktop environments follow a similar structure to __GNOME__, and we will restrict ourselves mostly to it to keep things less complex.

## Graphical Desktop Background
Each Linux distribution comes with its own set of desktop backgrounds. You can change the default by choosing a new wallpaper or selecting a custom picture to be set as the desktop background. If you do not want to use an image as the background, you can select a color to be displayed on the desktop instead.

In addition, you can also change the desktop theme, which changes the look and feel of the Linux system. The theme also defines the appearance of application windows.

We will learn how to change the desktop background and theme.

## Customizing the Desktop Background
If you do not like any of the installed wallpapers, you can use different shades of color as the background using the __Colors and Gradients__ drop-down in the __Appearance__ window.

In the __Ubuntu__ screenshot shown, you can get here by either right clicking on the desktop, or by selecting __System Settings->Appearance__.  For other recent Linux distributions, you can vary the background by selecting __System Settings->Background__.

There are three types of color: solid, horizontal gradient, and vertical gradient. Click the box at the bottom and pick the effect between solid and the two gradients. In addition, you can also install packages that contain wallpapers by searching for packages using “wallpaper” as a keyword.

Note: The next few screens cover the demonstrations and Try-It-Yourself activities of a member of each of the three Linux distribution families we cover in this course. You can view a demonstration for the distribution type of your choice and practice the procedure through the relevant Try-It-Yourself activity.

![image][img4]

## Changing the Desktop Background in CentOS
Click below to view a demonstration on how to change the background in CentOS. (The exact details may vary very slightly depending on your distribution version.)

[video][vid2]

## Changing the Desktop Background in openSUSE
Click below to view a demonstration on how to change the desktop background in openSUSE. (The exact details may vary very slightly depending on your distribution version.)

[video][vid3]

## Changing the Desktop Background in Ubuntu
Click below to view a demonstration on how to change the desktop background in Ubuntu. (The exact details may vary very slightly depending on your distribution version.)

[video][vid4]

## Try-It-Yourself: Changing the Desktop Background
To practice changing the desktop background in your chosen distribution, click the relevant link below. (The exact details may vary very slightly depending on your distribution version.)

+ [Changing the Desktop Background in CentOS][centosdb]
+ [Changing the Desktop Background in openSUSE][susedb]
+ [Changing the Desktop Background in Ubuntu][ubuntudb]

## gnome-tweak-tool
Most settings, both personal and system-wide, are to be found by clicking in the upper right hand corner, on either a gear or other obvious icon, depending on your Linux distribution.

However, there are many settings which many users would like to modify which are not accessible; the default settings utility is unfortunately rather limited in modern __GNOME__-based distributions. The desire for simplicity has actually made it difficult to adapt your system to your tastes and needs.

Fortunately, there is a standard utility, __gnome-tweak-tool__, which exposes many more setting options. It also permits you to easily install __extensions__ by external parties. Not all Linux distributions install this tool by default, but it is always available. You may have to run it by hitting __Alt-F2__ and then typing in the name. You may want to add it to your Favorites list as we shall discuss.

In the screenshot below, the keyboard mapping is being adjusted so the useless __CapsLock__ key can be used as an additional __Ctrl__ key; this saves users who use __Ctrl__ a lot (such as __emacs__ aficionados) from getting physically damaged by pinkie strain.

![image][img5]

## Changing the Theme
__The visual appearance of applications__ (the buttons, scroll bars, widgets, and other graphical components) are controlled by a theme. __GNOME__ comes with a set of different themes which can change the way your applications look. 

The exact method for changing your theme may depend on your distribution. However, for all __GNOME__-based distributions, you can simply run __gnome-tweak-tool__, as shown in the screenshot from __Ubuntu__.

There are other options to get additional themes beyond the default selection. You can download and install themes from http://art.gnome.org/themes/

![image][img6]

## Knowledge Check
1. Which of the following is a popular desktop environment and graphical user interface that runs on top of the Linux operating system?

    A. Fedora
    B. GNOME
    C. SUSE
    D. Debian

    Ans: B
    Explanation
    GNOME is a popular desktop environment and graphical user interface that runs on top of the Linux operating system.

2. Which of the following is a program that adds many more customization options to a GNOME desktop, including installing and configuring extensions?

    A. gnome-extension-editor
    B. gnome-tweak-toolcorrect
    C. gnome-restore-omitted-options
    D. gnome-make-desktop-sane

    Ans: B
    Explanation
    gnome-tweak-tool is a program that adds many more customization options to a GNOME desktop, including installing and configuring extensions.

3. Which of the following steps initiates changing the desktop background?

    A. When logging in, before typing your password, click on the upper right corner.
    B. Right-click on the desktop and select Change Desktop Background.
    C. Reinstall the system.

    And: B
    Explanation
    Right-clicking on the desktop is the first step to changing the desktop background. Some of the following steps will differ slightly accord to your Linux distribution.

## Lab 1: Customizing the Desktop
Despite the length of this section, we will not do very elaborate step-by-step lab exercises, because of the diversity of Linux distributions and versions, and because they each customize their desktops, even if the underlying code base is the same. Trying to give exact instructions is an exercise in futility; not only are there many variations, they are susceptible to change every time a new version of a Linux distribution is released.

For the most part, this is not a problem. Graphical interfaces are designed to be easy to navigate and figure out, and they really do not vary very much, not only from one distribution to another, but even between operating systems. So, the only way you can get more adept at working efficiently on your desktop is to simply explore, play, and modify. The same points will apply to the next chapter, on graphical system configuration.

Linux is so customizable that very few people who use it stay with the default look and feel of the desktop. You may as well get started now in making your desktop reflect your likes and personality.

+ Start by changing the desktop background to something that better suits yours tastes; perhaps one of the provided backgrounds, a solid color of your choice, or a personal picture that you can transfer onto your Linux environment.
+ Next, select a theme from the available themes for your distribution that, again, suits your tastes and personality. Have fun and explore with this exercise.

Click [the link][lab1] to view a solution to the Lab exercise.

# Section 2: Session Management
## Logging In and Out
The next few screens cover the demonstrations and Try-It-Yourself activity for a member of each of the three Linux distribution families we cover in this course. You can view a demonstration for the distribution type of your choice and practice the procedure through the relevant Try-It-Yourself activity.

## Logging In and Logging Out Using the GUI in openSUSE and CentOS
Click below to view a demonstration on how to log in and log out using the GUI in __openSUSE__. Please note the video shows __openSUSE__, but the procedures are exactly the same (and appear the same as well) on __CentOS__ and other recent __GNOME__-based Linux distributions.

[video][vid5]

## Logging In and Logging Out Using the GUI in Ubuntu
Click below to view a demonstration on how to log in and log out using the GUI in __Ubuntu__, a member of the __Debian__ Family Version of Linux.

[video][vid6]

## Try-It-Yourself: Logging In and Logging Out
To practice logging in and logging out using the GUI __openSUSE__, click the link below.

[Logging In and Logging Out using the GUI in openSUSE][tiylilo]

(We have not shown the other distributions, as they are all almost exactly the same.)

## Locking the Screen
It is often a good idea to lock your screen to prevent other people from accessing your session while you are away from your computer. Note this does not suspend the computer; all your applications and processes continue to run while the screen is locked. There are two ways to lock your screen:

+ Using the graphical interface.
+ Using the keyboard shortcut __SUPER-L__. (The __SUPER__ key is also known as the __Windows__ key). On some distributions, you can also hit __CTL-ALT-L__. 

The keyboard shortcut for locking the screen in the three distros can be modified by altering keyboard settings, the exact prescription varying by distribution, but not hard to ascertain.

The screenshot shows how to lock the screen for __Ubuntu__; the following screen gives details for __openSUSE__. The details vary little in modern distributions, so we do not give more examples.

[image][img7]

## Locking and Unlocking the Screen in openSUSE
To lock and unlock your screen in __openSUSE__, perform the following steps:

1. Click the power icon on the upper-right corner of the desktop.
2. Click the lock icon. The screen is locked immediately.
3. Press __Enter__. The login screen is displayed.
4. To unlock the screen, enter the password.
5. Click __Unlock__ and the desktop screen is displayed.

Note: When you lock the screen, GNOME will blank the screen or run a screensaver, depending on your settings.

![image][img8]

# Switching Users
Linux is a true multi-user operating system, which allows more than one user to be simultaneously logged in. If more than one person uses the system, it is best for each person to have their own user account and password. This allows for individualized settings, home directories, and other files. Users can take turns using the machine, while keeping everyone's sessions alive, or even be logged in simultaneously through the network.

Note: The next few screens cover the demonstrations and Try-It-Yourself activity for a member of each of the three Linux distribution families we cover in this course. You can view a demonstration for the distribution type of your choice and practice the procedure through the relevant Try-It-Yourself activity.

## Switching Users in openSUSE and CentOS
Click below to view a demonstration on how to switch users while running current X session in __openSUSE__.  Please note the video shows __openSUSE__, but the procedures are exactly the same (and appear the same as well) on __CentOS__ and other recent __GNOME__-based Linux distributions.

[video][vid7]

## Switching Users in Ubuntu
Click below to view a demonstration on how to switch users while running current X session in __Ubuntu__.

[vido][vid8]

## Shutting Down and Restarting
Besides normal daily starting and stopping of the computer, a system restart may be required as part of certain major system updates, generally only those involving installing a new Linux __kernel__.

Initiating the shutdown process from the graphical desktop is rather trivial on all current Linux distributions, with very little variation. (We will discuss later how to do this from the command line, using the `shutdown` command.) In all cases, you click on either a settings (gear) or a power icon and follow the prompts. We will only show the detail for the __Ubuntu__ Linux distribution.

## Shutting Down and Restarting in Ubuntu
To shut down the computer in Ubuntu, perform the following steps:

1. On the __Ubuntu__ desktop screen, click either the power icon (for earlier versions) or the gear icon in the upper-right corner of the screen.
2. Click __Shut Down...__  The __Restart__ and __Shut Down__ icons are displayed.
3. Click the shut down icon on the right to shutdown the system and click the restart icon on the left to restart the system.

Shutdown, reboot, and logout operations will ask for confirmation before going ahead. This is because many applications will not save their data properly when terminated this way.

Always save your documents and data before restarting, shutting down, or logging out. The Ubuntu screenshot given here is similar to all of the distribution confirmation windows.

![image][img9]

## Suspending
Most modern computers support __suspend mode__ or __sleep mode__ when you stop using your computer for a short while. Suspend mode saves the current system state and allows you to resume your session more quickly while remaining on, but using very little power. It works by keeping your system’s applications, desktop, and so on, in system RAM, but turning off all of the other hardware. The suspend mode bypasses the time for a full system start-up and continues to use minimal power.

## Suspending the System
To suspend the system in __Ubuntu__, the procedure is the same as for shutdown or locking the screen. After you click the icon in the upper right side, you just select __Suspend__.

For other distributions, it is confusing; you click on the power icon while simultaneously holding down the __Alt__ key; then you click on the double dot icon to effectuate suspension. There are extensions you can install to make this less laborious if you find having to use a mouse and a key a little too much.

Note: To wake your system and resume your session, move the mouse or press any button on the keyboard. The system will wake up with the screen locked, just as if you had manually locked it; type in your password to resume.

![image][imga]

## Knowledge Check
1. What action saves the current state of the system in RAM?

    A. Switching user
    B. Suspending 
    C. Shutting down
    D. Logging out

    Ans: 
    Explanation
    Suspending the system saves the current state of the system in RAM.

2. What keyboard shortcut is used to lock the screen?

    A. CTRL-SUPER-ALT-L
    B. SUPER-L 
    C. CTRL-ALT-F7
    D. CTRL-ALT-DEL

    Ans: B
    Explanation
    The keyboard shortcut used to lock the screen is SUPER-L; on some distributions, you can also do CTRL-ALT-L.

# Section 3: Basic Operations
## Basic Operations
Even experienced users can forget the precise command that launches an application, or exactly what options and arguments it requires. Fortunately, Linux allows you to quickly open applications using the graphical interface.

Applications are found at different places in Linux (and within __GNOME__):

+ In __CentOS__, applications can be opened from the __Applications__ menu in the upper-left corner of the screen.
+ In __openSUSE__, applications can be opened from the __Activities__ menu in the upper-left corner of the screen.
+ In __Ubuntu__, applications can be opened from the __Dash__ button in the upper-left corner of the screen.
+ For __KDE__, and other environments, applications can be opened from the button in the lower-left corner.

On the following screens you will learn how to perform basic operations in Linux using the graphical Interface.

![image][imgb]
![image][imgc]

## Locating Applications
Unlike other operating systems, the initial install of Linux usually comes with a wide range of applications and software archives that contain thousands of programs that enable you to accomplish a wide variety of tasks with your computer. For most key tasks, a default application is usually already installed. However, you can always install more applications and try different options.

For example, __Firefox__ is popular as the default browser in many Linux distributions, while __Epiphany, Konqueror__, and __Chromium__ (the open-source base for __Google Chrome__) are usually available for install from software repositories. Proprietary web browsers, such as __Opera__ and __Chrome__, are also available.

Locating applications from the __GNOME__ and __KDE__ menus is easy, as they are neatly organized in functional submenus.

![image][imgd]

## Default Applications
Multiple applications are available to accomplish various tasks and to open a file of a given type. For example, you can click on a web address while reading an email and launch a browser such as __Firefox__ or __Chrome__.

To set default applications, enter the __System Settings__ menu (on all recent Linux distributions) and then click on __Details->System->Default Applications__. The exact list will vary from what is shown here in the __Ubuntu__ screenshot according to what is actually installed and available on your system.

![imag][imge]

## File Manager
Each distribution implements the __File Manager__ utility, which is used to navigate the file system. It can locate files and, when a file is clicked upon, either it will run if it is a program, or an associated application will be launched using the file as data. This behavior is completely familiar to anyone who has used other operating systems.

To start the __File Manager__, you will have to locate its icon, a file cabinet, which is easily found under __Favorites__ or __Applications__.

The __File Manager__ (__Files__ in the case of __Ubuntu__) will open a window with your __Home__ directory displayed. The left panel of the __File Manager__ window holds a list of commonly used directories, such as __Computer__, __Home__, __Desktop__, __Documents__, __Downloads__, and __Trash__.

You can click the magnifying glass icon on the top-right of the __File Manager__ window to search for files or directories (folders) .

![image][imgf]

## Home Directories
The __File Manager__ lets you access different locations on your computer and the network, including the __Home__ directory, __Desktop, Computer, Network__, and other attached devices. The __Browse Network__ and __Connect to Server__ options access networked and shared devices, such as file servers and printers present on the local network.

Every user with an account on the system will have a home directory, usually created under `/home`, and usually named according to the user, such as `/home/student`.

By default, files the user saves will be placed in a directory tree starting there. Account creation, whether during system installation or at a later time, when a new user is added, also induces default directories to be created under the user's home directory, such as __Documents__, __Desktop__, and __Downloads__.

In the screenshot shown for __CentOS 7__, we have chosen the list format and are also showing "hidden files" (those starting with a period.)  See if you can do the same on your distribution.

![image][imgg]

## Viewing Files
The __File Manager__ allows you to view files and directories in more than one way.

You can switch between the __Icons__ and __List__ formats, either by clicking the familiar icons in the top bar, or you can press  __CTRL-1__ or __CTRL-2__ respectively.

In addition, you can also arrange the files and directories by __Name, Size, Type__, or __Modification Date__ for further sorting. To do so, click View and select __Arrange Items__.

Another useful option is to show __hidden__ files (sometimes imprecisely called system files), which are usually configuration files that are hidden by default and whose name starts with a dot. To show hidden files, select __Show Hidden Files__ from the menu or press __CTRL-H__.

The file browser provides multiple ways to customize your window view to facilitate easy drag and drop file operations. You can also alter the size of the icons by selecting __Zoom In__ and __Zoom Out__ under the __View__ menu.

The screenshot is taken from __openSUSE__.

![image][imgh]

## Searching for Files
The __File Manager__ includes a great search tool inside the file browser window.

1. Click __Search__ in the toolbar (to bring up a text box).
2. Enter the keyword in the text box. This causes the system to  perform a recursive search from the current directory for any file or directory which contains a part of this keyword.
3. To open the __File Manager__ from the command line, on most systems simply type `nautilus`.

Note: Both the above methods will open the graphical interface for the program.

The shortcut key to get to the search text box is __CTRL-F__. You can exit the search text box view by clicking the Search button or __CTRL-F__ again.

Another quick way to access a specific directory is to press __CTRL-L__, which will give you a __Location__ text box to type in a path to a directory.

You can refine your search beyond the initial keyword by providing drop-down menus to further filter the search.

1. Based on __Location__ or __File Type__, select additional criteria from the drop-down.
2. To regenerate the search, click the __Reload__ button.
3. To add multiple search criteria, click the + button and select __additional search criteria__.

For example, if you want to find a PDF file containing the word Linux in your __home__ directory, navigate to your __home__ directory and search for the word “Linux”. You should see that the default search criterion limits the search to your __home__ directory already. To finish the job, click the + button to add another search criterion, select __File Type__ for the type of criterion, and select __PDF__ under the __File Type__ drop-down.

![image][imgi]

## Editing a File
Editing any text file through the graphical interface is easy in the __GNOME__ desktop environment. Simply double-click the file on the desktop or in the __Nautilus__ file browser window to open the file with the default text editor.

The default text editor in __GNOME__ is __gedit__. It is simple yet powerful, ideal for editing documents, making quick notes, and programming. Although __gedit__ is designed as a general purpose text editor, it offers additional features for spell checking, highlighting, file listings, and statistics.

You will learn much more about using text editors in a later chapter.

## Removing a File
Deleting a file in Nautilus will automatically move the deleted files to the .local/share/Trash/files/ directory (a trash can of sorts) under the user's __HOME__ directory. There are several ways to delete files and directories using Nautilus.

1. Select all the files and directories that you want to delete.
2. Press __Delete__ (in __Unity/KDE__) or __CTRL-Delete__ (in __GNOME__) on your keyboard. Or, right-click the file.
3. Select __Move to Trash__. Or, highlight the file.
4. Click __Edit__ and __Move to Trash__ through the graphical interface.

To permanently delete a file:

1. On the left panel inside a __Nautilus__ file browser window, right-click on the __Trash__ directory.
2. Select __Empty Trash__.

Alternatively, select the file or directory you want to permanently delete and press __Shift-Delete__.

As a precaution, you should __never delete your home directory__, as doing so will most likely erase all your __GNOME__ configuration files and possibly prevent you from logging in. Many personal system and program configurations are stored under your __home__ directory.

Note: The next few screens cover the demonstrations and Try-It-Yourself activities for a member of each of the three Linux distribution families we cover in this course. You can view a demonstration for the distribution type of your choice and practice the procedure through the relevant Try-It-Yourself activity.

## Locating and Setting Default Applications, and Exploring Filesystems in Ubuntu
Click below to view demonstrations of Locating and Setting Default Applications, and Exploring Filesystems in __Ubuntu__.

[video][vid9]

## Locating and Setting Default Applications, and Exploring Filesystems in openSUSE
Click below to view demonstrations of Locating and Setting Default Applications, and Exploring Filesystems in __openSUSE__.

[video][vida]

## Try-It-Yourself: Locating and Setting Default Applications
To practice locating and setting default applications in your chosen distribution, click on the links below.

[Locating and Setting Default Applications in Ubuntu][ubsdf]

[Locating and Setting Default Applications in openSUSE][ossdf]

## Knowledge Check
1. Which of these are default directories available under the __home__ directory?

    A. Desktop
    B. Documents 
    C. Root
    D. Downloads 

    Ans: A, B, D
    Explanation
    Default directories available under the __home__ directory include __Documents__, __Desktop__, and __Downloads__.

2. What is the default Text Editor in GNOME?

    A. gedit 
    B. Notepad
    C. Nautilus
    D. redit

    Ans: A
    Explanation
    __gedit__ is the default text editor in __GNOME__.

## Lab 2: Viewing File sort options
Find the latest modified file in `/var/log`.

Click [the link][lab2] below to view a solution to the Lab exercise.

## Lab 3: Recovering Deleted Files
The basic operations will be the same here, whether you have a __GNOME__ or __KDE__ desktop, although exact procedures and choices may differ slightly.

1. Create a new text file on the desktop named lab.txt, using the graphical file manager.
2. Delete the file by sending it to __Trash__.
3. Verify the file is now in `~/.local/share/Trash`, or a subdirectory thereof. (Note, You will have to get your file browser to show hidden files and directories, those that start with a .).
4. Recover the file and make sure it is in its original location.

Click [the link][lab3] to view a solution to the Lab exercise.

# Summary
You have completed this chapter. Let's summarize the key concepts covered:

+ __GNOME__ is a popular desktop environment and graphical user interface that runs on top of the Linux operating system.
+ The default display manager for __GNOME__ is called __gdm__.
+ The __gdm__ display manager presents the user with the login screen, which prompts for the login username and password.
+ Logging out through the desktop environment kills all processes in your current __X__ session and returns to the display manager login screen.
+ Linux enables users to switch between logged-in sessions.
+ Suspending puts the computer into sleep mode.
+ For each key task, there is generally a default application installed.
+ Every user created in the system will have a __home__ directory.
+ The __Places__ menu contains entries that allow you to access different parts of the computer and the network.
+ __Nautilus__ gives three formats to view files.
+ Most text editors are located in the __Accessories__ submenu.
+ Each Linux distribution comes with its own set of desktop backgrounds.
+ __GNOME__ comes with a set of different themes which can change the way your applications look.




[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005900_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008600_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V001500_DTH.mp4
[vid4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005300_DTH.mp4
[vid5]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007800_DTH.mp4
[vid6]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004600_DTH.mp4
[vid7]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008700_DTH.mp4
[vid8]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008900_DTH.mp4
[vid9]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V010100_DTH.mp4
[vida]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002400_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a3a72f3ec6ae857193e073098fd6b5f9/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch04_screen03.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/44717c86868ff7e9edc71c5747bb84ab/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen28.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c4a2925d0a2d22c238c9f1d91f71635b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen29.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/601552faa90b0d72941ad4e6048e34d0/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/wallpaperubuntu.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b9aeb9e063eda9567443ab77501286d3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/gnometweaktool.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3b96462047b8da666c50589c7d570824/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/themesuse.png
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9473190458fa8e2f0a2f81354cd71a98/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lockubuntu.png
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f4d46b253fe9ce5df21b117349a09dbb/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/locksuse.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a8013f2d5e4b761901c90e330c133acf/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/ubuntushutdowngui.png
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9473190458fa8e2f0a2f81354cd71a98/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lockubuntu.png
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e7b1de61ac15ee5dc0f5b60a64b144d9/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/centos7-suse-apps.png
[imgc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1d3575c5fb18b2157ee4889cb31d1217/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/ubuntu-apps.png
[imgd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d41c55a443fccfd606e81d031293b3f2/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch04_screen39a.png
[imge]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a1cf5a1de9d3377424320c1037c9d5ea/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/defappsubuntu.png
[imgf]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/97762847d4dde516ac0f74c346f06ccc/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/homefilesubuntu.png
[imgg]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c05ceb1a2c2f1e93bac749cca25da5a2/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/homefilescentos7.png
[imgh]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/59b49f03cf57ecaf483df8f2f06f32b9/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/homefilessuse.png
[imgi]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/92b46e00f94ca300fff886db41b6d2d3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/searchubuntu.png

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-desktop.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-filesort.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-recoverfiles.html

[centosdb]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/backgroundcentos/index.html
[susedb]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/backgroundopensuse/index.html
[ubuntudb]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/backgroundubuntu/index.html
[tiylilo]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/loginsuse/index.html
[ubsdf]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingdefubuntu/index.html
[ossdf]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingdefsuse/index.html
