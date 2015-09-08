import os
import sys
import csv
import json
import requests
#import re
#from glob import glob
#from jinja2 import Template

DATA_DIR = 'data'

# Returns a list made of data from the specified csv name located in the data folder.
def CSVList(csv_name):
	csv_path = os.path.join(DATA_DIR, csv_name)
	csv_file = csv.DictReader(open(csv_path, encoding= 'utf-8'))
	csv_list = list(csv_file)
	return csv_list

# Returns a list made of data from the specified json name located in the data folder.
def JSONList(json_name):
	json_path = os.path.join(DATA_DIR, json_name)
	json_file = json.loads(open(json_path).read())
	json_data = list(json_file)
	return json_data

# Given a URL and a name of an unexisting file, saves the html text to the file in the data folder.
def SaveHTML(url, file_to_name):
	if os.path.exists(os.path.join(DATA_DIR, file_to_name)):
		file_to_name += "_v2"
	response = requests.get(str(url))
	html = response.text
	file = open(DATA_DIR + "/" + file_to_name + ".html", 'w')
	file.write(html)
	file.close()