# HTTP Client-Side Program - Pre-Final Version
# Author: Pavan Kumar Paluri @ UH-RTLAB
# Copyright @ RT-LAB, UNiversity of Houston, 2020
# Client-side HTTP Request Generator of Random File Size requests
import requests
from requests import get
import random
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


# Maintain a list of file sizes -> {1KB, 100KB, 1MB}
list_file_sizes = [1000, 100000, 1000000]
print(list_file_sizes)
# pick a random request
random_req = random.choice(list_file_sizes)
print(f'random file-size request size: {random_req}')
PARAMS = {'random_request': random_req}
result = requests.get(url='http://localhost/complex_hmap.php', params=PARAMS)
print(f"result: {result.url}")
# If status code is 200 -> OK | elif 404! NOT OK | elif 301! Resource Moved Permanently
print(f'return code for HTTP request is {result.status_code}')
print(f'header Info: {result.headers}')
print(f"Server's Response to HTTP request: {requests.Response}")
file_nm = '/Users/pavankumarpaluri/Documents/competetivePython/new.txt'
download_txt(result.url, file_nm)

