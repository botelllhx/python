m = [[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]

mensagem = False

for a in range(5):
    for j in range(5):
        m[a][j] = int(input("Preencha a matriz: "))

num = int(input("Digite um numero: "))

for a in range(5):
    for j in range(5):
        if m[a][j] == num:
            mensagem = True


if mensagem == False:
    print("Não encontrado")
else :
    print("Número encontrado é: ", m[a][j])