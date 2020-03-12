class Thing:
	def __init__(self, noun, name, desc, canGet):
		self.name, self.desc, self.canGet = name, desc, canGet

things = {
	"rope": Thing(
		"rope",
		"a length of [rope]",
		"Quite a bit of rope in a coil",
		True
	),
	"drain": Thing(
		"hole",
		"hole in the floor",
		"There's a hole in the floor. Looks like it was for draining water.",
		False
	),
	"glass": Thing(
		"glass",
		"a drinking [glass]",
		"For an ice cold beer.",
		False
	),
}