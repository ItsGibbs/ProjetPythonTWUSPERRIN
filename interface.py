import pygame
from game import Game
pygame.init()


pygame.display.set_caption("Jeu d'insulte") # création du titre de l'interface
screen = pygame.display.set_mode((960,540)) #création de l'interface
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
background = pygame.image.load('Image/Bar.gif') #charger une image

# game = Game()

running = True

while running:

    screen.blit(background,(0,0)) #mettre l'image sur l'interface

#     interface.blit(game.player.image, game.player.rect)

    pygame.display.flip() #mettre a jour l'interface avec l'image

    for event in pygame.event.get():
        # pour la fermeture de l'interface de jeu
        if event.type == pygame.quit:
            running = False
            pygame.quit()

