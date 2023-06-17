import turtle
import math

TEMP_MAX = 200
TEMP_MIN = 20

class Bichinhos:
  def __init__(self, nome, posicao, cor) -> None:
        self.nome = nome
        self.temperatura = 60
        self.posicao = posicao 
        self.caneta = turtle.Turtle()
        self.cor = cor
        self.caneta.goto(posicao)
  def desenhar(self):
     self.caneta.penup()
     self.caneta.shape("turtle")
     self.caneta.pendown()
     self.caneta.color(self.cor)
     print(self.posicao)

  def mover(self):
    self.posicao = [self.posicao[0] + 10, self.posicao[1]]
    self.caneta.goto(self.posicao)
  
    
  def calc_temp(self, pos_fogueira):
        Dist = math.sqrt((pos_fogueira[1] - self.posicao[1])**2 + (pos_fogueira[0] - self.posicao[0])**2) 
        self.temperatura = -Dist/2 + 500
        print(pos_fogueira)
        print(self.posicao)
        print(Dist)
        print(self.temperatura)