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

snakeLength=1
snake = [[[0,0],False]]*625

food = [12*20,12*20]

def restart():
    global lastKeyPressed_right
    global lastKeyPressed_up
    global lastKeyPressed_left
    global lastKeyPressed_down
    global snake
    global snakeLength
    global food
    global Alive
    global x
    global y

    lastKeyPressed_right = True
    lastKeyPressed_up = False
    lastKeyPressed_left = False
    lastKeyPressed_down = False

    x=5
    y=12

    for i in range(1,625):
        snake[i]=[[0,0],False]
    snake[0]=[[x*20,y*20],True]

    snakeLength=1

    Alive = True

    food = [12*20,12*20]


restart()


def move():
    global lastKeyPressed_right
    global lastKeyPressed_up
    global lastKeyPressed_left
    global lastKeyPressed_down
    global x
    global y
    

    if lastKeyPressed_right:
        x+=1

    if lastKeyPressed_up:
        y-=1

    if lastKeyPressed_left:
        x-=1
        
    if lastKeyPressed_down:
        y+=1

    for i in reversed(range(1,625)):
        snake[i][0]=snake[i-1][0]

    snake[0][0]=[20*x,20*y]
        
        

def newKeyPressed():#clears out the current movement direction
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



def feed():#grows the snake and sets more food
    global snake
    global snakeLength
    global food
    samePlace=True

    snake[snakeLength][1]=True
    snakeLength+=1

    while samePlace:
        placeFood()
        for i in range(snakeLength):
            if (snake[i][0]==food and snake[i][1]):
                break
            samePlace=False


quit = False
Alive = True
while not quit:
    pygame.display.update()
    pygame.time.delay(200)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Alive = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:
        restart()

    if keys[pygame.K_q]:
        break
        
    if not Alive:#freezes the game while user decides to restart or quit
        continue
    
    moved = False#to ensure the snake cant move back in on itself
    
    if keys[pygame.K_RIGHT]:
        if not lastKeyPressed_left and not moved:
            moved = True
            newKeyPressed()
            lastKeyPressed_right = True

    if keys[pygame.K_UP]:
        if not lastKeyPressed_down and not moved:
            moved = True
            newKeyPressed()
            lastKeyPressed_up = True

    if keys[pygame.K_LEFT]:
        if not lastKeyPressed_right and not moved:
            moved = True
            newKeyPressed()
            lastKeyPressed_left = True

    if keys[pygame.K_DOWN]:
        if not lastKeyPressed_up and not moved:
            moved = True
            newKeyPressed()
            lastKeyPressed_down = True

        #it was here that i realized i couldve used an enum
        #instead of all these booleans and made life easier
        
    move()
        
        #oh jk. wouldve been the same amount of work because
        #python doesnt have switch case

    
    if not 0<=x<=24 or not 0<=y<=24:#if you hit a wall
        print("oof, thats a wall")

    if x<0:     #check if snake is still alive
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
    

    if snake[0][0]==food:#if you ate the food
        feed()

    for i in range(1,snakeLength):
        if (snake[0][0]==snake[i][0] and snake[i][1]):#if you bit yourself
            print("oops, done bit myself")
            Alive=False
            break

    win.fill((0,0,0))
    for i in snake:
        if i[1]:
            pygame.draw.rect(win, (0,255,0), (i[0][0],i[0][1],20,20))
    pygame.draw.rect(win, (255,0,0), (food[0],food[1],20,20))

    if not Alive:
        print("i ded")
        print("Your snake was ",snakeLength," blocks long")



pygame.quit()
