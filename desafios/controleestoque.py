estoque = []

while True: 
    print("==== CONTROLE ESTOQUE ====")
    print("1- Cadastrar produto")
    print("2- listar produto")
    print("3- consultar produto")
    print("4- excluir produto")
    print("5- sair")

    opção = input("Digite uma opção:")

    if opção == '1':
        produto = input("Digite o produto que quer cadastrar no estoque:").lower()
        estoque.append(produto)

    elif opção == '2':
        print("===== PRODUTOS NO ESTOQUE =====")
        for produto in estoque:
            print(produto)

    elif opção == '3':
        busca = input("Qual produto deseja consultar:").lower()
        if busca in estoque:
            print("=== ENCONTRADO ===")
            print(f"{busca}")
        else:
            print("produto nao encontrado")

    elif opção == '4':
        excluir = input("Qual produto voce deseja excluir:").lower()
        if excluir in estoque:
            estoque.remove(excluir)
        else:
            print("produto nao encontrado")

    elif opção == '5':
        print("saindo...")
        break