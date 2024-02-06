# Conversor de Unidades
opcao = input('''Digite o número da opção da conversão que você quer fazer:
              1 - Quilômetros para milhas
              2 - Milhas para Quilômetros
              3 - Metros para Pés
              4 - Pés para Metros
              5 - Graus Celsius para Fahrenheit
              6 - Graus Fahrenheit para Celsius''')

numero = float(input("Digite o valor a ser convertido: "))

match opcao:
    case "1":
        conversao = numero*0.621371
    case "2":
        conversao = numero*1.60934
    case "3":
        conversao = numero*3.28084
    case "4":
        conversao = numero*0.3048
    case "5":
        conversao = numero*(9/5)+32
    case "6":
        conversao = (numero-32)*5/9
    case _:
        print("Opcão inválida")

print(f"Resultado da conversão: {conversao}")