vmin = int (input("Qual o valor minimo do intervalo dos codigos? "))
vmax =int(input("E qual o valor maximo? "))
vmaxc= vmax+1
multiplo=0
for i in range (vmin,vmaxc):
    codv=i%7
    if codv ==0:
        multiplo+=1
print(f"Existem {multiplo} codigos validos")
