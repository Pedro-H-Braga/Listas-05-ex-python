'''
Dados dois números inteiros positivos, determinar o máximo 
divisor comum entre eles usando o algoritmo de Euclides

1 var auxiliar, 2 entradas, se entradas < 0 exiba(error), se a < b exiba(error):

pegar resto de a por b > dividir b pelo resto até ser igual a 0
'''

#a = int(input('Informe o primeiro numero: '))
#b = int(input('Informe o segundo numero: '))
a = 1500
b = 155

auxiliar = 0
for b in range(True):
#while b != 0:  
    if b == 0:
        print(f'O MDC pelo algoritmo de euclides é: {a}')
        break
    else: 
        print(f'O MDC pelo algoritmo de euclides é: {a}')
   
    auxiliar = b
    print(auxiliar)
    b = a % b
    print(b)
    a = auxiliar
    print(a)

    '''
        #break
    '''