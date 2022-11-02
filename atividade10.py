p1 = float ( input ( "Digite a nota total da prova primeiro bimestre (Valor maximo de 25 pts):"))
t1 = float ( input ( "Digite a nota total do trabalho do primeiro bimestre (Valor maximo de 25 pts):" ))
p2 = float ( input ( "Digite a nota total da prova do segundo bimestre (Valor maximo de 25 pts):"))
t2 = float ( input ( "Digite a nota total do trabalho do segundo bimestre (Valor maximo de 25 pts):" ))
p3 = float ( input ( "Digite a nota total da prova do terceiro (Valor maximo de 25 pts):"))
t3 = float ( input ( "Digite a nota total do trabalho do terceiro bimestre (Valor maximo de 25 pts):" ))
p4 = float ( input ( "Digite a nota total da prova do terceiro bimestre (Valor maximo de 25 pts):"))
t4 = float ( input ( "Digite a nota total do trabalho do qaurto bimestre (Valor maximo de 25 pts):" ))

media1 = ((p1 + t1) / 2)
print("Sua media foi:", media1)
media2= ((p2 + t2) / 2)
print("Sua media foi:", media2)
media3= ((p3 + t3) / 2)
print("Sua media foi:", media3)
media4= ((p4 + t4) / 2)
print("Sua media foi:", media4)

totalp= p1 + p2 + p3 + p4
print("O total da prova foi:", totalp)

totalt= t1 +t2 + t3+ t4
print("O total do trabalho foi:",totalt)

totalanual= totalp + totalt
if totalanual <= 59:
    print("Você foi reprovado!")
elif totalanual >= 60:
    print("Você foi aprovado!")
elif totalanual >=40 and 60:
    print("Você esta de recuperação!")
else:
    print("Valor invalid")