from bs4 import BeautifulSoup
import requests
import re
from lxml import html

datakd=""
def kdspositivos(datakd):
    
  req = requests.get(str(datakd))

  kddif = re.findall(r'[+][0-9]+',req.text)

  i = 1 

  print('Jogador'+' '+'KD\n')

  for kdDiffCol  in kddif:
        
    tree = html.fromstring(req.content)

    name_player = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[{}]/td[1]/a'.format(i))

    print(name_player[0].text + ' ' + kdDiffCol,'\n')  
    
    i += 1 





