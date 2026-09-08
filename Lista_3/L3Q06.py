num1 = int(input("Digite o primeiro numero: "))
num2 = int (input("Digite o segundo numero:"))
num1c= num1+1
num1v= num1-1

if num1<num2:
    for i in range (num1c,num2):
        print(i)
elif num1>num2:
    for i in range (num1v,num2,-1):
        print(i)
else:
    print("Ambos os numeros sao o mesmo, nao existe intervalo inteiro")