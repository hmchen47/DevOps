Chapter 06: Common Applications
===============================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be familiar with common Linux applications, including:

+ Internet applications such as browsers, and email programs.
+ Office Productivity Suites such as __LibreOffice__.
+ Developer tools, such as compilers, debuggers, etc.
+ Multimedia applications, such as those for audio and video.
+ Graphics editors such as the __GIMP__ and other graphics utilities.

# Section 1: Internet Applications
## Internet Applications
The Internet is a global network that allows users around the world to perform multiple tasks, such as searching for data, communicating through emails and online shopping. Obviously, you need to use network-aware applications to take advantage of the Internet. These include:

+ Web browsers
+ Email clients
+ Online media applications
+ Other applications.

[image][img1]

## Web Browsers
As discussed in the earlier chapter on Network Operations, Linux offers a wide variety of web browsers, both graphical and text-based, including:

+ __Firefox__
+ __Google Chrome__
+ __Chromium__
+ __Epiphany__ (renamed __web__)
+ __Konqueror__
+ __linx__
+ __lynx__.

## Email Applications
Email applications allow for sending, receiving, and reading messages over the Internet. Linux systems offer a wide number of __email clients__, both graphical and text-based. In addition, many users simply use their browsers to access their email accounts.

Most email clients use the __Internet Message Access Protocol (IMAP)__ or the older __Post Office Protocol (POP)__ to access emails stored on a remote mail server. Most email applications also display __HTML (HyperText Markup Language)__ formatted emails that display objects, such as pictures and hyperlinks. The features of advanced email applications include the ability of importing address books/contact lists, configuration information, and emails from other email applications.

Linux supports the following types of email applications:

+ Graphical email clients, such as __Thunderbird, Evolution__, and __Claws Mail__
+ Text mode email clients, such as __mutt__ and __mail__
+ All web browser-based clients, such as __gmail, yahoo mail__, and __Office 365__.

![image][img2]

## Other Internet Applications
Linux systems provide many other applications for performing Internet-related tasks. These include:

|  Application  | Use       |
|--------------|-----------|
| __FileZilla__ | Intuitive graphical __FTP__ client that supports __FTP, Secure File Transfer Protocol (SFTP)__, and __FTP Secured (FTPS)__. Used to transfer files to/from __(FTP)__ servers |
| __Pidgin__ | To access __GTalk, AIM, ICQ, MSN, IRC__ and other messaging networks |
| __Ekiga__ | To connect to __Voice over Internet Protocol (VoIP)__ networks |
| __Hexchat__   | To access __Internet Relay Chat (IRC)__ networks |

## Knowledge Check
1. Which two of the following are common __protocols__ used to access emails stored on a remote mail server?

    A. __mutt__

    B. __POP__ 

    C. __mail__

    D. __IMAP__ 

    Ans: B, D
    Explanation: The POP and IMAP protocols are used to access emails stored on a remote mail server.
   
2. Which two of the following are text mode email __clients__ widely available in Linux?

    A. mutt 

    B. Evolution

    C. mail 

    D. Claws Mail

    ANs: A, C

    Explanation: mutt and mail are text mode email clients widely available in Linux.

3. What is __Ekiga__ used for?

    A. To connect to __VoIP__ 

    B. To access __IRC__

    C. To connect to __FTP__ Servers

    D. To access __GTalk__

    Ans: A
    Explanation: Ekiga is used to connect to VoIP networks.


# Section 2: Productivity and Development Applications
## Office Applications
Most day-to-day computer systems have __productivity applications__ (sometimes called __office suites__) available or installed. Each suite is a collection of closely coupled programs used to create and edit different kinds of files such as:

+ Text (articles, books, reports etc.)
+ Spreadsheet
+ Presentation
+ Graphical objects.

Most Linux distributions offer __LibreOffice__, an open source office suite that started in 2010 and has evolved from __OpenOffice.org__. While other office suites are available as we have listed, __LibreOffice__ is the most mature, widely used and intensely developed.

In addition, Linux users have full access to Internet-based Office Suites such as __Google Docs__ and __Microsoft Office 365__.

## LibreOffice Components
The component applications included in LibreOffice are:

+ __Writer__: Word Processing
+ __Calc__: Spreadsheets
+ __Impress__:  Presentations
+ __Draw__:  Create  and edit graphics and diagrams.

The LibreOffice applications can read and write non-native document formats, such as those used by Microsoft Office. Usually, fidelity is maintained quite well, but complicated documents might have some imperfect conversions.

![image][img3]

## Development Applications
Linux distributions come with a complete set of applications and tools that are needed by those developing or maintaining both user applications and the kernel itself.  

These tools are tightly integrated and include:

