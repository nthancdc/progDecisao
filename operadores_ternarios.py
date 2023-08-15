'''
Crie um programa que pergunte a idade do usuário e em seguida informe se este usuário é menor ou maior de idade.
'''

idade = int(input("Qual é a sua idade? "))
resposta = ("Você é menor de idade.", "Você é maior de idade!") [idade >= 18]

print(resposta)