cont = 0
total = 0


print("=" * 20)
print("Carlinhos Imports")
print("=" * 20)

while True:
    produto = input("Nome do Produto: ")
    preco = int(input("Preço: R$ "))
    total = total + preco
    
    if total == preco:
        menor = preco
        nome_menor = produto
    
    if preco < menor:
        menor = preco
        nome_menor = produto

    if preco > 1000:
        cont = cont + 1
    continuar = input("Quer continuar? [S/N]: ").upper()
    if continuar != 'S':
        break
print("====== FIM DO PROGRAMA ======")
print(f"O total da compra foi R${total}")
print(f"Temos {cont} produto(s) custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_menor} que custa R${menor:.2f}")
