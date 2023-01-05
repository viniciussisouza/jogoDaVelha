import os
import random
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2  # 1 = CPU - 2 = Jogador
maxJogadas = 9
vitoria = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def tela():

    global velha
    global jogadas
    os.system("cls") or None
    print("    0   1   2")
    print(f'0:   {velha[0][0]}  | {velha[0][1]} | {velha[0][2]}')
    print("    -----------")
    print(f'1:   {velha[1][0]}  | {velha[1][1]} | {velha[1][2]}')
    print("    -----------")
    print(f'2:   {velha[2][0]}  | {velha[2][1]} | {velha[2][2]}')
    print(f'Jogadas: {Fore.GREEN}{str(jogadas)} {Fore.RESET}')


def jogadorJoga():

    global jogadas
    global quemJoga
    global vitoria
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            linha = int(input('Que linha você quer jogar? '))
            coluna = int(input('Que coluna você quer jogar? '))
            while velha[linha][coluna] != " ":
                linha = int(input('Que linha você quer jogar? '))
                coluna = int(input('Que coluna você quer jogar? '))

            velha[linha][coluna] = "X"
            jogadas += 1
            quemJoga = 1
            os.system("cls") or None

        except:
            print("Linha e\ou coluna inválida")

def cpuJoga():

    global jogadas
    global quemJoga
    global vitoria
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        linha = random.randrange(0, 3)
        coluna = random.randrange(0, 3)
        while velha[linha][coluna] != " ":
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
        velha[linha][coluna] = "O"
        jogadas += 1
        quemJoga = 2

def  verificarVitoria():
    global velha
    vit = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vit = "n"
        #Verificar Linhas
        il = 0
        ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vit = s
                break
            il += 1
        if vit != "n":
            break

    #Verificar colunas


        il = 0
        ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vit = s
                break
            ic += 1
        if vit != "n":
            break

    #Verificar Diagonal 1:

        soma = 0
        idiag = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
                soma += 1
            idiag += 1

        if soma == 3:
            vit = s
            break
    #Verificar Diagonal 2:

        soma = 0
        idiagl= 0
        idiagc = 2
        while idiagc >= 0:
            if velha[idiagl][idiagc] == s:
                soma += 1
            idiagl += 1
            idiagc -= 1

        if soma == 3:
            vit = s
            break
    return vit

def redefinir():
    global velha
    global maxJogadas
    global quemJoga
    global jogadas
    global vitoria
    jogadas = 0
    quemJoga = 2  # 1 = CPU - 2 = Jogador
    maxJogadas = 9
    vitoria = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

while jogarNovamente == "s":
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        vitoria = verificarVitoria()
        if vitoria != "n" or jogadas >= maxJogadas:
            break

    print(Fore.RED + "Fim de Jogo!" + Fore.YELLOW)
    if vitoria == "X" or vitoria == "O":
        print(f'Resultado: Jogador {vitoria} venceu!!')
    else:
        print('Resultado: empate!!!')

    jogarNovamente = input(Fore.BLUE + "Deseja jogar novamente? s/n " + Fore.RESET)
    redefinir()
