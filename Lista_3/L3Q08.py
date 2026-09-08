num = int (input("Digite um numero de 1 a 10: "))
print(f"Tabuada do numero {num}:")
for i in range (0,11):
    resul = num*i
    print(f"{num}X{i}={resul}")