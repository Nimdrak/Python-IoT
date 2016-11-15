#!/bin/bash 

if [ $# == 0 ]; then
  echo Please read the man page for the wondershaper and 
  echo the file /usr/share/doc/wondershaper/README.Debian
  exit
fi

if [ $# == 1 ]; then
  /sbin/tc -s qdisc ls dev $1
  /sbin/tc -s class ls dev $1
  exit
fi

if [ "$2" == "del" ]; then
  /sbin/tc qdisc del dev $1 root    2> /dev/null > /dev/null
  echo Wondershaper queues have been cleared.
  exit
fi

# please read the README before filling out these values 
#
# Set the following values to somewhat less than your actual download
# and uplink speed. In kilobits. Also set the device that is to be shaped.
UPLINK=$2
DEV=$1

#########################################################

# clean existing down- and uplink qdiscs, hide errors
/sbin/tc qdisc del dev $DEV root    2> /dev/null > /dev/null

###### uplink

# install root HTB

/sbin/tc qdisc add dev $DEV root handle 1:0 htb default 15 

# main class

/sbin/tc class add dev $DEV parent 1:0 classid 1:1 htb rate ${UPLINK}mbit 

# high prio class 1:5

/sbin/tc class add dev $DEV parent 1:1 classid 1:5 htb rate $(($UPLINK/2))mbit \
    ceil ${UPLINK}mbit prio 2

# bulk and default class 1:10 - gets slightly less traffic, 
#  and a lower priority:

/sbin/tc class add dev $DEV parent 1:1 classid 1:10 htb rate $(($UPLINK/2))mbit \
    ceil ${UPLINK}mbit prio 6

# 'traffic we hate'

/sbin/tc class add dev $DEV parent 1:1 classid 1:15 htb rate $(($UPLINK/2))mbit \
    ceil ${UPLINK}mbit prio 10

# all get Stochastic Fairness:
/sbin/tc qdisc add dev $DEV parent 1:5 handle 5: sfq perturb 10
/sbin/tc qdisc add dev $DEV parent 1:10 handle 10: sfq perturb 10
/sbin/tc qdisc add dev $DEV parent 1:15 handle 15: sfq perturb 10
