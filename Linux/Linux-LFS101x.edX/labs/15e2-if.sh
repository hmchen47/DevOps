#!/bin/bash

file=$1

if [ -f $file ]
then
    echo "The $file exists"
else
    echo "The $file does not exist"
fi