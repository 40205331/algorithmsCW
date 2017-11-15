import sys
# set colours for pieces
Black = '\033[94m'
Red = '\033[91m'
End = '\033[0m'

# create classes for pieces on the board
class hashtag(object):
	def __repr__(self):
		return hashtag()
	def __str__(self):
		return Black + "|   #   |" + End

class atsign(object):
	def __repr__(self):
		return atsign()
	def __str__(self):
		return Red + "|   @   |" + End

class emptySpace(object):
	def __repr__(self):
		return emptySpace()
	def __str__(self):
		return "|       |" 		

class hashtagKing(object):
	def __repr__(self):
		return hashtagKing()
	def __str__(self):
		return Black + "| King# " + End

class atsignKing(object):
	def __repr__(self):
		return atsignKing()
	def __str__(self):
		return Red + "| King@ |" + End
		
# create lists for items to be removed if pieces are taken
hashPieces = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
atPieces = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
noPieces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#method to remove a hashtag item from the list if a piece is taken
def hashPieceTaken(hashPieces, noPieces):
	#remove first item in the list
	hashPieces.pop(0)
	#reset the stalemate list
	noPieces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	# if list is empty other team wins
	if not hashPieces:
		print "Player 1 wins!"
		sys.exit()

#method to remove a atsign item from the list if a piece is taken
def atPiecesTaken(atPieces, noPieces):
	#remove first item in the list
	atPieces.pop(0)
	#reset stalemate list
	noPieces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	# if list is empty player 2 wins
	if not atPieces:
		print "Player 2 wins!"
		sys.exit()

# method for if there cant be a winner
def noPiecesLeft(noPieces):
	# remove first item in the list
	noPieces.pop(0)
	# if list is empty its a stalemate
	if not noPieces:
		print "Piece has not been taken in 40 turns. It's a stalemate"
		sys.exit() 

# create board
board =[["      ","   1   ", "     2    ","    3    ","    4    ","   5   ", "      6   ","    7    ","    8    "],
			['----------------------------------------------------------------------------------'], 
		 	["   2 " , emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag()],
		 	['----------------------------------------------------------------------------------'], 
		 	["   4 " , hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   6 " , emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag()],
		 	['----------------------------------------------------------------------------------'],
		 	["   8 " , emptySpace(), emptySpace(), emptySpace(), hashtagKing(), emptySpace(), emptySpace(), emptySpace(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   10 " , emptySpace(), emptySpace(), atsign(), emptySpace(), atsignKing(), emptySpace(), emptySpace(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   12 " , atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   14 " , emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign()], 
		 	['----------------------------------------------------------------------------------'],
		 	["   16 " , atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace()]]
#print board
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
	    for row in board]))

