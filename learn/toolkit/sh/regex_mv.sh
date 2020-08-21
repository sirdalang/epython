#!/bin/bash

if [ -z "$1" ];then 
    echo "null destination"
    exit 0
fi

v_files=$(find . | grep '\.sh$')
echo ""
echo "Move "
echo $v_files
echo "to "
echo $1

read -r -p "Please Confirm (ctrl-c to exit):  " input

v_filenumber=0
for v_file in $v_files
do 
    mv $v_file $1/
    let "v_filenumber += 1"
done

echo "Move Finished($v_filenumber files)! "