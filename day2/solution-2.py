file = open("./input", "r")
input = file.read()

class Play:
	rock = "A"
	paper = "B"
	scissors = "C"

class Strategy:
  lost = "X"
  draw = "Y"
  win = "Z"

class PlayScore:
	rock = 1
	paper = 2
	scissors = 3

class Result:
	lost = 0
	draw = 3
	win = 6

def getPlayScoreBasedOnResultScore(playerOnePlay: PlayScore, resultScore: Result):
	match resultScore:
		case Result.lost:
			match playerOnePlay:
				case PlayScore.rock:
					return PlayScore.scissors
				case PlayScore.paper:
					return PlayScore.rock
				case PlayScore.scissors:
					return PlayScore.paper
		case Result.draw:
			match playerOnePlay:
				case PlayScore.rock:
					return PlayScore.rock
				case PlayScore.paper:
					return PlayScore.paper
				case PlayScore.scissors:
					return PlayScore.scissors
		case Result.win:
			match playerOnePlay:
				case PlayScore.rock:
					return PlayScore.paper
				case PlayScore.paper:
					return PlayScore.scissors
				case PlayScore.scissors:
					return PlayScore.rock
	return 0

def getPlayScore(play: str):
	match play:
		case Play.rock:
			return PlayScore.rock
		case Play.paper:
			return PlayScore.paper
		case Play.scissors:
			return PlayScore.scissors
	return 0

def getResultScore(strategy: str):
	match strategy:
		case Strategy.lost:
			return Result.lost
		case Strategy.draw:
			return Result.draw
		case Strategy.win:
			return Result.win
	return 0

def getScore(round: str):
	players = round.split(' ')
	playerOnePlayScore = getPlayScore(players[0])
	resultScore = getResultScore(players[1])
	playerTwoPlayScore = getPlayScoreBasedOnResultScore(playerOnePlayScore, resultScore)
	return playerTwoPlayScore + resultScore

def getTotalScore(input: str):
	scoreList = []
	theTournament = input.split("\n")
	for eachRound in theTournament:
		score = getScore(eachRound)
		scoreList.append(score)
	return sum(scoreList)

print("what would your total score be if everything goes exactly according to your strategy guide?")
print(getTotalScore(input))
