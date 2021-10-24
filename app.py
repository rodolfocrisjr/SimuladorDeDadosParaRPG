import random
import os
from random import randint

valor_minimo_d4 = 1
valor_maximo_d4 = 4

valor_minimo_d6 = 1
valor_maximo_d6 = 6

valor_minimo_d8 = 1
valor_maximo_d8 = 8

valor_minimo_d10 = 1
valor_maximo_d10 = 10

valor_minimo_d12 = 1
valor_maximo_d12 = 12

valor_minimo_d20 = 1
valor_maximo_d20 = 20

# Execução da função
def jogar_dados(dado):
    if dado == '1':
        print(f'{os.linesep}Jogando dado...{os.linesep}')
        print(random.randint(valor_minimo_d4, valor_maximo_d4))

    elif dado == '2':
        print(f'{os.linesep}Jogando dado...{os.linesep}')
        print(random.randint(valor_minimo_d6, valor_maximo_d6))

    elif dado == '3':
        print(f'{os.linesep}Jogando dado...{os.linesep}')
        print(random.randint(valor_minimo_d8, valor_maximo_d8))

    elif dado == '4':
        print(f'{os.linesep}Jogando dado...{os.linesep}')
        print(random.randint(valor_minimo_d10, valor_maximo_d10))

    elif dado == '5':
        print(f'{os.linesep}Jogando dado...{os.linesep}')
        print(random.randint(valor_minimo_d12, valor_maximo_d12))

    elif dado == '6':
        print(f'{os.linesep}Jogando dado...{os.linesep}')
        print(random.randint(valor_minimo_d20, valor_maximo_d20))

    else:
        print(f'{os.linesep}Digite um número entre 1 e 6{os.linesep}')


def start():
    # Apresentar o programa
    print('Olá! Bem vindo ao simulador de dados para RPG!')
    # Apresentar as opções de dados
    while True:
        dado = input(
            f'{os.linesep}Qual dado gostaria de jogar?{os.linesep}[1] - D4{os.linesep}[2] - D6{os.linesep}[3] - D8{os.linesep}[4] - D10{os.linesep}[5] - D12{os.linesep}[6] - D20{os.linesep}')

        jogar_dados(dado)


if __name__ == '__main__':
    start()