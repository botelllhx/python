# • Crie um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input("Em qual turno você estuda?: "))
turno = turno.lower()
match (turno):
    case "matutino":
        print("Bom dia!")
    case "vespertino":
        print("Boa tarde!")
    case "noturno":
        print("Boa noite!")