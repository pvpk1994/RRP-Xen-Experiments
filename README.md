# RRP-Xen: Experiment Results

This repository comprises of scheduling latency, file transfer latency, Throughput computation experiments 

## Redis-Cli Experiments

This directory comprises of results of Redis-Cli Benchmarking techniques
Domains tested: 1/7, 2/7, 3/7, 4/7 (The experimental setup assumes Redis-Cli software to be installed in the VM that is being evaluated)

Steps:

 0. Run a compute intensive Linux command ```yes``` in other VMs that are not being evaluated. 
    (For example: If 2 VMs with availability factors 3/7 and 4/7 are operating in RRP-controlled cpupool. 
    Let us suppose VM with availability factor 3/7 is being evaluated, run ```yes``` in 4/7 VM.)
    
 1. Run the command in vantage VM: ```nohup ./redis-cli --intrinsic-latency 100 2>&1 > output.txt &```

 2. Immediately after the command is run, try to obtain the PID of this process using (ps -ef)
 
 3. Next, use this PID in ```chrt -v -f -a -p 1 <PID>``` to change the SCHEDULING POLICY of this process to SCHED_FIFO
 
 4. Try to maintain a remote counter to keep track of 100s ~ 1min 40s time period.
 
 5. Results are stored in output.txt file. To collect the max latency -> avg run result * worst_run gives the max latency of this run
 
 6. Repeat this experiment 3 times for each domain and gather the averages of these 3 runs.
 
 Note: Repeat the process for following domain pairs ```<3/7, 4/7>, <1/14, 3/7, IDLE>, ... ```
  
 If unschedulable using RRP-AAF, omit that pair and proceed with the next pair.
 
 ## HTTPS-Nginx Latency-Throughput Experiments
 
 Software Requirements for Vantage VM: Nginx application web-server, PHP 7.0 Fast-CGI, ngrok.
 
 Software Requirements for Remote Client Machine: WRK2 tool, Python-3 (to run latency_throughput_extractor.py)
 
 Steps:
 
 0. Run a compute intensive Linux command ```yes``` in other VMs that are not being evaluated. 
    (For example: If 2 VMs with availability factors 3/7 and 4/7 are operating in RRP-controlled cpupool. 
    Let us suppose VM with availability factor 3/7 is being evaluated, run ```yes``` in 4/7 VM.)
 
 1. Run random file generator program to generate a total of 1GB files (899 1KB files, 1000 100KB files, 1000 1MB files) and place all these files in a ```tmpfs``` directory where PHP application resides.
 
 2. Replace ```/etc/nginx/nginx.conf``` with the nginx.conf provided in this repo. 
 
 3. Run ```sudo nginx -s reload``` and ```sudo nginx -t``` to confirm Nginx application web server is up and running. 
 
 4. Run ```sudo systemctl restart php7.0-fpm``` to activate PHP 7.0 fastCGI gateway.
 
 5. Set the priority of nginx worker and master processes from ```SCHED_OTHER``` to ```SCHED_FIFO```.
 
 6. Run ngrok and copy the https address.
 
 7. In the client machine, Now open ```http_client.lua``` and change ip address in line 82 from the above copied addr.
 
 8. In the client machine, run ```script_http_automate.sh```, the ngrok on Vantage VM should now start serving the file-size requests. This can be confirmed by ```200 OK``` status.
 
 9. If the status is ```500 Bad Gateway```, it implies something is wrong in the experimental setup.
 
 10. On the client machine, the results are gathered in ```results``` directory. 
