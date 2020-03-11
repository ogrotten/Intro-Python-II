from room import Room
from player import Human
import os
import time

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of player, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before player, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """player've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
    ),
}

# Link rooms together

room["outside"].n = room["foyer"]
room["foyer"].s = room["outside"]
room["foyer"].n = room["overlook"]
room["foyer"].e = room["narrow"]
room["overlook"].s = room["foyer"]
room["narrow"].w = room["foyer"]
room["narrow"].n = room["treasure"]
room["treasure"].s = room["narrow"]

global info
info = None

def pause(x):
	time.sleep(x)

def where(player):
	print (f"You are in the {player.location.name}\n{player.location.desc}") 

def cli(player):
	global info
	cmd = input("\n> ").lower()

	if cmd in ("n", "e", "w", "s"):
		go(cmd, player)

	elif cmd in ("h", "help"):
		info = "\nCommands: [n]orth, [e]ast, [w]est, [s]outh, [h]elp, [q]uit."

	elif cmd in ("q", "quit"):
		print("\nPeace.\n")
		exit()

	else:
		info = "\nSorry. Can't help you."


def go(dir, player):
	global info
	
	if dir == "n":
		try:
			info = f"\nYou came from the {player.location.name} to the south."
			player.location = player.location.n
		except: 
			info = "\nCan't go North from here."

	elif dir == "e":
		try:
			info = f"\nYou came from the {player.location.name} to the west."
			player.location = player.location.e
		except: 
			info = "\nCan't go East from here."

	elif dir == "w":
		try:
			info = f"\nYou came from the {player.location.name} to the east."
			player.location = player.location.w
		except: 
			info = "\nCan't go West from here."

	elif dir == "s":
		try:
			info = f"\nYou came from the {player.location.name} to the north."
			player.location = player.location.s
		except: 
			info = "\nCan't go South from here."
	


count = 0
isPlaying = True 

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Human("The Player", room["outside"], "player", "nothing")


# Write a loop that: 
while isPlaying:
	os.system("cls")
	# * Prints the current room name
	# * Prints the current description (the textwrap module might be useful here).

	where(player)

	if info != None:
		print(info)
		info = None

	# * Waits for user input and decides what to do.
	cli(player)

	count += 1
	if count > 14:
		break

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
