import random

class Tile:
	def __init__ (self, has_ship=False, is_revealed=False):
		self.has_ship = has_ship
		self.is_revealed = is_revealed

	def enemy_vision (self):
		if not self.is_revealed:
			return '-'
		elif self.has_ship:
			return 'o'
		else:
			return 'x'

	def player_vision (self):
		if self.has_ship:
			return 'o'
		else:
			return '-'

class Board:
	def __init__ (self, width=10, height=10):
		self.tiles = [ [ Tile() for j in range(0, width)] for i in range(0, height)]
		self.width = width
		self.height = height

	def player_vision (self):
		for row in self.tiles:
			print ' '.join([tile.player_vision() for tile in row])

	def enemy_vision (self):
		for row in self.tiles:
			print ' '.join([tile.enemy_vision() for tile in row])

	def add_enemy_ship (self, ship_length):
		x = random.randint(0, self.width - 1)
		y = random.randint(0, self.height - 1)

		tile = self.tiles[x][y]

		if tile.has_ship:
			return self.add_enemy_ship(ship_length)

		direction = random.choice([ (0, 1), (1, 0), (0, -1), (-1, 0) ])

		for i in range(0, ship_length):
			diff_x, diff_y = direction

			x += diff_x
			y += diff_y

			new_tile = self.tiles[x][y]
			new_tile.has_ship = True


		self.tiles[x][y].has_ship = True

myBoard = Board()
myBoard.add_enemy_ship(2)
myBoard.add_enemy_ship(3)

enemyBoard = Board()

enemyBoard.enemy_vision()
print '*******************'
myBoard.player_vision()