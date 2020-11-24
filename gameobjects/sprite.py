# Pandemic Delivery Game
# This code is released under MIT by Fabio Ishikawa

class Sprite(object):
	def __init__(self, name):
		self.name = name

	def print_name(self):
		print("name: " + self.name)