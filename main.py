from bichinhos import Bichinhos
from fogueira import Fogueira

cont_bichinhos = 5
list_bichinhos = []
fogueira = Fogueira([0,0], 90)


for elemento in range(0,5):
  novo_bichinho = Bichinhos("lentao", [20,20*elemento], "red")
  list_bichinhos.append(novo_bichinho)
  
fogueira.desenhar()

for bichinho in list_bichinhos:
  bichinho.desenhar()
  
def rodar_simulacao():
    for bichinho in list_bichinhos:
        bichinho.mover()
  
for elemento in range(0,10):
  rodar_simulacao()