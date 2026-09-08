l5s = ["Calculadora", "Calendario", "Relogio", "Bloco de Notas", "Paint"]
print("Lista inicial:")
print(l5s)

del l5s[1]
ns = input ("Digite o nome do novo software: ")
l5s.append(ns)

print ("Lista apos as alteracoes:")
print(l5s)