#!/bin/bash

a=$(pwd)
echo $a
python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/post_processing/data_searching_and_sum_back_up.py $a
python /home/controller/IoT/cloud/Rest_API_Python/HttpClient/post_processing/data_searching_and_sum_back_up_link.py $a
