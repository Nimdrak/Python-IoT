#!/bin/bash
a=$(ssh server@192.0.0.112 ps -ef|grep "iperf"|awk '{print $2}')
echo $a
#ssh pi@192.0.0.110 kill -9 $a

