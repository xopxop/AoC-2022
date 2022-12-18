import re
file = open("./input", "r")
input = file.read()

class CRATE:
	def __init__(self, name: str):
		self.name = name

class STACK:
	def __init__(self):
		self.crates = []

class INSTRUCTION:
	def __init__(self, createNo, fromStack, toStack):
		self.createNo = createNo
		self.fromStack = fromStack
		self.toStack = toStack

def populateStacks(stacks, crateLevels: str):
	for eachLevel in reversed(crateLevels):
		stackIndex = 0
		for i in range(0, len(eachLevel)):
			if i % 4 == 0:
				if eachLevel[i] == '[':
					stacks[stackIndex].crates.append(CRATE(eachLevel[i + 1]))
				stackIndex += 1

def getStacks(stackContainer: str):
	stackNo = int(stackContainer.split('\n')[-1].strip().split('   ')[-1])
	stacks = [STACK() for i in range(stackNo)]
	populateStacks(stacks, stackContainer.split('\n')[:-1])
	return stacks

def getInstruction(instructionsContainer: str):
	instructions = []
	for instruction in instructionsContainer.split('\n'):
		words = instruction.split(' ')
		instructions.append(INSTRUCTION(words[1], words[3], words[5]))
	return instructions

def solution(input: str):
	inputContainer = input.split('\n\n')
	stacks = getStacks(inputContainer[0])
	instructions = getInstruction(inputContainer[1])
	for instruction in instructions:
		fromStack = stacks[int(instruction.fromStack) - 1]
		toStack = stacks[int(instruction.toStack) - 1]
		for i in range(0, int(instruction.createNo)):
			toStack.crates.append(fromStack.crates.pop())
	answer = ""
	for stack in stacks:
		answer += stack.crates[-1].name
	return answer

print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
print(solution(input))