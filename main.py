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

human = 'x'
computer = 'o'

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


def ai_turn():
    best_score = -999
    best_move = []
    for n in range(0, 3):
        for m in range(0, 3):
            if board[n][m].text == '':
                board[n][m].set_text('x')
                score = minimax(board, 0, False)
                print("Score is: ", score)
                board[n][m].set_text('')  # Undo the previous move
                if score > best_score:
                    best_score = score
                    best_move = (n, m)
    board[best_move[0]][best_move[1]].set_text('o')


def minimax(table, depth, is_minimizing):
    scores = {'o': -10 - depth, 'x': 10 - depth, 'draw': 0 - depth}
    if check_win() is not None:
        score = scores[check_win()]
        return score
    if is_minimizing:
        best_score = -999
        for index_1 in range(0, 3):
            for index_2 in range(0, 3):
                if table[index_1][index_2].text == '':
                    table[index_1][index_2].set_text('x')
                    score = minimax(table, depth + 1, False)
                    table[index_1][index_2].set_text('')
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 999
        for index_1 in range(0, 3):
            for index_2 in range(0, 3):
                if table[index_1][index_2].text == '':
                    table[index_1][index_2].set_text('o')
                    score = minimax(table, depth + 1, True)
                    table[index_1][index_2].set_text('')
                    best_score = min(score, best_score)
        return best_score


def random_computer():
    a = free_squares()
    if len(a) > 0:
        r = random.randrange(0, len(a))
        board[a[r][0]][a[r][1]].set_text('o')


def check_win():
    for row in range(0, 3):
        if board[row][0].text == board[row][1].text == board[row][2].text and board[row][0].text != '':
            winner = board[row][0].text
            return winner
    for col in range(0, 3):
        if board[0][col].text == board[1][col].text == board[2][col].text and board[0][col].text != '':
            winner = board[0][col].text
            return winner
    if board[0][0].text == board[1][1].text == board[2][2].text and board[0][0].text != '':
        winner = board[0][0].text
        return winner
    if board[0][2].text == board[1][1].text == board[2][0].text and board[0][2].text != '':
        winner = board[0][2].text
        return winner
    if len(free_squares()) == 0:
        return 'draw'


def free_squares():
    global board
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


def reset():
    for location in range(0, 3):
        for place in board[location]:
            place.set_text('')


while is_running:
    screen.blit(background, (0, 0))
    time_delta = clock.tick(5) / 1000.0
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                for i in range(0, 3):
                    for button in board[i]:

                        if event.ui_element == button and button.text == '':

                            button.set_text("x")
                            ai_turn()
                            if check_win() is not None:
                                print(check_win())

        manager.process_events(event)
    manager.update(time_delta)
    drawline()
    manager.draw_ui(screen)
    pygame.display.update()
