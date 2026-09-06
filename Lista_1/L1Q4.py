import math
print("Saiba a medida de um triangjlp retanfjo ")
medida = int (input("Digite 1 pa saber o balor da h e 2 para cayeto"))
if medida==1:
    c1 =float (input(" c adjascente"))
    c2 = float (input(" c oposto"))
    hp = math.sqrt ((c1**2)+(c2**2))
    print(f" a medida {hp:.5f}")
    
elif medida==2:
    hip = float (input(" v hip"))
    c = float (input("v c"))
    cq = math.sqrt ((hip**2)-(c**2))
    print(f"o v c e {cq:.5f}")
    
else:
    print ("Opçao invalida!")