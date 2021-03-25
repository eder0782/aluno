import telepot

bot_server = telepot.Bot('1488068658:AAHymNOhXTkIAq6o_Ep7_-RZVomUpHhRL9Q')

def mensagem(msg):
    print(msg['text'])


bot_server.message_loop(mensagem)


while True:
    pass