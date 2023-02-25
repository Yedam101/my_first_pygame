import pygame
from sys import exit

pygame.init() 
screen = pygame.display.set_mode((800,400)) # 여기까지 실행하면 창이 떴다가 바로 꺼짐. 이를 해결하기 위해 While 루프 돌리기
pygame.display.set_caption('Runner') # 게임 창의 title
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get(): # 창 닫기 버튼
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all elements
    # update everything
    pygame.display.update() # 창이 while 루프 종료 전까지는 계속 켜있게 해줌
    clock.tick(60) # 최대 프레임 속도 설정

