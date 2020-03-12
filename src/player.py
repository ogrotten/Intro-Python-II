# Write a class to hold player information, e.g. what room they are in
# currently.

class Mob:
	def __init__(self, kind, location):
		(self.kind, self.location) = (kind, location)

	def kill():
		return (f"{kind} is dead.")

class Human(Mob):
	def __init__(self, name, location, kind, inv):
		super().__init__(kind, location)
		self.name, self.inv  = name, inv

	def where(self, rooms):
		print (f"You are in the {self.location.name}\n{self.location.desc}")

		if len(self.location.items) == 2:
			stuff = (" ".join(self.location.items))
		else:
			stuff = (", ".join(self.location.items))
		
		if len(stuff) > 0:
			if len(stuff) > 1:
				addand = stuff.split()
				addand.insert(-1, "and")
				stuff = (" ".join(addand))
			print (f"\nHere you see {stuff}.")
		# if len(room[self.location.items]) > 0
		# 	print (f"You are in the {self.location.name}\n{self.location.desc}")
		
		return

	def action(self, cmd, player, rooms):
		currentloc = player.location
		newloc = None
		directions = player.location.exits.keys()

		args = cmd.split()
		if len(args) > 2:
			info = f"\n {len(args)} commands. Two words only."
			return info
		else:
			verb = args[0]
			try: 
				noun = args[1]
			except:
				pass

		if verb in directions:
			info = f"\nYou came from the {player.location.name} to the south."
			newloc = rooms[currentloc.exits[verb]]
			player.location = newloc

		elif verb in ("g", "get"):
			if noun in currentloc.items:
				info = currentloc.items
			info += (f"\nYou said '{verb} {noun}'. You have it.")
			

		elif verb in ("h", "help"):
			info = "\nCommands:\nn)orth, e)ast, w)est, s)outh, h)elp, q)uit."

		elif verb in ("q", "quit"):
			print("\nPeace.\n")
			exit()

		else:
			info = "\nSorry. Can't help you."

		# print("action", player.location.name)
		return info

# class Critter(Mob):