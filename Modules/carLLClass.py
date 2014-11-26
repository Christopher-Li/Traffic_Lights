import carClass

CARLENGTH = 0.5


class carLL:
	# Documentation
	#
	# Has a head pointer, tail pointer, and a length of the lane
	# append() = given a speed and route of a car, will add the car to the tail of the list
	# remove() = removes the first element in the linked list and returns it. If list is empty, returns None
	# calculateScore() = returns the score of the entire linked list
	# incrementDistance() = given the change in time and whether the light is green for the light, 
	#						it will shift the cars distance so the distance between each car is
	#						CARLENGTH, and only one car can go through the intersection.
	# nextImportantTime() = returns the time until the next car will cross the intersection or is 1 second
	#						away from the light. Returns 0 if the LinkedList is empty.
	# isEmpty() = returns a boolean. True if the Linked List is empty, 
	#			  and False is the Linked List contains values

	###### Testing ######
	# printLL() = prints every element in the LinkedList


	def __init__(self,length):
		self.head = None
		self.tail = None
		self.length = length

	def append(self, speed, route):
		carItem = carClass.car(speed,route,self.length)
		if self.head == None:
			self.head = self.tail = carItem
		else:
			self.tail.next = carItem
			self.tail = carItem

	def remove(self):
		if self.head == None: # Linked List is empty
			temp = None
		elif self.head == self.tail: # if there is one item in the Linked List
			temp = self.head
			self.head = self.tail = None
		else: # there are 2 or more items in the Linked List
			temp = self.head
			self.head = self.head.next

		return temp

	def calculateScore(self):
		score = 0
		if self.head == None:
			return score
		
		temp = self.head
		while temp != None:
			score += temp.carScore()
			temp = temp.next

		return score

	def incrementDistance(self,timeDiff,isLightGreen):
		if self.head == None:
			return None
		
		removedCar = None
		# increment first element in LinkedList
		temp = self.head
		if temp.distanceLeft(timeDiff) > 0: # if car will not reach the intersection
			temp.distance = temp.distanceLeft(timeDiff)
			maxDistance = temp.distance + CARLENGTH
		elif isLightGreen: # if car will reach the intersection and has light
			removedCar = self.remove()
			maxDistance = CARLENGTH
		else: # if car will reach the intersection and light is red
			temp.distance = 0
			maxDistance = CARLENGTH

		# increment every other car
		temp = temp.next
		while temp != None:
			if temp.distanceLeft(timeDiff) < maxDistance:
				temp.distance = maxDistance
				maxDistance += CARLENGTH
			else:
				temp.distance = temp.distanceLeft(timeDiff)
				maxDistance = temp.distance + CARLENGTH
			temp = temp.next

		return removedCar

	def nextImportantTime(self):
		if self.head == None:
			return 0
		timeCrossIntersection = self.head.distance/self.head.speed

		temp = self.head
		while temp != None and temp.distance/temp.speed <= 1:
			temp = temp.next

		if temp != None:
			return min(timeCrossIntersection, temp.distance/temp.speed - 1)
		else:
			return timeCrossIntersection

	def isEmpty(self):
		if self.head:
			return False
		else:
			return True

	def printLL(self):
		print "printing list"
		if self.head == None:
			print "empty"

		temp = self.head
		while temp != None:
			print "Speed: " , temp.speed , "\tRoute:" , temp.route, "\tDistance: " , temp.distance
			temp = temp.next



