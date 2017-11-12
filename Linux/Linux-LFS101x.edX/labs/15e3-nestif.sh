#!/bin/bash
echo "Enter the first number"
read inp1

echo "Enter the second number"
read inp2

echo 
echo "1. Addition"
echo "2. Substraction"
echo "3. Multiplication"
echo -n "Please choose a word [1, 2, or 3]? "
read oper
echo " "

# if [ ( $oper -ne 1 ) || ( $oper -ne 2 ) || ( $oper -ne 3 ) ]; then
#     echo "Entered value not 1, 2 or 3"
#     exit 1
# fi

if [ $oper -eq 1 ]
then
    echo "Addition result " $(($inp1 + $inp2))
else
    if [ $oper -eq 2 ]
    then
        echo "Substraction result " $(($inp1 - $inp2))
    else
        if [ $oper -eq 3 ]
        then
            echo "Multiplication result " $(($inp1 * $inp2))
        fi
    fi
fi
