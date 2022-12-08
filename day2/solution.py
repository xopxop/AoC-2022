file = open("./input", "r")
input = file.read()

class Play:
	rock = "AX"
	paper = "BY"
	scissors = "CZ"

class PlayScore:
	rock = 1
	paper = 2
	scissors = 3

class Result:
	lost = 0
	draw = 3
	win = 6

def getPlayResult(playerOnePlay, playerTwoPlay):
	match playerTwoPlay:
		case PlayScore.rock:
			match playerOnePlay:
				case PlayScore.rock:
					return Result.draw
				case PlayScore.paper:
					return Result.lost
				case PlayScore.scissors:
					return Result.win
		case PlayScore.paper:
			match playerOnePlay:
				case PlayScore.rock:
					return Result.win
				case PlayScore.paper:
					return Result.draw
				case PlayScore.scissors:
					return Result.lost
		case PlayScore.scissors:
			match playerOnePlay:
				case PlayScore.rock:
					return Result.lost
				case PlayScore.paper:
					return Result.win
				case PlayScore.scissors:
					return Result.draw
	return 0

def getPlayScore(play: str):
	if (play in Play.rock):
		return PlayScore.rock
	elif (play in Play.paper):
		return PlayScore.paper
	elif (play in Play.scissors):
		return PlayScore.scissors
	return 0

def getScore(round: str):
	players = round.split(' ')
	playerOnePlayScore = getPlayScore(players[0])
	playerTwoPlayScore = getPlayScore(players[1])
	resultScore = getPlayResult(playerOnePlayScore, playerTwoPlayScore)
	return playerTwoPlayScore + resultScore

def getTotalScore(input: str):
	scoreList = []
	theTournament = input.split("\n")
	for eachRound in theTournament:
		score = getScore(eachRound)
		scoreList.append(score)
	return sum(scoreList)

print("What would your total score be if everything goes exactly according to your strategy guide?")
print(getTotalScore(input))
