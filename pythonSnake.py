#fix the movement functions
import pygame
import random as rand
pygame.init()

x = 5
y = 12

win = pygame.display.set_mode((500,500))
pygame.draw.rect(win, (0,255,0), (20*x,20*y,20,20))

pygame.display.set_caption("Python (Ha! See what I did there? ( ͡° ͜ʖ ͡°)")

lastKeyPressed_right = True
lastKeyPressed_up = False
lastKeyPressed_left = False
lastKeyPressed_down = False

snake = [[[0,0],False]]*625
for i in range(1,625):
    snake[i]=[[0,0],False]
snake[0]=[[x*20,y*20],True]

snakeLength=1

food = [12*20,12*20]

def newKeyPressed():
    global lastKeyPressed_right
    global lastKeyPressed_up
    global lastKeyPressed_left
    global lastKeyPressed_down

    lastKeyPressed_right = False
    lastKeyPressed_up = False
    lastKeyPressed_left = False
    lastKeyPressed_down = False




def placeFood():
    global food
    
    food[0]=20*rand.randint(0,24)
    food[1]=20*rand.randint(0,24)



def feed():
    global snake
    global snakeLength
    global food
    samePlace=True

    snake[snakeLength][1]=True
    snakeLength+=1

    while samePlace:
        placeFood()
        for i in range(snakeLength):
            #print(snake[i])
            if (snake[i][0]==food and snake[i][1]):
                break
            samePlace=False


#print(snake)


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
        
    snake[0][0][0]=x*20
    snake[0][0][1]=y*20

    if snake[0][0]==food:
        feed()

    for i in range(1,snakeLength):
        if (snake[0][0]==snake[i][0] and snake[i][1]):
            print(snake[0],snake[1])
            Alive=False
            break

    for i in reversed(range(1,625)):
        snake[i][0]=snake[i-1][0]

    win.fill((0,0,0))
    for i in snake:
        if i[1]:
            pygame.draw.rect(win, (0,255,0), (i[0][0],i[0][1],20,20))
    pygame.draw.rect(win, (255,0,0), (food[0],food[1],20,20))

    if not Alive:
       print("i ded")



pygame.quit()
