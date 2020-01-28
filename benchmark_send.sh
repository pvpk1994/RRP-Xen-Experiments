#!/bin/bash
################################################################
# author: Guangli Dai @RTLab @UH
# Input: smallest density; largest density; step of each density change; 
#        the port the server listens to; ip address of the domain where server is set.
# Please run this script AFTER the benchmark_server.sh has been launched.
# This file runs the client part (data collection) of the benchmark automatically.
# The program halts automatically when the data collection is done.
# Current version supports Linux and Mac environments only.
# NOTICE: Your gcc version may be changed by this script.
# Last modified: Oct 5th, 2019 need to be tested. Put two folders.
################################################################

echo "Usage of the script: input the start and end of the range of the density, the step length, the port and the ip address of the server."
if [ $# -lt 5 ]
then
	echo "Not enough arguments passed in."
	exit 0
fi

start=$1
end=$2
step=$3
port=$4
host=$5

#check the environment first
./gcc_install.sh
#takes in and analyze parameters

#compile
gccinfo=$(gcc -v 2>&1);

if [ `echo $gccinfo | grep -c "Apple"` -gt 0 ]
then
	echo "Mac version."
	ccflag=""
else
	ccflag="-lrt"
fi
gcc sendTask.c -o sendTask ${ccflag}

#execute recursively
now=$start
wcet=30
dir=./result_${host}_${start}_${end}_${step}
if [ ! -d ${dir} ]
then
	mkdir $dir
fi
echo ${host} > ${dir}/README
while [ $(bc <<< "$now > ${end}") -lt 1 ]
do
	fileName=${dir}/${host}_${now}_${wcet}.log
	rm ${fileName} 2>/dev/null 
	touch ${fileName}
	for i in {1..100}
	do
		./sendTask ${now} ${wcet} ${port} ${host} ${fileName}
		sleep 0.03s
	done
	now=$(echo ${now}+${step} | bc)
	echo Current round ends. Result saved to ${fileName}
	
done