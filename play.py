import pygame
from sys import exit

pygame.init() 
screen = pygame.display.set_mode((800,500)) # 바탕화면
# 여기까지 실행하면 창이 떴다가 바로 꺼짐. 이를 해결하기 위해 While 루프 돌리기
pygame.display.set_caption('Runner') # 게임 창의 title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)


sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha() # 바탕 위의 스크린
ground_surface = pygame.image.load('graphics/ground2.png').convert_alpha()
text_surface = test_font.render("GG", False, 'Blue')


enamy_surf = pygame.image.load("graphics/snail/walk01.png").convert_alpha()
enamy_rect = enamy_surf.get_rect(bottomright = (500, 333))

player_surf = pygame.image.load("graphics/Player/Skeleton_Walk1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,330))

while True:
    for event in pygame.event.get(): # 창 닫기 버튼
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0)) # blit는 블록 이미지 전송을 의미. 화면 만들기
    screen.blit(ground_surface, (0,20))
    screen.blit(text_surface, (350,50))


    enamy_rect.x -= 3
    if enamy_rect.x < -50:
        enamy_rect.x = 800
    screen.blit(enamy_surf, enamy_rect)

    player_rect.x += 4
    if player_rect.x > 900:
        player_rect.x = -10
    screen.blit(player_surf, player_rect)

    if player_rect.colliderect(enamy_rect): # True or False 

    # 1:13:42 https://www.youtube.com/watch?v=AY9MnQ4x3zk

    pygame.display.update() # 창이 while 루프 종료 전까지는 계속 켜있게 해줌
    clock.tick(60) # 최대 프레임 속도 설정

