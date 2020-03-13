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
		self.name, self.inv = name, inv


	def where(self, rooms, things):
		print (f"You are in the {self.location.name}\n{self.location.desc}")

		getnames = []
		
		for x in self.location.items:
			getnames.append(things[x].name)

		if len(getnames) > 0:
			if len(getnames) > 1:
				# addand = stuff.split()
				if len(getnames) == 2:
					getnames.insert(-1, "and")
					stuff = (" ".join(getnames))
				else:
					addand = [getnames.pop()]
					addand.insert(0, "and")
					stuff = f'{(", ".join(getnames))}, {(" ".join(addand))}'
			else:
				stuff = getnames[0]
			print (f"\nHere you see {stuff}.")

	def action(self, cmd, player, rooms, things):
		info = ""
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
			# print(noun)
			if noun in currentloc.items:
				currentloc.items.remove(noun)
				print(currentloc.items)
				# for x in currentloc.items:
				# 	if x == noun:
				# 		text += things[x].name
				self.inv = [self.inv] + [noun]
			info += (f"\nYou took {things[noun].name}.")
			

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