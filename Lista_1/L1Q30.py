
print("Sistemas de resultado final")
nota = float(input("informe sua nota final"))
if 10 >=nota >=7.0:
    print (f" nota final {nota}. Estudante aprovado!")
elif 5.0<=nota<=6.9:
    print(f" nota final {nota}. Estudante em recuperacao!")
elif nota<5.0:
    print(f"nota final {nota}. Estudante reprvado!")
else:
    print (" valor de nota invalida!")
    