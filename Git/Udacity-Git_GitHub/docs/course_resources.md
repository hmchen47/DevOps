How to Use Git and GitHub: Version Control for Code
URL: https://www.udacity.com/wiki/ud775#git-installation-instructions

Contents

1 Course Resources
1.1 Git installation instructions
1.2 Additional Learning
2 Course Syllabus
2.1 Prerequisite Knowledge
2.2 Lesson 1: Navigating a Commit History
2.3 Lesson 2: Creating and Modifying a Repository
2.4 Lesson 3: Using GitHub to Collaborate
3 Acknowledgements
Course Resources

Git installation instructions

Follow the instructions here to install Git.

Additional Learning

The following resources may also be helpful in learning more about Git:

A cheat sheet of common Git commands (https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
A tutorial where you enter Git commands in the browser (https://try.github.io/)
A game giving practice with some more advanced Git branching techniques (http://pcottle.github.io/learnGitBranching/)
A Git tutorial where you enter commands on your own computer (http://gitimmersion.com/)
Instructional videos made by Git (http://git-scm.com/videos/)
Course Syllabus

Prerequisite Knowledge

Familiarity with a Unix-style command line will be important in this course.  If you haven't used a Unix-style command line before, visit this page for some additional resources.

Lesson 1: Navigating a Commit History

In this lesson, you’ll learn about a few different types of version control systems and discover what makes Git a great version control system for programmers. You’ll also get practice using Git to view the history of an existing project. You’ll learn to see all the versions that have been saved, checkout a previous version, and compare two different versions.

Instructor notes for lesson 1

Lesson 2: Creating and Modifying a Repository

In this lesson, you’ll learn how to create a repository and save versions of your project. You’ll learn about the staging area, committing your code, branching, and merging, and how you can use these to make you more efficient and effective.

Instructor notes for lesson 2

Lesson 3: Using GitHub to Collaborate

In this lesson, you’ll get practice using GitHub or other remote repositories to share your changes with others and collaborate on multi-developer projects. You’ll learn how to make and review a pull request on GitHub. Finally, you’ll get practice by collaborating with other Udacity students to write to a create-your-own-adventure story.

Instructor notes for lesson 3

Acknowledgements

We'd like to thank Jessica Uelmen for managing the project, Taylor Gilkeson and Justine Lai for producing and editing the course, and Larry Madrigal for his guest appearance in Lesson 1.  We couldn't have made this course without them.

-- Caroline and Sarah

This page was last edited on 2015/03/12 21:17:35.




Instructor Notes for Lesson 1
URL: https://www.udacity.com/wiki/ud775/lesson-1-notes

Contents

1 Morsel 2: Course overview
2 Morsel 4: Finding Diffs Between Larger Files
2.1 Asteroids Game
2.2 Downloading the old and new versions of the file
2.3 Mistake in Solution
3 Morsel 5: Reflections
4 Morsel 14: One Commit per Logical Change
4.1 What is a README?
5 Morsel 21: Cloning and Exploring The Repo
5.1 Cloning a Repository
5.2 Asteroids URL
5.3 Exiting git log
5.4 Getting Colored Output
5.5 Copying and Pasting from the Command Line
5.6 Using git log and git diff
5.7 Entering commit IDs
6 Morsel 23: Concept Map: repository, clone, log
6.1 Instructions
7 Morsel 25: Checking Out Old Versions of Code
7.1 QuickEdit Mode
7.2 Most Recent Commit
7.3 Format of git checkout
7.4 Windows Explorer
7.5 Entering commit IDs
8 Morsel 29: Setting Up Your Workspace on Windows
8.1 Changing background color
8.2 Downloading necessary files
8.3 Making Git configurations
8.4 Make sure you can start your editor from Git Bash
8.5 Restart Git Bash
9 Morsel 30: Setting Up Your Workspace on Mac
9.1 Downloading necessary files
9.2 Make sure you can start your editor from the terminal
9.3 Making Git configurations
9.4 Restart the terminal
10 Morsel 33: Survey Says!
Morsel 2: Course overview

Check out this page for some tutorials to get started using a Unix-style command line.

Morsel 4: Finding Diffs Between Larger Files

Asteroids Game

If you're interested, you can play the Asteroids game on Doug's website.

Downloading the old and new versions of the file

You can get the two versions of the game.js file in the Downloadables section on this page.  Here's how to get them on to your computer:

Click on the file you want in the Downloadables section
In the new tab that opens, right click and choose Save As
Make sure to take note of where you download them!

Mistake in Solution

When showing the output of running diff on Mac, Caroline accidentally showed the output of diff -u game_new.js game_old.js, that is, she put the files in the incorrect order. (She showed typing the correct command, but the output shown is from running the command with the arguments reversed). If you've run your command correctly, your output should be the reverse of Caroline's: that is, you should see minus signs where she has plus signs and vice versa.

Morsel 5: Reflections

Like Sarah said, there is a lot of research out there on reflection.  If you want a quick intro with some neat graphics, check out this site.

For a more in-depth look, check out this seminal 20-page paper on the topic.

Morsel 14: One Commit per Logical Change

What is a README?

Many projects contain a file named "README" that gives a general description of what the project does and how to use it.  It's often a good idea to read this file before doing anything with the project, so the file is given this name to make users more likely to read it.

Morsel 21: Cloning and Exploring The Repo

Cloning a Repository

To clone a repository, run git clone followed by a space and the repository URL.

Asteroids URL

Use the following url to clone the Asteroids repository: https://github.com/udacity/asteroids.git

Exiting git log

To stop viewing git log output, press q (which stands for quit).

Getting Colored Output

To get colored diff output, run git config --global color.ui auto

Copying and Pasting from the Command Line

To complete this quiz, you'll want to copy and paste some commit ids.

Windows 
To copy and paste within Git Bash, follow the instructions on this page.

Mac 
To copy and paste within the terminal on Mac, use Cmd+C and Cmd+V

Ubuntu 
To copy and paste within the terminal on Ubuntu, use Ctrl+Shift+C and Ctrl+Shift+V.

Using git log and git diff

As a reminder, running git log will show a list of the recent commits with information about them, including commit IDs.  Running git diff followed by two commit IDs will compare the two versions of the code in those commits.  If you need a refresher, you may want to rewatch this video.

Entering commit IDs

If it is easier, you may enter the first four or more characters of the commit ID rather than pasting the entire ID.

Morsel 23: Concept Map: repository, clone, log

Instructions

Check each concept you thing log should be connected to.  For each concept you check, write the connection type ("type-of", "part-of", or "operates-on") you think applies in the box next to it.  If none of the existing connection types work, write "other".

Morsel 25: Checking Out Old Versions of Code

QuickEdit Mode

To make copying and pasting in GitBash easier by turning on QuickEdit mode, follow the instructions here.

Most Recent Commit

The commit ID of the most recent commit is 3884eab839af1e82c44267484cf2945a766081f3.  You can use this commit ID to return to the latest commit after checking out an older commit.

Format of git checkout

The command Caroline types to checkout the "Revert controls" commit is git checkout b0678b161fcf74467ed3a63110557e3d6229cfa6.

Windows Explorer

When Caroline mentions opening a "file navigation GUI" on Windows, she is referring to the Windows Explorer.

Entering commit IDs

If it is easier, you may enter the first four or more characters of the commit ID rather than pasting the entire ID.

Morsel 29: Setting Up Your Workspace on Windows

Changing background color

If you prefer the background color of Git Bash to be something other than black, you can change it in the "Defaults" menu under the "Colors" tab.  If you like the background color as-is, you don't need to make any changes.

Downloading necessary files

Save this file in your home directory with the name git-completion.bash.
Save this file in your home directory with the name git-prompt.sh.
Save bash_profile_course from the Downloadables section in your home directory with the name .bash_profile.  (If you're curious to learn more about how bash prompts work, see this page.)
Making Git configurations

Run the following Git configuration commands.  The first one will need to be modified if you are using a text editor other than Sublime, or if Sublime is installed in another location for you.  See this page for the correct command for a couple of other popular text editors.  For any other editor, you'll need to enter the command you use to launch that editor from Git Bash.

git config --global core.editor "'C:/Program Files/Sublime Text 2/sublime_text.exe' -n -w"
git config --global push.default upstream
git config --global merge.conflictstyle diff3
Make sure you can start your editor from Git Bash

If you use Sublime, you can do this by adding the following line to your .bash_profile:

alias subl="C:/Program\ Files/Sublime\ Text\ 2/sublime_text.exe"
Restart Git Bash

You'll need to close and re-open Git Bash before all your changes take effect.

Morsel 30: Setting Up Your Workspace on Mac

Downloading necessary files

Save this file in your home directory with the name git-completion.bash.
Save this file in your home directory with the name git-prompt.sh.
Save bash_profile_course from the Downloadables section in your home directory with the name .bash_profile.  If you use Linux, you may need to name this file .bashrc instead of .bash_profile. (If you're curious to learn more about how bash prompts work, see this page.)
Make sure you can start your editor from the terminal

If you use Sublime, you can do this by add the following line to your .bash_profile:

alias subl="/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl"
Making Git configurations

Run the following Git configuration commands.  The first one will need to be modified if you are using a text editor other than Sublime, or if Sublime is installed in another location for you.  See this page for the correct command for a couple of other popular text editors.  For any other editor, you'll need to enter the command you use to launch that editor from the terminal.

git config --global core.editor "subl -n -w"
git config --global push.default upstream
git config --global merge.conflictstyle diff3
Restart the terminal

You'll need to close and re-open the terminal before all your changes take effect.

Morsel 33: Survey Says!

You can complete the survey here.

Thanks in advance!



Instructor Notes for Lesson 2
URL: https://www.udacity.com/wiki/ud775/lesson-2-notes
Contents

1 Morsel 3: Initializing a Repository
1.1 Git repositories and directories
2 Morsel 6: Staging Area
3 Morsel 9: Committing Changes
3.1 Git cheat sheet
4 Morsel 10: git diff Revisited
5 Morsel 11: Commit the Bug Fix
6 Morsel 17: Branches for Collaboration
6.1 Checking out the coins branch
6.2 Viewing the commit history
7 Morsel 23: Merging Coins into Master
8 Morsel 24: Merging on the Command Line
8.1 Checking out the coins branch
8.2 A note about git merge
8.3 Merge conflict
8.4 Merge conflict (Newline characters between Windows and Unix systems)
8.5 Comparing a commit to its parent
9 Morsel 28: Update Easy Mode
9.1 Diagramming Tools
10 Morsel 30: Committing the Conflict Resolution
Morsel 3: Initializing a Repository

Git repositories and directories

Each Git repository is tied to a specific directory - the directory where you ran git init.  Only files from that directory (and subdirectories inside that directory) will be contained in that repository, and you can have different repositories in different directories.

Note: it's often the case that a Git repository in some directory will only contain, or track, some of the files in that directory, rather than all of them.  You'll see how this works later this lesson.

Morsel 6: Staging Area

If you accidentally add a file to the staging area, you can remove it using git reset.  For example, if you accidentally add lesson_2_reflections.txt, but don’t want it to be committed yet, run git reset lesson_2_reflections.txt and the file will be removed from the staging area, but it will still be in your working directory.

Morsel 9: Committing Changes

Git cheat sheet

You've just learned several Git commands pretty quickly.  If you'd like some help keeping track of them, you might be interested in this Git cheat sheet.  By now, we've covered the commands in the sections "Configure Tooling", "Create Repositories", and "Make Changes".  You'll be learning many of the remaining commands on this sheet throughout the rest of this course.

Morsel 10: git diff Revisited

If you are following along, you should run git checkout master before you commit.  This is because your HEAD is still 'detached' from Lesson 1 when you checked out an old commit, and running this command will fix that.  You'll learn more about what this command does later this lesson.

Morsel 11: Commit the Bug Fix

You may notice that our commit id is different from yours, even though we made the same change, while the commit ids up to this point have all been the same.  That’s because if there is any difference between two commits, including the author or the time it was created, the commits will have different ids.  Check out this page if you’re interested in learning more about Git internals and how commit ids are generated.

Morsel 17: Branches for Collaboration

Checking out the coins branch

Note that you'll need to check out the coins branch using the command git checkout coins before you can view the coins branch using git log.

Viewing the commit history

The full command Caroline types to see the visual representation of the commit history is git log --graph --oneline master coins.

Morsel 23: Merging Coins into Master

If a branch is deleted and leaves some commits unreachable from existing branches, those commits will continue to be accessible by commit id, until Git’s garbage collection runs. This will happen automatically from time to time, unless you actively turn it off.  You can also run this process manually with git gc.

Morsel 24: Merging on the Command Line

Checking out the coins branch

If you haven't already checked out the coins branch, you'll need to do so now with the command git checkout coins before you'll be able to refer to it.  Once you've done that, decide whether you should keep it checked out or check out a different branch before completing the merge.

A note about git merge

git merge will also include the currently checked-out branch in the merged version.  So if you have branch1 checked out, and you run git merge branch2 branch3, the merged version will combine branch1 as well as branch2 and branch3.  That’s because the branch1 label will update after you make the merge commit, so it’s unlikely that you didn’t want the changes from branch1 included in the merge.  For this reason, you should always checkout one of the two branches you’re planning on merging before doing the merge.  Which one you should check out depends on which branch label you want to point to the new commit.

Since the checked-out branch is always included in the merge, you may have guessed that when you are merging two branches, you don't need to specify both of them as arguments to git merge on the command line. If you want to merge branch2 into branch1, you can simply git checkout branch1 and then type git merge branch2. The only reason to type git merge branch1 branch2 is if it helps you keep better mental track of which branches you are merging.

Also, since the two branches are merged, the order in which they are typed into the command line does not matter. The key is to remember that git merge always merges all the specified branches into the currently checked out branch, creating a new commit for that branch.

Merge conflict

If you get a message like this

Auto-merging game.js
CONFLICT (content): Merge conflict in game.js
Automatic merge failed; fix conflicts and then commit the result.
then your files were not in the same state as Caroline's when you started the merge.  To fix this, complete the following steps:

Restore your files to their state before you started the merge by running git merge --abort
Double check the state of your files.  If you run git log while the master branch is checked out, you should see Caroline's "Add color" commit as the second-most-recent, and the most recent should be your commit fixing the bullet bug.  If you use git diff to compare your commit to Caroline's, your commit should introduce the line this.delayBeforeBullet = 10; on line 424.  The line should be indented to the same level as the line below it using only spaces (no tabs), and the line should have no spaces after it.
Once your file is in the correct state, create a new commit with your changes.
Try the merge again.
Merge conflict (Newline characters between Windows and Unix systems)

Context: Whenever we hit the "Enter" key on the keyboard, we are actually telling the computer to insert an invisible character into our text file to indicate to the computer that there should be a new line. Unix systems adds one character called the "line feed" character or LF or \n while Windows systems adds two characters, "carriage return" and "line feed" or CRLF or \r\n.

Caroline's files have LF because her files were edited on Mac OSX, which uses LF. If a Windows user were to edit Caroline's files, the Windows text editor might convert all LF to CRLF to make editing files possible. When the Windows user merges her file with Caroline's files, a merge conflict will result due to the different LF and CRLF characters.

To fix this, Windows users should set the global autocrlf attribute to true: git config --global core.autocrlf true. More information can be found here: https://help.github.com/articles/dealing-with-line-endings/#platform-all

Comparing a commit to its parent

The command Caroline mentions to compare a commit to its parent is git show commit_id

Morsel 28: Update Easy Mode

Diagramming Tools

gliffy
yUML
If you have a favorite that we don't have listed here, mention it in a forum post so that others can find it!

Morsel 30: Committing the Conflict Resolution

Near the beginning of the video, Caroline accidentally says "I still need to let Git know that the conflict is reserved." She meant "resolved", not "reserved".

This page was last edited on 2015/03/12 21:06:28.






Instructor Notes for Lesson 3
URL: https://www.udacity.com/wiki/ud775/lesson-3-notes
Contents

1 Morsel 5: Adding a Remote
1.1 Copy the HTTPS URL, not the SSH URL!
1.2 Sharing your reflections
2 Morsel 12: Fork the Recipes Repository
3 Morsel 23: Making a Pull Request
4 Morsel 27: Updating Your Local Repository
4.1 Simulate Sarah's changes
4.2 Make sure you are on the master branch
4.3 Use git add on the conflicting files before committing
5 Morsel 29: CM: Fork, Fetch, Pull Request
Morsel 5: Adding a Remote

Copy the HTTPS URL, not the SSH URL!

At 1:29, Caroline copies the URL to the repository. The video mistakenly shows the URL to use if the repository is accessed over SSH. The course assumes that the student will use HTTPS, not SSH. Please click on the HTTPS button and copy the URL that shows up for HTTPS. It will begin with https:// rather than git@github.com.

If you are interested in using SSH instead, you can follow the instructions here, but this is not recommended unless you are already familiar with SSH keys.

Sharing your reflections

We encourage you to be bold in sharing your reflections on GitHub.  If you're not happy with any of your responses, the best solution is to update that response in one or more new commits.  The previous response will still be visible in the commit history, but updating your perspective over time is part of the learning process! Having a commit history that shows your updating perspective will reflect well on you, not poorly.

That said, if you've written anything in your reflections repository that you are not comfortable sharing, you can checkout the commit before you introduced that change, create a new branch at that point, and commit any other changes you are willing to share to the new branch.  Then, by only pushing your new branch, you can keep the changes on your original branch private.

Morsel 12: Fork the Recipes Repository

Larry's repository on GitHub can be found here.

Morsel 23: Making a Pull Request

Sarah accidentally says that the local master is the only thing that changes when you run git pull origin master.  However, the working directory and staging area will also update when you run git pull.  That's why when you run git pull, you see your files update, not just the git log output.

Morsel 27: Updating Your Local Repository

Simulate Sarah's changes

To simulate Sarah's changes, first download the file sarah_changes_2.sh from the Downloadables section.  Then, using Git Bash or your terminal, cd to the directory where you've saved the file.  Then type bash sarah_changes_2.sh followed by a space, followed by the url to your fork.  For example, if Caroline were running the code, she would type bash sarah_changes_2.sh https://github.com/cbuckey-uda/recipes.git, but you should use the url for your fork, not Caroline's fork.  If you haven't set up password-caching, then you will be prompted to enter your GitHub username and password.

Note: This code will not actually create a pull request.  Instead, it will update the commit history on GitHub to make it look as though the pull request has already been merged.  You will not need to merge a pull request.  Instead, check for a commit on the master branch on GitHub with the message "Merge pull request".

Make sure you are on the master branch

You'll want to make sure you check out the master branch before following the steps in this video.

Use git add on the conflicting files before committing

Just as in lesson 2, before running git commit to create the merge commit, you'll need to use git add to add any files that had conflicts to the staging area.

Morsel 29: CM: Fork, Fetch, Pull Request

You can see the full final version of the concept map here, with all the nodes, including those we pruned in earlier versions.

This page was last edited on 2015/03/12 21:17:12.