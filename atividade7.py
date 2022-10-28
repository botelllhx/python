# Crie um programa para realizar as operações de uma tabuada de multiplicação, onde será solicitado ao usuário digitar qual
# numero será a tabuada e qual intervalo do inicio e fim da tabuada, e exibir na tela o resultado conforme intervalo.

num = int(input("Digite um numero inteiro para a tabuada: "))
inicio = int(input("Digite onde a tabuada se inicia: "))
final = int(input("Digite onde a tabuada finaliza: "))
for i in range (inicio, final+1):
    print("O resultado é:", (num)*(i))