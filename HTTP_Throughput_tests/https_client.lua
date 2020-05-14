-- HTTP web based client - URI modifier
-- Author:: Pavan Kumar Paluri
-- Copyright @ University of Houston - RTLAB @ 2020

-- init a random value
-- maintain an array of file size requests
local file_size_req = {1000, 100000, 1000000}

-- init a random seed
math.randomseed(os.time()) -- gives a random val on each run

-- HTTP req function that will run at each new request spawned by wrk2
http_req_gen = function()
	-- choose a random req
	local rand_req = file_size_req[math.random(1, #file_size_req)]
	print(rand_req)
	
	-- Define a path that will append a new val to the specified URI
	url_path = "https://dc5503d4.ngrok.io/complex_hmap.php?random_request=" .. rand_req
	print(url_path)

	-- return the requested object with the current URL path
	return wrk.format("GET", url_path)
end

-- invoke the above function
http_req_gen()
