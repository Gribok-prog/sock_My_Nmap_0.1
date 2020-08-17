#!/usr/bin/env python 

import socket
from colorama import *
import os 

tras = input ('start/output: ')
if tras == 'start':
	os.system('clear')

	init(autoreset= True)
	print()
	print(Fore.GREEN + 'My port is open')
	print()
	print(Fore.RED + "It's not legal, but who the fuck is that")
	print(Fore.RED + "port scanner from 20 to 20000. If you want to register the: output")

	mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 135, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]
	sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

	host = input('[*] Enter host [*]:> ') 
		

	for port in mas:
		if sock.connect_ex((host, port)):
			print ('host:', host, 'port', port, 'is closed') 
		else:
			print ('host:', host, 'port', port, 'is open')
	input(Fore.RED + 'All, enter?\n')
	
elif tras == 'output':
	os.system('clear')
