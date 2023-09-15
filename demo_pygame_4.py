import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Ishan's Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:  # Making sure the top right corner of our character is less than the screen width - its width 
        x += vel

    '''if keys[pygame.K_UP] and y > vel:  # Same principles apply for the y coordinate
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel'''
    if not(isJump): # Checks is user is not jumping
        if keys[pygame.K_UP] and y > vel:  # Same principles apply for the y coordinate
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        # This is what will happen if we are jumping
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
        
    win.fill((0,0,255))
    pygame.draw.rect(win, (255,0,255), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()
