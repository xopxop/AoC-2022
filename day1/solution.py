file = open("./input", "r")
input = (file.read())

def totalCalories(caloriesList: str):
  totalCalories = 0
  for calories in caloriesList:
    totalCalories += int(calories)
  return totalCalories

def getCaloriesPerElseList(input: str):
  return input.split('\n\n')

def findMaxCaloriesPerElfList(input: str):
  maxCaloriesPerElfList = []
  caloriesPerElfList = getCaloriesPerElseList(input)
  for caloriesPerElf in caloriesPerElfList:
    caloriesList = caloriesPerElf.splitlines()
    totalCaloriesPerElf = totalCalories(caloriesList)
    maxCaloriesPerElfList.append(totalCaloriesPerElf)
  return maxCaloriesPerElfList

maxCaloriesPerElfList = findMaxCaloriesPerElfList(input)
maxCaloriesPerElfList.sort(reverse=True)
print('How many total Calories is that Elf carrying?')
print(maxCaloriesPerElfList[0])
print('How many Calories are those Elves carrying in total?')
print(maxCaloriesPerElfList[0] + maxCaloriesPerElfList[1] + maxCaloriesPerElfList[2])
