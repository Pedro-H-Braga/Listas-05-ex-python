''' 
Faça um programa que leia um número e imprima o seu fatorial.

𝑛! = 𝑛 ∗ (𝑛 − 1) ∗ (𝑛 − 2) ∗ … ∗ 1

𝐸𝑥𝑒𝑚𝑝𝑙𝑜:
6! = 6 ∗ 5 ∗ 4 ∗ 3 ∗ 2 ∗ 1
6! = 720

Lembrando ainda que:
0! = 1
'''

entrada = int(input("Informe um valor: "))
fatorial = 1
contador = 1

for contador in range(contador, entrada):
    contador += 1
    if entrada == 0:
        fatorial = 1
        break
    elif entrada < 0:
        print('não existe fatorial de numero negativo') 
    else:      
        fatorial *= contador

print(f"Fatorial de {entrada} e: {fatorial}")