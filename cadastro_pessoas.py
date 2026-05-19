cont = 0
cont1 = 0
cont2 = 0

while True:
    print("=-"*20)
    print("CADASTRE UMA PESSOA")
    print("=-"*20)
    
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper()

    while sexo != 'M' and sexo != 'F':
        print("Opção ínvalida!! Tente novamente..)
        sexo = input("Sexo [M/F]: ").upper()

    print("=-"*20)
    decisao = input("Quer continuar? [S/N]: ").upper()

    while decisao != 'S' and decisao != 'N':
        print("Opção ínvalida!! Tente novamente..)
        decisao = input("Quer continuar? [S/N]: ").upper()

    if idade > 18:
        cont = cont +1
    if sexo == 'M':
        cont1 = cont1 + 1
    if sexo == "F" and idade < 20:
        cont2 = cont2 + 1

    if decisao == 'N':
        break

print("===== FIM DO PROGRAMA =====")
print(f"Total de pessoas com mais de 18 anos: {cont}")
print(f"Ao total temos {cont1} homen(s) cadastrado(s)")
print(f"E temos {cont2} mulher(es) com menos de 20 anos.")
