# HTTP Client-Side Program - Final Version
# Author: Pavan Kumar Paluri @ UH-RTLAB
# Copyright @ RT-LAB, UNiversity of Houston, 2020
# Client-side HTTP Request Generator of Random File Size requests
import requests
from requests import get
import random
import time
from flask import render_template
from flask import Flask
from flask import request
app = Flask(__name__)


def download_txt(result_url, file_name):
    with open(file_name, "wb") as file:
        # Get request
        response = get(result_url)
        # now write to file
        file.write(response.content)


list_file_sizes = [1000, 100000, 1000000]
request_rate = int(input('Enter after how many seconds to respawn a new file size request:'))
counter = 0
while 1:
    # Pick a random request from the lot
    random_req = random.choice(list_file_sizes)
    print(f'random file-size request size: {random_req}')
    PARAMS = {'random_request': random_req}
    result = requests.get(url='http://localhost/http_server.php',
                          params=PARAMS)
    print(f"result: {result.url}")
    # If status code is 200 -> OK | elif 404! NOT OK | elif 301! Resource Moved Permanently
    print(f'return code for HTTP request is {result.status_code}')
    print(f'header Info: {result.headers}')
    print(f"Server's Response to HTTP request: {requests.Response}")
    file_nm = '/Users/pavankumarpaluri/Documents/http_thrp_logs/log_' + str(counter) + '.txt'
    download_txt(result.url, file_nm)
    counter += 1
    # Can exit the indefinite loop if we hit a counter val of 100 as we have sizable samples
    if counter == 100:
        print("Sizable Sample Limit Reached, Exiting!!")
        exit(0)
    print("Going to sleep at Start: %s", time.ctime())
    time.sleep(request_rate)
    print("About time to re-spawn new request: %s", time.ctime())

