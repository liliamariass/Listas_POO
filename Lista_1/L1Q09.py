print("Saiba se o triangulo é equilatero ou escaleno")
l1 = int (input("qual o valor do 1° lado? "))
l2 = int (input (" Qual o valor do 2°? "))
l3 = int (input ("Qual o valor do 3°? "))

if l1 == l2 and l2 == l3:
    print ( " O triangulo é equilatero")
elif l1!=l2 and l2!=l3:
    print (" o triangulo é escaleno")
else:
    print ("nao é um triangulo")