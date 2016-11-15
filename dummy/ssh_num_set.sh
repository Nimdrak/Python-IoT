#!/bin/bash

#scp /home/controller/IoT/dummy/sshd_config pi@192.0.0.110:/etc/ssh
#sudo scp /home/controller/IoT/dummy/sshd_config pi@192.0.0.111:/etc/ssh
sudo scp /home/controller/IoT/dummy/sshd_config pi@192.0.0.111:
ssh pi@192.0.0.111 sudo cat /home/pi/sshd_config > /etc/ssh/sshd_config