#team 1 logic
def team1(board):
	print "team 1 turn"
	while True:
		# validation for movement
		while True:
			# validation to make sure only numbers are entered
			RowCoordinate = raw_input ("enter row number: ")
			try:
				RowCoordinateInt = int(RowCoordinate)
			except SyntaxError:
				print "Please enter (only) a number: "	
				continue
			except ValueError:
				print "Please enter (only) a number: "	
				continue
			# if a number non even number from 2-16 is entered throw error
			if RowCoordinateInt not in [2, 4, 6, 8, 10, 12, 14, 16]:
				print "row coordinate out of range"
				continue 
			else:
				RowCoordinateInt = int(RowCoordinate)
				break

		# validation to make sure only numbers are entered
		while True:

			ColCoordinate = raw_input ("enter column number: ")
			try:
				ColCoordinateInt = int(ColCoordinate)
			except SyntaxError:
				print "Please enter (only) a number: "	
				continue
			except ValueError:
				print "Please enter (only) a number: "	
				continue
			# if a number out with 1-8 is entered throw error
			if ColCoordinateInt not in [1, 2, 3, 4, 5, 6, 7, 8]:
				print "column coordinate out of range"
				continue
			else:
				ColCoordinateInt = int(ColCoordinate)
				break
		
		# validation to make sure only numbers are entered
		while True:
			
			RowDestination = raw_input ("enter row number to move to: ")
			try:
				RowDestinationInt = int(RowDestination)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except ValueError:
				print "Please enter a number: "	
				continue
			# if a number non even number from 2-16 is entered throw error
			if RowDestinationInt not in [2, 4, 6, 8, 10, 12, 14, 16]:
				print "row coordinate out of range"
				continue 
			else:
				RowDestinationInt = int(RowDestination)
				break

		# validation to make sure only numbers are entered
		while True:

			ColDestination = raw_input ("enter column number to move to: ")
			try:
				ColDestinationInt = int(ColDestination)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except ValueError:
				print "please enter a number: "	
				continue
			# if a number out with 1-8 is entered throw error
			if ColDestinationInt not in [1, 2, 3, 4, 5, 6, 7, 8]:
				print "Column coordinate out of range"
				continue
			else:
				ColDestinationInt = int(ColDestination)
				break

		# Movement validations
		# if piece to move is an atsign
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
			# make sure piece cant move more than one column either way
			if type(board[RowCoordinateInt-2][ColCoordinateInt+1]) == type(emptySpace()) and type(board[RowCoordinateInt-2][ColCoordinateInt-1]) == type(emptySpace()):
				# make sure piece cant move more than one row forward
			 	if RowDestinationInt is not RowCoordinateInt - 2:
			 		print "error can only move one row forward"
			 		continue 
		
		# validation to make sure the piece moves forward
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
			if RowDestinationInt >= RowCoordinateInt:
				print "Invalid move. Must move diagonally forward"
				continue
				
		# validation to make sure king moves forward or backwards only one space
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
			if type(board[RowCoordinateInt-2][ColCoordinateInt+1]) == type(emptySpace()) and type(board[RowCoordinateInt-2][ColCoordinateInt-1]) == type(emptySpace()):
				if RowDestinationInt is not RowCoordinateInt - 2 or RowDestinationInt is not RowCoordinateInt + 2:
					print "Invalid move. Must move diagonally forward or backwards"
					continue
			
		# validation to make sure piece moves left or right
		if ColDestinationInt == ColCoordinateInt:
			print "Invalid move. Must move left or right"
			continue
			
		# validation to move on top of an enemy piece
		if type(board[RowDestinationInt][ColDestinationInt]) == type(hashtag()):
			print "Invalid move. Already a counter here"
			continue
			
		# validation to try move an opponents piece
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
			print "Invalid move. this is an enemy"
			continue
			
		# validation to move on top of your own piece
		if type(board[RowDestinationInt][ColDestinationInt]) == type(atsign()):
			print "Invalid move. Already a counter here"
			continue
			
		# validation to move an empty space
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(emptySpace()):
			print "Invalid move. Can't move empty space"
			continue
			
		# movement logic for a regular atsign to move the correct spaces to take enemy pieces forward and to the left and reprint board
		if RowCoordinateInt > 4:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
				if RowCoordinateInt > 4 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = atsign()
							hashPieceTaken(hashPieces, noPieces)
							if  RowDestinationInt == 2:
								board[RowDestinationInt][ColDestinationInt] = atsignKing()
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
		
		# movement logic for a regular atsign to move the correct spaces to take enemy pieces forward and to the right and reprint board
		if RowCoordinateInt > 4:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
				if RowCoordinateInt > 4 and ColCoordinateInt < 7:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtagKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = atsign()
							hashPieceTaken(hashPieces, noPieces)
							if  RowDestinationInt == 2:
								board[RowDestinationInt][ColDestinationInt] = atsignKing()
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
		
		# movement logic for a king atsign to move the correct spaces to take enemy pieces forward and to the right and reprint board
		if RowCoordinateInt > 4:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
				if RowCoordinateInt > 4 and ColCoordinateInt < 7 :	
					if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtagKing()):
							if RowDestinationInt < RowCoordinateInt:
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
								board[RowDestinationInt][ColDestinationInt] = atsignKing()
								hashPieceTaken(hashPieces, noPieces)
								if  RowDestinationInt == 2:
									board[RowDestinationInt][ColDestinationInt] = atsignKing()
									board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
									for row in board]))
								break
			
			# movement logic for a king atsign to move the correct spaces to take enemy pieces forward and to the left and reprint board
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):		
				if RowCoordinateInt > 4 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
							if RowDestinationInt < RowCoordinateInt: 
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
								board[RowDestinationInt][ColDestinationInt] = atsignKing()
								hashPieceTaken(hashPieces, noPieces)
								if  RowDestinationInt == 2:
									board[RowDestinationInt][ColDestinationInt] = atsignKing()
									board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
									for row in board]))
								break
		
		# movement logic for a regular atsign to move the correct spaces to take enemy pieces backwards and to the right and reprint board
		if RowCoordinateInt < 14:		
			if RowCoordinateInt < 14 and ColCoordinateInt < 7:
				if type(board[RowCoordinateInt + 4][ColCoordinateInt + 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
						if RowDestinationInt < RowCoordinateInt:
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt + 2][ColCoordinateInt + 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = atsignKing()
							hashPieceTaken(hashPieces, noPieces)
							if  RowDestinationInt == 2:
								board[RowDestinationInt][ColDestinationInt] = atsignKing()
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
		
			# movement logic for a regular atsign to move the correct spaces to take enemy pieces backwards and to the left and reprint board
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
				if RowCoordinateInt < 14 and ColCoordinateInt > 2:		
					if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
							if RowDestinationInt < RowCoordinateInt:
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
								board[RowDestinationInt][ColDestinationInt] = atsignKing()
								hashPieceTaken(hashPieces, noPieces)
								print "219"
								if  RowDestinationInt == 2:
									print "lllll"
									board[RowDestinationInt][ColDestinationInt] = atsignKing()
									board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
									for row in board]))
								break
		
		# movement logic for regular piece to move to an empty space 
		if RowDestinationInt >= 2:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = atsign()
				noPiecesLeft(noPieces)
				if  RowDestinationInt == 2:
					board[RowDestinationInt][ColDestinationInt] = atsignKing()
					board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break
		
		# # movement logic for king piece to move to an empty space 
		if RowDestinationInt >= 2:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = atsignKing()
				noPiecesLeft(noPieces)
				if  RowDestinationInt == 2:
					board[RowDestinationInt][ColDestinationInt] = atsignKing()
					board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break

