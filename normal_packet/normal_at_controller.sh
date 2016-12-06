#!/bin/bash


################################################
############ Initialization input ##############
############# Initialization ssh ###############

/home/byounguklee/mininet/con_python/normal_packet/make_data/delete_ex_data.sh


#################################################

IFS=',' read -r -a input_length_path <<< $(cat /home/byounguklee/mininet/con_python/output_txt/output_link_length.txt)

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

done < /home/byounguklee/mininet/con_python/output_txt/output_ip_mean.txt



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

done < /home/byounguklee/mininet/con_python/output_txt/output_ip_mean_193.txt



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

done < /home/byounguklee/mininet/con_python/output_txt/output_port.txt



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

done < /home/byounguklee/mininet/con_python/output_txt/output_ip_link.txt


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
	
done

echo "10.0.0.1 kill"
ssh 10.0.0.1 pkill -9 iperf
echo "10.0.0.2 kill"
ssh 10.0.0.2 pkill -9 iperf
echo "10.0.0.3 kill"
ssh 10.0.0.3 pkill -9 iperf
echo "10.0.0.4 kill"
ssh 10.0.0.4 pkill -9 iperf

echo "wait 20 seconds"
sleep 5

############################################ 
############################################ 

echo "Previous output file deleted"

#for ((s=1; s<=number_line ;s++))
#do

#eval a='$'{array_$s[0]}
#eval b='$'{array_$s[1]}
#eval e='$'{port_$s[0]}
#eval f='$'{port_$s[1]}

# a is server(receiver side)
#echo "iperf server $s $a on"
#echo "pi@$a iperf -s -u -f m -p $e"
#ssh pi@$a iperf -s -u -U -f m -p $e -w 320k -e>> /home/byounguklee/mininet/con_python/normal_packet/output/output_servers_${a}_${b}_${e}_${f}.txt 2>> /home/byounguklee/mininet/con_python/normal_packet/output/output_servers_${a}_${b}_${e}_${f}.txt &

#done

#echo "wait 20 seconds"
#sleep 5

rm /home/byounguklee/mininet/con_python/normal_packet/output/*.txt
#ssh 10.0.0.1 rm /home/byounguklee/output_1/*.txt
#ssh 10.0.0.2 rm /home/byounguklee/output_2/*.txt
#ssh 10.0.0.3 rm /home/byounguklee/output_3/*.txt
#ssh 10.0.0.4 rm /home/byounguklee/output_4/*.txt


############################################ 
############################################


echo "iperf server on"


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
#echo "iperf client $s $b on"
#echo "ssh pi@$b iperf -c $a -p $e -u -t 100 -f m -b normal -x V " 
#echo "$a $b $c $d $e $f $g $h"

echo "server $a at port $e ON and 193 is $g"
ssh $a /home/byounguklee/mininet/con_python/normal_packet/normal_at_server.sh $e $a $f $b

sleep 2 
done

echo "wait 20 seconds"
sleep 20


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
#echo "iperf client $s $b on"
#echo "ssh pi@$b iperf -c $a -p $e -u -t 100 -f m -b normal -x V " 
#echo "$a $b $c $d $e $f $g $h"

echo "client $b at port $f ON and 193 is $h"
echo "client $b at port $f 's mean $c and variance $d"
echo "time_slot length is 10 and time_length 10"

sleep 0.5

ssh $b /home/byounguklee/mininet/con_python/normal_packet/normal_at_client.sh $a $e $h $c $d 10 120 $b $f & # a and e! neither b nor f
#sleep 5

done


