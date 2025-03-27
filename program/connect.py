import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows, cols = 6, 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ")
    for x in range(rows):
        print("   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] in ["🔵", "🔴"]:
                print("", gameBoard[x][y], end=" |")
            else:
                print("  ", end=" |")
        print()
    print("   +----+----+----+----+----+----+----+")

def getLowestEmptyRow(col):
    for row in range(rows-1, -1, -1):
        if gameBoard[row][col] == "":
            return row
    return -1

def modifyTurn(spacePicked, turn):
    row, col = spacePicked
    gameBoard[row][col] = turn

def checkWin(player):
    # Check horizontal
    for r in range(rows):
        for c in range(cols - 3):
            if all(gameBoard[r][c + i] == player for i in range(4)):
                return True

    # Check vertical
    for r in range(rows - 3):
        for c in range(cols):
            if all(gameBoard[r + i][c] == player for i in range(4)):
                return True

    # Check diagonal (\)
    for r in range(rows - 3):
        for c in range(cols - 3):
            if all(gameBoard[r + i][c + i] == player for i in range(4)):
                return True

    # Check diagonal (/)
    for r in range(3, rows):
        for c in range(cols - 3):
            if all(gameBoard[r - i][c + i] == player for i in range(4)):
                return True

    return False

turnCounter = 0
players = ["🔵", "🔴"]

while True:
    printGameBoard()
    currentPlayer = players[turnCounter % 2]

    # Get valid move
    while True:
        move = input(f"Player {currentPlayer}, choose a column (A-G): ").upper()
        if move in possibleLetters:
            col = possibleLetters.index(move)
            row = getLowestEmptyRow(col)
            if row != -1:
                break
            else:
                print("Column is full. Try another.")
        else:
            print("Invalid input. Choose a column from A to G.")

    modifyTurn((row, col), currentPlayer)

    # Check for a win
    if checkWin(currentPlayer):
        printGameBoard()
        print(f"Player {currentPlayer} wins!")
        break

    # Check for draw
    if all(gameBoard[0][c] != "" for c in range(cols)):
        printGameBoard()
        print("It's a draw!")
        break

    turnCounter += 1
