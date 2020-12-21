import pygame, random, time
from dataclasses import dataclass   
import PySimpleGUI as sg

a = 4

def countdown(a: int):
    '''Обратный отсчёт времени перед началом игры \n
    
    a - целое количество секунд, 
        меньшее 6, которые отсчитываются после нажатия клавиши "ПРОБЕЛ", до начала игры 
    '''    
    a = range(1, a+1)
    a = a[::-1]
    fontBIG = pygame.font.Font(None, 80)
    list = [fontBIG.render('0', True, [0, 0, 0]), fontBIG.render('1', True, [0, 0, 0]), fontBIG.render('2', True, [0, 0, 0]), fontBIG.render('3', True, [0, 0, 0]), fontBIG.render('4', True, [0, 0, 0]), fontBIG.render('5', True, [0, 0, 0])]
    for i in a:
        win.blit(list[i], (50, 50))
        win.blit(albert_Bg, (0,0))
        win.blit(text, textpos)
        win.blit(R_player, R_playerpos)
        win.blit(L_player, L_playerpos)
        win.blit(R_score[R], R_scorepos)
        win.blit(L_score[L], L_scorepos)
        win.blit(albert_wasd, (20, 400))
        win.blit(albert_arrows, (400, 400))
        win.blit(list[i], (235, 210))
        pygame.display.update()
        time.sleep(1)

def left_player(e):
    '''Добавление в память компьютера последние действия левого игрока \n
    
    e - значение из "pygame.KEYDOWN"
        полученное с помощью нажатия клавиши клавиатуры
    l - массив левого игрока,
        заполненный во время игры \n
    c - массив условия получения очка
    '''

    global l, c
    if e == pygame.K_w: #1 - вверх, 2 - вниз, 3 - влево, 4 - вправо
        l += [1]
        if l[len(l)-1] != c[len(l)-1]:
            l = []
    if e == pygame.K_s:
        l += [2]
        if l[len(l)-1] != c[len(l)-1]:
            l = []
    if e == pygame.K_a:
        l += [3]
        if l[len(l)-1] != c[len(l)-1]:
            l = []
    if e == pygame.K_d:
        l += [4]
        if l[len(l)-1] != c[len(l)-1]:
            l = []
    return l

def right_player(e):
    '''Добавление в память компьютера последние действия правого игрока \n
    
    e - значение из "pygame.KEYDOWN"
        полученное с помощью нажатия клавиши клавиатуры
    r - массив правого игрока,
        заполненный во время игры \n
    c - массив условия получения очка
    '''
    
    global r, c
    if e == pygame.K_UP: #1 - вверх, 2 - вниз, 3 - влево, 4 - вправо
        r += [1]
        if r[len(r)-1] != c[len(r)-1]:
            r = []
    if e == pygame.K_DOWN:
        r += [2]
        if r[len(r)-1] != c[len(r)-1]:
            r = []
    if e == pygame.K_LEFT:
        r += [3]
        if r[len(r)-1] != c[len(r)-1]:
            r = []
    if e == pygame.K_RIGHT:
        r += [4]
        if r[len(r)-1] != c[len(r)-1]:
            r = []
    return r



def block_creating(level):
    '''Создание платформ согласно уровню \n
    
    level - двумерный массив координат,
        некоторым из которых принадлежат блоки, пустые символы и вопросительный знак
    '''
    
    x=y=0 # координаты
    for i in level: # вся строка
        for j in i: # каждый символ
            if j=="-":
                    #создаем блок, заливаем его картинкой и рисуем его
                block=platform_image
                screen.blit(block,(x,y))
            if j=="?":
                gun=gun_image
                screen.blit(gun,(x,y)) 
                
            x+=level_platform_width #блоки платформы ставятся на ширине блоков
        y+=level_platform_height    #то же самое и с высотой
        x=0                   #на каждой новой строчке начинаем с нуля
