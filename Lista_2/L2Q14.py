frase = input("Digite uma frase: ")
palavras = frase.split()
vezes = {}
for palavra in palavras:
    if palavra in vezes:
        vezes[palavra]+=1
    else:
        vezes[palavra]=1
for palavra, quantidade in vezes .items():
    print (f"{palavra}: {quantidade}")