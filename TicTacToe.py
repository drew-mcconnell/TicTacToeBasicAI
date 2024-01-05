import random
import replit
from GameRecord import GameRecord

def printBoard(board):
  #replit.clear()
  print(board[0], '|', board[1], '|', board[2])
  print("----------")
  print(board[3], '|', board[4], '|', board[5])
  print("----------")
  print(board[6], '|', board[7], '|', board[8])
  print("\n")

def isMoveTaken(move, board):
  #TODO1
  if board[move] == 'X' or board[move] == 'O':
    #print("move taken")
    return True
  
  #print("move not taken")
  return False

def getMove(board):
  while True:
    move = input("What's your move?")
    try:
      move = int(move)
      if not isMoveTaken(move-1, board):
        return move
      else:
        print("This place has already been taken. Try again.")
    except: 
      print("That is not a valid move. Please enter a number between 1-9 that has not been used before.")

def checkForWinner(board):
  if(board[0] == board[1] and board[0] == board[2] or
  board[3] == board[4] and board[3] == board[5] or 
  board[6] == board[7] and board[6] == board[8] or 
  board[0] == board[3] and board[0] == board[6] or
  board[1] == board[4] and board[1] == board[7] or
  board[2] == board[5] and board[2] == board[8] or
  board[0] == board[4] and board[0] == board[8] or
  board[2] == board[4] and board[2] == board[6]):
    return True
  
  return False

def isCorner(move, moveList):
  if(move in [1,3,7,9]):
    return True
  return False

def isMiddle(move):
  return move == 5

def randomlyPickCorner():
  return random.randint(1, 3, 7, 9)

def computerTurnRandom(board, stage, moveList):
  #numbers are based on numbers printed to user (1-9), not indices (0-8)
  if stage == 0:
    #for first stage, randomly choose corner
    return randomlyPickCorner
  elif stage == 1:
    #get player's last move
    playersLastMove = moveList[stage-1]
    
    #if user played in corner, play in middle
    if(isCorner(playersLastMove)):
      return 4
    #if user played in middle or side, play in a corner
    else:
      return randomlyPickCorner()
    
  elif stage == 2:
    #TODO
    print()

  elif stage == 3:
    #TODO
    print()
  elif stage == 4:
    print()
  elif stage == 5:
    print()
  elif stage == 6:
    print()
  elif stage == 7:
    print()
  elif stage == 8:
    print()
  elif stage == 9:
    print()
    
def restart():
  #restart = input("Do you want to play again?")
  #if(restart == 'no' or restart == "No" or restart == "NO" or restart == "n"):
  #  return False
  #else:
  return True

def logGame(board, moveList, winner, file):
  newGame = GameRecord(board, moveList, winner)
  f = open(file, "a")
  f.write(newGame.__str__())
  f.close()
  print("logged game in:", file)

def getPastGames(file):
  
  gameList = []
  f = open(file, 'r')
  numLines = len(open(file).readlines())

  for x in range(0, numLines, 3):
    
    #print("reading new game")
    
    tempGame = GameRecord()
    tempGame.board = []
    tempGame.moveList = []
    
    b = f.readline()
    #print("b: ", b)
    for i in b[:-1]:
      tempGame.board.append(i)
    #print("tempGame.board: ", tempGame.board)
    #tempGame.board = f.readline()
    
    mL = f.readline()
    #print("mL: ", mL)
    for j in mL[:-1]:
      tempGame.moveList.append(int(j))
    #tempGame.moveList = f.readline()
    #print("tempGame.moveList: ", tempGame.moveList)
    
    tempGame.winner = f.readline()[0]
    #print("winner: ", tempGame.winner)

    gameList.append(tempGame)
    #print("tempGame: ", tempGame)

  #print("all games:")
  #for x in gameList:
  #  print(x)
  f.close()
  return gameList

def sameCurrentState(currentGameMoveList, oldGameMoveList):
  #print("\ncurrentGameMoveList: ", currentGameMoveList)
  #print("oldGameMoveList: ", oldGameMoveList)
  
  #get old game state only until current stage
  oldGameMoveListUntilCurrentStage = oldGameMoveList[:len(currentGameMoveList)]
  #get difference of movelists up until the current stage
  difference = set(currentGameMoveList).difference(set(oldGameMoveListUntilCurrentStage))
  #print("Difference: ", difference)

  #turn difference into boolean and return False if there is a difference (will be False if there is no difference, so this will evaluate to True if they are different)
  if(bool(difference)):
    return False

  #if no difference in moveLists, compare X's and O's to see if the players have the same spots in both boards
  #get array of every other index starting at 0
  currentXs = set(currentGameMoveList[::2])
  #print(currentXs)
  
  #get array of every other index starting at 1
  currentOs = set(currentGameMoveList[1:len(currentGameMoveList):2])
  #print(currentOs)
  
  #get array of every other index starting at 0
  oldXs = set(oldGameMoveList[::2])
  #print(oldXs)
  
  #get array of every other index starting at 1
  oldOs = set(oldGameMoveList[1:len(oldGameMoveList):2])
  #print(oldOs)
  
  boardsAreSame = not bool(currentXs.difference(oldXs)) and not bool(currentOs.difference(oldOs))
  #print("boards are the same: ", boardsAreSame)

  return boardsAreSame

