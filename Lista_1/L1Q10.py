print("Saiba o montante total a ser pago para financiar")
valor = float (input("ql valor "))
taxa = float (input("porcentagem da taxa"))
meses = int (input("quantos meses"))

taxa=taxa/100
juros=valor*taxa*meses
valorf=valor+juros

print (f"O valor inicial foi {valor:.2f}. Com os juros de {juros}, o valor total a ser pago é {valorf:.2f}")