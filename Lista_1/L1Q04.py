import math
print("Saiba a medida de um triangulo retangulo:")
medida = int (input("Digite 1 para saber o valor da hipotenusa 2 para cateto: "))
if medida==1:
    c1 =float (input(" Digite o valor do cateto adjascente: "))
    c2 = float (input(" Digite o valor do cateto oposto: "))
    hp = math.sqrt ((c1**2)+(c2**2))
    print(f" a medida da hipotenusa é: {hp:.5f}")

elif medida==2:
    hip = float (input("Digite o valor da hipotenusa: "))
    c = float (input("Digite o valor do cateto: "))
    cq = math.sqrt ((hip**2)-(c**2))
    print(f"o valor do outro cateto é: {cq:.5f}")

else:
    print ("Opçao invalida!")