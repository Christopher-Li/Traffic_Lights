import sys
sys.path.insert(0,"../Modules")

import carClass
import carLLClass
import intersectionClass
import fileToArray

# files
file_full_name = raw_input("Where are the car routes!?")
output_file_full_name = raw_input("Output file?")
output = open(output_file_full_name,'w')

vehicleRouteArray = fileToArray.fileToArray(file_full_name)
time = float(vehicleRouteArray[0][0])
timeDiff = 0
condition = True
intersect = intersectionClass.intersection()
while vehicleRouteArray != []:
	# add cars
	while vehicleRouteArray != [] and float(vehicleRouteArray[0][0]) == time:
		car = vehicleRouteArray[0]
		vehicleRouteArray = vehicleRouteArray[1:]
		intersect.addCar(float(car[1]), car[2][1:], ord(car[2][0]) - 65)
		vehicleRouteArray[1:]

	# determine if loop should end early
	if not vehicleRouteArray:
		break

	# determine light change
	print time
	print timeDiff, "timediff"
	if intersect.determineLight():
		stringToWrite = '%r 0\n' %(time)
		print time, "time"
		print stringToWrite, "stringtowrite"
		output.write(stringToWrite)
		# increment distance
		intersect.incrementDistance(timeDiff)
		timeDiff = 1.0
		time += timeDiff
	else:
		# print "INTERSECTION \n"
		# intersect.printLanes()
		# increment distance
		intersect.incrementDistance(timeDiff)

		# increment time
		# nextImportantTime = min(nextCarEntry, intersection.nextImportantTime())
		# nit is nextImportantTime
		nit1 = float(vehicleRouteArray[0][0]) - time
		nit2 = intersect.nextImportantTime()
		# print time , "time"
		# print timeDiff, "timeDiff"
		if nit2 == 0:
			timeDiff = nit1
		else:
			timeDiff = min(nit1, nit2)
		time += timeDiff

	# reevaluate condition
	condition = vehicleRouteArray or not intersect.isEmpty()