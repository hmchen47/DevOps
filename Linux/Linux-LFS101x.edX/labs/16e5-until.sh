#!/bin/bash

number=0

until [ $number -ge 10 ]; do
    echo "Number = $number"
    number=$(($number + 1))
done
