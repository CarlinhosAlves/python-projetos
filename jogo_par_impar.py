cont = 0 

print("Vamos jogar Par ou Ímpar")
print("=-"*20)
while True:
    
    valor = int(input("Diga um valor: "))
    escolha = input("Par ou ímpar? [P/I]: ").upper()

    import random
    numero = random.randint(0,10)

    print("=-"*20)
    s = numero + valor
    
    if s % 2 == 0:
        resultado = 'P'
        texto = 'PAR'
    elif s % 2 != 0:
        resultado = 'I'
        texto = 'ÍMPAR'
   
    if resultado == escolha:
        print(f"Você jogou {valor} e o computador {numero}. Total de {s}. DEU {texto}")
        print("=-"*20)
        print("Você VENCEU!!!")
        print("Vamos jogar novamente...")
        print("=-"*20)
        cont = cont + 1
        
    else:   
        print(f"Você jogou {valor} e o computador {numero}. Total de {s}. DEU {texto}")   
        print("=-"*20)
        print("Você PERDEU!!!")
        print("=-"*20)
        break
print(f"GAME OVER! Você venceu {cont} vez(es) ")
