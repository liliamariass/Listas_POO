
print("Saiba se os arquivos da instituicao podem ser distribuidos igualmente em lotes de 3 arquivos")
arquivos = 5776
lotes = 5776%3

if lotes==0:
    print("Os arquivos podem ser distribuidos")
else:
    print("Os arquivos nao podem ser distribuidos")