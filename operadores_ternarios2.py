'''
Crie um programa que pergunte a idade do usuário e em seguida informe se este usuário é menor ou maior de idade.
'''

idade = int(input("Qual é a sua idade? "))
resposta = "Você é maior de idade!" if idade >= 18 else "Você é menor de idade."

print(resposta)