print("Registro do tempo total de execução da rotina de processamento\n")
tempoh = int (input("Digite o numero de horas de execução: "))
tempom = int (input("Digite o numero de minutos: "))

tempohm = tempoh * 60
tempohsomam = tempohm+tempom
tempos = tempohsomam *60

print(f"o tempo total da execucao da rotina de processamento em segundos é: {tempos}")
