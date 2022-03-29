import random
from time import sleep

import jogos_titulos
import jogos_menu


def jogar():

    sleep(1)
    jogos_titulos.titulo('ADIVINHE O NÚMERO')

    # introdução
    sleep(2)
    print('Olá, eu sou RANDOM!')
    sleep(2)
    print('Vou pensar em um número de 0 a 50 e você tem 5 chances para adivinhar!')
    sleep(2)
    jogos_titulos.titulo('ADIVINHE O NÚMERO')
    for c in range(3):
        print('...')
        sleep(2)
    jogos_titulos.titulo('ADIVINHE O NÚMERO')
    print('Já pensei! Agora tente adivinhar!')
    sleep(2)
    jogos_titulos.titulo('ADIVINHE O NÚMERO')
    print('Ah, já ia esquecendo... você começa o jogo com 100 pontos e a cada tentativa você perde 20 pontos!!')
    sleep(2)
    jogos_titulos.titulo('ADIVINHE O NÚMERO')
    print('Agora sim, vamos lá!')
    # introdução

    pontos = 100
    computador = random.randint(0, 50)  # Computador escolhe um número aleatório

    for tentativa in range(1, 6):
        sleep(3)
        jogos_titulos.titulo('ADIVINHE O NÚMERO')
        sleep(1)
        chute = int(input('{}º tentativa: '.format(tentativa)))  # Solicita um número para o usuário
        for c in range(3):
            print('...')
            sleep(2)

        acerta = chute == computador
        erra = chute != computador
        maior = computador > chute
        menor = computador < chute

        # Apresenta uma dica se está quente ou frio,
        # conforme a proximidade do chute para o número escolhido pelo computador
        if abs(computador - chute) > 20:
            dica = 'Iiih... ainda tá frio!'
        elif abs(computador - chute) > 10:
            dica = 'Ohh...tá esquentando'
        else:
            dica = 'Nuuuu...tá pegando fogooo!!!!'

        if tentativa == 5 and erra:  # Não acertou e as tentativas acabaram
            print('Não foi dessa vez! :(')
            sleep(1)
            print('Suas chances acabaram!!')
            sleep(1)
            pontos -= 20
        elif acerta:  # Acertou
            print('Acertou miserávi!!\n')
            break
        elif erra and maior:  # Erra e o número do computador é maior que o chute
            print('Não, não, não!')
            sleep(1)
            print(dica)
            pontos -= 20
            print('O número é maior!  ---> Pontuação: {}'.format(pontos))
        elif erra and menor:  # Erra e o número do computador é menor que o chute
            print('Ixi! Ainda não é esse! Tenta de novo...')
            sleep(1)
            print(dica)
            pontos -= 20
            print('É um número menor!---> Pontuação: {}'.format(pontos))

    sleep(2)
    jogos_titulos.titulo('ADIVINHE O NÚMERO')
    print('O número que pensei foi {}!'.format(computador))  # Informa o número escolhido pelo computador
    sleep(2)
    jogos_titulos.titulo('ADIVINHE O NÚMERO')
    print('Sua pontuação final foi {}!'.format(pontos))  # Mostra a pontuação final

    # Finaliza o jogo
    sleep(2)
    jogos_titulos.titulo('ADIVINHE O NÚMERO')
    print('Obrigado por jogar!!!')
    jogos_menu.finaliza('1')


if __name__ == "__main__":
    jogar()
