'''
11)	Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado somente o algarismo das centenas.
'''

num = int(input("Me informe um número de três algarismos: "))

if (num >=100 and num <= 999):
    print(f"O algarismo das centenas do seu número é: {num // 100}.")
else:
    print("Você não me disse um número de 3 algarismos.")
print("FIM DO PROGRAMA.")
