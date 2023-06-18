import turtle

class Fogueira:
    def __init__(self, posicao, intensidade):
        self.posicao = posicao
        self.intensidade = intensidade
        self.criar_caneta()


    def desenhar(self):
     self.caneta.penup()
     self.caneta.shape("arrow")
     self.caneta.color("red")

    def criar_caneta(self):
       self.caneta = turtle.Turtle()
    
    
        