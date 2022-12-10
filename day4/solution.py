file = open("./input", "r")
input = file.read()

def fullyContainedByOneAnother(assignmentPairs: str):
	assignments = assignmentPairs.split(',')
	assignmentOne = assignments[0].split('-')
	assignmentTwo = assignments[1].split('-')
	if int(assignmentOne[0]) <= int(assignmentTwo[0]) and int(assignmentOne[1]) >= int(assignmentTwo[1]):
		return True
	elif int(assignmentTwo[0]) <= int(assignmentOne[0]) and int(assignmentTwo[1]) >= int(assignmentOne[1]):
		return True
	return False

def solution(input: str):
	fullyContainedAssignmentPairs = []
	assignmentPairsList = input.split('\n')
	for assignmentPairs in assignmentPairsList:
		if fullyContainedByOneAnother(assignmentPairs):
			fullyContainedAssignmentPairs.append(assignmentPairs)
	return fullyContainedAssignmentPairs

print("In how many assignment pairs does one range fully contain the other?")
print(len(solution(input)))
