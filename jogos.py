import forca
import adivinhacao

print('-----------------------------------------')
print("Escolha seu Jogo")
print('-----------------------------------------')


print("(1) Forca \n(2) Adivinhação")
jogo = int(input("Qual jogo?\n"))

if(jogo == 1):
    print("Forca")
    forca.jogar()
elif(jogo == 2):
    print("Adivinhação")
    adivinhacao.jogar()
else:
    print("Opção Invalida")
