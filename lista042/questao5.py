'''
5.	Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final, informe na tela se o estado inserido está ou não na região Sudeste
'''

sigla = input("Me diga uma sigla de um estado Brasileiro: ")

if (sigla == "RJ" or sigla == "SP" or sigla == "MG" or sigla == "ES"):
    print(f"O estado {sigla} corresponde à um estado da região Sudeste.")
else:
    print(f"O estado {sigla} NÃO corresponde à um estado da região Sudeste")
print("FIM DO PROGRAMA.")