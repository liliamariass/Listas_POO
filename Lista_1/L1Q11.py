print("Saiba o valor total a ser pago para o emprestimo ")
valor = float (input("ql valor emprwstado "))
taxa = float (input("porcentagem da taxa de juros mensal"))
meses = int (input("quantos meses serao necessarios para quitar"))

taxa=taxa/100
juros=valor*taxa*meses
valorf=valor+juros

print (f"O valor dos juros foi R${juros}, o montante total a ser pago é R{valorf:.2f}")