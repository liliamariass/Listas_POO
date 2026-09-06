
print("Sistema de coleta dos valores do experimento")
s1 = float (input("Digite a mediçao do sensor 1: "))
s2 = float (input("Digite a mediçao do sensor 2: "))
s3 = float (input("Digite a mediçao do sensor 3: "))
s4 = float (input("Digite a mediçao do sensor 4: "))
s5 = float (input("Digite a mediçao do sensor 5: "))

somav = 0
contadorv = 0

if 0<s1<1000:
    somav+=s1
    contadorv+=1
if 0<s2<1000:
    somav+=s2
    contadorv+=1
if 0<s3<1000:
    somav+=s3
    contadorv+=1
if 0<s4<1000:
    somav+=s4
    contadorv+=1
if 0<s5<1000:
    somav+=s5
    contadorv+=1

if contadorv>0:
    media=somav/contadorv
    print(f"A media das medicoes validas é: {media}")
else:
    print("Nenhuma das mediçoes foi valida!")