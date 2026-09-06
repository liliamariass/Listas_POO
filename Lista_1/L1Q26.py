
print("Sistema de classificacao por idade")
idade = int(input("Digite a sua idade"))
if idade>0 and idade<12:
    print("Crianca")
elif idade>13 and idade<18:
    print("adolescente")
elif idade>18:
    print("adulto")
else:
   print ("A idade inserida é invalida")