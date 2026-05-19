n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
op = 0
while op != 5:

    print("=-="*10)
    print("           M E N U")
    print("=-="*10)

    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior número")
    print("[4] Novos números")
    print("[5] Sair do programa")

    op = int(input("Escolha uma operação: "))

    if op == 1:
        print("Resultado:", n1 + n2)
    elif op == 2:
        print("Resultado:",n1*n2)
    elif op == 3:
        if n1>n2:
            print("O maior número é o :",n1)
        elif n1<n2:
            print("O maior número é: ",n2)
    elif op == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
    elif op == 5:
        print("Finalizando...")
    else:
        print("Opção inválida")

print("Fim do Programa")
