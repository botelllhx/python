# Crie um programa de calculadora que realiza as operações de soma, multiplicação, divisão e subtração
# será perguntado ao usuário se deseja continuar com o uso da calculadora.
# enquanto ele digitar (“S” – Sim) o programa irá reiniciar a calculadora.
print("Calculadora")
resposta = "s"
while resposta == "s":

    operacao = str(input("Qual operação gostaria de efetuar?(soma, subtracao, divisao ou multiplicacao): "))
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2

    if  operacao == "soma":
        print("O resultado é: ", soma)
    elif operacao == "subtracao":
        print("O resultado é: ", subtracao)
    elif operacao == "multiplicacao":
        print("O resultado é: ", multiplicacao)
    elif operacao == "divisao":
        print("O resultado é: ", divisao)
    else:
        print("Confira os dados digitados!")


    resposta = str(input("Gostaria de continuar usando a calculadora?(s ou n): "))

