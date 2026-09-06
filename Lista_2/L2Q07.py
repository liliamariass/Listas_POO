notas = [1.7, 2.4, 3.7, 4.8, 5.2, 6.3, 7.1, 8.5, 9.6, 10]
try:
    media = sum (notas)/len(notas)
    print (f"A media das notas e: {media}")
except ZeroDivisionError:
    print ("A lista esta vazia!")