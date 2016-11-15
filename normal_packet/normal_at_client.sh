#!/bin/bash

######echo $1 # source's IP
######echo $2 # source's port
######echo $3 # source's 193
############################
############################

#echo $1 # destination's IP $a
#echo $2 # destination's port
#echo $3 # destination's 193 

#echo $4 # mean
#echo $5 # variance
#echo $6 # time_slot_length
#echo $7 # time_length
#echo $8 # source's IP $b
#echo $9 # source's port

time_length=$7
for ((a=1; a<=time_length ; a++))
do

#	var=$(python /home/controller/IoT/normal_packet/normal_number.py $4 $5)
#	echo "$var"
	var=$(python /home/server/normal_number.py $4 $5)
	iperf -c $1 -p $2 -u -t $6 -f M -b $var -T 1000 -x V>> /home/server/output/output_clients_$1_$8_$2_$9.txt 2>> /home/server/output/output_clients_$1_$8_$2_$9.txt
#	iperf3 -c $1 -p $2 -u -t $6 -f m -b $var -T 1000 -V -J -d >> /home/server/output/output_clients_$1_$8_$2_$9.txt 2>> /home/server/output/output_clients_$1_$8_$2_$9.txt

	sleep 5

done

WORK_PID=`ps -ef|grep 'iperf -c $1 -p $2 -u -t $6 -f m -b $var -T 1000'| grep -v grep | awk '{print $2}'`
ps -ef|grep 'iperf -c $1 -p $2 -u -t $6 -f m -b $var -T 1000'| grep -v grep 

sync
wait $WORK_PID >> /home/server/output/output_clients_$1_$8_$2_$9.txt
date '+%F %R' >> /home/server/output/output_clients_$1_$8_$2_$9.txt
echo "client process $1_$8_$2_$9 is finished" >> /home/server/output/output_clients_$1_$8_$2_$9.txt
echo "client process $1_$8_$2_$9 is finished"

sleep 15
#date > /home/server/output/$8.txt
#ifconfig >> /home/server/output/$8.txt
scp /home/server/output/*.txt controller@193.0.0.200:/home/controller/IoT/normal_packet/output/
#sleep 15
#rsync -arlvz -e ssh /home/server/output/*.txt controller@193.0.0.200:/home/controller/IoT/normal_packet/output/


