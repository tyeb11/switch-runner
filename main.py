
from os import PRIO_PGRP, truncate
import pygame
from sys import exit
from random import randint

from pygame.constants import BUTTON_LEFT



#SCORE
def display_score():
    
    current_time=int(pygame.time.get_ticks()/1000)-start_time
    score_surf = test_font.render(f'Score: {current_time}',True,(254,0,0))
    score_rec = score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rec)
    #print(current_time)
    return current_time

pygame.init()


start_time=0
score=0


#SOUND
sound=pygame.mixer.Sound('music/run.mp3')
#sound.set_volume(0.1)

sound1=pygame.mixer.Sound('music/entry.mp3')
#sound1.set_volume(0.1)


#FONT
test_font = pygame.font.Font('fonts/ChelaOne-Regular.ttf',35)
head_font =pygame.font.Font('fonts/Nosifer-Regular.ttf',50)



#OBSTRACLE
def obstacle_movement(obstacle_list):
    
    if obstacle_list:
        for obstacle_react in obstacle_list:
            if score>10:
                obstacle_react.x-=15+5
            else:
                obstacle_react.x-=15

            if obstacle_react.bottom==460 or obstacle_react.bottom==260:
                screen.blit(enemy1_img,obstacle_react)
            else: 
                screen.blit(enemy_img,obstacle_react)



        
        

        return obstacle_list

    else:
        return []



def collisions(player,obstracles):
    if obstracles:
        for obstacle_rect in obstracles:
            if player.colliderect(obstacle_rect):return False
    return True








y=400
clock = pygame.time.Clock()

#GRAPHICS

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Switch Runner')
bk_img=pygame.image.load('Assets/background.jpeg').convert_alpha()

player_img=pygame.image.load('Assets/box.jpeg').convert_alpha()
player_rec =player_img.get_rect(midbottom=(250,200))

platform_img = pygame.image.load('Assets/bk.jpeg').convert_alpha()
platform_rec=platform_img.get_rect(midbottom=(400,400))
platform_rec1=platform_img.get_rect(midbottom=(400,200))


enemy_img=pygame.image.load('Assets/enemy.jpeg').convert_alpha()
enemy_rec = enemy_img.get_rect(midbottom=(1050,y))

enemy1_img=pygame.image.load('Assets/enemy1.jpeg').convert_alpha()
enemy1_rec = enemy1_img.get_rect(midbottom=(650,y))

game_name = head_font.render('Switch Runner',True,(51,153,255))
game_name_rec = game_name.get_rect(center=(400,80))

game_message =test_font.render('Press   Tab   to run',True,(0,204,102))
game_message_rec =game_message.get_rect(center=(400,420))

player_stand = pygame.image.load('Assets/box.jpeg').convert_alpha()


player_stand_rec = player_stand.get_rect(center=(400,200))

enemy_stand_img=pygame.image.load('Assets/entryenemy1.png').convert_alpha()
enemy_stand_rec = enemy_stand_img.get_rect(midbottom=(600,225))

enemy1_stand_img=pygame.image.load('Assets/entryenemy.png').convert_alpha()
enemy1_stand_rec = enemy1_stand_img.get_rect(midbottom=(200,275))
platform1_img = pygame.image.load('Assets/bk.jpeg').convert_alpha()

game_message1 =test_font.render('Press   Esc   to Quit',True,(255,51,51))
game_message1_rec =game_message1.get_rect(center=(400,500))



player_above=True


player_plat1=True
player_plat2=False


obstacle_rect_list=[]

game_active=False

#TIMER
obstacle_timer=pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,randint(800,1000))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #print("SPACE")
                    
                    print(player_above)
                    if player_plat1:
                        if player_above:
                            player_rec.bottom=player_rec.bottom+60
                            player_above=False
                        else:
                            player_rec.bottom=player_rec.bottom-60
                            player_above=True

                    if player_plat2:
                        if player_above:
                            player_rec.bottom=player_rec.bottom+60
                            player_above=False
                        else:
                            player_rec.bottom=player_rec.bottom-60
                            player_above=True
                        
                    

                if event.key ==pygame.K_UP:
                    print("Key up")
                    if player_above and player_rec.bottom==400:
                    
                        player_rec.bottom=260
                        player_above=False
                        player_plat2=False
                        
                        if player_plat1:
                            player_plat1=False
                        else:
                            player_plat1=True
                        #player_rec.bottom=460
                        
                    
                    
                    
                if event.key ==pygame.K_DOWN:
                    print("Key down")
                    if player_above==False and player_rec.bottom==260:
                    
                        #player_rec.bottom=400
                        player_rec.bottom=400
                        player_above=True
                        player_plat1=False
                        if player_plat2:
                            player_plat2=False
                        else:
                            player_plat2=True
                        
                    
                    
                    

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    game_active=True
                    start_time=int(pygame.time.get_ticks()/1000)
                    enemy_rec.left=800
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


        if event.type == obstacle_timer and game_active:
                #print('test')
            if randint(0,2):
                obstacle_rect_list.append(enemy_img.get_rect(midbottom=(randint(800,1000),y)))
                obstacle_rect_list.append(enemy1_img.get_rect(midbottom=(randint(1000,1500),y+60)))
            else:
                obstacle_rect_list.append(enemy_img.get_rect(midbottom=(randint(1100,1300),200)))
                obstacle_rect_list.append(enemy1_img.get_rect(midbottom=(randint(1300,1700),200+60)))

    if game_active:
        
        sound1.set_volume(0)
        sound.play(loops=-1)
        sound.set_volume(0.1)


        screen.blit(bk_img,(0,0))
        screen.blit(platform_img,(-100,y))
        screen.blit(platform_img,(-100,200))
        score =display_score()
        enemy_rec.x-=15
        screen.blit(enemy_img,enemy_rec)

        obstacle_rect_list=obstacle_movement(obstacle_rect_list)
        

        game_active=collisions(player_rec,obstacle_rect_list)

        

        
            
        

            

        

        screen.blit(player_img,player_rec)

        if player_rec.colliderect(enemy_rec):game_active=False
    else:
        sound.play(loops=-1)
        sound.set_volume(0)
        sound1.play(loops=-1)
        sound1.set_volume(0.1)

        screen.fill((96,96,96))
        obstacle_rect_list.clear()

        
        screen.blit(game_name,game_name_rec)
        screen.blit(player_stand,player_stand_rec)
        screen.blit(platform1_img,(-100,225))
        screen.blit(enemy1_stand_img,enemy1_stand_rec)
        screen.blit(enemy_stand_img,enemy_stand_rec)
        score_message=test_font.render(f'Your Score:{score}',False,(102,204,0))
        score_message_rect=score_message.get_rect(center=(400,420))
        screen.blit(game_message1,game_message1_rec)
        if score ==0:

            screen.blit(game_message,game_message_rec)
        else:
            screen.blit(score_message,score_message_rect)
        

    



    pygame.display.flip()
    clock.tick(60)
