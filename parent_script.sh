#!/bin/bash



#step1 : execuse main.py. we can make output_including_ip.txt from input.txt
#	 then we can add control-arp flow rule, and purpose flow rule accroding to output_including_ip.txt


rm /home/byounguklee/mininet/con_python/output_txt/input.txt
rm /home/byounguklee/mininet/con_python/output_txt/input_mean.txt
rm /home/byounguklee/mininet/con_python/output_txt/input_mean_trun.txt

cp /home/byounguklee/mininet/con_python/input.txt /home/byounguklee/mininet/con_python/output_txt/input.txt
cp /home/byounguklee/mininet/con_python/input_mean.txt /home/byounguklee/mininet/con_python/output_txt/input_mean.txt
matlab -nojvm -l_nonlim.m nosplash < /home/byounguklee/mininet/con_python/real_nonlim.m
cp /home/byounguklee/mininet/con_python/input_mean_trun.txt /home/byounguklee/mininet/con_python/output_txt/input_mean_trun.txt

rm /home/byounguklee/mininet/con_python/input.txt
rm /home/byounguklee/mininet/con_python/input_mean.txt
rm /home/byounguklee/mininet/con_python/input_mean_trun.txt



cp /home/byounguklee/mininet/con_python/output_txt/input.txt /home/byounguklee/mininet/con_python/input.txt 
cp /home/byounguklee/mininet/con_python/output_txt/input_mean_trun.txt /home/byounguklee/mininet/con_python/input_mean.txt 


python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/main.py input.txt



#step2 : we make output_ip_mean from output_including_ip.txt and input_mean.txt  
#        output_including_ip.txt + input_mean.txt  --> output_ip_mean.txt
python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/pre_processing/ip_mean_processing.py
python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/pre_processing/ip_link_processing.py
python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/pre_processing/length_processing.py
python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/pre_processing/server_controlling_processing.py
python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/pre_processing/estimate_link.py
python /home/byounguklee/mininet/con_python/cloud/Rest_API_Python/HttpClient/pre_processing/estimate_DC.py





#step3 : we make those server iperf -s and iperf -c according to output_ip_mean
#	

/home/byounguklee/mininet/con_python/normal_packet/normal_at_controller.sh


#step4 : If you need, link capaciy can be controlled

