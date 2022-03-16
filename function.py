
import pygame

Black = (0, 0, 0)
Blue = (5, 83, 171)
White = (247, 245, 230)
related_color = (252, 251, 230)
Red1 = (176, 4, 4)
Red2 = (255, 189, 189)

def potentialList(Cell, cells):
    for cell in cells:
        if cell.row == Cell.row and cell.column != Cell.column:
            for number in Cell.potential:
                if cell.number == number:
                    Cell.potential.remove(number)
        if cell.column == Cell.column and cell.row != Cell.row:
            for number in Cell.potential:
                if cell.number == number:
                    Cell.potential.remove(number)
        if cell.block == Cell.block and (cell.column != Cell.column or cell.row != Cell.row):
            for number in Cell.potential:
                if cell.number == number:
                    Cell.potential.remove(number)

    for eli in Cell.eliminate:
        for num in Cell.potential:
            if eli == num:
                Cell.potential.remove(num)

    return Cell.potential

def createBoard(cells):
    board = []

    for r in range(1, 10):
        row = []
        for cell in cells:
            if cell.row == r:
                row.append(cell.number)

        board.append(row)
    return board

def createPuzzleBoard(cells):
    board = []

    for r in range(1, 10):
        row = []
        for cell in cells:
            if cell.row == r:
                row.append(cell.puzzleNumber)

        board.append(row)
    return board

def showBoard(board, cells):
    print("--------------------------------------------")
    for row in board:
        print(row)
    print("--------------------------------------------")

