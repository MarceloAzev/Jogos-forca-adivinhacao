import random

def jogar():

    print('-----------------------------------------')
    print("Bem vindo no jogo de Adivinhação")
    print('-----------------------------------------')

    numero_secreto = random.randrange(1,101) # randrange(valor incial, valor final +1 - 1 até 100) 
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil \n(2) Médio \n(3) Difícil")

    nivel = int(input("Defina o nivel: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        print("Opção Invalida!")
    # range(valor inicial de rodada, valor final +1, salto) - rodada > total de tentativas
    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite seu número entre 1 e 100: ")
        numero_chute = int(chute)
        print("Você digitou",numero_chute)

        if(numero_chute < 1 or numero_chute > 100):
            print("Você deve digitar um número entre 1 e 100 \n")
            continue

        acertou = numero_chute == numero_secreto
        maior = numero_chute > numero_secreto
        menor = numero_chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos\n".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu numero foi maior que o número secreto. \n")
            elif(menor):
                print("Você errou! O seu numero foi menor que o número secreto. \n")
            pontos_perdido = abs(numero_secreto - numero_chute) 
            pontos = pontos - pontos_perdido


    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar()
