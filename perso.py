import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.Health = 100 
        self.Maxhealth = 100
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 300
