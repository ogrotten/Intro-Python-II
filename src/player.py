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
	def where(self, room):
		# print (self.location.desc)
		return
	# def move(dir):
		# get direction
		# move only if that direction is available.
