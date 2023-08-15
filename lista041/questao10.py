'''
10)	Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo número informado é ou não um divisor do primeiro número informado.
'''

num1 = int(input("Me diga o primeiro número: "))
num2 = int(input("Me diga o segundo número: "))

if (num1 % num2 == 0):
    print(f"{num2} é divisor de {num1}.")
else:
    print(f"{num2} não é divisor de {num1}.")