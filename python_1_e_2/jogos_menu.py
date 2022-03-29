import os
from time import sleep

import adivinhar_numero
import forca_jogo


def iniciar(jogo):

    os.system('cls')
    while jogo not in '123':

        jogo = input('Escolha o jogo que deseja jogar:\n'
                     '(1) Adivinhe o número\n'
                     '(2) Forca\n'
                     '(3) Sair\n')

        if jogo == '1':
            adivinhar_numero.jogar()
        elif jogo == '2':
            forca_jogo.jogar()
        elif jogo == '3':
            os.system('cls')
            print('Tchau...até a próxima!!!')
        else:
            os.system('cls')
            print('Opção inválida!')
        sleep(2)
        os.system('cls')


def finaliza(jogo):

    os.system('cls')
    escolher = '0'

    while escolher not in '123':
        escolher = input('O que você deseja fazer agora?\n'
                         '(1) JOGAR NOVAMENTE\n'
                         '(2) ESCOLHER OUTRO JOGO\n'
                         '(3) SAIR\n')

        if escolher == '1':
            if jogo == '1':
                adivinhar_numero.jogar()
            if jogo == '2':
                forca_jogo.jogar()
        elif escolher == '2':
            iniciar('0')
        elif escolher == '3':
            os.system('cls')
            print('Tchau...até a próxima!!!')
            sleep(2)
        else:
            print('Opção inválida!')


if __name__ == "__main__":
    iniciar('0')
