import psutil
import pygame

#Funções
def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    tela.fill(preto)
    pygame.draw.rect(s1, azul, (20, 50, largura_tela-2*20, 70))
    larg = larg*mem.percent/100
    pygame.draw.rect(s1, vermelho, (20, 50, larg, 70))
    tela.blit(s1, (0, 0))
    total = round(mem.total/(1024**3), 1)
    texto_barra = "Uso de memória (Total: " + str(total) + "GB): "
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))

def mostra_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2*20
    pygame.draw.rect(s2,azul,(20,50,largura_tela - 2*20,70))
    larg = larg*capacidade/100
    pygame.draw.rect(s2, vermelho, (20, 50, larg, 70))
    tela.blit(s2, (0, altura_tela / 3))
    text = font.render("Uso da CPU:",1,branco)
    tela.blit(text,(20,200))

def uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2*20
    pygame.draw.rect(s3,azul,(20,50,larg,70))
    larg = larg*disco.percent/100
    pygame.draw.rect(s3, vermelho, (20, 50, larg, 70))
    tela.blit(s3, (0, 2 * altura_tela / 3))
    total = round(disco.total/(1024*1024*1024),2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra,1,branco)
    tela.blit(text,(20,400))
    dic_interfaces = psutil.net_if_addrs()
    IP = 'IP da rede:'+ dic_interfaces['Ethernet'][0].address
    text2 = font.render(IP,1,branco)
    tela.blit(text2, (20, 550))

#Programa principal
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0,0,255)
vermelho = (255,0,0)
pygame.font.init()
font = pygame.font.Font(None, 32)
# Iniciando a janela principal
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
pygame.display.init()

s1 = pygame.surface.Surface((largura_tela,altura_tela/3))
s2 = pygame.surface.Surface((largura_tela,altura_tela/3))
s3 = pygame.surface.Surface((largura_tela,altura_tela/3))

pygame.draw.rect(s1, azul, (20, 50, largura_tela - 2 * 20, 70))
tela.blit(s1, (0, 0))
pygame.draw.rect(s2, azul, (20, 50, largura_tela - 2 * 20, 70))
tela.blit(s2, (0, altura_tela / 3))
pygame.draw.rect(s3, azul, (20, 50, largura_tela - 2 * 20, 70))
tela.blit(s3, (0, 2 * altura_tela / 3))

# Cria relógio
clock = pygame.time.Clock()

cont = 60

terminou = False

while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    if cont == 60:
        mostra_uso_memoria()
        mostra_cpu()
        uso_disco()
        cont = 0
    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)
    cont = cont+1

# Finaliza a janela
pygame.display.quit()