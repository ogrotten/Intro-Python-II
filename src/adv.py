# python libs
import os
import time

# my libs
from room import *
from item import *
from player import Human

global info
info = None
global isPlaying
isPlaying = True 
count = 0

def cli(player):
	global info
	global isPlaying
	cmd = input("\n> ").lower()

	info = player.action(cmd, player, rooms, things)

player = Human("The Player", rooms["outside"], "player")

while isPlaying:
	os.system("cls")

	player.where(rooms, things)

	if info != None:
		print(info)
		info = None

	cli(player)

	count += 1
	if count > 14:
		break

