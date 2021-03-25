import MetaTrader5 as mt

if not mt.initialize():
    print('Falha na inicialização: ' + str(mt.last_error()))
    quit()
total = [1,2]
total.count
mt.Buy()

# print(mt.terminal_info())
# print(mt.account_info())