#!/bin/bash

for filename in $(ls)
do
    # take extension available in a filename
    ext=${filename##*\.}
    case "$ext" in
        c)      echo "$filename : C source file"
        ;;
        o)      echo "$filename : Object file"
        ;;
        sh)     echo "$filename : Shell file"
        ;;
        txt)    echo "$filename : Text file"
        ;;
        *)      echo "$filename : Unknow file type/not processed"
        ;;
    esac
done
