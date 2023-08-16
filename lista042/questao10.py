'''
10.	Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições devem seguir as regras da tabela abaixo:
'''

n = input("Qual é seu nome? ")
n1 = float(input("Qual foi a sua nota da primeira prova? "))
n2 = float(input("Qual foi a sua nota da segunda prova? "))

if ((n1 + n2) / 2 >= 3.0 and (n1 + n2) / 2 <= 6.9):
    print(f"{n}, você está em prova final.")
elif ((n1 + n2) / 2 >= 7.0):
    print(f"{n}, você foi aprovado.")
else:
    print(f"{n}, você foi reprovado.")