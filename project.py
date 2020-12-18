import pygame, random, time
import PySimpleGUI as sg

sg.theme('DarkAmber')

pygame.init()
#PySimpleGUI.init()

#win_launcher = pygame.display.set_mode((500, 500))
#pygame.display.set_caption('Game Library')

layout = [
    [sg.Button('Игра Альбера')],
    [sg.Button('Игра Карена')],
    [sg.Button('Игра Михаила')],
    [sg.Output(size=(100, 20))]
]

window = sg.Window('Выбор игры', layout)

game = True
a = 0
while game:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False 
        elif keys[pygame.K_1]:
            a = 1
            game = False
        elif keys[pygame.K_2]:
            a = 2
            game = False
        elif keys[pygame.K_3]:
            a = 3
            game = False

    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Игра Альбера':
        a = 1
        game = False
    if event == 'Игра Карена':
        a = 2
        game = False
    if event == 'Игра Михаила':
        a = 3
        game = False

if a == 1:
    winx = 500
    winy = 500
    win = pygame.display.set_mode((winx, winy))
    pygame.display.set_caption('The fastest finger in the world')


    albert_p1 = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Up.png'), ((15 * winx) // 100, (15 * winy) // 100))
    albert_p2 = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Down.png'), ((15 * winx) // 100, (15 * winy) // 100))
    albert_p3 = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Left.png'), ((15 * winx) // 100, (15 * winy) // 100))
    albert_p4 = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Right.png'), ((15 * winx) // 100, (15 * winy) // 100))
    albert_Bg = pygame.transform.scale(pygame.image.load('SpritesAlbert/albert.Bg.png'), (winx, winy))

    x = [(10 * winx) // 100, (32 * winx) // 100, (53 * winx) // 100, (74 * winx) // 100]
    y = (32 * winy) // 100

    l = []
    L = 0
    r = []
    R = 0
    c = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)] #condition

    #TEXT
    font = pygame.font.Font(None, 40) #None - шрифт (мб потом добавлю)
    text = font.render('', True, [0, 0, 0])
    textpos = (80, 10)
    L_score = [font.render('0', True, [0, 0, 0]), font.render('1', True, [0, 0, 0]), font.render('2', True, [0, 0, 0]), font.render('3', True, [0, 0, 0]), font.render('4', True, [0, 0, 0]), font.render('5', True, [0, 0, 0])]
    L_scorepos = (10, 70)
    R_score = [font.render('0', True, [0, 0, 0]), font.render('1', True, [0, 0, 0]), font.render('2', True, [0, 0, 0]), font.render('3', True, [0, 0, 0]), font.render('4', True, [0, 0, 0]), font.render('5', True, [0, 0, 0])]
    R_scorepos = (445, 70)
    font2 = pygame.font.Font(None, 60)
    vic1 = font2.render('1`ST PLAYER WINS!!!', True, [0, 255, 0])
    vic2 = font2.render('2`ND PLAYER WINS!!!', True, [0, 255, 0])
    vicpos = (20, 150)




    game = True
    while game:
        win.blit(albert_Bg, (0,0))
        win.blit(text, textpos)
        win.blit(L_score[L], L_scorepos)
        win.blit(R_score[R], R_scorepos)
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
                if event.key == pygame.K_w: #1 - вверх, 2 - вниз, 3 - влево, 4 - вправо
                    l += [1]
                    if l[len(l)-1] != c[len(l)-1]:
                        l = []
                if event.key == pygame.K_s:
                    l += [2]
                    if l[len(l)-1] != c[len(l)-1]:
                        l = []
                if event.key == pygame.K_a:
                    l += [3]
                    if l[len(l)-1] != c[len(l)-1]:
                        l = []
                if event.key == pygame.K_d:
                    l += [4]
                    if l[len(l)-1] != c[len(l)-1]:
                        l = []
                if event.key == pygame.K_UP: #1 - вверх, 2 - вниз, 3 - влево, 4 - вправо
                    r += [1]
                    if r[len(r)-1] != c[len(r)-1]:
                        r = []
                if event.key == pygame.K_DOWN:
                    r += [2]
                    if r[len(r)-1] != c[len(r)-1]:
                        r = []
                if event.key == pygame.K_LEFT:
                    r += [3]
                    if r[len(r)-1] != c[len(r)-1]:
                        r = []
                if event.key == pygame.K_RIGHT:
                    r += [4]
                    if r[len(r)-1] != c[len(r)-1]:
                        r = []
        if len(l) == 4:
            if l == c:
                L += 1
                c = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)]
                text = font.render('Last Winner is Player1!', True, [0, 0, 0])
                r = []
                l = []
                if L == 5:
                    win.blit(albert_Bg, (0,0))
                    win.blit(L_score[L], L_scorepos)
                    win.blit(vic1, vicpos)
                    win.blit(R_score[R], R_scorepos)
                    pygame.display.update()
                    time.sleep(5)
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