# team 2 logic
def team2(board):
	print "team 2 turn"
	while True:
		# validation for movement
		while True:
			# make sure only numbers are entered 
			RowCoordinate = raw_input ("enter row number: ")
			try:
				RowCoordinateInt = int(RowCoordinate)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except ValueError:
				print "Please enter a number: "	
				continue
				# throw error if any non even number between 2 - 16 is entered
			if RowCoordinateInt not in [2, 4, 6, 8, 10, 12, 14, 16]:
				print "row coordinate out of range"
				continue 
			else:
				RowCoordinateInt = int(RowCoordinate)
				break

		while True:
			# make sure only numbers are entered
			ColCoordinate = raw_input ("enter column number: ")
			try:
				ColCoordinateInt = int(ColCoordinate)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except ValueError:
				print "Please enter a number: "	
				continue
			# throw error if number out with 1-8 is entered
			if ColCoordinateInt not in [1, 2, 3, 4, 5, 6, 7, 8]:
				print " Column coordinate out of range"
				continue
			else:
				ColCoordinateInt = int(ColCoordinate)
				break

		while True:
			# make sure only numbers are entered
			RowDestination = raw_input ("enter row number to move to: ")
			try:
				RowDestinationInt = int(RowDestination)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except ValueError:
				print "Please enter a number: "	
				continue
			# throw error if non even number between 2-16 is enetered
			if RowDestinationInt not in [2, 4, 6, 8, 10, 12, 14, 16]:
				print "row coordinate out of range"
				continue 
			else:
				RowDestinationInt = int(RowDestination)
				break

		while True:
			# make sure only number is entered
			ColDestination = raw_input ("enter column number to move to: ")
			try:
				ColDestinationInt = int(ColDestination)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except ValueError:
				print "please enter a number: "	
				continue
			# throw error if number outwith 1-8 is entered
			if ColDestinationInt not in [1, 2, 3, 4, 5, 6, 7, 8]:
				print "Column coordinate out of range"
			else:
				ColDestinationInt = int(ColDestination)
				break
		
		# Movement validations
		# if piece to move is an atsign
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
			# # make sure piece cant move more than one column either way
			if RowCoordinateInt < 16 and ColCoordinateInt < 8:
				if type(board[RowCoordinateInt + 2][ColCoordinateInt+1]) == type(emptySpace()) and type(board[RowCoordinateInt + 2][ColCoordinateInt-1]) == type(emptySpace()):
					# make sure piece cant move more than one row
					if RowDestinationInt is not RowCoordinateInt + 2:
						print "Invalid move. Must move forward"
						continue
		
		# validation to make the piece go forward 
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
			if RowDestinationInt <= RowCoordinateInt:
				print "Invalid move must move forward"
				continue
				
		# validation to make sure king moves forward or backwards only one space
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):
			if type(board[RowCoordinateInt + 2][ColCoordinateInt+1]) == type(emptySpace()) and type(board[RowCoordinateInt + 2][ColCoordinateInt-1]) == type(emptySpace()):
				if RowDestinationInt is not RowCoordinateInt - 2 or RowDestinationInt is not RowCoordinateInt + 2:
					print "Invalid move. Must move diagonally forward or backwards"
					continue
				
		# validation so that the piece must move left or righ
		if ColDestinationInt == ColCoordinateInt:
			print "Invalid move. Must move left or right"
			continue
			
		# validation so the piece cant move on top of your own piece
		if type(board[RowDestinationInt][ColDestinationInt]) == type(hashtag()):
			print "Invalid move. Already a counter here"
			continue
			
		# validation so you cant move an empty space
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(emptySpace()):
			print "Invalid move. Can't move empty space"
			continue
		
		# validation so you cant land on an enemy counter
		if type(board[RowDestinationInt][ColDestinationInt]) == type(atsign()):
			print "Invalid move. Already a counter here"
			continue
		
		# validation so you cant move an enemy
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
			print "Invalid move. this is an enemy"
			continue
		
		# movement logic for a regular hashtag to move the correct spaces to take enemy pieces forward and to the left and reprint board
		if RowCoordinateInt < 14:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
				if RowCoordinateInt < 14 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsign()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = hashtag()
							atPiecesTaken(atPieces, noPieces)
							if  RowDestinationInt == 16:
								board[RowDestinationInt][ColDestinationInt] = hashtagKing()
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
											for row in board]))
							break
							
		# movement logic for a regular hashtag to move the correct spaces to take enemy pieces forward and to the right and reprint board
		if RowCoordinateInt > 4:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
				if RowCoordinateInt < 14 and ColCoordinateInt < 7:
					if type(board[RowCoordinateInt + 4][ColCoordinateInt + 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(atsign()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt + 2][ColCoordinateInt + 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = hashtag()
							hashPieceTaken(hashPieces, noPieces)
							if  RowDestinationInt == 16:
								board[RowDestinationInt][ColDestinationInt] = hashtagKing()
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
		
		# movement logic for a king hashtag to move the correct spaces to take enemy pieces forward and to the right and reprint board
		if RowCoordinateInt < 14:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):	
				if RowCoordinateInt < 14 and ColCoordinateInt < 7:
					if type(board[RowCoordinateInt + 4][ColCoordinateInt + 2]) == type(emptySpace()):
						if RowDestinationInt > RowCoordinateInt:
							if type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(atsign()) or type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(atsignKing()):
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								board[RowCoordinateInt + 2][ColCoordinateInt + 1] = emptySpace()
								board[RowDestinationInt][ColDestinationInt] = hashtagKing()
								atPiecesTaken(atPieces, noPieces)
								if  RowDestinationInt == 16:
									board[RowDestinationInt][ColDestinationInt] = hashtagKing()
									board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
									for row in board]))
								break
			
			# movement logic for a hashtag king to move the correct spaces to take enemy pieces forward and to the left and reprint board
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				if RowCoordinateInt < 14 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsign()) or type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsignKing()):
							if RowDestinationInt > RowCoordinateInt:
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
								board[RowDestinationInt][ColDestinationInt] = hashtagKing()
								atPiecesTaken(atPieces, noPieces)
								if  RowDestinationInt == 16:
									board[RowDestinationInt][ColDestinationInt] = hashtagKing()
									board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
									for row in board]))
								break
						
		# movement logic for a king hashtag to move the correct spaces to take enemy pieces backward and to the right and reprint board
		if RowCoordinateInt > 4:		
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				if RowCoordinateInt > 4 and ColCoordinateInt < 7:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(atsign()) or type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(atsignKing()):
							if RowDestinationInt > RowCoordinateInt:
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
								board[RowDestinationInt][ColDestinationInt] = hashtagKing()
								atPiecesTaken(atPieces, noPieces)
								if  RowDestinationInt == 16:
									board[RowDestinationInt][ColDestinationInt] = hashtagKing()
									board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
									for row in board]))
								break
		
			# movement logic for a king hashtag to move the correct spaces to take enemy pieces backward and to the left and reprint board
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				if RowCoordinateInt > 4 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(atsign()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(atsignKing()):
							if RowDestinationInt > RowCoordinateInt:
								board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
								board[RowDestinationInt][ColDestinationInt] = hashtagKing()
								atPiecesTaken(atPieces, noPieces)
								if  RowDestinationInt == 16:
									board[RowDestinationInt][ColDestinationInt] = hashtagKing()
									board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
								print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
									for row in board]))
								break
						
		# movement logic if regular piece moves to an empty space
		if RowDestinationInt < 16:
			print "1"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = hashtag()
				noPiecesLeft(noPieces)
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break
		
		
			# movement logic if king piece moves to an empty space
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = hashtagKing()
				noPiecesLeft(noPieces)
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break

# loop team 1 then team 2
while True:
	team1(board)
	team2(board)