Chapter 17: Printing
====================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should know how to:

+ Configure a printer on a Linux machine.
+ Print documents.
+ Manipulate postscript and pdf files using command line utilities.


# Section 1: Configuration
To manage printers and print directly from a computer or across a networked environment, you need to know how to configure and install a printer. Printing itself requires software that converts information from the application you are using to a language your printer can understand. The Linux standard for printing software is the __Common UNIX Printing System (CUPS)__.

## CUPS Overview
__CUPS__ is the software that is used behind the scenes to print from applications like a web browser or LibreOffice. It converts page descriptions produced by your application (put a paragraph here, draw a line there, and so forth) and then sends the information to the printer. It acts as a __print server__ for local, as well as network printers.

Printers manufactured by different companies may use their own particular print languages and formats. __CUPS__ uses a modular printing system which accommodates a wide variety of printers and also processes various data formats. This makes the printing process simpler; you can concentrate more on printing and less on how to print.

Generally, the only time you should need to configure your printer is when you use it for the first time. In fact, __CUPS__ often figures things out on its own by detecting and configuring any printers it locates.

## How Does CUPS Work?
__CUPS__ carries out the printing process with the help of its various components:

+ Configuration Files
+ Scheduler
+ Job Files
+ Log Files
+ Filter
+ Printer Drivers
+ Backend.

![image][img1]

## Scheduler
CUPS is designed around a __print scheduler__ that manages print jobs, handles administrative commands, allows users to query the printer status, and manages the flow of data through all CUPS components.

As you will see shortly, CUPS has a browser-based interface, which allows you to view and manipulate the order and status of pending print jobs.

## Configuration Files
The print scheduler reads server settings from several configuration files, the two most important of which are `cupsd.conf` and `printers.conf`. These and all other CUPS related configuration files are stored under the `/etc/cups/` directory.

`cupsd.conf` is where most system-wide settings are located; it does not contain any printer-specific details. Most of the settings available in this file relate to network security, i.e. which systems can access CUPS network capabilities, how printers are advertised on the local network, what management features are offered, and so on.

`printers.conf` is where you will find the printer-specific settings. For every printer connected to the system, a corresponding section describes the printer’s status and capabilities. This file is generated only after adding a printer to the system and should not be modified by hand.

You can view the full list of configuration files by typing: `ls -l /etc/cups/`

## Job Files
CUPS stores print requests as files under the `/var/spool/cups` directory (these can actually be accessed before a document is sent to a printer). Data files are prefixed with the letter `d` while control files are prefixed with the letter `c`. After a printer successfully handles a job, data files are automatically removed. These data files belong to what is commonly known as the __print queue__.

![image][img2]

## Log Files
Log files are placed in `/var/log/cups` and are used by the scheduler to record activities that have taken place. These files include access, error, and page records.

