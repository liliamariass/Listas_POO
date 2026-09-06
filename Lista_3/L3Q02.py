def calculo(x,y):
    mult = x*y
    soma = x+y
    if mult<=1000:
        print(f"Valores dentro do limite\nProduto: {mult}")
    else:
        print(f"Valores acima do limite\nSoma: {soma}")
        
v1 = int (input("Digite o primeiro valor: "))
v2 = int (input("Digite o segundo valor: "))

resultado = calculo(v1,v2)

print(f"{resultado}")