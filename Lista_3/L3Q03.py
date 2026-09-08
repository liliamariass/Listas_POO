print("Sistema de manutencao da rede do laboratorio\n")
lm=0
ls=0
latencia=0
maiorl=0
soma=0
for i in range(10):
    latencia = float(input("Digite o tempo de resposta do teste:"))
    if latencia<=100:
        lm+=1
    else:
        ls+=1
    soma = soma+latencia
    if latencia>maiorl:
        maiorl = latencia
   
print(f"\nTestes com a latencia menor que 100ms: {lm}")
print(f"Teste com a latencia superior a 100ms: {ls}")
medial= soma/10
print(f"Media das latencias registradas: {medial}")
print(f"Maior Latencia registrada: {maiorl}")