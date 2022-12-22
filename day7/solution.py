file = open("./input", "r")
input = file.read()

size = 0

class File:
	def __init__(self, name, size):
		self.name = name
		self.size = size

class Dir:
	def __init__(self, name):
		self.name = name
		self.size = 0
		self.subDirs = []
		self.files = []

def nextLevelDir(dir: Dir, name: str):
	for subdir in dir.subDirs:
		if subdir.name == name:
			return subdir
	return None

def createFileSystem(lines: [str]):
	dirsStack = []
	for line in lines:
		input = line.split(' ')
		if input[0] == '$':
			if input[1] == 'cd':
				if input[2] == '..':
					dirsStack[-2].size += dirsStack.pop().size
				else:
					if len(dirsStack) == 0 and input[2] == '/':
						dirsStack.append(Dir(input[2]))
					else:
						dirsStack.append(nextLevelDir(dirsStack[-1], input[2]))
			continue
		if input[0] == 'dir':
			dirsStack[-1].subDirs.append(Dir(input[1]))
		else:
			dirsStack[-1].files.append(File(input[1], input[0]))
			dirsStack[-1].size += int(input[0])
	if len(dirsStack) != 0:
		loopNo = len(dirsStack)
		index = 0
		while index < loopNo - 1:
			dirsStack[-2].size += dirsStack.pop().size
			index += 1
		return dirsStack[-1]

def countDirectory(dir: Dir):
	global size
	if dir.size <= 100000:
		size += dir.size
	for subdir in dir.subDirs:
		countDirectory(subdir)

def solution(input):
	lines = input.split('\n')
	root = createFileSystem(lines)
	countDirectory(root)
	print(size)

print("What is the sum of the total sizes of those directories?")
solution(input)