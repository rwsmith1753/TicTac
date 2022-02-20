
import string
import os
from subprocess import call

#clear screen
_ = call('clear' if os.name == 'posix' else 'cls')

#empty variables for board
grid = {'A1':' ','B1':' ','C1':' ','A2':' ','B2':' ','C2':' ','A3':' ','B3':' ','C3':' '}

#reset game parameters
turns = 0
win_game = False

#introduction
print('Welcome to Tic Tac Toe!\n\nPlayer One will be X\nPlayer Two will be O')
print('To place your piece, enter the column letter followed by the row number')
print('Example: A1, or a1')
print('Player One, you go first.')

#game cycle
while win_game == False:
    #loop through X and O turns
    piece = ''
    if turns % 2 == 0:
        piece = 'X'
        turns += 1
    else:
        piece = 'O'
        turns += 1

    #function for displaying board with each move
    def print_board():
        global grid
        
        header = '   A     B     C   \n'
        row1 = f'     |     |     \n1  {grid["A1"]}  |  {grid["B1"]}  |  {grid["C1"]}  \n _____|_____|_____\n'
        row2 = f'     |     |     \n2  {grid["A2"]}  |  {grid["B2"]}  |  {grid["C2"]}  \n _____|_____|_____\n'
        row3 = f'     |     |     \n3  {grid["A3"]}  |  {grid["B3"]}  |  {grid["C3"]}  \n      |     |     '

        print(header, row1, row2, row3)


    print_board()

    #player move
    move = input(f'{piece}: ')

    #match input to grid format
    move = move.capitalize()

    while move not in grid.keys() or grid[move] != ' ':
        print('Invalid Move')
        move = input(f'{piece}: ')
        move = move.capitalize()

        

    #add move to board
    grid.update({move:piece})
    #clear screen and print current board
    _ = call('clear' if os.name == 'posix' else 'cls')


    #winning scenarios. Will compare with each move. Game over if match. Keep playing until match.
    if grid['A1'] == grid["B1"] == grid["C1"] and grid['A1'] != ' ':
        print_board()
        print(f'{piece} Wins!!')
        win_game = True
    elif grid["A2"] == grid["B2"] == grid["C2"] and grid["A2"] != ' ':
        print_board()
        print(f'{piece} Wins!!')
        win_game = True
    elif grid["A3"] == grid["B3"] == grid["C3"] and grid["A3"] != ' ':
        print_board()
        print(f'{piece} Wins!!')
        win_game = True 
    elif grid['A1'] == grid["A2"] == grid["A3"] and grid['A1'] != ' ':
        print_board()
        print(f'{piece} Wins!!')
        win_game = True
    elif grid["B1"] == grid["B2"] == grid["B3"] and grid["B1"] != ' ':
        print_board()
        print(f'{piece} Wins!!')
        win_game = True
    elif grid["C1"] == grid["C2"] == grid["C3"] and grid["C1"] != ' ':
        print_board()
        print(f'{piece} Wins!!')
        win_game = True
    elif grid['A1'] == grid["B2"] == grid["C3"] and grid['A1'] != ' ':
        print_board()
        print(f'{piece} Wins!!')
        win_game = True 
    elif grid["A3"] == grid["B2"] == grid["C1"] and grid["A3"] != ' ':
        print_board()
        print(f'{piece} Wins!!')
        win_game = True
    else:
        pass
    
    #draw scenario
    spaces_left = list(filter(lambda space: space if grid[space] == ' ' else '', grid))
    if len(spaces_left) == 0:
        print('Cat Game!!!')
        print_board()
        break
    else:
        pass
