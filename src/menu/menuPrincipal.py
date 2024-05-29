from src.utils.limparTerminal import limparTerminal
from src.menu.menuUsuario import menuUsuario
from src.menu.menuVendedor import menuVendedor

def menuPrincipal():
    while True:
        limparTerminal()
        print("==" * 30)
        print("Menu Principal")
        # print("1 - CRUD Compras")
        # print("2 - CRUD Produtos")
        print("3 - CRUD Usuários")
        print("4 - CRUD Vendedores")
        print("0 - Sair")
        print("==" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "3":
                menuUsuario()
            case "4":
                menuVendedor()
            case "0":
                limparTerminal()
                break
            case _:
                print("\nOpção inválida\n")
                input()