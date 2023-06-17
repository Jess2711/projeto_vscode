import turtle

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

  def mover(self):
    self.posicao = [self.posicao[0] + 10, self.posicao[1]]
    self.caneta.goto(self.posicao)
  
    
    
  #def verificar_temperatura(self):
        #if self.temperatura 