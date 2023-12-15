def user_input():
    global turn, user_entry
    acceptable_values = [1, 2, 3]
#CHECKS WHICH PLAYER PLAYS SO THE INPUT GETS CUSTOMIZED FOR THE PLAYER
    if turn % 2 == 0:
        line = input('Player X, choose a line (1, 2, 3): ')
        column = input('Player X, choose a column(1, 2, 3): ')
    else:
        line = input('Player O, choose a line (1, 2, 3): ')
        column = input('Player O, choose a column (1, 2, 3): ')
#CHECK IF INPUT IS A POSITIVE DIGIT BETWEEN 1 AND 3
    if line.isdigit() and column.isdigit():
        if int(line) in acceptable_values and int(column) in acceptable_values:
            user_entry = [int(line),int(column)]
            tictactoe()
#IF THE INPUT IS A DIGIT BUT NOT BETWEEN 1 AND 3
        else:
            print("Sorry! The number needs to be 1, 2 or 3. Please try again")
            user_input()
#IF THE INPUT IS NOT A DIGIT
    else:
        print("Sorry! The input needs to be a number between 1 and 3. Please try again")
        user_input()

#GLOBAL VARIABLES
user_entry = []
turn = 0
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def pass_turn():
    global turn
    turn +=1
    game_table()
    user_input()

def tictactoe():
    global turn, row1, row2, row3

    if user_entry[0] == 1:
        if user_entry[1] == 1:
            if row1[0] == ' ':
                if turn % 2 == 0:
                    row1[0] = 'X'
                    win_check()
                else:
                    row1[0] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

        elif user_entry[1] == 2:
            if row1[1] == ' ':
                if turn % 2 == 0:
                    row1[1] = 'X'
                    win_check()
                else:
                    row1[1] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

        elif user_entry[1] == 3:
            if row1[2] == ' ':
                if turn % 2 == 0:
                    row1[2] = 'X'
                    win_check()
                else:
                    row1[2] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

    elif user_entry[0] == 2:
        if user_entry[1] == 1:
            if row2[0] == ' ':
                if turn % 2 == 0:
                    row2[0] = 'X'
                    win_check()
                else:
                    row2[0] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

        elif user_entry[1] == 2:
            if row2[1] == ' ':
                if turn % 2 == 0:
                    row2[1] = 'X'
                    win_check()
                else:
                    row2[1] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

        elif user_entry[1] == 3:
            if row2[2] == ' ':
                if turn % 2 == 0:
                    row2[2] = 'X'
                    win_check()
                else:
                    row2[2] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

    elif user_entry[0] == 3:
        if user_entry[1] == 1:
            if row3[0] == ' ':
                if turn % 2 == 0:
                    row3[0] = 'X'
                    win_check()
                else:
                    row3[0] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

        elif user_entry[1] == 2:
            if row3[1] == ' ':
                if turn % 2 == 0:
                    row3[1] = 'X'
                    win_check()
                else:
                    row3[1] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

        elif user_entry[1] == 3:
            if row3[2] == ' ':
                if turn % 2 == 0:
                    row3[2] = 'X'
                    win_check()
                else:
                    row3[2] = 'O'
                    win_check()
            else:
                print('Sorry! Someone already played on that spot, try again.')
                user_input()

def win_check():
    global row1, row2, row3
    if turn==8:
        game_table()
        print('DRAW')
        replay()
    #CHECK IF PLAYER X OR PLAYER O WON IN LINES
    elif row1 == ['X', 'X', 'X'] or row2 == ['X', 'X', 'X'] or row3 == ['X', 'X', 'X']:
        print('Congratulations player X, You won TicTacToe!')
        replay()
    elif row1 == ['O', 'O', 'O'] or row2 == ['O', 'O', 'O'] or row3 == ['O', 'O', 'O']:
        print('Congratulations player O, You won TicTacToe!')
        replay()

    #CHECK IF PLAYER X OR PLAYER O WON IN COLUMNS
    elif row1[0] == row2[0] == row3[0] == 'X' or row1[1] == row2[1] == row3[1] == 'X' or row1[2] == row2[2] == row3[2] == 'X':
        print('Congratulations player X, You won TicTacToe!')
        replay()
    elif row1[0] == row2[0] == row3[0] == 'O' or row1[1] == row2[1] == row3[1] == 'O' or row1[2] == row2[2] == row3[2] == 'O':
        print('Congratulations player O, You won TicTacToe!')
        replay()

    #CHECK IF PLAYER X OR PLAYER O WON IN DIAGONALS
    elif row1[0] == row2[1] == row3[2] == 'X' or row1[2] == row2[1] == row3[0] == 'X':
        print('Congratulations player X, You won TicTacToe!')
        replay()
    elif row1[0] == row2[1] == row3[2] == 'O' or row1[2] == row2[1] == row3[0] == 'O':
        print('Congratulations player O, You won TicTacToe!')
        replay()
    #IF NO ONE WON YET
    else:
        pass_turn()

def game_table():
    global row1, row2, row3, turn
    print(f'Turn: {turn}')
    print(row1)
    print(row2)
    print(row3)

def replay():
    global row1, row2, row3, turn
    x = input('Do you wish to play again? Type Y if yes or just type anything for no. : ')
    if x == 'Y' or x == 'y':
        turn = 0
        row1 = [' ', ' ', ' ']
        row2 = [' ', ' ', ' ']
        row3 = [' ', ' ', ' ']
        game_table()
        user_input()
    else:
        pass

game_table()
user_input()
