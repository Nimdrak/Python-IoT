#!/bin/bash

#in mininet case, just one thing is okay!

mkdir .ssh
chmod 700 .ssh
cat /home/byounguklee/id_rsa.pub >> .ssh/authorized_keys


##In this case, the file have to be moved to /home/[account's name]/
#cat /home/controller/id_rsa.pub >> .ssh/authorized_keys
