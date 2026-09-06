print("Saiba qual foi o servidor com melhor desempenho. ")
s1 = float (input( "Digite o tempo de resposta do Servidor 1: "))
s2 = float (input( "Digite o tempo de resposta do Servidor 2: "))
s3 = float (input( "Digite o tempo de resposta do Servidor 3: "))
s4 = float (input( "Digite o tempo de resposta Servidor 4: "))

if s1 < s2 and s1 < s3 and  s1 <s4:
    print ("O servidor com melhor desempenho foi o Servidor 1")
elif s2 < s1 and s2 < s3 and s2<s4:
    print ("O servidor com melhor desempenho foi o Servidor 2")
elif s3< s1 and s3 < s2 and s3<s4:
    print ("O servidor com melhor desempenho foi o Servidor 3")
else:
    print ("O servidor com melhor desempenho foi o Servidor 4")
