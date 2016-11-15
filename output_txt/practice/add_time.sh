#!/bin/bash

./add_time_module.sh < ./$1.txt
cat ./result.txt > ./result_$1.txt