+ Advanced editors customized for programmers' needs, such as `vi` and `emacs`.
+ Compilers (such as `gcc` for programs in C and C++) for every computer language that has ever existed.
+ Debuggers such as `gdb` and various graphical front ends to it and many other debugging tools (such as `valgrind`).  
+ Performance measuring and monitoring programs, some with easy to use graphical interfaces, others more arcane and meant to be used only by serious experienced development engineers.
+ Complete Integrated Development Environments (IDE's) such as `Eclipse`, that put all these tools together.

On other operating systems, these tools have to be obtained and installed separately, often at a high cost, while on Linux they are all available at no cost through standard package installation systems.

## Knowledge Check
What is the use of the Impress component in LibreOffice?

    A. Word processing
    B. Spreadsheets
    C. Create and edit graphics and diagrams
    D. Presentations 

    Ans: D
    Explanation
    The Impress component in LibreOffice is used to prepare presentations.


# Section 3: Multimedia Applications
## Sound Players
Multimedia applications are used to listen to music, view videos, et.c, as well as to present and view text and graphics. Linux systems offer a number of __sound player__ applications including:

| Application   | Use |
|---------------|-----|
| __Amarok__    | Mature __MP3__ player with a graphical interface, that plays audio and video files, and streams (online audio files). It allows you to create a playlist that contains a group of songs, and uses a database to store information about the music collection. |
| __Audacity__ | Used to record and edit sounds and can be quickly installed through a package manager. __Audacity__ has a simple interface to get you started. |
| __Rhythmbox__ |  Supports a large variety of digital music sources, including streaming Internet audio and podcasts. The application also enables search of particular audio in a library. It supports ‘smart playlists’ with an ‘automatic update’ feature, which can revise playlists based on specified selection criteria. |

Of course, Linux systems can also connect with commercial online music streaming services, such as __Pandora__ and __Spotify__ through web browsers.

## Movie Players
__Movie__ (video) __players__ can portray input from many different sources, either local to the machine or on the Internet.

Linux systems offer a number of movie players including:

+ __VLC__
+ __MPlayer__
+ __Xine__
+ __Totem__.

## Movie Editors
__Movie editors__ are used to edit videos or movies. Linux systems offer a number of movie editors including:

| Application   | Use |
|---------------|-----|
| __Cinepaint__ | Frame-by-frame retouching. __Cinepaint__ is used for editing images in a video. |
| __Blender__ | Create 3D animation and design. __Blender__ is a professional tool that uses modeling as a starting point. There are complex and powerful tools for camera capture, recording, editing, enhancing and creating video, each having its own focus. |
| __Cinelerra__ | Capture, compose, and edit audio/video. |
| __FFmpeg__ | Record, convert, and stream audio/video. __FFmpeg__ is a format converter, among other things, and has other tools such as __ffplay__ and __ffserver__. |


# Section 4: Graphics Editors and Utilities
## GIMP (GNU Image Manipulation Program)
__Graphic editors__ allow you to create, edit, view, and organize images of various formats,  like Joint Photographic Experts Group (JPEG or JPG), Portable Network Graphics (PNG), Graphics Interchange Format (GIF), and Tagged Image File Format (TIFF).

__GIMP (GNU Image Manipulation Program)__ is a feature-rich image retouching and editing tool similar to __Adobe Photoshop__ and is available on all Linux distributions. Some features of the __GIMP__ are:

+ It can handle any image file format.
+ It has many special purpose plugins and filters.
+ It provides extensive information about the image, such as layers, channels, and histograms.

![iamge][img4]

## Graphics Utilities
n addition to the GIMP, there are other graphics utilities that help perform various image-related tasks, including:

| Graphic Utility | Use |
|-----------------|-----|
| __eog__ | __Eye of Gnome (eog)__ is an image viewer that provides slide show capability and a few image editing tools, such as rotate and resize. It can also step through the images in a directory with just a click. |
| __Inkscape__ | __Inkscape__ is an image editor with lots of editing features. It works with layers and transformations of the image. It is sometimes compared to Adobe Illustrator. |
| __convert__ | __convert__ is a command line tool (part of the ImageMagick set of applications) that can modify image files in many ways. The options include file format conversion and numerous image modification options, such as blur, resize, despeckle, etc. |
| __Scribus__ | __Scribus__ is used for creating documents used for publishing and providing a _What You See Is What You Get_ (_WYSIWYG_) environment. It also provides numerous editing tools. |


# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ Linux offers a wide variety of Internet applications, such as web browsers, email clients, online media applications, and others.
+ Web browsers supported by Linux can be either graphical or text-based, such as __Firefox, Google Chrome, Epiphany, w3m, lynx__, and others.
+ Linux supports graphical email clients, such as __Thunderbird, Evolution__, and __Claws Mail__, and text mode email clients, such as __mutt__ and __mail__.
+ Linux systems provide many other applications for performing Internet-related tasks, such as __Filezilla, XChat, Pidgin__, and others.
+ Most Linux distributions offer __LibreOffice__ to create and edit different kinds of documents.
+ Linux systems offer entire suites of development applications and tools, including compilers and debuggers.
+ Linux systems offer a number of sound players including __Amarok, Audacity__, and __Rhythmbox__.
+ Linux systems offer a number of movie players, including __VLC, MPlayer, Xine__, and __Totem__.
+ Linux systems offer a number of movie editors, including __Kino, Cinepaint, Blender__ among others.
+ The __GIMP (GNU Image Manipulation Program)__ utility is a feature-rich image retouching and editing tool available on all Linux distributions.
+ Other graphics utilities that help perform various image-related tasks are __eog, Inkscape, convert__, and __Scribus__.



[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V004300_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9ab13d93d41e76edae95a90f12c96dd3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch17_screen03.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7ea5bcb37db44af78b8e56e6f351fc00/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch17_screen05.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/312e3a47c107ec3d31fa9bd195254e87/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/ooffice.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/eb5482ce7f196048de0070d3a517dd8c/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/gimpsuse.png

