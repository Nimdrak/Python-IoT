#!/bin/bash

############################
####### ARP setting ########
############################

echo arp_setting! type the password lanada
/home/controller/IoT/arp_setting/arp_setting_con.sh


##############################
####### Basic setting ########
##############################

echo 'switch 1'
ssh switch1@191.0.0.1 ./basic_setting.sh
echo 'switch 2'
ssh switch2@191.0.0.2 ./basic_setting.sh
echo 'switch 3'
ssh switch3@191.0.0.3 ./basic_setting.sh
echo 'switch 4'
ssh switch4@191.0.0.4 ./basic_setting.sh



####################################
####### Periodic arp update ########
####################################

/home/controller/IoT/arp_setting/new_arp_setting_periodic.sh




