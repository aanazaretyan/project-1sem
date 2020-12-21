import pygame

class objectq:
    def __init__(self,x,y,colour,speed_x,speed_y):
        self.x : float = x
        self.y : float = y
        self.r : float = 5
        self.colour = colour
        self.speed_x : float = speed_x
        self.speed_y : float = speed_y

    def draw(self, win):
        pygame.draw.circle(win,self.colour,(self.x,self.y),self.r)

    def hitWall(self):
        if self.x + self.r == 500.0:
            self.speed_x *= -1.0
        if self.x - self.r == 0.0:
            self.speed_x *= -1.0
        if self.y + self.r == 500.0:
            self.speed_y *= -1.0
        if self.y - self.r == 0.0:
            self.speed_y *= -1.0

    def movement(self):
        self.x -= self.speed_x
        self.y -= self.speed_y

def windraw():
    win.fill((255,255,255))
    Ball.draw(win)
    pygame.display.update()

if __name__=='__main__':

    pygame.init()
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Игра для тестов")
    win.fill((255,255,255))
    Ball = objectq(40.0,460.0,(255,0,50),0.5,0.5)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        Ball.hitWall()
        Ball.movement()
        windraw()

    pygame.quit()
