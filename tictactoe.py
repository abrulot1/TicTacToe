from os import system, name	#to clear the console
from time import sleep #to pause screen before clearing


def get_player_char():
	"""	 Gets player input on which character they want

		Parameters: None
		Outputs: Character that the player chooses to be (upper case)
	"""
	valid_input = False
	choice = ''

	while not valid_input:
		choice = input('Player 1 are you "X" or "O": ')
		
		if choice.lower() == 'x' or choice.lower() == 'o':
			valid_input = True
		else:
			print("You must be 'X' or 'O', please try again")
	return choice.upper()


def get_user_choice(player, board):
	""" Gets player's input for the next move and checks if it is a valid move,
				will also update the board with the current player's choice

		Parameters: player = Character representing which player is making the move choice
				board = list containing the items representing the current game board
		Outputs: An updated list showing the board state
	"""
	valid_input = False

	while not valid_input: 
		choice = input(f"Player {player} what position will you play (enter 1-9): ")

		if not choice.isdigit():
			print("Your choice is not a number, please try again\n")

		if choice.isdigit():
			if int(choice) in range(1,10):
				if board[int(choice) - 1] == 'X' or board[int(choice) - 1] == 'O':
					print("The square you chose is taken, please try again\n")
				else:
					update_board(player, int(choice), board)
					valid_input = True
			else:
				print("Your choice is not in range 1-9, please try again\n")
	return board


def draw_board(board):
	"""	Used display the current game state on the screen

		Parameters: board = list containing the items representing the current game board
		Outputs: None 
	"""
	print("\n\n\n\n\t " + board[0] + " | " + board[1] + " | " + board[2])
	print("\t" + "-----------")
	print("\t " + board[3] + " | " + board[4] + " | " + board[5])
	print("\t" + "-----------")
	print("\t " + board[6] + " | " + board[7] + " | " + board[8] + "\n")

	
def update_board(player, selection, board):
	"""Puts the current player's character in chosen spot on the board

		Parameters: player = character representing the current player, X or O
					selection = integer containing the current player's choice
					board = list containing the items representing the current game board
		Outputs: Returns an updated list representing the current board with moves
	"""
	board[selection - 1] = player
	return board


def win_conditions(board, player):
	""" Checks whether or not a player has won the game

		Parameters: board = represents current plays made by the users
					player = stores character whose current move is being checked
		Outputs: Boolean representing whether or not a player has won.
	"""
	if(board[0] == board[1] == board[2] == player or
		board[3] == board[4] == board[5] == player or
		board[6] == board[7] == board[8] == player or
		board[0] == board[3] == board[6] == player or
		board[1] == board[4] == board[7] == player or
		board[2] == board[5] == board[8] == player or
		board[0] == board[4] == board[8] == player or
		board[2] == board[4] == board[6] == player
		): 
		system('cls' if name == 'nt' else 'clear')
		draw_board(board)
		print(f"\nCongratulations player {player}, you've won!\n")
		sleep(3)
		return True
	else:
		return False


def play_another():
	"""Gets user input about playing another game

		Parameters: None
		Outputs: Boolean representing player choice
	"""
	valid_choice = False

	while not valid_choice:
		choice = input("\nDo you want to play again? (Y or N): ")
		
		if choice.upper() == 'Y':
			return True
		elif choice.upper() == 'N':
			return False
		else:
			print("\nPlease input 'Y' or 'N'")


def play_game(board, player1, player2):
	"""	Function where most of the game logic resides

		Parameters: board = list of player moves
					player1 = contains the player's character choice X or O
					player2 = contains the player's character choice X or O
		Outputs: None
	"""
	won = False
	player_moves = []	

	#clear the screen of previous output
	system('cls' if name == 'nt' else 'clear')

	while not won:
		draw_board(board)
		if len(player_moves) == 0:
			if player1 == 'X':
				board = get_user_choice(player1, board)
				player_moves.append(player1)
			else:
				board = get_user_choice(player2, board)
				player_moves.append(player2)
		elif player_moves[-1] == 'O':
			if player1 == 'X':
				board = get_user_choice(player1, board)
				player_moves.append(player1)
				if len(player_moves) >= 5:
					won = win_conditions(board, player1)
			else:
				board = get_user_choice(player2, board)
				player_moves.append(player2)
				if len(player_moves) >= 5:
					won = win_conditions(board, player2)
		elif player_moves[-1] == 'X':
			if player1 == 'O':
				board = get_user_choice(player1, board)
				player_moves.append(player1)
				if len(player_moves) >= 5:
					won = win_conditions(board, player1)
			else:
				board = get_user_choice(player2, board)
				player_moves.append(player2)
				if len(player_moves) >= 5:
					won = win_conditions(board, player2)
			
		if(len(player_moves) == 9 and not won):
			system('cls' if name == 'nt' else 'clear')
			draw_board(board)
			print("\nIt's a draw, no winners here.\n")
			break
		
		#clear the screen of previous output
		system('cls' if name == 'nt' else 'clear')


def main():
	play_again = True	

	print("\nWelcome to the Tic Tac Toe board!\n")

	while play_again:
		moves = ["1", "2", "3", "4", "5", "6", "7" , "8", "9"]
		player1 = ""
		player2 = ""

		#Assign player roles (X or O)
		player1 = get_player_char()
		if player1 == 'X':
			player2 = 'O'
		else:
			player2 = 'X'

		#run game logic
		play_game(moves, player1, player2)
		play_again = play_another()

	print("Thank you for being here, goodbye!\n")


if __name__ == "__main__":
	main()

