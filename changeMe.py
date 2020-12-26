#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# github/hanzdev

import random
from os import system
from colorama import Fore
import itertools
import threading
import time
import sys


def main():
	system("clear")
	system("cat src/banner.txt")
	print(Fore.CYAN + "changeMe - Mac and hostname changer.\n")

	input(Fore.WHITE + "Press enter to continue...")

	done = False

	def animate():
		for c in itertools.cycle(['|', '/', '-', '\\']):
			if done:
				break
			sys.stdout.write('\rProcessing... ' + c)
			sys.stdout.flush()
			time.sleep(0.1)


	t = threading.Thread(target=animate)
	t.start()

	time.sleep(3)
	done = True

def hostnames():

	global names
	names = []
	names.append("marry")
	names.append("school")
	names.append("arch")
	names.append("mint")
	names.append("windows")
	names.append("debian")
	names.append("ubuntu")
	names.append("home")
	names.append("firefox")
	names.append("mark")
	names.append("hello")
	names.append("ilovelinux")
	names.append("john")
	names.append("kali")
	names.append("parrot")
	names.append("backbox")
	names.append("alice")
	names.append("tiffany")


def changer():

	nam3 = random.choice(names)
	system("hostname " +  nam3)
	system("clear")
	system("cat src/banner.txt")

	try:
		system("ifconfig eth0 down && macchanger -r eth0 && ifconfig eth0 up && macchanger -s eth0")
	except:
		print(Fore.RED + "Pls check your device. (ifconfig)")

	try:
		system("ifconfig eth1 down && macchanger -r eth1 && ifconfig eth1 up && macchanger -s eth1")
	except:
		print(Fore.RED + "Pls check your device. (ifconfig)")

	try:
		system("ifconfig eth2 down && macchanger -r eth2 && ifconfig eth2 up && macchanger -s eth2")
	except:
		print(Fore.RED + "Pls check your device. (ifconfig)")

	try:
		system("ifconfig enp7s0 down && macchanger -r enp7s0 && ifconfig enp7s0 up && macchanger -s enp7s0")
	except:
		print(Fore.RED + "Pls check your device. (ifconfig)")


	print(Fore.MAGENTA + f"Your new hostname => {nam3}")



main()
hostnames()
changer()

