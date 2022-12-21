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
			print(input[i + 3])
			for y in range(i + 3, len(input)):
				if allCharactersDifferent(input[y: y + 14]):
					return y + 14
	return None

print("How many characters need to be processed before the first start-of-packet marker is detected?")
print(solution(input))