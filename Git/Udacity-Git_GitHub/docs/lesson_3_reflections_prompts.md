Using GitHub to Collaborate
===========================

# Create a GitHub account
In this lesson, you'll be sharing changes on GitHub, so you'll need a GitHub account. If you don't already have one, you can create an account by visiting github.com and clicking "Sign up for GitHub".

When you're asked to choose a plan, you can choose a free plan, since we won't be using any of the paid features in this course.

## Set up Password Caching
Every time you send changes to GitHub via the command line, you'll need to type your password to prove that you have permission to modify the repository. This can get annoying quickly, so many people like to set up password caching, which will let you type your password once and have it auto-filled on that computer in the future. To do this, follow the instructions here. If you're using Windows and you followed our Git installation instructions earlier, you're using msysgit, so you can follow the instructions for msysgit.


# Adding A Remote
## Copy the HTTPS URL, not the SSH URL!
At 1:29, Caroline copies the URL to the repository. The video mistakenly shows the URL to use if the repository is accessed over SSH. The course assumes that the student will use HTTPS, not SSH. Please click on the `HTTPS` button and copy the URL that shows up for HTTPS. It will begin with `https://` rather than `git@github.com`.

If you are interested in using SSH instead, you can follow the instructions [here](https://help.github.com/articles/generating-ssh-keys/), but this is not recommended unless you are already familiar with SSH keys.

## Sharing your reflections
We encourage you to be bold in sharing your reflections on GitHub. If you're not happy with any of your responses, the best solution is to update that response in one or more new commits. The previous response will still be visible in the commit history, but updating your perspective over time is part of the learning process! Having a commit history that shows your updating perspective will reflect well on you, not poorly.

That said, if you've written anything in your reflections repository that you are not comfortable sharing, you can checkout the commit before you introduced that change, create a new branch at that point, and commit any other changes you are willing to share to the new branch. Then, by only pushing your new branch, you can keep the changes on your original branch private.


# Make changes on GitHub
Now that you've seen how to create a remote repository and push changes to it, use the GitHub website to create a new file for your lesson 3 reflections and add the below question and your thoughts on it.

If you prefer to start from the file [lesson_3_reflection_prompts.txt](https://www.udacity.com/api/nodes/3055218617/supplemental_media/lesson-3-reflection-promptstxt/download) in the Downloadables section, you can download that file, commit it locally, push to GitHub, then add your response using the GitHub website.

## Reflect: Using a remote repository
Use the following reflection prompt:
    __When would you want to use a remote repository rather than keeping all your work local?__


# Concept Map: GitHub, Push, Pull, Remote
We’ve introduced a few new concepts since we last revisited our concept map.
+ GitHub
+ git push
+ git pull
+ remote

## Previous Version
Here’s what the map looked like the last time we added new concepts.
[!Concept Map from last time](https://lh5.ggpht.com/Z28RbAv_05Kk0yYk3MSBNqMIM8zRWSLL4rTmhwnX4oQ8Xwt30mndbKJT2vJ8bATFAiDomLL3O2VgUD2VUrk=s300)

## Where Do the New Concepts Go?
There's wasn't a lot of screen real estate left, so we pruned off some of the concepts from last lesson that aren't tightly entwined with the new ones that will come up this lesson, and added in nodes for the new concepts.

[!Which concept belongs where? Concept Map with blanks](https://lh3.ggpht.com/6cQ5xH6wnhnVXUanc5R2HE0-ayTaL-4eApx7F2D7gPiRCMmFET3lXH_WiC2GpU6yZm-RwNwA_v69TPZkJK0=s300#w=1800&h=1012)

In the following quiz, write in the concept that you think belongs in each new empty node.

Remember that this map is subjective, so what we have here may not fit your mental model exactly; feel free to draw out the connections you see between the concepts and share your version on the forums!


# Reflect: Manual vs. automatic pull
Now that you've both pushed changes to GitHub, and pulled changes from GitHub, add the following question and your thoughts on it to your reflections file:
    __Why might you want to always pull changes manually rather than having Git automatically stay up-to-date with your remote repository?__


# Fork The Recipes Repository
Larry's repository on GitHub can be found [here](https://github.com/LarryMad/recipes).


# Add a new recipe to the repository
On your own computer, add a new recipe for a food that you like and commit it on the master branch.

## Push your changes
Push the master branch to your fork. If you're having trouble remembering how to push, you may want to rewatch [this video](https://classroom.udacity.com/courses/ud775/lessons/3105028581/concepts/30736788930923#). When you're finished, continue to the next screen to answer a question about where your commit exists at different points in time.


# Forks, Clones, and Branches
Now that you've seen how you can make a copy of a repository on GitHub by forking it, go add the the following question and your thoughts on it to your reflections file:
    __Describe the differences between forks, clones, and branches. When would you use one instead of another?__


# Simulate Sarah's Changes
In the Downloadables section, there is a file called [sarah_changes.sh](https://www.udacity.com/api/nodes/3108878699/supplemental_media/sarah-changessh/download?_ga=1.34385894.672083044.1467344711), which contains code to make it look like Sarah has modified your fork on GitHub. To run the code, download the file, then using Git Bash or your terminal, cd to the directory where you've saved it. Then type `bash sarah_changes.sh` followed by a space, followed by the url to your fork. For example, if Caroline were running the code, she would type bash `sarah_changes.sh` https://github.com/cbuckey-uda/recipes.git, but you should use the url for your fork, not Caroline's fork. If you haven't set up password caching, then you will be prompted to enter your GitHub username and password.

# Which commits exist where?
The commit by Larry adding the chili recipe should have been in both places, since it was present in the original repository before you forked it. Your commit adding a new spice should only have been present locally, since you made the commit locally but didn't push. The commit by Sarah removing cumin should only have been present on GitHub, since Sarah made the change and pushed it to GitHub, but you didn't pull yet.


# Reflect: Local copies of remote branches
Now that you've seen how to update your local copy of remote branches, and how to combine conflicting changes from multiple people, add the following question and your thoughts on it to your reflections file:
    __What is the benefit of having a copy of the last known state of the remote stored locally?__


# Making A Pull Request
Suppose you run each of the given commands in order with the local `master` branch checked out. Check each place (working directory, staging area, local `master`, or GitHub `master`) where the files would be changed by that command.

Sarah accidentally says that the local master is the only thing that changes when you run `git pull origin master`. However, the working directory and staging area will also update when you run `git pull`. That's why when you run `git pull`, you see your files update, not just the `git log` output.


# Reflect: Collaboration using Git and GitHub
Now that you've seen how multiple people can share changes to a project using GitHub, and review proposed changes using pull requests, go add the following question and your thoughts on it to your reflections file:
    __How would you collaborate without using Git or GitHub? What would be easier, and what would be harder?__


# Updating Your Local Repository
You can download `sarah_changes_2.sh` [here](https://www.udacity.com/api/nodes/3106648623/supplemental_media/sarah-changes-2sh/download?_ga=1.238512199.672083044.1467344711)

## Simulate Sarah's changes
To simulate Sarah's changes, first download the file `sarah_changes_2.sh` from the Downloadables section. Then, using Git Bash or your terminal, cd to the directory where you've saved the file. Then type `bash sarah_changes_2.sh` followed by a space, followed by the url to your fork. For example, if Caroline were running the code, she would type `bash sarah_changes_2.sh https://github.com/cbuckey-uda/recipes.git`, but you should use the url for your fork, not Caroline's fork. If you haven't set up password-caching, then you will be prompted to enter your GitHub username and password.

Note: This code will not actually create a pull request. Instead, it will update the commit history on GitHub to make it look as though the pull request has already been merged. You will not need to merge a pull request. Instead, check for a commit on the master branch on GitHub with the message "Merge pull request".

## Make sure you are on the master branch
You'll want to make sure you check out the master branch before following the steps in this video.

## Make sure you are on the master branch
You'll want to make sure you check out the master branch before following the steps in the instructions video.

## Use `git add` on the conflicting files before committing
Just as in lesson 2, before running `git commit` to create the merge commit, you'll need to use `git add` to add any files that had conflicts to the staging area.


# Commit merging a pull request
After running git log -n 1, you should have seen output something like this:
> commit bc368511c6406028c77e2631f77c4d22a5da16d0
> Merge: 79fff84 23d1775
> Author: cbuckey 
> Date:   Tue Sep 30 18:50:28 2014 -0400
> 
>     Merge pull request #1 from cbuckey-uda/different-oil
> 
>     Change vegetable oil to canola oil

Notice that the commit message:
+ Indicates that a pull request was merged
+ Gives the number of the pull request (#1 here)
+ Gives the branch the pull request was merged from (cbuckey-uda/different-oil here).
+ Contains the title of the pull request.

GitHub automatically creates a commit message like this whenever a pull request is merged to make it easy to see pull requests in the commit history. Even when the merge is a fast-forward merge, GitHub still creates this commit.


# Concept Map: Fork, Fetch, Pull Request, Fast-Forward Merge
Here are the big new concepts we’ve introduced since we last revisited our concept map:
+ fork
+ fetch
+ pull request
+ fast-forward merge

## Previous Version
Here’s what the map looked like the last time we added new concepts.
[!Concept Map from last time](https://lh4.ggpht.com/wEnzBhcuYbVkhm9Np2M10M2WyL6hwyZntk7CQurM-40ivnwYZpcFDNYD7XLez3fw2mHSHfzxrjSUsVVoKQ=s350)

## Where Do the New Concepts Go?
Here's how we fit the new concepts in to the map. Which new concept belongs where?  
[!Concept Map with blanks](https://lh4.ggpht.com/08c6Bro_8Pv-IpiEBLkupgi6Z8EQI-5REm9ts1vf3BjkkGC2V3_lilY9P5vc-AjSBUUCNzV7TVf2klrTUogO=s350#w=1800&h=1012)

In the following quiz, write in the concept that you think belongs in each new empty node.

Remember that this map is subjective, so what we have here may not fit your mental model exactly; feel free to draw out the connections you see between the concepts and share your version on the forums!


# Concept Map: Fork, Fetch, Pull Request
You can see the [full final version](https://www.udacity.com/wiki/ud775/concept-map?nocache) of the concept map here, with all the nodes, including those we pruned in earlier versions.


# Reflect: When to use a separate branch
You just saw that the workflow when making changes in a separate branch is more complicated than working directly in master, especially when you need to stay up-to-date with changes others are making. Rather than simply pulling and pushing, you need to pull changes into your local master branch, merge the local master into your branch (different-oil, in our case), then push your branch to the remote before finally merging your branch into master, either locally or on GitHub.

Given that, please add the following question and your thoughts on it to your reflections file:
    __When would you want to make changes in a separate branch rather than directly in master? What benefits does each approach have?__


# Fork the repository and clone your fork
Now that you've learned how to fork a repository, push changes to your fork, and make a pull request, you’re ready to contribute to the create-your-own-adventure story that you saw at the beginning of the lesson. To do this, first you should fork [this repository](https://github.com/udacity/create-your-own-adventure). Then clone your fork, and make a branch to make your changes in.

Note: You could make your changes directly to the master branch in your fork, but when contributing to a public repository, it’s standard practice to make the changes in a non-master branch within the fork. This way, you can easily keep your master branch up-to-date with master of the original repository, and merge changes from master into your branch when you are ready.

Note for Windows Users: The story has grown so large that it exceeds Windows' path length limit. If you encounter an error when cloning you can work around it by modifying a configuration setting. Run this command in git bash: `git config --system core.longpaths true`.

## Make a change to the story
Next, you should actually make a change to the story. For instructions on how to do so, please read the [README](https://github.com/udacity/create-your-own-adventure/blob/master/README.md) in the create-your-own-adventure repository.

## Make a pull request
Next, you should make a pull request containing your changes to the original repository. To do this, click the "pull request" button from your branch like you did before, but this time, leave the original repository as the base.

## Ask for your pull request to be merged
You don't have permission to modify this repository, so you'll need someone at Udacity to merge your pull request. Our helpful bot Casey may be able to merge your pull request automatically. To have your pull request automatically merged, you'll need to follow the guidelines in the [README](https://github.com/udacity/create-your-own-adventure/blob/master/README.md) of the repository, and in addition you won't be able to delete or modify lines. That restriction on deletions is because Casey doesn't want to merge a request that accidentally deletes part of the story, and she can't tell the difference between an accidental deletion and an intentional modification. To request auto-merging, leave a comment on the pull request containing "@casey-collab". For example "Please review this, @casey-collab". Make sure to leave the comment on the "Conversation" tab of the pull request, not the "Files changed" tab.

There are some valid pull requests that Casey won't be able to merge. For example, she won't accept a pull request that fixes a typo, since that modifies a line. If you'd like to make a pull request Casey can't merge, feel free to do so, and someone from Udacity will merge the pull request if we have time. However, we can't guarantee a response to these pull requests.

## If needed, update your pull request
If someone merges your pull request or leaves a comment, GitHub will email you and let you know. If you're asked to make some changes, push those changes to your fork to update the pull request. Make sure you let the reviewer know that they should take another look!

If your pull request would result in a merge conflict, and you're not sure how to resolve it, see the next video for instructions.





Original refection contents
---------------------------

When would you want to use a remote repository rather than keeping all your work local?

    backup, collaboration, etc.

Why might you want to always pull changes manually rather than having Git automatically stay up-to-date with your remote repository?

    Sometimes changes might be changed again.  Manually pull is not necessary.

Describe the differences between forks, clones, and branches.  When would you use one instead of another?

    forks - only used in GitHub as clone with local repository
    clone - make a copy with remote users/GitHub
    branches - when adding new features, fixing bug, or doing experiment, a new brach will fork to prevent from modifying the original documents

What is the benefit of having a copy of the last known state of the remote stored locally?

    it will resolve the issue by changing same item by two or more different persons

How would you collaborate without using Git or GitHub?  What would be easier, and what would be harder?

    The collobration can use subversion or other version control sofyware.  However, Git it up-to-date methodology that make everything much easier.

When would you want to make changes in a separate branch rather than directly in master?  What benefits does each approach have?

    collobration with different thoughts from different people.  Seprate their own change in different braches until merge is required


Create a GitHub account
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/m-3105688910

In this lesson, you'll be sharing changes on GitHub, so you'll need a GitHub account. If you don't already have one, you can create an account by visiting github.com and clicking "Sign up for GitHub".

When you're asked to choose a plan, you can choose a free plan, since we won't be using any of the paid features in this course.

Set up Password Caching

Every time you send changes to GitHub via the command line, you'll need to type your password to prove that you have permission to modify the repository. This can get annoying quickly, so many people like to set up password caching, which will let you type your password once and have it auto-filled on that computer in the future. To do this, follow the instructions here. If you're using Windows and you followed our Git installation instructions earlier, you're using msysgit, so you can follow the instructions for msysgit.

	git config --global credential.helper wincred


Adding a Remote
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3073678893/m-3073678894

Copy the HTTPS URL, not the SSH URL!

At 1:29, Caroline copies the URL to the repository. The video mistakenly shows the URL to use if the repository is accessed over SSH. The course assumes that the student will use HTTPS, not SSH. Please click on the HTTPS button and copy the URL that shows up for HTTPS. It will begin with https:// rather than git@github.com.

If you are interested in using SSH instead, you can follow the instructions here, but this is not recommended unless you are already familiar with SSH keys.

Sharing your reflections

We encourage you to be bold in sharing your reflections on GitHub. If you're not happy with any of your responses, the best solution is to update that response in one or more new commits. The previous response will still be visible in the commit history, but updating your perspective over time is part of the learning process! Having a commit history that shows your updating perspective will reflect well on you, not poorly.

That said, if you've written anything in your reflections repository that you are not comfortable sharing, you can checkout the commit before you introduced that change, create a new branch at that point, and commit any other changes you are willing to share to the new branch. Then, by only pushing your new branch, you can keep the changes on your original branch private.



Concept Map: GitHub, Push, Pull, Remote
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3154688535/m-3127058545

We’ve introduced a few new concepts since we last revisited our concept map.

GitHub
git push
git pull
remote
Previous Version

Here’s what the map looked like the last time we added new concepts.

Concept Map from last time

Where Do the New Concepts Go?

There's wasn't a lot of screen real estate left, so we pruned off some of the concepts from last lesson that aren't tightly entwined with the new ones that will come up this lesson, and added in nodes for the new concepts.

Which concept belongs where? Concept Map with blanks

In the following quiz, write in the concept that you think belongs in each new empty node.

Remember that this map is subjective, so what we have here may not fit your mental model exactly; feel free to draw out the connections you see between the concepts and share your version on the forums!



Add a new recipe to the repository
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3077038991/m-3050368892

On your own computer, add a new recipe for a food that you like and commit it on the master branch.

Push your changes

Push the master branch to your fork. If you're having trouble remembering how to push, you may want to rewatch this video (https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3073678893/m-3073678894). When you're finished, continue to the next screen to answer a question about where your commit exists at different points in time.



Where was your commit?
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3077038991/m-3060868831

Before you ran git push, your change should have only existed locally via git log. Commits will not automatically be shared to remotes - you have to manually push your branch if you want to share changes.

After you ran git push, your change should have existed locally and on your fork. It should not have existed on Larry's repository, which is the repository you forked. The reason you forked in the first place is because you don't have permission to change Larry's repository!



git pull origin master = git fetch origin (remote repository master) + git merge master origin/master (merge both local master and remote master)

hmchen (master) recipes $ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        sarah_changes.sh

nothing added to commit but untracked files present (use "git add" to track)
hmchen (master) recipes $ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
hmchen (master) recipes $ git fetch origin
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 1
Unpacking objects: 100% (3/3), done.
From https://github.com/hmchen47/recipes
   a6a2f99..896f807  master     -> origin/master

 
 Making a Pull Request Solution
 URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3328228620/m-3307938831

Sarah accidentally says that the local master is the only thing that changes when you run git pull origin master. However, the working directory and staging area will also update when you run git pull. That's why when you run git pull, you see your files update, not just the git log output.


hmchen (master) recipes $ git branch different-oil
hmchen (master) recipes $ git checkout different-oil
Switched to branch 'different-oil'
hmchen (different-oil) recipes $ git branch
* different-oil
  master
hmchen (different-oil) recipes $ git status
On branch different-oil
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   cake-recipe.txt

hmchen (different-oil *) recipes $ git add cake-recipe.txt
hmchen (different-oil +) recipes $ git commit -m 'oil change'
[different-oil 1439f08] oil change
 1 file changed, 1 insertion(+), 1 deletion(-)
hmchen (different-oil) recipes $ git push origin different-oil
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 298 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To https://github.com/hmchen47/recipes.git
 * [new branch]      different-oil -> different-oil

git pull from GitHub


Simulate Sarah's changes
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3106648622/m-3106648623

To simulate Sarah's changes, first download the file sarah_changes_2.sh from the Downloadables section. Then, using Git Bash or your terminal, cd to the directory where you've saved the file. Then type bash sarah_changes_2.sh followed by a space, followed by the url to your fork. For example, if Caroline were running the code, she would type bash sarah_changes_2.sh https://github.com/cbuckey-uda/recipes.git, but you should use the url for your fork, not Caroline's fork. If you haven't set up password-caching, then you will be prompted to enter your GitHub username and password.

Note: This code will not actually create a pull request. Instead, it will update the commit history on GitHub to make it look as though the pull request has already been merged. You will not need to merge a pull request. Instead, check for a commit on the master branch on GitHub with the message "Merge pull request".

Make sure you are on the master branch

You'll want to make sure you check out the master branch before following the steps in this video.


Commit merging a pull request
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3062598627/m-3060778977

After running git log -n 1, you should have seen output something like this:

commit bc368511c6406028c77e2631f77c4d22a5da16d0
Merge: 79fff84 23d1775
Author: cbuckey 
Date:   Tue Sep 30 18:50:28 2014 -0400

    Merge pull request #1 from cbuckey-uda/different-oil

    Change vegetable oil to canola oil
Notice that the commit message:

Indicates that a pull request was merged
Gives the number of the pull request (#1 here)
Gives the branch the pull request was merged from (cbuckey-uda/different-oil here).
Contains the title of the pull request.

Concept Map: Fork, Fetch, Pull Request, Fast-Forward Merge
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/e-3138278543/m-3125038547

Here are the big new concepts we’ve introduced since we last revisited our concept map:

fork
fetch
pull request
fast-forward merge


Previous Version (conceptmap4.png)

Here’s what the map looked like the last time we added new concepts.

Concept Map from last time (conceptmap5.jpg)

Where Do the New Concepts Go?

Here's how we fit the new concepts in to the map. Which new concept belongs where? Concept Map with blanks

In the following quiz, write in the concept that you think belongs in each new empty node.

Remember that this map is subjective, so what we have here may not fit your mental model exactly; feel free to draw out the connections you see between the concepts and share your version on the forums!


Modifying the Adventure Repository
URL: https://www.udacity.com/course/viewer#!/c-ud775/l-3105028581/m-3080679121

Fork the repository and clone your fork

Now that you've learned how to fork a repository, push changes to your fork, and make a pull request, you’re ready to contribute to the create-your-own-adventure story that you saw at the beginning of the lesson. To do this, first you should fork this repository. Then clone your fork, and make a branch to make your changes in.

Note: You could make your changes directly to the master branch in your fork, but when contributing to a public repository, it’s standard practice to make the changes in a non-master branch within the fork. This way, you can easily keep your master branch up-to-date with master of the original repository, and merge changes from master into your branch when you are ready.

Make a change to the story

Next, you should actually make a change to the story. For instructions on how to do so, please read the README in the create-your-own-adventure repository.

Make a pull request

Next, you should make a pull request containing your changes to the original repository. To do this, click the "pull request" button from your branch like you did before, but this time, leave the original repository as the base.

Ask for your pull request to be merged

You don't have permission to modify this repository, so you'll need someone at Udacity to merge your pull request. Our helpful bot Casey may be able to merge your pull request automatically. To have your pull request automatically merged, you'll need to follow the guidelines in the README of the repository, and in addition you won't be able to delete or modify lines. That restriction on deletions is because Casey doesn't want to merge a request that accidentally deletes part of the story, and she can't tell the difference between an accidental deletion and an intentional modification. To request auto-merging, leave a comment on the pull request containing "@casey-collab". For example "Please review this, @casey-collab". Make sure to leave the comment on the "Conversation" tab of the pull request, not the "Files changed" tab.

There are some valid pull requests that Casey won't be able to merge. For example, she won't accept a pull request that fixes a typo, since that modifies a line. If you're taking the course for free and you'd like to make a pull request Casey can't merge, feel free to do so, and someone from Udacity will merge the pull request if we have time. However, we can't guarantee a response to these pull requests, unless you are enrolled in the paid version of the course. In that case, you can ask your project evaluator to merge your pull request. See the final project instructions for more details.

If needed, update your pull request

If someone merges your pull request or leaves a comment, GitHub will email you and let you know. If you're asked to make some changes, push those changes to your fork to update the pull request. Make sure you let the reviewer know that they should take another look!

If your pull request would result in a merge conflict, and you're not sure how to resolve it, see the next video for instructions.


