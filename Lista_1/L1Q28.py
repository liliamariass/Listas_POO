
print("Saiba em qual regiao do plano cartesiano um ponto esta localizado")
x= float (input("Qual o valor do eixo das abcissas? (x): "))
y= float (input("Qual o valor do eixo das ordenadas? (y): "))
if x>0 and y>0:
    print (f" o ponto ({x:.0f},{y:.0f}) esta localizado no primeiro Quadrante")
elif x<0 and y>0:
    print (f" o ponto ({x:.0f},{y:.0f}) esta localizado no segundo Quadrante")
elif x<0 and y<0:
    print (f" o ponto ({x:.0f},{y:.0f}) esta localizado no terceiro Quadrante")
elif x>0 and y<0:
    print (f" o ponto ({x},{y}) esta localizado no quarto Quadrante")
elif x==0 and y!=0:
    print (f" o ponto ({x},{y}) esta localizado no eixo das ordenadas")
elif y==0 and x!=0:
    print (f" o ponto ({x},{y}) esta localizado no eixo das abcissas")
else:
    print (f" o ponto ({x},{y}) esta localizado na origem")