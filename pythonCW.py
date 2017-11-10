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



board =[["      ","   1   ", "     2    ","    3    ","    4    ","   5   ", "      6   ","    7    ","    8    "],
			['----------------------------------------------------------------------------------'], 
		 	["   2 " , emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag()],
		 	['----------------------------------------------------------------------------------'], 
		 	["   4 " , hashtag(), atsign(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   6 " , atsign(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag()],
		 	['----------------------------------------------------------------------------------'],
		 	["   8 " , emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   10 " , emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), hashtag(), emptySpace(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   12 " , atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   14 " , hashtag(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign()], 
		 	['----------------------------------------------------------------------------------'],
		 	["   16 " , atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace()]]

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
	    for row in board]))
def team1(board):

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
			else:
				ColDestinationInt = int(ColDestination)
				break

		# Movement validations
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
		


		if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
			if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtag()):
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = atsign()
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				print board[RowDestinationInt - 2][ColDestinationInt - 1]
				print RowDestinationInt
				print ColDestinationInt
				break
		if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
			if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtag()):
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = atsign()
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break
		
		if  RowDestinationInt == 2:
			board[RowDestinationInt][ColDestinationInt] = atsignKing()
			board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
			#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
			 #   for row in board]))
	        #break

		else:
			print "else"
			board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
			board[RowDestinationInt][ColDestinationInt] = atsign()
			
	        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
			    for row in board]))
	        break

def team2(board):
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
			else:
				ColDestinationInt = int(ColDestination)
				break

		# Movement validations
		if RowDestinationInt == RowCoordinateInt:
			print "Invalid move. Must move forward"
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


		if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
			if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(atsign()):
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = hashtag()
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				print '1'
				print board[RowDestinationInt - 2][ColDestinationInt - 1]
				print RowDestinationInt
				print ColDestinationInt
				break
		if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
			print "sss"
			if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(atsign()):
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = hashtag()
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				print "2"
				break
		
		if  RowDestinationInt == 16:
			board[RowDestinationInt][ColDestinationInt] = hashtagKing()
			board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
		

		else:
			print "else"
			board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
			board[RowDestinationInt][ColDestinationInt] = atsign()
			
	        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
			    for row in board]))
	        break
while True:
	team1(board)
	team2(board)
	break
