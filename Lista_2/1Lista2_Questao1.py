
print("Sistema academico que gera codigos numericos")
codigosv = 0
soma = 0

while codigosv < 10:
    codigos = int (input("Digite o codigo: "))
    
    if codigos%6 == 0:
        codigosv+=1
        soma+=codigos
        
print (f"A soma dos 10 valores validos foi {soma}")