import random
import time

continuar = True
print('Bem vindo ao Jogo da Velha Triangular!')
jogador = 0


def troca(num, jog):
    global um
    global dois
    global tres
    global quatro
    global cinco
    global seis
    global sete
    global oito
    global nove
    if num == 1:
        um = f'({jog})'
    if num == 2:
        dois = f'({jog})'
    if num == 3:
        tres = f'({jog})'
    if num == 4:
        quatro = f'({jog})'
    if num == 5:
        cinco = f'({jog})'
    if num == 6:
        seis = f'({jog})'
    if num == 7:
        sete = f'({jog})'
    if num == 8:
        oito = f'({jog})'
    if num == 9:
        nove = f'({jog})'


um = '(1)'
dois = '(2)'
tres = '(3)'
quatro = '(4)'
cinco = '(5)'
seis = '(6)'
sete = '(7)'
oito = '(8)'
nove = '(9)'


def tabuleiro():
    out = um.center(60) + ('\n' * 5) + f'{dois}\n'.center(45)
    out += ' ' * 16 + f'{tres}\n' + ' ' * 29 + f'{quatro}\n' + ' ' * 22 + f'{cinco}\n\n'
    out += f'{seis}'.center(49)
    out += ('\n' * 7) + f'{sete}' + ' ' * 10 + oito + ' ' * 45 + f'{nove}'
    return out


listx = []
listy = []
jogadores = ['x', 'y']
jogador = random.choice(jogadores)
while continuar is not None:
    print(f"Jogador '{jogador}' começa.")
    tab = tabuleiro()
    print(tab)
    num = int(input(f"Jogada de '{jogador}', escolha um espaço no tabuleiro:\n"))
    if jogador == 'x':
        listx = listx + [num]
    if jogador == 'y':
        listy = listy + [num]
    troca(num, jogador)
    tab = tabuleiro()
    print(tab)
    print(listx)
    print(listy)
    if jogador == 'x':
        jogador = 'y'
    else:
        jogador = 'x'
