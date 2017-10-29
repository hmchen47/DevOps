Greeating and Modifying Repository
----------------------------------

# Initializing A Repository
## Git repositories and directories
Each Git repository is tied to a specific directory - the directory where you ran `git init`. Only files from that directory (and subdirectories inside that directory) will be contained in that repository, and you can have different repositories in different directories.

Note: it's often the case that a Git repository in some directory will only contain, or track, some of the files in that directory, rather than all of them. You'll see how this works later this lesson.

## Quiz: New repository
Q: How many commits do you think a new repository contains?

Q: What command could you use to find out?

A commit is a snapshot of the repository.

Ans: 0, `git log`

# Quiz: Examining The New Repository
Run the commands `git init` and `git status` in the directory with your reflection.

# Reflect: Initializing a Repository
Now that you’ve initialized your first repository, go to your reflections directory, create a new file called `lesson_2_reflections.txt`, and add the following question and your thoughts on it:
	__What happens when you initialize a repository? Why do you need to do it?__

You may also wish to run `git status` after you have created the file. You should see that now both files are listed as untracked files.

Supplement material: [lesson-2-reflection-prompts.txt](https://d17h27t6h515a5.cloudfront.net/topher/2017/May/592910ce_lesson-2-reflection-prompts/lesson-2-reflection-prompts.txt)


# Quiz: Staging Area
If you accidentally add a file to the staging area, you can remove it using git reset. For example, if you accidentally add lesson_2_reflections.txt, but don’t want it to be committed yet, run `git reset lesson_2_reflections.txt` and the file will be removed from the staging area, but it will still be in your working directory.


# Concept Map: init, add, staging area
We’ve introduced a few new concepts since we last revisited our concept map.
+ git init
+ git add
+ git status
+ staging area
+ working directory

## Previous Version
Remember our concept map from last lesson? Here’s what it looked like the last time we added a new concept.
[!Concept Map from last time](https://lh5.ggpht.com/sEID_-UrxpMAWGxZeZ3wLkZLQY88K3FH7sWSRaVAslq_a3xQUpGKWJopOgTENGhilICMJsT8URIpqflutkU=s300)

## Where Do the New Concepts Go?
Here’s the structure we’ve come up with for how to add these new concepts in to the map. Which concept belongs where?
[!Concept Map with blanks](https://lh6.ggpht.com/5XQ4zmwFbreGMI09mMdFke4eeBBvPD7S5mcgYLcRo9KzVpvEC_AwVkvbV2QcM9uPJ_4aXaA5OoLcAWvW9w=s300#w=1800&h=1012)

In the following quiz, write in the concept that you think belongs in each new empty node.


# Reflect: Staging Area
Now that you’ve added a file to the staging area (or maybe multiple files!), go add the following question and your thoughts on it to your lesson_2_reflections file:
	__How is the staging area different from the working directory and the repository? What value do you think it offers?__


# How to write a commit message
You're about to make your first commit to your reflections repository. When you do this, you'll need to write a commit message describing your changes. If you followed the instructions in the "Setting Up Your Workspace" video for your platform near the end of Lesson 1, the editor you chose will appear as soon as you run git commit and allow you to write a commit message. If you get an error message, you should try revisiting the instructions in Lesson 1 and make sure your text editor is set up properly.

You can also specify a commit message via the command line by running `git commit -m "Commit message"` instead of just `git commit`. It's still a good idea to get an editor set up, since this will make it easier to write long commit messages that fully describe the change.

## Commit message style
While commit message style varies from person to person, this [style guide](http://udacity.github.io/git-styleguide/) describes some common best practices when writing commit messages.

# Udacity Git Commit Message Style Guide
## Introduction
This style guide acts as the official guide to follow in your projects. Udacity evaluators will use this guide to grade your projects. There are many opinions on the "ideal" style in the world of development. Therefore, in order to reduce the confusion on what style students should follow during the course of their projects, we urge all students to refer to this style guide for their projects.

## Commit Messages
### Message Structure
A commit messages consists of _three distinct parts_ separated by a blank line: the title, an optional body and an optional footer. The layout looks like this:
```s
type: subject

body

footer
```
The title consists of the type of the message and subject.

## The Type
The type is contained within the title and can be one of these types:
+ feat: a new feature
+ fix: a bug fix
+ docs: changes to documentation
+ style: formatting, missing semi colons, etc; no code change
+ refactor: refactoring production code
+ test: adding tests, refactoring test; no production code change
+ chore: updating build tasks, package manager configs, etc; no production code change

## The Subject
Subjects should be no greater than 50 characters, should begin with a capital letter and do not end with a period.

Use an imperative tone to describe what a commit does, rather than what it did. For example, use `change`; not changed or changes.

## The Body
Not all commits are complex enough to warrant a body, therefore it is optional and only used when a commit requires a bit of explanation and context. Use the body to explain the `what` and `why` of a commit, not the how.

When writing a body, the blank line between the title and the body is required and you should limit the length of each line to no more than 72 characters.

## The Footer
The footer is optional and is used to reference issue tracker IDs.

## Example Commit Message
> feat: Summarize changes in around 50 characters or less
> 
> More detailed explanatory text, if necessary. Wrap it to about 72
> characters or so. In some contexts, the first line is treated as the
> subject of the commit and the rest of the text as the body. The
> blank line separating the summary from the body is critical (unless
> you omit the body entirely); various tools like `log`, `shortlog`
> and `rebase` can get confused if you run the two together.
> 
> Explain the problem that this commit is solving. Focus on why you
> are making this change as opposed to how (the code explains that).
> Are there side effects or other unintuitive consequenses of this
> change? Here's the place to explain them.
> 
> Further paragraphs come after blank lines.
> 
> - Bullet points are okay, too
> 
> - Typically a hyphen or asterisk is used for the bullet, preceded
> by a single space, with blank lines in between, but conventions
> vary here
> 
> If you use an issue tracker, put references to them at the bottom,
> like this:
> 
> Resolves: #123
> See also: #456, #789


# Quiz: Git Diff Revisited
If you are following along, you should run `git checkout master` before you commit. This is because your HEAD is still 'detached' from Lesson 1 when you checked out an old commit, and running this command will fix that. You'll learn more about what this command does later this lesson.


# Commit the Bug Fix
## Leave 'detached HEAD' state
Right now, your HEAD should still be 'detached' from Lesson 1 when you checked out an old commit. To fix that, run the command `git checkout master`. You'll learn more about what this command does later this lesson.

## Fix the delay bug
Now, if you were following along with Caroline, you may have already fixed the bug in the Asteroids repository. If not, go ahead and make the change and add it to the staging area now.

In game.js find the statement if (this.delayBeforeBullet <= 0) { (should be on line 423). On the next line, insert this.delayBeforeBullet = 10;

## Stage your change
Then stage your change by adding the game.js file to the staging area. If you’re having trouble remembering how to stage changes, use this video as a refresher.

## Commit your change
Now, go ahead and commit this change. Make sure to use a meaningful commit message! If you have trouble remember how to commit, refer to this video.

You may notice that our commit id is different from yours, even though we made the same change, while the commit ids up to this point have all been the same. That’s because if there is any difference between two commits, including the author or the time it was created, the commits will have different ids. Check out [this page](http://git-scm.com/book/en/Git-Internals-Git-Objects) if you’re interested in learning more about Git internals and how commit ids are generated.


# Reflect: Commit Size
Now that you’ve committed changes using the staging area, go add the following question and your thoughts on it to your lesson_2_reflections file:
	__How can you use the staging area to make sure you have one commit per logical change?__


# Reflect: When to Use Branches
Now that you’ve learned how to create a branch in Git, go add the following question and your thoughts on it to your reflections file:
	__What are some situations when branches would be helpful in keeping your history organized? How would branches help?__


# Branches For Collaboration
## Viewing the commit history
The full command Caroline types to see the visual representation of the commit history is `git log --graph --oneline master coins`.

## Checking out the coins branch
Note that you'll need to check out the coins branch using the command `git checkout coins` before you can view the coins branch using `git log`.


# Reflect: Visualizing with Diagrams
Now that you’ve had some experience creating branches and drawing diagrams of your history, go add the following question and your thoughts on it to your reflections file:
	__How do the diagrams help you visualize the branch structure?__


# Merging Coins Into Master
If a branch is deleted and leaves some commits unreachable from existing branches, those commits will continue to be accessible by commit id, until Git’s garbage collection runs. This will happen automatically from time to time, unless you actively turn it off. You can also run this process manually with `git gc`.


# Merging On The Command Line
## Checking out the coins branch
If you haven't already checked out the coins branch, you'll need to do so now with the command `git checkout coins` before you'll be able to refer to it. Once you've done that, decide whether you should keep it checked out or check out a different branch before completing the merge.

## A note about git merge
`git merge` will also include the currently checked-out branch in the merged version. So if you have __branch1 checked out__, and you run `git merge branch2 branch3`, the merged version will __combine branch1 as well as branch2 and branch3__. That’s because the branch1 label will update after you make the merge commit, so it’s unlikely that you didn’t want the changes from branch1 included in the merge. For this reason, you should always checkout one of the two branches you’re planning on merging before doing the merge. Which one you should check out depends on which branch label you want to point to the new commit.

Since the checked-out branch is always included in the merge, you may have guessed that when you are merging two branches, you don't need to specify both of them as arguments to `git merge` on the command line. If you want to merge branch2 into branch1, you can simply `git checkout branch1` and then type `git merge branch2`. The only reason to type `git merge branch1 branch2` is if it helps you keep better mental track of which branches you are merging.

Also, since the two branches are merged, the order in which they are typed into the command line does not matter. The key is to remember that `git merge` always merges all the specified branches into the currently checked out branch, creating a new commit for that branch.

## Merge conflict
If you get a message like this

> Auto-merging game.js
> CONFLICT (content): Merge conflict in game.js
> Automatic merge failed; fix conflicts and then commit the result.

then your files were not in the same state as Caroline's when you started the merge. To fix this, complete the following steps:
1. Restore your files to their state before you started the merge by running `git merge --abort`
2. Double check the state of your files. If you run `git log` while the master branch is checked out, you should see Caroline's "Add color" commit as the second-most-recent, and the most recent should be your commit fixing the bullet bug. If you use `git diff` to compare your commit to Caroline's, your commit should introduce the line `this.delayBeforeBullet = 10;` on line 424. The line should be indented to the same level as the line below it using only spaces (no tabs), and the line should have no spaces after it.
3. Once your file is in the correct state, create a new commit with your changes.
4. Try the merge again.

## Merge conflict (Newline characters between Windows and Unix systems)
Context: Whenever we hit the "Enter" key on the keyboard, we are actually telling the computer to insert an invisible character into our text file to indicate to the computer that there should be a new line. Unix systems adds one character called the "line feed" character or LF or \n while Windows systems adds two characters, "carriage return" and "line feed" or CRLF or \r\n.

Caroline's files have LF because her files were edited on Mac OSX, which uses LF. If a Windows user were to edit Caroline's files, the Windows text editor might convert all LF to CRLF to make editing files possible. When the Windows user merges her file with Caroline's files, a merge conflict will result due to the different LF and CRLF characters.

To fix this, Windows users should set the global autocrlf attribute to true: `git config --global core.autocrlf true`. More information can be found here: https://help.github.com/articles/dealing-with-line-endings/#platform-all

## Comparing a commit to its parent
The command Caroline mentions to compare a commit to its parent is `git show commit_id`


# Reflect: Merging Two Branches
Now that you’ve learned how to use Git to merge branches together, go add the following question and your thoughts on it to your reflections file:
	__What is the result of merging two branches together? Why do we represent it in the diagram the way we do?__


# Update Easy Mode
## Motivation
Master has updated since the easy-mode branch was created. In this case, it has the addition of coins, which you might like to include in the easy-mode branch. In general, it’s very common that if you make a branch, either an experimental branch or to work on a new feature, you want to periodically merge master into that branch. This is because master usually contains the official version of the code, and it’s common to want experimental changes to include all of the changes to master.

## Previous version of the diagram
Here’s what the history looks like right now.
[!old diagram](https://lh6.ggpht.com/4Z1H9ULiwr6p2zn8ISqJtlleMX7BFMLAEpXbXEqNoQz4JboVxjdJNN2leARBL6lzPFBTHy-V4WS0XIZccQ=s600#w=1920&h=1080)

## Draw an updated diagram
If you merge master into the easy-mode branch, what will the history look like afterward? Take a minute to draw the new history using whatever method you like best. You might want to use pencil and paper, or create a text file with stars and dashes similar to the output of `git log --graph`, or maybe use an online diagramming tool like `gliffy` or `yUML`. Once you’re finished, watch the solution to compare your diagram to Sarah’s.

Diagramming Tools
+ [gliffy](https://www.gliffy.com/)
+ [yUML](http://yuml.me/diagram/activity/draw)


# Committing The Conflict Resolution
Near the beginning of the video, Caroline accidentally says "I still need to let Git know that the conflict is reserved." She meant "resolved", not "reserved".


# Concept Map: branch, merge
Here's where we left off with the concept map: [!Concept Map branch and merge](https://lh3.ggpht.com/-Xk8Mi7vOfVQDRPES-yvjNtPSaWraY7qFAgJYVh2txL4u3E63JA2yUeSiVHF3E5jbalSSoPl6fFAOCJr9nM=s300#w=1920&h=1080)

## New ideas
Since then, we've talked about a few new ideas. The biggest ones are the ideas of _branching_ and _merging_.

Where do branching and merging fit best in the Concept Map? Continue to the quiz to add them.
[!Concept Map branch and merge](https://lh6.ggpht.com/kESRoctpd5X-DdZn1VBRnwFoyxK8zU3IEk7R20wJVrRe0NBSuUVvWCKrk5noBM4CjtEuDkqWenf8tDRaM6Q=s300#w=1848&h=1036)


# Reflect: Automatic vs. Manual Merging
Now that you’ve learned when Git will not be able to automatically merge branches, and what happens when it can’t, go add the following question and your thoughts on it to your reflections file:
	__What are the pros and cons of Git’s automatic merging vs. always doing merges manually?__





# Original Relection Note

What happens when you initialize a repository? Why do you need to do it?

	reflections $ git init
		Initialized empty Git repository in d:/Users/hmchen/Documents/CurrentProjects/GitHub/Udacity/version-control/reflections/.git/
	
    initialize an empty git repository with .git hidden directory to store configure and objects

How is the staging area different from the working directory and the repository?
What value do you think it offers?

    Staging area is a temporay repository where git adds files to the temporary area and allows to reset before commit the files from stagaing area to repository

How can you use the staging area to make sure you have one commit per logical change?
    
    git diff -> to view the differece between staging area and workign directory
    git diff --staged --> to view the difference between staging are and most recently commit
    git diff commit1 commit 2 -> to check the difference between two commits

What are some situations when branches would be helpful in keeping your history organized? How would branches help?
	
	when adding new feature, bug fix, or experimental 
	beanch will add an extra path and separate from the master.  When makeing any change, it woun't affect the main branch.
	git branch <- to display all the branches, including master
	git checkout branch_name <- switch to another branch
	git branch -d branch_name <- delet a branch
	within each branch, git add and git commit are requried to comit the change
	git checkout -b new_branch = git branch new_branch + git checkout new_branch
	git commit -m "msg" <- add files in staging areas into repository
	git commit --amend -m "ms" <- revise committed message

How do the diagrams help you visualize the branch structure?

	the diagram and show the relationship of all branches and their history (via git log)
	Besides, the diagram alsow shows the unreachable branch

What is the result of merging two branches together? Why do we represent it in the diagram the way we do?

	combine the changes from two branches and compare with the latest same master commit to decide which changes to add and delete
	the diagram make it wasier to view the relationship and modification between two branches

What are the pros and cons of Git’s automatic merging vs. always doing merges manually?

	git autmatic merge let teh system judge the combination of changes which make out life easier.  However, the merge sometimes conflict each other, manual meger should be conduct to identify the conflicts and make appropriate modifications.




Instructor Notes

Staging Area
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/e-2960548768/m-2976708608

If you accidentally add a file to the staging area, you can remove it using git reset. For example, if you accidentally add lesson_2_reflections.txt, but don’t want it to be committed yet, run git reset lesson_2_reflections.txt and the file will be removed from the staging area, but it will still be in your working directory.

Concept Map: init, add, staging area
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/e-2960548771/m-2985978647

We’ve introduced a few new concepts since we last revisited our concept map.

git init
git add
git status
staging area
working directory
Previous Version

Remember our concept map from last lesson? Here’s what it looked like the last time we added a new concept.

Concept Map from last time

Where Do the New Concepts Go?

Here’s the structure we’ve come up with for how to add these new concepts in to the map. Which concept belongs where?

Concept Map with blanks

In the following quiz, write in the concept that you think belongs in each new empty node.



git diff Revisited
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/e-2960548777/m-2960548778

If you are following along, you should run git checkout master before you commit. This is because your HEAD is still 'detached' from Lesson 1 when you checked out an old commit, and running this command will fix that. You'll learn more about what this command does later this lesson.



Leave 'detached HEAD' state
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/m-2971848583

Right now, your HEAD should still be 'detached' from Lesson 1 when you checked out an old commit. To fix that, run the command git checkout master. You'll learn more about what this command does later this lesson.

Fix the delay bug

Now, if you were following along with Caroline, you may have already fixed the bug in the Asteroids repository. If not, go ahead and make the change and add it to the staging area now.

In game.js find the statement if (this.delayBeforeBullet <= 0) { (should be on line 423). On the next line, insert this.delayBeforeBullet = 10;

Stage your change

Then stage your change by adding the game.js file to the staging area. If you’re having trouble remembering how to stage changes, use this video as a refresher.

Commit your change

Now, go ahead and commit this change. Make sure to use a meaningful commit message! If you have trouble remember how to commit, refer to this video.

You may notice that our commit id is different from yours, even though we made the same change, while the commit ids up to this point have all been the same. That’s because if there is any difference between two commits, including the author or the time it was created, the commits will have different ids. Check out this page (http://git-scm.com/book/en/v2/Git-Internals-Git-Objects) if you’re interested in learning more about Git internals and how commit ids are generated.



Viewing the commit history
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/e-2960548785/m-2960548786

The full command Caroline types to see the visual representation of the commit history is git log --graph --oneline master coins.




Merging on the Command Line
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/e-2989238628/m-2960548799

Checking out the coins branch

If you haven't already checked out the coins branch, you'll need to do so now with the command git checkout coins before you'll be able to refer to it. Once you've done that, decide whether you should keep it checked out or check out a different branch before completing the merge.

A note about git merge

git merge will also include the currently checked-out branch in the merged version. So if you have branch1 checked out, and you run git merge branch2 branch3, the merged version will combine branch1 as well as branch2 and branch3. That’s because the branch1 label will update after you make the merge commit, so it’s unlikely that you didn’t want the changes from branch1 included in the merge. For this reason, you should always checkout one of the two branches you’re planning on merging before doing the merge. Which one you should check out depends on which branch label you want to point to the new commit.

Since the checked-out branch is always included in the merge, you may have guessed that when you are merging two branches, you don't need to specify both of them as arguments to git merge on the command line. If you want to merge branch2 into branch1, you can simply git checkout branch1 and then type git merge branch2. The only reason to type git merge branch1 branch2 is if it helps you keep better mental track of which branches you are merging.

Also, since the two branches are merged, the order in which they are typed into the command line does not matter. The key is to remember that git merge always merges all the specified branches into the currently checked out branch, creating a new commit for that branch.

Merge conflict

If you get a message like this

Auto-merging game.js
CONFLICT (content): Merge conflict in game.js
Automatic merge failed; fix conflicts and then commit the result.
then your files were not in the same state as Caroline's when you started the merge. To fix this, complete the following steps:

1. Restore your files to their state before you started the merge by running git merge --abort

2. Double check the state of your files. If you run git log while the master branch is checked out, you should see Caroline's "Add color" commit as the second-most-recent, and the most recent should be your commit fixing the bullet bug. If you use git diff to compare your commit to Caroline's, your commit should introduce the line this.delayBeforeBullet = 10; on line 424. The line should be indented to the same level as the line below it using only spaces (no tabs), and the line should have no spaces after it.

3. Once your file is in the correct state, create a new commit with your changes. 

4. Try the merge again. 

Merge conflict (Newline characters between Windows and Unix systems)

Context: Whenever we hit the "Enter" key on the keyboard, we are actually telling the computer to insert an invisible character into our text file to indicate to the computer that there should be a new line. Unix systems adds one character called the "line feed" character or LF or \n while Windows systems adds two characters, "carriage return" and "line feed" or CRLF or \r\n.

Caroline's files have LF because her files were edited on Mac OSX, which uses LF. If a Windows user were to edit Caroline's files, the Windows text editor might convert all LF to CRLF to make editing files possible. When the Windows user merges her file with Caroline's files, a merge conflict will result due to the different LF and CRLF characters.

To fix this, Windows users should set the global autocrlf attribute to true: git config --global core.autocrlf true. More information can be found here: https://help.github.com/articles/dealing-with-line-endings/#platform-all

Comparing a commit to its parent

The command Caroline mentions to compare a commit to its parent is git show commit_id



Update Easy Mode
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/e-2958508789/m-2952168755

Motivation

Master has updated since the easy-mode branch was created. In this case, it has the addition of coins, which you might like to include in the easy-mode branch. In general, it’s very common that if you make a branch, either an experimental branch or to work on a new feature, you want to periodically merge master into that branch. This is because master usually contains the official version of the code, and it’s common to want experimental changes to include all of the changes to master.

Previous version of the diagram

Here’s what the history looks like right now. 
old diagram (branchDiagram.png)
If you merge master into the easy-mode branch, what will the history look like afterward?

Draw a diagram showing what it looks like afterward

Take a minute to draw the new history using whatever method you like best. You might want to use pencil and paper, or create a text file with stars and dashes similar to the output of git log --graph, or maybe use an online diagramming tool like gliffy (https://www.gliffy.com/) or yUML (http://yuml.me/diagram/activity/draw). Once you’re finished, watch the solution to compare your diagram to Sarah’s.



Concept Map: branch, merge
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/e-2962508640/m-2976898589

Here's where we left off with the concept map: Concept Map branch and merge (conceptmap2.png)

New ideas

Since then, we've talked about a few new ideas. The biggest ones are the ideas of branching and merging.

Where do branching and merging fit best in the Concept Map? Continue to the quiz to add them.

Concept Map branch and merge (conceptmap3.jpg)



Simulate Sarah's Changes
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3060569115/m-3108878699

In the Downloadables section, there is a file called sarah_changes.sh, which contains code to make it look like Sarah has modified your fork on GitHub. To run the code, download the file, then using Git Bash or your terminal, cd to the directory where you've saved it. Then type bash sarah_changes.sh followed by a space, followed by the url to your fork. For example, if Caroline were running the code, she would type bash sarah_changes.sh https://github.com/cbuckey-uda/recipes.git, but you should use the url for your fork, not Caroline's fork. If you haven't set up password caching, then you will be prompted to enter your GitHub username and password.



Which commits exist where?
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3060569115/m-3075768626

The commit by Larry adding the chili recipe should have been in both places, since it was present in the original repository before you forked it. Your commit adding a new spice should only have been present locally, since you made the commit locally but didn't push. The commit by Sarah removing cumin should only have been present on GitHub, since Sarah made the change and pushed it to GitHub, but you didn't pull yet.
```