#!/bin/bash

echo -e "Enter absolute path of the file name you want to read"
read file
echo

exec < $file    # redirect strin to a file
if [ $? -ne 0 ]; then
    echo
    echo "$file not existed"
    exit 1
fi

while read line
do
    echo $line
done
