import pygame
import time
pygame.init()
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)

xPos = 10
yPos = 150
change = 0

botYPos = 250
botYChange = -3

displayWidth = 600
displayHeight = 400

paddleHeight = 50
paddleLength = 10

ballXPos = displayWidth // 2
ballYPos = displayHeight // 2
ballSize = 10
ballXChange = 2
ballYChange = 2

playerScore = '0'
botScore = '0'
font = pygame.font.Font('freesansbold.ttf', 32)

display = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Pongs")

gameOver = False
while not gameOver:
    display.fill(black)
    displayPlayerScore = font.render(playerScore, True, white)
    displayBotScore = font.render(botScore, True, white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change = -3
            if event.key == pygame.K_s:
                change = +3
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_w) or (event.key == pygame.K_s):
                change = 0
    
    yPos += change
    playerPaddle = pygame.draw.rect(display, white, [xPos, yPos, paddleLength, paddleHeight])
    if yPos < 0:
        yPos = 0
    if yPos + paddleHeight > displayHeight:
        yPos = displayHeight - paddleHeight

    ball = pygame.draw.rect(display, white, [ballXPos,ballYPos,ballSize,ballSize])
    ballXPos -= ballXChange
    ballYPos -= ballYChange
    if ballYPos < 0:
        ballYChange = -ballYChange
    if ballXPos < 0:
        ballXChange = -ballXChange
        ballXPos = displayWidth // 2
        ballYPos = displayHeight // 2
        botScore = str(int(botScore)+1)
    if ballYPos + ballSize > displayHeight:
        ballYChange = -ballYChange
    if ballXPos + ballSize > displayWidth:
        ballXChange = -ballXChange
        ballXPos = displayWidth // 2
        ballYPos = displayHeight // 2
        playerScore = str(int(playerScore)+1)

    botPaddle = pygame.draw.rect(display, white, [displayWidth-20, botYPos, paddleLength, paddleHeight])
    if (botYPos - ballYPos) > -20:
        botYChange = -1.75
    elif (botYPos - ballYPos) == -20:
        botYChange = 0
    elif (botYPos - ballYPos) < -20:
        botYChange = 1.75
    botYPos += botYChange

    if pygame.Rect.colliderect(playerPaddle, ball) is True:
        ballXPos += 4
        ballXChange = -ballXChange
    if pygame.Rect.colliderect(botPaddle, ball) is True:
        ballXPos -= 4
        ballXChange = -ballXChange

    display.blit(displayPlayerScore, (150,20))
    display.blit(displayBotScore, (displayWidth-160,20))
    for i in range(displayHeight):
        if (i % 50) == 15:
            pygame.draw.rect(display, white, [displayWidth//2, i, 5, 25])
    pygame.display.update()
    clock.tick(120)
    time.sleep(0)

pygame.quit()
quit()