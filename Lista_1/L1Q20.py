print ("Verificacao para entrar na area restrita")
nome = input("qual o seu nome?")
nasc = int (input (f" {nome}, digite o ano do seu nascimento"))
idade=2026-nasc
if idade<18:
    print(f"{nome}, voce tem {idade} anos. precisa entrar com um acompanhate")
else:
    print(f"{nome}, voce tem {idade} anos. pode entrar normalmente")