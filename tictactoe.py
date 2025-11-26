# fron random import randrange



########################################################################################################
# Create a game of tictactoe
# computer starts in the middle
# User must enter in the number of the square they choose between 1-10, can't overlap 
# 4 possible outcomes : continue, tie. user wins or computer wins
# must display board
#######################################################################################################


# def enter_move(board):
#     try:
#         user_choice = int(input("Please select the number you'll like to place the 'O' "))
#     except:
#         user_choice = int(input("Please try again. Enter in your move"))
#     # checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.


# while continue_game:
#     user_choice = int(input("Please select the number you'll like to place the 'O' "))
#     if user_choice in nums:
#         print(user_choice)
#     else:
#         nums.append(user_choice)


display_board(board)