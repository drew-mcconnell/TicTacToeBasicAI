import random
import replit
from GameRecord import GameRecord
import TicTacToe

def checkForNumTies(logFile, tieMax):
  games = TicTacToe.getPastGames(logFile)

  tieCount = 0
  for i in range(len(games)-1, 0, -1):
    #print("i:", i)
    print("game winner: ", games[i].winner)
    if(games[i].winner != "T"):
      print("game is not a tie")
      return -1
    else:
      tieCount += 1
      print("game is a tie")
      print("ties in a row: ", tieCount)
      if(tieCount >= tieMax):
        print("10 ties")
        return len(games)

  return -1

if __name__=="__main__":
  
  runType = input("Do you want to play player vs. computer (1) or computer vs. computer? (2)")

  #run player vs. computer
  if(runType == '1'):
    TicTacToe.runGame('GameLog.txt', "pvc", TicTacToe.calculateWinIndexByPercentage, 10)
  
  #run algorithm tests w/ computer vs. computer
  else:

    for i in range(10):
      print("i: ", i)
      log = "TestLog.txt"
      logFile = open(log,'w')
      logFile.truncate()
      logFile.close()

      while True:
        
        tieMax = 10
        randomizationNum = 10
        TicTacToe.runGame(log, "cvc", TicTacToe.calculateWinIndexByPercentage, randomizationNum)

        tieNum = checkForNumTies(log, tieMax)
        if(tieNum != -1):
          print("Ten Ties Reached after", tieNum, "games.")
          f = open("AlgorithmLog.txt", 'a');
          fileString = "TieMax: " + str(10) + "\nGames until reached tieMax: " + str(tieNum) + "\nRandomization num: " + str(randomizationNum) + "\nWinIndexType: percentage\n"
          f.write(fileString)
          f.close()
          break
          #erase log file
      logFile = open(log,'w')
      logFile.truncate()
      logFile.close()
        
