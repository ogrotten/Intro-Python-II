class Location:
	def __init__(self, name, desc, exits, items):
		self.name = name
		self.desc = desc
		self.exits = exits
		self.items = items


rooms = {
	"outside": Location(
		"Outside Cave Entrance",
		"North of you, the cave mount beckons",
		{"n":"foyer"},
		["rope", "shoes"]
	),
	"foyer": Location(
		"Foyer",
		"Dim light filters in from the south. Dusty passages run north and east.",
		{"n":"overlook", "e":"narrow", "s":"outside", },
		["candle", "sock", "acorn"]
	),
	"overlook": Location(
		"Grand Overlook",
		"A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
		{"s":"foyer" },
		[]
	),
	"narrow": Location(
		"Narrow Passage",
		"The narrow passage bends here from west to north. The smell of gold permeates the air.",
		{"n":"alcove", "w":"foyer"},
		[]
	),
	"alcove": Location(
		"Treasure Chamber",
		"You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
		{"s":"narrow"},
		[]
	),
}

