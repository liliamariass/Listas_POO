
print("Sistema de horas de estudo")
quant = float(input("Quantas horas planeja estudar essa semana? "))
if quant<10:
    print (f"{quant} horas é uma quantidade muito baixa")
elif quant>40:
    print (f"{quant} horas é uma quantidade muito alta")
else:
    print (f"Plano configurado para {quant} horas ")