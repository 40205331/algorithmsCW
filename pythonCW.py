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
		 	["   4 " , hashtag(), atsign(), hashtag(), hashtag(), hashtag(), emptySpace(), hashtag(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   6 " , atsign(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag(), emptySpace(), hashtag()],
		 	['----------------------------------------------------------------------------------'],
		 	["   8 " , emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   10 " , emptySpace(), emptySpace(), emptySpace(), emptySpace(), emptySpace(), hashtag(), emptySpace(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   12 " , atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace(), atsign(), emptySpace()],
		 	['----------------------------------------------------------------------------------'],
		 	["   14 " , hashtag(), atsign(), atsignKing(), atsign(), emptySpace(), atsign(), emptySpace(), atsign()], 
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
			if RowCoordinateInt not in ["2", "4", "6", "8", "10", "12", "14", "16"]:
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
			if ColCoordinateInt not in ["1", "2", "3", "4", "5", "6", "7",]:
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
			if RowDestinationInt not in ["2", "4", "6", "8", "10", "12", "14", "16"]:
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
				if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtag()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = atsign()
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
						
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
				if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtag()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = atsign()
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
			
		print RowDestinationInt
		print ColDestinationInt
		if  RowDestinationInt == 2:
			print "lllll"
			board[RowDestinationInt][ColDestinationInt] = atsignKing()
			board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
			print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
			break
			
		if RowCoordinateInt > 4:
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):	
				if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(hashtagKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = atsignKing()
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
			
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):		
				print "193"
				if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = atsignKing()
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
			
		if RowCoordinateInt < 14:		
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):		
				print "204"
				if type(board[RowCoordinateInt + 4][ColCoordinateInt + 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt + 2][ColCoordinateInt + 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = atsignKing()
						print "208"
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
		
		
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):		
				if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(hashtag()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(hashtagKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = atsignKing()
						print "219"
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
		
		if RowDestinationInt > 2:
			print "1"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsign()):
				print "else"
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = atsign()
		
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break
		
		if RowDestinationInt > 2:
			print "2"
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(atsignKing()):
				print "else"
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = atsignKing()
		
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
			except ValueError:
				print "Please enter a number: "	
				continue
			if RowCoordinateInt not in ["2", "4", "6", "8", "10", "12", "14", "16"]:
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
			if RowDestinationInt not in ["2", "4", "6", "8", "10", "12", "14", "16"]:
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
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
				if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsign()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = hashtag()
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
						
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtag()):
				if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(atsign()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = hashtag()
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
				if type(board[RowCoordinateInt + 4][ColCoordinateInt + 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(atsign()) or type(board[RowCoordinateInt + 2][ColCoordinateInt + 1]) == type(atsignKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt + 2][ColCoordinateInt + 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = hashtagKing()
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
			
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				print "193"
				if type(board[RowCoordinateInt + 4][ColCoordinateInt - 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsign()) or type(board[RowCoordinateInt + 2][ColCoordinateInt - 1]) == type(atsignKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt + 2][ColCoordinateInt - 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = hashtagKing()
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
						
		if RowCoordinateInt > 4:		
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				print "204"
				if type(board[RowCoordinateInt - 4][ColCoordinateInt + 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(atsign()) or type(board[RowCoordinateInt - 2][ColCoordinateInt + 1]) == type(atsignKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt - 2][ColCoordinateInt + 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = hashtagKing()
						print "208"
						print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
							for row in board]))
						break
		
		
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):		
				if type(board[RowCoordinateInt - 4][ColCoordinateInt - 2]) == type(emptySpace()):
					if type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(atsign()) or type(board[RowCoordinateInt - 2][ColCoordinateInt - 1]) == type(atsignKing()):
						board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
						board[RowCoordinateInt - 2][ColCoordinateInt - 1] = emptySpace()
						board[RowDestinationInt][ColDestinationInt] = hashtagKing()
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
		
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break
		
		
			
			if type(board[RowCoordinateInt][ColCoordinateInt]) == type(hashtagKing()):
				print "else"
				board[RowCoordinateInt][ColCoordinateInt] = emptySpace()
				board[RowDestinationInt][ColDestinationInt] = hashtagKing()
		
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
					for row in board]))
				break

while True:
	team1(board)
	team2(board)
	
