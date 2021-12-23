import pygame, sys
from pygame.locals import *


largura_tela = 400
altura_tela = 300
FPS = 200
largura_linha = 10
paleta_tamanho = 50
PALETAOFFSET = 20
preto = (0,0,0)
branco = (255,255,255)

def desenhaPlacar(placar):
    resultadoSurf = BASICFONT.render('placar = %s' %(placar), True, branco)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (largura_tela - 150, 25)
    DISPLAYSURF.blit(resultadoSurf, resultadoRect)

def verificaPlacar(paleta1,bola,placar,bolaDirx):
    if bola.left == largura_linha:
        return 0
    elif bola.right == largura_tela - largura_linha:
        placar += 10
        return placar
    elif bolaDirx == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += 1
        return placar

def verificaColisaoBola(bola,paleta1,paleta2,bolaDirx):
    if bolaDirx == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        return -1
    elif bolaDirx == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        return -1
    else:
        return 1


def InteligenciaArtificial(bola,bolaDirx,paleta2):
    if bolaDirx == 1:
        if paleta2.centery > bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -= 1
    return paleta2


def verificaColisao(bola, bolaDirX, bolaDirY):
    if bola.top == (largura_linha) or bola.bottom == (altura_tela - largura_linha):
            bolaDirY = bolaDirY * -1
    if bola.left == (largura_linha) or bola.right == (largura_tela - largura_linha):
            bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY

def moveBola(bola, bolaDirx,bolaDiry):
    bola.x += bolaDirx
    bola.y += bolaDiry
    return bola

def desenhaArena():
    DISPLAYSURF.fill(preto)
    pygame.draw.rect(DISPLAYSURF,branco,((0,0),(largura_tela,altura_tela)),largura_linha*2)
    pygame.draw.line(DISPLAYSURF, branco, ((largura_tela // 2), 0), ((largura_tela // 2), altura_tela),
                     (largura_linha // 4))

def desenhaPaleta(paleta):
    if paleta.bottom > altura_tela - largura_linha:
        paleta.bottom = altura_tela - largura_linha
    elif paleta.top < largura_linha:
        paleta.top = largura_linha
    pygame.draw.rect(DISPLAYSURF,branco,paleta)
def desenhaBola(bola):
    pygame.draw.rect(DISPLAYSURF,branco,bola)

def main():
    pygame.init()
    global DISPLAYSURF
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((largura_tela,altura_tela))
    pygame.display.set_caption("PongNet")
    terminou = False
    bolax = largura_tela//2 - largura_linha//2
    bolay = altura_tela//2 - largura_linha//2
    jogadorUm_posicao = (altura_tela - paleta_tamanho) // 2
    jogadorDois_posicao = (altura_tela - paleta_tamanho) // 2
    placar = 0
    bolaDirx = -1
    bolaDiry = -1
    paleta1 = pygame.Rect(PALETAOFFSET, jogadorUm_posicao, largura_linha, paleta_tamanho)
    paleta2 = pygame.Rect(largura_tela - PALETAOFFSET - largura_linha, jogadorDois_posicao, largura_linha,
                          paleta_tamanho)
    bola = pygame.Rect(bolax,bolay,largura_linha,largura_linha)
    desenhaArena()
    desenhaPaleta(paleta1)
    desenhaPaleta(paleta2)
    desenhaBola(bola)
    while not terminou:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                paleta1.y = mouseY
            pygame.mouse.set_visible(0)
            desenhaArena()
            desenhaPaleta(paleta1)
            desenhaPaleta(paleta2)
            desenhaBola(bola)

            bola = moveBola(bola, bolaDirx, bolaDiry)
            bolaDirx, bolaDiry = verificaColisao(bola, bolaDirx, bolaDiry)
            paleta2 = InteligenciaArtificial(bola, bolaDirx,paleta2)
            bolaDirx  = bolaDirx  * verificaColisaoBola(bola, paleta1, paleta2, bolaDirx)
            placar = verificaPlacar(paleta1,bola,placar,bolaDirx)
            desenhaPlacar(placar)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()



