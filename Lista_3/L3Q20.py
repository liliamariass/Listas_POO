medicoes = []
soma=0
for i in range(5):
    medicao = float(input("Digite a quantidade de memoria utilizada no teste: "))
    medicoes.append(medicao)
for medicao in medicoes:
    soma+=medicao
print(f"A soma dos valores registrados é: {soma}")
    