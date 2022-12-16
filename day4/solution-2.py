file = open("./input", "r")
input = file.read()

def overlap(assignmentPairs: str):
	assignments = assignmentPairs.split(',')
	assignmentOne = assignments[0].split('-')
	assignmentTwo = assignments[1].split('-')
	assignmentOneArray = range(int(assignmentOne[0]), int(assignmentOne[1]) + 1)
	assignmentTwoArray = range(int(assignmentTwo[0]), int(assignmentTwo[1]) + 1)
	if int(assignmentTwo[0]) in assignmentOneArray:
		return True
	elif int(assignmentTwo[1]) in assignmentOneArray:
		return True
	elif int(assignmentOne[0]) in assignmentTwoArray:
		return True
	elif int(assignmentOne[1]) in assignmentTwoArray:
		return True
	return False

def solution(input: str):
	fullyContainedAssignmentPairs = []
	assignmentPairsList = input.split('\n')
	for assignmentPairs in assignmentPairsList:
		if overlap(assignmentPairs):
			fullyContainedAssignmentPairs.append(assignmentPairs)
	return fullyContainedAssignmentPairs

print("In how many assignment pairs do the ranges overlap?")
print(len(solution(input)))
