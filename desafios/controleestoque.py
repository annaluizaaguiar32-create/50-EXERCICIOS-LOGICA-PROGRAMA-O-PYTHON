estoque = [
    ['monitor',10 ],
    ['mouse', 5 ],
    ['teclado', 8]
]

while True: 
    print("==== CONTROLE ESTOQUE ====")
    print("1- Cadastrar produto")
    print("2- listar produto")
    print("3- Atualizar estoque")
    print("4- consultar produto")
    print("5- excluir produto")
    print("6- sair")

    opção = input("Digite uma opção:")

    if opção == '1':
        produto = input("Digite o produto que quer cadastrar no estoque:").lower()
        quantidade = int(input("quantidade:"))
        estoque.append([produto,quantidade])

    elif opção == '2':
        print("===== PRODUTOS NO ESTOQUE =====")
        for produto in estoque:
            print(produto)
    
    elif opção == '3':
        busca = input("qual produto deseja atualizar:").lower()

        encontrado = False

        for produto in estoque:
            if produto[0] == busca:
                print("ENCONTRADO")
                quantidadenova = int(input("Digite a quantidade:"))

                produto[1] = quantidadenova
                encontrado = True
                print("ESTOQUE ATUALIZADO")
        if encontrado == False:
                print("produto nao encontrado")


    elif opção == '4':
        busca = input("Qual produto deseja consultar:").lower()
        if busca in estoque:
            print("=== ENCONTRADO ===")
            print(f"{busca}")
        else:
            print("produto nao encontrado")

    elif opção == '5':
        excluir = input("Qual produto voce deseja excluir:").lower()
        if excluir in estoque:
            estoque.remove(excluir)
        else:
            print("produto nao encontrado")

    elif opção == '6':
        print("saindo...")
        break