import pygame
import random
import os

pygame.init()


#game variable 
window_writh=500
window_length=500
wigth= (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)
startimg = pygame.image.load("Start.png")
endimg = pygame.image.load("Game Over.jpeg")
snake_length=10
snake_writh=15
music = {1 :"Motorball  Alita Battle Angel OST.mp3" , 2 : "NFS.mp3",3:"Eclipse.mp3",4:"DMC.mp3",5:"Fearless.mp3"}





game_window=pygame.display.set_mode((window_writh, window_length))
pygame.display.set_caption("Box Snake Game")
clock = pygame.time.Clock()
startimg=pygame.transform.scale(startimg, (window_writh, window_length)).convert_alpha()
endimg=pygame.transform.scale(endimg, (window_writh, window_length)).convert_alpha()
#fount for text on game screen and function
font=pygame.font.SysFont(None,35,True)


#Displaying Text on game screen
def text_on_screen(text , color, x, y):

    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake( snk_list):
    length_of_list=len(snk_list)

    for x,y in snk_list:
        if x==snk_list[length_of_list-1][0] and y==snk_list[length_of_list-1][1] :
            color=green
        else :
            color=black
        pygame.draw.rect(game_window , color, [x, y, snake_writh , snake_length])

def game_over(highscore):
    
    game_window.blit(endimg,(0,0))
    text_on_screen("HIGHSCORE  "+str(highscore),(0,0,255),window_writh/3,window_length/5)
    with open("highscore.txt","w") as f:
        f.write(str(highscore))
    text_on_screen("PRESS ENTER TO CONTINUE",(0,0,255),window_writh/3,window_length/1.3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.draw.rect(game_window , green, [100, 100, snake_writh , snake_length])
                game()

def welcome():
    game_window.fill(wigth)
    game_window.blit(startimg,(0,0))
    text_on_screen("Welcome to box snack game click to start ",black,100,300)
    pygame.display.update()
##    for event in pygame.event.get():
##        print(event)
##        
##        if event.type == pygame.KEYDOWN:
##            print("keydown")
##            if event.key == pygame.K_RIGHT:
##                print("Right arrow key presed")
##        if True :
##            print("working")
##        if event.type == pygame.QUIT :
##                pygame.quit()
##        if event.type == pygame.MOUSEBUTTONDOWN :
##            if event.button == LEFT:
    pygame.time.delay(5000)
    game()
    
def game():
    
    exit_game=False
    food_x=random.randint(20, window_writh-20)
    food_y=random.randint(20, window_length-20)
    snake_x=random.randint(20, window_writh-20)
    snake_y=random.randint(20, window_length-20)
    velocity_x=0
    velocity_y=0
    score=0
    speed=1
    fps = 60
    snk_length=1
    snk_list=[]
    #check if highscore.txt exist
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore = f.read()
    #Game Loop
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x=speed
                    velocity_y=0
                if event.key == pygame.K_LEFT:
                    velocity_x=-speed
                    velocity_y=0
                if event.key == pygame.K_UP:
                    velocity_x=0
                    velocity_y=-speed
                if event.key == pygame.K_DOWN:
                    velocity_x=0
                    velocity_y=speed
                    
            if event.type == pygame.QUIT:
                exit_game = True
        if (not (pygame.mixer.music.get_busy())):
            rum=random.randint(0,5)
            pygame.mixer.music.load(music[rum])
            pygame.mixer.music.play()
        
        game_window.fill(red)
        if snake_x<window_writh-15 and snake_x>9:
            snake_x+=velocity_x
        else:
            pygame.time.delay(3000)
            game_window.fill(red)
            game_over(highscore)

        if snake_y<window_length-10 and snake_y>0:
            snake_y+=velocity_y
        else:
            pygame.time.delay(3000)
            game_window.fill(red)
            game_over(highscore)
            


        if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
            score+=10
            if score % 100 == 0 :
                speed+=1
            #print(score)
            if score > int(highscore):
                highscore=score
            food_x=random.randint(20, window_writh-20)
            food_y=random.randint(20, window_length-20)
            snk_length+=15

        

        head=[]
        head.append(snake_x)
        head.append(snake_y)


##     Logic for snk into its tail
##        if head in snk_list:
##            game_over(highscore)


        snk_list.append(head)


        if len(snk_list)>snk_length:
            del snk_list[0]
            if snk_length%100==0:
                for i in range (5):
                    del snk_length[i]
        plot_snake(snk_list)

        
        text_on_screen("Score = "+str(score), black, window_writh-150, 30)
        pygame.draw.rect(game_window, wigth ,[food_x, food_y, 10,10])
        
        pygame.display.update()
        clock.tick(fps)

    #Exit Game
    pygame.quit()


welcome()
