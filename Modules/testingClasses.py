import carClass
import carLLClass
import intersectionClass

slow = carClass.car(4.0,"A0342",12.0)
med = carClass.car(6.0,"A3451",12.0)
fast = carClass.car(8.0,"A2342",12.0)
a = carLLClass.carLL()
a.printLL()
a.remove()
a.printLL()
a.append(slow)
a.printLL()
print a.calculateScore()
a.incrementDistance(0.3, True)
a.append(med)
a.incrementDistance(0.5,True)
a.append(fast)
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