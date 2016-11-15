#!/bin/bash

echo "parshing log file"
cat ./output/output_servers_192.0.0.111_192.0.0.121.txt|awk -F 'Bytes  ' {'print $2'} > ./temp.txt

echo "remove empty line"
sed -i '/^$/d' temp.txt

echo "parshing log file"
cat ./temp.txt|awk '{print $1}' >./temp2.txt


echo "get average Mbits/sec"
cat temp2.txt | awk 'BEGIN{TOTAL=0;COUNT=0}
{TOTAL+=$1;COUNT+=1.0}END{print"%f / %f => %.3f\n", TOTAL, COUNT, TOTAL/COUNT}' > result
