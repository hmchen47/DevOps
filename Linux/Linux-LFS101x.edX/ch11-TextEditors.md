Chapter 11: Text Editors
========================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be familiar with:

+ How to create and edit files using the available Linux text editors.
+ nano, a simple text-based editor.
+ gedit, a simple graphical editor
+ vi and emacs, two advanced editors with both text-based and graphical interfaces.


# Section 1: Basic Editors: nano and gedit
## Overview of Text Editors in Linux
At some point, you will need to manually edit __text files__. You might be composing an email off-line, writing a script to be used for __bash__ or other command interpreters, altering a system or application configuration file, or developing source code for a programming language such as __C__ or __Java__.

Linux Administrators quite often sidestep the text editors, by using graphical utilities for creating and modifying system configuration files. However, this can be far more laborious than directly using a text editor. Note that word processing applications such as __Notepad__ or the applications that are part of office suites are not really basic text editors because they add a lot of extra (usually invisible) formatting information that will probably render system administration configuration files unusable for their intended purpose. So, using text editors really is essential in Linux.

By now, you have certainly realized Linux is packed with choices; when it comes to text editors, there are many choices, ranging from quite simple to very complex, including:

+ `nano`
+ `gedit`
+ `vi`
+ `emacs`.

In this section, we will learn about `nano` and `gedit` editors, which are relatively simple and easy to learn. Before we start, let's take a look at some cases where an editor is not needed.

![image][img1]

## Creating Files Without Using an Editor
Sometimes, you may want to create a short file and don't want to bother invoking a full text editor. In addition, doing so can be quite useful when used from within scripts, even when creating longer files. You will no doubt find yourself using this method when you start on the later chapters that cover __bash__ scripting!

If you want to create a file without using an editor, there are two standard ways to create one from the command line and fill it with content.

The first is to use echo repeatedly:
```
$ echo line one > myfile
$ echo line two >> myfile
$ echo line three >> myfile
```
Earlier, we learned that a single greater-than sign (`>`) will send the output of a command to a file. Two greater-than signs (`>>`) will append new output to an existing file.

The second way is to use cat combined with redirection:
```
$ cat << EOF > myfile
> line one
> line two
> line three
> EOF
$
```
Both the above techniques produce a file with the following lines in it:
```
line one
line two
line three
```
and are extremely useful when employed by scripts.

## nano and gedit
There are some text editors that are pretty obvious; they require no particular experience to learn and are actually quite capable, if not robust. A particularly easy to use one is the text-terminal based editor __nano__. Just invoke `nano` by giving a file name as an argument. All the help you need is displayed at the bottom of the screen, and you should be able to proceed without any problem.

As a graphical editor, `gedit` is part of the __GNOME__ desktop system (`kwrite` is associated with __KDE__). The `gedit` and `kwrite` editors are very easy to use and are extremely capable. They are also very configurable. They look a lot like `Notepad` in __Windows__. Other variants such as `kate` are also supported by __KDE__.

## nano
__nano__ is easy to use, and requires very little effort to learn. To open a file in nano, type `nano <filename>` and press Enter.  If the file does not exist, it will be created.

`nano` provides a two line “shortcut bar” at the bottom of the screen that lists the available commands. Some of these commands are:

+ `CTRL-G`: Display the help screen
+ `CTRL-O`: Write to a file
+ `CTRL-X`: Exit a file
+ `CTRL-R`: Insert contents from another file to the current buffer
+ `CTRL-C`: Cancels previous commands.

![image][img2]

## gedit
__gedit__ (pronounced 'g-edit') is a simple-to-use graphical editor that can only be run within a __Graphical Desktop environment__. It is visually quite similar to the __Notepad__ text editor in __Windows__, but is actually far more capable and very configurable and has a wealth of plugins available to extend its capabilities further.

To open a new file in gedit, find the program in your desktop's menu system, or from the command line type `gedit <filename>`.  If the file does not exist, it will be created.

Using gedit is pretty straight-forward and does not require much training. Its interface is composed of quite familiar elements.

![image][img3]

## Lab 1: Using nano
Using `nano`, we are going to create a file named `myname.txt`, and have it include your name on the first line, and the current date on the last line. To do this:

1. Start nano by typing `nano myfile.txt`.
2. Add your name in the first line of the file.
3. Add the date in the last line of the file.
4. Close the file.

## Lab 2: Using gedit
Using `gedit`, we are going to either create or reuse a file named `myname.txt`, and have it include your street address on the second line and the name of your city on the last line:

