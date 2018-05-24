import pygame
pygame.init()

x = 5
y = 10

win = pygame.display.set_mode((500,500))
pygame.draw.rect(win, (255,0,0), (20*x,20*y,20,20))

pygame.display.set_caption("Python (Ha! See what I did there? ( ͡° ͜ʖ ͡°)")

lastKeyPressed_right = True
lastKeyPressed_up = False
lastKeyPressed_left = False
lastKeyPressed_down = False

def newKeyPressed():
    global lastKeyPressed_right
    global lastKeyPressed_up
    global lastKeyPressed_left
    global lastKeyPressed_down

    lastKeyPressed_right = False
    lastKeyPressed_up = False
    lastKeyPressed_left = False
    lastKeyPressed_down = False


Alive = True
while Alive:
    pygame.display.update()
    pygame.time.delay(200)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Alive = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        newKeyPressed()
        lastKeyPressed_right = True

    if keys[pygame.K_UP]:
        newKeyPressed()
        lastKeyPressed_up = True

    if keys[pygame.K_LEFT]:
        newKeyPressed()
        lastKeyPressed_left = True

    if keys[pygame.K_DOWN]:
        newKeyPressed()
        lastKeyPressed_down = True

        #it was here that i realized i couldve used an enum
        #instead of all these booleans and made life easier
        
    if lastKeyPressed_right:
        x+=1

    if lastKeyPressed_up:
        y-=1

    if lastKeyPressed_left:
        x-=1
        
    if lastKeyPressed_down:
        y+=1
        
        #oh jk. wouldve been the same amount of work because
        #python doesnt have switch case

    if x<0:
        x=0
        Alive=False
        
    if y<0:
        y=0
        Alive=False
        
    if x>24:
        x=24
        Alive=False
        
    if y>24:
        y=24
        Alive=False

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (20*x,20*y,20,20))

    



pygame.quit()
