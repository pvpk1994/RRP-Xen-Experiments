#!/bin/bash
################################################################
# author: Guangli Dai @RTLab @UH
# Input: A port number you would like the server to listen to.
# This file runs the server part of the benchmark automatically.
# In this version, you have to use Ctrl+C to stop the script at the end of the test.
# Current version supports Linux and Mac environments only.
# NOTICE: Your gcc version may be changed by this script.
# Last modified: Oct 4th, 2019
################################################################
if [ $# -lt 1 ]
then
	echo "Please provide a port."
	exit
fi

#check the compiler's version
./gcc_install.sh

#compile
gccinfo=$(gcc -v 2>&1);

if [ `echo $gccinfo | grep -c "Apple"` -gt 0 ]
then
	echo "Mac version."
	ccflag=""
else
	ccflag="-lrt"
fi
gcc receiveTask.c -o recTask ${ccflag}


#run the server
./recTask $1