#!/bin/bash

for p  in {1..100000};do

/home/controller/IoT/arp_setting/arp_setting_con.sh

echo "p == $p"
sleep 10

done

