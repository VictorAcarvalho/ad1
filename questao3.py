
print("="*100)
print("Bem vindo ao programa verificador de frases")

def main():
    print("Digite as linhas abaixo")
    line=input()
    splitedLine = line.split(" ")
    palindromeList= []
    phrases =[]
    spplitedPhrases= [] 
    vowels ="AaEeIiOoUu"
    if line =='':
        return print("Nenhuma linha não vazia foi lida!!")
    while line != "":
        phrases.append(line)
        spplitedPhrases.append(splitedLine)
        line=input()
        splitedLine = line.split(" ") 
        for i in line:
            if i[::-1] == i:
                palindromeList.append(line)
    palindrome = palindromeList[0]
    mostAccentueLine=mostAccentue(phrases) 
    mostVowel = vowelsCount(mostAccentueLine , vowels)
    bigWord = biggestWord(spplitedPhrases)
    palindromeQuantity = palindromeCount(palindrome)
    print("A linha com mais vogais sem acento: {}".format(mostAccentueLine))
    print("Quantidade de vogais sem acento: {}".format(mostVowel))
    print("A maior palavra digita é :  {}".format(bigWord))
    print("Linha com mais Palíndromos: {}".format(palindrome))
    print("O número de palavras palíndromas:{}".format(palindromeQuantity))
    
    
def mostAccentue(phrasesList):
    mostAccentuesPhrase = (max(phrasesList, key=str.isascii)) 

    return mostAccentuesPhrase

def vowelsCount(phrase, vowels):
    phraseVowel = [each for each in phrase if each in vowels]
    return len(phraseVowel)


def biggestWord(lst):
    mergedList = []
    for i in lst:
        for j in i:
            mergedList.append(j)
    resulted = max(mergedList,key=len) 
    return resulted

def palindromeCount(string:str):
    splited = len(string.split(" "))-1
    return splited
main()

