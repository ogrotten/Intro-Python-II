class Thing:
	def __init__(self, noun, name, desc, canGet):
		self.noun, self.name, self.desc, self.canGet = noun, name, desc, canGet

things = {
	"rope": Thing(
		"rope",
		"a length of [rope]",
		"Quite a bit of rope in a coil",
		True
	),
	"drain": Thing(
		"hole",
		"a hole in the floor",
		"There's a hole in the floor. Looks like it was for draining water.",
		False
	),
	"glass": Thing(
		"glass",
		"a drinking [glass]",
		"For an ice cold beer.",
		False
	),
	"candle": Thing(
		"candle",
		"a [candle]",
		"A light source in a former age. It's just a nub.",
		False
	),
	"sock": Thing(
		"sock",
		"a [sock]",
		"Someone wore this on their left foot for *a long time*.",
		False
	),
	"acorn": Thing(
		"acorn",
		"an [acorn]",
		"At some point, a tree may grow from it.",
		False
	),
	"shoes": Thing(
		"shoes",
		"a pair of [shoes]",
		"Kinda worn but serviceable.",
		False
	),
}