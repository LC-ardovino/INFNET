#Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), toda vez que a tecla espaço for pressionada ou o botão direito for clicado.


import pygame, random

pygame.init()


def quadrado():
    cor = amarelo
    area = (random.randint(10, largura_tela - 30), random.randint(10, altura_tela - 30), 50, 50)
    pygame.draw.rect(tela, cor, area)


largura_tela = 800
altura_tela = 600
amarelo = (255, 255, 0)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Mostra quadrados(clique espaço)')

terminou = False
clock = pygame.time.Clock()

while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                quadrado()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[2]:
                quadrado()

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()

pygame.quit()