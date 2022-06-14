import requests
import re

def validadorurl():
    checkurl = str(input("Digite o link do top20\n"))

    validador = re.search('\w.*.hltv.org.*players', checkurl)   
