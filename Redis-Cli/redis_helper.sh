#!/bin/bash
# This script serves as a helper script to run redis-cli as a real-time process with #1 priority
# and to bind this process to either VCPU #0 or VCPU #1 of a given VM in a 2-VCPU per VM. 
# In this example script, the redis process is hard-pinned to CPU #1 i.e., VCPU#1 
chrt -v -f -a -p 1 $1
taskset -pc 1 $1 
