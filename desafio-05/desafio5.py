 # Geração de números aleatórios
import random

megasena = []

while len(megasena) < 6:
    numero = random.randint(1,60)
    if numero not in megasena:
        megasena.append(numero)

print("Os números do jogo da Mega sena são: ",megasena)