# Crie um programa que receba 5 produtos em variáveis constantes
# O usuário deverá informar a quantidade de cada produto.

print("Loja do Botelho!")

# Valor dos produtos
iphone = 2980
samsung = 2540
tablet = 1950
ps5 = 2100
notebook = 2350

# Quantidade dos produtos
print("O valor do iphone é de R$ ", iphone)
qntiphone = int(input("Quantos iphones você gostaria de comprar?: "))
print("O valor do samsung é de R$ ", samsung)
qntsamsung = int(input("Quantos samsungs você gostaria de comprar?: "))
print("O valor do tablet é de R$ ", tablet)
qnttablet = int(input("Quantos tablets você gostaria de comprar?: "))
print("O valor do ps5 é de R$ ", ps5)
qntps5 = int(input("Quantos ps5 você gostaria de comprar?: "))
print("O valor do notebook é de R$ ", notebook)
qntnotebook = int(input("Quantos notebooks você gostaria de comprar?: "))

# Total dos produtos
total = (qntiphone*iphone)+(qntsamsung*samsung)+(qnttablet*tablet)+(qntps5*ps5)+(qntnotebook*notebook)
print ("O valor total da compra é: R$ ", total)

# Parcelamento
parcela3 = round(total / 3, 2)
print ("O valor total parcelado em 3x é: R$ ", float(parcela3))
parcela6 = round ((total*1.05)/6, 2)
print ("O valor total parcelado em 6x é: R$ ", float(parcela6))

# Desconto
desconto10 = round(total-(total*0.10),2)
print ("O valor total á vista com desconto é: R$ ", float(desconto10))

print ("Volte sempre! :)")