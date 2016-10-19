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

	def add_ship (self, ship_length):
		x = random.randint(0, self.width - 1)
		y = random.randint(0, self.height - 1)

		tile = self.tiles[x][y]

		if tile.has_ship:
			return self.add_ship(ship_length)

		direction = random.choice([ (0, 1), (1, 0), (0, -1), (-1, 0) ])

		for i in range(0, ship_length):
			diff_x, diff_y = direction

			new_tile = self.tiles[x][y]

			x += diff_x
			y += diff_y

			if y <= 0 or y >= self.height or x <= 0 or x >= self.width:
				return self.add_ship(ship_length)

		new_tile.has_ship = True

		self.tiles[x][y].has_ship = True

	def check_tile (self, x, y):
		tile = self.tiles[x][y]
		tile.is_revealed = True
		if tile.has_ship:
			print 'Booom! You hit it!'
		else:
			print 'NEIN'

myBoard = Board()
myBoard.add_ship(2)
myBoard.add_ship(3)
myBoard.add_ship(4)

enemyBoard = Board()
enemyBoard.add_ship(4)
enemyBoard.add_ship(4)
enemyBoard.add_ship(4)
enemyBoard.add_ship(4)
enemyBoard.add_ship(4)
enemyBoard.add_ship(4)

enemyBoard.enemy_vision()
print '*******************'
myBoard.player_vision()


while True:
	x = int(raw_input('Dime x:\n'))
	y = int(raw_input('Dime y:\n'))
	enemyBoard.check_tile(x, y)
	enemyBoard.enemy_vision()
	print '*******************'
	myBoard.player_vision()



