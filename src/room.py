# Implement a class to hold room information. This should have name and
# description attributes.

class Location:
	def __init__(self, name, desc, exits):
		self.name = name
		self.desc = desc
		self.exits = exits


room = {
    "outside": Location("Outside Cave Entrance", "North of player, the cave mount beckons"),
    "foyer": Location(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
    ),
    "overlook": Location(
        "Grand Overlook",
        """A steep cliff appears before player, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
    ),
    "narrow": Location(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    ),
    "treasure": Location(
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
