from controle_notas import add_note, list_notes

entrada = None

def mostrar_menu():
    print("Escolha uma das opções abaixo para continuar: ")
    print("1 - Adicionar uma nova tarefa")
    print("2 - Visualizar todas as tarefas")
    print("3 - Marcar uma tarefa como concluída")
    print("4 - Remover uma tarefa")
    print("5 - Sair")    

print("Bem vindo ao meu programa Task Manager")
while True:
    mostrar_menu()

    entrada = input("Digite o número da opção desejada: ")

    match entrada:
        case "1":
            print("Você escolheu adicionar uma nova tarefa.")
            nome_tarefa = input("Defina o nome da tarefa: ")
            add_note(nome_tarefa)

        case "2":
            print("Você escolheu visualizar todas as tarefas.")
            list_notes()

        case "3":
            print("Você escolheu marcar uma tarefa como concluída.")
            
        
        case "4":
            print("Você escolheu remover uma tarefa.")
        
        case "5":
            print("Você escolheu sair do programa.")
        
            break
        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")