par=0
soma=0
for i in range(1,21):
    num=i%2
    if num ==0:
        par+=1
        soma+=i
media = soma/par
print(f"A media dos identificadores pares é: {media:.0f}")