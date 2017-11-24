#!/bin/bash
#
# check for an argument, print a usage message if not supplied.
#
if [ $# != 1 ] ; then
      echo "Usage: $0 without or more than one argument"
      echo $*
      exit 1
fi
echo "Usage: $0 with argument $1"
exit 0