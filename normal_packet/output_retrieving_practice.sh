#1/bin/bash

ssh server@193.0.0.11 scp /home/server/output/*.txt controller@193.0.0.200:/home/controller/IoT/normal_packet/output/

a=$(date)
ifconfig >> ./$a.txt


