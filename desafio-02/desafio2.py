# Calculadora
operacao = input('''Escolha o tipo de operação que você deseja fazer:
            + para adição
            - para subtração
            * para multiplicação
            / para divisão
            ''')

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o primeiro número: "))

if operacao == '+':
    print('{}+{} = '.format(n1, n2))
    print(n1+n2)
elif operacao == '-':
    print('{}-{} = '.format(n1, n2))
    print(n1-n2)
elif operacao == '*':
    print('{}*{} = '.format(n1, n2))
    print(n1*n2)
elif operacao == '/':
    if n2 == 0:
        print("Não é possível dividir por zero")
    else:    
        print('{}/{} = '.format(n1, n2))
        print(n1/n2)
else:
    print("Você não digitou um operador válido, por favor rode o programa novamente")