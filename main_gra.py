import pygame
import sys
import time
import logging
from logic import check_win, is_board_full
from minimax import evaluate, minimax, find_best_move, ai_move 



open('logi.log', 'w').close()
logging.basicConfig(
    filename='logi.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


pygame.init()
WIDTH, HEIGHT = 600, 700
ROWS, COLS = 3, 3
SQSIZE = WIDTH // COLS
BOTTOM_PANEL = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kółko i Krzyżyk")


WHITE = (255, 255, 255)
BG_COLOR = (30, 30, 30)
LINE_COLOR = (70, 70, 70)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (200, 50, 50)
BUTTON_COLOR = (50, 150, 50)
TEXT_COLOR = (255, 255, 255)
TURN_COLOR = (180, 180, 180)

FONT = pygame.font.SysFont("arial", 40)
SMALL_FONT = pygame.font.SysFont("arial", 28)
BIG_FONT = pygame.font.SysFont("arial", 55)


board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
vs_ai = False
start_time = 0
game_over = False
player = 1

def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}m {seconds}s"



def draw_lines():
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQSIZE), (WIDTH, i * SQSIZE), 5)
        pygame.draw.line(screen, LINE_COLOR, (i * SQSIZE, 0), (i * SQSIZE, WIDTH), 5)

def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * SQSIZE + SQSIZE // 2
            y = row * SQSIZE + SQSIZE // 2
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), SQSIZE // 3, 10)
            elif board[row][col] == 2:
                offset = 40
                pygame.draw.line(screen, CROSS_COLOR, (col * SQSIZE + offset, row * SQSIZE + offset),
                                 (col * SQSIZE + SQSIZE - offset, row * SQSIZE + SQSIZE - offset), 12)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQSIZE + offset, row * SQSIZE + SQSIZE - offset),
                                 (col * SQSIZE + SQSIZE - offset, row * SQSIZE + offset), 12)

def draw_winner(player):
    text = FONT.render(f"Gracz {player} wygrywa!", True, TEXT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - BOTTOM_PANEL + 25))
    duration = format_time(time.time() - start_time)
    logging.info(f"Gracz {player} wygrał! Czas gry: {duration}")

def draw_tie():
    text = FONT.render("Remis!", True, TEXT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - BOTTOM_PANEL + 25))
    duration = format_time(time.time() - start_time)
    logging.info(f"Remis! Czas gry: {duration}")

def draw_turn(player):
    symbol = 'O' if player == 1 else 'X'
    text = SMALL_FONT.render(f"Tura: Gracz {player} ('{symbol}')", True, TURN_COLOR)
    screen.blit(text, (20, HEIGHT - BOTTOM_PANEL + 10))
    instruction = SMALL_FONT.render("Naciśnij R, aby zrestartować", True, TURN_COLOR)
    screen.blit(instruction, (WIDTH - instruction.get_width() - 10, HEIGHT - BOTTOM_PANEL + 10))

def draw_button(text, y):
    rect = pygame.Rect(WIDTH // 2 - 150, y, 300, 60)
    pygame.draw.rect(screen, BUTTON_COLOR, rect, border_radius=10)
    txt = FONT.render(text, True, TEXT_COLOR)
    screen.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))
    return rect

def show_start_screen():
    screen.fill(BG_COLOR)
    title = BIG_FONT.render("Kółko i Krzyżyk", True, TEXT_COLOR)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    pvp_button = draw_button("Gracz vs Gracz", 250)
    ai_button = draw_button("Gracz vs SI", 350)

    pygame.display.update()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if pvp_button.collidepoint(e.pos):
                    return False
                elif ai_button.collidepoint(e.pos):
                    return True

def restart():
    global board, game_over, player, start_time
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    screen.fill(BG_COLOR)
    draw_lines()
    game_over = False
    player = 1
    start_time = time.time()
    logging.info("Gra została zrestartowana")

def ai_play_move(): 
    global player, game_over
    if not is_board_full(board):
        row, col = find_best_move(board)
        if row != -1 and col != -1:
            board[row][col] = 2
            logging.info("Ruch AI")
            if check_win(board, 2):
                game_over = True
            elif is_board_full(board):
                game_over = True
            player = 1
            return True
    return False


if __name__ == "__main__": 
    vs_ai = show_start_screen()
    restart()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info("Gra zakończona przez użytkownika")
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if my < WIDTH:
                        row = my // SQSIZE
                        col = mx // SQSIZE
                        if board[row][col] == 0:
                            board[row][col] = player
                            logging.info(f"Gracz {player} wykonał ruch na polu ({row}, {col})")
                            if check_win(board, player):
                                game_over = True
                            elif is_board_full(board):
                                game_over = True
                            else:
                                player = 2 if player == 1 else 1
                                if vs_ai and player == 2:
                                    pygame.time.delay(300)
                                    ai_play_move()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart()

        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()

        if game_over:
            if is_board_full(board) and not check_win(board, 1) and not check_win(board, 2):
                draw_tie()
            else:
                if check_win(board, 1):
                    draw_winner(1)
                elif check_win(board, 2):
                    draw_winner(2)
        else:
            draw_turn(player)

        pygame.display.update()
