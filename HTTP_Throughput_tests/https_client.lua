-- HTTP web based client - URI modifier
-- Author:: Pavan Kumar Paluri
-- Copyright @ University of Houston - RTLAB @ 2020

-- init a random value
-- maintain an array of file size requests
local file_size_req = {1000, 100000, 1000000}

-- init a random seed
math.randomseed(os.time()) -- gives a random val on each run  



-- HTTP response generator function 

http_response_gen = function(url)
	local http_request = require "http.request"
	--local rand_req = file_size_req[math.random(1, #file_size_req)]
	--print("random request is: " .. rand_req)
	-- Get the complete URL path
	local url_path = url .. "/http_server.php?random_request=" .. 1000
	-- print("Final URL path is: " .. url_path)
	local headers, stream = assert(http_request.new_from_uri(url .. "/http_server.php?random_request=" .. 1000):go())
	local body = assert(stream: get_body_as_string())
	if headers:get ":status" ~= "200" then
		error(body)
	end
	print(body)
end



-- HTTPS request & Response Generators

https_gen = function(url)
	require("socket")
	local https = require("ssl.https")
	local url_path = url .. "/http_server.php?random_request=" .. 1000
	local body, code, headers, status = https.request(url_path)
	--print(status)
	--print(body)
end



-- HTTP req function that will run at each new request spawned by wrk2

http_req_gen = function(inp_str)
	-- choose a random req
	-- local rand_req = file_size_req[math.random(1, #file_size_req)]
	-- print(rand_req)
	
	-- Define a path that will append a new val to the specified URI
	url_path = inp_str .. "/complex_hmap.php?random_request=" .. 1000
	-- print(url_path)

	-- return the requested object with the current URL path
	return wrk.format("GET", url_path)
end




-- HTTP response Handler

response = function(status, headers, body)
	if status == 200 then
		print("Response has: " .. body)
	end
end

-- main function 
-- invoke the above function
--print("Enter the of Server: ")
--input_str = io.read("*l") -- read a string in
-- Place the newly obtained URL of server in the " "
-- Format of string (Example: http://localhost)

input_str = "https://b9d74531.ngrok.io"

-- File Size Request inputted from end user
--print("Enter the File Size: {Options:: 1000; 100000; 1000000}")
--file_req = io.read("*n")  -- read a file_size number in 
 -- ENABLE ONLY HTTPS REQUEST EXCHANGE 
https_gen(input_str)
--http_req_gen(input_str, file_req)
--http_response_gen(input_str)
