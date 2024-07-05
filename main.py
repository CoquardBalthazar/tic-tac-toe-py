from functions import *

while True :
    # SET THE GAME
    gameboard = [" "," "," "," "," "," "," "," "," "," "]
    indexboard = ['0','1','2','3','4','5','6','7','8','9']
    player1_marker, player2_marker = marker_player()
    turn = play_first()
    print(turn + ' will go first.')

    # SET Game On
    ready = input('Are you ready to start the game (YES or NO) : ').upper()

    if ready == 'YES' or ready[0]=='y'.upper():
        game_on = True
    else :
        game_on= False
    
    
    # GAME IS ON - while it is on, the loop continue
    while game_on :
        
        if turn == 'Player 1':
            ## 1-DISPLAY BOARD
            display_board(gameboard)
            
            print('^State of the game^')
            
            display_board(indexboard)
            print('^ Here is the position board ^')
            
            print( '\n'*3 )
            
            ## 2-CHOICE POSITION
            print(f"{turn}, it is time to play !")
            position = next_position(gameboard)
            
            ## 3-ASSIGN MARKER TO BOARD
            assign_marker(gameboard, position, player1_marker)
            
            ## 4-CHECK IF WIN
            if check_win(gameboard, player1_marker) :
                display_board(gameboard)
                print(f"{turn} you won the game !! Félicitations :D")
                game_on = False
            
            ##5-CHECK IF TIE
            else: 
                if check_tie(gameboard):
                    display_board(gameboard)
                    print('Its a draw! Félicitations to both players')
                    game_on = False
                    break
                else:
                    turn = 'Player 2' 
        else:
            ## 1-DISPLAY BOARD
            display_board(gameboard)
            
            print('^State of the game^')
            
            display_board(indexboard)
            print('^ Here is the position board ^')
            
            print( '\n'*3 )
            
            ## 2-CHOICE POSITION
            print(f"{turn}, it is time to play !")
            position = next_position(gameboard)
            
            ## 3-ASSIGN MARKER TO BOARD
            assign_marker(gameboard, position, player2_marker)
            
            ## 4-CHECK IF WIN
            if check_win(gameboard, player2_marker) :
                display_board(gameboard)
                print(f"{turn} you won the game !! Félicitations :D")
                game_on = False
            
            ##5-CHECK IF TIE
            else: 
                if check_tie(gameboard):
                    display_board(gameboard)
                    print('Its a draw! Félicitations to both players')
                    game_on = False
                    break
                else:
                    turn = 'Player 1' 
                    
    # GAME IS OFF - IF GAMEON IS FALSE, ASK IF WANTS TO REPLAY:
    if not replay():
        break
