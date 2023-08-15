'''
3)	Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou é ímpar.
'''

num = int(input("Me diga um número: "))
resto = num %2

if (resto == 0):
    print("Seu número é par!")
else:
    print("Seu número é ímpar!")
print("FIM DO PROGRAMA!!")