Chapter 04: Graphical Interface
===============================

# Introduction/ Learning Objectives
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

# Section 3: Basic Operations



# Summary



[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005900_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008600_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V001500_DTH.mp4
[vid4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V005300_DTH.mp4
[vid5]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007800_DTH.mp4
[vid6]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004600_DTH.mp4
[vid7]: 
[vid8]: 
[vid9]: 
[vida]: 
[vidb]: 


[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a3a72f3ec6ae857193e073098fd6b5f9/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch04_screen03.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/44717c86868ff7e9edc71c5747bb84ab/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen28.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c4a2925d0a2d22c238c9f1d91f71635b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch03_screen29.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/601552faa90b0d72941ad4e6048e34d0/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/wallpaperubuntu.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b9aeb9e063eda9567443ab77501286d3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/gnometweaktool.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3b96462047b8da666c50589c7d570824/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/themesuse.png
[img7]: 
[img8]: 
[img9]: 
[imga]: 
[imgb]: 
[imgc]: 
[imgd]: 
[imge]: 
[imgf]: 

[centosdb]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/backgroundcentos/index.html
[susedb]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/backgroundopensuse/index.html
[ubuntudb]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/backgroundubuntu/index.html
[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-desktop.html