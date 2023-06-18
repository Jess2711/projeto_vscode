import turtle
import math
from random import randint

TEMP_MAX = 140 #variaveis estaticas
TEMP_MIN = 80
STEP = 5

class Bichinhos:
  def __init__(self, nome, cor) -> None:
        self.nome = nome
        self.temperatura = 60 #não estaticas de cada objeto
        self.posicao = __class__.gera_posicao() 
        self.cor = cor
        self.criar_caneta()
        self.caneta.goto(self.posicao)
        self.gene = __class__.gera_gene()
        


  def criar_caneta(self):
     self.caneta = turtle.Turtle()
     self.caneta.penup() 
     self.caneta.shape("turtle")
     self.caneta.color(self.cor)


  def limpar_visual(self):
     self.caneta.clear()
     
    

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
       
  def calc_dist(self, pos_fogueira):
     return math.sqrt((pos_fogueira[1] - self.posicao[1])**2 + (pos_fogueira[0] - self.posicao[0])**2) 
     


  def calc_temp(self, pos_fogueira, intensidade_fogueira):
        Dist = self.calc_dist(pos_fogueira)
        self.temperatura = -5/3*Dist + intensidade_fogueira

    

  def esta_vivo(self):
     if self.temperatura > TEMP_MAX or self.temperatura < TEMP_MIN:
        return False
     else:
        return True
     
  
  def reproduzir(self, partner):
     novo_bichinho = Bichinhos("lentinho", "blue") 
     gene_novo_bichinho = (self.gene + partner.gene)/2
     novo_bichinho.gene = gene_novo_bichinho
     return novo_bichinho
  

     


  @staticmethod
  def gera_posicao():
      posicao = [(randint(-250,+250)), (randint(-250,+250))]
      return posicao
      

  @staticmethod
  def gera_gene():
    gene=float(randint(0,100))/100
    return gene
  
  