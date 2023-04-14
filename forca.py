import random

def jogar():
    saudacao_inicial()
    palavra_secreta = criacao_palavra_secreta()
    letras_acertadas = criacao_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    total_de_tentativas = 6

    

    #enquanto (true)
    while( not enforcou and  not acertou):

        print("Tentativa {} de {}".format(erros+1, total_de_tentativas))
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        mensagem_de_vitoria()
    else:
        mensagem_de_derrota(palavra_secreta)
    print("Fim do Jogo!")

def saudacao_inicial():
    print('-----------------------------------------')
    print("Bem vindo no jogo da Forca")
    print('-----------------------------------------')

def criacao_palavra_secreta():
    #abertura de arquivo para leitura e codificação do arquivos em utf-8
    arquivo = open("palavra.txt", "r", encoding="utf-8")
    
    palavras = []
    #inserindo a palavras do arquivos em uma lista
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    #fechamento do arquivo
    arquivo.close()

    #sorteio para indice da palavra a ser escolhida
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].lower()

    return palavra_secreta

def criacao_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?\n")
    chute = chute.strip().lower()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if( chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_de_vitoria():
    print("Parabéns, você ganhou!")
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

def mensagem_de_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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
    
if(__name__ == "__main__"):
    jogar()

