import random as rand
import math

class Map21x21(object):

	def __init__(self, treasure=True, start='0, 0'):
		self.mapa = {}
		for y in range(-10, 11):
			for x in range(-10, 11):
				coord = str(x) + ', ' + str(y)
				if(coord == start):
					self.mapa[coord] = 'X'
				elif(treasure == True):
					if(rand.randrange(20) == 7):
						self.mapa[coord] = 'T'
					else:
						self.mapa[coord] = '-'
				else:
					self.mapa[coord] = '-'

	def printMap(self, format):
		if(format == 0):
			print(self.mapa)
		elif(format == 1):
			z = ''
			for w in range(-10, 11):
				for x in range(-10, 11):
					y = -w
					coord = str(x) + ', ' + str(y)
					z += self.mapa[coord] + '  '
					if(x == 10):
						z += '\n'
			print(z)
		else:
			print('That is not a format type!')

	def findValue(self, valueToFind, sskips=0):
		try:
			skips = int(sskips)
		except ValueError:
			print('That is not a valid skip value!')
			return None
		foundValueCoord = None
		for w in range(-10, 11):
			for x in range(-10, 11):
				y = -w
				coord = str(x) + ', ' + str(y)
				if(self.mapa[coord] == valueToFind):
					if(skips <= 0):
						foundValueCoord = coord
						break
					else:
						skips -= 1
						continue
				else:
					continue
			if(foundValueCoord != None):
				break
		return foundValueCoord

		def triangleDistance(self, coord1, coord2):
			try:
				x1 = int(coord1.split(', ')[0])
				x2 = int(coord2.split(', ')[0])
				y1 = int(coord1.split(', ')[1])
				y2 = int(coord2.split(', ')[1])
			except ValueError:
				print('Those are invalid coordinates!')
				return 0
			return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)