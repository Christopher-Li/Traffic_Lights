import carClass
import carLLClass
import intersectionClass

intersections = intersectionClass.intersection()
slow = [4.0,"A0342"]
med = [6.0,"A3411"]
fast = [8.0,"A2342"]
a = carLLClass.carLL(12.0)
a.printLL()
a.remove()
a.printLL()
a.append(slow[0],slow[1])
a.printLL()
print a.calculateScore()
a.incrementDistance(0.3, True)
a.append(med[0],med[1])
a.incrementDistance(0.1,True)
a.append(fast[0],fast[1])
a.printLL()
print a.nextImportantTime() , "False"
a.incrementDistance(a.nextImportantTime(),False)
a.printLL()
print a.nextImportantTime() , "False"
a.incrementDistance(a.nextImportantTime(),False)
a.printLL()
print a.nextImportantTime() , "False"
a.incrementDistance(a.nextImportantTime(),False)
a.printLL()
print a.nextImportantTime()
a.incrementDistance(a.nextImportantTime(),True)
a.printLL()