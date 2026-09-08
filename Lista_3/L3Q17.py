vogais = 0
consoante =0

for i in range (10):
    letra = input ("Digite uma letra: ")
    if letra == "A" or letra == "a" or letra == "E" or letra == "e" or letra == "I" or letra == "i" or letra == "O" or letra == "o" or letra == "U" or letra == "u":
        vogais+=1
    else:
        consoante+=1
print(f"Quantidade de vogais: {vogais}\nQuantidade de consoantes: {consoante}")
