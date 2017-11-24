#!/bin/bash

echo "Please enter the first number "
read first
echo "Please enter teh second number "
read second
echo

if [ $first -eq 0 ] && [ $second -eq 0 ]
then
    echo "Num1 and Num2 are zero."
elif [ $first -eq $second ]
then
    echo "Both values ($first) are equal"
elif [ $first -gt $second ]
then
    echo "$first is greather than $second"
else
    echo "$first is less than $second"
fi