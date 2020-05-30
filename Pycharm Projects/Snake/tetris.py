import pygame
import random


class Cube:

    side = 20

    def __init__(self, color, x, y):
        self.color = color
        self.speed = 15
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, Cube.side, Cube.side))
        pygame.draw.rect(win, self.color, (self.x + 1, self.y + 1, Cube.side-2, Cube.side-2))

    def move(self):
        self.y += 10


class Piece:

    no_of_cubes = 4
    colors = [(0, 255, 0), (0, 255, 255), (255, 0, 0), (255, 255, 0), (0, 0, 255), (255, 128, 0), (255, 0, 255)]
    shapes = {'S': ['r', 'u', 'r'],
              'Z': ['r', 'd', 'r'],
              'L': ['d', 'r', 'r'],
              'J': ['r', 'r', 'u'],
              'I': ['r','r', 'r'],
              'O': ['r', 'd', 'l'],
              'T': ['r', 'u', 'd', 'r']}

    def __init__(self):
        self.shape_no = random.randrange(len(Piece.shapes))
        self.color = Piece.colors[self.shape_no]
        self.x = random.choice(range(20, width-100, 20))
        self.y = 0
        self.shape = self.make_shape()
        self.done = False

    def make_shape(self):
        side = Cube.side
        x = self.x
        y = self.y
        shape = [Cube(self.color, self.x, self.y)]
        directions = list(Piece.shapes.values())[self.shape_no]
        for d in directions:
            if d == 'r':
                x += side
            elif d == 'd':
                y += side
            elif d == 'l':
                x -= side
            elif d == 'u':
                y -= side
            shape.append(Cube(self.color, x, y))
        return shape

    def draw(self):
        for cube in self.shape:
            cube.draw()

    def move(self):
        for cube in self.shape:
            cube.y += 10
            if cube.y >= height - Cube.side:
                self.done = True


def main():
    global win, width, height
    width = 400
    height = 600
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")

    pieces = [Piece()]

    run = True

    while run:

        win.fill((0, 0, 0))
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for i, p in enumerate(pieces):
            p.draw()
            if not p.done:
                p.move()
            if i == len(pieces)-1 and p.done:
                pieces.append(Piece())


        pygame.display.update()


main()
