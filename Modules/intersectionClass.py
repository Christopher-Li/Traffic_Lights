import carClass
import carLLClass

LENGTH = 15.0


class intersection:
	# Documentation
	#
	# Has an array of carLL named lanes, where 0 corresponds to North, 1 to East, 2 to South and 3 to West
	# Has a boolean lightisNS that is True when the NS light is green. The light always starts green for NS
	# nextImportantTime() = returns the next important time in the intersection. Returns 0 there are no cars.
	# incrementDistance() = takes change and time and increments all cars in all lanes by that time.
	# determineLight() = takes scores of ns and ew lanes and determines which light should be shown
	#					 returns True if light has changed and False if light has not changed
	# addCar() = takes a speed, route and laneNumber and appends the car into the lane corresponding to the lane
	#			 number.
	# isEmpty() = returns a boolean.

	######### Testing #########
	# printLL() = prints every car in every lane


	def __init__(self):
		self.lanes = []
		for i in range(4):
			self.lanes.append(carLLClass.carLL(LENGTH))
		self.lightIsNS = True

	def nextImportantTime(self):
		counter = 0
		test = []
		for i in range(4):
			if self.lanes[i].nextImportantTime():
				test.append(self.lanes[i].nextImportantTime())
				counter += 1

		if test == []:
			return 0
		else:
			return min(test)

	def incrementDistance(self,timeDiff):
		for i in range(4):
			if i % 2: # EW lanes
				self.lanes[i].incrementDistance(timeDiff,not self.lightIsNS)
			else: # NS lanes
				self.lanes[i].incrementDistance(timeDiff,self.lightIsNS)

	def determineLight(self):
		nsScore = 0
		ewScore = 0
		for i in range(4):
			if i % 2: # EW lanes
				ewScore += self.lanes[i].calculateScore()
			else: # NS lanes
				nsScore += self.lanes[i].calculateScore()

		if nsScore >= ewScore and self.lightIsNS: # light stays NS
			self.lightIsNS = True
			return False
		elif nsScore >= ewScore and not self.lightIsNS: # light changes from EW to NS
			self.lightIsNS = True
			return True
		elif nsScore < ewScore and self.lightIsNS: # light stays EW
			self.lightIsNS = False
			return False
		else: # light changes from NS to EW
			self.lightIsNS = False
			return True

	def addCar(self, speed, route, laneNumber):
		self.lanes[laneNumber].append(speed, route)

	def printLanes(self):
		if self.lightIsNS:
			print "NS LIGHT IS ON"
		else:
			print "EW LIGHT IS ON"
		for i in range(4):
			print "lane# ", i
			self.lanes[i].printLL()
			print 