def calculateWinIndexBySimpleMath(wins, ties, losses):
  #wins weighted: 2
  #ties weighted: 1
  #loss weighted: -1
  return (wins * 2) + ties - losses

def calculateWinIndexByPercentage(wins, ties, losses):
  #calculate percentage, then
  #win percentage weighted: 2
  #tie percentage weighted: 1
  #loss percentage weighted: -1
  totalMoves = wins + ties + losses
  winPercentage = float(wins / totalMoves) if totalMoves > 0 else 0
  tiePercentage = float(ties / totalMoves) if totalMoves > 0 else 0
  lossPercentage = float(losses / totalMoves) if totalMoves > 0 else 0
  return round((winPercentage * 2) + tiePercentage - lossPercentage, 2)

#TODO
def computerTurnPredictive():
  # STRATEGY 2
  # other strategy could be to run possibilities for moves from current stage through the end, determine if they end in a win, they decide on the best move

  #iterate from current stage to the end, testing every open move to see which one ends in a win
  #if none end in a win, choose one that ends in a tie
  #if none end in a tie, choose randomly from open moves
  print()

def computerTurnHistorical(currentBoard, currentMoveList, computerSymbol, logFile, winIndexFunc, randomizationValue):
  # STRATEGY 1
  # AI Computer ideas
  # keep track of game states over time
  # each time the computer needs to make a move,
  # consult past game states and determine if certain moves at that stage led to a win or a loss
  #
  # important factors to take into account:
  #   1. stage
  #   2. previous moves
  #   3. move on current stage
  #   3. if ^ move ended in win, loss, or tie
  #   4. ?
  #
  # decision-making process for a given turn
  #   1. iterate through past games
  #   2. if old game state is same as current state
  #   3. then look at move from old game
  #   4. if game ended in win, add tally for that move
  #   5. keep tally for every unique move at the current stage with the same game state
  #   6. if game ended in tie, keep tally for ties, but keep moving
  #   7. if game ended in loss, don't make move
  #   8. make move associated with the most wins
  #   9. if all games ended in loss, try new move or random move

  remainingSpots = list(set([1,2,3,4,5,6,7,8,9]) - set(currentMoveList))
  #print("moveList: ", currentMoveList)
  #print("remainingSpots: ", remainingSpots)
  #print("computer symbol: ", computerSymbol)

  gameList = getPastGames(logFile)
  #print("number of historical games: ", len(gameList))
  gamesWithCurrentState = []

  winningGames = []
  tyingGames = []
  losingGames = []
  currentStage = len(currentMoveList)

  #find all games with the current game state at current stage
  for i in gameList:
    #print("\ncomparing game state")
    isSameState = sameCurrentState(currentMoveList, i.moveList)
    #print(i)
    #print("is same current state: ", isSameState)
    #find all games with the same state
    if(isSameState):
      gamesWithCurrentState.append(i)
    

  #print("gamesWithCurrentState: ", len(gamesWithCurrentState))
  #sort winning, tying, and losing games from the same state
  for game in gamesWithCurrentState:
    #print("checking winner")
    if(game.winner == computerSymbol):
      #print("winning game")
      winningGames.append(game)
    elif(game.winner == 'T'):
      #print("tying game")
      tyingGames.append(game)
    else:
      #print("losing game")
      losingGames.append(game)

  #for each possibly next play, tally the times it has resulted in a win, tie, or loss, and use all three to calculate chance of winning with that play
  nextWinMoves = [0,0,0,0,0,0,0,0,0]
  nextTieMoves = [0,0,0,0,0,0,0,0,0]
  nextLoseMoves = [0,0,0,0,0,0,0,0,0]
    
  for game in winningGames:
    nextWinMoves[game.moveList[currentStage]-1] += 1
  #print("nextWinMoves: ", nextWinMoves)

  for game in tyingGames:
    nextTieMoves[game.moveList[currentStage]-1] += 1
  #print("nextTieMoves: ", nextTieMoves)
  
  for game in losingGames:
    nextLoseMoves[game.moveList[currentStage]-1] += 1
  #print("nextLoseMoves: ", nextLoseMoves)

  #find index (the move number) of that's most likely to win
  nextBestMoves = [0,0,0,0,0,0,0,0,0]
  
  #start bestMoveIndex at the index of the first remaining spot to avoid the best index being a spot that is already taken (if everything else is <0)
  bestMoveIndex = remainingSpots[0]-1

  #iterate through moves to find the move that is most likely to result in a win
  for i in range(9):
    nextBestMoves[i] = winIndexFunc(nextWinMoves[i], nextTieMoves[i], nextLoseMoves[i])
    #calculateWinIndexByPercentage(nextWinMoves[i], nextTieMoves[i], nextLoseMoves[i])#calculateWinIndexBySimpleMath(nextWinMoves[i], nextTieMoves[i], nextLoseMoves[i])

    #store best index if it's greater than current best AND found in remainingSpots
    if((nextBestMoves[i] > nextBestMoves[bestMoveIndex]) and ((i+1) in remainingSpots)):
      bestMoveIndex = i
  
  #print("nextBestMoves: ", nextBestMoves)
  #print("bestMoveIndex: ", bestMoveIndex)
  
  #print("choosing randomly from: ", remainingSpots)
    
  
  #find all of the options with the highest rating (could be less than 0) and choose randomly from them (it's an index, so the actually move is one higher (1-9))
  equallyBestIndices = []
  for i in range(len(nextBestMoves)):
    #add index to equallyBestIndices if it's rating equals the current best and it is found in remainingSpots
    if((nextBestMoves[i] == nextBestMoves[bestMoveIndex]) and ((i+1) in remainingSpots)):
      equallyBestIndices.append(i)
  #print("equallyBestIndices: ", equallyBestIndices)

  #-------------- TODO ----------------
  # add option for randomly doing something unpredictable 1 in 10 chance
  if(random.randint(0,randomizationValue) == 0):
    #print("randomizing some craziness")
    return random.choice(remainingSpots)
  else:
    return random.choice(equallyBestIndices) + 1
    

