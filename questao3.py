print("="*100)
print("Bem vindo ao programa verificador de frases")

def 

def main():
    print("Digite as linhas abaixo")
    phrases =[]
    line=input()  
    if line =='':
        return print("Nenhuma linha não vazia foi lida!!")
    while line != "":
        phrases.append(line)
        line=input()
    return phrases

main()