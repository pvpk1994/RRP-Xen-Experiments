
################################################################
# author: Guangli Dai @ RTLab @UH
# This file helps analyze the data collected from the client
# The result from each domain is put into corresponding csv file in conclusion folder
# usage: python3 analyze.py
################################################################

import os, sys
import csv

#read file and collect info and write to the result file
def collect(filename, writer):
	title_info = filename.split('/')#get the last part's name out first
	title_info = title_info[3]
	title_info = title_info.split('_')
	print(title_info)
	density = title_info[1]
	print("Parsing result from density "+density)
	with open(filename, 'r') as f:
		csv_reader = csv.reader(f, delimiter=',')
		tardiness = 0
		missed_num = 0
		total_num = 0
		for row in csv_reader:
			ddl = float(row[0])
			exe_end = float(row[1])
			total_num+= 1
			if exe_end>ddl:
				missed_num += 1
				tardiness += exe_end - ddl
		if total_num==0:
			print("ERROR: File "+filename+" empty!")
			return
		completion_ratio = 1- missed_num/total_num
		avg_tar = tardiness/total_num
		writer.writerow({'density':density, 'completion ratio':completion_ratio, 'average tardiness':avg_tar})


			



#read file analyze average latency and completion ratio
path= "./"
dirs = os.listdir(path)

for dir_now in dirs:
	if os.path.isdir(dir_now):
		print("Going into directory "+dir_now)
		if dir_now.find("result")==-1:
			continue
		files = os.listdir(path+"/"+dir_now)
		#open result file to write in
		resultf_name = ""
		with open(path+"/"+dir_now+"/README") as readme:
			id_now = readme.readline().split()[0]
			print(id_now)
			if not os.path.exists(path+"/conclusion"):
				os.mkdir(path+"/conclusion")
			resultf_name = "./conclusion/"+id_now + "_result.csv"
		resultf= open(resultf_name, "w")
		writer = csv.DictWriter(resultf, fieldnames=['density','completion ratio','average tardiness'])
		for file in files:
			if file=="README":
				continue
			collect(path+"/"+dir_now+"/"+file, writer)

#draw pic after reading all files