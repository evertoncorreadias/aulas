import pygame

pygame.init()
pygame.mixer.music.load('sino.mp3')
pygame.mixer.music.play()
pygame.event.wait()