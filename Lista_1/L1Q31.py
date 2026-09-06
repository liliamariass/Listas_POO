
print("Saiba se o ano é bissexto")
ano = int(input("Digite o ano que quer saber"))
div400 = ano%400
div4 = ano%4
ndiv100 = ano%100
if div400==0:
    print (f"{ano} é um ano bissexto")
elif div4==0 and ndiv100!=0:
    print (f"{ano} é um ano bissexto")
else:
    print (f"{ano} não é um ano bissexto")