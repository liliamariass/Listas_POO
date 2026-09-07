
print("Sistema de classificacao por idade")
idade = int(input("Digite a sua idade: "))
if idade>0 and idade<12:
    print("Voce é crianca")
elif idade>13 and idade<18:
    print("Você é adolescente")
elif idade>18:
    print("Você é adulto")
else:
   print ("A idade inserida é invalida")