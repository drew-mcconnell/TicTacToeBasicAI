class GameRecord:
  board = [] #final board
  moveList = [] #list in order that they were played
  winner = "" #"player" or "computer" or "tie"

  def __init__(self, board = [], moveList = [], winner = ""):
    self.board = board
    self.moveList = moveList
    self.winner = winner

  def __str__(self):
    output = ""
    for x in self.board:
      output += x
    
    output += "\n"

    for y in self.moveList:
      output += str(y)
    
    output += "\n" + self.winner + "\n"

    return output
  
  def __repr__(self):
    return self.__str__()