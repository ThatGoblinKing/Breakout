import pygame
import random

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, sizeX, sizeY))
    def checkCollision(self, ballX, ballY):
        colliding = (ballX >= self.xpos and ballX + 20 <= self.xpos + sizeX and ballY + 20 >= self.ypos and ballY <= self.ypos + sizeY)
        return colliding
    def die(self):
        self.isDead = True

pygame.init()
pygame.display.set_caption("")
screenX = 1920/2
screenY = 1080/2
screen = pygame.display.set_mode((screenX, screenY))
playerSize = 150

doExit = False
moveSpeed = 3.5
clock = pygame.time.Clock()

#Paddle Positions
playerX = 20
playerY = screenY - 40

#Ball Positions
bx = screenX/2
by = screenY/2
#Ball Velocity
ballVelo = 5
bVx = ballVelo
bVy = -ballVelo

columns = 12
rows = 3
blockSection = screenY/3

blockGapX, blockGapY = (10, 10)
sizeX = (screenX/columns) - blockGapX
sizeY = (blockSection/rows) - blockGapY


bricks = []

for x in range(columns):
    for y in range (rows):
        bricks.append(brick(x * (screenX/columns), y * (blockSection/rows)))


bricksOnScreen = len(bricks)

while not doExit:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True #exits game loop

    #Game Logic
    #Controls
    keys = pygame.key.get_pressed()


    #P1
    if keys[pygame.K_a] and playerX > 0:
        playerX-=5
    if keys[pygame.K_d] and playerX + playerSize < screenX:
        playerX+=5

    bx += bVx
    by += bVy

    #Ball bounce
    if bx < 0:
        bVx *= -1
        bColor = (255, 255, 255)

    if bx + 20 > screenX:
        bVx *= -1
        bColor = (255, 255, 255)

    if by < 0 or by + 20 > screenY:
        bVy *= -1
    if by > playerY - 20 and bx + 20 > playerX and bx < playerX + playerSize:
        by = playerY - 20
        bVy *= -1

    if bricksOnScreen == 0 or by + 20 >= screenY:
        for brick in bricks:
            brick.isDead = False
        bx = screenX/2
        by = screenY/2
        bvx = - ballVelo
        bVy = -ballVelo
        bricksOnScreen = len(bricks)

    #Render Section
    screen.fill((0,0,0))
    for brick in bricks:
        brick.draw()
        if (not brick.isDead) and brick.checkCollision(bx, by):
            bVy *= -1
            brick.die()
            bricksOnScreen -= 1


    #Paddles
    pygame.draw.rect(screen, (255, 255, 255), (playerX, playerY, playerSize, 20))

    #Ball
    pygame.draw.rect(screen, (255, 255, 255), (bx, by, 20, 20))

    pygame.display.flip()
pygame.quit() 