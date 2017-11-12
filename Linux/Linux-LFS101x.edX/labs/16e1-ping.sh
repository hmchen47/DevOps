#!/bin/bash

echo "Enter IP address"
read ip
echo 

if [ ! -z $ip ]; then
    ping -c 3 $ip
    if [ $? -eq 0 ]; then
        echo
        echo "Machine is giving ping response"
    else
        echo
        echo "Machine is not giving ping response"
    fi
else
    echo
    echo "IP address is empty"
fi
