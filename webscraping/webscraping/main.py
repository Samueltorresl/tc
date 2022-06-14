from bs4 import BeautifulSoup
import requests
import re
from lxml import html


##FUNÇÕES

def kdspositivos():
    
  req = requests.get(str(data))

#expressao regular para encontrar os kds+ no req
  kddif = re.findall(r'[+][0-9]+',req.text)

  i = 1 

  print('\n''Jogador'+' '+'KD\n')

#vai printar enquanto estiver na class kdDiffCol
  for kdDiffCol  in kddif:
        
    tree = html.fromstring(req.content)

#pega o padrao xpath da tag e add 1 sempre que a lista atualizar  
    name_player = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[{}]/td[1]/a'.format(i))

    print(name_player[0].text, ' ->' + ' ' + kdDiffCol,'\n')  
    
    i += 1 
 

def ratingall():
    
    req = requests.get(str(data))

#expressao regular que verifica os ratings dos jogadores   
    rating_geral = re.findall(r'<td class="ratingCol">(.+)</td>',req.text)

    i = 1 

    print('\n''Jogador'+'   '+'Rating\n')

    for ratingCol in rating_geral:

        tree = html.fromstring(req.content)

#pega o padrao xpath da tag e add 1 sempre que a lista atualizar
        name_player = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[{}]/td[1]/a'.format(i))

        print(name_player[0].text, ' ->' + ' ' + ratingCol,'\n')
        
        i += 1

def roundsall():

    req = requests.get(str(data))

    rounds_players = re.findall(r'<td class="statsDetail gtSmartphone-only">(.+)</td>',req.text)

    i = 1

    print('\n''Jogador'+'   '+'Rounds\n')

    for Smartphoneonly in rounds_players:
    
        tree = html.fromstring(req.content)

#pega o padrao xpath da tag e add 1 sempre que a lista atualizar
        name_player = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[{}]/td[1]/a'.format(i))

        print(name_player[0].text, ' ->' + ' ' + Smartphoneonly,'\n')
        
        i += 1

###########################################################################################################################

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
checkurl = str(input("Digite o link do top20:\n"))


validador = re.search('\w.*.hltv.org.*players', checkurl)

#substitui o valor que o usuário inseriu procurando pelo padrao da expressão
data = re.sub("(19|20)\d\d[- \.](0[1-9]|1[012])[- \.](0[1-9]|[12][0-9]|3[01])",datauser,checkurl, 1)

#mesma coisa do if de cima, é um validador
if validador:
    print('Aguarde, carregando os dados!\n')

else: 
    print('Você não colocou o link da hltv, ou não colocou o link do ranking')

    exit()

print('Digite 1 - Players com KD+\nDigite 2 - Rating de Todos os Players\nDigite 3 - Ver Quantos Rounds o Player Ganhou\nDigite 4 - Vizualizar a Tabela Por Completo -->''\n')


#funcionalidades do menu
botao = int(input())

if botao == 1:
    
   kdspositivos()

if botao == 2:
    ratingall()

if botao ==3:
    roundsall()

else:
    print('Coloque um valor válido')

