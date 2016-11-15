#!/bin/bash

#sudo /etc/init.d/ssh restart
#ssh server@193.0.0.11 sudo /etc/init.d/ssh restart
#ssh server@193.0.0.21 sudo /etc/init.d/ssh restart
#ssh server@193.0.0.31 sudo /etc/init.d/ssh restart
#ssh server@193.0.0.41 sudo /etc/init.d/ssh restart




#step1 : execuse main.py. we can make output_including_ip.txt from input.txt
#	 then we can add control-arp flow rule, and purpose flow rule accroding to output_including_ip.txt


rm /home/controller/IoT/output_txt/input.txt
rm /home/controller/IoT/output_txt/input_mean.txt
rm /home/controller/IoT/output_txt/input_mean_trun.txt

cp /home/controller/IoT/input.txt /home/controller/IoT/output_txt/input.txt
cp /home/controller/IoT/input_mean.txt /home/controller/IoT/output_txt/input_mean.txt
matlab -nojvm -l_nonlim.m nosplash < ./real_nonlim.m
cp /home/controller/IoT/input_mean_trun.txt /home/controller/IoT/output_txt/input_mean_trun.txt

rm /home/controller/IoT/input.txt
rm /home/controller/IoT/input_mean.txt
rm /home/controller/IoT/input_mean_trun.txt



cp /home/controller/IoT/output_txt/input.txt /home/controller/IoT/input.txt 
cp /home/controller/IoT/output_txt/input_mean_trun.txt /home/controller/IoT/input_mean.txt 


python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/main.py input.txt



#step2 : we make output_ip_mean from output_including_ip.txt and input_mean.txt  
#        output_including_ip.txt + input_mean.txt  --> output_ip_mean.txt
python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/ip_mean_processing.py
python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/ip_link_processing.py
python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/length_processing.py
python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/server_controlling_processing.py
python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/estimate_link.py
python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/estimate_DC.py

#python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/cal_trun.py

#python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/estimate_link_trun.py
#python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/pre_processing/estimate_DC_trun.py





#step3 : we make those server iperf -s and iperf -c according to output_ip_mean
#	

/home/controller/IoT/normal_packet/normal_at_controller.sh


#step4 : If you need, link capaciy can be controlled

#ssh pi@192.168.0.129 sudo ./link_capacity_control.sh eth2 10000
#ssh pi@192.168.0.129 sudo ./link_capacity_control.sh eth2 10000


#ssh pi@192.168.0.103 sudo ./link_capacity_control.sh eth2 10000
#ssh pi@192.168.0.103 sudo ./link_capacity_control.sh eth2 10000

#ssh pi@192.168.0.111 sudo ./link_capacity_control.sh eth2 10000
#ssh pi@192.168.0.111 sudo ./link_capacity_control.sh eth2 10000

#ssh pi@192.168.0.120 sudo ./link_capacity_control.sh eth2 10000
#ssh pi@192.168.0.120 sudo ./link_capacity_control.sh eth2 10000




