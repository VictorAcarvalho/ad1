from curses.ascii import isdigit
from inspect import isdatadescriptor


print("="*100)
print("Bem vindo ao programa de potenciação")
base= input("Digite um valor como base: ")
exponent= input("Digite um valor como expoente: ") 


  

def main( base , exponent):
    calc= 0
    if isdigit(base) == False and isdigit(exponent) == False:
        return print("Base {} e expoente {}, não estão no formato adequado".format(base,exponent))
    else:
        if isdigit(base) == False:
            return print("A base {} não está no formato devido".format(base))
        if isdigit(exponent) == False:
            return print("Expoente {} não está no devido formato".format(exponent))

    calc= int(base)**int(exponent)       
    return print("{} elevado a {}, é igual a {}".format(base,exponent,calc))


main(base,exponent)