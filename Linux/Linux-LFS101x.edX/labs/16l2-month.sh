#!/bin/bash

echo -n "Enter a numeric value (1~12) to covert to the month: "
read mon
echo

case "$mon" in
    "1")    echo "This is January.";;
    "2")    echo "This is Feburary.";;
    "3")    echo "This is March.";;
    "4")    echo "This is April.";;
    "5")    echo "This is May.";;
    "6")    echo "This is June.";;
    "7")    echo "This is July.";;
    "8")    echo "This is August.";;
    "9")    echo "This is September.";;
    "10")   echo "This is October.";;
    "11")   echo "This is November.";;
    "12")   echo "This is December.";;
    *)    echo "Invalid value ($mon)";;
esac
