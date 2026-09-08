notas={
"Lilia": 10,
"Maria": 9,    
"Ana": 7,    
"Maya": 5,
"Lara": 3,    
}
for aluno, nota in notas.items():
    print(f"Aluno: {aluno}") 
    print(f"Nota: {nota}")
    if nota>=7.0:
        print (f"Situação: aprovado\n")
    else:
        print ("Situacao: reprovado\n")


