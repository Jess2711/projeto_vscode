from bichinhos import Bichinhos
from fogueira import Fogueira
import turtle
from random import randint



#for bichinho in list_bichinhos:
  #bichinho.criar_visual()

def listar_sobreviventes():
    list_vive = []
    for bichinho in list_bichinhos:
      if bichinho.esta_vivo():
        list_vive.append(bichinho)
    return list_vive
      
        

def gerar_descendente(list_vive):
   bichinho1 = list_vive[randint(0, len(list_vive) - 1)]
   bichinho2 = list_vive[randint(0, len(list_vive) - 1)]
   return bichinho1.reproduzir(bichinho2)

def gerar_descendentes(list_vive):
   #for bichinho in list_bichinhos:
      #if not bichinho.esta_vivo():
         #bichinho = gerar_descendente(list_vive)
    for i in range(0, len(list_bichinhos)-1):
       bichinho = list_bichinhos[i]
       if not bichinho.esta_vivo():
          list_bichinhos[i] = gerar_descendente(list_vive)

def visual():
   criar_visual = turtle.Screen()
   criar_visual.clear()


def calc_media_gene():
   somar = 0
   for bichinho in list_bichinhos:
      somar+=bichinho.gene
   return somar/len(list_bichinhos)

def calc_media_dist():
   somar = 0
   for bichinho in list_bichinhos:
      somar+=bichinho.calc_dist(fogueira.posicao)
   return somar/len(list_bichinhos)
  

def rodar_simulacao(rodada):
    for bichinho in list_bichinhos:
        bichinho.mover(fogueira.posicao)
        bichinho.calc_temp(fogueira.posicao, fogueira.intensidade)
    if rodada%100 == 0:
      visual()
      fogueira.criar_caneta()
      fogueira.desenhar()
      print(calc_media_gene())
      print(calc_media_dist())
      for bichinho in list_bichinhos:
        bichinho.criar_caneta()
        bichinho.limpar_visual()
      list_vive = listar_sobreviventes()
      if not len(list_vive) == 0:
        gerar_descendentes(list_vive)  



#a = visual()
#print(a)

      
cont_bichinhos = 100
list_bichinhos = []
fogueira = Fogueira([200,150],50)


for elemento in range(0,cont_bichinhos):
  novo_bichinho = Bichinhos("lentao","red")
  list_bichinhos.append(novo_bichinho)
  
fogueira.desenhar()   

  
for rodada in range(1,500):
  rodar_simulacao(rodada)

