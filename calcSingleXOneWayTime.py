def fileToArray(vehicleRouteFileName):
	vehicleRouteData = open(vehicleRouteFileName,'r')
	vehicleRouteDataArray = []
	for line in vehicleRouteData:
		vehicleRouteDataArray.append(line.split())
	vehicleRouteData.close()
	return vehicleRouteDataArray

def calcSingleXOneWayTotalTime(vehicleRouteFileName,trafficLightFileName):
	vehicleRouteArray = fileToArray(vehicleRouteFileName)
	trafficLightArray = fileToArray(trafficLightFileName)
	totalTime = 0
	numStops = 0

	# iterate through each car in vehicleRouteArray and add up individual times
	for i in range(0,len(vehicleRouteArray)):
		j = 0
		isNS = True
		# iterate through each light change and check when vehicle[i] arrives at the intersection
		while (j<len(trafficLightArray)) and 3 + float(vehicleRouteArray[i][0]) > float(trafficLightArray[j][0])
			j += 1
			isNS = not(isNS)
		#on exiting while loop, j is the index of the light change after vehicle[i] arrives and isNS is the 
		#direction of the light when it gets there
		#in the case that there is no light change after vehicle arrives, j = len(trafficLightArray)
		if (j<len(trafficLightArray)):
			#if car gets stopped at traffic light
			if((vehicleRouteArray[i][1][0]=='B' or vehicleRouteArray[i][1][0]=='D') == (isNS)):
				#add the time the car had to wait: from time it gets to intersection to one second after light change
				totalTime += (float(trafficLightArray[j][0]) + 1) - (float(vehicleRouteArray[i][0]) + 3)
				numStops += 1
			#else if the car arrives at intersection within a second of the light turning green
			#true if time that the car reaches the intersection is less than one greater than the time of the (j-1)th light change
			elif (j > 0 and float(vehicleRouteArray[i][0]) + 3 - float(trafficLightArray[j-1][0]) < 1):
				# add the time between one second after light change and time car reaches intersection
				totalTime += (1 + float(trafficLightArray[j-1][0])) - (float(vehicleRouteArray[i][0]) + 3)
				numStop += 1
		totalTime += 7

	print(numStops)
	return totalTime

vehicleRouteFileName = raw_input("vehicleRouteFileName?")
trafficLightFileName = raw_input("trafficLightFileName?")
print calcSingleXOneWayTotalTime(vehicleRouteFileName, trafficLightFileName)