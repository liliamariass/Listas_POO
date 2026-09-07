print("Análise do crescimento da quantidade de combinações possíveis do algoritmo de processamento ")
opcoes= int(input( "Digite a quantidade de opções disponíveis: "))
etapas = int (input("Digite a quantidade de etapas do algoritmo: "))

comb = opcoes ** etapas
print (f"O numero de combinacoes: {comb:.0f}")