import pygame, random, time
pygame.init()

winx = 500
winy = 500
win = pygame.display.set_mode((winx, winy))
pygame.display.set_caption('The fastest finger in the world')

p1 = pygame.transform.scale(pygame.image.load('Up.png'), ((15 * winx) // 100, (15 * winy) // 100))
p2 = pygame.transform.scale(pygame.image.load('Down.png'), ((15 * winx) // 100, (15 * winy) // 100))
p3 = pygame.transform.scale(pygame.image.load('Left.png'), ((15 * winx) // 100, (15 * winy) // 100))
p4 = pygame.transform.scale(pygame.image.load('Right.png'), ((15 * winx) // 100, (15 * winy) // 100))
Bg = pygame.transform.scale(pygame.image.load('Bg.png'), (winx, winy))

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
    win.blit(Bg, (0,0))
    win.blit(text, textpos)
    win.blit(L_score[L], L_scorepos)
    win.blit(R_score[R], R_scorepos)
    for i in range(4):
        if c[i] == 1:
            win.blit(p1, (x[i], y))
        elif c[i] == 2:
            win.blit(p2, (x[i], y))
        elif c[i] == 3:
            win.blit(p3, (x[i], y))
        else:
            win.blit(p4, (x[i], y))
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
                win.blit(Bg, (0,0))
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
                win.blit(Bg, (0,0))
                win.blit(L_score[L], L_scorepos)
                win.blit(vic2, vicpos)
                win.blit(R_score[R], R_scorepos)
                pygame.display.update()
                time.sleep(5)
                game = False
        else:
            r = []
pygame.quit()































import pygame #импорт библиотеки
from dataclasses import dataclass 
pygame.init()
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
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon) #установка иконы игры
hero_image=pygame.image.load("dean1.2.png") #загрузка картинки персонажа
hero_images_right=[pygame.image.load("dean1.4.png"), pygame.image.load("dean1.8.png"),pygame.image.load("dean1.9.png")]
hero_images_left=[pygame.image.load("dean1.5.png"),pygame.image.load("dean1.6.png"),pygame.image.load("dean1.7.png")]
background_image=pygame.image.load("background.png") #загружаем фон
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
