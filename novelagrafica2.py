import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Toma de Decisiones")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

font = pygame.font.Font(None, 36)

MENU = 0
DECISION = 1
RESULTADO = 2

estado_juego = MENU

img_1 = pygame.image.load("png_1")
img_2 = pygame.image.load("png_2")
img_3 = pygame.image.load("png_3")
img_4 = pygame.image.load("png_4")
img_5 = pygame.image.load("png_5")
img_6 = pygame.image.load("png_6")
img_7 = pygame.image.load("png_7")
img_8 = pygame.image.load("png_8")
img_9 = pygame.image.load("png_9")
img_10 = pygame.image.load("png_10")
img_11 = pygame.image.load("png_11")
img_12 = pygame.image.load("png_12")
img_13 = pygame.image.load("png_13")
img_14 = pygame.image.load("img_14")