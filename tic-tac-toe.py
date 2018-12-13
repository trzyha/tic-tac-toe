#Tic-Tac-Toe game
xo_change = 1

board_array = (["7", "|", "8", "|", "9"],
               ["---", "-", "---", "-", "---"],
               ["4", "|", "5", "|", "6"],
               ["---", "-", "---", "-", "---"],
               ["1", "|", "2", "|" ,"3"])

takenField = []

def draw_array():
  for elem in board_array:
    print ("{: ^3} {: ^1} {: ^3} {: ^1} {: ^3} ".format(*elem))

def xo():
  if xo_change %2 == 0:
    return "O"
  elif xo_change %2 != 0:
    return "X"

def clean():
  cls = lambda: print('\n'*100)
  cls()
  
def checkGameStatus():
  if (board_array[0][0] == "X" and board_array[0][2] == "X" and board_array[0][4] == "X") or (board_array[2][0] == "X" and board_array[2][2] == "X" and board_array[2][4] == "X") or (board_array[4][0] == "X" and board_array[4][2] == "X" and board_array[4][4] == "X") or (board_array[0][0] == "X" and board_array[2][0] == "X" and board_array[4][0] == "X") or (board_array[0][2] == "X" and board_array[2][2] == "X" and board_array[4][2] == "X") or (board_array[0][4] == "X" and board_array[2][4] == "X" and board_array[4][4] == "X") or (board_array[0][0] == "X" and board_array[2][2] == "X" and board_array[4][4] == "X") or (board_array[0][4] == "X" and board_array[2][2] == "X" and board_array[4][0] == "X"):
    print ("X WON!")
    return False
  elif (board_array[0][0] == "O" and board_array[0][2] == "O" and board_array[0][4] == "O") or (board_array[2][0] == "O" and board_array[2][2] == "O" and board_array[2][4] == "O") or (board_array[4][0] == "O" and board_array[4][2] == "O" and board_array[4][4] == "O") or (board_array[0][0] == "O" and board_array[2][0] == "O" and board_array[4][0] == "O") or (board_array[0][2] == "O" and board_array[2][2] == "O" and board_array[4][2] == "O") or (board_array[0][4] == "O" and board_array[2][4] == "O" and board_array[4][4] == "O") or (board_array[0][0] == "O" and board_array[2][2] == "O" and board_array[4][4] == "O") or (board_array[0][4] == "O" and board_array[2][2] == "O" and board_array[4][0] == "O"):
    print ("O WON!")
    return False
  elif (board_array[0][0] == ("O" or "X")):
    print ("DRAW")
    return False
  else:
    print ("NOT YET!")
    return True

def checkTakenField(x):
  if any(x in sublist for sublist in takenField) == True:
    takenField.append(x)
    return False
  else:
    takenField.append(x)
    return True
    
clean()
print ("Tic-Tac-Toe GAME (use NumPad)")
draw_array()

while checkGameStatus() == True:
  pos = input("It is %s turn (1-9) [q - quit]: " % xo() )
  if checkTakenField(pos) == True:
    print (takenField)
  #if pos = 0 and pos <=9:
    if pos == "7":
      clean()
      board_array[0][0] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "8":
      clean()
      board_array[0][2] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "9":
      clean()
      board_array[0][4] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "4":
      clean()
      board_array[2][0] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "5":
      clean()
      board_array[2][2] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "6":
      clean()
      board_array[2][4] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "1":
      clean()
      board_array[4][0] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "2":
      clean()
      board_array[4][2] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "3":
      clean()
      board_array[4][4] = xo()
      draw_array()
      xo_change = xo_change + 1
    elif pos == "q":
      print ("You've quit :(((((")
      break
    else:
      pos = input("Again! Your move (1-9): ")