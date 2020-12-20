import pygame

class object:
    def __init__(self):
        self.x : float = 40
        self.y : float = 460
        self.r : float = 5
        self.colour = (225,50,50)
        self.speed_x : float = 0.5
        self.speed_y : float = 0.25

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
    Ball = object()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        Ball.hitWall()
        Ball.movement()
        windraw()

    pygame.quit()
