print("Bem vindo a Calculadora Pixl em rem")

def Cal(pixel):
    a = pixel/16
    return f"{a:.2f}rem"

while True:
    print(15*"=")
    x= float(input("Quantos pixels coverterei?? Aprete 0 se quer parar o loop! >> "))
    if x == 0:
     break
    print("\n",Cal(x))
    
    
# So dar um run!
