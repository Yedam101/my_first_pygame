import pygame
from sys import exit

pygame.init() 
screen = pygame.display.set_mode((800,400)) # 바탕화면
# 여기까지 실행하면 창이 떴다가 바로 꺼짐. 이를 해결하기 위해 While 루프 돌리기
pygame.display.set_caption('Runner') # 게임 창의 title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True


sky_surface = pygame.image.load('graphics/sky1.png').convert_alpha() # 바탕 위의 스크린
ground_surface = pygame.image.load('graphics/ground2.png').convert_alpha()

score_surf = test_font.render("GG", False, 'Blue')
score_rect = score_surf.get_rect(topleft = (400,60))


enamy_surf = pygame.image.load("graphics/snail/walk01.png").convert_alpha()
enamy_rect = enamy_surf.get_rect(center = (500, 300))

player_surf = pygame.image.load("graphics/Player/Skeleton_Walk1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,330))
player_gravity = 0



while True:
    for event in pygame.event.get(): # 창 닫기 버튼
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            
            if event.type == pygame.KEYDOWN: # jump
                if event.key == pygame.K_SPACE and player_rect.bottom >= 330:
                    player_gravity = -20
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enamy_rect.left = 800
                player_rect.left = 0
                
                

    if game_active:
        screen.blit(sky_surface, (0,0)) # blit는 블록 이미지 전송을 의미. 화면 만들기
        screen.blit(ground_surface, (0,20))
        pygame.draw.rect(screen, 'green', score_rect)
        pygame.draw.rect(screen, 'green', score_rect, 10)
        #pygame.draw.ellipse(screen, 'gold', (0,0), (800,500))
        screen.blit(score_surf, score_rect)


        enamy_rect.x -= 3
        if enamy_rect.x < -50:
            enamy_rect.x = 800
        screen.blit(enamy_surf, enamy_rect)

        # Player
        player_rect.x += 4
        if player_rect.x > 900:
            player_rect.x = -10 


        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 330:
            player_rect.bottom = 330 # 바닥에 붙이기
        screen.blit(player_surf, player_rect)

        
        if enamy_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('yellow')


    pygame.display.update() # 창이 while 루프 종료 전까지는 계속 켜있게 해줌
    clock.tick(60) # 최대 프레임 속도 설정

