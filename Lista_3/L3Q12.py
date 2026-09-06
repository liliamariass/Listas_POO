soma=0
i=0
while i<10:
    codigo=int(input("Digite o Codigo: "))
    coddiv3 = codigo%3
    if coddiv3 == 0:
        i+=1
        soma+=codigo
print(f"A soma dos valores validos é: {soma}")
    
