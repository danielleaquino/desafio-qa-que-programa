# Análise de Frequência de Letras
frequencia_letras = {}

texto = input("Digite o texto: ")

for caractere in texto:
    if caractere.isalpha():
        letra = caractere.lower()
        frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1

if not frequencia_letras:
    print("Não há nenhuma letra!")
else:
    print("\nFrequência de letras no texto:")
    for letra, frequencia in frequencia_letras.items():
        print(f"{letra}: {frequencia}")