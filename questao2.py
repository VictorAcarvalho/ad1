print("="*100)
print("Bem vindo ao programa de indentificação de maior e menor número")


def maxAndMinimalElements(number):
    return print("Menor número: {} , maior número: {}".format(min(number),max(number)))


def main():
    index= 1
    values= []
    lines = int(input("Digite o número de linhas que deseja escrever: "))
    if lines =="" or 0:
        return print("Nenhuma linha lida com conteúdo, portanto não há soma nem média!")
    while index <= lines:
        number = input("digite um número: ")
        while number != '':
            values.append(int(number))
            number = input("digite um número: ")
        index= index+1
        print("\n")
    return(maxAndMinimalElements(values))


main()