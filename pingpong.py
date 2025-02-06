import pygame


window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()
playerimg = pygame.image.load('player.png')
playerimg = pygame.transform.scale(playerimg,(100,100))

class GameObject():
    def __init__(self,x,y,img):
        self.rect = img.get_rect(center=((x,y)))
        self.speed = 3
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
        
        
player = Player(100,250,playerimg)

canplay = True
while canplay == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            canplay = False


    fps.tick(60)
    window.fill('white')
    window.blit(playerimg,player.rect)
    player.move()
    pygame.display.update()

