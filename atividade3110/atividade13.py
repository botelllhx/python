# Crie um programa que leia um conjunto de nomes de 20 estudantes
# inscritos na prova do ENEM. Com esses nomes, realizar uma
# ordenação crescente usando uma função para facilitar a localização
# do nome na lista que será afixada no quadro de avisos da escola.

print("Lista de inscritos no ENEM")

lista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(20):
    lista[i] = str(input("Digite o nome de inscrição: "))

def OrdenacaoCrescente():
    lista.sort()
    print(lista)

OrdenacaoCrescente()