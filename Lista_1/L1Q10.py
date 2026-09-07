print("Saiba o montante total a ser pago para financiar")
valor = float (input("Qual o valor financiado? "))
taxa = float (input("Qual a porcentagem  da taxa de juros mensal? "))
meses = int (input("quantos meses sera o financiamento? "))

taxa=taxa/100
juros=valor*taxa*meses
valorf=valor+juros

print (f"O valor inicial foi {valor:.2f}. Com os juros de {juros}, o valor total a ser pago é {valorf:.2f}")