'''
) Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem crescente.
'''

v1 = int(input("Dê um número a variável A: "))
v2 = int(input("Dê um número a variável B: "))
v3 = int(input("Dê um número a variável C: "))

# A tem que ser menor que B
if (v1 > v2):
    auxiliar = v1
    v1 = v2
    v2 = auxiliar
# garantido até aqui que entre A e B, o menor está em A

# A tem que ser menor que B
if (v1 > v3):
    auxiliar = v1
    v1 = v3
    v3 = auxiliar
# garantido até aqui que entre A é o menor dos 3

# agora é necessário garantir que B seja menor que C
if (v2 > v3):
    auxiliar = v2
    v2 = v3
    v3 = auxiliar
# garantido até aqui que entre B e C, o B é o menor, ou seja, o C é o maior de todos
print(f"A ordem crescente dos seus números é: {v1}, {v2} e {v3}")