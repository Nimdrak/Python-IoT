#!/bin/bash

for p  in {1..100000};do

sudo arp -s 192.0.0.1 90:9f:33:ee:83:d4
sudo arp -s 192.0.0.2 90:9f:33:ee:83:c1 
sudo arp -s 192.0.0.3 90:9f:33:ee:83:c5  
sudo arp -s 192.0.0.4 90:9f:33:ee:83:e3   


sudo arp -s 192.0.0.200 00:1f:d0:9a:01:bd



#OVS
scp /home/controller/IoT/arp_setting/new_arp_setting.sh switch1@191.0.0.1:/home/switch1
scp /home/controller/IoT/arp_setting/new_arp_setting.sh switch2@191.0.0.2:/home/switch2
scp /home/controller/IoT/arp_setting/new_arp_setting.sh switch3@191.0.0.3:/home/switch3
scp /home/controller/IoT/arp_setting/new_arp_setting.sh switch4@191.0.0.4:/home/switch4



ssh switch1@191.0.0.1 ./new_arp_setting.sh
ssh switch2@191.0.0.2 ./new_arp_setting.sh
ssh switch3@191.0.0.3 ./new_arp_setting.sh
ssh switch4@191.0.0.4 ./new_arp_setting.sh

echo "p == $p"
sleep 10

done

