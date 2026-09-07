print("Sistema de estacionamento da empresa Xyz")
placa = int (input("Digite o numero da placa: "))

placaip = placa%2

if placaip==0:
    print ("Por favor, utilize o portao A")
else:
    print ("Por favor. utilize o portao B")