prim= int(input("Digite o primeiro identificador: "))
ulti= int(input("Digite o ultimo identificador: "))
soma=0
u=ulti+1
quant = abs(prim-u)

for i in range (prim, u):
    soma+=i
    
media=soma/quant
print(f"a media dos numeros existentes no intervalo dos dois numeros é: {media:.2f}")
