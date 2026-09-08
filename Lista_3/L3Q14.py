num = int(input("Digite o numero que deseja saber o fatorial: "))
fator=1
nv=num+1
for i in range(1,nv):
    fator=fator*i
print(f"{num}! = {fator}")