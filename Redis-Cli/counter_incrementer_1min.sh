#!/bin/bash

# Step-1: Initiate redis-server as a Background process (./redis-server &)
# Step-2: Server is now ready to accpet incoming connections.
# Step-3: Run this bash script to record the counter increment value for a   
#         tracing period of 1 minute. Results are gathered in output_counter
# Note: The counter functions like a "yeild" in python, we need to flush the  
#       counter value on every run and it can be accomplished as follows:
#       ./redis-cli flushall # flushes the counter value and reinitiates it 0

runtime="1 minute"
endtime=$(date -ud "$runtime" +%s)

while [[ $(date -u +%s) -le $endtime ]]
do
        ./redis-cli incr mycounter > output_counter.txt
done
