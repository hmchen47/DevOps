#!/bin/bash

# Prompts the user for a directory name and then creates it  with mkdir.

echo "Give a directory name to create:" 
read NEW_DIR

# Save original directory so we can return to it (could also just use pushd, popd)

ORIG_DIR=$(pwd)

# check to make sure it doesn't already exist!

[[ -d $NEW_DIR ]] && echo $NEW_DIR already exists, aborting && exit 
mkdir $NEW_DIR

# Changes to the new directory and prints out where it is using pwd.  

cd $NEW_DIR
pwd

# prompt to ask how many files to create
echo "How many files to create? "
read FNUM

# Using touch, creates several empty files and runs ls on them to verify they are empty.

# for n in 1 2 3 4
for n in $(seq 1 $FNUM)
do 
    touch file$n 
done

ls file?

# (Could have just done touch file1 file2 file3 file4, just want to show do loop!)

# Puts some content in them using echo and redirection.

for names in file?  
do 
    echo This file is named $names > $names
done

# Displays their content using cat

cat file?

# Says goodbye to the user and cleans up after itself 

cd $ORIG_DIR 
rm -rf $NEW_DIR 
echo "Goodbye My Friend!"


#!/bin/bash
# mkdir $1; cd $1; echo $(pwd); \
# touch file$2 file$3 file$4; \
# echo This is File1 > file$2; \
# echo This is File2 > file$3; \
# echo This is File3 > file$4; \
# cat file$2 file$3 file$4; \
# echo Goodby\!; \
# cd ../; rm -r $1