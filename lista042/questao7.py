'''
7.	Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é o menor, ou ainda, se ambos são iguais.
'''

num1 = int(input("Me diga um número: "))
num2 = int(input("Me diga um outro número: "))

if (num1 > num2):
    print(f"O número {num1} é maior que o número {num2}.")
elif (num2 > num1):
        print(f"O número {num2} é maior que o número {num1}.")
else:
    print("Os números informados são iguais.")
print("FIM DO PROGRAMA.")