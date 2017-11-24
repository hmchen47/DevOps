#!/bin/bash

echo -n "Entera number: "
read count

if [ $count -eq 100 ]
then
    echo "Count is 100."
elif [ $count -gt 100 ]
then
    echo "Count is greater than 100."
else
    echo "Counter is less than 100."
fi