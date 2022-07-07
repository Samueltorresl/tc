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

def mapsall():
        
    req = requests.get(str(data))

#expressao regular que verifica os mapas dos jogadores   
    maps_geral = re.findall(r'<td class="statsDetail">([^\.]\d+)</td>',req.text)

    i = 1 

    print('\n''Jogador'+'   '+'Mapa\n')

    for statsDetail in maps_geral:

        tree = html.fromstring(req.content)

#pega o padrao xpath da tag e add 1 sempre que a lista atualizar
        name_player = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[{}]/td[1]/a'.format(i))

        print(name_player[0].text, ' ->' + ' ' + statsDetail,'\n')
        
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

    print('Organizar por mais mapas jogados --> 1\nOrganizar por mais rounds jogados --> 2\nOrganizar por maior KD --> 3\nOrganizar por maior Rating 2.0 --> 4')
    
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

def rank_mundial():
    
    print('Digite 1 - 2022\nDigite 2 - 2021\nDigite 3 - 2020\nDigite 4 - 2019\nDigite 5 - 2018\nDigite 6 - 2017\nDigite 7 - 2016\nDigite 8 - 2015\n')
    
    opcao = int(input('Aguardando Valor -->'))
    
    req = requests.get(str('https://www.hltv.org/ranking/teams/'))

    datarank=''
#Datas de cada ano na hltv
    data_2022 = 'https://www.hltv.org/ranking/teams/2022/june/13'

    data_2021 = 'https://www.hltv.org/ranking/teams/2021/december/27'

    data_2020 = 'https://www.hltv.org/ranking/teams/2020/december/28'

    data_2019 = 'https://www.hltv.org/ranking/teams/2019/december/30'

    data_2018 = 'https://www.hltv.org/ranking/teams/2018/december/31'

    data_2017 = 'https://www.hltv.org/ranking/teams/2017/december/25'

    data_2016 = 'https://www.hltv.org/ranking/teams/2016/december/26'

    data_2015 = 'https://www.hltv.org/ranking/teams/2015/december/28'
    
    def funcaorankingall(datarank):

        req = requests.get(str(datarank))

        nome_time = re.findall(r'<span class="name">([\w+\s.]+\w+)</span>',req.text)

        pontos = re.findall(r'<span class="points">(.+)</span>',req.text)

        j = 1

        print('Posição    Time      Pontuação\n')

        for name, points in zip(nome_time, pontos):

            print( '#',j,'  --> ',name,'-->', points)

            j += 1

    #opcao 2022
    if opcao == 1: 
        funcaorankingall(data_2022) 

    if opcao == 2: 
        funcaorankingall(data_2021)

    if opcao == 3: 
        funcaorankingall(data_2020)

    if opcao == 4: 
        funcaorankingall(data_2019)

    if opcao == 5: 
        funcaorankingall(data_2018)

    if opcao == 6: 
        funcaorankingall(data_2017)

    if opcao == 7: 
        funcaorankingall(data_2016)

    if opcao == 8: 
        funcaorankingall(data_2015)

def eventos_principais():
    
    req = requests.get(str('https://www.hltv.org/'))

    #expressao regular para encontrar os eventos no req
    evento_principal = re.findall(r'<span class="eventname">(([\w+\s]+\w+))</span>',req.text)

    eventos = re.findall(r'<span class="upcomingeventname" title="[\w+\s]+\w+">(([\w+\s]+\w+))</span>',req.text)

    print('\n''Eventos:\n')

    print(evento_principal,'\n')

    #vai printar enquanto estiver na class kdDiffCol
    for upcomingeventname in eventos:
        
        print(upcomingeventname,'\n')

#funcao que da o start no nosso robo
def inicio():

    print('Digite 1 - Players com KD+\nDigite 2 - Rating de Todos os Players\nDigite 3 - Ver Quantos Rounds o Player Ganhou\nDigite 4 - Vizualizar os Mapas\nDigite 5 - Vizualizar a Tabela Por Completo\nDigite 6 Para Ver o Ranking Mundial Por Ano\nDigite 7 Para Ver os Eventos Principais -->\n')

    #funcionalidades do menu
    botao = int(input())

    if botao == 1: 
        kdspositivos()

    if botao == 2: 
        ratingall()

    if botao == 3: 
        roundsall()

    if botao == 4: 
        mapsall()

    if botao == 5: 
        tabelacompleta()

    if botao == 6: 
        rank_mundial()
    
    if botao == 7:
        eventos_principais()
      
        

###########################################################################################################################

## Pede a data para o usuário
datauser = str(input("Digite a Data: \n"))

#valida a data por meio de expressão regular
validadordata = re.search('(19|20)\d\d[- \.](0[1-9]|1[012])[- \.](0[1-9]|[12][0-9]|3[01])', datauser)
#exemplo \d{2}\-\d{2}\-\d{4}

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

    inicio()
else: 
    print('Você não colocou o link da hltv, ou não colocou o link do ranking')

    exit()

print('Quer rodar o programa denovo ?')

x=1

while (x==1):

    rodar_denovo = int(input('Digite 1 - Sim\nDigite 2 - Não\n'))

    if rodar_denovo == 1: inicio()

    if rodar_denovo == 2: exit()