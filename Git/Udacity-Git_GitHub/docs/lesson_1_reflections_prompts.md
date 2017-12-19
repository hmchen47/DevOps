Navigating a Commit History
---------------------------

# Course Overview
Check out [this page](https://www.udacity.com/wiki/ud775/command-line-instructions) for some tutorials to get started using a Unix-style command line.

There's also a [Udacity Unix Command Line Basics course](https://classroom.udacity.com/courses/ud595/lessons/4597278561/concepts/46968695970923) that will get you up to speed in no time!


# Finding Diffs Between Larger Files
## Asteroids Game
If you're interested, you can play the Asteroids game on [Doug's website](http://dougmcinnes.com/html-5-asteroids/).

## Downloading the old and new versions of the file
The two versions of the `game.js` file are - [game_old.js](https://www.udacity.com/api/nodes/2960778928/supplemental_media/game-oldjs/download?_ga=1.32442489.672083044.1467344711) and [game_new.js](https://www.udacity.com/api/nodes/2960778928/supplemental_media/game-newjs/download?_ga=1.34079078.672083044.1467344711). 

When showing the output of running `diff` on Mac, Caroline accidentally showed the output of `diff -u game_new.js game_old.js`, that is, she put the files in the incorrect order. (She showed typing the correct command, but the output shown is from running the command with the arguments reversed). If you've run your command correctly, your output should be the reverse of Caroline's: that is, you should see minus signs where she has plus signs and vice versa.


# Reflection
Like Sarah said, there is a lot of research out there on reflection. If you want a quick intro with some neat graphics, check out [this site](https://sites.google.com/site/reflection4learning/why-reflect).

For a more in-depth look, check out this [seminal 20-page paper](http://184.182.233.150/rid=1LW06D9V6-26428MK-1Z64/Mezirow's%20chapter,%20How%20Critical%20Refletion%20Triggers%20TL.pdf) on the topic.

+ How did viewing a diff between two versions of a file help you see the bug that was introduced?
    + Windows: `fc file1 file2`
    + Linux/Mac: `diff file1 file2`

+ How could having easy access to the entire history of a file make you a more efficient programmer in the long term?
    version control

+ What do you think are the pros and cons of manually choosing when to create a commit, like you do in Git, vs having versions automatically saved, like Google docs does?
    + manually - meanful
    + automatically - prevent from gorgetting

+ Why do you think some version control systems, like Git, allow saving multiple files in one commit, while others, like Google Docs, treat each file separately?
    These files are most likely related.  Therefore, commit them together will provide meaningful records.  

+ How can you use the commands git log and git diff to view the history of files?
    + `git log` --> viewing the committed versions and their ID
    + `git diff first_id second_id` --> list the difference of these two commits
    + `git config --global color.ui auto` --> change default color setting

+ How might using version control make you more confident to make changes that could break something?
    + `git log` --> find the appropriate commit from the comments and its ID
    + `git checkout ID` <-- go to the committed ID

+ Now that you have your workspace set up, what do you want to try using Git for?
    + edit my code


# [Reflect: Using diff to Find Bugs](https://www.udacity.com/course/viewer#!/c-ud775/l-2980038599/m-2997518619)
## Make sure you can access the command line
If you are on Windows, you’ll need to install some software in order to use a unix-like command line (different from the Windows built-in Command Prompt), as we mentioned previously. For more info, [check out this page](https://www.udacity.com/wiki/ud775/command-line-instructions#windows-users).

## Choose a text editor
As noted in the previous video, you should make sure to use a simple text editor like [Notepad++](http://notepad-plus-plus.org/), [Sublime](http://www.sublimetext.com/3), [Atom](https://atom.io/), emacs, vim, etc. and not a rich-text editor like Microsoft Word or OpenOffice, so that you can easily look at your files' content on the command line.

If you don’t have one that you like yet, `Sublime` is a good option that will work on Windows, Mac, and Linux. We have provided more detailed instructions for setting up Sublime than for other editors, and we use Sublime for all the examples in the course. You can download `Sublime` [here](http://www.sublimetext.com/3).

## Make sure you can launch your editor from the command line
It will be helpful to be able to launch your text editor from the command line. See here for instructions on how to do this for Sublime. If you have trouble getting this working, videos at the end of the lesson called "Setting up Your Workspace on Windows" and "Setting Up Your Workspace on Mac" will demonstrate this process, so you can wait until then.

## Set up your course workspace
Right now, you should create a `version-control` directory (a more computer-science-y term for “folder”) to hold all your files for this course in an easy to remember location, then create a `reflections` sub-directory, and within that, create a plain text file called `lesson_1_reflections.txt` for the questions from this lesson.

You can do this by running the following commands in either Git Bash or the terminal (the bits after the # signs are comments, anything after those are not interpreted):

``` bash
cd ~                          # change directories to your home directory
mkdir version-control         # make version-control directory
cd version-control            # go to version-control directory
mkdir reflections             # create reflections directory
cd reflections                # go to reflections directory
subl lesson_1_reflections.txt # launch sublime with file called lesson_1_reflections.txt (you can replace subl with another editor here if you prefer a different one)
```

If you prefer, rather than creating the file from scratch, you could download the [lesson_1_reflections_prompts.txt](https://www.udacity.com/api/nodes/2997518619/supplemental_media/lesson-1-reflection-promptstxt/download) file from the Downloadables section, place it in the `reflections` directory and rename it, then add your response after the first prompt.

Once you’ve saved your file, if you want to double-check that everything has gone as planned, try these commands:

```bash
pwd # print working directory - shows what directory you are in
ls  # list the files in this directory
```

If you're having trouble getting this working, videos at the end of the lesson called "Setting up Your Workspace on Windows" and "Setting Up Your Workspace on Mac" will demonstrate parts of this process, so you might want to wait until then. In the mean time, you can create the directories and file using your OS’s Graphical Interface for working with files (Finder, Windows Explorer, etc). It's good to get some practice using the command line, though, since we'll be using it a lot in this course, so once you've watched the workspace instructions, make sure you can complete actions like this on the command line.

You are also welcome to use a different naming scheme, but later in the course we will refer to this file structure and it will be up to you to translate to whatever naming scheme you chose instead!

## Use short lines
Many command line tools, including Git, are less useful if your files contain very long lines. For example, if you use `diff` to compare two files that have all their content on the same line, `diff` will only show you that the two files are different. It will not be able to pinpoint the location of the difference for you.

For this reason, it is a good idea to make sure you keep your lines reasonably short when writing your reflections (or other plain-text files). The exact limit is a matter of personal preference. Many developers use a max line length of 80 to 120 characters. Some editors can automatically insert line breaks for you, but for others, like Sublime, you will need to remember to press enter when you want to create a new line.

## Do the first reflection exercise
Populate `lesson_1_reflections.txt` with the following question and your thoughts on it:
    __How did viewing a diff between two versions of a file help you see the bug that was introduced?__

When you've created your document, written down your thoughts, and saved the file, click "Next" to learn about some systems that can help you create these versions of your files.
    Like Sarah said, there is a lot of research out there on reflection. If you want a quick intro with some neat graphics, check out [this site](https://sites.google.com/site/reflection4learning/why-reflect).
    
    For a more in-depth look, check out [this seminal 20-page paper](http://184.182.233.150/rid=1LW06D9V6-26428MK-1Z64/Mezirow's%20chapter,%20How%20Critical%20Refletion%20Triggers%20TL.pdf) on the topic.

Populate `lesson_1_reflections.txt` with the following question and your thoughts on it:
    __How did viewing a diff between two versions of a file help you see the bug that was introduced?__


# Reflect: Using History for Efficiency
Now that you've learned about some version control systems, and how they can help you save the history of a file, go add the following question and your thoughts on it to your reflections file:
    __How could having easy access to the entire history of a file make you a more efficient programmer in the long term?__


# Concept Map: diff
Now that you know about `git diff`, you can add it to the concept map.

## Previous version
First, let’s look at the original map:
[!Original Concept Map](https://lh4.ggpht.com/3NnbttO-b4oJKwGdQmGWL-bzrZx7IXECjkIKPRTZ6UeRa04VCQBq01867CCC2e3AeMJMmmh71aCio33fAEA=s450)

## New addition
Remember that we are trying to avoid cluttering up our map, so try to only add relationships that would not be implied by other relationships already on the map.

If you were to put "git diff" on the map, which of the following existing concept(s) would you directly connect it with?
+ commit
+ Google Docs
+ git
+ Version Control


# [How Often to Commit](https://www.udacity.com/course/viewer#!/c-ud775/l-2980038599/e-2419878582/m-2438328585)
Since you can choose when to make a commit, you might be wondering how often to commit your changes. It's usually a good idea to keep commits small. As the diff between two versions gets bigger, it gets harder to understand and less useful. However, you don’t want to make your commits too small either. If you always save a commit every time you change a line of code, your history will be harder to read since it will have a huge number of commits over a short time period.

A good rule of thumb is to __make one commit per logical change__. For example, if you fixed a typo, then fixed a bug in a separate part of the file, you should use one commit for each change since they are logically separate. If you do this, each commit will have one purpose that can be easily understood. Git allows you to write a short message explaining what was changed in each commit, and that message will be more useful if each commit has a single logical change.

# Commit Size Quiz
To get some practice thinking about how often to commit, on the next screen, mark whether you think the following would be good commit sizes. If not, indicate whether you think this commit is too small and you’d like to wait and commit later, or whether you think it’s too big and you would have committed earlier. This is subjective, so there aren’t any definite right or wrong answers, but just choose the answer you think is best in each case.
+ You commit all the changes required to add a new feature, which you’ve been working on for a week. You haven’t committed since you started working on it.
+ You find three typos in your README. You fix and commit the first.
+ You commit all the changes required to add a new feature, which you’ve been working on for an hour.
+ You fix two small bugs in different functions and commit them both at once.

## One Commit per `Logical Change` Solution
+ You commit all the changes required to add a new feature, which you’ve been working on for a week. You haven’t committed since you started working on it.
    This commit seems _too big_. It's easier to understand what each commit does if each only does one thing and is fairly small. Going a week without committing is not the best idea.

+ You found three typos in your README. You fix and commit the first.
    This commit seems _too small_. It would be better to fix all three typos, then commit. That way, your history won't get too cluttered with typo fixes. Plus, you don’t need to worry about introducing bugs to a README, so bundling changes together is more likely to be a good idea.

+ You commit all the changes required to add a new feature, which you’ve been working on for an hour.
    This is probably a _good size_ for a commit. All the work is on a single feature, so the commit will have a clear logical purpose. After an hour, the diff will probably have a fair amount of content in it, but not too much to understand.

    On the other hand, sometimes after working for an hour you’ll have run into more than one natural committing point, in which case you would want to break the feature up into smaller commits. Because of this, “too big” could also be a reasonable answer here.

+ You fix two small bugs in different functions and commit them both at once.
    This commit is probably _too big_. It would have been better to commit after the first bug fix, since the two bug fixes aren't related to each other.

## Judgment Call
Choosing when to commit is a judgment call, and it's not always cut-and-dried. When choosing whether to commit, just keep in mind that each commit should have one clear, logical purpose, and you should never do too much work without committing.

## What is a README?
Many projects contain a file named "README" that gives a general description of what the project does and how to use it. It's often a good idea to read this file before doing anything with the project, so the file is given this name to make users more likely to read it.


# Reflect: Manual Commits
Now you've learned about Git commits and thought about good times to create commits, go add the following question and your thoughts on it to your reflections file:
    __What do you think are the pros and cons of manually choosing when to create a commit, like you do in Git, vs having versions automatically saved, like Google Docs does?__

+ In _competition style coding_, you might use multiple files to solve a problem, or the problems might have some interdependencies.
  But if the problems were unrelated and each could be solved in a single file, you would want to track them separately.
+ Different chapters of a novel might be fairly independent, so it’s possible you would want to track them separately. But what if you wanted to make sure the transitions between chapters were smooth? Or what if you wanted to rename a character?


# Reflect: Multi-File Commits
Go add the following question and your thoughts on it to your reflections file:
    __Why do you think some version control systems, like Git, allow saving multiple files in one commit, while others, like Google Docs, treat each file separately?__


# [Installing Git](https://www.udacity.com/course/viewer#!/c-ud775/l-2980038599/m-2473698566)
Now we’re going to give you a chance to use Git and practice these commands on the Asteroids repository yourself. To do that, you’ll need to install Git. If you already have Git installed, check its version using the command `git --version`. If you have at least version 1.8, you can continue to the next video. Otherwise, we highly recommend upgrading, since Git added a lot of new features in version 1.8 and we will be assuming you have it.

If you haven’t already installed Git, or if you need to upgrade, go ahead and do so now by following the instructions here: https://git-scm.com/downloads

If you run into any problems, please post about them in the forums. Once you have Git installed, click “Next” and Caroline will walk you through how to download the Asteroids repository.


# [Cloning and Exploring The Repo](https://www.udacity.com/course/viewer#!/c-ud775/l-2980038599/e-2960778944/m-2960778945)
## Cloning a Repository
To clone a repository, run `git clone` followed by a space and the repository URL.

## Asteroids URL
Use the following url to clone the [Asteroids repository](https://github.com/udacity/asteroids.git)

## Exiting `git log`
To stop viewing `git log` output, press `q` (which stands for quit).

## Getting Colored Output
To get colored diff output, run `git config --global color.ui auto`

## Copying and Pasting from the Command Line
To complete this quiz, you'll want to copy and paste some commit ids.

+ Windows 
    To copy and paste within Git Bash, follow the instructions on [this page](https://www.udacity.com/wiki/ud775/git-bash-copy-paste).
+ Mac 
    To copy and paste within the terminal on Mac, use `Cmd+C` and `Cmd+V`
+ Ubuntu 
    To copy and paste within the terminal on Ubuntu, use `Ctrl+Shift+C` and `Ctrl+Shift+V`.

# Using `git log` and `git diff`
As a reminder, running 'git log' will show a list of the recent commits with information about them, including commit IDs. Running 'git diff' followed by two commit IDs will compare the two versions of the code in those commits. If you need a refresher, you may want to rewatch [this video](https://classroom.udacity.com/courses/ud775/lessons/2980038599/concepts/29607789370923).

## Entering commit IDs
If it is easier, you may enter the first four or more characters of the commit ID rather than pasting the entire ID.

[Git Errors and Warnings](https://www.udacity.com/course/viewer#!/c-ud775/l-2980038599/e-2993748573/m-2952808956)

[Checking Out Old Versions of Code](https://www.udacity.com/course/viewer#!/c-ud775/l-2980038599/e-2960778952/m-2960778953)


# Reflect: Using Git to View History
Now that you've had some experience using Git yourself, go add the following question and your thoughts on it to your reflections file:
    __How can you use the commands git log and git diff to view the history of files?__


# Concept Map: Repository, Clone, Log
Check each concept you think `log` should be connected to. For each concept you check, write the connection type ("type-of", "part-of", or "operates-on") you think applies in the box next to it. If none of the existing connection types work, write "other".


# Git Errors and Warnings Solution
+ Should not be doing an octopus
    Octopus is a strategy Git uses to combine many different versions of code together. This message can appear if you try to use this strategy in an inappropriate situation.

+ You are in 'detached HEAD' state
    HEAD is what Git calls the commit you are currently on. You can “detach” the HEAD by switching to a previous commit, which we’ll see in the next video. Despite what it sounds like, it’s actually not a bad thing to detach the HEAD. Git just warns you so that you’ll realize you’re doing it.

+ Panic! (the 'impossible' happened)
    This is a real error message, but it’s not output by Git. Instead it’s output by GHC, the compiler for a programming language called Haskell. It’s reserved for particularly surprising errors!


# Checking Out Old Versions Of Code
You can download the troubleshooting_guide.pdf [here](https://www.udacity.com/api/nodes/2960778953/supplemental_media/troubleshooting-guidepdf/download?_ga=1.71397332.672083044.1467344711).

## QuickEdit Mode
To make copying and pasting in GitBash easier by turning on QuickEdit mode, follow the instructions [here](https://www.udacity.com/wiki/ud775/git-bash-copy-paste).

## Most Recent Commit
The commit ID of the most recent commit is 3884eab839af1e82c44267484cf2945a766081f3. You can use this commit ID to return to the latest commit after checking out an older commit.

## Format of `git checkout`
The command Caroline types to checkout the "Revert controls" commit is `git checkout b0678b161fcf74467ed3a63110557e3d6229cfa6`.

## Windows Explorer
When Caroline mentions opening a "file navigation GUI" on Windows, she is referring to the Windows Explorer.

## Entering commit IDs
If it is easier, you may enter the first four or more characters of the commit ID rather than pasting the entire ID.

## Most Recent Commit
The commit ID of the most recent commit is `3884eab839af1e82c44267484cf2945a766081f3`. You can use this commit ID to return to the latest commit after checking out an older commit.


# Reflect: Confidence from Version Control
Now that you know how to return to a previous version of your files using Git, go add the following question and your thoughts on it to your reflections file:
    __How might using version control make you more confident to make changes that could break something?__


# Setting Up Your Workspace On Windows
You can download `.bash_profile_course` [here](https://www.udacity.com/api/nodes/3341718587/supplemental_media/bash-profile-course/download?_ga=1.37232743.672083044.1467344711).

## Setting Up Your Workspace on Windows
https://www.udacity.com/course/viewer#!/c-ud775/l-2980038599/m-3341718587

## Changing background color
If you prefer the background color of `Git Bash` to be something other than black, you can change it in the "Defaults" menu under the "Colors" tab. If you like the background color as-is, you don't need to make any changes.

## Downloading necessary files
+ Save [this file](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash) in your home directory with the name `git-completion.bash`.
+ Save [this file](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh) in your home directory with the name `git-prompt.sh`.
+ Download `bash_profile_course` from the Downloadables section.
  If you already have a file in your home directory named `.bash_profile`, copy the content from `bash_profile_course` and paste it at the bottom of `.bash_profile`. Otherwise, move `bash_profile_course` to your home directory and rename it to `.bash_profile`. (If you're curious to learn more about how bash prompts work, see [this page](http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html).)

## Making Git configurations
Run the following Git configuration commands. The first one will need to be modified if you are using a text editor other than Sublime, or if Sublime is installed in another location for you. See [this page](https://help.github.com/articles/associating-text-editors-with-git/) for the correct command for a couple of other popular text editors. For any other editor, you'll need to enter the command you use to launch that editor from Git Bash.

```bash
    git config --global core.editor "'C:/Program Files/Sublime Text 2/sublime_text.exe' -n -w"
    git config --global push.default upstream
    git config --global merge.conflictstyle diff3
```
Make sure you can start your editor from Git Bash

If you use Sublime, you can do this by adding the following line to your `.bash_profile`:
    `alias subl="C:/Program\ Files/Sublime\ Text\ 2/sublime_text.exe"`

## Restart Git Bash
You'll need to close and re-open Git Bash before all your changes take effect.


# Setting Up Your Workspace On Mac
## Downloading necessary files
+ Save [this file](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash) in your home directory with the name `git-completion.bash`.
+ Save [this file](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh) in your home directory with the name `git-prompt.sh`.
+ Download `bash_profile_course` [here](https://www.udacity.com/api/nodes/3341718587/supplemental_media/bash-profile-course/download?_ga=1.37232743.672083044.1467344711).
  If you already have a file in your home directory named .bash_profile, copy the content from `bash_profile_course` and paste it at the bottom of `.bash_profile`. Otherwise, move `bash_profile_course` to your home directory and rename it to `.bash_profile`. If you use Linux, you may need to name this file `.bashrc` instead of `.bash_profile`. (If you're curious to learn more about how bash prompts work, see [this page](http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html).)

## Make sure you can start your editor from the terminal
If you use `Sublime`, you can do this by add the following line to your `.bash_profile` (you may need to change the path if Sublime is installed in a different location for you):
    __alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"__

## Making Git configurations
Run the following Git configuration commands. The first one will need to be modified if you are using a text editor other than `Sublime`, or if `Sublime` is installed in another location for you. See this page for the correct command for a couple of other popular text editors. For any other editor, you'll need to enter the command you use to launch that editor from the terminal.

```bash
git config --global core.editor "'/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl' -n -w"
git config --global push.default upstream
git config --global merge.conflictstyle diff3
```
(Instead of the first command, you may be able to use the simpler `git config --global core.editor "subl -n -w"` as shown in the video, but many students have found this does not work for them.)

## Restart the terminal
You'll need to close and re-open the terminal before all your changes take effect.


# Reflect: How Do You Want to Use Git?
Go add the following question and your thoughts on it to your reflections file:
    __Now that you have your workspace set up, what do you want to try using Git for?__


# Gitbash on Windows
## QuickEdit Mode
To make copying and pasting in GitBash easier by turning on `QuickEdit` mode, follow the instructions here.

## Most Recent Commit
The commit ID of the most recent commit is `3884eab839af1e82c44267484cf2945a766081f3`. You can use this commit ID to return to the latest commit after checking out an older commit.

## Format of `git checkout`
The command Caroline types to checkout the "Revert controls" commit is `git checkout b0678b161fcf74467ed3a63110557e3d6229cfa6`.

## Windows Explorer
When Caroline mentions opening a "file navigation GUI" on Windows, she is referring to the Windows Explorer.

## Entering commit IDs
If it is easier, you may enter the first four or more characters of the commit ID rather than pasting the entire ID.


## Tracking versions using Git
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3449338567/m-3419258939

You would be able to see the difference between the two versions, but you would no longer be able to directly access the old version.

This is false. You could still access the old version of the file by checking out the commit associated with that version. Then the recipe would temporarily revert to its state at the time that commit was made. 

Using `git diff` to compare the two versions would show the same changes as `diff -u` did in the previous exercise.

This is true. `diff -u` and `git diff` show very similar outputs. Even if the exact format was slightly different, the actual changes indicated would be the same. 

Q: The name of the file would change when you saved a second version in Git.

Ans: This is false. The name of the file would remain the same. Git does not rename files when you save a new commit. Instead, Git uses the commit IDs to refer to different versions of the files, and you can use git checkout to access old versions of your files. 

Q: To save two versions of the file, you would create two commits.

Ans: This is true. Commits are Git's way of saving versions, so to save two different versions, you would create two commits.


# Git command review
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3381678812/m-3423338650

Q: Compare two commits, printing each line that is present in one commit but not the other.

Ans: `git diff` will do this. It takes two arguments - the two commit ids to compare. 

Q: Make a copy of an entire Git repository, including the history, onto your own computer.

Ans: `git clone` will do this. It takes one argument - the url of the repository to copy. 

Q: Temporarily reset all files in a directory to their state at the time of a specific commit.

Ans: `git checkout` will do this. It takes one argument - the commit ID to restore. 

Q: Show the commits made in this repository, starting with the most recent.

Ans: `git log` will do this. It doesn't take any arguments.


# Behavior of git clone
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3450848635/m-3397019070

Q: If someone else gives you the location of their directory or repository, you can copy or clone it to your own computer.

A:  This is _true_ for both copying a directory and cloning a repository.

    As you saw in the previous lesson, if you have a URL to a repository, you can copy it to your computer using `git clone`.

    For copying a directory, you weren't expected to know this, but it is possible to copy a directory from one computer to another using the command scp, which stands for "secure copy". The name was chosen because the scp command lets you securely copy a directory from one computer to another. 

Q: The history of changes to the directory or repository is copied.

A: This is _true_ for cloning a repository, but not for copying a directory. The main reason to use git clone rather than copying the directory is because git clone will also copy the commit history of the repository. However, copying can be done on any directory, whereas git clone only works on a Git repository. 

Q: If you make changes to the copied directory or cloned repository, the original will not change.

A: This is _true_ for both copying a directory and cloning a repository. In both cases, you're making a copy that you can alter without changing the original. 

Q: The state of every file in the directory or repository is copied.

A: This is _true_ for both copying a directory and cloning a repository. In both cases, all the files are copied.


# Behavior of `git log`
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3433848834/m-3449268633

`git log` lists the most recent commit first, as you can verify by checking the commit dates. The middle commit probably contains the code for the mute button, since the commit message indicates that the mute button was added in that commit. The top commit also probably contain the mute button, since that commit is more recent and nothing suggests the mute button has been removed. The bottom commit probably does not contain the mute button, since that commit was created before the commit that added the mute button.

To summarize:

commit 7be5a12f1567866b0d77ccdf2055d1a33831da78 (the top commit listed)

Yes, probably contains the mute button.

commit 06d72e1f95f046002ec46f41cf71957227111141 (the middle commit listed)

Yes, probably contains the mute button.

commit 3d4d45b246aad6a1cd0afaf7cfae26966110727e (the bottom commit listed)

No, probably does not contain the mute button.

git log output

For reference, here is the git log output again:
```s
commit 7be5a12f1567866b0d77ccdf2055d1a33831da78
Author: Ellison Leão <el@gmail.com>
Date:   Fri Jul 11 12:56:26 2014 -0300

    Add sound for the wing.

commit 06d72e1f95f046002ec46f41cf71957227111141
Author: Ellison Leão <el@gmail.com>
Date:   Wed Jul 9 23:42:55 2014 -0300

    Add mute button.

commit 3d4d45b246aad6a1cd0afaf7cfae26966110727e
Author: Ellison Leão <el@gmail.com>
Date:   Mon Jul 7 17:35:47 2014 -0300

    Fix leaderboard button
```

# Behavior of `git diff`
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3449118607/m-3410149165

The middle commit, 06d72e, is the first commit with the mute button, so comparing that commit and the previous commit, 3d4d45, would show the changes that add the mute button.

In order for the changes adding the mute button to be shown as additions, the commit with the mute button needs to be the second argument to `git diff`. That is because `git diff` considers the first argument as the "original", and the second argument as the "new" version, so additions are lines present in the second argument but not the first.

Thus, the last command listed, `git diff 3d4d45 06d72e`, is correct, and would show the mute button lines as additions. Reversing the arguments and running `git diff 06d72e 3d4d45` would instead show the mute button lines as deletions.



# Behavior of `git checkout`
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3369359474/m-3411528756

Q: Checking out an earlier commit will change the state of at least one file.

Ans: This is _sometimes true_. Git doesn't allow you to save a new commit if no files have been updated, so you might think this is always true. However, it's possible to do the following:
+ Save a commit (call this commit 1).
+ Update some files and save another commit (call this commit 2).
+ Change all the files back to their state during commit 1, then save again (call this commit 3).
    
This sometimes happens if commit 2 contained a bug, and it's important to fix the bug quickly. The easiest thing to do might be to remove all the changes introduced by commit 2 to fix the bug, then figure out how to safely reintroduce the changes later.

At this point, commit 3 is the latest commit, so if you checkout commit 1, none of the files will be changed. 

Q: Checking out an earlier commit will change the state of more than one file.

Q: Checking out an earlier commit will change the state of every file in the repository.

Ans: Both of these are _sometimes true_. Since each commit tracks the state of all files in the repository, it is possible that checking out an earlier commit will change the state of multiple files, or even all the files in the repository. However, it is possible to save a new commit after changing only one file, so it is possible only one file will change. 


Q: After checking out a commit, the state of all the files in the repository will be from the same point in time.

Ans: This is _always true_. A commit saves a snapshot of all files in the repository at the time the commit was made, so checking out an earlier commit will result in all the files being reverted to their state at the time the commit was made. That is, the files will be in a consistent state.


# New repository introduction
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3426928665/m-3423498893

In the rest of this problem set, you'll be using a new repository to get additional practice viewing history with Git. The process will be similar to the one you went through for the asteroids repository in the previous lesson.

The new repository is also a game, Pappu Pakia, that you can play in your browser, and like in the lesson, you'll be tracking down some bugs in the game by looking through its commit history. As such, don't be surprised if you spot some bugs when you start the game!

## Clone the repository
To get started, clone the repository, which is located at the url https://github.com/udacity/pappu-pakia.git. Then open the file index.htm using your web browser. On the next screen, select the two creators of the game. Their names will be displayed on the initial screen when you open the game.


# Cloning the repository
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3426928665/m-3383589115

You can clone the repository by running git clone https://github.com/udacity/pappu-pakia.git. To open the game in your web browser, follow the same process as in this video.

Q: Creators of the game

Ans: As stated on the initial page of Pappu Pakia, the game was created by Rishabh and Kushagra. Many thanks to Kushagra and Rishabh for creating this awesome game! We made some modifications to the game to create the following exercises, but you can play the original version of their game here.

Q: Strange behavior

If you actually started playing the version of the game that you cloned, you may have noticed some strange behavior. This is expected! You'll look into this behavior further in the next exercise.


# Buggy behavior
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3403578765/m-3435808540

The commit that introduced this bug has the ID 547f4171a82ec6429d002c1acef357aec41d3f17. One way to find this out would have been to run git log, which should have shown that the most recent 4 commits, and their commit ids, were:
```s
    commit fa4c6bade4970c282b3870ad16f1bde8164663a9
    changing flattr link

    commit 708bcce690e5faa5739bd471507c102ea16b77f7
    pressing down arrow wont cause scroll down anymore

    commit 547f4171a82ec6429d002c1acef357aec41d3f17
    refactoring collision detection

    commit 71d52709ddc4066e7a79a1d0a412e43429a0cdeb
    removing old readme
    (This output has been shortened to be easier to read.)
```

Then you could use `git checkout` to examine old commits and see which ones have the bug. You already know the most recent commit, "changing flattr link" has the bug, so you could run `git checkout 708bcce690e5faa5739bd471507c102ea16b77f7` to test the second-most-recent commit . You should find that this commit also has the bug. Next, you'll find the commit "refactoring collision detection" also has the bug, but the commit "removing old readme" does not. That means the commit "refactoring collision detection" with commit ID 547f4171a82ec6429d002c1acef357aec41d3f17, is the one that introduced the bug.



# Examining the buggy commit
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3408798627/m-3406858799

Use Git's history to figure out what changes were introduced in the commit that caused the bug. On the next screen, check any changes that were introduced, and enter the name of the file that was affected.

## Finding and fixing the bug
Now that you know what changes were introduced by the buggy commit, do you have any idea what could have caused the bug? If not, don't worry about it. The answer will be in the solution if you're curious.

Once you've identified the code that caused the bug, obtain a working version of the game. You can do this by either:

Q: Figuring out what caused the bug (or check the solution), and modify the code to fix the bug

Ans: Checking out the commit before the one with the bug. That commit won't contain the most up-to-date version of the code, but for the purposes of the upcoming exercise it won't matter.


# Changes introduced
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3408798627/m-3377159147

To find the lines introduced by the buggy commit, you can use `git diff`. You'll need the ID of the buggy commit, which you just found to be 547f4171a82ec6429d002c1acef357aec41d3f17. Then you'll need the ID of the previous commit, which will be the commit below it in git log. (That's because git log lists the most recent commit first.) That turns out to be 71d52709ddc4066e7a79a1d0a412e43429a0cdeb.

Thus, by running git diff 71d52709ddc4066e7a79a1d0a412e43429a0cdeb 547f4171a82ec6429d002c1acef357aec41d3f17, you can find out that the lines changed by the buggy commit were:
```js
-    return !(
-      bounds1.end_x < bounds2.start_x ||
-      bounds2.end_x < bounds1.start_x ||
-      bounds1.end_y < bounds2.start_y ||
-      bounds2.end_y < bounds1.start_y
-    );
-
+    if (bounds1.end_x < bounds2.start_x) {
+        return true;
+    }
+    if (bounds2.end_x < bounds1.start_x) {
+        return true;
+    }
+    if (bounds1.end_y < bounds2.start_y) {
+        return true;
+    }
+    if (bounds2.end_y < bounds1.start_y) {
+        return true;
+    }
+    return false;
```
This change represents an "or" expression being separated out into several "if" statements. The number of functions did not change, and no variables were renamed.

## File changed

Near the top of the git diff output, you can see the lines
```s
--- a/js/utils.js
+++ b/js/utils.js
```
This indicates that the file changed was `js/utils.js`, that is, the file `utils.js` within the `js` directory.

## What caused the bug
Based on the change that was made, a reasonable guess is that the bug is some sort of logic error - maybe the new version does not return true and false at the correct times.

It turns out that this is correct. The new code has true and false reversed! Even if you weren't sure exactly why the bug was there, congratulations! You tracked down exactly where the bug was introduced, and knew which lines introduced it, without knowing the code base. All you had to know was how to use Git.



# There is a second bug
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3439038623/m-3406808897

Now you should have a version of the code that works much better - your pappu is not flickering across the screen, and there are plenty of obstacles to avoid. However, there is another, harder to see, bug in the code.

During the game, a cluster of berries appears reasonably often. When the pappu hits those berries, it should split into three pappu clones, but instead, nothing seems to happen.

Finding the bug

This time, instead of checking out old versions of the code, just run git log and look at the 10 most recent commits. Based only on the commit messages, which commit do you think is most likely to have introduced this bug? You can't be sure just by reading the messages, but pick the one you think is most likely.



# Identifying the bug
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3439038623/m-3410128686

One reasonable guess is that the commit with message "speeding clones up", that is, commit 003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a, is likely to be the one causing the bug. The bug is related to clones, and this commit changed the behavior of clones, so it seems plausible that this commit caused the bug.

Of course, the most likely-looking commit won't always be the culprit, so you'll always have to take a closer look at the suspicious commit to see if it actually caused the bug. In this case, the commit "speeding up clones" did in fact cause the bug.

Using this strategy of examining the most likely looking commits doesn't always work, but it often does, and it can save a lot of debugging time. This is one of the reasons it's so useful to make one commit per logical change and give each commit a good message - to make it possible to take shortcuts like this!



# Examining the buggy commit
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3440418791/m-3453178597

Again, use Git's history to figure out what changes were introduced in the commit that caused the bug. On the next screen, select the change that was introduced, and enter the name of the file that was affected.

## Finding and fixing the bug
Now that you know what changes were introduced by the buggy commit, do you have any idea what could have caused the bug? If not, don't worry about it. The answer will be in the solution if you're curious.

It's not necessary to obtain a working version of the game for future exercises. However, it can still be nice to verify that you've actually found the bug! You can do this by either:

Q: Figure out what caused the bug (or check the solution), and modify the code to fix the bug.

Check out the commit before the one with the bug. That commit won't contain the most up-to-date version of the code, but it will let you verify that your hunch was correct. (Note: this will not work if you modified the code to fix the last bug.)


# Changes introduced
https://www.udacity.com/course/viewer#!/c-ud775/l-3394248803/e-3440418791/m-3455588748

As before, you can use git diff to find the lines introduced by the buggy commit. Again, you'll need the ID of the buggy commit, which is 003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a, and the ID of the previous commit, which is 746f762e38b5bbb7d0b837464ef6ec3f8ee5bf91.

Thus, by running git diff 746f762e38b5bbb7d0b837464ef6ec3f8ee5bf91 003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a, you can find out that the change made by the buggy commit was:
```js
-      clone.x += utils.randomNumber(5, 10);
-      clone.y += utils.randomNumber(-20, 20);
+      clone.x += utils.randomNumber(500, 1000);
+      clone.y += utils.randomNumber(-2000, 2000);
```
That is, the x and y coordinate of each clone is changed by a larger random amount. This will have the effect of making the clones move more quickly, or speed up, since their positions change more quickly.

File changed

Near the top of the git diff output, you can see the lines:
```s
--- a/js/pappu.js
+++ b/js/pappu.js
```
This indicates that the file changed was js/pappu.js, that is, the file pappu.js in the directory js.

## What caused the bug
Based on the change that was made, one possible bug is that the clones move too quickly - so quickly they have left the screen before you see them. This turns out to be correct. If you change the code to have numbers bigger than the original numbers, but smaller than the new numbers, the clones will move more quickly, but still be visible. Some lines of code that work well are:
```js
clone.x += utils.randomNumber(20, 40);
clone.y += utils.randomNumber(-30, 30);
```
Again, even if you weren't sure exactly why the bug was there, congratulations! You tracked down which lines introduced a bug without knowing the code base, just by using Git.


# Quizzes:
## Old File Plus Diff
### Reconstructing a final file
Suppose you had a file, called `file.txt`, and you made a copy of this file, named it `updated.txt` and made some changes to it. Next, suppose you ran `diff -u file.txt updated.txt`.

The contents of the original file and the output of the diff are below. Given this information, it is possible to reconstruct what the final contents of `updated.txt` must have been. On the next screen, enter these contents.

Contents of original file.txt
A
B
C
D
E
F

These letters are stand-ins for the actual lines of the file. For example, this file could be a recipe, and the lines could be ingredients. Or the file could be a code file, and each letter could stand for a line of code.

Output of diff -u
```s
--- file.txt    2014-12-03 16:27:41.000000000 -0500
+++ updated.txt    2014-12-03 16:28:11.000000000 -0500
@@ -2,4 +2,6 @@
 B
+$
 C
-D
+#
+%
 E
```
Just like the letters, the symbols are stand-ins for actual lines.

### Final file
The contents of updated.txt must have been

A
B
$
C
#
%
E
F
The lines with plus signs in the diff output were added, meaning they were in updated.txt but not file.txt, and the lines with minus signs were removed, meaning they were in file.txt but not updated.txt. Any other lines were unchanged.

Starting from the original file, adding a dollar sign below line B, removing line D, and adding a pound sign and a percent sign above line E gives the file contents shown above.

## Tracking versions using Git
What if instead of saving a new version of the file named `updated.txt`, you had been using Git to track your changes to `file.txt`? On the next screen, select any of the statements that would be true.

Check all the statements that would be true if you tracked changes using Git:
A. You would be able to see the difference between the two versions, but you would no longer be able to directly access the old version.
B. Usybf `git diff` to compare the two versions would show the same changes as `diff -u` did in th eprevious exercise.
C. The name of the file would change when you saved a second version of Git.
D. To save two versions of the file, you would create two commits.

Ans: B, D

Ans: 
A. This is _false_. You could still access the old version of the file by checking out the commit associated with that version. Then the recipe would temporarily revert to its state at the time that commit was made. 

B. This is _true_. `diff -u` and `git diff` show very similar outputs. Even if the exact format was slightly different, the actual changes indicated would be the same. 

C. This is _false_. The name of the file would remain the same. Git does not rename files when you save a new commit. Instead, Git uses the commit IDs to refer to different versions of the files, and you can use git checkout to access old versions of your files. 

D. This is _true_. Commits are Git's way of saving versions, so to save two different versions, you would create two commits.


## Git command review
You learned four Git commands in the previous lesson. Each of the four actions on the next screen can be completed using one of the Git commands you learned. For each action, type the Git command you would use to complete that action.

A .Compare two commits, printing each line that is present in one commit but not the other.
B. Make a copy of an entire Git repository, including the history, onto your own computer.
C. Temporarily reset all files in a directory to their state at the time of a specific commit.
D. Show the commits made in this repository, starting with the most recent.

Ans: 
A. `git diff` will do this. It takes two arguments - the two commit ids to compare. 
B. `git clone` will do this. It takes one argument - the url of the repository to copy. 
C. `git checkout` will do this. It takes one argument - the commit ID to restore. 
D. `git log` will do this. It doesn't take any arguments.


## Behavior of git clone
For each of the statement on the next screen, select whether it is true if you clone a Git repository, if you copy a directory that is not being tracked using Git, or if it is true in both cases.

A. If someone else gives you the location of their directory or repository, you can copy or clone it to your own computer.
B. The history of changes to the directory or repository is copied.
C. If you make changes to the copied directory or cloned repository, the original will not change.
D. The state of every file in the directory or repository is copied.

Ans: 
A.  This is _true_ for both copying a directory and cloning a repository.
    As you saw in the previous lesson, if you have a URL to a repository, you can copy it to your computer using `git clone`.
    For copying a directory, you weren't expected to know this, but it is possible to copy a directory from one computer to another using the command `scp`, which stands for "secure copy". The name was chosen because the `scp` command lets you securely copy a directory from one computer to another. 
B.  This is _true_ for cloning a repository, but not for copying a directory. The main reason to use `git clone` rather than copying the directory is because `git clone` will also copy the commit history of the repository. However, copying can be done on any directory, whereas `git clone` only works on a Git repository. 
C.  This is _true_ for both copying a directory and cloning a repository. In both cases, you're making a copy that you can alter without changing the original. 
D.  This is _true_ for both copying a directory and cloning a repository. In both cases, all the files are copied.


## Behavior of git log
Suppose you ran `git log` in a repository. Part of the output is given below. If you were to run git checkout and examine each of these three commits in turn, which ones would you expect to contain code for a mute button?

```s
git log output:
commit 7be5a12f1567866b0d77ccdf2055d1a33831da78
Author: Ellison Leão <el@gmail.com>
Date:   Fri Jul 11 12:56:26 2014 -0300

    Add sound for the wing.

commit 06d72e1f95f046002ec46f41cf71957227111141
Author: Ellison Leão <el@gmail.com>
Date:   Wed Jul 9 23:42:55 2014 -0300

    Add mute button.

commit 3d4d45b246aad6a1cd0afaf7cfae26966110727e
Author: Ellison Leão <el@gmail.com>
Date:   Mon Jul 7 17:35:47 2014 -0300

    Fix leaderboard button
```
For this `git log` output, check all these commits you would expect to contain code for a mute button.
A. commit 7be5a12f1567866b0d77ccdf2055d1a33831da78 (the top commit listed)
B. commit 06d72e1f95f046002ec46f41cf71957227111141 (the middle commit listed)
C. commit 3d4d45b246aad6a1cd0afaf7cfae26966110727e (the bottom commit listed)

Ans: 
`git log` lists the most recent commit first, as you can verify by checking the commit dates. The middle commit probably contains the code for the mute button, since the commit message indicates that the mute button was added in that commit. The top commit also probably contain the mute button, since that commit is more recent and nothing suggests the mute button has been removed. The bottom commit probably does not contain the mute button, since that commit was created before the commit that added the mute button.

To summarize:
commit 7be5a12f1567866b0d77ccdf2055d1a33831da78 (the top commit listed)
Yes, probably contains the mute button.

commit 06d72e1f95f046002ec46f41cf71957227111141 (the middle commit listed)
Yes, probably contains the mute button.

commit 3d4d45b246aad6a1cd0afaf7cfae26966110727e (the bottom commit listed)
No, probably does not contain the mute button.


## Behavior of git checkout
On the next screen, check whether each statement is always, sometimes, or never true about using git checkout to checkout an earlier commit in a repository with multiple files.

A. Checking out an earlier commit will change the state of at least one file.
B. Checking out an earlier commit will change the state of more than one file.
C. Checking out an earlier commit will change the state of every file in the repository.
D. After checking out a commit, the state of all the files in the repository will be from the same point in time.

Ans: 
A.  This is _sometimes true_. Git doesn't allow you to save a new commit if no files have been updated, so you might think this is always true. However, it's possible to do the following:
    + Save a commit (call this commit 1).
    + Update some files and save another commit (call this commit 2).
    + Change all the files back to their state during commit 1, then save again (call this commit 3).
    This sometimes happens if commit 2 contained a bug, and it's important to fix the bug quickly. The easiest thing to do might be to remove all the changes introduced by commit 2 to fix the bug, then figure out how to safely reintroduce the changes later.
    At this point, commit 3 is the latest commit, so if you checkout commit 1, none of the files will be changed. 
B.& C. Both of these are `sometimes true`. Since each commit tracks the state of all files in the repository, it is possible that checking out an earlier commit will change the state of multiple files, or even all the files in the repository. However, it is possible to save a new commit after changing only one file, so it is possible only one file will change. 
D. This is `always true`. A commit saves a snapshot of all files in the repository at the time the commit was made, so checking out an earlier commit will result in all the files being reverted to their state at the time the commit was made. That is, the files will be in a consistent state.


## New repository introduction
In the rest of this problem set, you'll be using a new repository to get additional practice viewing history with Git. The process will be similar to the one you went through for the asteroids repository in the previous lesson.

The new repository is also a game, Pappu Pakia, that you can play in your browser, and like in the lesson, you'll be tracking down some bugs in the game by looking through its commit history. As such, don't be surprised if you spot some bugs when you start the game!

## Clone the repository
To get started, clone the repository, which is located at the url https://github.com/udacity/pappu-pakia.git. Then open the file index.htm using your web browser. On the next screen, select the two creators of the game. Their names will be displayed on the initial screen when you open the game.

```s
    git clone https://github.com/udacity/pappu-pakia.git
```

A. Creators of the game

Ans: As stated on the initial page of Pappu Pakia, the game was created by Rishabh and Kushagra. Many thanks to Kushagra and Rishabh for creating this awesome game! We made some modifications to the game to create the following exercises, but you can play the original version of their game here.


## Buggy behavior
If you started playing Pappu Pakia, you should have noticed some pretty strange behavior! The game seems empty of any obstacles, so it's pretty boring. Also, the bird (called a "pappu"), seems to flicker in various locations across the screen.

As you did in the previous lesson, use Git to checkout commits, run the game, and figure out which commit introduced the bug. When deciding where to start, it may be helpful to know that the bug was introduced recently! Enter the ID of the buggy commit on the next screen. You can also enter only the first four or more characters of the commit ID if that is easier.

In case you forget it and need it again, here is the ID of the most recent commit in the repository: `fa4c6bade4970c282b3870ad16f1bde8164663a9`

Both of those bugs were introduced by the same commit:
+ There are no obstacles
+ The pappu flickers across the screen

Q: Which commit introduced the byggy behavior?

Ans: 
The commit that introduced this bug has the ID `547f4171a82ec6429d002c1acef357aec41d3f17`. One way to find this out would have been to `run git` log, which should have shown that the most recent 4 commits, and their commit ids, were:
```s
commit fa4c6bade4970c282b3870ad16f1bde8164663a9
changing flattr link

commit 708bcce690e5faa5739bd471507c102ea16b77f7
pressing down arrow wont cause scroll down anymore

commit 547f4171a82ec6429d002c1acef357aec41d3f17
refactoring collision detection

commit 71d52709ddc4066e7a79a1d0a412e43429a0cdeb
removing old readme
(This output has been shortened to be easier to read.)
```
Then you could use `git checkout` to examine old commits and see which ones have the bug. You already know the most recent commit, "changing flattr link" has the bug, so you could run `git checkout 708bcce690e5faa5739bd471507c102ea16b77f7` to test the second-most-recent commit. You should find that this commit also has the bug. Next, you'll find the commit "refactoring collision detection" also has the bug, but the commit "removing old readme" does not. That means the commit "refactoring collision detection" with commit ID `547f4171a82ec6429d002c1acef357aec41d3f17`, is the one that introduced the bug.


## Examining the buggy commit
Use Git's history to figure out what changes were introduced in the commit that caused the bug. On the next screen, check any changes that were introduced, and enter the name of the file that was affected.

##Finding and fixing the bug
Now that you know what changes were introduced by the buggy commit, do you have any idea what could have caused the bug? If not, don't worry about it. The answer will be in the solution if you're curious.

Once you've identified the code that caused the bug, obtain a working version of the game. You can do this by either:
+ Figuring out what caused the bug (or check the solution), and modify the code to fix the bug
+ Checking out the commit before the one with the bug. That commit won't contain the most up-to-date version of the code, but for the purposes of the upcoming exercise it won't matter.

Q: Which of the following changes was made? Check all that apply
A. An "or" expression was separated out into several "if" statements.
B. Some variables were renamed.
C. A function was refactored into two fucntions.
D. Two functions were combined into one function.

Q: Which file was affected by the buggy commit? Enter the name.
   _____________

Ans: 
A,
js/utils

+ Changes introduced
To find the lines introduced by the buggy commit, you can use `git diff`. You'll need the ID of the buggy commit, which you just found to be `547f4171a82ec6429d002c1acef357aec41d3f17`. Then you'll need the ID of the previous commit, which will be the commit below it in git log. (That's because git log lists the most recent commit first.) That turns out to be `71d52709ddc4066e7a79a1d0a412e43429a0cdeb`.

Thus, by running `git diff 71d52709ddc4066e7a79a1d0a412e43429a0cdeb 547f4171a82ec6429d002c1acef357aec41d3f17`, you can find out that the lines changed by the buggy commit were:
```js
-    return !(
-      bounds1.end_x < bounds2.start_x ||
-      bounds2.end_x < bounds1.start_x ||
-      bounds1.end_y < bounds2.start_y ||
-      bounds2.end_y < bounds1.start_y
-    );
-
+    if (bounds1.end_x < bounds2.start_x) {
+        return true;
+    }
+    if (bounds2.end_x < bounds1.start_x) {
+        return true;
+    }
+    if (bounds1.end_y < bounds2.start_y) {
+        return true;
+    }
+    if (bounds2.end_y < bounds1.start_y) {
+        return true;
+    }
+    return false;
```
This change represents an "or" expression being separated out into several "if" statements. The number of functions did not change, and no variables were renamed.

+ File changed
Near the top of the git diff output, you can see the lines
```s
--- a/js/utils.js
+++ b/js/utils.js
```
This indicates that the file changed was js/utils.js, that is, the file utils.js within the js directory.

+ What caused the bug
Based on the change that was made, a reasonable guess is that the bug is some sort of logic error - maybe the new version does not return true and false at the correct times.

It turns out that this is correct. The new code has true and false reversed! Even if you weren't sure exactly why the bug was there, congratulations! You tracked down exactly where the bug was introduced, and knew which lines introduced it, without knowing the code base. All you had to know was how to use Git.


## There is a second bug
Now you should have a version of the code that works much better - your pappu is not flickering across the screen, and there are plenty of obstacles to avoid. However, there is another, harder to see, bug in the code.

During the game, a cluster of berries appears reasonably often. When the pappu hits those berries, it should split into three pappu clones, but instead, nothing seems to happen.

### Finding the bug
This time, instead of checking out old versions of the code, just run `git log` and look at the 10 most recent commits. Based only on the commit messages, which commit do you think is most likely to have introduced this bug? You can't be sure just by reading the messages, but pick the one you think is most likely.

Q: based on the commit messages, which commit do you think introduced the bug preventing the pappu clones from appearing?

Copy and past the commit ID or enter the first four or more characters, in the box: ______________

Ans: 
+ Identifying the bug
One reasonable guess is that the commit with message "speeding clones up", that is, commit 003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a, is likely to be the one causing the bug. The bug is related to clones, and this commit changed the behavior of clones, so it seems plausible that this commit caused the bug.

Of course, the most likely-looking commit won't always be the culprit, so you'll always have to take a closer look at the suspicious commit to see if it actually caused the bug. In this case, the commit "speeding up clones" did in fact cause the bug.

Using this strategy of examining the most likely looking commits doesn't always work, but it often does, and it can save a lot of debugging time. This is one of the reasons it's so useful to make one commit per logical change and give each commit a good message - to make it possible to take shortcuts like this!


## Examining the buggy commit
Again, use Git's history to figure out what changes were introduced in the commit that caused the bug. On the next screen, select the change that was introduced, and enter the name of the file that was affected.

### Finding and fixing the bug
Now that you know what changes were introduced by the buggy commit, do you have any idea what could have caused the bug? If not, don't worry about it. The answer will be in the solution if you're curious.

It's not necessary to obtain a working version of the game for future exercises. However, it can still be nice to verify that you've actually found the bug! You can do this by either:
+ Figure out what caused the bug (or check the solution), and modify the code to fix the bug.
+ Check out the commit before the one with the bug. That commit won't contain the most up-to-date version of the code, but it will let you verify that your hunch was correct. (Note: this will not work if you modified the code to fix the last bug.)

Q: Which of the following changes was made in the buggy commit?
A. In the buggy commit, the x and y coordinate of each clone is changed by a large fixed amount.
B. In the buggy commit, the x and y coordinate of each clone is changed by a large random amount.
C. In the buggy commit, the verlocity y of each clone is set to a large fixed amount.
D. In the buggy commit, the verlocity y of each clone is set to a large random amount.

Q: Which filoe was effected by the buggy commit?

Ans: B, js/pappu.js


### Changes introduced
As before, you can use `git diff` to find the lines introduced by the buggy commit. Again, you'll need the ID of the buggy commit, which is 003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a, and the ID of the previous commit, which is 746f762e38b5bbb7d0b837464ef6ec3f8ee5bf91.

Thus, by running git diff 746f762e38b5bbb7d0b837464ef6ec3f8ee5bf91 003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a, you can find out that the change made by the buggy commit was:
```js
-      clone.x += utils.randomNumber(5, 10);
-      clone.y += utils.randomNumber(-20, 20);
+      clone.x += utils.randomNumber(500, 1000);
+      clone.y += utils.randomNumber(-2000, 2000);
```
That is, the x and y coordinate of each clone is changed by a larger random amount. This will have the effect of making the clones move more quickly, or speed up, since their positions change more quickly.

### File changed
Near the top of the git diff output, you can see the lines:

--- a/js/pappu.js
+++ b/js/pappu.js
This indicates that the file changed was `js/pappu.js`, that is, the file `pappu.js` in the directory `js`. ## What caused the bug Based on the change that was made, one possible bug is that the clones move **too** quickly - so quickly they have left the screen before you see them. This turns out to be correct. If you change the code to have numbers bigger than the original numbers, but smaller than the new numbers, the clones will move more quickly, but still be visible. Some lines of code that work well are:
```js
clone.x += utils.randomNumber(20, 40);
clone.y += utils.randomNumber(-30, 30);
```
Again, even if you weren't sure exactly why the bug was there, congratulations! You tracked down which lines introduced a bug without knowing the code base, just by using Git.

