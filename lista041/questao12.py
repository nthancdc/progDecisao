'''
12)	Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número.
'''

n1 = int(input("Me fale o primeiro número: "))
n2 = int(input("Me fale o segundo número: "))
n3 = int(input("Me fale o terceiro número: "))
n4 = int(input("Me fale o quarto número: "))
n5 = int(input("Me fale o quinto número: "))

maior = n1
menor = n1

if (maior < n2):
    maior = n2
if (maior < n3):
    maior = n3
if (maior < n4):
    maior = n4
if (maior < n5):
    maior = n5

if (menor > n2):
    menor = n2
if (menor > n3):
    menor = n3
if (menor > n4):
    menor = n4
if (menor > n5):
    menor = n5

print(f"O maior número que você me informou foi o: {maior} e o menor número foi o: {menor}.")