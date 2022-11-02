#Faça um programa para imprimir igual abaixo:
#1
#2 2
#3 3 3 ...
#n n n n ...
#“n” para um ”numero” (range) informado pelo usuário.
# Use uma função que receba um valor n inteiro e imprima até a
#“n-Linha” informada pelo usuário.

num = int(input("Digite um numero: "))

for i in range(1, num+1):
    for j in range(1, i+1):
        print (i, end="")
    num = num + 1
    print ("\r")
