#!/bin/sh

while true
do
    ifconfig | grep "inet addr"
    sleep 10
done