import pygame
import sys #инициализирует системные настройки для корректной работы
import random

pygame.init() 

FPS = 100 #частота обновления экрана
# зададим цвета с помощью переменных
orange = (255,150,100)
red = (255,0,0)
green = (0, 128, 0)
blue = (51,153, 255)
white = (255,255,255)
yellow = (255,255,0)
win_width = 700 #задаем ширину экрана
win_height = 700 #задаем высоту экрана
clock = pygame.time.Clock() 

size_block = 100 #задаём размер клеточки
margin = 15 # задаём размер одного поля
width = size_block*6 + margin*7 #задаём общий размер всегей игровой области
height = size_block*6 + margin*7

size_window = (width, height)
screen = pygame.display.set_mode(size_window) #задаем размер экрана

pygame.display.update()#обновление экрана

masClick = [[0]*6 for i in range (6)] # 1 variant - 3адаём массив нулей
masGreen = [[0]*6 for i in range (6)]

query = 0 # какой по счету ход - 1, 2, 3, 4, 5, 6
countGreen = 0
kol = 0

for row in range(6):
    for col in range(6):
        colorY = random.randint(0,6)
        colorX = random.randint(0,6)
        if col == colorY or row == colorX:
            color = green
            x=col*size_block + (col + 1)*margin
            y=row*size_block + (row + 1)*margin
            pygame.draw.rect(screen,color,(x,y,size_block,size_block))
            masGreen[row][col]="x"
            countGreen = countGreen + 1
        else:
            color = yellow
            x=col*size_block + (col + 1)*margin
            y=row*size_block + (row + 1)*margin
            pygame.draw.rect(screen,color,(x,y,size_block,size_block))
print(masGreen)
pygame.display.update()

def test():
    pygame.time.delay(2500) # замедление скорости мигания экрана
    for row in range(6):
         for col in range(6):
                 color = yellow
                 x=col*size_block + (col + 1)*margin
                 y=row*size_block + (row + 1)*margin
                 pygame.draw.rect(screen,color,(x,y,size_block,size_block))
    pygame.display.update()
test() # запускаем функцию

done = True
game_over = False # переменная конца игры
while done:     
    for i in pygame.event.get():
        # проверка события на выход из игры
        if i.type == pygame.QUIT:
            done = False
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN and not game_over:

            x_mouse,y_mouse = pygame.mouse.get_pos() # 1 variant - узнаём координаты щелчка мыши
            x_mouse = pygame.mouse.get_pos()[0] # 2 variant - узнаём x щелчка мыши
            y_mouse = pygame.mouse.get_pos()[1] # 2 variant - узнаём y щелчка мыши
            x_col = x_mouse//(size_block + margin) # узнаем номер квадрата по х (0,1 или 2)
            y_col = y_mouse//(size_block + margin) # узнаем номер квадрата по у (0,1 или 2)
            masClick[y_col][x_col]="x"
            if masClick[y_col][x_col] == masGreen[y_col][x_col]:
                kol=kol+1
                color = green
                x=x_col*size_block + (x_col + 1)*margin
                y=y_col*size_block + (y_col + 1)*margin
                pygame.draw.rect(screen,color,(x,y,size_block,size_block))
                pygame.display.update()
            query = query + 1
            
            if query == countGreen:
                print("Game over")
                print(masClick)
                game_over = True #в переменной будет храниться знак победителя
                rez1="Всего угадано клеток -       из"
                rez2=str(kol)
                rez3=str(query)
                screen.fill(green)
                font = pygame.font.SysFont(None, 60)
                text1 = font.render(str(rez1),True,yellow)
                text2 = font.render(str(rez2),True,yellow)
                text3 = font.render(str(rez3),True,yellow)
                text_rect = text1.get_rect()
                text_y = screen.get_height()/2 - text_rect.height/2 + 30
                screen.blit(text1, (15, text_y))
                screen.blit(text2, (510, text_y))
                screen.blit(text3, (640, text_y))
            else:
                game_over = False
    
    pygame.display.update()
