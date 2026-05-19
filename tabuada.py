while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("=-"*20)
    for i in range (1,11):
        
        print(f"{n} x {i} = {n*i}")
    print("=-"*20)   
print("PROGRAMA TABUADA ENCERRADO -- VOLTE SEMPRE")