1. Start gedit by typing `gedit myfile.txt`.
2. Add your street address  in the second line of the file.
3. Add the name of your city on the last line of the file.
4. Close the file.


# Section 2: More Advanced Editors: vi and emacs
## vi and emacs
Developers and administrators experienced in working on UNIX-like systems almost always use one of the two venerable editing options: `vi` and `emacs`. Both are present or easily available on all distributions and are completely compatible with the versions available on other operating systems.

Both `vi` and `emacs` have a basic purely text-based form that can run in a non-graphical environment. They also have one or more graphical interface forms with extended capabilities; these may be friendlier for a less experienced user. While `vi` and `emacs` can have significantly steep learning curves for new users, they are extremely efficient when one has learned how to use them.

You need to be aware that fights among seasoned users over which editor is better can be quite intense and are often described as a holy war.

## Introduction to vi
Usually, the actual program installed on your system is `vim`, which stands for __vi Improved__, and is aliased to the name `vi`. The name is pronounced as “vee-eye”.

Even if you do not want to use `vi`, it is good to gain some familiarity with it: it is a standard tool installed on virtually all Linux distributions. Indeed, there may be times where there is no other editor available on the system.

__GNOME__ extends `vi` with a very graphical interface known as `gvim` and __KDE__ offers `kvim`. Either of these may be easier to use at first.

When using `vi`, all commands are entered through the keyboard; you do not need to keep moving your hands to use a pointer device such as a mouse or touchpad, unless you want to do so when using one of the graphical versions of the editor.

## vimtutor
Typing `vimtutor` launches a short but very comprehensive tutorial for those who want to learn their first `vi` commands. This tutorial is a good place to start learning `vi`. Even though it provides only an introduction and just seven lessons, it has enough material to make you a very proficient `vi` user, because it covers a large number of commands. After learning these basic ones, you can look up new tricks to incorporate into your list of vi commands because there are always more optimal ways to do things in vi with less typing.

![image][img4]

## Modes in vi
`vi` provides three modes, as described in the table below. It is vital to not lose track of which mode you are in. Many keystrokes and commands behave quite differently in different modes.

| Mode | Feature |
|------|---------|
| __Command__ | - By default, vi starts in Command mode.  |
|   | - Each key is an editor command. |
|   | - Keyboard strokes are interpreted as commands that can modify file contents. |
| __Insert__ | - Type `i` to switch to Insert mode from Command mode. |
|   | - Insert mode is used to enter (insert) text into a file. |
|   | - Insert mode is indicated by an “`-- INSERT --`” indicator at the bottom of the screen. |
|   | - Press `Esc` to exit Insert mode and return to Command mode. |
| __Line__ | - Type __`:`__ to switch to the Line mode from Command mode. Each key is an external command, including operations such as writing the file contents to disk or exiting. |
|   | Uses line editing commands inherited from older line editors. Most of these commands are actually no longer used. Some line editing commands are very powerful. |
|   | - Press `Esc` to exit Line mode and return to Command mode. |


## Working with Files in vi
The table describes the most important commands used to start, exit, read, and write files in __vi__. The __ENTER__ key needs to be pressed after all of these commands.

| Command | Usage |
|---------|-------|
| `vi myfile` | Start the vi editor and edit the myfile file |
| `vi -r myfile` | Start vi and edit myfile in recovery mode from a system crash |
| `:r file2` | Read in file2 and insert at current position |
| `:w` | Write to the file |
| `:w myfile` | Write out the file to myfile |
| `:w! file2` | Overwrite file2 |
| `:x` or `:wq` | Exit vi and write out modified file |
| `:q` | Quit vi |
| `:q!` | Quit vi even though modifications have not been saved |


## Changing Cursor Positions in vi
The table describes the most important keystrokes used when changing cursor position in vi. Line mode commands (those following colon (__`:`__)) require the __ENTER__ key to be pressed after the command is typed.

| Key | Usage |
|-----|-------|
| arrow keys | To move up, down, left and right |
| `j` or `<ret>` | To move one line down |
| `k` | To move one line up |
| `h` or `Backspace` | To move one character left |
| `l` or `Space` | To move one character right |
| `0` | To move to beginning of line |
| `$` | To move to end of line |
| `w` | To move to beginning of next word |
| `:0` or `1G` | To move to beginning of file |
| `:n` or `nG` | To move to line n |
| `:$` or `G` | To move to last line in file |
| `CTRL-F` or `Page Down` | To move forward one page |
| `CTRL-B` or `Page Up` | To move backward one page |
| `^l` | To refresh and center screen |

