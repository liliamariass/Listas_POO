notas = []
soma = 0
contador = 0
maior = 0
menor = 1

for i in range (5):
    try:
        n=float (input("Digite a nota: "))
        notas.append(n)
    except ValueError:
            print("Entrada inválida! ")
for nota in notas:
    soma+=nota
    contador+=1
    if nota>maior:
        maior = nota
    if menor<nota:
        menor = nota
media = soma/contador

print(f"Todas as notas: {notas}")
print(f"Media das notas: {media}")
print(f"A maior nota foi: {maior}")
print (f"A menor nota foi: {min(notas)}")