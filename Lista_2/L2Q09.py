notas = []

for n in range (0,5):
    try:
        x=float (input("Digite a nota:"))
        notas.append(x)
    except ValueError:
            print("Entrada inválida! ")
    
media = sum(notas)/len(notas)
    
print(f"Todas as notas: {notas}")
print(f"Media das notas: {media}")
print(f"A maior nota foi: {max(notas)}")
print (f"A menor nota foi: {min(notas)}")