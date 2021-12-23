#iniciando a tela.
import random
import pygame
pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela,altura_tela))
clock = pygame.time.Clock()
quadrados_iniciais = 20
terminou = False
preto = (0, 0, 0)
branco = (255, 255, 255)
pontos = 0

class Quadradinhos():
    def __init__(self):
        self.largura = 30
        self.altura = 30
        self.x = random.randint(0, largura_tela-self.largura)
        self.y = random.randint(0, altura_tela-self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (random.randint(20,255), random.randint(20,255), random.randint(20,255))
    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

def mostra_tempo(tempo,pontos):
    fonte = pygame.font.Font(None, 24)
    text = fonte.render("Tempo: " + str(tempo) + "s",f'Pontuação:{pontos}', 1, branco)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)
def mostra_pontuação_final(tela,pontos):
    tela.fill(preto)
    font = pygame.font.Font(None,36)
    text = font.render(f"Pontuação:{str(pontos)} quadradinhos",1,branco)
    textpos = text.get_rect(center=(tela.get_width() / 2, tela.get_height() / 2))
    tela.blit(text, textpos)

lista = []
for i in range(0,quadrados_iniciais):
    q = Quadradinhos()
    q.desenha(tela)
    lista.append(q)


while not terminou:
    pontos = 0
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for q in lista:
                if q.area.collidepoint(pos):
                    lista.remove(q)
                    pontos = pontos + 1

        if event.type == pygame.QUIT:
            terminou = True
    conta_clocks = 0
    conta_segundos = 5
    conta_clocks = conta_clocks+1
    if conta_clocks ==50:
        if conta_segundos >= 0:
            conta_segundos =conta_segundos - 1
        conta_clocks = 0
        q = Quadradinhos()
        lista.append(q)

    if conta_segundos >= 0:
        tela.fill(preto)

        for i in lista:
            i.desenha(tela)

        mostra_tempo(conta_segundos,pontos)
    else:

        mostra_pontuação_final(tela, pontos)

        for q in lista:
            lista.remove(q)





    pygame.display.update()

    clock.tick(50)
pygame.display.quit()
pygame.quit()


pygame.quit()