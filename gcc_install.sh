#!/bin/bash
################################################################
# author: Guangli Dai @RTLab @UH
# This file checks the gcc version and install the required gcc for the benchmark to work
# Currently support Linux and Mac enviorments only.
# NOTICE: Your gcc version may be changed by this script.
# Last modified: Oct 4th, 2019
################################################################
gccinfo=$(gcc -v 2>&1); #the output of gcc here is in the error (2)
#echo ${gccinfo};

isApple=`echo ${gccinfo} | grep -c "Apple"`;
if [ ${isApple} -gt 0 ]
then
	echo "MAC OS detected.";
	flag=`echo ${gccinfo} | grep -c "clang version 11"`;
	if [ ${flag} -gt 0 ]
	then
		echo "gcc version fits.";
	else
		echo "clang 11 is not supported, will start installation now.";
		#brew install gcc;
	fi
else
	echo "Linux detected.";
	flag=`echo ${gccinfo} | grep -c "gcc version 6"`;
	if [ ${flag} -gt 0 ]
	then
		echo "gcc version fits.";
	else
		echo "gcc version 6 is not supported, will start installation now.";
		sudo apt-get update && \
		sudo apt-get install build-essential software-properties-common -y && \
		sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y && \
		sudo apt-get update && \
		sudo apt-get install gcc-6 g++-6 -y && \
		sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-6 && \
		gcc -v
	fi
fi


