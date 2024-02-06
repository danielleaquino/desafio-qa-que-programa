# Temporizador/Contador
import time
opcao = input('''Escolha 1 ou 2 da opcao que você deseja para o contador:
                 1 - Temporizador (Contagem progressiva)
                 2 - Contador (Contagem regressiva) ''')

tempo = int(input("Digite o tempo em segundos:"))

if opcao == '1':
    contador = 0
    while contador < tempo:
        print(contador + 1, end='\n')
        time.sleep(1)
        contador+=1
elif opcao == '2':
    while tempo > 0:
        print(''*10, end='\n')
        print(tempo, end='\n')
        time.sleep(1)
        tempo -= 1
else:
    print("Escolha inválida.")

print(' ' * 10, end='\r')
print("\nTempo esgotado!")    