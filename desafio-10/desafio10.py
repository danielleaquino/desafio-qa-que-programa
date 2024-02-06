import random

class JogoDaAdivinhacao:
    def __init__(self):
        self.pontuacao = 0
        self.maxtentativas = 7

    def menu (self):
        print('''\nJogo do número de adivinhação:
            1 - Jogar
            2 - Ver pontuação
            3 - Zerar pontuação
            4 - Sair\n''')
        
    def jogar(self):
        while True:
            self.menu()
            opcao = input ("Escolha uma opcao:\n")
            if opcao == '1':
                self.jogar_rodada()
            elif opcao == '2':
                self.mostrar_pontuacao()
            elif opcao == '3':
                self.zerar_pontuacao()
            elif opcao == '4':
                print("\nObrigado por jogar. Até logo!\n")
                break
            else:
                print("\nOpção inválida.")

    def jogar_rodada (self):
        numero = random.randint(1, 100)
        print("Você tem até no máximo 7 tentativas para adivinhar um número inteiro de 1 a 100!")
        while 0 < self.maxtentativas :
            print (f"Você tem {self.maxtentativas} tentativas restantes")
            resposta = int(input("Qual é o número?\n"))
            if numero == resposta:
                print ("Parabéns você acertou!")
                self.pontuacao +=1
                self.maxtentativas = 7
                break
            elif numero > resposta:
                print (f"Você errou! O número é maior que {resposta}")
                self.maxtentativas -= 1
            else:
                print (f"Você errou!O número é menor que {resposta}")
                self.maxtentativas -= 1
        if self.maxtentativas == 0:
            print(f"Você perdeu! o número sorteado foi o número: {numero}")

    def mostrar_pontuacao (self):
        print(f"A sua pontuacao é {self.pontuacao}")
    
    def zerar_pontuacao (self):
        self.pontuacao = 0
        print ("Sua pontuação foi zerada")


if __name__ == "__main__":
    jogo = JogoDaAdivinhacao()
    jogo.jogar()       