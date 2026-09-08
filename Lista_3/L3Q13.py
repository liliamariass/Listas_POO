
r=0
while r < 2:
    temp = float(input("\nDigite a temperatura: "))
    atual = input("Esta em qual escala? ")
    conv = input ("Deseja converter para qual? ")
    if atual == "Celsius" and conv =="Fahrenheit":
        convCF = (temp*1.8)+32
        print(f"{temp}° {atual} = {convCF}° {conv} ")
    
    elif atual == "Celsius" and conv == "Kelvin":
        convCK = temp + 273.15
        print(f"{temp}° {atual} = {convCK}° {conv} ")
    
    elif atual == "Fahrenheit" and conv == "Celsius":
        convFC = (temp-32)/1.8
        print(f"{temp}° {atual} = {convFC}° {conv} ")
    
    elif atual == "Fahrenheit" and conv == "Kelvin":
        convFK = ((temp-32)/1.8)+273.15
        print(f"{temp}° {atual} = {convFK}° {conv} ")
    
    elif atual == "Kelvin" and conv == "Celsius":
        convKC = temp-273.15
        print(f"{temp}° {atual} = {convKC}° {conv} ")
    
    elif atual == "Kelvin" and conv == "Fahrenheit":
        convKF = ((temp-273.15)*1.8)+32
        print(f"{temp}° {atual} = {convKF}° {conv} ")
    
    r = int (input("Digite 1 se deseja fazer nova conversão: "))
    if r!=1:
        print("Programa encerrado.")