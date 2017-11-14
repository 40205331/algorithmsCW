import sys

Black = '\033[94m'
Red = '\033[91m'
End = '\033[0m'

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
		
hashPieces = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
atPieces = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
noPieces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def hashPieceTaken(hashPieces, noPieces):
	hashPieces.pop(0)
	noPieces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	if not hashPieces:
		print "Player 1 wins!"
		sys.exit()

def atPiecesTaken(atPieces, noPieces):
	atPieces.pop(0)
	noPieces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	if not atPieces:
		print "Player 2 wins!"
		sys.exit()

def noPiecesLeft(noPieces):
	noPieces.pop(0)
	if not noPieces:
		print "Piece has not been taken in 40 turns. It's a stalemate"
		sys.exit() 


board =[["      ","   1   ", "     2    ","    3    ","    4    ","   5   ", "      6   ","    7    ","    8    "],
			['----------------------------------------------------------------------------------'], 
		 	["   2 " , emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag()],
		 	['----------------------------------------------------------------------------------'], 
		 	["   4 " , hashtag(), emptySpace(), hashtag(), atsign(), hashtag(), emptySpace(), hashtag(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   6 " , emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag()],
		 	['----------------------------------------------------------------------------------'],
		 	["   8 " , emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   10 " , emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   12 " , atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   14 " , emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign()], 
		 	['----------------------------------------------------------------------------------'],
		 	["   16 " , atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace()]]

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
	    for row in board]))
