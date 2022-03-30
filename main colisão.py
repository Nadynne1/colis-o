import pygame
from random import randint
pygame.init()

x = -50  #max = 185 min = 285
y = 100
pos_x = -210
pos_y = 1200
pos_ya = 2000
pos_yb = 1000
y1 = -50
timer = 0
tempo_segundo = 0

velocidade = 10
velocidade1 = -20
v_carros = 10

fundo1 = pygame.image.load('pista 1..png')
fundo2 =pygame.image.load('pista2.png')
carro = pygame.image.load('carro vermelho.png')
carro2 = pygame.image.load('carro amarelo.png')
carro3 = pygame.image.load('principal.png')
carro4 = pygame.image.load('carro branco.png')


font = pygame.font.SysFont('Fixedsys Regular',50)
texto = font.render("tempo:",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)


janela = pygame.display.set_mode((800,650))
pygame.display.set_caption("colisão")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 185:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= -285:
        x -= velocidade

  # colisão
    if ((x + 80 > pos_x + 400  and  y  +  170 > pos_yb)):             #lado direito
        y = 1200

    if ((x - 40 < pos_x and  y  +  190 > pos_y)):                      #lado esquerdo
        y = 1200

    if ((x + 10 > pos_x + 200 and y + 30 > pos_ya)) or ((x - 70 < pos_x +200 and y + 30 > pos_ya)):
        y = 1200


    if((pos_y <= -240)) :
        pos_y = randint(800,1000)

    if((pos_ya <= -240)) :                       # pos_ya carro amarelo
        pos_ya =randint(1000,2000)

    if ((pos_yb <= -240)):                       # pos_yb carro branco
        pos_yb = randint(1400,3200)

    pos_y -= v_carros
    pos_ya -= v_carros +4
    pos_yb -= v_carros +5

    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("tempo:"+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0


    y1 -= velocidade1
    if (y1>=700):
        y1= -50

    janela.blit(fundo1,(0,0))
    janela.blit(fundo2,(120,y1))
    janela.blit(carro3,(x,y))
    janela.blit(carro2,(pos_x,pos_y))
    janela.blit(carro,(pos_x + 200,pos_ya))
    janela.blit(carro4,(pos_x + 400,pos_yb))
    janela.blit(texto,pos_texto)


    pygame.display.update()
pygame.quit()