disciplina={
"nome": "Programacao Orientada a Objetos",
"professor": "Mario Aparecido",    
"carga_horaria": "80h",    
"periodo": "3°",    
}
chave = input ("Digite o nome da chave: ")
try:
    chaved=disciplina[chave]
    print ("A chave existe")
except KeyError:
    print("A chave nao foi encontrada")
