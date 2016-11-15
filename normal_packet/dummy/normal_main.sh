#!/bin/bash


################################################
############ Initialization input ##############

/home/controller/IoT/normal_packet/make_data/delete_ex_data.sh


#################################################

IFS=',' read -r -a input_length_path <<< $(cat /home/controller/IoT/output_txt/output_link_length.txt)

echo "length_path"
echo ${input_length_path[@]}
echo "number line"
echo ${#input_length_path[@]}
number_line=${#input_length_path[@]} 


################################################## 
################# ip_mean ################# 
p=0
while read line
do

p=$(expr $p + 1)
IFS=',' read -r -a array_$p <<< "$line"

done < /home/controller/IoT/output_txt/output_ip_mean.txt



echo "array ip_mean result"

for ((s=1; s<=number_line ;s++))
do
eval a='$'{array_$s[@]}
echo $a

done
	
################################################## 
################# ip_mean_193 ################# 
p=0
while read line
do

p=$(expr $p + 1)
IFS=',' read -r -a arrayee_$p <<< "$line"

done < /home/controller/IoT/output_txt/output_ip_mean_193.txt



echo "arrayee ip_mean_!93 result"

for ((s=1; s<=number_line ;s++))
do
eval a='$'{arrayee_$s[@]}
echo $a

done
	

################################################## 
################# ip_port ################# 
p=0
while read line
do

p=$(expr $p + 1)
IFS=',' read -r -a port_$p <<< "$line"

done < /home/controller/IoT/output_txt/output_port.txt



echo "array ip_mean result"

for ((s=1; s<=number_line ;s++))
do
eval a='$'{port_$s[@]}
echo $a

done
	



############################################ 
#################  ip_link ################# 
 
p=0
while read line
do

p=$(expr $p + 1)
IFS=',' read -r -a array_link_$p <<< "$line"

done < /home/controller/IoT/output_txt/output_ip_link.txt


echo "array ip_link result"

for ((s=1; s<=number_line ;s++))
do
eval a='$'{array_link_$s[@]}
echo $a

done

############################################ 
############################################ 

echo "iperf process kill"

for ((s=1; s<=number_line ;s++))
do

eval a='$'{arrayee_$s[0]}
eval b='$'{arrayee_$s[1]}
	
#echo "$a kill"
#ssh server@$a pkill -9 iperf
#echo "$b kill"
#ssh server@$b pkill -9 iperf


done

echo "193.0.0.11 kill"
ssh server@193.0.0.11 pkill -9 iperf
echo "193.0.0.21 kill"
ssh server@193.0.0.21 pkill -9 iperf
echo "193.0.0.31 kill"
ssh server@193.0.0.31 pkill -9 iperf
echo "193.0.0.41 kill"
ssh server@193.0.0.41 pkill -9 iperf

echo "wait 20 seconds"
sleep 5

############################################ 
############################################ 

#echo "iperf server on"

#for ((s=1; s<=number_line ;s++))
#do

#eval a='$'{array_$s[0]}
#eval b='$'{array_$s[1]}
#eval e='$'{port_$s[0]}
#eval f='$'{port_$s[1]}

# a is server(receiver side)
#echo "iperf server $s $a on"
#echo "pi@$a iperf -s -u -f m -p $e"
#ssh pi@$a iperf -s -u -U -f m -p $e -w 320k -e>> /home/controller/IoT/normal_packet/output/output_servers_${a}_${b}_${e}_${f}.txt 2>> /home/controller/IoT/normal_packet/output/output_servers_${a}_${b}_${e}_${f}.txt &

#done

#echo "wait 20 seconds"
#sleep 5


############################################ 
############################################


echo "iperf client on"


for ((s=1; s<=number_line ;s++))
do

eval a='$'{array_$s[0]}
eval b='$'{array_$s[1]}
eval c='$'{array_$s[2]}
eval d='$'{array_$s[3]}
eval e='$'{port_$s[0]}
eval f='$'{port_$s[1]}
eval g='$'{arrayee_$s[0]}
eval h='$'{arrayee_$s[1]}

#b is client(transmitter side)
echo "iperf client $s $b on"
#echo "ssh pi@$b iperf -c $a -p $e -u -t 100 -f m -b normal -x V " 

/home/controller/IoT/normal_packet/normal_sub_client.sh $a $b $c $d $e $f $g $h &

done


