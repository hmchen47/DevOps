#!/bin/bash

echo -n "Enter the first string: "
read str1
echo -n "Enter the second string: "
read str2

echo $str1; echo $str2

myLen1=${#str1}
myLen2=${#str2}

echo Length of the first string is: $myLen1
echo Length of the first string is: $myLen2
