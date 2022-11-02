ganho = float (input("Quanto você ganha por horas trabalhadas?: "))
ht = float (input ("Qual é o numero de horas que você trabalha por mês?: "))
result = ganho * ht
print ("O salario bruto é R$", result, "/mês.")

impostorenda = result * 0.11
print("O valor descontado do imposto de renda é: ", impostorenda)
inss = result * 0.08
print("O valor descontado do INSS é: ", inss)
sindicato = result * 0.05
print("O valor descontado do sindicato é: ", sindicato)

total = result - (impostorenda+inss+sindicato)
print("O meu salario é R$ ", total)