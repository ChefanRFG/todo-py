import pygame
import sys
pygame.init()

image = pygame.image.load("1.png")

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

image=pygame.transform.scale(image, (screen_width, screen_height))

screen.blit(image,(0,0))
pygame.display.flip()

font = pygame.font.SysFont(None, 24)
img = font.render("hola", True, "Black")
screen.blit(img, (20, 20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_q:
                image1 = pygame.image.load("2.png")
                screen.blit(image1,(0,0))
                pygame.display.update()

                image1=pygame.transform.scale(image1, (screen_width, screen_height))

    keys = pygame.key.get_pressed()



    if keys[pygame.K_a]:

        image2 =pygame.image.load("3.png")
        screen.blit(2,(0,0))
        pygame.display.update()

        image2=pygame.transform.escale(image2, (screen_width, screen_height))

