theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def displayBoard():
    print('-------------------------')
    print('|' + '\t' + '1 :' + '\t' + '\t' + '|' + '\t' + '2' + '\t' + '\t' + '|' + '\t' + '3' + '\t' + '\t' + '|')
    print('-------------------------')
    print('|' + '\t' + '4' + '\t' + '\t' + '|' + '\t' + '5' + '\t' + '\t' + '|' + '\t' + '6' + '\t' + '\t' + '|')
    print('-------------------------')
    print('|' + '\t' + '7' + '\t' + '\t' + '|' + '\t' + '8' + '\t' + '\t' + '|' + '\t' + '9' + '\t' + '\t' + '|')
    print('-------------------------')


def printBoard(board):
    print('--+--+--+--+')
    print('|' + '\t' + '1 :' + board['1'] + '\t' + '|' + '\t' + '2 :' + board['2'] + '\t' + '|' + '\t' + '3 :' + board[
        '3'] + '\t' + '|')
    print('--+--+--+--+')
    print('|' + '\t' + '4 :' + board['4'] + '\t' + '|' + '\t' + '5 :' + board['5'] + '\t' + '|' + '\t' + '6 :' + board[
        '6'] + '\t' + '|')
    print('--+--+--+--+')
    print('|' + '\t' + '7 :' + board['7'] + '\t' + '|' + '\t' + '8 :' + board['8'] + '\t' + '|' + '\t' + '9 :' + board[
        '9'] + '\t' + '|')
    print('--+--+--+--+')

player1 = 0
player2 = 0

def showingwinner(winnerturn, playerx, playero, startagaingame):
    print("\nGame Over.\n")
    print(" ** " + winnerturn + " won. **")
    if winnerturn == 'X':
        global player1
        player1 += 10
        print("Player " + winnerturn + " gets " + str(player1) + " points")
        startagaingame += 1
    if winnerturn == 'O':
        global player2
        player2 += 10
        print("Player " + winnerturn + " gets " + str(player2) + " points")
        startagaingame += 1
def drawgame(drawpoints):
    global player2
    player2 += 10 + drawpoints
    global player1
    player1 += 10 + drawpoints
def playagain():
    print("Do want to play Again?(y/n)")
    again = input()
    if again == 'Y' or again == 'y':
        theBoard['1']=  ' '
        theBoard['2'] = ' '
        theBoard['3'] = ' '
        theBoard['4'] = ' '
        theBoard['5'] = ' '
        theBoard['6'] = ' '
        theBoard['7'] = ' '
        theBoard['8'] = ' '
        theBoard['9'] = ' '
        game()
    else:
        quit()

# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0
    drawgamepoints = 5
    startagain = 0
    for i in range(17):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")
        move = input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count <= 8:

            if(theBoard['1'] == theBoard['2'] == theBoard['3'] != ' '):    # across the top
                printBoard(theBoard)
                showingwinner(turn, player2, player1,startagain)
                break
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                showingwinner(turn, player2, player1,startagain)
                break
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the bottom
                printBoard(theBoard)
                showingwinner(turn, player2, player1,startagain)
                break
            if theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                showingwinner(turn, player2, player1,startagain)
                break
            if theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                showingwinner(turn, player2, player1,startagain)
                break
            if theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                showingwinner(turn, player2, player1,startagain)
                break
            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                showingwinner(turn, player2, player1,startagain)
                break
            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                showingwinner(turn, player2, player1,startagain)
                break
        #if(i==3):
           # print("game end")
            #playagain()
                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            drawgame(drawgamepoints)
        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
            # Now we will ask if player wants to restart the game or not.
    playagain()
game()