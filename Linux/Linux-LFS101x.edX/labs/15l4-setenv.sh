#!/bin/bash

echo "Enter 1 or 2, to set the environmental variable EVAR to Yes or No"
read ans

# Set up a return code
RC=0

if [ $ans -eq 1 ]  
then 
    export EVAR="Yes"
else
    if [ $ans -eq 2 ]
    then
	export EVAR="No"
    else
# can only reach here with a bad answer
	export EVAR="Unknown"
	RC=1
    fi    
fi
echo "The value of EVAR is: $EVAR"
exit $RC












#!/bin/bash

# # Read in the number 
# echo "Please enter the number 1 or 2"; read NUM

# echo 
# echo "enter: $NUM"

# # check the number
# if [($NUM != "1") && ($NUM != "2")]; then
#     echo "Enter $NUM, but only 1 & 2 acceptable"
#     exit 1
# fi


