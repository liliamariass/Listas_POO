nota = 0
notas = [1.7, 2.4, 3.7, 4.8, 5.2, 6.3, 7.1, 8.5, 9.6, 10]
aprovado=0

for nota in notas:
    if nota>=7:
        aprovado+=1
print (f"foram aprovados {aprovado} estudantes. ")
