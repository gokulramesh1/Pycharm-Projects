import pygame
import random


class Ball:

    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.change = 10
        self.xchange = random.choice([6, -6])
        self.ychange = random.choice([8, -8])
        self.color = (255, 0, 0)
        self.radius = 5

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        if self.y <= 0:
            self.ychange *= -1
        elif self.y >= height:
            self.ychange *= -1
        self.x += self.xchange
        self.y += self.ychange


class Paddle:

    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 60
        self.color = (255, 255, 255)
        self.diry = 0
        self.speed = 15
        self.side = side

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self):

        keys = pygame.key.get_pressed()

        if self.side == 'right':
            if keys[pygame.K_UP]:
                self.diry = -1
            elif keys[pygame.K_DOWN]:
                self.diry = 1
            else:
                self.diry = 0

        if self.side == 'left':
            if keys[pygame.K_w]:
                self.diry = -1
            elif keys[pygame.K_s]:
                self.diry = 1
            else:
                self.diry = 0

        self.y += self.diry*self.speed

        if self.y <= 0:
            self.y = 0
        elif self.y >= height - self.height:
            self.y = height - self.height


class Score:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.font = pygame.font.Font("freesansbold.ttf", 24)
        self.val = 0
        self.color = (255, 255, 255)

    def show(self):
        score = self.font.render(str(self.val), True, self.color)
        win.blit(score, (self.x, self.y))


def collision(ball, paddle):

    if paddle.side == 'right':
        poc = ball.x + ball.radius
        pad = paddle.x
        if pad <= poc <= pad+10 and paddle.y < ball.y < paddle.y + paddle.height:
            ball.xchange += 2
            return True
    elif paddle.side == 'left':
        poc = ball.x - ball.radius
        pad = paddle.x + paddle.width
        if pad >= poc >= pad-10 and paddle.y < ball.y < paddle.y + paddle.height:
            ball.xchange -= 2
            return True


def redraw():
    win.fill((0, 0, 0))
    b.draw()
    p1.draw()
    p2.draw()
    s1.show()
    s2.show()


def main():
    global width, height, b, win, p1, p2, s1, s2
    pygame.init()
    width = 800
    height = 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")

    b = Ball()
    p1 = Paddle(width-30, height//2 - 10, 'right')
    p2 = Paddle(20, height//2 - 10, 'left')
    s1 = Score(5, 5)
    s2 = Score(width-29, 5)

    run = True

    while run:

        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        b.move()
        p1.move()
        p2.move()

        if b.x >= 800:
            s1.val += 1
            b = Ball()
        elif b.x <= 0:
            s2.val += 1
            b = Ball()

        if collision(b, p1) or collision(b, p2):
            b.xchange *= -1

        redraw()

        pygame.display.update()


main()