def runGame(logFile, playType, winIndexFunction, randomizationValue):
  board = ['1','2','3','4','5','6','7','8','9']
  stage = 1 #keeps track of which move we're on
  moveList = []
  #logFile = input("What log file would you like to use? ") #"PercentageTestCpuVsCpuWithRandom100.txt"
  #winIndexFunction = calculateWinIndexByPercentage

  #playType = input("Player vs. computer (pvc) or Computer vs. Computer (cvc)?")

  printBoard(board)

  currentPlayerSymbol = 'X' #X goes first

  startingPlayer = random.randint(0,1)

  #if doing player vs. computer
  if(playType == "pvc"):
    #print("startingPlayer: ", startingPlayer)
    if(startingPlayer):
      print("Computer goes first")
    else:
      print("Player goes first")

  #computerTurnHistorical(['1','X','3','4','X','6','O','X','O'], [4,8,7,6,1], 'O')
  while True:

    #if it's player's turn
    if(((startingPlayer == 0 and (stage % 2)) or (startingPlayer == 1 and not(stage % 2))) and (playType == "pvc")):
      print("Player's move")
      #player vs. computer
      move = getMove(board)
      
      #computer vs. computer
      #move = computerTurnHistorical(board, moveList, currentPlayerSymbol, logFile, winIndexFunction)
      
    #if it's cpu's turn
    #elif(startingPlayer == 1 and not(stage % 2) or (startingPlayer == 0 and (stage % 2))):
    else:
      print("Computer's move")
      move = computerTurnHistorical(board, moveList, currentPlayerSymbol, logFile, winIndexFunction, randomizationValue)
      
    
    board[move-1] = currentPlayerSymbol
    moveList.append(move)

    printBoard(board)

    #print("move: ", move)

    if(checkForWinner(board)):
      print(currentPlayerSymbol + " wins!\nLet's start over.\n")
      logGame(board, moveList, currentPlayerSymbol, logFile)
      if(restart()):
        break
      else:
        exit()
    elif(stage == 9):
      print("It's a tie! Let's start over.\n")
      logGame(board, moveList, "T", logFile)
      if(restart()):
        break
      else:
        exit()
    
    stage += 1
    #print("\n\nstage: ", stage)
    if(currentPlayerSymbol == 'X'):
      currentPlayerSymbol = 'O'
    else:
      currentPlayerSymbol = 'X'

#if __name__=="__main__":
#    for i in range(1000):
#      main()