## Using Modes and Cursor Movements in vi
Click below to view a demonstration on how to use Modes and Cursor Movements in the __vim__ editor.

[video][vid1]

## Searching for Text in vi
The table describes the most important commands used when searching for text in __vi__. The ENTER key should be pressed after typing the search pattern.

| Command | Usage |
|---------|-------|
| `/pattern` | Search forward for pattern |
| `?pattern` | Search backward for pattern |

The table describes the most important keystrokes used when searching for text in vi.

| Key | Usage |
|-----|-------|
| `n` | Move to next occurrence of search pattern |
| `N` | Move to previous occurrence of search pattern |

## Working with Text in vi
The table describes the most important keystrokes used when changing, adding, and deleting text in vi.

Click the link below to download a consolidated PDF file with commands for vi.

[commands for vi][vicmd]

| Key | Usage |
|-----|-------|
| `a` | Append text after cursor; stop upon `Escape` key |
| `A` | Append text at end of current line; stop upon `Escape` key |
| `i` | Insert text before cursor; stop upon `Escape` key |
| `I` | Insert text at beginning of current line; stop upon `Escape` key |
| `o` | Start a new line below current line, insert text there; stop upon `Escape` key |
| `O` | Start a new line above current line, insert text there; stop upon `Escape` key |
| `r` | Replace character at current position |
| `R` | Replace text starting with current position; stop upon `Escape` key |
| `x` | Delete character at current position |
| `Nx` | Delete N characters, starting at current position |
| `dw` | Delete the word at the current position |
| `D` | Delete the rest of the current line |
| `dd` | Delete the current line |
| `Ndd` or `dNd` | Delete N lines |
| `u` | Undo the previous operation |
| `yy` | Yank (copy) the current line and put it in buffer |
| `Nyy` or `yNy` | Yank (copy) N lines and put it in buffer |
| `p` | Paste at the current position the yanked line or lines from the buffer |

## Using External Commands, Saving, and Closing in the vi Editor
Click below to view a demonstration on how to use External commands, Saving, and Closing in the __vi__ editor.

[vido][vid2]

## Using External Commands
Typing `: sh command` opens an external command shell. When you exit the shell, you will resume your __vi__ editing session.

Typing `:!command` executes a command from within __vi__. The command follows the exclamation point. This technique is best suited for non-interactive commands, such as `: ! wc %`. Typing this will run the `wc` (word count) command on the file; the character `%` represents the file currently being edited.

![image][img5]

## Introduction to emacs
The __emacs__ editor is a popular competitor for __vi__. Unlike __vi__, it does not work with modes. __emacs__ is highly customizable and includes a large number of features. It was initially designed for use on a console, but was soon adapted to work with a GUI as well. __emacs__ has many other capabilities other than simple text editing; it can be used for email, debugging, etc.

Rather than having different modes for command and insert, like __vi__, __emacs__ uses the `CTRL` and __Meta__ (`Alt` or `Esc`) keys for special commands.

![image][img6]


## Working with emacs
The table lists some of the most important key combinations that are used when starting, exiting, reading, and writing files in __emacs__.

