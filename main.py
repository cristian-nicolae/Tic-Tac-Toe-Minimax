import pygame
import pygame_gui
import random

pygame.init()
pygame.display.set_caption('Tic Tac Toe')

# Global variables
width = 600
height = 600
XO = 'x'
clock = pygame.time.Clock()
is_running = True
line_color = "black"
winner = None
draw = None

screen = pygame.display.set_mode((width, height))
background = pygame.Surface((width, height))
background.fill(pygame.Color('Grey'))

manager = pygame_gui.UIManager((width, height))

# First row
button1_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 0, 0), (200, 200)),
                                         text='',
                                         manager=manager)
button1_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 1, 0), (200, 200)),
                                         text='',
                                         manager=manager)
button1_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 2, 0), (200, 200)),
                                         text='',
                                         manager=manager)
# Second row
button2_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 0, 200), (200, 200)),
                                         text='',
                                         manager=manager)
button2_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 1, 200), (200, 200)),
                                         text='',
                                         manager=manager)
button2_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 2, 200), (200, 200)),
                                         text='',
                                         manager=manager)
# Third row
button3_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 0, 400), (200, 200)),
                                         text='',
                                         manager=manager)
button3_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 1, 400), (200, 200)),
                                         text='',
                                         manager=manager)
button3_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200 * 2, 400), (200, 200)),
                                         text='',
                                         manager=manager)
board = [[button1_1, button1_2, button1_3], [button2_1, button2_2, button2_3], [button3_1, button3_2, button3_3]]


def random_computer():
    a = free_squares()
    r = random.randrange(0, len(a))
    board[a[r][0]][a[r][1]].set_text('o')


def check_win():
    global board, winner, draw
    for row in range(0, 3):
        if board[row][0].text == board[row][1].text == board[row][2].text and board[row][0].text != '':
            print("Winner is " + board[row][0].text)
            break
    for col in range(0, 3):
        if board[0][col].text == board[1][col].text == board[2][col].text and board[0][col].text != '':
            print("Winner is " + board[col][0].text)
            break
    if board[0][0].text == board[1][1].text == board[2][2].text and board[0][0].text != '':
        print("Winner is " + board[0][0].text)
    if board[0][2].text == board[1][1].text == board[2][0].text and board[0][2].text != '':
        print("Winner is " + board[0][2].text)


def free_squares():
    free_spaces = []
    for a in range(0, 3):
        for b in range(0, 3):
            if board[a][b].text == '':
                couple = (a, b)
                free_spaces.append(couple)
    return free_spaces


def draw_xo(row, col):
    global board, XO
    if XO == 'x':
        board[row - 1][col - 1].set_text("x")
        XO = 'o'

    else:
        board[row - 1][col - 1].set_text("o")
        XO = 'x'
    pygame.display.update()


def drawline():
    pygame.display.update()
    pygame.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pygame.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    # drawing horizontal lines
    pygame.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pygame.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)


while is_running:
    screen.blit(background, (0, 0))
    time_delta = clock.tick(10) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                for i in range(0, 3):
                    for button in board[i]:
                        if event.ui_element == button and button.text == '':
                            button.set_text("x")
                            random_computer()
                            check_win()
                            print(free_squares())

        manager.process_events(event)
    manager.update(time_delta)
    drawline()
    manager.draw_ui(screen)
    pygame.display.update()
