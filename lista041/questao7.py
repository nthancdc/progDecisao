'''
7)	Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo deste valor, ou seja, o número lido como sendo positivo
'''

num = int(input("Me informe um número: "))
mn = num * -1

if (num < 0):
    print(f"O módulo do seu número é: {mn}.")
if (num >= 0):
    print(f"O módulo do seu número é: {num}.")