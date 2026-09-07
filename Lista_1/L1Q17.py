print("Programa para determinar a corrente eletrica de um  equipamento")
tensao = float(input(" Digite a tensao em volts: "))
resistencia = float(input("Digite a resistencia eletrica em ohms: "))
corrente = tensao/resistencia

print(f"a corrente do equipamento é de {corrente}A")