@dataclass
class Jump:
    '''Класс системы прыжка \n
    
    self.isJump - буллевая переменная,
        определяющая активное положение персонажа (в прыжке или на земле) \n
    self.jump - ускорение изменения вертикальной скорости
    '''
    
    isJump: bool
    jump: float
    def update(self, isSpace, hero_y, dt):
        '''Определение правил прыжка \n
        
        isSpace - буллевая переменная,
            проверяющая нажатие клавиши "ПРОБЕЛ" \n
        hero_y - y-координата персонажа \n
        dt - обработка FPS
        '''
        if not(self.isJump):
            if isSpace:
                self.isJump=True     
                self.jump=0.5    
        else:
            hero_y-=self.jump*dt
            self.jump-=0.001*dt         
            if hero_y>win_height-150:    
                self.isJump=False
                self.jump=0   
        return hero_y



def texting():
    '''Проявление надписей'''
    win.blit(text,textscopes)
    win.blit(text2,(40,30))
    win.blit(text3,(40,50))

def lowSpeed():
    """
    Возможность снижения скорости персонажа,
        если он движется быстрее его изначальной скорости
    speed - скорость персонажа
    """
    global speed
    if speed > 5:
        speed -= 5

def drawWindow():
    """
    Заполнение экрана черным цветом и замена спрайта \n
    aimCount -  счётчик
        от 0 до 30  
    """
    global aimCount
    # после каждого перемещения нужно заполнять поле черным цветом    
    win.fill((0,0,0))
    # создание объекта
    if aimCount + 1 >= 30:
        aimCount = 0
    if left:
        win.blit(walk_left[aimCount // 5], (x, y))
        aimCount += 1
    elif right:
        win.blit(walk_right[aimCount // 5], (x, y))
        aimCount += 1
    else:
        win.blit(play_stand, (x, y))
    for bullet in bullets:
        bullet.draw(win)
    texting()

    pygame.display.update()

class snaryad():
    '''Класс, описывающий снаряд \n
        self.x - координата по Х \n
        self.y - координата по у \n
        self.r - радиус снаряда \n
        self.colour - цвет снаряда \n
        self.direction - направление движения снаряда (если direction = 1, то снаряд летит вправо, если direction = -1, то снаряд летит влево) \n
        self.bulletSpeed - скорость снаряда \n
        '''
    
    def __init__(self,x,y,r,colour,direction):
        '''Контсруктор класса snaryad'''
        
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour
        self.direction = direction
        self.bulletSpeed = 8 * direction

    def draw(self, win):
        '''Функция прорисовки снаряда
        
        win - игровое окно,
            на котором рисуется объект класса snaryad
        '''
        pygame.draw.circle(win,self.colour,(self.x,self.y),self.r)

    def movement(self, sec: float):
        '''Функция перемещения снаряда
        sec - нецелое количество секунд от последнего перемещения
        '''
        
        self.x += sec * self.bulletSpeed
        return self.x

def menu():
    sg.theme('DarkAmber')

    #win_launcher = pygame.display.set_mode((500, 500))
    #pygame.display.set_caption('Game Library')

    layout = [
        [sg.Text('Добро пожаловать в наш лаунчер!')],
        [sg.Text('Здесь вы можете выбрать игру на свой вкус: \n1 - Игра для двоих, 2 - Игра для любителей попрыгать, 3 - Игра про Трампа')],
        [sg.Text('Для того чтобы начать играть, нажмите на иконку игры')],
        [sg.Button(image_filename = 'Images/ИграАльберта.PNG', image_size=(450,100), key = 'firstGame')],
        [sg.Button(image_filename = 'Images/ИграКарена.PNG', image_size=(450,260), key = 'secondGame')],
        [sg.Button(image_filename = 'Images/ИграМихаила.PNG', image_size=(450,100), key = 'thirdGame')],
        [sg.Text('Если вы хотите поддержать наш проект, \nотправьте немного денег на этот счет: **********')],
        [sg.Button(button_text = 'Exit', key = 'Exit')]
    ]

    window = sg.Window('Выбор игры', layout)

    game = True
    global a
    while game:

        event, values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            a = 0
            break
        if event == 'Exit':
            a = 0
            break
        if event == 'firstGame':
            a = 1
            break
        if event == 'secondGame':
            a = 2
            break
        if event == 'thirdGame':
            a = 3
            break
    window.close()
    return a

if __name__ == "__main__":
    menu()
    if a == 1:
        
        pygame.init()

        win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('The fastest fingers in the world')

        #menu option
        albert_menu_Bg = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.menu.bg.jpg'), (500, 500))
            
        font00 = pygame.font.Font(None, 40)
        font01 = pygame.font.Font(None, 25)
        menu = True
        while menu:
            win.blit(albert_menu_Bg, (0,0))
            win.blit(font00.render('Добро пожаловать в игру', True, [0, 0, 0]), (70, 10))
            win.blit(font00.render('"Самые быстрые пальцы в мире"', True, [0, 0, 0]), (25, 40))
            win.blit(font01.render('Нажмите пробел для продолжения...', True, [0, 0, 0]), (90, 470))
            win.blit(font01.render('Если вы ошиблись, начинайте вводить символы заново', True, [0, 0, 0]), (5, 100))
            win.blit(font01.render('Обратите внимание, игра только для двух игроков!', True, [0, 0, 0]), (5, 120))
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    pygame.quit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu = False
        

        albert_p1 = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Up.png'), (80, 80))
        albert_p2 = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Down.png'), (80, 80))
        albert_p3 = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Left.png'), (80, 80))
        albert_p4 = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Right.png'), (80, 80))
        albert_Bg = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Bg.png'), (500, 500))
        albert_arrows = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.arrows.png'), (80, 80))
        albert_wasd = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.wasd.png'), (80, 80))

        x = [60, 160, 260, 360]
        y = 150

        L = 0
        R = 0
        c = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)] #condition

        #TEXT
        gameover = 0
        try:
            win.blit(albert_menu_Bg, (0,0))
        except pygame.error:
            gameover = 1
        if gameover != 1:
            font = pygame.font.Font(None, 40) #None - шрифт (мб потом добавлю)
            font2 = pygame.font.Font(None, 30)
            font3 = pygame.font.Font(None, 60)
            text = font.render('', True, [0, 0, 0])
            textpos = (93, 10)
            L_player = font2.render('PLAYER 1', True, [0, 0, 0])
            L_playerpos = (5, 70)
            R_player = font2.render('PLAYER 2', True, [0, 0, 0])
            R_playerpos = (400, 70)
            L_score = [font.render('0', True, [0, 0, 0]), font.render('1', True, [0, 0, 0]), font.render('2', True, [0, 0, 0]), font.render('3', True, [0, 0, 0]), font.render('4', True, [0, 0, 0]), font.render('5', True, [0, 0, 0])]
            L_scorepos = (30, 100)
            R_score = [font.render('0', True, [0, 0, 0]), font.render('1', True, [0, 0, 0]), font.render('2', True, [0, 0, 0]), font.render('3', True, [0, 0, 0]), font.render('4', True, [0, 0, 0]), font.render('5', True, [0, 0, 0])]
            R_scorepos = (455, 100)
            vic1 = font3.render('1`ST PLAYER WINS!!!', True, [0, 255, 0])
            vic2 = font3.render('2`ND PLAYER WINS!!!', True, [0, 255, 0])
            vicpos = (30, 150)

            countdown(5)
            l = []
            r = []    
            game = True
            while game:
                win.blit(albert_Bg, (0,0))
                win.blit(text, textpos)
                win.blit(R_player, R_playerpos)
                win.blit(L_player, L_playerpos)
                win.blit(R_score[R], R_scorepos)
                win.blit(L_score[L], L_scorepos)
                win.blit(albert_wasd, (20, 400))
                win.blit(albert_arrows, (400, 400))
                for i in range(4):
                    if c[i] == 1:
                        win.blit(albert_p1, (x[i], y))
                    elif c[i] == 2:
                        win.blit(albert_p2, (x[i], y))
                    elif c[i] == 3:
                        win.blit(albert_p3, (x[i], y))
                    else:
                        win.blit(albert_p4, (x[i], y))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game = False

                    elif event.type == pygame.KEYDOWN:
                        left_player(event.key)
                        right_player(event.key)
                if len(l) == 4:
                    if l == c:
                        L += 1
                        c = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)]
                        text = font.render('Last Winner is Player1!', True, [0, 0, 0])
                        r = []
                        l = []
                        if L == 5:
                            win.blit(albert_Bg, (0,0))
                            win.blit(R_player, R_playerpos)
                            win.blit(L_player, L_playerpos)
                            win.blit(L_score[L], L_scorepos)
                            win.blit(R_score[R], R_scorepos)
                            win.blit(vic1, vicpos)
                            pygame.display.update()
                            time.sleep(4)
                            game = False
                    else:
                        l = []
                if len(r) == 4:
                    if r == c:
                        R += 1
                        if R == 5:
                            game = False
                        c = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)]
                        text = font.render('Last Winner is Player2!', True, [0, 0, 0])
                        r = []
                        l = []
                        if R == 5:
                            win.blit(albert_Bg, (0,0))
                            win.blit(L_score[L], L_scorepos)
                            win.blit(vic2, vicpos)
                            win.blit(R_score[R], R_scorepos)
                            pygame.display.update()
                            time.sleep(5)
                            game = False
                    else:
                        r = []
            pygame.quit()
        else:
            pygame.quit()



    elif a == 2:
        import pygame #импорт библиотеки
        from dataclasses import dataclass 
        pygame.init()
        win_width=800 #ширина окна
        win_height=600 #высота окна
        fps=60
        display=(win_width,win_height) #размеры окна
        background=(255, 0, 0)
        hero_x=0#координата х персонажа
        hero_y=450 #координата y персонажа
        hero_speed=0.2 #скорость персонажа
        hero_image_number=0
        isJump=False #переменные для создания прыжка 
        jump=0
        dt=0
        gun_width=40 
        gun_height=15
        font=pygame.font.SysFont('arial', 32)
        follow=font.render('☺ Find the way out ☺', 1, (255,0,0))
        #переменные для создания уровня
        level_platform_width=32
        level_platform_height=32
        clock=pygame.time.Clock() #управляющая кадрами в секунду
        game_over=False #конец игры    
        screen=pygame.display.set_mode((display)) #устанавливаем размер экрана
        pygame.display.set_caption("Supernatural Game") #даем название игры
        icon=pygame.image.load("SpritesKaren/icon.png")
        pygame.display.set_icon(icon) #установка иконы игры
        platform_image=pygame.transform.scale(pygame.image.load('SpritesKaren/kblocks.png'),(level_platform_width, level_platform_height) )
        gun_image=pygame.transform.scale(pygame.image.load('SpritesKaren/gunone.png'),(gun_width, gun_height) )
        hero_image=pygame.image.load("SpritesKaren/dean1.2.png") #загрузка картинки персонажа
        hero_images_right=[pygame.image.load("SpritesKaren/dean1.4.png"), pygame.image.load("SpritesKaren/dean1.8.png"),pygame.image.load("SpritesKaren/dean1.9.png")]
        hero_images_left=[pygame.image.load("SpritesKaren/dean1.5.png"),pygame.image.load("SpritesKaren/dean1.6.png"),pygame.image.load("SpritesKaren/dean1.7.png")]
        background_image=pygame.image.load("SpritesKaren/background.png") #загружаем фон
        level = [
                "                         ",
                "                         ",                  
                " ---  - -  - --  --  --  ",
                "  -   - -  ----  -   --  ",
                " -    ---  -     --  - -",
                "                         ",
                "                         ",
                "-------------------  ----",
                "                         ", 
                "              ---------- ",     
                "          ----           ",
                "                         ",
                "  -----------        ?   ",
                "                         ",
                "                         ",
                "             -----       ",
                "     -----               ",]
        
        jumping=Jump(False,0)                  

        while not game_over:
            '''Creates the game cycle'''
            for event in pygame.event.get(): #смотрим каждое событие из списка всех событий
                if event.type==pygame.QUIT or ((hero_x>=620 and hero_x<=700) and (hero_y>=300 and hero_y<=350)): #проверяем, является ли тип события типом выхода из игры (событие:конец игры)
                    game_over=True
                    break
            screen.blit(background_image,(0,0))
            screen.blit(follow,(0,0))
            block_creating(level)
            keys=pygame.key.get_pressed() #список нажатых клавиш клавиатуры
            if keys[pygame.K_RIGHT] and hero_x<win_width-80: #перемещение персонажа вправо
                hero_x+=hero_speed*dt
                hero_image_number+=1
                screen.blit(hero_images_right[hero_image_number//21],(hero_x,hero_y))
            elif keys[pygame.K_LEFT] and hero_x>0: #перемещение персонажа влево
                hero_x-=hero_speed*dt 
                hero_image_number+=1
                screen.blit(hero_images_left[hero_image_number//21],(hero_x,hero_y))
            else:
                hero_image_number=0  
                screen.blit(hero_image,(hero_x,hero_y))
            hero_y=jumping.update(keys[pygame.K_SPACE], hero_y, dt)
            if hero_image_number>fps-1:
                hero_image_number=0    
                    #расположение персонажа в соответсвии с координатами
            pygame.display.update() #обновляем окно 
            dt=clock.tick(fps) #рисуются 60 кадров в секунду    
        pygame.quit()





    elif a == 3:
        pygame.init()
        # создаем игровое окно
        win = pygame.display.set_mode((1000,700))
        # заголовок
        pygame.display.set_caption("Игра на питоне")

        font = pygame.font.Font(None,20)
        text = font.render('Hello! This is my first game! Here are some feachers:', True, [255,255,255])
        textscopes = (40,10)
        text2 = font.render('You are able to move with these bottoms ( <-  ^  -> )', True, [255,255,255])
        text3 = font.render('Also it is possible to run with (SHIFT) and shoot with bottom (F)', True, [255,255,255])

        # добавление спрайтов
        walk_right = [pygame.image.load('Sprites/pygame_right_1.png'),
        pygame.image.load('Sprites/pygame_right_2.png'),pygame.image.load('Sprites/pygame_right_3.png'),
        pygame.image.load('Sprites/pygame_right_4.png'),pygame.image.load('Sprites/pygame_right_5.png'),
        pygame.image.load('Sprites/pygame_right_6.png')]

        walk_left = [pygame.image.load('Sprites/pygame_left_1.png'),
        pygame.image.load('Sprites/pygame_left_2.png'),pygame.image.load('Sprites/pygame_left_3.png'),
        pygame.image.load('Sprites/pygame_left_4.png'),pygame.image.load('Sprites/pygame_left_5.png'),
        pygame.image.load('Sprites/pygame_left_6.png')]

        play_stand = pygame.image.load('Sprites/pygame_idle.png')
        clock = pygame.time.Clock()
        

        #параметры
        x = 50
        y = 700 - 76
        width = 60
        height = 71
        speed = 5
        speedCount = 10

        isJump = False
        jumpCount = 10
        aimCount = 0

        right = False
        left = False

        bullets : list = []
        lastMove = 'right'
        direction = 1
        #coolDown = 0

        WHITE = (255, 255, 255)
        RED = (225, 0, 50)
        GREEN = (0, 225, 0)
        BLUE = (0, 0, 225)

        # цикл самой игры
        run = True
        while run:
            # время через которое цикл будет обновляться
            clock.tick(30)

            # Перемещение патрона
            for bullet in bullets:
                if bullet.x < 1000 and bullet.x > 0:
                    bullet.x += bullet.bulletSpeed
                else:
                    bullets.pop(bullets.index(bullet))

            # опишем структуру выхода из программы
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # отслеживание нажатий 
            keys = pygame.key.get_pressed()

            # определение последнего направления
            if lastMove == 'right':
                direction = 1
            else:
                direction = -1

            # запуск снаряда
            if keys[pygame.K_f]:
                bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 5, RED, direction))

                    
            # управление персонажем
            if keys[pygame.K_LSHIFT]:
                speed += 5
            if keys[pygame.K_LEFT] and x > 5:
                x -= speed
                left = True
                right = False
                lastMove = 'left'
            elif keys[pygame.K_RIGHT] and x < 1000 - width - 5:
                x += speed
                left = False
                right = True
                lastMove = 'right'
            else:
                left = False
                right = False
                aimCount = 0
            if not(isJump):
                if keys[pygame.K_UP]:
                    isJump = True
            else:
                if jumpCount >= -10:
                    if jumpCount < 0:
                        y += (jumpCount ** 2) / 2
                    else:
                        y -= (jumpCount ** 2) / 2
                    jumpCount -= 1
                else:
                    isJump = False
                    jumpCount = 10
            lowSpeed()
            drawWindow()

        pygame.quit()