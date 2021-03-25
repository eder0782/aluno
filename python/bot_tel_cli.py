import telepot
from datetime import datetime

bot_cli = telepot.Bot('1435110631:AAF6e60mvu0N-fnJGuiyV6eiCotmHNObgUA')

ini = datetime.now()
result = bot_cli.sendMessage(chat_id='@teste_santo',text='EURUSD;15:30;call')

print(result)

dif = datetime.now() - ini

print(dif)