def text_to_screen(screen, text, x, y, size, color, fonttype):

    text = str(text)
    font = pygame.font.Font(fonttype, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def printNumberToBoard(cells, screen, Black):
    for cell in cells:
        if cell.puzzleNumber != 0:
            text_to_screen(screen, cell.puzzleNumber, cell.centerx - 10,
                           cell.centery - 13, 30, Black, 'freesansbold.ttf')
        if cell.entered != 0:
            text_to_screen(screen, cell.entered, cell.centerx -
                           10, cell.centery - 13, 30, Blue, 'freesansbold.ttf')

def drawBoard(screen, cells, rects, Black):
    for cell in cells:
        rect = pygame.Rect((cell.x, cell.y, 80, 80))
        pygame.draw.rect(screen, (60, 64, 59), rect, 1)
        cell.centerx = rect.centerx
        cell.centery = rect.centery
        cell.center = rect.center
        cell.left = rect.left
        cell.right = rect.right
        cell.top = rect.top
        cell.bottom = rect.bottom

        rects.append(rect)

    for col in range(0, 11):
        if col % 3 == 1:
            pygame.draw.line(screen, (60, 64, 59),
                             (col * 80, 80), (col * 80, 800), 6)

    for row in range(0, 11):
        if row % 3 == 1:
            pygame.draw.line(screen, Black, (80, row * 80), (800, row * 80), 6)

def drawLines(screen, Black):
    for col in range(0, 11):
        if col % 3 == 1:
            pygame.draw.line(screen, (60, 64, 59),
                             (col * 80, 80), (col * 80, 800), 6)

    for row in range(0, 11):
        if row % 3 == 1:
            pygame.draw.line(screen, Black, (80, row * 80), (800, row * 80), 6)

def printCellNumber(cell, screen, rectColor, textColor, text):
    chosenCell = pygame.Rect(cell.left + 1, cell.top + 1, 78, 78)
    pygame.draw.rect(screen, rectColor, chosenCell)
    drawLines(screen, Black)
    text_to_screen(screen, text, cell.centerx - 10,
                   cell.centery - 13, 30, textColor, 'freesansbold.ttf')

def indicate_related_number_cell(chosen_cell, cells):
    if chosen_cell.puzzleNumber != 0:
        for cell in cells:
            if cell.ordinalnumber != chosen_cell.ordinalnumber:
                if cell.number != chosen_cell.number:
                    cell.related_number = 0
                else:
                    if cell.puzzleNumber == 0 and cell.entered == 0:
                        cell.related_number = 0
                    else:
                        cell.related_number = 1
    else:
        if chosen_cell.entered != 0:
            for cell in cells:
                if cell.ordinalnumber != chosen_cell.ordinalnumber:
                    if cell.number != chosen_cell.entered:
                        cell.related_number = 0
                    else:
                        if cell.puzzleNumber == 0 and cell.entered == 0:
                            cell.related_number = 0
                        else:
                            cell.related_number = 1
        if chosen_cell.entered == 0:
            for cell in cells:
                cell.related_number = 0

def indicate_wrong_cell(cell, cells, number):

    if number == 0:
        for cellx in cells:
            if cellx.related_wrong == 1:
                cellx.related_wrong = 0
    else:
        if not cell.wrong:
            if cell.number != number:
                for cellx in cells:
                    if cellx.row == cell.row or cellx.column == cell.column or cellx.block == cell.block:
                        if cellx.ordinalnumber != cell.ordinalnumber and cellx.number == number and \
                                (cellx.puzzleNumber != 0 or cellx.entered == cellx.number):
                            cellx.related_wrong = 1
                if number == 0:
                    cell.wrong = 0
                else:
                    cell.wrong = 1
        else:
            if cell.number == number:
                for cellx in cells:
                    if cellx.related_wrong != 0 and cellx.ordinalnumber != cell.ordinalnumber and (
                            cellx.row == cell.row or cellx.column == cell.column or cellx.block == cell.block):
                        cellx.related_wrong = 0
                cell.wrong = 0
            else:
                for cellx in cells:
                    if cellx.related_wrong != 0 and cellx.ordinalnumber != cell.ordinalnumber and cellx.number == cell.entered and (
                            cellx.row == cell.row or cellx.column == cell.column or cellx.block == cell.block):
                        cellx.related_wrong = 0
                    if cellx.row == cell.row or cellx.column == cell.column or cellx.block == cell.block:
                        if cellx.ordinalnumber != cell.ordinalnumber and cellx.number == number:
                            if cellx.puzzleNumber != 0 or cellx.entered == cellx.number:
                                cellx.related_wrong = 1
                if number == 0:
                    cell.wrong = 0
                else:
                    cell.wrong = 1
    cell.entered = number


def indicate_related_pencil_cell(cells, cell, number, pencil_number):
    for cellx in cells:
        if cellx.row == cell.row or cellx.column == cell.column or cellx.block == cell.block:
            if cellx.puzzleNumber == number or (cellx.entered == cellx.number and cellx.number == number):
                cellx.related_pencil = True
                if number in pencil_number:
                    pencil_number.remove(number)


def print_board(cells, screen, chosen_cell, chosenColor, Yellow2, related_number_color):
    for cell in cells:
        if cell.chosen:
            text = ""
            if cell.puzzleNumber == 0:
                if cell.entered == 0:
                    printCellNumber(
                        cell, screen, chosenColor, Blue, text)
                else:
                    printCellNumber(
                        cell, screen, chosenColor, Blue, cell.entered)
            if cell.puzzleNumber != 0:
                printCellNumber(
                    cell, screen, chosenColor, Black, cell.number)

        if not cell.chosen:
            if cell.row == chosen_cell.row or cell.column == chosen_cell.column or cell.block == chosen_cell.block:
                if cell.puzzleNumber == 0:
                    if cell.entered == 0:
                        printCellNumber(
                            cell, screen, related_color, Black, "")
                    else:
                        printCellNumber(
                            cell, screen, related_color, Blue, cell.entered)
                if cell.puzzleNumber != 0:
                    printCellNumber(
                        cell, screen, related_color, Black, cell.number)
            else:
                if cell.puzzleNumber == 0:
                    if cell.entered == 0:
                        printCellNumber(
                            cell, screen, Yellow2, Black, "")
                    else:
                        printCellNumber(
                            cell, screen, Yellow2, Blue, cell.entered)
                if cell.puzzleNumber != 0:
                    printCellNumber(
                        cell, screen, Yellow2, Black, cell.number)

        if chosen_cell.puzzleNumber != 0 and cell.ordinalnumber != chosen_cell.ordinalnumber:
            if cell.puzzleNumber != 0 and cell.number == chosen_cell.entered:
                printCellNumber(cell, screen, chosenColor, Black, cell.number)

        if cell.related_number:
            if cell.puzzleNumber != 0:
                printCellNumber(
                    cell, screen, related_number_color, Black, cell.number)
            else:
                printCellNumber(
                    cell, screen, related_number_color, Blue, cell.entered)

        if cell.wrong:
            if cell.chosen:
                printCellNumber(cell, screen, chosenColor, Red1, cell.entered)
            else:
                printCellNumber(cell, screen, Red2, Red1, cell.entered)

        if cell.related_wrong != 0:
            if cell.entered == 0:
                printCellNumber(cell, screen, Red2, Black, cell.number)
            else:
                printCellNumber(cell, screen, Red2, Blue, cell.number)

        if cell.pencil:
            for x in cell.pencil_number:
                if x == chosen_cell.puzzleNumber or x == chosen_cell.entered:
                    if x <= 3:
                        text_to_screen(screen, str(x), cell.left + 10 + 25 * (x - 1), cell.top + 10, 15, Blue,
                                       'freesansbold.ttf')
                    if x <= 6 and x > 3:
                        text_to_screen(screen, str(x), cell.left + 10 + 25 * (x - 4), cell.top + 32, 15, Blue,
                                       'freesansbold.ttf')
                    if x <= 9 and x > 6:
                        text_to_screen(screen, str(x), cell.left + 10 + 25 * (x - 7), cell.top + 54, 15, Blue,
                                       'freesansbold.ttf')
                else:
                    if x <= 3:
                        text_to_screen(screen, str(x), cell.left + 10 + 25 * (x - 1), cell.top + 10, 15, (78, 94, 83),
                                       'freesansbold.ttf')
                    if x <= 6 and x > 3:
                        text_to_screen(screen, str(x), cell.left + 10 + 25 * (x - 4), cell.top + 32, 15, (78, 94, 83),
                                       'freesansbold.ttf')
                    if x <= 9 and x > 6:
                        text_to_screen(screen, str(x), cell.left + 10 + 25 * (x - 7), cell.top + 54, 15, (78, 94, 83),
                                       'freesansbold.ttf')

        if cell.related_pencil:
            printCellNumber(cell, screen, (137, 161, 143), Black, cell.number)

            cell.related_pencil = False


def pencil_input(cells, cell, chosen_cell, number, screen, chosenColor, Yellow2, related_number_color):
    if number in cell.pencil_number:
        cell.pencil_number.remove(number)
    else:
        cell.pencil_number.append(number)

    indicate_related_pencil_cell(cells, cell, number, cell.pencil_number)

    print_board(cells, screen, chosen_cell, chosenColor, Yellow2, related_number_color)


def input_number(cell, cells, number, chosen_cell, screen, chosenColor, Yellow2, related_color):
    if number != 0:
        cell.pencil = False
    else:
        cell.pencil = True
    cell.pencil_number = []

    remove_related_pencil_number(cell, cells, number)
    indicate_wrong_cell(cell, cells, number)
    indicate_related_number_cell(
        chosen_cell, cells)
    print_board(
        cells, screen, chosen_cell, chosenColor, Yellow2, related_color)


def remove_related_pencil_number(cell, cells, number):
    for cellx in cells:
        if cellx.row == cell.row or cellx.column == cell.column or cellx.block == cell.block:
            if number == cell.number and number in cellx.pencil_number:
                cellx.pencil_number.remove(number)
