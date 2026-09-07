print("Saiba o valor total a ser pago para o emprestimo ")
valor = float (input("qual o valor emprestado? "))
taxa = float (input(" Qual a porcentagem da taxa de juros mensal? "))
meses = int (input("quantos meses serao necessarios para quitar o emprestimo? "))

taxa=taxa/100
juros=valor*taxa*meses
valorf=valor+juros

print (f"O valor dos juros foi R${juros:.2f} e o montante total a ser pago é R${valorf:.2f}")