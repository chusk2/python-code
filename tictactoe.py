### Imports
from guizero import App, PushButton, Box, Text
from random import choice

### Functions ------------
def initial_player() :
    """Choose randomly a first turn"""
    first_player = choice(['X','0'])
    return first_player
    

def change_player() :
    # allow function to change player's value
    global player

    if player == 'X' :
        player = '0'
    else :
        player = 'X'
    current_player.value = f'Now it is the turn of player: {player}'

def clean_board() :
    """Create a clean board of buttons"""
    for y in range(3) :
        for x in range(3) :
            button = PushButton(board, grid=[x,y], text ='', width = 5, height=4,
                    command = chosen_box, args=[x,y])
            buttons_grid[x][y] = button

def disable_buttons() :
    # disable all buttons if there is a winner
    for y in range(3) :
        for x in range(3) :
            buttons_grid[x][y].disable()

def check_winner() :
    #Check for three in a row or a column or a diagonal
    
    ## check rows
    for y in range(3) :
        
        # first owner of the cell
        # check if it contains some text
        winner = buttons_grid[0][y].text
        if winner == '' : continue
                    
        # start counting wins for winner
        wins = 0
        for x in range(3) :
            
            # owner of the current cell
            owner = buttons_grid[x][y].text
                        
            if owner != '' and owner == winner :
                    wins += 1
            else :
                break
        
        if wins == 3 :
            disable_buttons()
            show_winner.value = f'Player {winner} won the game!'
            win = True
            return win
    
    ## check columns
    
    for x in range(3) :
        # first owner of the cell
        # check if it contains some text
        winner = buttons_grid[x][0].text
        # if empty, continue with next row
        if winner == '' : continue
        # start counting wins for winner
        wins = 0
        for y in range(3) :
            # owner of the current cell
            owner = buttons_grid[x][y].text
            
            if owner != '' and owner == winner :
                wins += 1
            else :
                break
        if wins == 3 :
            disable_buttons()
            show_winner.value = f'Player {winner} won the game!'
            win = True
            return win

    ## check diagonal from left to right
    
    # first owner of the cell
    # check if it contains some text
    winner = buttons_grid[0][0].text
    if winner != '' : 
        #start checking for diagonal
        
        wins = 0
        for x,y in zip(range(3),range(3)) :
            # owner of the current cell
            owner = buttons_grid[x][y].text
            
            if owner != '' and owner == winner :
                wins += 1
            # stop because one cell was empty
            else :
                break
        if wins == 3 :
            disable_buttons()
            show_winner.value = f'Player {winner} won the game!'
            win = True
            return win
    
             
    ## check diagonal from right to left
   
    # first owner of the cell
    # check if it contains some text
    winner = buttons_grid[2][2].text
    if winner != '' :
        #start checking for diagonal
        wins = 0
        inverse_range = range(2,-1,-1) # range(start,stop,step)
        # create tuples of coordinates: (0,0) , (1,1) and (2,2)
        reversed_coordinates = [(i,j) for i,j in zip(inverse_range,inverse_range)]
        for x,y in reversed_coordinates :
            # owner of the current cell
            owner = buttons_grid[x][y].text
            
            if owner != '' and owner == winner :
                wins += 1
            # stop because one cell was empty
            else :
                break
    if wins == 3 :
        disable_buttons()
        show_winner.value = f'Player {winner} won the game!'
        win = True
        return win

def chosen_box(x,y) :
    # make possible function changes player value
    
    global player
    global buttons_grid
    global moves
    # make function displays player on button
    buttons_grid[x][y].text = player
    # disable the button so it cannot be selected again
    buttons_grid[x][y].disable()
    
    
    moves += 1
    # start checking for a winner if at least
    # three turns have been reached
    if moves >= 3 :
        check_winner()
    if moves == 9 and not win :
        show_winner.value = 'It\'s a draw game!'
    change_player()


### Actual program
app = App()
title = Text(app,text='Tic Tac Toe Game', color = 'blue')
current_player = Text(app,text = '')
show_winner = Text(app,text='')
moves = 0
win = False
# choose who's first turn
player = initial_player()
current_player.value = f'Player: {player} starts the game.'
board = Box(app,layout = 'grid', border = 2)
buttons_grid = [ [None, None, None],
                [None, None, None],
                [None, None, None] ]
clean_board()

app.display()
