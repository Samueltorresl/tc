import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
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

#pega o xpath da tag e add 1 sempre que a lista atualizar  
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

#expressao regular para verificar os rounds ganhos
    rounds_players = re.findall(r'<td class="statsDetail gtSmartphone-only">(.+)</td>',req.text)

    i = 1

    print('\n''Jogador'+'   '+'Rounds\n')

    for Smartphoneonly in rounds_players:
    
        tree = html.fromstring(req.content)

#pega o padrao xpath da tag e add 1 sempre que a lista atualizar
        name_player = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[{}]/td[1]/a'.format(i))

        print(name_player[0].text, ' ->' + ' ' + Smartphoneonly,'\n')
        
        i += 1

def tabelacompleta():

    print('Escolha como você deseja organizar sua tabela\n')
    print('Organizar por mais mapas jogados --> 1\nOrganizar por mais rounds jogados --> 2\nOrganizar por maior KD --> 3\nOrganizar por maior Rating 1.0 --> 4')
    menu = int(input())

    option = Options()
    option.headless = True
    driver = webdriver.Firefox()


    driver.get(data)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    time.sleep(2)
    # Organizar por mais mapas jogados
    if menu == 1: 
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/table/thead/tr/th[3]').click()
    # Organizar por mais rounds jogados
    if menu == 2:
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/table/thead/tr/th[4]').click()
    # Organizar por maior KD
    if menu == 3:
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/table/thead/tr/th[6]').click()
    #Organizar por maior Rating 2.0
    if menu == 4:
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/table/thead/tr/th[7]').click()

    time.sleep(1)
    tabela = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/table')
    html_content = tabela.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Tranforma o html em uma tabela 
    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Player', 'Maps', 'Rounds', 'K/D', 'Rating2.0']]
    df.columns = ['Jogador', 'Mapas', 'Rounds', 'K/D', 'Rating 2.0']

    # Mostra o ranking na tela
    print(df)

    # Converte o conteudo em um dicionario
    top10ranking = {}
    top10ranking['Ranking'] = df.to_dict('records')

    driver.quit()

    js = json.dumps(top10ranking)
    fp = open('ranking.json', 'w')
    fp.write(js)
    fp.close()

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

#expressao regular que valida o link do usuário
validador = re.search('\w.*.hltv.org.*players', checkurl)

#expressao regular que substitui a data do usuario 
data = re.sub("(19|20)\d\d[- \.](0[1-9]|1[012])[- \.](0[1-9]|[12][0-9]|3[01])",datauser,checkurl, 1)

#mesma coisa do if de cima, é um validador
if validador:
    print('Aguarde, carregando os dados!\n')

else: 
    print('Você não colocou o link da hltv, ou não colocou o link do ranking')

    exit()

print('Digite 1 - Players com KD+\nDigite 2 - Rating de Todos os Players\nDigite 3 - Ver Quantos Rounds o Player Ganhou\nDigite 4 - Vizualizar a Tabela Por Completo''-->''\n')


#funcionalidades do menu
botao = int(input())

if botao == 1:
    
   kdspositivos()

if botao == 2:
    ratingall()

if botao == 3:
    roundsall()

if botao == 4:
    tabelacompleta()

else:
    print('Coloque um valor válido')

