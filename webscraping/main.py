from bs4 import BeautifulSoup
import requests
import re

# FUNCOES 
def kdspositivos():
    
  req = requests.get(str(data))

  kddif = re.findall(r'[+][0-9]+',req.text)

  nome_player = re.findall(r'<(.*?>(.*?)<\/\1', req.text)
  print (nome_player)

  for kdDiffCol  in kddif:
    print(kdDiffCol)

def ratingall():

    req = requests.get(str(data))
    
    rating_geral = re.findall(r'<td class="ratingCol">(.+)</td>',req.text)

    for ratingCol in rating_geral:
        print(ratingCol)



## Pede a data para o usuário
datauser = str(input("Digite a Data: \n"))

#valida a data por meio de expressão regular
validadordata = re.search('(19|20)\d\d[- \.](0[1-9]|1[012])[- \.](0[1-9]|[12][0-9]|3[01])', datauser)

#Se a data estiver certa prossegue.
if validadordata:
    print('Prossiga Com O Link : \n')

else: 
    print('Coloque a data no formato yyyy-mm-dd')

    exit()

#valida o link que o usuário vai colocar
checkurl = str(input("Digite o link do top20\n"))


validador = re.search('\w.*.hltv.org.*players', checkurl)

#substitui o valor que o usuário inseriu procurando pelo padrao da expressão
data = re.sub("(19|20)\d\d[- \.](0[1-9]|1[012])[- \.](0[1-9]|[12][0-9]|3[01])",datauser,checkurl, 1)

#mesma coisa do if de cima, é um validador
if validador:
    print('Aguarde, carregando os dados!\n')

else: 
    print('Você não colocou o link da hltv, ou não colocou o link do ranking')

    exit()

print('Digite 1 - Players com KD+\nDigite 2 - Rating de Todos os Players\nDigite 3 - Vizualizar a Tabela Por Completo\n-->')
print(data)

#funcionalidades do menu
botao = int(input())

if botao == 1:
    
   kdspositivos()

if botao == 2:
    ratingall()

