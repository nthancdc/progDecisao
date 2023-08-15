'''
6)	Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o maior valor e o menor valor lido.
'''

num1 = int(input("Me diga o primeiro número: "))
num2 = int(input("Me diga o segundo número: "))
dif1 = num1 - num2
dif2 = num2 - num1

if (num1 > num2):
    print(f"A diferença dos seus números é: {dif1}.")
else:
    print(f"A diferença dos seus números é: {dif2}.")