import random

class routeGenerator:
	def __init__(self):
		self.time = 0
	def generate(self,total,spread):
		file_full_name = raw_input("Give output file unique file name: ")
		f = open(file_full_name,'w')
		for i in range(1,total):
			self.time += random.randint(0,2) * spread
			self.stringToWrite = str(self.time) + ' ' + route().routeData + '\n'
			print(self.stringToWrite)
			f.write(str(self.stringToWrite))
		f.close()



class intersectionForTestSuite:
	def __init__(self,value):
		self.value = value
		self.up = self.value - 3 if (self.value >= 3) else None
		self.left = self.value - 1 if(self.value % 3 != 0) else None
		self.down = self.value + 3 if (self.value < 6) else None
		self.right = self.value + 1 if (self.value % 3 != 2) else None

class startingPoint:
	def __init__(self,next):
		self.next = next

class route:
	def __init__(self):
		i = random.randint(0,3)
		j = random.randint(0,2)
		k = random.randint(0,1)
		if (i == 0):
			case = 2 if k else 1
		elif (i == 1):
			case = 3 if k else 2
		elif (i == 2):
			case = 0 if k else 3
		else:
			case =1 if k else 0
		self.routeData = ['A','B','C','D'][i] + str(j)
		self.nextValue = startingPointArray[i][j].next.value
		while(self.nextValue != None):
			self.routeData = self.routeData + str(self.nextValue)
			l = random.randint(0,1)
			if case == 0:
				self.nextValue = intersectionArray[self.nextValue].up if l else intersectionArray[self.nextValue].right
			elif case == 1:
				self.nextValue = intersectionArray[self.nextValue].down if l else intersectionArray[self.nextValue].right
			elif case == 2:
				self.nextValue = intersectionArray[self.nextValue].down if l else intersectionArray[self.nextValue].left
			elif case == 3:
				self.nextValue = intersectionArray[self.nextValue].up if l else intersectionArray[self.nextValue].right								

intersectionArray = [None]*9
for i in range (0,9):
	intersectionArray[i] = intersectionForTestSuite(i)

startingPointArray = [[None,None,None],[None,None,None],[None,None,None],[None,None,None]]
for i in range (0,4):
	for j in range(0,3):
		startingPointArray[i][j] = startingPoint(intersectionArray[((i*(i+1)) if (i*(i+1))<12 else 0) + j * (3 if (i % 2) else 1)])

r = routeGenerator()
r.generate(100,0.3)
r.generate(100,0.5)
r.generate(100,1)