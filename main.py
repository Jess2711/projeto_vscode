from bichinhos import Bichinhos
from fogueira import Fogueira

cont_bichinhos = 5
list_bichinhos = []
list_vive = []
fogueira = Fogueira([0,0], 90)



for elemento in range(0,cont_bichinhos):
  novo_bichinho = Bichinhos("lentao","red")
  list_bichinhos.append(novo_bichinho)
  
fogueira.desenhar()

for bichinho in list_bichinhos:
  bichinho.desenhar()
  
def rodar_simulacao(rodada):
    for bichinho in list_bichinhos:
        bichinho.mover(fogueira.posicao)
        bichinho.calc_temp(fogueira.posicao)
    if rodada%100 == 0:
      listar_sobreviventes()
        

  
for rodada in range(0,500):
  rodar_simulacao(rodada)

def listar_sobreviventes():
    list_vive = []
    for bichinho in list_bichinhos:
      if bichinho.check_viver():
        list_vive.append(bichinho)
        print(bichinho.temperatura)