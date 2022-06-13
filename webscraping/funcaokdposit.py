from bs4 import BeautifulSoup
import requests
import re

def kdspositivos():
      
  req = requests.get('https://www.hltv.org/stats/players?startDate=2021-06-12&endDate=2022-06-12&rankingFilter=Top20')

  kddif = re.findall(r'[+][0-9]+',req.text)

  for kdDiffCol  in kddif:
    print(kdDiffCol)






