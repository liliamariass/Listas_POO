print("Saiba a raiz da equacao")
a = float (input("Digite o coeficiente de a: "))
b = float (input("Digite o coeficiente de b: "))
c = float (input("Digite o coeficiente de c: "))

delta=(b**2)-(4*a*c)

if delta==0:
    raizu= (-b/(2*a))
    print (f"Há uma unica raiz real: {raizu}")
elif delta>0:
    raiz1= (-b + (delta**0.5))/(2*a)
    raiz2= (-b - (delta**0.5))/(2*a)
    print (f"Há duas raizes reais: {raiz1} e {raiz2}")
else:
    print ("Não há raizes reais.")