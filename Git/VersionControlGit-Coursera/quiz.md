Version Control with Git
========================

by Atlassian

# Module 1 Assessment
1. Which one of these statements about Git is true?

        A. Git helps manage the history of the project.
        B. Each version of the project is called a branch.
        C. A commit containing one small change to a project is not practical.

        Ans: A
        This is covered in 'DevOps and Git in a Nutshell'.


2. Which one of these statements about branches is true?

        A. The default branch is named "master".
        B. A branch contains a small part of the project.
        C. By default, a commit does not belong to a branch.

        Ans: A
        This is covered in 'DevOps and Git in a Nutshell'.


3. What is a request to merge your branch into another branch called?

        A. Code review
        B. Automated test
        C. Pull request

        Ans: C
        This is covered in 'DevOps and Git in a Nutshell'.


4. If a remote repository is offline, which one of the following is true?

        A. You must wait for the remote repository to become available.
        B. You can continue to work with the local repository.
        C. You can continue to work, but only with the current version of the project.

        Ans: B
        This is covered in 'DevOps and Git in a Nutshell'.


5. Which one of the following is true?

        A. Git does not scale to large projects.
        B. Git is owned by a single company.
        C. Git implements distributed version control.

        Ans: C
        This is covered in 'Git Overview'.


6. Which one of these statements about commits is true?

        A. A commit contains only the changes to the project since the previous commit.
        B. A commit is a snapshot of the project.
        C. Only the most recent commit is saved in the repository.

        Ans: B
        This is covered in 'Git Overview'.


7. Which location contains the list of files that will be included in the next commit?

        A. Working tree
        B. Remote repository
        C. Branch
        D. Staging area

        Ans: D
        This is covered in 'Git Locations'.


8. Which location contains the commit history of a project?

        A. Staging area
        B. Remote repository
        C. Branch
        D. Working tree

        Ans: B
        This is covered in 'Git Locations'.


9. When a file is first placed in the working tree, what is its status?

        A. Staged
        B. Modified
        C. Untracked
        D. Committed

        Ans: C
        This is covered in 'Commit to a Local Repository'.


10. What must you do to add a new file to the next commit?

        A. Push the file.
        B. Add the file to the staging area.
        C. Tag the file.
        D. Check out the file.

        Ans: B
        This is covered in 'Commit to a Local Repository'.


11. If you create a local repository in a folder with existing files, what will be the status of the files?

        A. Staged
        B. Untracked
        C. Committed
        D. Modified

        Ans: B
        This is covered in 'Commit to a Local Repository'.


12. Immediately after you commit, where is the commit located?

        A. Neither repository
        B. Remote repository
        C. Local repository
        D. Local repository and remote repository

        Ans: C
        This is covered in 'Commit to a Local Repository'.

13. Which one of these statements about remote repositories is true?

        A. A remote repository usually has a working tree.
        B. A remote repository usually has a staging area.
        C. By convention, remote repository names end in ".git".
        D. You must have one remote repository for each local repository.

        Ans: C
        This is covered in 'Create a Remote Repository'.

14. What is a local copy of a remote repository called?

        A. Branch
        B. Origin
        C. Clone
        D. Master

        Ans: C
        This is covered in 'Push to a Remote Repository'.

15. After you clone a repository, which one of the following is true?

        A. New commits to the local repository will automatically be pushed to the remote repository.
        B. The remote repository information is available in the local repository.
        C. New commits on the remote repository will automatically be added to the local repository.
        D. Only the most recent commit is available locally.

        Ans: B
        This is covered in 'Push to a Remote Repository'.

16. What is origin?

        A. The default branch name.
        B. The first version of a file in the repository.
        C. An alias for the remote repository's URL.
        D. The first commit of the repository.

        Ans: C
        This is covered in 'Push to a Remote Repository'.


17. What must you do to add a local commit to the remote repository?

        A. Push
        B. Stage
        C. Pull
        D. Merge

        Ans: A
        This is covered in 'Push to a Remote Repository'.


# Module 2 Assessment
1. In Git, what is modeled as a directed acyclic graph?

        A. The staging area.
        B. The working tree.
        C. The commit history.

        Ans: C
        This is covered in 'Git's Graph Model'.


2. How are Git commits connected?

        A. A commit object contains the SHA-1 of its child or children.
        B. A commit references its parent(s).
        C. The staging area lists the connections.

        Ans: B
        This is covered in 'Git's Graph Model'.

3. What is a Git ID?

        A. The name of a Git object.
        B. The ID of the local repository.
        C. The user's name and email address.

        Ans: A
        This is covered in 'Git IDs'.


4. If a large file changes by one character, what would you expect to happen to its corresponding SHA-1 value?

        A. It would slightly change.
        B. It would not change.
        C. It would change drastically.

        Ans: C
        This is covered in 'Git IDs'.


5. What do branch labels point to?

        A. The most recent commit of a branch.
        B. The initial commit of a branch.
        C. Every commit of a branch.

        Ans: A
        This is covered in 'References'.


6. How many HEAD references are in a local repository?

        A. One for each branch label.
        B. One for each commit.
        C. One.

        Ans: C
        This is covered in 'References'.


7. Which one of these statements is correct?

        A. A tag always points to a specific commit.
        B. A tag is another name for a branch label.
        C. The HEAD reference always points to a tag.

        Ans: A
        This is covered in 'References'.


8. What happens when a branch is created?

        A. The HEAD reference changes.
        B. A branch label is created.
        C. Commits are copied.

        Ans: B
        This is covered in 'Branches'.


9. Which one of these statements is correct?

        A. Checkout updates the working tree and HEAD reference.
        B. Checkout prevents others from changing a branch.
        C. Checkout retrieves content from the remote repository.

        Ans: A
        This is covered in 'Branches'.


10. What does a detached HEAD mean?

        A. The HEAD reference does not point to anything.
        B. The HEAD reference points to a branch label.
        C. The HEAD reference points directly to a commit SHA-1.

        Ans: C
        This is covered in 'Branches'.


11. What does "deleting a branch" immediately do?

        A. Deletes all of the commits of the branch.
        B. Deletes a branch label.
        C. Deletes only the commits that are unique to the branch.

        Ans: B
        This is covered in 'Branches'.


12. Which one of the following statements is true?

        A. A commit can only belong to one branch at a time.
        B. A merge always creates a new commit.
        C. Merging combines the work of branches.

        ANs: C
        This is covered in 'Merging'.


13. Which one of the following statements about fast-forward merges is true?

        A. The merge moves a branch label.
        B. The merge may change some commits.
        C. The merge may result in a merge conflict.

        Ans: A
        This is covered in 'Merging'.

14. If Git informs you that a fast-forward merge is not possible, which one of these statements is probably true?

        A. The merge has merge conflicts.
        B. The checked out commit has multiple parents.
        C. A commit was made on the base branch after the topic branch was created.

        Ans: C
        This is covered in 'Merging'.


15. Which one of these statements is true?

        A. The files in the working tree change after a fast-forward merge.
        B. A fast-forward merge results in a non-linear commit history.
        C. To perform a fast-forward merge, checkout the topic branch.

        Ans: A
        This is covered in 'Merging'.


16. Which one of these statements about a merge involving a merge commit is true?

        A. A merge commit results in a linear commit history.
        B. The merge is aborted if there are merge conflicts.
        C. Git places the result of the merge into a new commit.

        Ans: C
        This is covered in 'Merging'.








