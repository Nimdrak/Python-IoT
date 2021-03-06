#!/bin/bash 

# need to do at the client(sender) side
# OVS1 of:000000259006798c
# OVS2 of:00000025900b66fe
# OVS3 of:00000025900ca3f4
# OVS4 of:0000002590322dca

echo "$1 Mbps is link bandwidth [->] ovs 1 and ovs 2, port 4, eth3"
echo "$1 Mbps is link bandwidth [->] ovs 2 and ovs 1, port 2, eth1"

ssh ovs@192.0.0.1 sudo ./link_capacity_control.sh eth3 $1
ssh ovs@192.0.0.2 sudo ./link_capacity_control.sh eth1 $1

 
echo "$2 Mbps is link bandwidth [->] ovs 1 and ovs 3, port 2, eth2"
echo "$2 Mbps is link bandwidth [->] ovs 3 and ovs 1, port 2, eth1"

ssh ovs@192.0.0.1 sudo /home/ovs/link_capacity_control.sh eth1 $2
ssh ovs@192.0.0.3 sudo /home/ovs/link_capacity_control.sh eth1 $2


echo "$3 Mbps is link bandwidth [->] ovs 2 and ovs 3, port 3, eth4"
echo "$3 Mbps is link bandwidth [-<] ovs 3 and ovs 2, port 6, eth5"

ssh ovs@192.0.0.2 sudo /home/ovs/link_capacity_control.sh eth4 $3
ssh ovs@192.0.0.3 sudo /home/ovs/link_capacity_control.sh eth5 $3


echo "$4 Mbps is link bandwidth [->] ovs 2 and ovs 4, port 4, eth5"
echo "$4 Mbps is link bandwidth [->] ovs 4 and ovs 2, port 5, eth6"

ssh ovs@192.0.0.2 sudo /home/ovs/link_capacity_control.sh eth5 $4
ssh ovs@192.0.0.4 sudo /home/ovs/link_capacity_control.sh eth6 $4


echo "$5 Mbps is link bandwidth [->] ovs 3 and ovs 4, port 5, eth4"
echo "$5 Mbps is link bandwidth [<-] ovs 4 and ovs 3, port 2, eth1"

ssh ovs@192.0.0.3 sudo /home/ovs/link_capacity_control.sh eth4 $5
ssh ovs@192.0.0.4 sudo /home/ovs/link_capacity_control.sh eth1 $5






