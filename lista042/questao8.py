'''
8.	Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números inseridos. O valor da variável maior deverá ser exibido ao final.
'''

num1 = int(input("Me diga um número: "))
num2 = int(input("Me diga um outro número: "))
num3 = int(input("Me diga um útimo número: "))

if (num2 < num1 and num3 < num1):
    maior = num1
if (num1 < num2 and num3 < num2):
    maior = num2
if (num2 < num3 and num1 < num3):
    maior = num3
print(f"O maior dentre os três números é o: {maior}.")