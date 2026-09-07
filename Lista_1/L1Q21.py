print ("Sistema de monitoramento da variacao de temperatura")
tempe= float (input("qual a temperatura esperada? "))
tempr= float (input ("Qual a temperatura regustrada? "))
variacao =abs (tempe-tempr)

print(f"a temperatura esperada foi de {tempe}° e a temperatura registrada foi de {tempr}°.Portanto, a variacao foi de {variacao}°")
