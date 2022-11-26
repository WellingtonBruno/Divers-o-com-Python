from random import choice
from time import sleep

cont = 1
comida = []
print( '-*' *20)
print('JOGO DA ESCOLHA DA COMIDA')
print( '-*' *20)
while True:
    r = str(input('\033[96mDigite a Comida que irei escolher para você: \033[m')).upper()
    if cont < 3:
        comida.append(r)
        comida[:]
        cont += 1
    else:
        break

sleep(1)
print('\033[0;49;35mEstou escolhendo sua comida\033[m')
sleep(2)
print('\033[49;93mTenha paciencia....\033[m')
sleep(2)
print('\033[49;96mQue escolha difícil!!\033[m')
sleep(2)
print('\033[34m.....\033[m')
sleep(3)
print(f'\033[32m......A escolha foi : \033[31m{choice(comida)}\033[m')


