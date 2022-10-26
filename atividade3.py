# Programa para receber dois números á serem calculados em todas as operações matematicas
# Incluir resto da divisão e potência.

print("Calcule dois números!")

n1 = input ("Escreva o primeiro numero:")
n2 = input ("Escreva o segundo numero:")

soma = (int(n1)+int(n2))
print ("O valor do primeiro número somado pelo segundo número é:",int(soma))

subtracao = (int(n1)-int(n2))
print ("O valor do primeiro número subtraído pelo segundo número é:", int(subtracao))

multiplacao = (int(n1)*int(n2))
print ("O valor do primeiro número multiplacado pelo segundo número é:", int (multiplacao))

divisao = (int(n1)/int(n2))
print ("O valor do primeiro número dividido pelo segundo número é:", int (divisao))

exponenciacao = (int(n1)**int(n2))
print ("O valor da exponeciação é:", int (exponenciacao))

resto = (int(n1)%int(n2))
print ("O valor do resto da divisão é:", int (resto))