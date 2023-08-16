'''
6.	Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela: “Dados inseridos estão incorretos”.
'''

id = int(input("Qual ano você nasceu? "))
at = int(input("Em que ano você está? "))

if (id < at):
    print(f"Ah, então você tem {at - id} anos de idade.")
else:
    print("Dados inseridos estão incorretos.")
print("Fim do programa.")