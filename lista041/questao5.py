'''
5)	Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor da média obtida pelo aluno.
'''

media1 = float(input("Me diga sua nota do primeiro bimestre: "))
media2 = float(input("Me diga sua nota do segundo bimestre: "))
media3 = float(input("Me diga sua nota do terceiro bimestre: "))
media4 = float(input("Me diga sua nota do quarto bimestre: "))

media = (media1 + media2 + media3 + media4) / 4

if (media >= 5):
    print(f"Sua média do ano foi: {media}. Parabéns, você foi aprovado!")
else:
    print(f"Sua média do ano foi: {media}. Meus pêsames, você foi reprovado.")