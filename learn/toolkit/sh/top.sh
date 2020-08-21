#!/bin/sh

# top.sh
# ´òÓ¡ÄÚ´æÏûºÄ

TMP_FILE="/tmp/ps.tmp"

ps > $TMP_FILE

v_process=$(cat $TMP_FILE | grep "ambarella_test" | awk '{print $1}')

while true
do
        echo 3 > /proc/sys/vm/drop_caches
        date
        cat /proc/$v_process/maps
        cat /proc/$v_process/status
        cat /proc/meminfo
        top -b -n 1
        sleep 30
done