import pygame
import time
import random

pygame.init()# инииализация экрана в начале кода

white = (255, 255, 255)# цвета и сопутствующие значения RGB
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600 #ширина окна(dis- значит "display"-дисплей, показ,экран, окно, игр.поле)
dis_height = 400 # высота окна

dis = pygame.display.set_mode((dis_width, dis_height))# создаёт окно с параметрами ширины и высоты)
pygame.display.set_caption('Snake Game by Tatiana')# создаёт заголовок экрана

clock = pygame.time.Clock()#делает на более быстрых компьютерах более продолжительную паузу, чем на медленных

snake_block = 10 #стандартная величина (клетка) сдвига положения змейки при нажатии на клавишу
snake_speed = 3 # скорость змейки

font_style = pygame.font.SysFont("bahnschrift", 25) # шрифт и размер шрифта для системных сообщений, например при  завершении иры
score_font = pygame.font.SysFont("comicsansms", 35) # # шрифт и размер шрифта счёта


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue) # функция выводит счёт(score)
    dis.blit(value, [0, 0])#blit указывает, что value будет написано на dis (то есть окне)


def our_snake(snake_block, snake_list): # функция нарисует змейку
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]) # змейка в виде зелёного 4угольника(клетки)


def message(msg, color):# создаём функцию, которая будет показывать сообщения на игр. экране
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop(): # описываем всю игровую логику в этой функции
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []# создаём список, в котором будем хранить показатель текущей длины змейки
    Length_of_snake = 1 # длина змейки

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # создаём переменную, которая будет указывать расположение еды по оси х
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 # то же самое по оси y

    while not game_over:

        while game_close == True: # Если змейка сталкивается с собственным хвостом, то игра выводит сообщение (строка64)
            dis.fill(white) # нанесение на окно белого фона
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1) # отнимаем саму длину змейки
            pygame.display.update() # метод для применения каких-либо изменений на экране

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: # события из класса КEYDOWN
                    if event.key == pygame.K_q: # если нажата клавиша q, то
                        game_over = True # игра закончена
                        game_close = False
                    if event.key == pygame.K_c: # если нажата клавиша с, то
                        gameLoop() # играем снова (запускается эта функция)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # если нажмем на знак "выход" то
                game_over = True # игра будет закончена
            if event.type == pygame.KEYDOWN:# события из класса КEYDOWN:
                if event.key == pygame.K_LEFT: #  если нажата клавиша влево, то
                    x1_change = -snake_block # змея передвинется на 1 стандартную величину влево по оси х
                    y1_change = 0 # по оси у нет изменений
                elif event.key == pygame.K_RIGHT: #  если нажата клавиша вправо, то
                    x1_change = snake_block # змея передвинется на 1 стандартную величину вправо по оси х
                    y1_change = 0 # по оси у нет изменений
                elif event.key == pygame.K_UP: #  если нажата клавиша вверх, то
                    y1_change = -snake_block # змея передвинется на 1 стандартную величину вверх по оси у
                    x1_change = 0 # по оси х нет изменений
                elif event.key == pygame.K_DOWN: #  если нажата клавиша вниз, то
                    y1_change = snake_block # змея передвинется на 1 стандартную величину вниз по оси у
                    x1_change = 0 # по оси х нет изменений

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: # если координаты змейки выходят за рамки игр. поля, то ира должна закончиться
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(red) # нанесение на окно красного фона
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block]) # рисуем прямоугольник, который выражает еду змейки
        snake_Head = [] # создаём список, который будет хранить показатель длины змейки при движении
        snake_Head.append(x1) # добавляем значения в список при изменении по оси х
        snake_Head.append(y1) # добавляем значения в список при изменении по оси у
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake: # если показатель текущей длины змейки больше длины змейки:
            del snake_List[0] # удаляем первый элемент в списке, чтобы длина не увеличивалась сама по себе при движении

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update() # применяем метод изменений на экране

        if x1 == foodx and y1 == foody: # указываем, что  если координаты змейки совпадают с координатами еды, еда появляется в новом месте ,а длина змейки увеличивается на 1 клетку
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1


        clock.tick(snake_speed) # не даёт программе работать быстрее в секунду, чем число-аргумент snake_speed

    pygame.quit() # quit-метод закрытия экрана
    quit()


gameLoop()
