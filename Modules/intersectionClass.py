import carClass
import carLLClass

class intersection:
	# Documentation
	#
	# Has an array of carLL named lanes, where 0 corresponds to North, 1 to East, 2 to South and 3 to West
	# Has a boolean lightisNS that is True when the NS light is green. The light always starts green for NS
	# nextImportantTime() = returns the next important time in the intersection. Returns 0 there are no cars.
	# incrementDistance() = takes change and time and increments all cars in all lanes by that time.
	# determineLight() = takes scores of ns and ew lanes and determines which light should be shown


	def __init__(self):
		for i in range(4):
			lanes[0] = carLLClass.carLL()
		self.lightIsNS = True

	def nextImportantTime(self):
		counter = 0
		for i in range(4):
			if lanes[i].nextImportantTime():
				test[counter] = lanes[i].nextImportantTime()
				counter += 1

		if test == []:
			return 0
		else:
			return min(test)

	def incrementDistance(self,timeDiff):
		for i in range(4):
			if i % 2: # EW lanes
				lanes[i].incrementDistance(timeDiff,not self.lightIsNS)
			else: # NS lanes
				lanes[i].incrementDistance(timeDiff,self.lightIsNS)

	def determineLight(self):
		nsScore = 0
		ewScore = 0
		for i in range(4):
			if i % 2: # EW lanes
				ewScore += lanes[i].calculateScore()
			else: # NS lanes
				nsScore += lanes[i].calculateScore()

		if nsScore >= ewScore and lightIsNS: # light stays NS
			lightIsNS = True
			return False
		elif nsScore >= ewScore and not lightIsNS: # light changes from EW to NS
			lightIsNS = True
			return True
		elif nsScore < ewScore and lightIsNS: # light stays EW
			lightIsNS = False
			return False
		else: # light changes from NS to EW
			lightIsNS = False
			return True





