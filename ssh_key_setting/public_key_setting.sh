#!/bin/bash

#scp /home/controller/.ssh/id_rsa.pub pi@$1:id_rsa.pub
#scp /home/controller/IoT/ssh_key_setting/ssh_setting.sh pi@$1:ssh_setting.sh

#ssh pi@$1 ./ssh_setting.sh


#scp /home/controller/.ssh/id_rsa.pub server@193.0.0.11:id_rsa.pub
#scp /home/controller/IoT/ssh_key_setting/ssh_setting.sh server@193.0.0.11:ssh_setting.sh
#ssh server@193.0.0.11 ./ssh_setting.sh

#scp /home/controller/.ssh/id_rsa.pub server@193.0.0.21:id_rsa.pub
#scp /home/controller/IoT/ssh_key_setting/ssh_setting.sh server@193.0.0.21:ssh_setting.sh
#ssh server@193.0.0.21 ./ssh_setting.sh

#scp /home/controller/.ssh/id_rsa.pub server@193.0.0.31:id_rsa.pub
#scp /home/controller/IoT/ssh_key_setting/ssh_setting.sh server@193.0.0.31:ssh_setting.sh
#ssh server@193.0.0.31 ./ssh_setting.sh

#scp /home/controller/.ssh/id_rsa.pub server@193.0.0.41:id_rsa.pub
#scp /home/controller/IoT/ssh_key_setting/ssh_setting.sh server@193.0.0.41:ssh_setting.sh
#ssh server@193.0.0.41 ./ssh_setting.sh


scp /home/server/.ssh/id_rsa.pub controller@193.0.0.200:id_rsa.pub
/home/controller/IoT/ssh_key_setting/ssh_setting.sh