def team1(board):
	print "team 1 turn"
	while True:

		while True:

			RowCoordinate = raw_input ("enter row number: ")
			try:
				RowCoordinateInt = int(RowCoordinate)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except ValueError:
				print "Please enter a number: "	
				continue
			if RowCoordinateInt not in [2, 4, 6, 8, 10, 12, 14, 16]:
				print "row coordinate out of range"
				continue 
			else:
				RowCoordinateInt = int(RowCoordinate)
				break

		while True:

			ColCoordinate = raw_input ("enter column number: ")
			try:
				ColCoordinateInt = int(ColCoordinate)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except ValueError:
				print "Please enter a number: "	
				continue
			if ColCoordinateInt not in [1, 2, 3, 4, 5, 6, 7, 8]:
				print "column coordinate out of range"
				continue
			else:
				ColCoordinateInt = int(ColCoordinate)
				break

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
			if RowDestinationInt not in [2, 4, 6, 8, 10, 12, 14, 16]:
				print "row coordinate out of range"
				continue 
			else:
				RowDestinationInt = int(RowDestination)
				break

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
			if ColDestinationInt not in [1, 2, 3, 4, 5, 6, 7, 8]:
				print "Column coordinate out of range"
				continue
			else:
				ColDestinationInt = int(ColDestination)
				break

		# Movement validations
		# 
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
			if RowDestinationInt >= RowCoordinateInt:
				print "Invalid move. Must move diagonally forward"
				continue
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
			if RowDestinationInt == RowCoordinateInt:
				print "Invalid move. Must move diagonally forward or backwards"
				continue
			
		if ColDestinationInt == ColCoordinateInt:
			print "Invalid move. Must move left or right"
			continue
			
		if type(board[RowDestinationInt][ColDestinationInt]) == type(hashtag()):
			print "Invalid move. Already a counter here"
			continue
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
			print "Invalid move. this is an enemy"
			continue
		if type(board[RowDestinationInt][ColDestinationInt]) == type(atsign()):
			print "Invalid move. Already a counter here"
			continue
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(emptySpace()):
			print "Invalid move. Can't move empty space"
			continue

		if RowCoordinateInt > 4:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
				if RowCoordinateInt > 4 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtag()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = atsign()
							hashPieceTaken(hashPieces, noPieces)
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
		
		if RowCoordinateInt > 4:
			print "1111"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
				print '5'
				if RowCoordinateInt > 4 and ColCoordinateInt < 7:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
						print '2'
						if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtag()):
							print "3"
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = atsign()
							hashPieceTaken(hashPieces, noPieces)
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
			
		"""print RowDestinationInt
		print ColDestinationInt
		if  RowDestinationInt == 2:
			print "lllll"
			board[RowDestinationInt][ColDestinationInt] = atsignKing()
			board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
			print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
			break"""
		
			
		if RowCoordinateInt > 4:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
				if RowCoordinateInt > 4 and ColCoordinateInt < 7 :	
					if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtagKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = atsignKing()
							hashPieceTaken(hashPieces, noPieces)
							acca = 0
							for i in range (8):
								if board[2][i] == type(atsign()):
									board[2][acca] = type(atsignKing())
								acca = acca + 1
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
			
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):		
				print "193"
				if RowCoordinateInt > 4 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = atsignKing()
							hashPieceTaken(hashPieces, noPieces)
							acca = 0
							for i in range (8):
								if board[2][i] == type(atsign()):
									board[2][acca] = type(atsignKing())
								acca = acca + 1
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
			
		if RowCoordinateInt < 14 and type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):		
			print "204"
			if RowCoordinateInt < 14 and ColCoordinateInt < 7:
				if type(board[RowCoordinateInt + 4][ColCoordinateInt + 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt + 2][ColCoordinateInt + 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = atsignKing()
						hashPieceTaken(hashPieces, noPieces)
						print "208"
						acca = 0
						for i in range (8):
							if board[2][i] == type(atsign()):
								board[2][acca] = type(atsignKing())
							acca = acca + 1
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
		
		
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
				if RowCoordinateInt < 14 and ColCoordinateInt > 2:		
					if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = atsignKing()
							hashPieceTaken(hashPieces, noPieces)
							print "219"
							acca = 0
							for i in range (8):
								if board[2][i] == type(atsign()):
									board[2][acca] = type(atsignKing())
								acca = acca + 1
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
		print
		if RowDestinationInt >= 2:
			print "1"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
				print "else1"
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = atsign()
				noPiecesLeft(noPieces)
				acca = 0
				for i in board[2]:
					if i == type(atsign()):
						board[2][acca] = atsignKing()
						print acca
					acca = acca + 1
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break
		
		if RowDestinationInt >= 2:
			print "2"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
				print "else"
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = atsignKing()
				noPiecesLeft(noPieces)
				acca = 0
				for i in range (8):
					if board[2][acca] == type(atsign()):
						board[2][acca] = type(atsignKing())
					acca = acca + 1
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break

def team2(board):
	print "team 2 turn"
	while True:

		while True:

			RowCoordinate = raw_input ("enter row number: ")
			try:
				RowCoordinateInt = int(RowCoordinate)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except (ValueError, IndexError):
				print "Please enter a number: "	
				continue
			except Error:
				continue
			if RowCoordinateInt not in [2, 4, 6, 8, 10, 12, 14, 16]:
				print "row coordinate out of range"
				continue 
			else:
				RowCoordinateInt = int(RowCoordinate)
				break

		while True:

			ColCoordinate = raw_input ("enter column number: ")
			try:
				ColCoordinateInt = int(ColCoordinate)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except (ValueError, IndexError):
				print "Please enter a number: "	
				continue
			except Error:
				continue
			if ColCoordinateInt not in [1, 2, 3, 4, 5, 6, 7, 8]:
				print " Column coordinate out of range"
				continue
			else:
				ColCoordinateInt = int(ColCoordinate)
				break

		while True:

			RowDestination = raw_input ("enter row number to move to: ")
			try:
				RowDestinationInt = int(RowDestination)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except (ValueError, IndexError):
				print "Please enter a number: "	
				continue
			except Error:
				continue
			if RowDestinationInt not in [2, 4, 6, 8, 10, 12, 14, 16]:
				print "row coordinate out of range"
				continue 
			else:
				RowDestinationInt = int(RowDestination)
				break

		while True:

			ColDestination = raw_input ("enter column number to move to: ")
			try:
				ColDestinationInt = int(ColDestination)
			except SyntaxError:
				print "Please enter a number: "	
				continue
			except (ValueError, IndexError):
				print "please enter a number: "	
				continue
			except Error:
				continue
				
			
			if ColDestinationInt not in [1, 2, 3, 4, 5, 6, 7, 8]:
				print "Column coordinate out of range"
			else:
				ColDestinationInt = int(ColDestination)
				break
		
		

		# Movement validations
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
			if RowDestinationInt <= RowCoordinateInt:
				print "Invalid move. Must move forward"
				continue
		
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):
			if RowDestinationInt == RowCoordinateInt:
				print "Invalid move. Must move diagonally forward or backwards"
				continue
				
		if ColDestinationInt == ColCoordinateInt:
			print "Invalid move. Must move left or right"
			continue
		if type(board[RowDestinationInt][ColDestinationInt]) == type(hashtag()):
			print "Invalid move. Already a counter here"
			continue
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(emptySpace()):
			print "Invalid move. Can't move empty space"
			continue
		if type(board[RowDestinationInt][ColDestinationInt]) == type(atsign()):
			print "Invalid move. Already a counter here"
			continue
		if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
			print "Invalid move. this is an enemy"
			continue
		

		if RowCoordinateInt < 14:
			print "H"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
				print "H"
				if RowCoordinateInt < 14 and ColCoordinateInt> 2:
					print "H"
					if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
						print "H"
						if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsign()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = hashtag()
							atPiecesTaken(atPieces, noPieces)
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
		
		if RowCoordinateInt > 4:
			print "1111"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
				print '11'
				if RowCoordinateInt < 14 and ColCoordinateInt < 7:
					if type(board[RowCoordinateInt + 4][ColCoordinateInt + 2]) == type(emptySpace()):
						print '2'
						if type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(atsign()):
							print "3"
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt + 2][ColCoordinateInt + 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = hashtag()
							hashPieceTaken(hashPieces, noPieces)
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
						
		if  RowDestinationInt == 16:
			board[RowDestinationInt][ColDestinationInt] = hashtagKing()
			board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
			print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
			break
		
		if RowCoordinateInt < 14:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):	
				if RowCoordinateInt < 14 and ColCoordinateInt < 7:
					if type(board[RowCoordinateInt + 4][ColCoordinateInt + 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(atsign()) or type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(atsignKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt + 2][ColCoordinateInt + 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = hashtagKing()
							atPiecesTaken(atPieces, noPieces)
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
			
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				print "193"
				if RowCoordinateInt < 14 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsign()) or type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsignKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = hashtagKing()
							atPiecesTaken(atPieces, noPieces)
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
						
		if RowCoordinateInt > 4:		
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				print "204"
				if RowCoordinateInt > 4 and ColCoordinateInt < 7:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(atsign()) or type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(atsignKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = hashtagKing()
							atPiecesTaken(atPieces, noPieces)
							print "208"
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
		
		
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				if RowCoordinateInt > 4 and ColCoordinateInt > 2:
					if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
						if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(atsign()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(atsignKing()):
							board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
							board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
							board[RowDestinationInt][ColDestinationInt] = hashtagKing()
							atPiecesTaken(atPieces, noPieces)
							print "219"
							print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
								for row in board]))
							break
						
		if RowDestinationInt < 16:
			print "1"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
				print "else"
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = hashtag()
				noPiecesLeft(noPieces)
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break
		
		
			
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):
				print "else"
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = hashtagKing()
				noPiecesLeft(noPieces)
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break

while True:
	team1(board)
	team2(board)
	
