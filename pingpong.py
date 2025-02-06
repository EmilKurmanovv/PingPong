import pygame


window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()
playerimg = pygame.image.load('player.png')
playerimg = pygame.transform.scale(playerimg,(100,100))
ballimg = pygame.image.load('ball.png')
ballimg = pygame.transform.scale(ballimg,(50,50))


class GameObject():
    def __init__(self,x,y,img):
        self.rect = img.get_rect(center=((x,y)))
        self.speed = 3
        self.speedx = self.speed
        self.speedy = self.speed
class Player(GameObject):
    def move(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.bottom > 500:
            self.rect.bottom = 500

        keylist = pygame.key.get_pressed()
        if keylist[pygame.K_w]:
            self.rect.y -= self.speed
        if keylist[pygame.K_s]:
            self.rect.y += self.speed
        
class Ball(GameObject):
    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom <= 500:
            self.speedy = -self.speedy
        if self.rect.top >= 0:
            self.speedy = -self.speedy
        if self.rect.left <= 0:
            self.speedx = -self.speedx
            self.rect.center = (350,250)
        if self.rect.right >= 700:
            self.speedx = -self.speedx
            self.rect.center = (350,250)
        

player = Player(100,250,playerimg)
ball = Ball(350,250,ballimg)

canplay = True
while canplay == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            canplay = False


    fps.tick(60)
    window.fill('white')
    window.blit(playerimg,player.rect)
    player.move()
    window.blit(ballimg,ball.rect)
    ball.move()
    pygame.display.update()

