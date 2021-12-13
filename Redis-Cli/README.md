This directory comprises of results of Redis-Cli Benchmarking techniques
Domains tested: 1/7, 2/7, 3/7, 4/7

Procedure:
---------
-> nohup ./redis-cli --intrinsic-latency 100 2>&1 > output.txt &
-Already installed in 3/7 and 4/7 domains as redis_cli_bgd.sh in redis_cli/src directory
1. On the first run, make sure proper permissions are given to this shell script. (chmoad a+x *.sh)
2. Immediately after you run, try to obtain the PID of this process using (ps -ef)
3. Next, use this PID in (chrt -v -f -a -p 1 <PID>) to change the SCHEDULING POLICY of this process to SCHED_FIFO
4. Try to maintain a remote counter (your personal counter outside of experiment env) to keep track of 100s ~ 1min 40s time period.
5. Results are stored in output.txt file.. to collect the max latency -> avg run result * worst_run gives the max latency of this run
6. Repeat this experiment 3 times for each domain and gather the averages of these 3 runs.
Repeat the process for following domain pairs <3/7, 4/7>, <1/14, 3/7, IDLE>, ... 
If unschedulable using RRP-AAF, omit that pair and proceed with the next pair.
**
To run redis-cli process without having to know its PID to bind it to a CPU **
taskset -c CPU_ID nohup ./redis-cli --intrinsic-latency 20 2>&1 > output.txt &

However, a shortcoming with the above command is that we cannot make sure if the priority of this latched process is #1 or not. 
We need chrt for that which takes <PID> as its argument. 
