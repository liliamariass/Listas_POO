menor= None
for i in range (10):
    lat=float(input("Digite a medicao de latencia: "))
    if menor is None or lat<menor:
        menor=lat
print(f"a menor medicao foi: {menor}")