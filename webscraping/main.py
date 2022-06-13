from bs4 import BeautifulSoup
import requests
import re
import funcaokdposit

checkurl = str(input("Digite o link do top20\n"))

validador = re.search('\w.*.hltv.org.*players', checkurl)

if validador:
    print('Aguarde, carregando os dados!\n')

else: 
    print('Você não colocou o link da hltv, ou não colocou o link do top20')

    exit()

print('Digite 1 - Players com KD+\nDigite 2 - Rating de Todos os Players\nDigite 3 - Vizualizar a Tabela Por Completo\n-->')

botao = int(input())

if botao == 1:
    
    funcaokdposit.kdspositivos()