elif a == 2:
    from dataclasses import dataclass 
    win_width=800 #ширина окна
    win_height=600 #высота окна
    fps=60
    display=(win_width,win_height) #размеры окна
    background=(255, 0, 0)
    hero_x=0 #координата х персонажа
    hero_y=450 #координата y персонажа
    hero_speed=0.2 #скорость персонажа
    hero_image_number=0
    isJump=False
    jump=0
    dt=0
    #переменные для создания уровня
    level_platform_wight=32
    level_platform_height=32
    platform_color="#B22222"
    clock=pygame.time.Clock() #управляющая кадрами в секунду
    game_over=False #конец игры    
    screen=pygame.display.set_mode((display)) #устанавливаем размер экрана
    pygame.display.set_caption("Supernatural Quest") #даем название игры
    icon=pygame.image.load("SpritesKaren/icon.png")
    pygame.display.set_icon(icon) #установка иконы игры
    hero_image=pygame.image.load("SpritesKaren/dean1.2.png") #загрузка картинки персонажа
    hero_images_right=[pygame.image.load("SpritesKaren/dean1.4.png"), pygame.image.load("SpritesKaren/dean1.8.png"),pygame.image.load("SpritesKaren/dean1.9.png")]
    hero_images_left=[pygame.image.load("SpritesKaren/dean1.5.png"),pygame.image.load("SpritesKaren/dean1.6.png"),pygame.image.load("SpritesKaren/dean1.7.png")]
    background_image=pygame.image.load("SpritesKaren/background.png") #загружаем фон
    level = [
            "                         ",
            "                         ",
            "                         ",
            "                         ",
            "                         ",
            "                         ",
            "                         ",
            "                         ", 
            "                         ",     
            "          ----           ",
            "                         ",
            "  -----------            ",
            "                         ",
            "                         ",
            "             -----       ",
            "     -----               ",]
    def blockcreating(level):
        x=y=0 # координаты
        for i in level: # вся строка
            for j in i: # каждый символ
                if j=="-":
                        #создаем блок, заливаем его цветом и рисуем его
                    block = pygame.Surface((level_platform_wight,level_platform_height))
                    block.fill(pygame.Color(platform_color))
                    screen.blit(block,(x,y))
                x+=level_platform_wight #блоки платформы ставятся на ширине блоков
            y+=level_platform_height    #то же самое и с высотой
            x=0                   #на каждой новой строчке начинаем с нуля
    @dataclass
    class Jump:
        isJump:bool
        jump:float
        def update(self,isSpace,hero_y,dt):
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
    jumping=Jump(False,0)                  

    while not game_over:
        for event in pygame.event.get(): #смотрим каждое событие из списка всех событий
            if event.type==pygame.QUIT: #проверяем, является ли тип события типом выхода из игры (событие:конец игры)
                game_over=True
                break
        screen.blit(background_image,(0,0))
        blockcreating(level)
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
    # создаем игровое окно
    win = pygame.display.set_mode((1000,700))
    # заголовок
    pygame.display.set_caption("Игра на питоне")

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

    class snaryad():
        def __init__(self,x,y,r,colour,direction):
            self.x = x
            self.y = y
            self.r = r
            self.colour = colour
            self.direction = direction
            self.bulletSpeed = 8 * direction

        def draw(self, win):
            pygame.draw.circle(win,self.colour,(self.x,self.y),self.r)

    clock = pygame.time.Clock()

    def lowSpeed():
        """
        def lowspeed() позволяет персонажу снизить скорость,
            если он движется бустрее его изначальной скорости
        """
        global speed
        if speed > 5:
            speed -= 5

    def drawWindow():
        """
        def drawWindow() заполняет экран черным цветом и меняет спрайт в зависимости от переменной aimCount    
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

        pygame.display.update()

    #параметры
    x = 50
    y : float = 700 - 76
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
            if len(bullets) < 10:
                    bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 
                    5, RED, direction))

                
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

        
    # на случай если программа не вышла прописываем функцию выхода еще раз
    pygame.quit()

else:
    pygame.quit()