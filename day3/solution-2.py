file = open("./input", "r")
input = file.read()

def convertPriority(item: chr):
	rawPriority = ord(item)
	if (rawPriority >= 65 and rawPriority <= 90):
		return rawPriority - 38
	elif (rawPriority >= 97 and rawPriority <= 122):
		return rawPriority - 96
	return None

def getPriority(ruckSacks: []):
	allItem = "".join(ruckSacks)
	for item in allItem:
		if (item in ruckSacks[0] and item in ruckSacks[1] and item in ruckSacks[2]):
			return convertPriority(item)
	return None

def divideRuckSacksIntoGroup(ruckSacks: []):
	groups = []
	ruckSackIndex = 0
	groupIndex = -1
	for ruckSack in ruckSacks:
		if ruckSackIndex % 3 == 0:
			groups.append([])
			groupIndex += 1
		groups[groupIndex].append(ruckSack)
		ruckSackIndex += 1
	return groups

def listOfPriority(input: str):
	priorityList = []
	ruckSacks = input.split("\n")
	groups = divideRuckSacksIntoGroup(ruckSacks)
	for group in groups:
		priority = getPriority(group)
		priorityList.append(priority)
	return priorityList

print("What is the sum of the priorities of those item types?")
print(sum(listOfPriority(input)))


