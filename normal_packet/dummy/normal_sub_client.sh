#!/bin/bash

#echo $1 # server
#echo $2 # client
#echo $3 
#echo $4
#echo $5
#echo $6
#echo $7 # server_193
#echo $8 # client_193

#################################################

#IFS=',' read -r -a input_length_path <<< $(cat /home/controller/IoT/output_txt/output_link_length.txt)

#echo "length_path"
#echo ${input_length_path[@]}
#echo "number line"
#echo ${#input_length_path[@]}
#number_line=${#input_length_path[@]} 

################################################

################################## a * p is total slot but change a ###############################
for a in {1..2};do


#####################################
echo "iperf server on"
#for ((s=1; s<=number_line ;s++))
#do

# a is server(receiver side)
echo "iperf server $s $1 $7 on"
echo "server@$7 iperf -s -u -f m -p $5"
ssh server@$7 iperf -s -u -U -f m -p $5 -e -x V>> /home/controller/IoT/normal_packet/output/output_servers_$1_$2_$5_$6.txt 2>> /home/controller/IoT/normal_packet/output/output_servers_$a_$b_$e_$f.txt &

#done

echo "wait 5 seconds"
sleep 5

######################################


for p in {1..2};do

	var=$(python /home/controller/IoT/normal_packet/normal_number.py $3 $4)
	var_sleep=$(python /home/controller/IoT/normal_packet/random_sleep.py)

	echo $var >>/home/controller/IoT/normal_packet/output/output_clients_$1_$2_$5_$6.txt
	echo $var_sleep
	echo "ssh server@$2 $8 iperf -c $1 $7 -p $5 -u -t 15 -f m -b $var -x V STAGE $a START" 

#	sleep $var_sleep
#########################time slot is 12 ###############################################################
	ssh server@$8 iperf -c $1 -p $5 -t 10 -f m -b $var -T 1000 -x V >> /home/controller/IoT/normal_packet/output/output_clients_$1_$2_$5_$6.txt 2>> /home/controller/IoT/normal_packet/output/output_clients_$1_$2_$5_$6.txt


#	a=$(ssh pi@$2 ps -ef | grep "$5"|grep "iperf"|awk '{print $2}')
#	echo $a
#	ssh pi@$2 kill -9 $a &

	#WORK_PID=`jobs -l | awk '{print $2}'`
	#ssh pi@$1 wait $WORK_PID
	#echo $p finished

	echo "ssh server@$2 $8 iperf -c $1 -p $5 -u -t 15 -f m -b $var -x V STAGE $a FINISHED"
	sleep 5

done

##############################################################################
#a=$(ssh server@$1 $7 ps -ef |grep "$5"|grep "iperf"|grep "601k"|awk '{print $2}')
a=$(ssh server@$7 ps -ef |grep "$5"|grep "iperf"|awk '{print $2}')
echo "$a kill server@$7 iperf -s -u -f m -p $5"
ssh server@$7 kill -9 $a

##########################################################################

done



echo "SERVICE $1 $2 $5 $6 FINISHED"
