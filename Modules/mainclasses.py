class Car:
	
	def __init__(self, route, timeCrossSensor):
		self.route = route
		self.timeCrossSensor = timeCrossSensor
		self.next = None
	
	def getRoute(self):
		return self.route
	
	def getTimeCrossSensor(self):
		return self.timeCrossSensor
	
	def getNext(self):
		return self.next
	
	def setRoute(self,newRoute):
		self.route = newRoute
	
	def setTimeCrossSensor(self, newTimeCrossSensor):
		self.timeCrossSensor = newTimeCrossSensor
	
	def setNext(self,newNext):
		self.next = newNext

class CarLinkedList:
	
	def __init__(self):
		self.head = None
		self.tail = None
	
	def isEmpty(self):
		return self.head == None
	
	def append(self,carItem):
		if (self.isEmpty()):
			self.head = self.tail = carItem
		else:
			self.tail.next = carItem
			self.tail = carItem
	
	def size(self):
		current = self.head
		count = 0
		while (current != None):
			count = count + 1
			current = current.getNext()
		return count
	
	def removeHead(self):
		self.head = self.head.next
	
	def getElement(self,indexNumber):
		temp = self.head
		for i in range(0,indexNumber):
			temp = temp.next
		return temp
	
	def getScore(self):
		score = 0
		for i in range(0,self.size()):
			score += float(1)/(self.getElement(i).getTimeCrossSensor() + 1)
		return score

class Intersection:
	
	def __init__(self):
		self.nsCarLL = CarLinkedList()
		self.ewCarLL = CarLinkedList()
		self.lightIsNS = True
	
	def toggleLight(self):
		self.lightIsNS = not(self.lightIsNS)
	
	def push(self,carInstance,ns):
		if(ns):
			self.nsCarLL.append(carInstance)
		else:
			self.ewCarLL.append(carInstance)
	
	def scoreComp(self):
		return self.nsCarLL.getScore()>=self.ewCarLL

	def determineLightisNS(self):
		if self.nsCarLL.getScore() > self.ewCarLL.getScore():
			return True
		else:
			return False