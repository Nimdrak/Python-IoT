#!/bin/bash


for p  in {1..100000};do


for q  in {1..300};do
/home/controller/IoT/arp_setting/arp_setting_con_wire.sh


echo wait 3 seconds
sleep 3
echo "p $p q $q"

done

#/home/controller/IoT/arp_setting/arp_setting_con.sh
#echo "p $p"
#sleep 3

done

