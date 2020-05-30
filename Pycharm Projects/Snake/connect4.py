import pygame
from itertools import cycle


class Slot:

    side = 50
    radius = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.filled = False

    def draw(self):
        centre = (self.x + self.side//2, self.y + self.side//2)
        pygame.draw.circle(win, self.color, centre, self.radius)

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.side:
            if self.y < pos[1] < self.y + self.side:
                return True


class Board:

    width = 350
    height = 300
    x = 25
    y = 55
    color = (0, 0, 255)

    def __init__(self):
        self.slots = []
        self.make_slots()
        self.done = False

    def make_slots(self):
        for i in range(self.x, self.x + self.width, Slot.side):
            col = []
            for j in range(self.y, self.y + self.height, Slot.side):
                col.append(Slot(i, j))
            self.slots.append(col)

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.color, (0, height-15, width, 15))
        for row in self.slots:
            for slot in row:
                slot.draw()


def check_win(game):

    board = game.slots
    combinations = [(1,0), (0,1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for i, col in enumerate(board):
        for j, slot in enumerate(col):

            if board[i][j].filled:

                color = board[i][j].color
                win_conds = []

                for c in combinations:
                    try:
                        win_conds.append([board[i+x*c[0]][j+x*c[1]] for x in range(4)])
                    except IndexError:
                        pass

                for cond in win_conds:

                    colors = [x.color for x in cond]

                    if len(set(colors)) == 1:

                        for x, s in enumerate(cond):
                            s.color = (0, 255, 0)

                        game.done = True

                        global win_color

                        if color == (255, 0, 0):
                            win_color = "Red"
                        elif color == (255, 255, 0):
                            win_color = "Yellow"

                        break


def show_win():
    font = pygame.font.Font("freesansbold.ttf", 24)
    msg = font.render(f"{win_color} wins! Click to play again", True, (0, 0, 0))
    win.blit(msg, (20, 15))



def main():
    global win, width, height, turn, game
    pygame.init()
    width = 400
    height = 370
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Connect 4")

    b = Board()

    red = (255, 0, 0)
    yellow = (255, 255, 0)
    turn = cycle([red, yellow])

    run = True

    while run:

        win.fill((255, 255, 255))
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not b.done:
                    for col in b.slots:
                        for slot in col:
                            if slot.is_over(pos):
                                for i, s in enumerate(col):
                                    if s.filled:
                                        col[i-1].color = turn.__next__()
                                        col[i-1].filled = True
                                        break
                                    elif i == len(col)-1:
                                        s.color = turn.__next__()
                                        s.filled = True
                    check_win(b)
                else:
                    b = Board()

        if b.done:
            show_win()

        b.draw()
        pygame.display.update()


main()