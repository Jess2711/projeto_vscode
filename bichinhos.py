import turtle
import math
from random import randint

TEMP_MAX = 200 #variaveis estaticas
TEMP_MIN = 20
STEP = 10

class Bichinhos:
  def __init__(self, nome, cor) -> None:
        self.nome = nome
        self.temperatura = 60 #não estaticas de cada objeto
        self.posicao = __class__.gera_posicao() 
        self.caneta = turtle.Turtle()
        self.cor = cor
        self.caneta.goto(self.posicao)
        self.gene = __class__.gera_gene()

  def desenhar(self):
     self.caneta.penup()
     self.caneta.shape("turtle")
     self.caneta.pendown()
     self.caneta.color(self.cor)
     print(self.posicao)

     #valor do gene = .34/100 = 34% 

  def mover(self, pos_fogueira):
    if (randint(0,100)) <= 100*self.gene:
       self.move_for_fogo(pos_fogueira)
    else:
       self.dist_to_fogo(pos_fogueira)
    self.caneta.goto(self.posicao)

  
  def move_for_fogo(self, pos_fogueira):
    aleatorio=(randint(0,1))
    if aleatorio == 0: #mover no x
      if self.posicao[0] < pos_fogueira[0]:
        self.posicao[0] += STEP
      else: 
        self.posicao[0] -= STEP   
    else:   
      if self.posicao[1] < pos_fogueira[1]:
        self.posicao[1] += STEP
      else: 
        self.posicao[1] -= STEP  

  def dist_to_fogo(self, pos_fogueira):
    aleatorio=(randint(0,1))
    if aleatorio == 0: #mover no x
      if self.posicao[0] < pos_fogueira[0]:
        self.posicao[0] -= STEP
      else: 
        self.posicao[0] += STEP   
    else:   
      if self.posicao[1] < pos_fogueira[1]:
        self.posicao[1] -= STEP
      else: 
        self.posicao[1] += STEP 
       
    
  def calc_temp(self, pos_fogueira):
        Dist = math.sqrt((pos_fogueira[1] - self.posicao[1])**2 + (pos_fogueira[0] - self.posicao[0])**2) 
        self.temperatura = -Dist/2 + 500
    

  def check_viver(self):
     if self.temperatura > (TEMP_MAX) or self.temperatura < (TEMP_MIN):
        return False
     else:
        return True

  @staticmethod
  def gera_posicao():
      posicao = [(randint(-250,+250)), (randint(-250,+250))]
      return posicao
      

  @staticmethod
  def gera_gene():
    gene=float(randint(0,100))/100
    return gene
  
  