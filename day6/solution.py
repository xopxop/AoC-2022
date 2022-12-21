file = open("./input", "r")
input = file.read()

def allCharactersDifferent(sequence: str):
	for character in sequence:
		if sequence.count(character) > 1:
			return False
	return True

def solution(input: str):
	for i in range(0, len(input)):
		if allCharactersDifferent(input[i: i + 4]):
			return i + 4
	return None

print("How many characters need to be processed before the first start-of-message marker is detected?")
print(solution(input))