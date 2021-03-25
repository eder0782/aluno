import requests
from datetime import datetime


ini = datetime.now()

retorno = requests.get('http://213.136.80.31:8080/')

tempo = datetime.now() - ini

print('tempo: ', tempo)
