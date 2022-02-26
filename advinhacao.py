import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade? \n(1) Fácil (2)Médio (3)Difícil')
    nivel = int(input('Escolha o nível'))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute_str = input('Digite seu numero de 1 a 99 ')
        print('Você digitou ', chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print('Digite seu numero de 1 a 100')
            continue

        elif acertou:
            print('Você acertou')
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print('Você errou! O chute foi maior')
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif(menor):
                print('Você errou! O chute foi menor')
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))


if __name__ == '__main__':
    jogar()