print("="*20)
print(" BANCO CAR")
print("="*20)

valor = int(input("Qual valor você quer sacar? R$ "))

ced50 = 50
ced20 = 20
ced10 = 10
ced5 = 5
ced2 = 2


while valor <= 1:
    print("Valor inválido, tente novamente")
    valor = int(input("Qual valor você quer sacar? R$ "))
if valor >= ced50:
    ced50 = valor // 50
    valor = valor % 50
    print(f"{ced50} nota de {50}")
if valor >= ced20:
    ced20  = valor // 20
    valor = valor % 20
    print(f"{ced20} nota(s) de R$:{20}")
if valor >= ced10:
    ced10 = valor // 10
    valor = valor % 10
    print(f"{ced10} nota(s) de R$:{10}")
if valor >= ced5:
    ced5 = valor // 5
    valor = valor % 5
    print(f"{ced5} nota(s) de R${5}")
if valor >= ced2:
    ced2 = valor // 2
    valor = valor % 2
    print(f"{ced2} nota(s) de R${2}")



print("="*20)
print("Volte sempre ao BANCO CAR !")
