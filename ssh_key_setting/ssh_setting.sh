#!/bin/bash

mkdir .ssh
chmod 700 .ssh
cat /home/server/id_rsa.pub >> .ssh/authorized_keys


##In this case, the file have to be moved to /home/[account's name]/
#cat /home/controller/id_rsa.pub >> .ssh/authorized_keys
