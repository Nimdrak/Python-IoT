#!/bin/bash

a=$(pwd)
echo $a
python /home/cloud1/IoT/cloud/Rest_API_Python/HttpClient/data_searching_and_sum_back_up.py $a
python /home/cloud1/IoT/cloud/Rest_API_Python/HttpClient/data_searching_and_loss_sum_back_up.py $a
