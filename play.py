import pygame
from sys import exit
from random import randint

def display_score():
    curr_time = int(pygame.time.get_ticks() / 100) - start_time
    score_surf = test_font.render(f'Score: {curr_time}', False, 'gold')
    score_rect = score_surf.get_rect(topleft = (350,60))
    # pygame.draw.rect(screen, 'green', score_rect)
    # pygame.draw.rect(screen, 'green', score_rect, 10)
    screen.blit(score_surf, score_rect)
    return curr_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 2
            screen.blit(enamy_surf, obstacle_rect)
        return obstacle_list
    
    else: return []

    

pygame.init() 
screen = pygame.display.set_mode((800,400)) # 바탕화면
# 여기까지 실행하면 창이 떴다가 바로 꺼짐. 이를 해결하기 위해 While 루프 돌리기
pygame.display.set_caption('Pixel Jumper') # 게임 창의 title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0

store_score = [0]
max_score = max(store_score)

sky_surface = pygame.image.load('graphics/sky1.png').convert_alpha() # 바탕 위의 스크린
ground_surface = pygame.image.load('graphics/ground2.png').convert_alpha()

# max_surf = test_font.render(f'BEST: {max_score}', False, 'Blue')

enamy_surf = pygame.image.load("graphics/snail/walk01.png").convert_alpha()
enamy_rect = enamy_surf.get_rect(center = (randint(500, 900), 300))
# obstacle
obstacle_rect_list = []

player_surf = pygame.image.load("graphics/Player/Skeleton_Walk1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,330))
player_gravity = 0

# intro screen
player_stand = pygame.image.load("graphics/snail/walk06.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (380,210))

game_name = test_font.render('Pixel Jumper', False, 'black')
game_name_rect = game_name.get_rect(center = (420,120))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)


while True:
    # event loop
    for event in pygame.event.get(): # 창 닫기 버튼
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity = -20
            
            if event.type == pygame.KEYDOWN: # jump
                if event.key == pygame.K_SPACE and player_rect.bottom >= 330:
                    player_gravity = -20
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enamy_rect.left = 800
                player_rect.left = 0
                start_time = int(pygame.time.get_ticks() / 100)

        if event.type == obstacle_timer:
                obstacle_rect_list.append(enamy_surf.get_rect(center = (randint(500,1000), 300)))
                         
                
    if game_active:
        screen.blit(sky_surface, (0,0)) # blit는 블록 이미지 전송을 의미. 화면 만들기
        screen.blit(ground_surface, (0,20))
        # pygame.draw.rect(screen, 'green', score_rect)
        # pygame.draw.rect(screen, 'green', score_rect, 10)
        # #pygame.draw.ellipse(screen, 'gold', (0,0), (800,500))
        # screen.blit(score_surf, score_rect)
        
        display_score()
        max_score = max(store_score)
        max_surf = test_font.render(f'BEST: {max_score}', False, 'gold') 
        screen.blit(max_surf, (30, 20)) # best score 표시

        # timer 때문에 더 이상 필요 x
        # enamy_rect.x -= 3
        # if enamy_rect.x < -50:
        #     enamy_rect.x = 800
        # screen.blit(enamy_surf, enamy_rect)

        # Player
        player_rect.x += 4
        if player_rect.x > 900:
            player_rect.x = -10 


        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 330:
            player_rect.bottom = 330 # 바닥에 붙이기
        screen.blit(player_surf, player_rect)

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        if enamy_rect.colliderect(player_rect):
            store_score.append(display_score())
            max_score = max(store_score) # 죽을 때 best score 계산
            game_active = False
    else:
        screen.fill('dark gray')
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        
        max_score = max(store_score)
        max_surf = test_font.render(f'BEST: {max_score}', False, 'gold') 
        screen.blit(max_surf, (30, 20))

        curr_score = store_score[-1]
        curr_surf = test_font.render(f'CURRENT: {curr_score}', False, 'gold') 
        screen.blit(curr_surf, (30, 60))


    pygame.display.update() # 창이 while 루프 종료 전까지는 계속 켜있게 해줌
    clock.tick(60) # 최대 프레임 속도 설정

