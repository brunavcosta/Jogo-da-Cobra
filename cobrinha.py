import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600,400))
pygame.display.set_caption("Jogo da Cobrinha")

cobra = [(100,50)]
direcao = (10,0)
comdida = (300,200)

def desenhar():
  tela.fill((0,0,0))
  for parte in cobra:
    pygame.draw.rect(tela, (0,255,0), (*parte, 10, 10))

  pygame.draw.rect(tela, (255,0,0), (*comdida, 10, 10))
  pygame.display.update()

rodando = True
relogio = pygame.time.Clock()

while rodando:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      rodando = False
    if evento.type ==pygame.KEYDOWN:
      if evento.key == pygame.K_LEFT:
        direcao = (-10,0)
      elif evento.key == pygame.K_RIGHT:
        direcao = (10,0)
      elif evento.key == pygame.K_UP:
        direcao = (0,-10)
      elif evento.key == pygame.K_DOWN:
        direcao = (0,10)

  nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
  cobra.insert(0, nova_cabeca)


  if nova_cabeca == comdida:
    comdida = (random.randint(0,59)*10, random.randint(0,39)*10) # Corrected random.randint and made food appear on a 10x10 grid
  else:
    cobra.pop()

  if nova_cabeca[0] < 0 or nova_cabeca[0] >= 600 or nova_cabeca[1] < 0 or nova_cabeca[1] >= 400:
    rodando = False
  
  if nova_cabeca in cobra[1:]:
    rodando = False

  desenhar()
  relogio.tick(15)

pygame.quit()