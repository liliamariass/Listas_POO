print("Media da temperatura interna do servidor")
t1 = float(input(" Digite a temperatura do primeiro sensor: "))
t2 = float(input(" Digite a temperatura segundo sensor: "))
t3 = float (input("Digite a temperatura do terceiro sensor: "))
tempm = (t1+t2+t3)/3

print (f"A temperatura media registrada foi: {tempm}")
