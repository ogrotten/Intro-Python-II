from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
    ),
}

# Link rooms together

room["outside"].nto = room["foyer"]
room["foyer"].sto = room["outside"]
room["foyer"].nto = room["overlook"]
room["foyer"].eto = room["narrow"]
room["overlook"].sto = room["foyer"]
room["narrow"].wto = room["foyer"]
room["narrow"].nto = room["treasure"]
room["treasure"].sto = room["narrow"]

def cli():
	cmd = input("\n> ")

	if cmd == "n":
		# move rooms
		# move("n")
		pass
	elif cmd == "q":
		print("\nPeace.\n")
		exit()

def where(player):
	print (f"You are in the {player.location.name}\n{player.location.desc}") 

def go(dir):
	print (dir)

count = 0
isPlaying = True

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
you = Player("The Player", room["outside"], "player", "nothing")


# Write a loop that: 
while isPlaying:
	os.system("cls")
	# * Prints the current room name
	# * Prints the current description (the textwrap module might be useful here).
	where(you)

	# * Waits for user input and decides what to do.
	cli()

	count += 1
	if count > 4:
		break

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
