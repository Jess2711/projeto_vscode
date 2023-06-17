import turtle

class Fogueira:
    def __init__(self, posicao, intensidade):
        self.posicao = posicao
        self.intensidade = intensidade
        self.caneta = turtle.Turtle()

    def desenhar(self):
     self.caneta.penup()
     self.caneta.shape("arrow")
     self.caneta.color("red")
     print(self.posicao) 
    
        