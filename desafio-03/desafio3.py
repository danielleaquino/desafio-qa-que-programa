# palíndromo
def teste_palindromo(texto):
    texto = texto.lower().replace(" ","").replace(",","").replace(".","").replace("!","").replace("?","")
    invertido = texto[::-1] 

    if texto == invertido:
        return True
    else:
        return False

frase = input("Digite uma palavra ou uma frase: ")
if teste_palindromo(frase):
    print("É um palíndromo!")
else:
    print ("Não é um palíndromo!")