agenda = {



}
for n in range (3):
    nome=input("Digite o nome do contato que deseja adcionar:")
    telefone= int(input("Digite o telefone: "))
    agenda[nome]=telefone

nomed=input("Digite o nome do contato que deseja pesquisar:")

if nomed in agenda:
    print (f"Contato:{nomed}\nTelefone:{agenda[nomed]} ")
else:
    print("Contato não encontrado.")