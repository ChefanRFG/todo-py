import pygame
import sys

pygame.init()

screen_width = 740
screen_height = 580
screen = pygame.display.set_mode((screen_width, screen_height))

pantalla_inicial = image1 = pygame.image.load("1.png")
image1 = pygame.transform.scale(image1, (screen_width, screen_height))

pantalla2 = image2 = pygame.image.load("2.png")
image2 = pygame.transform.scale(image2, (screen_width, screen_height))

pantalla3 = image3 = pygame.image.load("3.png")
image3 = pygame.transform.scale(image3, (screen_width, screen_height))

running = True

while running:
    if screen == "pantalla_inicial":
        screen.blit(image1, (0, 0))
        pygame.display.flip()

        font = pygame.font.SysFont(None, 24)
        text_img = font.render("Te despiertas de la caida, sientes frio", True, "Gray")
        screen.blit(text_img, (40, 40))
        pygame.display.flip()
        if screen == "pantalla2":

        current_image = image1
        if screen.type == pygame.QUIT:
               running = False
        if screen.type == pygame.KEYDOWN:
            if screen.key == pygame.K_q:
                current_image2 = image2
            if screen.key == pygame.K_a:
                current_image3 = image3

    screen.blit(text_img, (20, 20))
    pygame.display.flip()


pygame.quit()
sys.exit()