| Key` | Usage |
|------|-------|
| `emacs myfile` | Start emacs and edit myfile |
| `CTRL-x i` | Insert prompted for file at current position |
| `CTRL-x s` | Save all files |
| `CTRL-x CTRL-w` | Write to the file giving a new name when prompted |
| `CTRL-x CTRL-s` | Saves the current file  |
| `CTRL-x CTRL-c` | Exit after being prompted to save any modified files |

## Changing Cursor Positions in emacs
The table lists some of the keys and key combinations that are used for changing cursor positions in emacs.

| Key | Usage |
|-----|-------|
| `arrow keys` | Use the arrow keys for up, down, left and right |
| `CTRL-n` | One line down |
| `CTRL-p` | One line up |
| `CTRL-f` | One character forward/right |
| `CTRL-b` | One character back/left |
| `CTRL-a` | Move to beginning of line |
| `CTRL-e` | Move to end of line |
| `Meta-f` | Move to beginning of next word |
| `Meta-b` | Move back to beginning of preceding word |
| `Meta-<` | Move to beginning of file |
| `Meta-g-g-n` | Move to line n (can also use '`Esc-x Goto-line n`') |
| `Meta->` | Move to end of file |
| `CTRL-v` or `Page Down` | Move forward one page |
| `Meta-v` or `Page Up` | Move backward one page |
| `CTRL-l` | Refresh and center screen |

## Searching for Text in emacs
The table lists the key combinations that are used for searching for text in emacs.

| Key | Usage |
|-----|-------|
| `CTRL-s` | Search forward for prompted pattern, or for next pattern |
| `CTRL-r` | Search backwards for prompted pattern, or for next pattern |

## Working with Text in emacs
The table lists some of the key combinations used for changing, adding, and deleting text in emacs:

| Key | Usage |
|-----|-------|
| `CTRL-o` | Insert a blank line |
| `CTRL-d` | Delete character at current position |
| `CTRL-k` | Delete the rest of the current line |
| `CTRL-_` | Undo the previous operation |
| `CTRL-` (`space` or `CTRL-@`) | Mark the beginning of the selected  |region. The end will be at the cursor position
| `CTRL-w` | Delete the current marked text and write it to the buffer |
| `CTRL-y` | Insert at current cursor location whatever was most recently deleted |

Click the link to download a consolidated PDF file with commands for emacs:

[commands for emacs][emcmd]

## Knowledge Check
1. In the vim editor, which command is used to launch the tutorial?

        Explanation
        The vimtutor command is used to launch the tutorial in the vim editor.

2. Which of the following is used to exit emacs after prompting to save all modified files?

        A. CTRL-x c
        B. CTRL-x s
        C. CTRL-x CTRL-s
        D. CTRL-x CTRL-c

        Ans: D
        Explanation
        The CTRL-x CTRL-c is used to exit emacs after prompting to save all modified files.

## Lab 3: vi and emacs Tutorials
There is no shortage of online tutorials on the use of the basic editors available.

For __emacs__, it is as simple as starting the program (you do not even have to give a file name) and then typing `Ctl-h` and then `t`. This will launch the built-in emacs tutorial.

An excellent interactive __vi__ tutorial can be found at `www.openvim.com`.

You should take some time to familiarize yourself with these tutorials.


## Lab 4: Working with vi
You will need to become very comfortable with one of the editors widely available on Linux systems. In the following labs, we will concentrate on __vi__, which is on every Linux system and for which every system administrator developer develops at least some ability to use.

We should do similar exercises for __emacs__, which also has a wide user base and has many dedicated fans. However, given the limited amount of time, we recommend you do these labs as homework anyway, and if you are not already proficient with __vi__ or __emacs__, just use __nano__ or __gedit__ or __kedit__ for the course, as these simple editors have virtually no learning curve.

Keep in mind preferences are strong among individual Linux users and administrators. For example, your author finds __vi__ very confusing because of its different modes, and never uses it unless forced to. Perhaps the reason we do not have labs as long for __emacs__ here is your author finds it's much easier and more intuitive to use!

Click the links below to view a solution to the Lab exercises.

[Lab Solution: Navigating in vi][vinav]

[Lab Solution: Editing in vi][viedt]

[Lab Solution: External Commands in vi][viext]

# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ __Text editors__ (rather than word processing programs) are used quite often in Linux, for tasks such as creating or modifying system configuration files, writing scripts, developing source code, etc.
+ __nano__ is an easy-to-use text-based editor that utilizes on-screen prompts.
+ __gedit__ is a graphical editor, very similar to Notepad in Windows.
+ The __vi__ editor is available on all Linux systems and is very widely used. Graphical extension versions of vi are widely available as well.
+ __emacs__ is available on all Linux systems as a popular alternative to vi. emacs can support both a graphical user interface and a text mode interface.
+ To access the __vi tutorial__, type `vimtutor` at a command line window.
+ To access the __emacs tutorial__ type `Ctl-h` and then `t` from within emacs.
+ vi has three modes: __Command__, __Insert__, and __Line__; emacs has only one, but requires use of special keys. such as `Control` and `Escape`.
+ Both editors use various combinations of keystrokes to accomplish tasks; the learning curve to master these can be long, but once mastered using either editor is extremely efficient.


[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008800_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V001700_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002700_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/57bd3f905d0a25d34771843b351ff71a/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch10_screen03.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3b01b04e0ffdfcd2ab8f20ef6f2386f8/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/nano.png
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/739df8236f04571d52f8e387f0dfd50b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/gedit.png
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b1e67aea3546804f69588aab52e97fcb/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/vimtutorubuntu.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1b96ee76e521a7f91666d8df989960d6/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/vicommand.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/09ce664d78eeb53d6290f1460593c4a5/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/emacsubuntu.png

[vicmd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/dd0b84d079c38cca37826462d16a904e/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/VI_Editor.pdf
[emcmd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/2d9f15c41340c037c6bc9f335108994f/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/emacs.pdf
[vinav]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-vi-navigating.html
[viedt]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-vi-editing.html
[viext]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-vi-extcmds.html

