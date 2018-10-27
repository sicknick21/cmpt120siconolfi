# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Nicholas Siconolfi
# Created: 2018-10-23


import random

def printBoard(board):
    # This function prints out the board and the rows.
    # print the top border
    # for each row in the board...
    # print the row
    # print the next border    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('+-----------+')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('+-----------+')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('+-----------+')

def inputSymbol():
    # Lets the player type which symbol they want to be.
    letter = ''
    while not (letter == 'x' or letter == 'o'):
        print('Do you want to be x or o?')
        letter = input().lower()
    if letter == 'x':
        return ['x', 'o']
    else:
        return ['o', 'x']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'playertwo'
    else:
        return 'player'

def playAgain():
    # This function sees if the player wants to play again.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def markBoard(board, letter, move):
    # check to see whether the desired square is blank
    board[move] = letter

def isWinner(bo, le):
    #This function determines on how to be the winner of the game.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):
    # This function makes a copy of the board for the next game.
    copyBoard = []

    for i in board:
        copyBoard.append(i)

    return copyBoard

def isSpaceFree(board, move):
    # This function determines which space is free.
    return board[move] == ' '

def getPlayerMove(board):
    # This function lets the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getPlayerTwoMove(board, secondplayer):
    # This function lets the second player type in his move.
    if secondplayer == 'x':
        Symbol  = 'o'
    else:
        Symbol = 'x'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            markBoard(copy, secondplayer, i)
            if isWinner(copy, secondplayer):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            markBoard(copy, Symbol, i)
            if isWinner(copy, Symbol):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Tic Tac Toe Lab')

while True:
    theBoard = [' '] * 10
    Symbol, secondplayer = inputSymbol()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            printBoard(theBoard)
            move = getPlayerMove(theBoard)
            markBoard(theBoard, Symbol, move)

            if isWinner(theBoard, Symbol):
                printBoard(theBoard)
                print('You have won!')
                gameIsPlaying = False
            else:
                if hasBlanks(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'playertwo'

        else:
            # Player two's turn.
            move = getPlayerTwoMove(theBoard, secondplayer)
            markBoard(theBoard, secondplayer, move)

            if isWinner(theBoard, secondplayer):
                printBoard(theBoard)
                print('You lost.')
                gameIsPlaying = False
            else:
                if hasBlanks(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
