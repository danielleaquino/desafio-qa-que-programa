# Validador de E-mail
import re

def email_usuario():
    email = input("Digite um endereço de e-mail: ")
    return validar_email(email)

def validar_email(email):
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao_email, email) is not None

def main():
    if email_usuario():
        print("O e-mail é válido.")
    else:
        print("O e-mail é inválido.")

if __name__ == "__main__":
    main()