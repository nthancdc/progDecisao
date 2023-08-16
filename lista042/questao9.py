'''
9.	Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de idade, se é maior de idade, ou se é maior de 65 anos.
'''

id = int(input("Quantos anos você tem? "))

if (id >= 18 and id <= 65):
    print("Você é maior de idade.")
if (id > 65):
    print("Você tem mais de que 65 anos.")
if (id < 18):
    print("Você é menor de idade.")