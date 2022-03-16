import pygame
from pygame.constants import K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_BACKSPACE, K_DELETE, K_DOWN, K_LEFT, \
    K_RIGHT, K_UP

import createBoard
import function as func
from buttons import Button
from cells import Cell


def showPuzzle(screen, level, cells):
    running = True
    if not cells:
        board = createBoard.createANewBoard(cells)
        puzzle = createBoard.createPuzzle(cells, level)
        cells[0].level = level

    level = cells[0].level

    related_color = (60, 204, 250)
    Yellow2 = (252, 247, 204)
    Black = (0, 0, 0)

    button_color = (156, 243, 255)
    clicked_color = (184, 246, 255)
    hover_color = (75, 255, 255)
    chosenColor = (189, 240, 255)
    rects = []

    func.drawBoard(screen, cells, rects, Black)
    func.printNumberToBoard(cells, screen, Black)

    topBoard = cells[0].top
    leftBoard = cells[0].left
    rightBoard = cells[80].right
    bottomBoard = cells[80].bottom

    buttons = []

    for x in range(1, 10):
        if x <= 3:
            btn = Button(880 + 120 * x, 250, 100, 100, str(x), 80, Black, button_color, clicked_color, hover_color)
            btn.number = x
            buttons.append(btn)
        if 3 < x <= 6:
            btn = Button(880 + 120 * (x - 3), 370, 100, 100, str(x), 80, Black, button_color, clicked_color,
                         hover_color)
            btn.number = x
            buttons.append(btn)
        if x > 6:
            btn = Button(880 + 120 * (x - 6), 490, 100, 100, str(x), 80, Black, button_color, clicked_color,
                         hover_color)
            btn.number = x
            buttons.append(btn)

    exit_button = Button(1100, 800, 200, 50, "Exit", 30, Black, button_color, clicked_color, hover_color)

    func.text_to_screen(screen, "Difficulty: ", 80, 20,
                        30, Black, 'freesansbold.ttf')
    func.text_to_screen(screen, level, 250, 20, 30, Black, 'freesansbold.ttf')

    func.text_to_screen(screen, "Time ", 500, 20, 30, Black, 'freesansbold.ttf')

    chosen_cell = Cell(10, 10, 100, 100)
    chosen_cell.puzzleNumber = 0

    func.indicate_related_number_cell(chosen_cell, cells)
    func.print_board(cells, screen, chosen_cell,
                     chosenColor, Yellow2, related_color)

    erase_button = Button(1120, 130, 100, 100, "", 1, Black, button_color, clicked_color, hover_color)
    pencil_button = Button(1000, 130, 100, 100, "", 1, Black, button_color, clicked_color, hover_color)
    hint_button = Button(1240, 130, 100, 100, "", 1, Black, button_color, clicked_color, hover_color)

    pencil_img = pygame.image.load('pencil.png')
    hint_img = pygame.image.load('hint.png')

    erase_image = pygame.image.load("erase.png")

    pencil_mode = False
    func.text_to_screen(screen, "Off", 1030, 130, 20, Black, 'freesansbold.ttf')

    current_time = int(pygame.time.get_ticks() / 1000)
    check_finish_time = True

    while running:

        tick = int(pygame.time.get_ticks() / 1000)

        if tick == current_time + 1:
            current_time += 1
            if check_finish_time:
                cells[0].time += 1

        second = cells[0].time % 60
        min = int(cells[0].time / 60)

        str_second = str(second)
        str_min = str(min)
        if second < 10:
            str_second = "0" + str_second
        if min < 10:
            str_min = "0" + str_min

        pygame.draw.rect(screen, Yellow2, (600, 20, 300, 50))

        func.text_to_screen(screen, str_min, 590, 20, 30, Black, 'freesansbold.ttf')
        func.text_to_screen(screen, ":", 640, 20, 30, Black, 'freesansbold.ttf')
        func.text_to_screen(screen, str_second, 660, 20, 30, Black, 'freesansbold.ttf')

        if pencil_mode:
            str_pencil_mode = "On"
        else:
            str_pencil_mode = "Off"

        if pencil_button.drawButton(screen):
            pencil_mode = not pencil_mode

            pygame.draw.rect(screen, Yellow2, (1030, 110, 30, 10))
        func.text_to_screen(screen, str_pencil_mode, 1040, 130, 20, Black, 'freesansbold.ttf')
        screen.blit(pencil_img, (1025, 155))

        if chosen_cell.puzzleNumber == 0:
            if erase_button.drawButton(screen):
                for cell in cells:
                    if cell.ordinalnumber == chosen_cell.ordinalnumber and cell.number != cell.entered:
                        cell.entered = 0
                        cell.wrong = 0
                        func.input_number(cell, cells, 0, chosen_cell, screen, chosenColor, Yellow2, related_color)

            screen.blit(erase_image, (1135, 150))

            if hint_button.drawButton(screen):
                for cell in cells:
                    if cell.ordinalnumber == chosen_cell.ordinalnumber:
                        func.input_number(cell, cells, cell.number, chosen_cell, screen, chosenColor, Yellow2,
                                          related_color)
            screen.blit(hint_img, (1260, 150))

            for btn in buttons:
                if btn.drawButton(screen):
                    for cell in cells:
                        if cell.ordinalnumber == chosen_cell.ordinalnumber and cell.entered != cell.number:
                            if not pencil_mode:
                                func.input_number(cell, cells, btn.number, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, btn.number, screen, chosenColor, Yellow2,
                                                  related_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                screen.fill(Yellow2)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()

                if leftBoard <= x <= rightBoard and topBoard <= y and y <= bottomBoard:
                    for cell in cells:
                        if cell.left <= x <= cell.right and y >= cell.top and y <= cell.bottom:
                            cell.chosen = True
                            chosen_cell = cell
                        else:
                            cell.chosen = False

                else:
                    if not (1000 <= x <= 1340 and y >= 100 and 610 >= y):
                        for cell in cells:
                            cell.chosen = False
                            chosen_cell = Cell(10, 10, 100, 100)
                            chosen_cell.puzzleNumber = 100

                func.indicate_related_number_cell(chosen_cell, cells)
                func.print_board(cells, screen, chosen_cell,
                                 chosenColor, Yellow2, related_color)

            if event.type == pygame.KEYDOWN:
                for cell in cells:
                    if cell.adjust and cell.chosen:
                        if event.key == K_1:
                            if not pencil_mode:
                                func.input_number(cell, cells, 1, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 1, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_2:
                            if not pencil_mode:
                                func.input_number(cell, cells, 2, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 2, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_3:
                            if not pencil_mode:
                                func.input_number(cell, cells, 3, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 3, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_4:
                            if not pencil_mode:
                                func.input_number(cell, cells, 4, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 4, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_5:
                            if not pencil_mode:
                                func.input_number(cell, cells, 5, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 5, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_6:
                            if not pencil_mode:
                                func.input_number(cell, cells, 6, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 6, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_7:
                            if not pencil_mode:
                                func.input_number(cell, cells, 7, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 7, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_8:
                            if not pencil_mode:
                                func.input_number(cell, cells, 8, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 8, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_9:
                            if not pencil_mode:
                                func.input_number(cell, cells, 9, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                            if pencil_mode:
                                func.pencil_input(cells, cell, chosen_cell, 9, screen, chosenColor, Yellow2,
                                                  related_color)
                            break
                        if event.key == K_DELETE or event.key == K_BACKSPACE:
                            if chosen_cell.entered != chosen_cell.number:
                                cell.entered = 0
                                cell.wrong = 0
                                func.input_number(cell, cells, 0, chosen_cell, screen, chosenColor, Yellow2,
                                                  related_color)
                                break

                if event.key == K_RIGHT:
                    for cell in cells:
                        if cell.ordinalnumber == chosen_cell.ordinalnumber:
                            cell.chosen = 0

                    for cell in cells:
                        if chosen_cell.column == 9 and cell.column == 1 and cell.row == chosen_cell.row:
                            cell.chosen = 1
                            chosen_cell = cell
                            break
                        if cell.row == chosen_cell.row and cell.column == (chosen_cell.column + 1):
                            cell.chosen = 1
                            chosen_cell = cell
                            break
                    func.indicate_related_number_cell(chosen_cell, cells)
                    func.print_board(cells, screen, chosen_cell,
                                     chosenColor, Yellow2, related_color)

                if event.key == K_LEFT:
                    for cell in cells:
                        if cell.ordinalnumber == chosen_cell.ordinalnumber:
                            cell.chosen = 0

                    for cell in cells:
                        if chosen_cell.column == 1 and cell.column == 9 and cell.row == chosen_cell.row:
                            cell.chosen = 1
                            chosen_cell = cell
                            break
                        if cell.row == chosen_cell.row and cell.column == (chosen_cell.column - 1):
                            cell.chosen = 1
                            chosen_cell = cell
                            break
                    func.indicate_related_number_cell(chosen_cell, cells)
                    func.print_board(cells, screen, chosen_cell,
                                     chosenColor, Yellow2, related_color)

                if event.key == K_DOWN:
                    for cell in cells:
                        if cell.ordinalnumber == chosen_cell.ordinalnumber:
                            cell.chosen = 0

                    for cell in cells:
                        if chosen_cell.row == 9 and cell.row == 1 and cell.column == chosen_cell.column:
                            cell.chosen = 1
                            chosen_cell = cell
                            break
                        if cell.row == (chosen_cell.row + 1) and cell.column == chosen_cell.column:
                            cell.chosen = 1
                            chosen_cell = cell
                            break
                    func.indicate_related_number_cell(chosen_cell, cells)
                    func.print_board(cells, screen, chosen_cell,
                                     chosenColor, Yellow2, related_color)

                if event.key == K_UP:
                    for cell in cells:
                        if cell.ordinalnumber == chosen_cell.ordinalnumber:
                            cell.chosen = 0

                    for cell in cells:
                        if chosen_cell.row == 1 and cell.row == 9 and cell.column == chosen_cell.column:
                            cell.chosen = 1
                            chosen_cell = cell
                            break
                        if cell.row == (chosen_cell.row - 1) and cell.column == chosen_cell.column:
                            cell.chosen = 1
                            chosen_cell = cell
                            break

                    func.indicate_related_number_cell(chosen_cell, cells)
                    func.print_board(cells, screen, chosen_cell,
                                     chosenColor, Yellow2, related_color)

        check = True
        for cell in cells:
            if cell.puzzleNumber == 0:
                if cell.entered != cell.number:
                    check = False
                    break
        if check:
            check_finish_time = False
            func.text_to_screen(screen, "Finish !!!", 1100, 700, 50, (17, 0, 189), 'freesansbold.ttf')

        if exit_button.drawButton(screen):
            running = False
            screen.fill(Yellow2)

        pygame.display.flip()
