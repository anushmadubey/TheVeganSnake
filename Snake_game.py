import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')

icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

img = pygame.image.load('SnakeHead.png')
appleimg = pygame.image.load('apple.png')

apple_thickness = 30 
block_size = 20
FPS = 10

direction = "right"
clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():

    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")
    message_to_screen("Press C to continue, P to pause or Q to quit",
                      black,
                      25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #game_display.fill(white)
       
        clock.tick(5)
                    
                
                
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    game_display.blit(text, [0,0])


def rand_appleGen():
      rand_applex = round(random.randrange(0, display_width - apple_thickness))#/10.0)*10.0
      rand_appley = round(random.randrange(0, display_height - apple_thickness))#/10.0)*10.0
      return rand_applex, rand_appley


             
def game_intro():
    intro = True

    while intro:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        game_display.fill(white)
        message_to_screen("Snake game!",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to eat apples xD",
                          black,
                          -30)
        message_to_screen("Yes, a *vegetarian* game xD",
                          black,
                          10)
        

        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          45,
                          )
        message_to_screen("If you run into yourself, or the edges, you die.",
                          black,
                          70)
        

        message_to_screen("Press C to play, P to pause or Q to quit.",
                          black,
                          180)
        pygame.display.update()
        clock.tick(15)
    
def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    

    game_display.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(game_display, green, [XnY[0] ,XnY[1], block_size,block_size])

def text_objects (text, colour,size):
    if size == "small":
        text_surface = smallfont.render(text, True, colour)
    if size == "medium":
        text_surface = medfont.render(text, True, colour)
    if size == "large":
        text_surface = largefont.render(text, True, colour)
        
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, colour, y_displace=0, size = "small"):
    text_surf, text_rect = text_objects(msg,colour,size)
    text_rect.center = (display_width/2),(display_height/2)+y_displace
    game_display.blit(text_surf, text_rect)

    
def game_loop():
    global direction
    direction = 'right'
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    snakeList = []
    snakeLength = 1

    rand_applex, rand_appley = rand_appleGen()
    
    game_exit = False
    game_over = False

    while not game_exit:
        if game_over == True:
            message_to_screen("Game Over. ",
                              red,
                s              -50,
                              size ="large")
            message_to_screen("Press C to continue and Q to quit ",
                              black,
                              50,
                              size ="medium" )
            pygame.display.update()
            

        while game_over == True:
            #game_display.fill(white)
         

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
                   
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True

                
        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(white)
        
        #pygame.draw.rect(game_display, red, [rand_applex, rand_appley, apple_thickness, apple_thickness])
        game_display.blit(appleimg,(rand_applex, rand_appley))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
            
        for eachSegment in snakeList [:-1]:
            if eachSegment == snakeHead:
                game_over = True

        snake(block_size, snakeList)

        score(snakeLength - 1)        
        pygame.display.update()


        if lead_x > rand_applex and lead_x < rand_applex + apple_thickness or lead_x + apple_thickness > rand_applex and lead_x + apple_thickness < rand_applex + apple_thickness:
            if lead_y > rand_appley and lead_y < rand_appley + apple_thickness or lead_y + apple_thickness > rand_appley and lead_y + apple_thickness < rand_appley + apple_thickness:
               rand_applex, rand_appley = rand_appleGen()
               snakeLength += 1
              
        clock.tick(FPS)
    
    pygame.quit()
    quit()

game_intro()
game_loop()
 
