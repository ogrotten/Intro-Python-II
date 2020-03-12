# Write a class to hold player information, e.g. what room they are in
# currently.

class Mob:
	def __init__(self, kind, location):
		(self.kind, self.location) = (kind, location)

	def kill():
		return (f"{kind} is dead.")

class Human(Mob):
	def __init__(self, name="Miles", location = rooms["outside"], kind, inv):
		super().__init__(kind, location)
		self.name, self.inv  = name, inv

	def where(self, room):
		# print (self.location.desc)
		return

	def action(self, cmd, player, rooms=None):
		currentloc = player.location
		newloc = None
		directions = player.location.exits.keys()

		if cmd in directions:
			info = f"\nYou came from the {player.location.name} to the south."
			newloc = rooms[currentloc.exits[cmd]]
			player.location = newloc

		elif cmd in ("h", "help"):
			info = "\nCommands:\nn)orth, e)ast, w)est, s)outh, h)elp, q)uit."

		elif cmd in ("q", "quit"):
			print("\nPeace.\n")
			exit()

		else:
			info = "\nSorry. Can't help you."

		return info

# class Critter(Mob):