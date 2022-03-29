from time import sleep
import unidecode
import jogos_menu
import forca_palavras
import jogos_titulos


def jogar():
    dificuldade = escolhe_dificuldade()
    palavra_secreta = forca_palavras.gera_palavra(dificuldade)
    jogos_titulos.titulo('FORCA')
    palavra_escondida = "_" * (len(palavra_secreta))

    print('É uma palavra com {} letras.'.format(len(palavra_secreta)))
    print('PALAVRA: {}\n'.format(palavra_escondida))

    vidas = 7
    erros = 0
    rodada = 1

    while vidas > 0:

        sleep(2)

        palpite = ''
        while palpite == '':
            jogos_titulos.titulo('FORCA')
            print('PALAVRA: {} >>>>>>> VIDAS: {}\n'.format(palavra_escondida, "* " * vidas))
            palpite = pede_palpite(rodada)

        if palpite == '1':
            jogos_titulos.titulo('FORCA')
            print('A palavra é {}'.format(palavra_secreta))
            break
        elif unidecode.unidecode(palavra_secreta) == unidecode.unidecode(palavra_escondida) or \
                palpite == unidecode.unidecode(palavra_secreta):
            sleep(2)
            jogos_titulos.titulo('FORCA')
            print('Parabéns...você descobriu a palavra!!!')
            imprime_mensagem_vencedor(palavra_secreta)
            break

        possui = unidecode.unidecode(palavra_secreta).find(palpite)

        if len(palpite) > 1 and palpite not in unidecode.unidecode(palavra_secreta):
            print('A palavra não é {}!'.format(palpite))
            vidas -= 1
            rodada += 1
        elif possui != -1 and palpite not in unidecode.unidecode(palavra_escondida):
            index = 0
            sleep(2)
            jogos_titulos.titulo('FORCA')
            print('Muito bem! Tem {} na palavra!'.format(palpite))
            for letra in unidecode.unidecode(palavra_secreta):
                if palpite == unidecode.unidecode(letra):
                    lis = list(palavra_escondida)
                    lis[index] = palavra_secreta[index]
                    palavra_escondida = "".join(lis)
                index += 1
            rodada += 1
        elif palpite in unidecode.unidecode(palavra_escondida):
            sleep(2)
            jogos_titulos.titulo('FORCA')
            print('A letra {} já foi!'.format(palpite))
        else:
            sleep(2)
            jogos_titulos.titulo('FORCA')
            print('A palavra não possui a letra {}'.format(palpite))
            vidas -= 1
            rodada += 1
            erros += 1
            desenha_forca(erros)

        if vidas == 0:
            imprime_mensagem_perdedor(palavra_secreta)

    sleep(4)
    jogos_menu.finaliza('2')


def escolhe_dificuldade():
    dificuldade = '0'

    while dificuldade not in '123' or dificuldade == '':
        sleep(2)
        jogos_titulos.titulo('FORCA')

        dificuldade = input('Escolha o nível de dificuldade:\n'
                            '(1) Fácil\n'
                            '(2) Difícil\n'
                            '(3) Aleatório\n')
        if dificuldade not in '123':
            jogos_titulos.titulo('FORCA')
            print('Opção inválida!')
        elif dificuldade == '':
            continue
    return dificuldade


def pede_palpite(rodada):
    palpite = input('(1) DESISTIR\n'
                    'Palpite {} - Informe uma letra ou, se você já adivinhou, '
                    'pode digitar a palavra e depois tecle "ENTER":\n'.format(rodada))
    return unidecode.unidecode(palpite.strip().upper())


def desenha_forca(erros):
    sleep(2)
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor(palavra_secreta):
    sleep(2)
    print('A palavra é {}'.format(palavra_secreta))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    sleep(2)
    jogos_titulos.titulo('FORCA')
    print('Que pena...suas vidas acabaram...você foi enforcado!')
    print('A palavra é {}'.format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    jogar()
