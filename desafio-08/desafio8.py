#Lista de Tarefas

def adicionar_tarefa(lista_tarefa):
    tarefa = input("Digite a tarefa a ser adicionada: ")
    lista_tarefa.append(tarefa)
    print("A tarefa foi adicionada")

def remover_tarefa(lista_tarefa):
    if (len(lista_tarefa) > 0):
        print("Lista de tarefas")
        for indice, tarefa in enumerate(lista_tarefa):
            print(f"{indice}: {tarefa}")
        indice = int(input("\nDigite o número da tarefa a ser removida: "))
        if 0 <= indice < len(lista_tarefa):
            lista_tarefa.pop(indice)
            print("A tarefa foi removida")
        else:
            print ("Indice inválido")
    else:
        print("Lista de tarefas está vazia!")
       
def mostrar_tarefa(lista_tarefa):
    if (len(lista_tarefa)>0):
        print("Lista de tarefas:")
        for indice, tarefa in enumerate(lista_tarefa):
            print(f"{indice}: {tarefa}")
    else:
         print("Lista de tarefas está vazia!")

def main():

    lista_tarefa = []

    while True:
        opcao = input('''\nGerenciador de Lista de Tarefas:
              1 - Adicionar tarefa
              2 - Remover tarefa
              3 - Mostrar tarefa
              4 - Sair\n''')
        
        match opcao:
            case '1':
                  adicionar_tarefa(lista_tarefa)
            case '2':
                  remover_tarefa(lista_tarefa)
            case '3':
                  mostrar_tarefa(lista_tarefa)
            case '4':
                  print('Saiu')
                  break
            case _:
                  print("Opção inválida")

if __name__ == "__main__":
    main()              