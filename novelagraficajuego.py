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

def dibujar_menu():
    screen.fill(BLANCO)
    texto = font.render("Presiona el ESPACIO para empezar", True, NEGRO)
    screen.blit(texto, (200, 300))

def dibujar_menu1():
    image = pygame.image.load("1.png")
    screen.blit(image, (0,0))
    pygame.display.update()
    texto = font.render("Apareces en una cueva solitaria...", True, BLANCO)
    screen.blit(texto, (200, 300))

def dibujar_decision():
    screen.fill(NEGRO)
    opcion1 = font.render("1. Ir a la ciudad", True, BLANCO)
    opcion2 = font.render("2. Ir al bosque", True, BLANCO)
    screen.blit(opcion1, (100, 200))
    screen.blit(opcion2, (100, 300))

def dibujar_resultado(resultado):
    screen.fill(NEGRO)
    texto = font.render(resultado, True, BLANCO)
    screen.blit(texto, (200, 300))

corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        elif event.type == pygame.KEYDOWN:
            if estado_juego == MENU:
                if event.key == pygame.K_SPACE:
                    estado_juego = DECISION
            elif estado_juego == DECISION:
                if event.key == pygame.K_1:
                    resultado = "Llegaste a la ciudad, te encuentras un puesto de comida, deseas comerlo?"
                    estado_juego = RESULTADO
                elif event.key == pygame.K_2:
                    resultado = "Te perdiste atraves del vacio, quieres buscar el camino a la ciudad?"
                    estado_juego = RESULTADO
                    break
    dibujar_menu1()

def dibujar_decision():
    screen.fill(NEGRO)
    opcion3 = font.render("1. Comer la comida del puesto", True, BLANCO)
    opcion4 = font.render("2. Seguir el camino por las catacumbas", True, BLANCO)
    opcion5 = font.render("3. Buscar el camino a la ciudad", True, BLANCO)
    opcion6 = font.render("4. Buscar una salida", True, BLANCO)

    if estado_juego == MENU:
        dibujar_menu()
    elif estado_juego == DECISION:
        dibujar_decision()
    elif estado_juego == RESULTADO:
        dibujar_resultado(resultado)

    pygame.display.flip()

pygame.quit()
sys.exit()