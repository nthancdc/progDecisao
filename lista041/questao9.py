'''
9)	Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou nulo.
'''

num = int(input("Me informe um número: "))

if (num >= 1):
    print("O seu número é positivo.")
elif (num < 0):
    print("O seu número é negativo.")
else:
    print("O seu número é nulo")