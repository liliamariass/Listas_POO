
print("Calcule sei Indice de Massa corporal (IMC)")
peso = float(input("Digite seu peso em kg: "))
altura = float (input("Digite sua altura em metros: "))
imc = peso/(altura*altura)
if imc <18.5:
    print(f"seu IMC é {imc:.2f}. Esta abaixo do peso")
elif 18.5 <= imc <25:
    print(f"seu IMC é {imc:.2f}. Esta com peso normal")
elif 25 <= imc <30:
    print(f"seu IMC é {imc:.2f}. Esta com sobrepeso")
else:
    print(f"seu IMC é {imc:.2f}. Esta com obesidade")