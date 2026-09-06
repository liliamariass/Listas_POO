inventariolab = {}
inventariolab[1] = {
    "equipamento": "Notebook",
    "Marca": "Acer",
    "Situacao": "Funcionando"
}
        
inventariolab[2] = {
    "equipamento": "Imprenssora",
    "Marca": "HP",
    "Situacao": "Em manutencao"
}

inventariolab[3] = {
    "equipamento": "Monitor",
    "Marca": "Lenovo",
    "Situacao": "Funcionando"
}

inventariolab[4] = {
    "equipamento": "Projetor",
    "Marca": "Epson",
    "Situacao": "Em manutencao"
}


print("Inventario do Laboratorio:\n")

for patrimonio, dados in inventariolab.items():
    print(f"Patrimonio: {patrimonio}")
    print(f"Equipamento: {dados['equipamento']}")
    print(f"Marca: {dados['Marca']}")
    print(f"Situacao: {dados['Situacao']}\n")
    

