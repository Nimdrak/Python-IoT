#!/bin/bash

sudo arp -s 192.0.0.1 90:9f:33:ee:83:d4
sudo arp -s 192.0.0.2 90:9f:33:ee:83:c1 
sudo arp -s 192.0.0.3 90:9f:33:ee:83:c5  
sudo arp -s 192.0.0.4 90:9f:33:ee:83:e3   

sudo arp -s 192.0.0.11 6c:62:6d:d0:7c:67
sudo arp -s 192.0.0.21 1c:1b:0d:29:6b:d2
sudo arp -s 192.0.0.31 1c:1b:0d:29:6b:d1
sudo arp -s 192.0.0.41 1c:1b:0d:29:6d:1c 

sudo arp -s 192.0.0.200 00:1f:d0:9a:01:bd



###scp arp_setting.sh
#ssh server@193.0.0.11 rm ./arp_setting.sh
#ssh server@193.0.0.21 rm ./arp_setting.sh
#ssh server@193.0.0.31 rm ./arp_setting.sh
#ssh server@193.0.0.41 rm ./arp_setting.sh

#ssh switch1@191.0.0.1 rm ./arp_setting.sh
#ssh switch2@191.0.0.2 rm ./arp_setting.sh
#ssh switch3@191.0.0.3 rm ./arp_setting.sh
#ssh switch4@191.0.0.4 rm ./arp_setting.sh




#Host
scp /home/controller/IoT/arp_setting/arp_setting.sh server@193.0.0.11:/home/server
scp /home/controller/IoT/arp_setting/arp_setting.sh server@193.0.0.21:/home/server
scp /home/controller/IoT/arp_setting/arp_setting.sh server@193.0.0.31:/home/server
scp /home/controller/IoT/arp_setting/arp_setting.sh server@193.0.0.41:/home/server



#OVS
scp /home/controller/IoT/arp_setting/arp_setting.sh switch1@191.0.0.1:/home/switch1
scp /home/controller/IoT/arp_setting/arp_setting.sh switch2@191.0.0.2:/home/switch2
scp /home/controller/IoT/arp_setting/arp_setting.sh switch3@191.0.0.3:/home/switch3
scp /home/controller/IoT/arp_setting/arp_setting.sh switch4@191.0.0.4:/home/switch4


###setting arp_setting.sh
ssh server@193.0.0.11 ./arp_setting.sh
ssh server@193.0.0.21 ./arp_setting.sh
ssh server@193.0.0.31 ./arp_setting.sh
ssh server@193.0.0.41 ./arp_setting.sh

ssh switch1@191.0.0.1 ./arp_setting.sh
ssh switch2@191.0.0.2 ./arp_setting.sh
ssh switch3@191.0.0.3 ./arp_setting.sh
ssh switch4@191.0.0.4 ./arp_setting.sh


