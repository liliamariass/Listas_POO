print("Sistema de vendas informatica")
preco=float (input("Qual o preço unitario? "))
quant=int (input("Qual a quantidade de produtos? "))
desc= int (input("Qual o valor do desconto? "))

precoi= quant*preco
vdesc= precoi-desc
valorf = vdesc

print (f"Valor total: {valorf}")