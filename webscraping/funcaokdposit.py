from bs4 import BeautifulSoup
import requests
import re


def kdspositivos():

  req = requests.get(str('https://www.hltv.org/stats/players?startDate=2021-06-13&endDate=2022-06-13&rankingFilter=Top20'))

  kddif = re.findall(r'[+][0-9]+',req.text)

  for kdDiffCol  in kddif:
    print(kdDiffCol)
 