To view what log files exist, type: 
```bash
sudo ls -l /var/log/cups
```
(Note on some distributions permissions are set such that you don't need the sudo.) You can view the log files with the usual tools.

![image][img3]

## Filters, Printer Drivers, and Backends
__CUPS__ uses filters to convert job file formats to printable formats. Printer drivers contain descriptions for currently connected and configured printers, and are usually stored under `/etc/cups/ppd/`. The print data is then sent to the printer through a filter and via a backend that helps to locate devices connected to the system.

So, in short, when you execute a print command, the scheduler validates the command and processes the print job, creating job files according to the settings specified in the configuration files. Simultaneously, the scheduler records activities in the log files. Job files are processed with the help of the filter, printer driver, and backend, and then sent to the printer.

## Installing CUPS
Due to printing being a relatively important and fundamental feature of any Linux distribution, most Linux systems come with CUPS preinstalled. In some cases, especially for Linux server setups, CUPS may have been left uninstalled. This may be fixed by installing the corresponding package manually. To install CUPS, please ensure that your system is connected to the Internet.

You can use the commands shown below to manually install CUPS:

- CentOS: $ `sudo yum install cups`
- OpenSUSE: $ `sudo zypper install cups`
- Ubuntu: $ `sudo apt-get install cups`

The video below demonstrates this procedure for Ubuntu, the other two are similar, once the correct install command is provided.

Note: CUPS features are also supported by other packages, such as `cups-common` and `libcups2`, which contain the core CUPS libraries. The above install command will make sure any needed packages are also installed.

Click below to view the demonstration to install CUPS in Ubuntu.

[video][vid1]

## Managing CUPS
After installing CUPS, you'll need to start and manage the CUPS daemon so that CUPS is ready for configuring a printer. Managing the CUPS daemon is simple; all management features are wrapped around the cups init script, which can be easily started, stopped, and restarted.

### Managing the CUPS daemon in __Ubuntu__
Click below to view the demonstration to manage CUPS daemon in __Ubuntu__.

[video][vid2]

```bash
# start/stop/restart/display printer service
$ sudo /etc/init.d/cups start
$ sudo /etc/init.d/cups restart
$ sudo /etc/init.d/cups status
$ sudo /etc/init.d/cups stop

# boot time initial printer service
$ sudo update-rc cups enable
$ sudo update-rc -f cups default
$ sudo update-rc cups disable
```

### Managing the CUPS daemon in __openSUSE__
Click below to view the demonstration to manage CUPS daemon in __openSUSE__.

[video][vid3]

```bash
# start/stop/restart/display printer service
$ sudo /etc/init.d/cups start
$ sudo /etc/init.d/cups restart
$ sudo /etc/init.d/cups status
$ sudo /etc/init.d/cups stop

# boot time printer service
$ sudo chkconfig cups on
```

### Managing the CUPS in __CentOS__
Click below to view the demonstration to manage CUPS daemon in __CentOS__.

[video][vid4]

```bash
# start/stop/restart/display printer service
sudo service cups start
sudo service cups restart
sudo service cups status
sudo service cups stop

# boot time printer service
$ sudo chkconfig xups on
$ sudo chkconfig xups off
```
## Configuring a Printer from the GUI
Each Linux distribution has a GUI application that lets you add, remove, and configure local or remote printers. Using this application, you can easily set up the system to use both local and network printers. The following screens show how to find and use the appropriate application in each of the distribution families covered in this course.

When configuring a printer, make sure the device is currently turned on and connected to the system; if so it should show up in the printer selection menu. If the printer is not visible, you may want to troubleshoot using tools that will determine if the printer is connected. For common USB printers, for example, the __lsusb__ utility will show a line for the printer. Some printer manufacturers also require some extra software to be installed in order to make the printer visible to CUPS, however, due to the standardization these days, this is rarely required.

### Configuring a Printer in Ubuntu
Click below to view the demonstration to manage CUPS daemon in __Ubuntu__.

[video][vid5]

### Configuring a Printer in openSUSE
Click below to view the demonstration to manage CUPS daemon in __openSUSE__.

[video][vid6]

### Configuring a Printer in CentOS
Click below to view the demonstration to manage CUPS daemon in __Cent__.

[video][vid7]

## Adding Printers from the CUPS Web Interface
A fact that few people know is that CUPS also comes with its own web server, which makes a configuration interface available via a set of CGI scripts.

This web interface allows you to:

+ Add and remove local/remote printers
+ Configure printers:
    + Local/remote printers
    + Share a printer as a CUPS server
+ Control print jobs:
    + Monitor jobs
    + Show completed or pending jobs
    + Cancel or move jobs.

The __CUPS__ web interface is available on your browser at: `http://localhost:631`

Some pages require a username and password to perform certain actions, for example to add a printer. For most Linux distributions, you must use the root password to add, modify, or delete printers or classes.

## Knowledge Check
1. Which two things can CUPS do?

    A. Connect a local printer to a Linux system and share it over a network 
    B. Connect a network printer to a Linux system 
    C. Configure a network IP to the system
    D. Configure a local printer on Windows machine

    Ans: A, B
    Explanation
    CUPS can connect a local printer to a Linux system and share it over a network and can also connect a network printer to a Linux system.


# Section 2: Printing Operations
## Printing from the Graphical Interface
Many graphical applications allow users to access printing features using the `CTRL-P` shortcut. To print a file, you first need to specify the printer (or a file name and location if you are printing to a file instead) you want to use; and then select the page setup, quality, and color options. After selecting the required options, you can submit the document for printing. The document is then submitted to CUPS. You can use your browser to access the CUPS web interface at `http://localhost:631/` to monitor the status of the printing job. Now that you have configured the printer, you can print using either the Graphical or Command Line interfaces.

The screenshot shows the GUI interface for `CTRL-P` for __CentOS__, other Linux distributions appear virtually identical.

![image][img4]

## Printing from the Command-Line Interface
CUPS provides two command-line interfaces, descended from the __System V__ and __BSD__ flavors of UNIX. This means that you can use either `lp` (System V) or `lpr` (BSD) to print. You can use these commands to print text, PostScript, PDF, and image files.

These commands are useful in cases where printing operations must be automated (from shell scripts, for instance, which contain multiple commands in one file). 

`lp` is just a command line front-end to the lpr utility that passes input to `lpr`. Thus, we will discuss only lp in detail. In the example shown here, the task is to print the file called test1.txt.

![image][img5]

## Using lp
`lp` and `lpr` accept command line options that help you perform all operations that the GUI can accomplish. lp is typically used with a file name as an argument.

Some `lp` commands and other printing utilities you can use are listed in the table:

| Command | Usage |
|---------|-------|
| `lp <filename>` | To print the file to default printer |
| `lp -d printer <filename>` | To print to a specific printer (useful if multiple printers are available) |
| `program | lp` or `echo string | lp` | To print the output of a program  |
| `lp -n number <filename>` | To print multiple copies |
| `lpoptions -d printer` | To set the default printer |
| `lpq -a` | To show the queue status |
| `lpadmin` | To configure printer queues |

The `lpoptions` utility can be used to set printer options and defaults. Each printer has a set of tags associated with it, such as the default number of copies and authentication requirements. You can execute the command `lpoptions` help to obtain a list of supported options. `lpoptions` can also be used to set system-wide values, such as the default printer.

Click below to view a demonstration on how to print using `lp`.

[video][vid8]

## Try-It-Yourself: Printing with the lp Command
To practice, click the link provided below.

[Printing With the lp Command][lp]

## Managing Print Jobs
You send a file to the shared printer. But when you go there to collect the printout, you discover another user has just started a 200 page job that is not time sensitive. Your file cannot be printed until this print job is complete. What do you do now?

In Linux, command line print job management commands allow you to monitor the job state as well as managing the listing of all printers and checking their status, and canceling or moving print jobs to another printer.

Some of these commands are listed in the table. 

| Command | Usage |
|---------|-------|
| `lpstat -p -d` | To get a list of available printers, along with their status |
| `lpstat -a` | To check the status of all connected printers, including job numbers |
| `cancel job-id` OR `lprm job-id` | To cancel a print job |
| `lpmove job-id newprinter` | To move a print job to new printer |

## Try-It-Yourself: Managing Print Jobs
To practice, click the link provided below.

[Managing Print Jobs][pj]


# Section 3: Manipulating Postscript and PDF Files
## Working with PostScript
__PostScript__ is a standard __page description language__. It effectively manages scaling of fonts and vector graphics to provide quality printouts. It is purely a text format that contains the data fed to a PostScript interpreter. The format itself is a language that was developed by __Adobe__ in the early 1980s to enable the transfer of data to printers.

Features of PostScript are:

+ It can be used on any printer that is PostScript-compatible; i.e., any modern printer
+ Any program that understands the PostScript specification can print to it
+ Information about page appearance, etc. is embedded in the page

__Postscript__ has been for the most part superseded by the __PDF__ format (__Portable Document Format__) which produces far smaller files in a compressed format for which support has been integrated into many applications.   However, one still has to deal with postscript documents, often as an intermediate format on the way to producing final documents.

![image][img6]

__enscript__ is a tool that is used to convert a text file to PostScript and other formats. It also supports __Rich Text Format (RTF)__ and __HyperText Markup Language (HTML)__. For example, you can convert a text file to two columns (`-2`) formatted PostScript using the command: `enscript -2 -r -p psfile.ps textfile.txt`. This command will also rotate (`-r`) the output to print so the width of the paper is greater than the height (aka landscape mode) thereby reducing the number of pages required for printing.

The commands that can be used with enscript are listed in the table below (for a file called `textfile.txt`).

| Command | Usage |
|---------|-------|
| `enscript -p psfile.ps textfile.txt` | Convert a text file to PostScript (saved to psfile.ps) |
| `enscript -n -p psfile.ps textfile.txt` | Convert a text file to n columns where n=1-9 (saved in psfile.ps) |
| `enscript textfile.txt` | Print a text file directly to the default printer |

## Converting between PostScript and PDF
Most users today are far more accustomed to working with files in __PDF__ format, viewing them easily either on the Internet through their browser or locally on their machine. The __PostScript__ format is still important for various technical reasons that the general user will rarely have to deal with.

From time to time, you may need to convert files from one format to the other, and there are very simple utilities for accomplishing that task. __ps2pdf__ and __pdf2ps__ are part of the ghostscript package installed on or available on all Linux distributions. As an alternative, there are __pstopdf__ and __pdftops__ which are usually part of the __poppler__ package, which may need to be added through your package manager. Unless you are doing a lot of conversions or need some of the fancier options (which you can read about in the man pages for these utilities), it really does not matter which ones you use.

Another possibility is to use the very powerful __convert__ program, which is part of the __ImageMagick__ package.

Some usage examples:
| Command | Usage |
|---------|-------|
| `pdf2ps file.pdf` | Converts `file.pdf` to `file.ps` |
| `ps2pdf file.ps` | Converts `file.ps` to `file.pdf` |
| `pstopdf input.ps output.pdf` | Converts `input.ps` to `output.pdf` |
| `pdftops input.pdf output.ps` | Converts `input.pdf` to `output.ps` |
| `convert input.ps output.pdf` | Converts `input.ps` to `output.pdf` |
| `convert input.pdf output.ps` | Converts `input.pdf` to `output.ps` |

## Viewing PDF Content
Linux has many standard programs that can read __PDF__ files, as well as many applications that can easily create them, including all available office suites, such as __LibreOffice__.

The most common Linux PDF readers are:

1. __Evince__ is available on virtually all distributions and the most widely used program.
2. __Okar__ is based on the older `kpdf` and available on any distribution that provides the __KDE__ environment.
3. __GhostVw__ is one of the first open source PDF readers and is universally available.
4. __Xp__ is one of the oldest open source PDF readers and still has a good user base. 

A of these open source PDF readers support and can read files following the PostScript standard unlike the proprietary __Adobe Acrobat Reader__, which was once widely used on Linux systems, but, with the growth of these excellent programs, very few Linux users use it today.

## Manipulating PDFs with __pdftk__
At times, you may want to merge, split, or rotate PDF files; not all of these operations can be achieved while using a PDF viewer. A great way to do this is to use the "__PDF Toolkit__", `pdftk`, to perform a very large variety of sophisticated tasks. Some of these operations include:

+ Merging/Splitting/Rotating PDF documents
+ Repairing corrupted PDF pages
+ Pulling single pages from a file
+ Encrypting and decrypting PDF files
+ Adding, updating, and exporting a PDF’s metadata
+ Exporting bookmarks to a text file
+ Filling out PDF forms.

In short, there’s very little `pdftk` cannot do when it comes to working with PDF files; it is indeed the Swiss Army knife of PDF tools. However, unfortunately pdftk is no longer available on all Linux distributions, as we discuss next.

## Installing pdftk on Different Family Systems
To install `pdftk` on Ubuntu, use the following command:
```bash
$ sudo apt-get install pdftk
```
On CentOS 6:
```bash
$ sudo yum install pdftk
```
On openSUSE:
```bash
$ sudo zypper install pdftk
```
You may find that __CentOS__ (and __RHEL__) don't have pdftk in their packaging system, but you can obtain the __PDF Toolkit__ directly from the PDF Lab’s website, by downloading from: `http://www.pdflabs.com/docs/install-pdftk-on-redhat-or-centos/`  For __RHEL7/CentOS7__ and recent versions of Fedora, it is no longer possible to install `pdftk` without considerable __acrobatics__ as a required library, `libgcj`, is considered obsolete and no longer available. The authors of pdftk have long promised to distribute a version that will work on these systems, but have never done so.

![image][img7]

## Using pdftk
You can accomplish a wide variety of tasks using __pdftk__ including:

| Command | Usage |
|---------|-------|
| `pdftk 1.pdf 2.pdf cat output 12.pdf` | Merge the two documents `1.pdf` and `2.pdf`. The output will be saved to `12.pdf`. |
| `pdftk A=1.pdf cat A1-2 output new.pdf` | Write only pages 1 and 2 of `1.pdf`. The output will be saved to `new.pdf`. |
| `pdftk A=1.pdf cat A1-endright output new.pdf` | Rotate all pages of `1.pdf` 90 degrees clockwise and save result in `new.pdf`. |

## Encrypting PDF Files
If you’re working with PDF files that contain confidential information and you want to ensure that only certain people can view the PDF file, you can apply a password to it using the `user_pw` option. One can do this by issuing a command such as:
```bash
$ pdftk public.pdf output private.pdf user_pw PROMPT
```
When you run this command, you will receive a prompt to set the required password, which can have a maximum of 32 characters. A new file, `private.pdf`, will be created with the identical content as `public.pdf`, but anyone will need to type the password to be able to view it.

![image][img8]

## Using Ghostscript
__Ghostscript__ is widely available as an interpreter for the Postscript and PDF languages. The executable program associated with it is abbreviated to `gs`.

This utility can do most of the operations __pdftk__ can, as well as many others; see `man gs` for details. Use is somewhat complicated by the rather long nature of the options. For example:

+ Combine three PDF files into one:
```bash
    $ gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite  -sOutputFile=all.pdf file1.pdf file2.pdf file3.pdf
```
+ Split pages 10 to 20 out of a PDF file:
```bash
    $ gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dDOPDFMARKS=false -dFirstPage=10 -dLastPage=20\
    -sOutputFile=split.pdf file.pdf
```

## Using pdftk
Click below to view a demonstration of various tasks that can be performed on a PDF file using __pdftk__.

[video][vid9]

## Using Additional Tools
You can use other tools, such as __pdfinfo, flpsed__, and __pdfmod__ to work with PDF files.

__pdfinfo__ can extract information about PDF files, especially when the files are very large or when a graphical interface is not available.

__flpsed__ can add data to a PostScript document. This tool is specifically useful for filling in forms or adding short comments into the document.

__pdfmod__ is a simple application that provides a graphical interface for modifying PDF documents. Using this tool, you can reorder, rotate, and remove pages; export images from a document; edit the title, subject, and author; add keywords; and combine documents using drag-and-drop action.

For example, to collect the details of a document, you can use the following command:
```bash
$ pdfinfo /usr/share/doc/readme.pdf
```
![image][img9]

## Lab 1: Creating PostScript and PDF from Text Files
1. Check to see if the enscript package has been installed on your system, and if not, install it.

2. Using `enscript`, convert the text file `/var/dmesg` to PostScript format and name the result `/tmp/dmesg.ps`. (As an alternative, you can use any large text file on your system.) Make sure you can read the PostScript file (with `evince` for example) and compare to the original file.

    (Note: on some systems, such as RHEL7/CentOS7, evince may have problems with the PostScript file, but the PDF file you produce from it will be fine for viewing.)

3. Convert the PostScript document to PDF format, using `ps2pdf`. Make sure you can read the resulting PDF file. Does it look identical to the PostScript version?

4. Is there a way you can go straight to the PDF file without producing a PostScript file on the disk along the way?

5. Using pdfinfo, determine what is the PDF version used to encode the file, the number of pages, the page size, and other metadata about the file. (If you do not have pdfinfo you probably need to install the poppler-utils package.

Click [the link][lab1] to view a solution to the Lab exercise. 

## Lab 2: Combining PDFs
You can convert two text files (you can create them or use ones that already exist since this is non-destructive) into PDFs, or you can use two pre-exisiting ones. Combine them into one PDF, and view the result.

If pdftk is not installed, you can try to install. However, if you are on a system for which it is not available (such as RHEL7/CentOS7), you will have to use gs.

Click [the link][lab2] to view a solution to the Lab exercise.


# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ CUPS provides two command-line interfaces: the System V and BSD interfaces.
+ The CUPS interface is available at `http://localhost:631`
+ `lp` and `lpr`  are used to submit a document to CUPS directly from the command line.
+ `lpoptions` can be used to set printer options and defaults.
+ PostScript effectively manages scaling of fonts and vector graphics to provide quality prints.
+ `enscript` is used to convert a text file to PostScript and other formats.
+ __Portable Document Format (PDF)__ is the standard format used to exchange documents while ensuring a certain level of consistency in the way the documents are viewed.
+ `pdftk` joins and splits PDFs; pulls single pages from a file; encrypts and decrypts PDF files; adds, updates, and exports a PDF’s metadata; exports bookmarks to a text file; adds or removes attachments to a PDF; fixes a damaged PDF; and fills out PDF forms.
+ `pdfinfo` can extract information about PDF documents.
+ `flpsed` can add data to a PostScript document.
+ `pdfmod` is a simple application with a graphical interface that you can use to modify PDF documents.



[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007600_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008500_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003500_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007900_DTH.mp4
[vid4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V001300_DTH.mp4
[vid5]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008100_DTH.mp4
[vid6]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V001800_DTH.mp4
[vid7]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009200_DTH.mp4
[vid8]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008300_DTH.mp4
[vid9]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007000_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/28c1710704f1ec7b7ccd6077c7aa31f4/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch13_screen_05.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b27d7c01c145f191b20af19557961c06/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch13_screen_08.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8982f4095d6fedbc55e436c682674f3d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch13_screen_09.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/91be7ab270ff6ac96da0a42409b190fe/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/printingrhel7.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/66b0064f81cd4f18fa50ccd9fde41bf9/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/lprhel7.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0361c9466d73a78da7b4a4846bd6b984/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_Ch13_Screen_42.jpg
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a15d96f16e867048096a4f336e551157/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch13_Screen_48.jpg
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/36d90570d210656beea8e67715021db3/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/pdfencryptsuse.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5c4cda1c771ca4c7a29e6bb1d4a3d5ea/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch13_Screen_53.jpg

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-enscript.html

[lp]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usinglp/index.html
[pj]: https://learningmate.s3-us-west-2.amazonaws.com/LFS01/Chapter13/Section2/screen42/index.html

