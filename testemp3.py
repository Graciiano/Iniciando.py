import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("ex001.mp3")
sound.set_volume(0.5)
sound.play() 
                  