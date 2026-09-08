estudantes={
"Joao": {
    "nota1": 8.0,
    "nota2": 7.5
    },
"Sophia": {
    "nota1": 9.4,
    "nota2": 6.8
    },
"Daniela": {
    "nota1": 5.9,
    "nota2": 4.3
    }
}

for estudante, notas in estudantes.items():
    media = (notas['nota1']+notas['nota2'])/2
    notas["media"] = media
    situacao = "aprovado" if media >= 7.0 else "reprovado"
    print(f"Aluno: {estudante}")
    print(f"Nota 1: {notas['nota1']}")
    print(f"Nota 2: {notas['nota2']}")
    print(f"Média: {notas['media']:.2f}")
    print(f"Situação: {situacao}\n")