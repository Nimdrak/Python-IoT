#!/bin/bash

#scp /home/controller/.ssh/id_rsa.pub pi@$1:id_rsa.pub
#scp /home/controller/IoT/ssh_key_setting/ssh_setting.sh pi@$1:ssh_setting.sh

#ssh pi@$1 ./ssh_setting.sh


scp /home/controller/IoT/dummy/ovs_setting/basic_setting.sh switch1@191.0.0.1:basic_setting.sh

scp /home/controller/IoT/dummy/ovs_setting/basic_setting.sh switch2@191.0.0.2:basic_setting.sh

scp /home/controller/IoT/dummy/ovs_setting/basic_setting.sh switch3@191.0.0.3:basic_setting.sh

scp /home/controller/IoT/dummy/ovs_setting/basic_setting.sh switch4@191.0.0.4:basic_setting.sh

