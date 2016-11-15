#!/bin/bash

echo "ovs1"
ssh ovs@192.0.0.1 rm ./link_capacity_control.sh
echo "ovs2"
ssh ovs@192.0.0.2 rm ./link_capacity_control.sh
echo "ovs3"
ssh ovs@192.0.0.3 rm ./link_capacity_control.sh
echo "ovs4"
ssh ovs@192.0.0.4 rm ./link_capacity_control.sh

scp /home/controller/IoT/link_control/link_capacity_control.sh ovs@192.0.0.1:/home/ovs
scp /home/controller/IoT/link_control/link_capacity_control.sh ovs@192.0.0.2:/home/ovs
scp /home/controller/IoT/link_control/link_capacity_control.sh ovs@192.0.0.3:/home/ovs
scp /home/controller/IoT/link_control/link_capacity_control.sh ovs@192.0.0.4:/home/ovs

echo "link bandwidth initialization [->] ovs 1 and ovs 2"
echo "link bandwidth initialization [->] ovs 2 and ovs 1"

ssh ovs@192.0.0.1 sudo /sbin/tc qdisc del dev eth3 root
ssh ovs@192.0.0.2 sudo /sbin/tc qdisc del dev eth1 root

 
echo "link bandwidth initialization [->] ovs 1 and ovs 3"
echo "link bandwidth initialization [->] ovs 3 and ovs 1"

ssh ovs@192.0.0.1 sudo /sbin/tc qdisc del dev eth1 root
ssh ovs@192.0.0.3 sudo /sbin/tc qdisc del dev eth1 root


echo "link bandwidth initialization [->] ovs 2 and ovs 3"
echo "link bandwidth initialization [-<] ovs 3 and ovs 2"

ssh ovs@192.0.0.2 sudo /sbin/tc qdisc del dev eth4 root
ssh ovs@192.0.0.3 sudo /sbin/tc qdisc del dev eth5 root


echo "link bandwidth initialization [->] ovs 2 and ovs 4"
echo "link bandwidth initialization [->] ovs 4 and ovs 2"

ssh ovs@192.0.0.2 sudo /sbin/tc qdisc del dev eth5 root
ssh ovs@192.0.0.4 sudo /sbin/tc qdisc del dev eth6 root


echo "link bandwidth initialization [->] ovs 3 and ovs 4"
echo "link bandwidth initialization [<-] ovs 4 and ovs 3"

ssh ovs@192.0.0.3 sudo /sbin/tc qdisc del dev eth4 root
ssh ovs@192.0.0.4 sudo /sbin/tc qdisc del dev eth1 root

echo "link limitation is finished"



