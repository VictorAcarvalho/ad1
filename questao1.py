from __future__ import division


print("Bem vindo ao programa de soma entre números e suas médias")
values= []
division = 0
sum = 0.0
enterNumbers = input("Digite um valor: ")
if enterNumbers == "" or 0:
    print("Nenhuma linha lida com conteúdo, portanto não há soma nem média!")
else:
    while enterNumbers != "":    
        values.append(float(enterNumbers))
        enterNumbers=input("Digite um valor: ")

    for i in values:
        sum = sum + i

    division = sum / len(values)
    print("Soma dos números: ",sum)
    print("Média dos números: ",division)