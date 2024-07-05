#FUNC 0 : clear display
def clear_display():
    print('\n' * 5)

#FUNC 1 : displays the board (board as a list)
def display_board(board):
    #Clear Output
    clear_display()
    
    print(board[1]+ '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])


# FUNC 2 : get the player input, and assigns a marker to each player. Return a tupple of the markers for each player
def marker_player():
    marker = ''
    
    while marker != "X" and marker !="O":
        marker = input('Player1, please choose a marker between "X" and "O" : ').upper()
    
    if marker == "X":
        return ('X', 'O')
    else:
        return ('O', 'X')
    

#FUNC 3 : randomly returns which player starts first
def play_first():
    from random import randint
    
    if randint(0,1) == 0:
        return 'Player 1'
    else :
        return 'Player 2'

# FUNC 5 checks if the position choosen by the player is free on the board
def position_free (board, position):
    return board[position] == ' '

# FUNC 4 get the input, and returns the position chosen by the player to play next move. Use the func display to display an indexboard
def next_position(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not position_free(board, position):
        position = int(input('ased on this indexboard, please choose a position to play next (1-9),  : '))
        
    return position


# FUNC 6 Assign if free : assign the marker of the player if position_free is TRUE :
def assign_marker(board, position, marker):
    board[position] = marker


def check_win(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or #accross the top
            (board[4] == board[5] == board[6] == marker) or #accross the middle
            (board[7] == board[8] == board[9] == marker) or #accross the bottom
            (board[1] == board[4] == board[7] == marker) or #down left side 
            (board[2] == board[5] == board[8] == marker) or #down middle
            (board[3] == board[6] == board[9] == marker) or # down right side
            (board[3] == board[5] == board[7] == marker) or # diagonale uprigth down left
            (board[1] == board[5] == board[9] == marker)) # diagonale upleft down right

# FUNC 8 Test if there is a TIE == the board is full :
def check_tie(board):
    for i in range(1,10):
        if position_free(board, i):
            return False
    return True
  

# FUNC 9 Replay : a function that ask the player if he wants to replay and return True if yes:
def replay() :
    toreplay = ''
    
    while toreplay != 'YES' and toreplay != 'NO':
        toreplay = input('Do you want to replay (YES or NO) : ').upper()
    
    if toreplay == 'YES':
        return True
    else:
        return False
