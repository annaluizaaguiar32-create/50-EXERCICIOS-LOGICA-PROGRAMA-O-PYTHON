senha_correta = "1234"
tentativas = 5 

while tentativas > 0:
    senha = input("digite a senha de 4 digitos:")

    if len(senha) !=4 or not senha.isdigit():
        print("Digite uma senha com 4 digitos numericos!")
        tentativas = tentativas - 1
        print(f"{tentativas} tentativas restantes")
        continue 

    if len(set(senha)) !=4:
        print("A senha nao pode ter numeros repetidos!")
        tentativas = tentativas - 1
        print(f"{tentativas} tentativas restantes")
        continue

    if senha == senha_correta:
        print("Senha correta! COFRE DESBLOQUEADO")
        break

    certo = 0
    errado = 0 
    for i in range(4):
        if senha[i] == str(senha_correta)[i]:
            certo = certo + 1
    print(f"numeros na posição certa: {certo}")

    tentativas = tentativas - 1
    print(f"tentativas restantes: {tentativas}")

    if tentativas == 0:
        print("cofre bloqueado tentativas acabaram")