print("Sistema de monitoração de satélite")
tempoth = int (input("Digite em horas, o tempo de deslocamento da terra"))
#30km/s=108.000km/m
#distancia = velocidade x tempo
velocidademh = 108.000
metrosh = (velocidademh * tempoth)*1000

print (f" Em {tempoth} horas, a distância total percorrida pela terra {metrosh:.0f} metros")