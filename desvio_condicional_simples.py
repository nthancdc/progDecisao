'''
Crie um programa que pergunte dois números ao usuário.
Em seguida o programa deverá somar os dois números e apresentar o resultado se o valor for maior que 10
'''

num1 = int(input("Me fale o número 1:"))
num2 = int(input("Me fale o número 2:"))
soma = num1 + num2

if (soma >= 10):
 print(f"A soma destes números é: {soma}")

print("Fim do programa.")