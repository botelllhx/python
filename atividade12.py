# Faça um Programa que leia em um vetor de 10 caracteres (letras) e diga quantas consoantes foram lidas.
# Mostre as consoantes.

vetor = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    vetor [i] = str(input("Preencha o vetor com 10 letras (A,Z): "))

contador = 0

for i in (vetor):
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        contador += 1
        print(i)
print("A quantidade de consoantes é: ", contador)
