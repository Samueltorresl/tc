from bs4 import BeautifulSoup
import requests
import re
from lxml import html

data_rating=""

def ratingall(data_rating):
    
    req = requests.get(str(data_rating))
    
    rating_geral = re.findall(r'<td class="ratingCol">(.+)</td>',req.text)

    i = 1 

    print('Jogador'+' '+'Rating\n')

    for ratingCol in rating_geral:

        tree = html.fromstring(req.content)

        name_player = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[{}]/td[1]/a'.format(i))

        print(name_player[0].text + ' ' + ratingCol,'\n')
        
        i += 1