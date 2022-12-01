file = open("./input", "r")
input = (file.read())

def totalCalories(caloriesList: str):
  totalCalories = 0
  for calories in caloriesList:
    totalCalories += int(calories)
  return totalCalories

def getCaloriesPerElseList(input: str):
  return input.split('\n\n')

def findMaxCalories(input: str):
  maxCalories = 0
  caloriesPerElfList = getCaloriesPerElseList(input)
  for caloriesPerElf in caloriesPerElfList:
    caloriesList = caloriesPerElf.splitlines()
    totalCaloriesPerElf = totalCalories(caloriesList)
    if totalCaloriesPerElf > maxCalories:
      maxCalories = totalCaloriesPerElf
  return maxCalories

print(findMaxCalories(input))