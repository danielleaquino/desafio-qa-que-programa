# Jogo do Número Primo
import random

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def jogar(pontuacao):
    numero = random.randint(1, 100)
    print(f"O número {numero} é primo?")
    resposta = input("\nÉ primo (S) ou não primo (N)? ").strip().lower()
    if (resposta == 's' and primo(numero)) or (resposta == 'n' and not primo(numero)):
        pontuacao += 1
        print(f"Resposta correta! Sua pontuação é agora {pontuacao}.")
    else:
        print("Resposta incorreta! Sua pontuação permanece a mesma.")
    return pontuacao

def ver_pontuacao(pontuacao):
    print(f"Sua pontuação é {pontuacao}")
    return pontuacao

def zerar_pontuacao():
    print("Sua pontuação foi zerada!")
    return 0

def main():
    global pontuacao
    pontuacao = 0

    while True:
        opcao = input('''\nJogo do número primo:
            1 - Jogar
            2 - Ver pontuação
            3 - Zerar pontuação
            4 - Sair\n''')

        if opcao == '1':
            pontuacao = jogar(pontuacao)
        elif opcao == '2':
            pontuacao = ver_pontuacao(pontuacao)
        elif opcao == '3':
            pontuacao = zerar_pontuacao()
        elif opcao == '4':
            print('Saiu')
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()