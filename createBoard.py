from cells import Cell
import random
import function as func

cells = []


def createANewBoard(cells):
    board = []
    cardinalnumber = 0
    # create a blank board
    for row in range(1, 10):
        for column in range(1, 10):
            ancell = Cell(row, column, cardinalnumber, 0)
            ancell.x = 80 * column
            ancell.y = 80 * row
            if row <= 3 and column <= 3:
                ancell.block = 1
            if row <= 3 and column > 3 and column <= 6:
                ancell.block = 2
            if row <= 3 and column > 6:
                ancell.block = 3
            if row > 3 and row <= 6 and column <= 3:
                ancell.block = 4
            if row > 3 and row <= 6 and column > 3 and column <= 6:
                ancell.block = 5
            if row > 3 and row <= 6 and column > 6:
                ancell.block = 6
            if row > 6 and column <= 3:
                ancell.block = 7
            if row > 6 and column > 3 and column <= 6:
                ancell.block = 8
            if row > 6 and column > 6:
                ancell.block = 9

            cells.append(ancell)
            cardinalnumber += 1

    # Create a board

    while cells[80].number == 0:
        for cell in cells:
            if cell.number == 0:
                cell.potential = func.potentialList(cell, cells)
                if len(cell.potential) == 0:
                    x = cell.ordinalnumber
                    cells[x].potential = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    cells[x].eleminate = []
                    cells[x - 1].potential.remove(cells[x - 1].number)
                    cells[x - 1].number = 0
                    break

                if cell.number == 0:
                    cell.number = random.choice(cell.potential)
    board = func.createBoard(cells)
    return board


def createPuzzle(cells, level):
    # show a puzzle

    if level == "Easy":
        numberClues = random.choice(range(36, 47))
    elif level == "Medium":
        numberClues = random.choice(range(32, 36))
    elif level == "Hard":
        numberClues = random.choice(range(28, 32))
    elif level == "Expert":
        numberClues = random.choice(range(17, 28))

    chosenNumbers = random.sample(range(0, 80), numberClues)

    for chosen in chosenNumbers:
        for cell in cells:
            if chosen == cell.ordinalnumber:
                cells[chosen].puzzleNumber = cells[chosen].number
                cells[chosen].adjust = False
                cells[chosen].pencil = False
                break

    puzzle = func.createPuzzleBoard(cells)

    return puzzle
