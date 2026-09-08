equipamentos = {}
maior = 0
nomem = " "
for i in range (5):
    nome = input("Digite o nome do equipamento: ")
    valor = float (input("Digite o valor: "))
    print("\n")
    equipamentos[nome]=valor
for nome in equipamentos:
    preco = equipamentos[nome]
    if preco > maior:
        nomem = nome
print(f"Equipamentos:\n{equipamentos}")
print(f"\nO equipamento mais caro foi: {nomem}")
