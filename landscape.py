# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()

WIDTH = 500
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()



 

# ---------------------------
# Initialize global variables

# first 2 circles
circle_1_colour = (30, 50, 40)
circle_2_colour = (100, 20, 50)

circle_x = 50
circle_y = 250

circle_w = 450
circle_z = 250

circle_x_speed = 3
circle_y_speed = 0.5

circle_w_speed = -3
circle_z_speed = -0.5



# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
    # GAME STATE UPDATES
    # All game math and comparisons happen here

    if circle_x > 150 and circle_x < 350 and circle_y > 150 and circle_y < 350:
        circle_1_colour = (20, 35, 25)
    else:
        circle_1_colour = (40, 65, 50)


    if circle_w > 150 and circle_w < 350 and circle_z > 150 and circle_z < 350:
        circle_2_colour =(50, 10, 25)
    else:
        circle_2_colour =(130, 25, 45)
    
    circle_x += circle_x_speed
    circle_y += circle_y_speed
    
    circle_z += circle_z_speed
    circle_w += circle_w_speed
    
    #circle 1 X axis
    if circle_x > WIDTH:
        circle_x_speed *= -1
    elif circle_x < 0:
        circle_x_speed *= -1

    #circle 1 Y axis
    if circle_y > 350:
        circle_y_speed *= -1
    elif circle_y < 150: 
        circle_y_speed *= -1


    #circle 2 Y axis
    if circle_z > 350 :
        circle_z_speed *= -1
    elif circle_z < 150:
        circle_z_speed *= -1
        
    #circle 2 X axis
    if circle_w > WIDTH:
        circle_w_speed *= -1
    elif circle_w < 0:
        circle_w_speed *= -1


   
    
        
         
    
    # DRAWING
    screen.fill((30, 30, 30))  # always the first drawing command

    #sun
    pygame.draw.circle(screen, (255, 255, 0), (250, 250), 100)

    # planets
    pygame.draw.circle(screen, (30, 50, 40), (circle_x, circle_y), 30)
    pygame.draw.circle(screen, (100, 20, 50), (circle_w, circle_z), 30)

    #stars 
    pygame.draw.circle(screen, ('#FFFFFF'), (50, 200), 4)
    pygame.draw.circle(screen, ('#FFFFFF'), (400, 459), 16)
    pygame.draw.circle(screen, ('#FFFFFF'), (400, 300), 8)
    pygame.draw.circle(screen, ('#FFFFFF'), (50, 400), 8)
    pygame.draw.circle(screen, ('#FFFFFF'), (350, 50), 10)
    pygame.draw.circle(screen, ('#FFFFFF'), (10, 450), 6)
    pygame.draw.circle(screen, ('#FFFFFF'), (450, 30), 10)
    pygame.draw.circle(screen, ('#FFFFFF'), (200, 80), 13)
    pygame.draw.circle(screen, ('#FFFFFF'), (60, 60), 5)
    pygame.draw.circle(screen, ('#FFFFFF'), (300, 420), 9)
    
    
    #planets shadows
    pygame.draw.circle(screen, (circle_1_colour), (circle_x, circle_y), 25)
    pygame.draw.circle(screen, (circle_2_colour), (circle_w, circle_z), 25)

    
    #distant planets 

    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------
    

pygame.quit()

