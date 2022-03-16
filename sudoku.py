import puzzle
import pygame
from buttons import Button
import function as func

pygame.init()

running = True
screen = pygame.display.set_mode((1500, 900))
pygame.display.set_caption('Sudoku')
White = (255, 255, 255)
Yellow = (252, 247, 204)
Black = (0, 0, 0)
Blue = (17, 0, 189)
button_color = (156, 243, 255)
clicked_color = (184, 246, 255)
hover_color = (75, 255, 255)

screen.fill(Yellow)

start_button = Button(500, 400, 400, 50, "Start new game", 30, White, button_color, clicked_color, hover_color)
resume_button = Button(500, 500, 400, 50, "Resume game", 30, White, button_color, clicked_color, hover_color)
easy_button = Button(500, 300, 400, 50, "Easy", 30, Black, button_color, clicked_color, hover_color)
medium_button = Button(500, 400, 400, 50, "Medium", 30, Black, button_color, clicked_color, hover_color)
hard_button = Button(500, 500, 400, 50, "Hard", 30, Black, button_color, clicked_color, hover_color)
expert_button = Button(500, 600, 400, 50, "Expert", 30, Black, button_color, clicked_color, hover_color)

func.text_to_screen(screen, "Sudoku", 600, 200, 50, Blue, 'freesansbold.ttf')
func.text_to_screen(screen, "Developed by Khanh D Tran",
                    570, 750, 20, Blue, 'freesansbold.ttf')
check = True

new_cells = []
recent_cells = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if check:
        if start_button.drawButton(screen):
            screen.fill(Yellow)
            start_button.hide_button(screen)
            func.text_to_screen(screen, "Difficulty", 590,
                                200, 50, Blue, 'freesansbold.ttf')
            resume_button.enable = False
            check = False

    if recent_cells:
        if resume_button.drawButton(screen):
            screen.fill(Yellow)
            puzzle.showPuzzle(screen, "", recent_cells)
            check = True
            func.text_to_screen(screen, "Sudoku", 600, 200,
                                50, Blue, 'freesansbold.ttf')
            func.text_to_screen(screen, "Developed by Khanh D Tran",
                                570, 750, 20, Blue, 'freesansbold.ttf')
            resume_button.enable = True

    if not check:
        if easy_button.drawButton(screen):
            screen.fill(Yellow)
            puzzle.showPuzzle(screen, "Easy", new_cells)
            check = True
            func.text_to_screen(screen, "Sudoku", 600, 200,
                                50, Blue, 'freesansbold.ttf')
            func.text_to_screen(screen, "Developed by Khanh D Tran",
                                570, 750, 20, Blue, 'freesansbold.ttf')
            resume_button.enable = True
    if not check:
        if medium_button.drawButton(screen):
            screen.fill(Yellow)
            puzzle.showPuzzle(screen, "Medium", new_cells)
            check = True
            func.text_to_screen(screen, "Sudoku", 600, 200,
                                50, Blue, 'freesansbold.ttf')
            func.text_to_screen(screen, "Developed by Khanh D Tran",
                                570, 750, 20, Blue, 'freesansbold.ttf')
            resume_button.enable = True
    if not check:
        if hard_button.drawButton(screen):
            screen.fill(Yellow)
            puzzle.showPuzzle(screen, "Hard", new_cells)
            check = True
            func.text_to_screen(screen, "Sudoku", 600, 200,
                                50, Blue, 'freesansbold.ttf')
            func.text_to_screen(screen, "Developed by Khanh D Tran",
                                570, 750, 20, Blue, 'freesansbold.ttf')
            resume_button.enable = True
    if not check:
        if expert_button.drawButton(screen):
            screen.fill(Yellow)
            puzzle.showPuzzle(screen, "Expert", new_cells)
            check = True
            func.text_to_screen(screen, "Sudoku", 600, 200,
                                50, Blue, 'freesansbold.ttf')
            func.text_to_screen(screen, "Developed by Khanh D Tran",
                                570, 750, 20, Blue, 'freesansbold.ttf')
            resume_button.enable = True

    if new_cells:
        recent_cells = new_cells
        new_cells = []

    pygame.display.flip()

pygame.quit()
