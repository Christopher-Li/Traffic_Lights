class car:
	# Documentation
	#
	# Has a speed, route, distance, and next pointer
	# ********** speed, and distance must be floats *************
	# distanceLeft() = returns the distance of the car given the change in time
	# carScore = returns the score of the car

	def __init__(self,speed,route,distance):
		self.speed = speed
		self.route = route
		self.distance = distance
		self.next = None

	def distanceLeft(self,timeDiff):
		return self.distance - self.speed * timeDiff

	def carScore(self):
		time = self.distance/self.speed
		score = 1/ (time + 1)
		return score