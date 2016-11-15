#!/bin/bash
awk 'BEGIN{COUNT=0}; {COUNT+=10; printf"%d\t%f\n", COUNT, $1}' > result.txt
