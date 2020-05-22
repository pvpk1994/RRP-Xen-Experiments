#!/bin/bash

#  ###########################################################################################################
#  Automate the process of Running client LUA application by requesting only througput as an input from end user.
#  Developer: Pavan Kumar Paluri
#  Copyright@ RT-LAB UH 2020
#  ###########################################################################################################

# #######################
# Input 1: Thrpt
# Input 2: Host URL
# Input 3: Domain' AF
# Input 4: Scheduler Name
# ######################


read -p "Enter the Throuput: " THRPT_REQ
read -p "Enter the Host URL: " HOST_URL
read -p "Enter the Domain's WCET: " AF
read -p "Enter the Domain's Period: " PERIOD
read -p "Enter the name of the scheduler: " XEN_SCHED
read -p "Enter the File Size Request: " FILE_REQ

DEST_DIR=$(pwd)/results/
ONE_KB=one_kb/
HUN_KB=hun_kb/
ONE_MB=one_mb/

# Execute Command based on the file size request
if [ $FILE_REQ -eq 1000 ]
then
	./wrk -t8 -c20 -d30s -R$THRPT_REQ -s http_client.lua --latency $HOST_URL > "$DEST_DIR$ONE_KB$XEN_SCHED"_"$AF"_"$PERIOD"_"$THRPT_REQ"_"$FILE_REQ"_wrk.txt
	# "$XEN_SCHED_$AF_$THRPT_REQ_wrk.txt"

elif [ $FILE_REQ -eq 100000 ]
then
	./wrk -t8 -c20 -d30s -R$THRPT_REQ -s http_client.lua --latency $HOST_URL > "$DEST_DIR$HUN_KB$XEN_SCHED"_"$AF"_"$PERIOD"_"$THRPT_REQ"_"$FILE_REQ"_wrk.txt

else
	./wrk -t1 -c20 -d30s -R$THRPT_REQ -s http_client.lua --latency $HOST_URL > "$DEST_DIR$ONE_MB$XEN_SCHED"_"$AF"_"$PERIOD"_"$THRPT_REQ"_"$FILE_REQ"_wrk.txt
fi

# Confirmation
if [ $? -eq 0 ]; then
	STATUS="SUCCESS"
else
	STATUS="FAILED"
fi 

echo "STATUS:: ($STATUS)"

