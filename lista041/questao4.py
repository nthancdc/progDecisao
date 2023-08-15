'''
4)	Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por 4 e 5”.
'''

num = int(input("Me informe um número: "))

if (num % 4 == 0 and num % 5 == 0):
    print(num)
else:
    print("Seu número não é divisivel por 4 e nem por 5")