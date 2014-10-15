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
	for i in range(0,len(vehicleRouteArray)):
		j = 0
		isNS = True
		print('i' + str(i))
		print('j' + str(j))
		while (j<len(trafficLightArray) and 3 + float(vehicleRouteArray[i][0]) > float(trafficLightArray[j][0])):
			j += 1
			isNS = not(isNS)
			print('j' + str(j))
		if (j<len(trafficLightArray)):
			if ((vehicleRouteArray[i][1][0]=='B' or vehicleRouteArray[i][1][0]=='D') != (not isNS)):
				totalTime += float(trafficLightArray[j][0]) - float(vehicleRouteArray[i][0]) - 2
				numStops += 1
			elif (abs(float(vehicleRouteArray[i][0]) + 2.5 - float(trafficLightArray[j][0])) < 0.5):
				totalTime += 1 + float(trafficLightArray[j][0]) - float(vehicleRouteArray[i][0]) - 3
				numStops += 1
		totalTime += 7


	print(numStops)
	return totalTime

vehicleRouteFileName = raw_input("vehicleRouteFileName?")
trafficLightFileName = raw_input("trafficLightFileName?")
print calcSingleXOneWayTotalTime(vehicleRouteFileName, trafficLightFileName)