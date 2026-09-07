
print("Sistema de notas da disciplina x")
nota1= float(input("Digite a nota da primeira avaliacao: "))
nota2= float(input("Digite a nota da segunda avaliacao: "))
media = (nota1+nota2)/2
if media >= 6.0:
    print (f"Media final: {media} Aluno aprovado")
else:
    print (f"Media final: {media}. Aluno reprovado")