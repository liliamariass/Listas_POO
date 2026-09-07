
print("Prototipo de terminal para realizar operacoes matematicas")
valor1 = float(input("Digite o primeiro valor: "))
operacao = int(input("qual operacao deseja realizar? \ndigite 1 para adicao\n2 para subtracao\n3 para multiplicacao\n4 para divisao: "))
valor2 = float(input("Digite o segundo valor:"))

if operacao==1:
    resultado=valor1+valor2
    print(f"{resultado}")
elif operacao==2:
    resultado=valor1-valor2
    print(f"{resultado}")
elif operacao==3:
    resultado=valor1*valor2
    print(f"{resultado}")
elif operacao==4:
    resultado=valor1/valor2
    print(f"{resultado}")
else:
    print ("Operacao invalida!")
