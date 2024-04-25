
board = [1,2,3,4,5,6,7,8,9]


#to make X the first player,we assume the current player is O
current = "X"
def switchPlayer():
	global current
	if current == "X":
		current = "O"
		return "X"
	else:
		current = "X"
		return "O"



#draws the board
def drawBoard():
	print(f""" 

		{board[0]} | {board[1]} | {board[2]}
		{board[3]} | {board[4]} | {board[5]}
		{board[6]} | {board[7]} | {board[8]}

	""")


def getAllSides():
	#get rows
	firstRow = []
	secRow = []
	thirdRow = []


	#get columns
	firstCol = []
	secCol = []
	thirdCol = []

	#get diagonals
	firstDiagonal = []
	secDiagonal = []

	i = 0
	while i < len(board):
		#get rows
		if i < 3:
			firstRow.append(board[i])
		elif i > 2 and i < 6:					#don't understand why i < 2
			secRow.append(board[i])
		elif i > 5:								#don't understand why i > 5
			thirdRow.append(board[i])

		#get columns
		if i in [0,3,6]:
			firstCol.append(board[i])

		elif i in [1,4,7]:
			secCol.append(board[i])

		elif i in [2,5,8]:
			thirdCol.append(board[i])


		#get diagonals
		if i in [0,4,8]:
			firstDiagonal.append(board[i])

		if i in [2,4,6]:
			secDiagonal.append(board[i])

		i += 1

	#add all side to this dict and return it
	allSides = {"firstRow":firstRow,"secRow":secRow,"thirdRow":thirdRow,"firstCol":firstCol,"secCol":secCol,"thirdCol":thirdCol,"firstDiagonal":firstDiagonal,"secDiagonal":secDiagonal}
	return allSides
		


def checkWinner():
	sides = getAllSides()
	winner = ""
	gameWon = False
	draw = False


	#check for win first row
	for sideName,value in sides.items():
		if value[0] == "X" and value[1] == "X" and value[2] == "X":
			winner = "X" 
			gameWon = True
			print(f"{winner} won!!")
			
		elif value[0] == "O" and value[1] == "O" and value[2] == "O":
			winner = "O"
			gameWon = True
			print(f"{winner} won!!")

	#check for draw/no winner
	for cell in board:
		if type(board[0]) != int and  type(board[1]) !=  int and type(board[2]) !=  int:
			if type(board[3]) !=  int and type(board[4]) !=  int and  type(board[5]) !=  int:
				if type(board[6]) !=  int and type(board[7]) !=  int and type(board[8]) !=  int:
					draw = True
					
			
	if draw and not gameWon:
		print("Draw!Game over")
		gameWon = True

	if not gameWon:
		return False
	else:
		return True



def playGame():
	play = True
	while play:
		drawBoard()
		if checkWinner():
			play = False
			break
		currentPlayer = switchPlayer()	
		print(f"{currentPlayer}'s turn to play")
		cellNumb = input("Enter cell number to store: ")


		if cellNumb == "cls":
			play = False
			break

		try:
			cellNumb = int(cellNumb)
		except ValueError:
			print("Please Enter a number")

		if cellNumb > 9 or cellNumb  < 1: 
			print("Please enter numbers 1-9")
			playGame()

		i = 0
		while i < len(board):
			if board[i] == cellNumb:
				if board[i] == "X" or board[i] == "O":
					print("Please choose an empty slot!")
					return
				board[i] = currentPlayer
			i += 1



playGame()




