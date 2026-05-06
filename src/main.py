from controllers.filme_controller import FilmeController

def menu():
    controller = FilmeController()
    
    while True:
        print("\n--- SISTEMA REDE DE CINEMAS ---")
        print("1. Cadastrar Filme")
        print("2. Listar Filmes")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Título: ")
            duracao = int(input("Duração (min): "))
            genero = input("Género: ")
            elenco = input("Elenco: ")
            diretor = input("Diretor: ")
            
            resultado = controller.criar_filme(titulo, duracao, genero, elenco, diretor)
            print(resultado)
            
        elif opcao == "2":
            filmes = controller.obter_lista_filmes()
            print("\n--- FILMES EM CARTAZ ---")
            for f in filmes:
                print(f"{f.id} | {f.titulo} ({f.duracao} min) - {f.genero}")
        
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
