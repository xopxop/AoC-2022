file = open("./input", "r")
input = file.read()

def convertPriority(item: chr):
	rawPriority = ord(item)
	if (rawPriority >= 65 and rawPriority <= 90):
		return rawPriority - 38
	elif (rawPriority >= 97 and rawPriority <= 122):
		return rawPriority - 96
	return None

def getItem(firstCompartment: str, secondCompartment: str):
	for item in firstCompartment:
		if item in secondCompartment:
			return item
	return None

def getPriority(ruckSack: str):
	firstCompartment, secondCompartment = ruckSack[:len(ruckSack)//2], ruckSack[len(ruckSack)//2:]
	item = getItem(firstCompartment, secondCompartment)
	return convertPriority(item)

def listOfShareItem(input: str):
	priorityList = []
	ruckSacks = input.split("\n")
	for eachRuckSack in ruckSacks:
		priority = getPriority(eachRuckSack)
		priorityList.append(priority)
	return priorityList

print("What is the sum of the priorities of those item types?")
print(sum(listOfShareItem(input)))
