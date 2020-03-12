# python libs
import os
import time

# my libs
from room import *
from player import Human

global info
info = None
global isPlaying
isPlaying = True 
count = 0

def pause(x):
	time.sleep(x)
def where(player):
	# print(player.location)
	print (f"You are in the {player.location.name}\n{player.location.desc}") 
def cli(player):
	global info
	global isPlaying
	cmd = input("\n> ").lower()

	info = player.action(cmd, player, rooms)


player = Human("The Player", rooms["outside"], "player", "nothing")

# Write a loop that: 
while isPlaying:
	os.system("cls")

	where(player)

	if info != None:
		print(info)
		info = None

	cli(player)

	count += 1
	if count > 14:
		break

