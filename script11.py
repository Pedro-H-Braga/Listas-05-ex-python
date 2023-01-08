'''
Dados dois números inteiros positivos, determinar o máximo 
divisor comum entre eles usando o algoritmo de Euclides

1 var auxiliar, 2 entradas, se entradas < 0 exiba(error), se a < b exiba(error):

pegar resto de a por b > dividir b pelo resto até ser igual a 0
'''

#a = int(input('Informe o primeiro numero: '))
#b = int(input('Informe o segundo numero: '))
a = 1135
b = 120

auxiliar = 0
for a in range(True):
#while b != 0:  
    # auxiliar  b
    if auxiliar > 0:
        auxiliar = b
        b = a % b
        a = auxiliar
        print(f'O MDC pelo algoritmo de euclides é: {a}')
    else: break