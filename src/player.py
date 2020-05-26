class Mob:
	def __init__(self, kind, location):
		(self.kind, self.location) = (kind, location)

	def kill():
		return f"{kind} is dead."


class Human(Mob):
	def __init__(self, name, location, kind):
		super().__init__(kind, location)
		self.name = name
		self.inv = []

	def where(self, rooms, things):
		print(f"You are in the {self.location.name}\n{self.location.desc}")

		getnames = []

		for x in self.location.items:
			getnames.append(things[x].name)

		if len(getnames) > 0:
			stuff = self.sentence(getnames)
			print(f"\nHere you see {stuff}.")
		else:
			pass

	def action(self, cmd, player, rooms, things):
		info = ""
		currentloc = player.location
		newloc = None
		directions = player.location.exits.keys()

		args = cmd.split()
		if len(args) > 2:
			info = f"\n {len(args)} commands. Two words only."
			return info
		elif len(args) == 0:
			return

		else:
			verb = args[0]
			try:
				noun = args[1]
			except:
				pass

		if verb in directions:
			info = f"\nYou came from the {player.location.name}."
			newloc = rooms[currentloc.exits[verb]]
			player.location = newloc

		elif verb in ("g", "get"):
			if noun in currentloc.items:
				currentloc.items.remove(noun)
				self.inv.append(noun)
				info += f"\nYou took {things[noun].name}."
			else:
				info = "\nwat"
		
		elif verb in ("d", "drop"):
			if noun in self.inv:
				self.inv.remove(noun)
				currentloc.items.append(noun)
				info += f"\nYou dropped {things[noun].name}."
			else:
				info = "\nhuh?"

		elif verb in ("h", "help"):
			info = "\nCommands:\nn)orth, e)ast, w)est, s)outh"
			info += "\ng)et [item], h)elp, i)nventory, q)uit."

		elif verb in ("i", "inv"):
			carried = []
			for x in player.inv:
				if x == "":
					continue
				carried.append(things[x].name)
			info = f"\nYou carry {self.sentence(carried)}"

		elif verb in ("q", "quit"):
			print("\nPeace.\n")
			exit()

		else:
			info = "\nSorry. Can't help you."

		return info

	def sentence(self, incoming):
		if len(incoming) > 0:
			if len(incoming) > 1:
				if len(incoming) == 2:
					incoming.insert(-1, "and")
					stuff = " ".join(incoming)
				else:
					addand = [incoming.pop()]
					addand.insert(0, "and")
					stuff = f'{(", ".join(incoming))}, {(" ".join(addand))}'
			else:
				stuff = incoming[0]
			return stuff
		


# class Critter(Mob):

