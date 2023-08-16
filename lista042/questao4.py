'''
4.	Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso) correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o número inserido não corresponder à um dia da semana.
'''

dia = int(input("Me informe um número de 1 a 7: "))

if (dia >= 1 and dia <= 7):
    if (dia == 1):
        print(f"O número {dia} corresponde à Domingo.")
    if (dia == 2):
        print(f"O número {dia} corresponde à Segunda-feira.")
    if (dia == 3):
        print(f"O número {dia} corresponde à Terça-feira.")
    if (dia == 4):
        print(f"O número {dia} corresponde à Quarta-feira.")
    if (dia == 5):
        print(f"O número {dia} corresponde à Quinta-feira.")
    if (dia == 6):
        print(f"O número {dia} corresponde à Sexta-feira.")
    if (dia == 7):
        print(f"O número {dia} corresponde à Sábado.")
else:
    print("O número inserido não corresponde à um dia da semana.")

print("FIM DO PROGRAMA")