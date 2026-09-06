print("Programa para determinar a corrente eletrica de um equipamento")
tensao = float(input(" Digite a tensao em volts "))
potencia = float(input("Digite a resistencia eletrica em watts"))
corrente = tensao*potencia

print(f"{corrente}A")