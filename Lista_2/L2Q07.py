print("Media das notas armazenadas ")
soma = 0
contador = 0
notas = [1.7, 2.4, 3.7, 4.8, 5.2, 6.3, 7.1, 8.5, 9.6, 10]
for nota in notas:
    soma+=nota
    contador+=1
try:
    media = soma/contador
    print (f"A media das notas e: {media:.2f}")
except ZeroDivisionError:
    print ("A lista esta vazia!")